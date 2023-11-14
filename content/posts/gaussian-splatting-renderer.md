---
title: 'Understanding 3D Gaussian Splats by writing a software renderer'
description: 'Writing a software renderer for 3D Gaussian Splats in Python and Rust'
date: 2023-11-13T19:10:35-08:00
draft: false
---

If you want to skip to the code, you can find it [here](https://github.com/thomasantony/splat/).

[3D gaussian splats](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) have been all the rage since they were published. They may end up revolutionizing how we model realistic 3D worlds and seems to be the successor to [NeRFs](https://docs.nerf.studio/).

Most of the articles that I have seen about them addresses the training-side of it (which is arguably more important). Hardly any addresses the nitty-gritty details on how to parse a pre-trained model and view it. While differentiable rendering is a key part of what makes this technology possible, the differentiable part is not really necessary if all you are interested in is viewing a pre-trained model.

There are a few indepndantly written renderers on github - most of them using OpenGL, and some using WebGPU or WebGL. Some of the Python versions require CUDA (and are hence tied to NVIDIA systems). There is also a [Rust version](https://github.com/Lichtso/splatter) that is pretty platform-agnostic.

However, even the [simplest](https://github.com/limacv/GaussianSplattingViewer) of these use shaders - pieces of code written a special languages that run on the GPU. The particular example I linked also depends on OpenGL 4.3 and hence does not run on macOS.

My goal with this project was to write a renderer in plain Rust, doing all the rendering math on the CPU. And after spinning my wheels for a bit, I realized that I need to start even simpler - with a version written in pure Python in a [Jupyter notebook].


## What are 3D gaussian splats?

3D Gaussian Splats are a method of encoding information from a scene such that we can synthesize "novel views", that were not in the original set of photos used to generate it. There are some very neat examples on the [official site](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) for the paper. There have been also been a few web-based viwers ([https://gsplat.tech/](https://gsplat.tech/), [https://poly.cam/gaussian-splatting](https://poly.cam/gaussian-splatting) ) that show off some really good examples.


## Results

As of the time of writing, I have a working CPU-based Gaussian splat renderer prototype written in Python and a faster one written in Rust. On my M1 Max Macbook Pro, the Python version takes about 2-3 minutes to render a 2560x1440 image for the "[push sledge](https://gsplat.tech/)" model ([download here](https://media.reshot.ai/models/plush_sledge/output.zip)) with about ~284000 gaussians in it. The Rust version renders the same model pretty much instantly.

## How it works

### Python version
While the CPU-based renderer does not use any OpenGL or WebGPU shaders, it still follows mostly the same logic. For the Python version, I had to add in some (not-so-efficient) versions of things that are typically handled by the graphics rendering pipeline on a GPU. Here is the overall workflow for the renderer in the [Jupyter notebook](https://github.com/thomasantony/splat/blob/master/notes/00_Gaussian_Projection.ipynb):

1. Load the gaussians from the .ply file. I used the [ply-rs](https://docs.rs/ply-rs/latest/ply_rs/) crate in the Rust version and the `load_plyfile` functions from [util_gau.py](https://github.com/limacv/GaussianSplattingViewer/blob/main/util_gau.py).
   ```python
    from tqdm import tqdm
    model = load_ply('point_cloud.ply')


    print('Loading gaussians ...')
    gaussian_objects = []
    for (pos, scale, rot, opacity, sh) in tqdm(zip(model.xyz, model.scale, model.rot, model.opacity, model.sh)):
        gaussian_objects.append(Gaussian(pos, scale, rot, opacity, sh))
   ```
2. Initialize a Camera model with a certain dimensions and position. I used one based off of the version at https://github.com/limacv/GaussianSplattingViewer/ .
   ```python
    (h, w) = (720, 1280)
    camera = Camera(h, w, position=(-0.57651054, 2.99040512, -0.03924271), target=(-0.0, 0.0, 0.0))
   ```
3. Sort the gaussians by depth from the camera model (this may need to be repeated if the camera can be moved).
   ```python
    print('Sorting the gaussians by depth')
    indices = np.argsort([gau.get_depth(camera) for gau in gaussian_objects])
   ```
4. [Project the 3D gaussians](https://xoft.tistory.com/49) on to the camera plane to form ellipses. Compute the parameters of this ellipse (which represents a 2D gaussian and is represted by a variable called `conic`). See the `get_cov2d()` and the `get_conic_and_bb()` methods in the [Jupyter notebook](https://github.com/thomasantony/splat/blob/master/notes/00_Gaussian_Projection.ipynb)

5. This step is a quirk of how graphics rendering pipelines work. We start with a list of four 3D vertices (called a "quad"). In a typical 3D rendering pipeline, these may be actual vertices from a 3D model. In our case, we make the quad cover the entire screen. This is represented by the vertices [-1, 1], [1, 1], [1, -1] and [-1, -1]. This is essentially a square centered at the origin. These are in something called "Normalized Device Coordinates" which is agnostic to the actual resolution of the camera model or the screen.
    ```python
        vertices = np.array([[-1, 1], [1, 1], [1, -1], [-1, -1]])
        # Four values (bounds of the values used to evaluate gaussian)
        bboxsize_cam = np.multiply(vertices, bboxsize_cam)

        view_matrix = camera.get_view_matrix()
        projection_matrix = camera.get_projection_matrix()

        position4 = np.append(self.pos, 1.0)
        g_pos_view = view_matrix @ position4
        g_pos_screen = projection_matrix @ g_pos_view
        g_pos_screen = g_pos_screen / g_pos_screen[3]

        # Bounds of gaussian in Normalized Device Coordinates (-1 to 1)
        bbox_ndc = np.multiply(vertices, bboxsize_ndc) + g_pos_screen[:2]
        bbox_ndc = np.hstack((bbox_ndc, np.zeros((vertices.shape[0],2))))
        bbox_ndc[:,2:4] = g_pos_screen[2:4]
    ```

6. Since the final rendered view consists of a combination of all the gaussians, we add identical full-screen quads for each gaussian and procees them one by one. For each one, we generate the 2D gaussian parameters, as well as the bounding box of the gaussian in screen-coordinates.

7. In an actual graphics pipeline, this bounding box is then used to determine what pixels to draw on the screen. Since we are doing everything manually in the Python version, I scale the 2D gaussian bounding box by the screen size and iterate over each pixel within it, one by one. See the `plot_opacity()` function in the notebook for details.

8. For each pixel, sample the gaussian to obtain the opacity (alpha) value. Use the [spherical harmonics coefficients](https://xoft.tistory.com/50) to determine the RGB color of the pixel for the particular viewing direction from the camera to the gaussian. This pixel value is then added to the output image.

### Rust version
The Rust version uses the [euc](https://github.com/zesterer/euc) software rendering crate. I define a rendering pipeline with a "vertex" and "fragment" shader. It works very similar to how OpenGL or other graphics library does things. So I did not have to iterate over individual pixels like I did in the Python version.

### Repository layout

Github: [https://github.com/thomasantony/splat/](https://github.com/thomasantony/splat/)
```
.
├── Cargo.lock
├── Cargo.toml
├── LICENSE
├── README.md
├── notes
│   ├── 00_Gaussian_Projection.ipynb  <--- Python prototype
│   ├── requirements.txt              <--- install before running notebook
│   ├── util.py
│   └── util_gau.py
├── notes.md
├── src
│   ├── bin
│   │   ├── 00_ply_load.rs        <-- PLY file loading in Rust
│   │   ├── 01_naive_gaussian.rs  <-- Rendering some hard-coded gaussians
│   │   ├── 02_ply_demo.rs        <-- First version the worked
│   │   └── attempt03.rs          <-- incomplete attempt at a different approach
│   ├── camera.rs
│   ├── gaussians.rs
│   ├── lib.rs
│   ├── main.rs                   <-- Current version
│   └── pipelines.rs
```

## Lessons Learned

- When working on a new project, it is always better if you have a working example, or at least some kind of data or reference that you can use to figure out if you are going in the right direction. In this case, the "naive gaussians" example from [https://github.com/limacv/GaussianSplattingViewer](https://github.com/limacv/GaussianSplattingViewer), as well as viewing the GPU buffers for that code using [RenderDoc](https://renderdoc.org/) was extremely helpful

- Unless you are familiar with the field, it is really easy to mess up simple things like loading data from a data file. For example, the PLY model files used for storing the gaussian splats all contain fields called `opacity` and `scale`, the former being the visual opacity of the gaussian and the latter being a 3-vector describing the spread of the gaussian. It is easy to assume that `opacity` is a value between `[0,1]` and `scale` can be used directly to scale the gaussians. It turned out that the opacity was actually `log(opacity)` and had to be exponentiated before use.  Similarly, the `scale` parameter had to be passed through a sigmoid function before use. For someone not too familar with this field, it seems entirely arbitrary (though it makes sense later once you read about it). I would have been stuck with this for a lot longer if I had not seen the existing examples.
  ```rust
        ...
        ("scale_0", Property::Float(v)) => self.scale[0] = v.exp(),
        ("scale_1", Property::Float(v)) => self.scale[1] = v.exp(),
        ("scale_2", Property::Float(v)) => self.scale[2] = v.exp(),
        ("opacity", Property::Float(v)) => self.opacity = 1.0 / (1.0 + (-v).exp()),
        ...
  ```
- The [nalgebra](https://nalgebra.org/) crate, while being a great library for numerical manipulation, has some quirks that can trip you up. For example, if you print a matrix using the debug formatter (`{:?}`), it will print the transpose of the matrix for some reason. This led to me wasting a couple of hours trying to figure out why matrix multiplication no longer worked how I thought it did.
- `-a.max(b)` is not the same as `(-a).max(b)` in Rust
- [RenderDoc](https://renderdoc.org/) does not seem to be able to capture frames from OpenGL programs run in WSL2

## What's Next

While the Python version is far from being real-time, it seems like the rust version is performant enough to run in real-time. Some possible improvements:

* Use "structure-of-arrays" layout to hold the data. This may make a few operations such as sorting the gaussians significantly faster. I opted for array-of-structures in the current version due to how the [ply-rs](https://docs.rs/ply-rs/latest/ply_rs/) file parses data from the point cloud (PLY) files.
* Use a "[geometry shader](https://github.com/zesterer/euc/blob/290e14c0cbe7505867c44ca33a994a9fcfa00fb1/src/pipeline.rs#L221)" to generate the vertices for each gaussian.
* Add camera controls using [egui](https://github.com/emilk/egui) or [imgui](https://github.com/imgui-rs/imgui-rs)

## Acknowledgements

The following articles/code bases were extremely helpful in teaching me about how 3D Gaussian Splats work

- [numbyNum :: 3D Gaussian Splatting for Real-Time Radiance Field Rendering (Reviewed) | Medium](https://medium.com/@AriaLeeNotAriel/numbynum-3d-gaussian-splatting-for-real-time-radiance-field-rendering-kerbl-et-al-60c0b25e5544)
- [3D Gaussian Splatting -
A beginner friendly introduction to 3D Gaussian Splats and tutorial on how to train them.](https://www.reshot.ai/3d-gaussian-splatting)
- [limacv/GaussianSplattingViewer](https://github.com/limacv/GaussianSplattingViewer) - most of my code is based on the vertex and fragment shader code in this repository. Also [RenderDoc](https://renderdoc.org/) for digging into this program further.
- [\[Concept summary\] 3D Gaussian and 2D projection](https://xoft.tistory.com/49)
