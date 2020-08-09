---
title: flybywire — Declarative GUIs for Python inspired by React
description: >-
  Python is amazing. I love the flexibility, the clean and readable syntax and
  its huge ecosystem of libraries. However, when it comes to…
date: '2016-09-04T05:26:46.557Z'
categories: []
keywords: []
slug: /@tantony/flybywire-declarative-guis-for-python-inspired-by-react-ad2131d4cbc1
---

![Source: [xkcd#970](http://xkcd.com/970/) by Randall Monroe](/images/medium/1__Ql7p4__Wua5eSiZB41oAAlg.png)
Source: [xkcd#970](http://xkcd.com/970/) by Randall Monroe

Python is amazing. I love the flexibility, the clean and readable syntax and its huge ecosystem of libraries. However, when it comes to making modern GUIs, it comes up sort in many ways.

There are libraries like _PyQT_ and _Kivy_ to create GUIs for your Python application. However, each of them come with their [own problems](https://medium.com/@tryexceptpass/a-python-ate-my-gui-971f2326ce59#.lpb3pnf2d). Many modern UI solutions like Electron and React-Native looks to the web to avoid the problems of dealing with multiple platforms. After all, the web is one platform that DOES have it’s share of great (and at times awful) UIs.

[_flybywire_](https://github.com/thomasantony/flybywire) is my ongoing experiment to develop a declarative UI library, based off some great work by [Cristian Medina](https://medium.com/u/138c0eb26be5). So, what is _flybywire_ all about? Well, you need a bit of background before I can go into that.

#### React, ES6 and the Endless Abyss

[React](http://facebook.github.io/react) caught my interest sometime late last year when I was trying to build a desktop frontend for a Python project using [Electron](http://electron.atom.io). I was coming back to web development after a gap of nearly six years and my last experience in the field was with jQuery and PHP.

After finishing a basic [tutorial](http://reactfordesigners.com/labs/reactjs-introduction-for-people-who-know-just-enough-jquery-to-get-by/), I was really excited about the possibilities of React. However, that excitement was a little dulled once I discovered the wonderful world of node-based tools that seemed almost mandatory if you wanted to create anything serious. I found that javascript is no longer the innocent, interpreted language I knew it as. ES6, CoffeeScript, TypeScript, transpilers, _webpack_, the endless abyss that is **node-packages** … it is easy to get lost just trying to get a hang of all these tools and frameworks.

So where am I going with all this? Well, my (mis?)adventures with React, Redux etc. can be summarized as:

1.  React seems to have zeroed in on a really good way of defining UIs without much clutter. I especially loved the concept of one-way binding and views defined as pure functions of state which redraws the whole page when updated.
2.  I found redux to be a great addition to the React ecosystem that provides clean and predictable state management along with some very fancy debugging features.
3.  A Python programmer who wants to use React or Electron still has to navigate through the very confusing tooling (_npm_, _webpack_, _babel_ etc.) before they can even start to create anything useful.
4.  I don’t want to deal with Javascript to design my UI.

There has to be a way to do all this in Python!

#### The Magic of Websockets

Last week, I came across this [article](https://medium.com/@tryexceptpass/a-python-ate-my-gui-971f2326ce59#.lpb3pnf2d) which seemed to reflect many of the problems that I had faced when it came to Python GUIs. The article is part of a 3-part (so far) series that ends with the creation of [Sofi](http://github.com/tryexceptpass/sofi) (Cheers [Cristian](https://medium.com/u/138c0eb26be5)!). As described in the article, Sofi is:

> a system that will generate the necessary HTML and JavaScript code typically needed to produce a single-page application and serve it up through WebSockets

Though it is at a very early stage in its design, Sofi seems to do what it is supposed to. It allows you to design UIs in Python while leveraging web technologies like Bootstrap to render them. One thing I did not like about Sofi was the imperative nature of the UI design which reminded me of jQuery (and maybe a bit of Java AWT). After my experience with React, I wanted something declarative and functional.

So, is it possible to leverage websockets to implement something that keeps the general idea behind Sofi, but is declarative and functional like React?

### flybywire

_flybywire_ is my ongoing experiment based on Sofi to create a more declarative UI library. It re-renders the page every time the state changes. It uses a virtual-dom system similar to that used by React, to only update those parts of the page that have actually changed. The coding style in _flybywire_ applications was modeled after that of React. The library includes a helper function that allows components to be defined in a syntax inspired by JSX.

#### Usage

Below is a really simple demo app that is included with the library:

A simple counter app made using **flybywire**

And this is **counter.py.**

```python
from flybywire.core import App  
from flybywire.dom import h

def CounterView(count):  
    """A simple functional stateless component."""  
    return h('h1', str(count))

class CounterApp(App):  
    def \_\_init\_\_(self):  
        """Initialize the application."""  
        super().\_\_init\_\_()  
        self.set\_initial\_state(0)

def render(self):  
        """Renders view given application state."""  
        return h('div',  
                    \[CounterView(count=self.state),  
                     h('button', '+', onclick = self.increment),  
                     h('button', '-', onclick = self.decrement)\]  
                )

def increment(self, e):  
        """Increments counter."""  
        self.set\_state(self.state + 1)

def decrement(self, e):  
        """Decrements counter."""  
        self.set\_state(self.state - 1)

app = CounterApp()  
app.start()
```

#### How it Works

The structure of the code above should be very familiar to anyone who has worked with React before. _flybywire_ provides a helper function for building DOM structures. It is also possible to compose the UI out of stateless, functional components (like **CounterView** in the above example). This DOM structure is then converted into JSON format and sent to the browser over websockets using the [autobahn](http://www.autobahn.ws/python/) library. The javascript part of the library parses the virtual-DOM structure out of the JSON data and patches the existing DOM wherever it has changed. Any DOM event callbacks are also setup to be passed back to the Python app over websockets.

Some of the core parts of this library such as the event server and event processor were directly taken from Sofi with a few modifications. Instead of Bootstrap-based widgets, _flybywire_ allows you to define your own components that can be composed to form whatever widget you need.

It is now possible to make some really simple apps using _flybywire_. However, the library is at a very early stage, given that the First Commit in the repository was only three days ago!

#### What doesn’t work

Here’s some things that are missing and/or acts weird:

*   Some basic manipulations of the DOM elements such as focusing a particular input box or clearing the input box after a certain action is completed are currently not possible. This will probably require putting back some of the command system from Sofi that I had removed when making _flybywire_. This can also possibly be fixed by moving to a platform like Electron which may give greater control over the rendering process.
*   The server shuts down as soon as you close the browser window. This is done on purpose as there is currently no way to reset the application state without restarting the server. The shared state also results in weird behavior if you open multiple windows. Once we move to a platform like Electron, _flybywire_ will have hopefully have more fine control over the life cycle of the application.

#### **Coming Soon**

I will probably add a few more features over the weekend, particularly a better Component class for creating stateful components. Any suggestions/comments/ideas and constructive criticism are welcome!