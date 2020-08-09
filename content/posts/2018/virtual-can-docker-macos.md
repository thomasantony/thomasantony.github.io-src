---
title: Using VirtualCAN inside docker on macOS
description: >-
  At SmartAg, we use Docker to manage the development and runtime environments
  for our embedded software. For performing full-system…
date: '2018-02-09T03:42:31.359Z'
categories: []
keywords: [docker, socketcan, CANbus]
slug: /@tantony/using-virtualcan-inside-docker-on-macos-cfa10f7e75d6
draft: false
---

At [SmartAg](http://www.smart-ag.com/), we use Docker to manage the development and runtime environments for our embedded software. For performing full-system integrated tests, we have built comprehensive simulators that mimic the behavior of the hardware that we automate. Since most of the hardware communication happens over CAN, VirtualCAN is a great way of faking the hardware signals.

![](/images/medium/1__xk974__nijAtuCTMhs7B0__w.png)

Until now, any code that required a CAN interface could not run on my Macbook Pro. This was primarily because the linux kernel used by [Docker for Mac](https://www.docker.com/docker-mac) lacks support for [SocketCAN](https://en.wikipedia.org/wiki/SocketCAN) or VirtualCAN. After much [head-bashing](https://github.com/docker/for-mac/issues/2580), I realized that a better option would be `[docker-machine](https://docs.docker.com/machine/overview/)` , which is how docker was originally run on macOS before the official “Docker for Mac” release.

### Setting up a CAN-enabled docker-machine VM

1.  Install [Homebrew](https://brew.sh/) if you don’t already have it.
2.  Install `docker`, `docker-machine` and some associated software

brew install docker docker-compose docker-machine docker-credential-helper docker-machine-driver-xhyve

3\. Clone the repo from [https://github.com/boot2docker/boot2docker](https://github.com/boot2docker/boot2docker)

4\. Edit `kernel_config` in the `boot2docker` repo and add the following at the bottom:

```
CONFIG\_CAN=y  
CONFIG\_CAN\_RAW=y  
CONFIG\_CAN\_VCAN=y  
CONFIG\_CAN\_DEV=y  
CAN\_SLCAN=y  
CAN\_BCM=y
```

5\. Follow the instructions at [https://github.com/boot2docker/boot2docker/blob/master/doc/BUILD.md](https://github.com/boot2docker/boot2docker/blob/master/doc/BUILD.md) to build your custom `boot2docker` image. This basically boils down to:

```
docker build -t boot2docker .  
docker run --rm boot2docker > boot2docker-can.iso
```
6\. Fix some permissions required by the `xhyve` docker-machine driver.

```
sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve  
sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
```
7\. Create your new `docker-machine` VM with the following command. Change the command appropriately to allocate the desired number of CPUs, amount of RAM and disk space to the VM.

```
docker-machine create default --driver xhyve --xhyve-experimental-nfs-share --xhyve-cpu-count=4 --xhyve-memory-size=4096 --xhyve-disk-size=40000 --xhyve-boot2docker-url boot2docker-can.iso
```
8\. Your `docker-machine` VM is now ready. It should already be running. If you restart your machine, you can start the VM by typing `docker-machine start default` or stop it with `docker-machine stop default` .

9\. Set the environment parameters to use docker with your new VM by running `eval $(docker-machine env default)` . This command has to be run every time you are in a new terminal. You can also add this to your `.bashrc` to make it automatic.

10\. Check that it all works:

```
docker run -it --rm --privileged alpine /bin/sh
```
Inside the docker container, run:

```
zcat /proc/config.gz | grep CAN
```

The command should display the CAN flags that you set while compiling the kernel. SocketCAN/VirtualCAN is now enabled in any docker container that you start on this VM.

### Caveats

Running `docker` using `docker-machine` means that some things, such as port-forwarding does not work as you expect. A handy script for exposing any ports you want from your VM to `localhost` can be found here: [https://github.com/johanhaleby/docker-machine-port-forwarder](https://github.com/johanhaleby/docker-machine-port-forwarder)