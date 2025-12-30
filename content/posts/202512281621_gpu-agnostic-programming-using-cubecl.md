+++
title = "GPU-Agnostic Programming using CubeCL"
date = "2025-12-29T01:23:21.000Z"
draft = false
+++

[CubeCL](https://crates.io/crates/cubecl) is a Rust crate that is used for writing GPU programs in pure Rust, which is compatible with a wide range of GPU platforms. It is the underlying library powering the "[Burn](https://burn.dev/)" machine learning framework.

This article will look at some of the basics of how to use CubeCL and some of its quirks.

## Hello, World

We will start with a very simple parallel program - one that takes an array of numbers and doubles each element. Roughly the same as the following python function, except that it will be using the GPU and executing in parallel

```python
def double_array(numbers):
    output = []
    for i in range(len(numbers)):
        output[i] = numbers[i] * 2.0
    return output
```

Yes, I am aware that this could have been simplified using numpy or a list comprehension. But the point of the above code was to give a direct correlation to the GPU code that we will be writing.

We start off by creating a new Rust project using `cargo`:

```bash
cargo new first-gpu-program
cd first-gpu-program
```

Now we need to add the dependencies - in this case, just `cubecl` with the `wgpu` feature enabled. The WGPU backend allows running your code on a wide range of GPUs. Add the following under `[dependencies]` in `Cargo.toml`

```toml
cubecl = { version = "0.8.1", features = ["wgpu"] }
```

Build and run the program using `cargo run` and the program should build and print out "Hello, world!".

Just like on other GPU programming platforms, the basic unit of a parallel program in CubeCL is a "kernel". This is a function that gets dispatched to execute on the GPU. See the [CubeCL book](https://burn.dev/books/cubecl/getting-started/parallel_reduction.html) for more details. Kernels do not have a return value and will be returning data instead by writing to mutable array references that are passed into it.

Here is the CubeCL version of the Python program given above:

```rust
use cubecl::prelude::*;

#[cube(launch)]
fn kernel_double_numbers(input_data: &Array<u32>, output_data: &mut Array<u32>) {
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let index = block_id * CUBE_DIM + thread_id;
    output_data[index] = input_data[index] * 2;
}

fn main() {
    let device = Default::default();
    let client = cubecl::wgpu::WgpuRuntime::client(&device);

    let input_data = (1..11).collect::<Vec<u32>>();
    println!("Input: {:?}", &input_data);
    let num_elements = input_data.len();
    let zeros = vec![0u32; num_elements];
    let input_data_gpu = client.create(u32::as_bytes(&input_data));
    let output_data_gpu = client.create(u32::as_bytes(&zeros));

    unsafe {
        kernel_double_numbers::launch::<cubecl::wgpu::WgpuRuntime>(
            &client,
            CubeCount::Static(1, 1, 1),
            CubeDim::new(num_elements as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(&input_data_gpu, num_elements, 1),
            ArrayArg::from_raw_parts::<u32>(&output_data_gpu, num_elements, 1),
        )
    }

    let result = client.read_one(output_data_gpu.clone());
    let output = u32::from_bytes(&result).to_vec();
    println!("Output: {:?}", output);
}
```

Compile and run the program and you should see the following:

```
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Let's look at the code in more detail:

### Defining the Kernel

```rust
#[cube(launch)]
```

This is a Rust macro that converts a Rust function into a GPU kernel that can be dispatched. It generates the `::launch` method that is used to dispatch the kernel to the GPU. Within the kernel, you write the code for *one* of the threads. You identify the element of the array that you are supposed to operate on using the intrinsic values `CUBE_POS`, `UNIT_POS` etc.

#### CubeCL Topology

The following diagram illustrates the relationship between Units, Cubes, and Hyper-Cubes:

![CubeCL Topology](/images/cubecl.drawio.svg)

A cube is composed of units, so a 3x3x3 cube has 27 units that can be accessed by their positions along the x, y, and z axes. Similarly, a hyper-cube is composed of cubes, just as a cube is composed of units. Each cube in the hyper-cube can be accessed by its position relative to the hyper-cube along the x, y, and z axes. Hence, a hyper-cube of 3x3x3 will have 27 cubes. In this example, the total number of working units would be 27 x 27 = 729. (Source: [CubeCL Book](https://burn.dev/books/cubecl/getting-started/parallel_reduction.html#cubecl---topology))

The following table (also from the [CubeCL Book](https://burn.dev/books/cubecl/getting-started/parallel_reduction.html#cubecl---topology)) shows how CubeCL's topology constants map to CUDA and WebGPU equivalents:

| CubeCL | CUDA | WebGPU |
|--------|------|--------|
| `CUBE_COUNT_X` | `gridDim.x` | `num_workgroups.x` |
| `CUBE_COUNT_Y` | `gridDim.y` | `num_workgroups.y` |
| `CUBE_COUNT_Z` | `gridDim.z` | `num_workgroups.z` |
| `CUBE_POS_X` | `blockIdx.x` | `workgroup_id.x` |
| `CUBE_POS_Y` | `blockIdx.y` | `workgroup_id.y` |
| `CUBE_POS_Z` | `blockIdx.z` | `workgroup_id.z` |
| `CUBE_DIM_X` | `blockDim.x` | `workgroup_size.x` |
| `CUBE_DIM_Y` | `blockDim.y` | `workgroup_size.y` |
| `CUBE_DIM_Z` | `blockDim.z` | `workgroup_size.z` |
| `UNIT_POS` | N/A | `local_invocation_index` |
| `UNIT_POS_X` | `threadIdx.x` | `local_invocation_id.x` |
| `UNIT_POS_Y` | `threadIdx.y` | `local_invocation_id.y` |
| `UNIT_POS_Z` | `threadIdx.z` | `local_invocation_id.z` |
| `PLANE_DIM` | `warpSize` | `subgroup_size` |
| `ABSOLUTE_POS_X` | N/A | `global_id.x` |
| `ABSOLUTE_POS_Y` | N/A | `global_id.y` |
| `ABSOLUTE_POS_Z` | N/A | `global_id.z` |

In the example code, we assume that the array is to be accessed in the following manner:

```
[x x x x x x x x | x x x x x x x x]
 ^.............^   ^.............^
      Block 0           Block 1
```

This is accomplished by computing the index of the element as:

```rust
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let index = block_id * CUBE_DIM + thread_id;
```

### Initializing the CubeCL Device and Runtime

Going to the `main()` function, the first step is initializing the GPU and the CubeCL runtime:
```rust
    let device = Default::default();
    let client = cubecl::wgpu::WgpuRuntime::client(&device);
```

If you were using a different runtime (say CUDA), you would initialize that here instead of WGPU.

### Initializing GPU buffers and copying input data

The next step is to take the input data and copy it into GPU buffers. GPU buffers need to be defined for the output buffer as well:

```rust
    let input_data = (1..11).collect::<Vec<u32>>();
    println!("Input: {:?}", &input_data);
    let num_elements = input_data.len();

    let zeros = vec![0u32; num_elements];
    let input_data_gpu = client.create(u32::as_bytes(&input_data));
    let output_data_gpu = client.create(u32::as_bytes(&zeros));
```

Note here that the `zeros` variable (and any other CPU-side buffer) can be reused if multiple buffers need to be created. The values are copied to the GPU buffer in each case.

### Launching the kernel

```rust
    unsafe {
        kernel_double_numbers::launch::<cubecl::wgpu::WgpuRuntime>(
            &client,
            CubeCount::Static(1, 1, 1),
            CubeDim::new(num_elements as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(&input_data_gpu, num_elements, 1),
            ArrayArg::from_raw_parts::<u32>(&output_data_gpu, num_elements, 1),
        )
    }
```

This section actually launches the kernel, and dispatches it to the GPU for execution. The first argument is the client object that was initialized earlier.

The second and third arguments specify the "shape" and size of the "cubes" to be scheduled on the GPU. The kernel is executed on a "HyperCube" (called a Grid in CUDA) of cubes, and each cube consists of multiple units (threads). `CubeCount` specifies the size of the hypercube along X, Y, and Z dimensions (only X is used in this example), and `CubeDim` specifies the number of units/threads in each cube.

The `ArrayArg` objects take in the GPU buffer handles created before using `client.create()` and pass them as arguments to the kernel. These values map on to the `&Array<u32>` and `&mut Array<u32>` parameters in the kernel.

### Extracting the output values

Once the computation is complete, the values need to be copied back to the RAM so that we can use them elsewhere.

```rust
    let result = client.read_one(output_data_gpu.clone());
    let output = u32::from_bytes(&result).to_vec();
    println!("Output: {:?}", output);
```

The `output_data_gpu` handle is cloned here in case it needs to be used again elsewhere (maybe for launching another kernel).


## Scalar Arguments

You are also able to pass scalar values to the kernel - lets say, an integer that will be used in place of `2` for scaling the arrays. This is done by passing in an instance of `ScalarArg`. Modify the kernel as follows:

```rust
#[cube(launch)]
fn kernel_scale_numbers(input_data: &Array<u32>, scale: u32, output_data: &mut Array<u32>) {
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let index = block_id * CUBE_DIM + thread_id;
    output_data[index] = input_data[index] * scale;
    //                                       ^ used instead of 2
}
```

The kernel is then launched as:
```rust
    unsafe {
        kernel_scale_numbers::launch::<cubecl::wgpu::WgpuRuntime>(
            &client,
            CubeCount::Static(1, 1, 1),
            CubeDim::new(num_elements as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(&input_data_gpu, num_elements, 1),
            ScalarArg::new(3),  // <-- scalar argument
            ArrayArg::from_raw_parts::<u32>(&output_data_gpu, num_elements, 1),
        )
    }
```

Running the program should now give the output:
```
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```


## Backend-Agnostic Code

The examples above hardcoded the WGPU runtime as the CubeCL backend to use for running the code. This is not ideal if the code is to be distributed as a crate/library. CubeCL offers a generics-based pattern for making your code agnostic to the GPU platform. The kernel itself remains identical as it does not have any platform-specific references. However, the launching of the kernel needs to be extracted out into a separate function.


```rust
fn launch_scale_numbers_kernel<R: Runtime>(
    client: &ComputeClient<R::Server>,
    input: &Handle,
    scale: u32,
    output: &Handle,
    num_elements: usize,
) {
    unsafe {
        kernel_scale_numbers::launch::<R>(
            &client,
            CubeCount::Static(1, 1, 1),
            CubeDim::new(num_elements as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(input, num_elements, 1),
            ScalarArg::new(scale),
            ArrayArg::from_raw_parts::<u32>(output, num_elements, 1),
        )
    }
}
```

The function is then called as:

```rust
    launch_scale_numbers_kernel::<cubecl::wgpu::WgpuRuntime>(
        &client,
        &input_data_gpu,
        3,
        &output_data_gpu,
        num_elements,
    );
```

The `launch_scale_numbers_kernel` could be in a separate crate and is completely agnostic to the specific GPU platform that it will be deployed to. The platform is only specified when the function is called.


## Cube functions

You may want to split out small chunks of your kernel code so that it can be reused in multiple kernels. This is done using by defining functions that use the `#[cube]` macro and comes with a few caveats. The arguments to such functions can either be scalar values (`u32`, `f32` etc.), or a type like `Array`.

Example:

```rust
#[cube]
fn do_scale(input: &Array<u32>, scale: u32) -> u32 {
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let index = block_id * CUBE_DIM + thread_id;
    input[index] * scale
}

#[cube(launch)]
fn kernel_scale_numbers(input_data: &Array<u32>, scale: u32, output_data: &mut Array<u32>) {
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let index = block_id * CUBE_DIM + thread_id;
    output_data[index] = do_scale(input_data, scale);
}
```


## Shared Memory

Shared Memory is allocated in kernels and used for sharing information between threads in the same "cube" (aka block). Since this is implemented as on-chip SRAM, it is significantly faster than the "global" GPU memory. It is allocated in a kernel using the `SharedMemory` type:

```rust
let smem_histogram = SharedMemory::<u32>::new(SIZE);
```

In the above example, `SIZE` must be a constant known at compile-time.

It can then be used like any other array, except that the data in it is only shared across the threads in the same cube.

## Atomic Variables

The `Atomic` type allows definition of variables that are used for atomic read/write operations. Such operations are useful for avoiding race conditions. For Shared Memory, this is defined as:


```rust
let smem_histogram = SharedMemory::<Atomic<u32>>::new(SIZE);
```

For global memory, in CubeCL, it is not necessary to allocate the memory as Atomic. Instead, it is enough to change the type of the parameter to the kernel to say `&Array<Atomic<u32>>` instead of `&Array<u32>`.

Read operations are performed as:

```rust
let val = Atomic::load(&smem_histogram[i]);
```

Write operations can be done as:
```rust
Atomic::store(&smem_histogram[i], val);
```

See all the valid atomic operations on this [page](https://docs.rs/cubecl-core/0.8.1/cubecl_core/frontend/struct.Atomic.html)


## Plane Intrinsics

In CubeCL, there is a concept of something called a "plane". This is a sub-set of the threads in a block. This has to do with how the threads are actually scheduled on the GPU for execution. On NVIDIA GPUs, threads are scheduled for execution as sets of 32 threads called "warps". These are guaranteed to be running simultaneously on a GPU. If you schedule blocks that are larger than the warp-size on the GPU, the block gets split up into warps (aka planes in CubeCL), and gets swapped in and out.

CubeCL offers some GPU primitives that operate at the level of all threads on the plane. These are not very well documented at the time of writing unless you wade through some of the unit tests.

### Plane Exclusive Sum

Here is an example where we use plane intrinsics to compute an "[exclusive sum](https://en.wikipedia.org/wiki/Prefix_sum#Inclusive_and_exclusive_scans)". The algorithm will take an array like `[1, 1, 1, 1]` and return `[0, 1, 2, 3]`. It uses the [plane_exclusive_sum](https://docs.rs/cubecl/latest/cubecl/frontend/fn.plane_exclusive_sum.html) function.

```rust
#[cube(launch)]
fn kernel_plane_exclusive_sum(input_data: &Array<u32>, output_data: &mut Array<u32>) {
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;

    let local_data = input_data[block_id * CUBE_DIM + thread_id];
    let local_sum = plane_exclusive_sum(local_data);

    output_data[block_id * CUBE_DIM + thread_id] = local_sum;
}

fn main()
{
    let device = Default::default();
    let client = cubecl::wgpu::WgpuRuntime::client(&device);

    type R = cubecl::wgpu::WgpuRuntime;

    let input_data = vec![1u32; 16];
    println!("Input: {:?}", &input_data);
    let num_elements = input_data.len();
    let zeros = vec![0u32; num_elements];
    let input_data_gpu = client.create(u32::as_bytes(&input_data));
    let output_data_gpu = client.create(u32::as_bytes(&zeros));

    const SMALL_BLOCK_SIZE: usize = 8;
    let num_blocks = num_elements / SMALL_BLOCK_SIZE;
    unsafe {
        kernel_plane_exclusive_sum::launch::<R>(
            &client,
            CubeCount::Static(num_blocks as u32, 1, 1),
            CubeDim::new(SMALL_BLOCK_SIZE as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(&input_data_gpu, num_elements, 1),
            ArrayArg::from_raw_parts::<u32>(&output_data_gpu, num_elements, 1),
        )
    }
    let result = client.read_one(output_data_gpu.clone());
    let output = u32::from_bytes(&result).to_vec();
    println!("Plane Exclusive Sum: {:?}\n", output);
}
```

The magic happens in these lines:
```rust
    let local_data = input_data[block_id * CUBE_DIM + thread_id];
    let local_sum = plane_exclusive_sum(local_data);

    output_data[block_id * CUBE_DIM + thread_id] = local_sum;
```
The `plane_exclusive_sum` takes the value of `local_data` from every other unit/thread in the current plane/warp and computes an exclusive sum, and returns the value that should be returned by the current thread.

One caveat here is that this is limited to the plane (usually a maximum of 32-64 threads depending on the GPU platform). In the above example, we use an array with 16 elements and enforce a block-size (and hence plane size) of 8. This will give us the following result:

```
Input: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Plane Exclusive Sum: [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
```

If you want to perform an exclusive scan over the entire block (possibly multiple planes), we need to use a more complicated algorithm where shared memory is used to accumulate results between planes.

### Block Exclusive Sum

```rust
/// Performs exclusive sum over all elements in a block, using plane primitives
#[cube(launch)]
fn kernel_block_exclusive_sum(input_data: &Array<u32>, output_data: &mut Array<u32>) {
    let num_planes: u32 = CUBE_DIM / PLANE_DIM;
    let block_id = CUBE_POS;
    let thread_id = UNIT_POS;
    let plane_thread_idx = UNIT_POS_PLANE;
    let plane_idx = thread_id / PLANE_DIM;

    let thread_idx = block_id * CUBE_DIM + thread_id;

    // Select plane size as the smaller of the current block size or the max plane size
    // So if block size is 8, plane size will be 8
    // If block size is 64, plane size will be 32 (if that is the maximum)
    let plane_size = if CUBE_DIM < PLANE_DIM {
        CUBE_DIM
    } else {
        PLANE_DIM
    };

    // Define shared memory for inter-plane communication
    let mut shared_totals = SharedMemory::<u32>::new(2);

    // 1. local scan
    let original = input_data[thread_idx];
    let local_scan = plane_exclusive_sum(original);

    // 2. plane totals → shared mem
    let plane_total =
        plane_shuffle(local_scan, plane_size - 1) + plane_shuffle(original, plane_size - 1);
    if plane_thread_idx == 0 {
        shared_totals[plane_idx] = plane_total;
    }
    sync_cube();

    // 3. scan totals (single plane or serial)
    if plane_idx == 0 && plane_thread_idx < num_planes {
        let offset = plane_exclusive_sum(shared_totals[plane_thread_idx]);
        // reuse shared_totals for storing offsets
        shared_totals[plane_thread_idx] = offset;
    }
    sync_cube();

    // 4. apply offset
    let result = local_scan + shared_totals[plane_idx];

    output_data[block_id * CUBE_DIM + thread_id] = result;
}

fn main()
{
    let device = Default::default();
    let client = cubecl::wgpu::WgpuRuntime::client(&device);

    type R = cubecl::wgpu::WgpuRuntime;

    let input_data = vec![1u32; 64];
    println!("Input: {:?}", &input_data);
    let num_elements = input_data.len();
    let input_data_gpu = client.create(u32::as_bytes(&input_data));
    let zeros = vec![0u32; num_elements];
    let output_data_gpu = client.create(u32::as_bytes(&zeros));
    const BIG_BLOCK_SIZE: usize = 64;
    let num_blocks = num_elements / BIG_BLOCK_SIZE;
    unsafe {
        kernel_block_exclusive_sum::launch::<R>(
            &client,
            CubeCount::Static(num_blocks as u32, 1, 1),
            CubeDim::new(BIG_BLOCK_SIZE as u32, 1, 1),
            ArrayArg::from_raw_parts::<u32>(&input_data_gpu, num_elements, 1),
            ArrayArg::from_raw_parts::<u32>(&output_data_gpu, num_elements, 1),
        )
    }
    let result = client.read_one(output_data_gpu.clone());
    let output = u32::from_bytes(&result).to_vec();
    println!("Block Exclusive Sum: {:?}\n", output);
}
```

Here, we use a larger array with 64 elements to make sure that the block size exceeds the plane size (on WGPU) of 32.

The algorithm works as follows:

1. The local scan takes the 64-long array `[1, 1, ... 1]` and converts it into `[0, 1, ... 31, 0, 1, ... 31]`.

2. The next step is to compute the "shared totals". This is the total sum from each plane accumulated into a shared memory array. In this case, it would be `[32, 32]`. This is done by adding the last value of the local scan in the current plane, with the last value of the input array processed by the current plane.


To compute this, we use another plane-intrinsic function called [plane_shuffle](https://docs.rs/cubecl/latest/cubecl/frontend/fn.plane_shuffle.html). 

```rust
plane_shuffle(local_scan, plane_size - 1)
```

The above function call returns the value of `local_scan` from the thread index `plane_size - 1` (aka the final thread in the plane). So the shared total is computed as:

```rust
    let plane_total =
        plane_shuffle(local_scan, plane_size - 1) + plane_shuffle(original, plane_size - 1);
    if plane_thread_idx == 0 {
        shared_totals[plane_idx] = plane_total;
    }
```
The value is then stored into the shared memory by a single thread (gated by the `if` condition). There is no point in all of the threads trying to write the exact same value to the shared array.

3. Compute the offsets from the shared totals using another exclusive scan, i.e. `[32, 32]` becomes `[0, 32]`. These are the values to be added to each plane's local scan results. So we add `0` to the local scan results from plane 0, `32` to the local scan results from plane 1, etc.

This exclusive scan can also be performed using the `plane_exclusive_sum` function - except that we make sure to not use more threads than are required.

```rust
        let offset = plane_exclusive_sum(shared_totals[plane_thread_idx]);
        // reuse shared_totals for storing offsets
        shared_totals[plane_thread_idx] = offset;
```

4. Now applying the offset is as simple as taking the current thread's local scan result (`local_scan`) and adding the appropriate offset to it.

*Note*: `sync_cube()` is used to synchronize processing between all the threads/units in a block. All the threads will wait at these points until every other thread in the block has reached the same point.

This should now give the result:

```
Input: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Block Exclusive Sum: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
```

## Gotchas

* CubeCL does not like mutable unused variables without a type definition.

If you add the following to a kernel or a #[cube] function :
```rust
let mut mynumber = 0;
```

If you do not use this value anywhere in a way that lets the compiler infer its type, you will get an error message like:

```
error[E0283]: type annotations needed
  --> src/main.rs:88:1
   |
88 | #[cube(launch)]
   | ^^^^^^^^^^^^^^^ cannot infer type for struct `ExpandElementTyped<_>`
   |
   = note: multiple `impl`s satisfying `ExpandElementTyped<_>: IntoMut` found in the `cubecl_core` crate:
           - impl<T> IntoMut for ExpandElementTyped<T>
             where T: ExpandElementIntoMut;
           - impl<T> IntoMut for ExpandElementTyped<cubecl::frontend::SharedMemory<T>>
             where T: CubePrimitive;
   = note: this error originates in the attribute macro `cube` (in Nightly builds, run with -Z macro-backtrace for more info)
```

It doesn't say which line of the code causes the error, so it can be confusing if you did not know what to look for.


## Conclusion

CubeCL provides a compelling approach to GPU programming in Rust, offering the ability to write portable GPU code that can target multiple backends (WGPU, CUDA, etc.) from a single codebase. While the documentation is still maturing, the core concepts map well to existing GPU programming paradigms, making it accessible to developers familiar with CUDA or other GPU frameworks.
