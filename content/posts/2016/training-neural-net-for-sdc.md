---
title: Training a neural network in real-time to control a self-driving car
description: >-
  I was lucky enough to be accepted into the first cohort of Udacity’s Self
  Driving Car NanoDegree program back in October. Though I have…
date: '2016-12-11T05:02:01.849Z'
categories: []
keywords: []
slug: >-
  /@tantony/training-a-neural-network-in-real-time-to-control-a-self-driving-car-9ee5654978b7
---

I was lucky enough to be accepted into the first cohort of Udacity’s [Self Driving Car NanoDegree](http://www.udacity.com/drive) program back in October. Though I have been thinking of blogging about my experience since the start, it didn’t really happen till now. I am currently wrapping up Project #3 — “Behavioral Cloning”. This one was considerably tougher than the first two. However, it has been very fulfilling to finally complete it and here I will describe the approach I used for training a neural network to drive a car (in a simulator).

![](/images/medium/1__0ahKkWS__pXY6ktIJMLptgg.png)

The project description makes it looks easy (relatively). In the first project, we detected lanes using some basic Computer Vision methods and in the second, we classified traffic signs from the [German Traffic Signs dataset](http://benchmark.ini.rub.de/?section=gtsdb&subsection=news). The third one seemed like an extension of the second, where instead of classifying traffic signs, we had to predict steering angles based on a camera feed, using a neural network.

### Collecting Training Data

Unlike Project#2, this time we had to collect our own training data. This was more challenging than expected. As it turned out, controlling Udacity’s SDC simulator with a keyboard is not a simple task. Feedback from other students on Slack seemed to indicate that it also gave bad, jittery steering angle data. Fortunately, I have a friend who is crazy about car racing games and owns a Logitech G27 Racing wheel.

![Udacity’s SDC Simulator](/images/medium/1__HPYURL9VsoLEBJ68iYK__xg.png)
Udacity’s SDC Simulator

For training data, I recorded data (“camera” images + steering angle and other telemetry) where I drove through the two tracks a couple of times. I also recorded data while recovering from deliberate perturbations to the sides of the lane to make sure the neural net also learned how to recover from such situations.

### Picking the Architecture and Training the NN

I spent a lot of time experimenting with different convolutional neural network architectures, with varying levels of success. I also tried taking existing trained models like VGG16 and Google’s Inception v3 and adapting them to this purpose. Eventually, I settled upon NVIDIA’s End-to-End Deep Learning architecture described in this [paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf). It was relatively small in size and hence added very little latency when running it. I proceeded to use my gaming desktop with GTX 1070 GPU to train the model on ~32000 images.

What I learned is that “mean square error” was not at all a predictor of the performance of the network in the actual simulator. Another big issue was the turnaround time between collecting data, training the network and then testing it. Also, the ‘remote driving’ script provided by Udacity set the car’s throttle to a constant value with no way to control the speed.

That is when I came across [John Chen](https://medium.com/u/8a1f0a75e0b5)’s post on our Slack channel about how he developed an “[Agile Trainer](https://github.com/diyjac/AgileTrainer)” to reduce the turnaround time between data-collection and testing. His program uses PyGame and Joystick input to manually takeover control from the neural network whenever it deviated too much and also allowed to train the network at the same time.

I wrote my own live trainer based on this idea, which instead used keyboard input. It turned out that my keyboard based “remote driver” was able to control the simulator more reliably than the simulator’s “Training mode”.

Best of all, it allowed me to fine-tune the model from my bed with my Macbook Pro by “[NoMachine](https://www.nomachine.com/)”-ing into my desktop (which would be difficult with a joystick/racing wheel).

### **How it works**

The live trainer has a [Tkinter](https://docs.python.org/3/library/tk.html)\-based UI and a few simple keyboard controls.

![SDC Live Trainer interface](/images/medium/1__kW5kXDzFkn4DCDoIn4hZsg.png)
SDC Live Trainer interface

**Up/Down**: Control cruise speed

**Left/Right**: Steering

**x**: Toggle between autonomous and manual override modes

**c**: Center steering (only in manual override mode)

**z**: Toggle real-time training (only in manual override mode)

The speed of the car is controlled by a proportional-gain controller. It modulates the throttle based on speed feedback. This rudimentary “cruise control” gets the speed within +/- 1 mph of the target speed, which is good enough in this case.

The arrow keys increase/decrease the steering angle. The steering also has some slow auto re-centering dynamics added by the trainer. So the steering angle will keep “decaying” towards zero if you don’t press any key. The “autonomous rating” measures what percentage of the current session was spent in fully autonomous mode.

### Real-time training

The process of training itself is pretty simple. You can do one of two things:

1.  Deliberately perturb the car’s motion while in manual override and engage training mode once you have started the recovery process
2.  At any spots that the model has trouble with, engage training mode while driving through the spot manually to fine-tune the model.

The GIF below shows an example of the first case. I purposely drive the car towards the right edge using manual override and then start training the model once I have it recovering and returning to the center of the lane.

### Evaluating model performance

My initial model had some trouble navigating a couple of turns on track#1 in the simulator. I was able to successfully tune these spots using live training and finally get this result:

Track 2 was a little more difficult, with more sharp gradients and curves. However, I found that decreasing the speed down to 20 mph helped it navigate that track as well!

The live trainer code is on Github at: [**thomasantony/sdc-live-trainer**](https://github.com/thomasantony/sdc-live-trainer)

### Possibilities

A live trainer can also probably be used to perform the initial training of the network, though that would involve a lot more baby-sitting during the training process. The good thing is that you can immediately start seeing results as the model converges toward the right weights.

Is such an architecture extendable to real-world SDCs? It can definitely be done with scale models on scale tracks. On real cars it is probably a little more difficult (though there are probably ways to do it). NVIDIA’s [paper](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) mentions using real-world data to make a simulator. A live training methodology like the one described here can possibly be incorporated into such a simulator as well!

Let me know if you have any comments/suggestions!