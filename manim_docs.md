# Quickstart



# Quickstart[¶](#quickstart "Link to this heading")



Note


Before proceeding, install Manim and make sure it’s running properly by
following the steps in [Installation](../installation.html). For
information on using Manim with Jupyterlab or Jupyter notebook, go to the
documentation for the
[`IPython magic command`](../reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic.manim "manim.utils.ipython_magic.ManimMagic.manim"),
`%%manim`.




## Overview[¶](#overview "Link to this heading")


This quickstart guide will lead you through creating a sample project using Manim: an animation
engine for precise programmatic animations.


First, you will use a command line
interface to create a `Scene`, the class through which Manim generates videos.
In the `Scene` you will animate a circle. Then you will add another `Scene` showing
a square transforming into a circle. This will be your introduction to Manim’s animation ability.
Afterwards, you will position multiple mathematical objects (`Mobject`s). Finally, you
will learn the `.animate` syntax, a powerful feature that animates the methods you
use to modify `Mobject`s.




## Starting a new project[¶](#starting-a-new-project "Link to this heading")


Start by creating a new folder. For the purposes of this guide, name the folder `project`:



```
project/

```


This folder is the root folder for your project. It contains all the files that Manim needs to function,
as well as any output that your project produces.




## Animating a circle[¶](#animating-a-circle "Link to this heading")


1. Open a text editor, such as Notepad. Copy the following code snippet into the window:



```
from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

```


2. Save the code snippet into your project folder with the name `scene.py`.



```
project/
└─scene.py

```


3\. Open the command line, navigate to your project folder, and execute
the following command:



```
manim -pql scene.py CreateCircle

```


Manim will output rendering information, then create an MP4 file.
Your default movie player will play the MP4 file, displaying the following animation.



If you see an animation of a pink circle being drawn, congratulations!
You just wrote your first Manim scene from scratch.


If you get an error
message instead, you do not see a video, or if the video output does not
look like the preceding animation, it is likely that Manim has not been
installed correctly. Please refer to our [FAQ section](../faq/index.html)
for help with the most common issues.



### Explanation[¶](#explanation "Link to this heading")


Let’s go over the script you just executed line by line to see how Manim was
able to draw the circle.


The first line imports all of the contents of the library:



```
from manim import *

```


This is the recommended way of using Manim, as a single script often uses
multiple names from the Manim namespace. In your script, you imported and used
`Scene`, `Circle`, `PINK` and `Create`.


Now let’s look at the next two lines:



```
class CreateCircle(Scene):
    def construct(self):
        [...]

```


Most of the time, the code for scripting an animation is entirely contained within
the [`construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method of a [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") class.
Inside [`construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct"), you can create objects, display them on screen, and animate them.


The next two lines create a circle and set its color and opacity:



```
circle = Circle()  # create a circle
circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

```


Finally, the last line uses the animation [`Create`](../reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") to display the
circle on your screen:



```
self.play(Create(circle))  # show the circle on screen

```



Tip


All animations must reside within the [`construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method of a
class derived from [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene"). Other code, such as auxiliary
or mathematical functions, may reside outside the class.






## Transforming a square into a circle[¶](#transforming-a-square-into-a-circle "Link to this heading")


With our circle animation complete, let’s move on to something a little more complicated.


1. Open `scene.py`, and add the following code snippet below the `CreateCircle` class:



```
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

```


2. Render `SquareToCircle` by running the following command in the command line:



```
manim -pql scene.py SquareToCircle

```


The following animation will render:



This example shows one of the primary features of Manim: the ability to
implement complicated and mathematically intensive animations (such as cleanly
interpolating between two geometric shapes) with just a few lines of code.




## Positioning `Mobject`s[¶](#positioning-mobjects "Link to this heading")


Next, let’s go over some basic techniques for positioning `Mobject`s.


1. Open `scene.py`, and add the following code snippet below the `SquareToCircle` method:



```
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

```


2. Render `SquareAndCircle` by running the following command in the command line:



```
manim -pql scene.py SquareAndCircle

```


The following animation will render:



`next_to` is a `Mobject` method for positioning `Mobject`s.


We first specified
the pink circle as the square’s reference point by passing `circle` as the method’s first argument.
The second argument is used to specify the direction the `Mobject` is placed relative to the reference point.
In this case, we set the direction to `RIGHT`, telling Manim to position the square to the right of the circle.
Finally, `buff=0.5` applied a small distance buffer between the two objects.


Try changing `RIGHT` to `LEFT`, `UP`, or `DOWN` instead, and see how that changes the position of the square.


Using positioning methods, you can render a scene with multiple `Mobject`s,
setting their locations in the scene using coordinates or positioning them
relative to each other.


For more information on `next_to` and other positioning methods, check out the
list of [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") methods in our reference manual.




## Using `.animate` syntax to animate methods[¶](#using-animate-syntax-to-animate-methods "Link to this heading")


The final lesson in this tutorial is using `.animate`, a `Mobject` method which
animates changes you make to a `Mobject`. When you prepend `.animate` to any
method call that modifies a `Mobject`, the method becomes an animation which
can be played using `self.play`. Let’s return to `SquareToCircle` to see the
differences between using methods when creating a `Mobject`,
and animating those method calls with `.animate`.


1. Open `scene.py`, and add the following code snippet below the `SquareAndCircle` class:



```
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

```


2. Render `AnimatedSquareToCircle` by running the following command in the command line:



```
manim -pql scene.py AnimatedSquareToCircle

```


The following animation will render:



The first `self.play` creates the square. The second animates rotating it 45 degrees.
The third transforms the square into a circle, and the last colors the circle pink.
Although the end result is the same as that of `SquareToCircle`, `.animate` shows
`rotate` and `set_fill` being applied to the `Mobject` dynamically, instead of creating them
with the changes already applied.


Try other methods, like `flip` or `shift`, and see what happens.


3. Open `scene.py`, and add the following code snippet below the `AnimatedSquareToCircle` class:



```
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

```


4. Render `DifferentRotations` by running the following command in the command line:



```
manim -pql scene.py DifferentRotations

```


The following animation will render:



This `Scene` illustrates the quirks of `.animate`. When using `.animate`, Manim
actually takes a `Mobject`’s starting state and its ending state and interpolates the two.
In the `AnimatedSquareToCircle` class, you can observe this when the square rotates:
the corners of the square appear to contract slightly as they move into the positions required
for the first square to transform into the second one.


In `DifferentRotations`, the difference between `.animate`’s interpretation of rotation and the
`Rotate` method is far more apparent. The starting and ending states of a `Mobject` rotated 180 degrees
are the same, so `.animate` tries to interpolate two identical objects and the result is the left square.
If you find that your own usage of `.animate` is causing similar unwanted behavior, consider
using conventional animation methods like the right square, which uses `Rotate`.




## `Transform` vs `ReplacementTransform`[¶](#transform-vs-replacementtransform "Link to this heading")


The difference between `Transform` and `ReplacementTransform` is that `Transform(mob1, mob2)` transforms the points
(as well as other attributes like color) of `mob1` into the points/attributes of `mob2`.


`ReplacementTransform(mob1, mob2)` on the other hand literally replaces `mob1` on the scene with `mob2`.


The use of `ReplacementTransform` or `Transform` is mostly up to personal preference. They can be used to accomplish the same effect, as shown below.



```
class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

```


However, in some cases it is more beneficial to use `Transform`, like when you are transforming several mobjects one after the other.
The code below avoids having to keep a reference to the last mobject that was transformed.



Example: TransformCycle [¶](#transformcycle)



```
from manim import *

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))

```



```

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))


```

### You’re done![¶](#you-re-done "Link to this heading")


With a working installation of Manim and this sample project under your belt,
you’re ready to start creating animations of your own. To learn
more about what Manim is doing under the hood, move on to the next tutorial:
[Manim’s Output Settings](output_and_config.html). For an overview of
Manim’s features, as well as its configuration and other settings, check out the
other [Tutorials](index.html). For a list of all available features, refer to the
[Reference Manual](../reference.html) page.







---

# Adding Voiceovers to Videos



# Adding Voiceovers to Videos[¶](#adding-voiceovers-to-videos "Link to this heading")


Creating a full\-fledged video with voiceovers is a bit more involved than
creating purely visual Manim scenes. One has to use [a video editing
program](https://en.wikipedia.org/wiki/List_of_video_editing_software)
to add the voiceovers after the video has been rendered. This process
can be difficult and time\-consuming, since it requires a lot of planning
and preparation.


To ease the process of adding voiceovers to videos, we have created
[Manim Voiceover](https://voiceover.manim.community), a plugin
that lets you add voiceovers to scenes directly in Python. To install it, run



```
pip install "manim-voiceover[azure,gtts]"

```


Visit [the installation page](https://voiceover.manim.community/en/latest/installation.html)
for more details on how to install Manim Voiceover.



## Basic Usage[¶](#basic-usage "Link to this heading")


Manim Voiceover lets you …


* Add voiceovers to Manim videos directly in Python, without having to use a video editor.
* Record voiceovers with your microphone during rendering through a simple command line interface.
* Develop animations with auto\-generated AI voices from various free and proprietary services.


It provides a very simple API that lets you specify your voiceover script
and then record it during rendering:



```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService


# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class RecorderExample(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(RecorderService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

```


To get started with Manim Voiceover,
visit the [Quick Start Guide](https://voiceover.manim.community/en/latest/quickstart.html).


Visit the [Example Gallery](https://voiceover.manim.community/en/latest/examples.html)
to see some examples of Manim Voiceover in action.






---

# Manim’s Output Settings



# Manim’s Output Settings[¶](#manim-s-output-settings "Link to this heading")


This document will focus on understanding manim’s output files and some of the
main command\-line flags available.



Note


This tutorial picks up where [Quickstart](quickstart.html) left off, so please
read that document before starting this one.




## Manim output folders[¶](#manim-output-folders "Link to this heading")


At this point, you have just executed the following command.



```
manim -pql scene.py SquareToCircle

```


Let’s dissect what just happened step by step. First, this command executes
manim on the file `scene.py`, which contains our animation code. Further,
this command tells manim exactly which `Scene` is to be rendered, in this case,
it is `SquareToCircle`. This is necessary because a single scene file may
contain more than one scene. Next, the flag \-p tells manim to play the scene
once it’s rendered, and the \-ql flag tells manim to render the scene in low
quality.


After the video is rendered, you will see that manim has generated some new
files and the project folder will look as follows.



```
project/
├─scene.py
└─media
  ├─videos
  |  └─scene
  |     └─480p15
  |        ├─SquareToCircle.mp4
  |        └─partial_movie_files
  ├─text
  └─Tex

```


There are quite a few new files. The main output is in
`media/videos/scene/480p15/SquareToCircle.mp4`. By default, the `media`
folder will contain all of manim’s output files. The `media/videos`
subfolder contains the rendered videos. Inside of it, you will find one folder
for each different video quality. In our case, since we used the `-l` flag,
the video was generated at 480 resolution at 15 frames per second from the
`scene.py` file. Therefore, the output can be found inside
`media/videos/scene/480p15`. The additional folders
`media/videos/scene/480p15/partial_movie_files` as well as `media/text` and
`media/Tex` contain files that are used by manim internally.


You can see how manim makes use of the generated folder structure by executing
the following command,



```
manim -pqh scene.py SquareToCircle

```


The `-ql` flag (for low quality) has been replaced by the `-qh` flag, for
high quality. Manim will take considerably longer to render this file, and it
will play it once it’s done since we are using the `-p` flag. The output
should look like this:



And the folder structure should look as follows.



```
project/
├─scene.py
└─media
  ├─videos
  | └─scene
  |   ├─480p15
  |   | ├─SquareToCircle.mp4
  |   | └─partial_movie_files
  |   └─1080p60
  |     ├─SquareToCircle.mp4
  |     └─partial_movie_files
  ├─text
  └─Tex

```


Manim has created a new folder `media/videos/1080p60`, which corresponds to
the high resolution and the 60 frames per second. Inside of it, you can find
the new `SquareToCircle.mp4`, as well as the corresponding
`partial_movie_files`.


When working on a project with multiple scenes, and trying out multiple
resolutions, the structure of the output directories will keep all your videos
organized.


Further, manim has the option to output the last frame of a scene, when adding
the flag `-s`. This is the fastest option to quickly get a preview of a scene.
The corresponding folder structure looks like this:



```
project/
├─scene.py
└─media
  ├─images
  | └─scene
  |   ├─SquareToCircle.png
  ├─videos
  | └─scene
  |   ├─480p15
  |   | ├─SquareToCircle.mp4
  |   | └─partial_movie_files
  |   └─1080p60
  |     ├─SquareToCircle.mp4
  |     └─partial_movie_files
  ├─text
  └─Tex

```


Saving the last frame with `-s` can be combined with the flags for different
resolutions, e.g. `-s -ql`, `-s -qh`




## Sections[¶](#sections "Link to this heading")


In addition to the movie output file one can use sections. Each section produces
its own output video. The cuts between two sections can be set like this:



```
def construct(self):
    # play the first animations...
    # you don't need a section in the very beginning as it gets created automatically
    self.next_section()
    # play more animations...
    self.next_section("this is an optional name that doesn't have to be unique")
    # play even more animations...
    self.next_section("this is a section without any animations, it will be removed")

```


All the animations between two of these cuts get concatenated into a single output
video file.
Be aware that you need at least one animation in each section. For example this wouldn’t create an output video:



```
def construct(self):
    self.next_section()
    # this section doesn't have any animations and will be removed
    # but no error will be thrown
    # feel free to tend your flock of empty sections if you so desire
    self.add(Circle())
    self.next_section()

```


One way of fixing this is to wait a little:



```
def construct(self):
    self.next_section()
    self.add(Circle())
    # now we wait 1sec and have an animation to satisfy the section
    self.wait()
    self.next_section()

```


For videos to be created for each section you have to add the `--save_sections` flag to the Manim call like this:



```
manim --save_sections scene.py

```


If you do this, the `media` folder will look like this:



```
media
├── images
│   └── simple_scenes
└── videos
    └── simple_scenes
        └── 480p15
            ├── ElaborateSceneWithSections.mp4
            ├── partial_movie_files
            │   └── ElaborateSceneWithSections
            │       ├── 2201830969_104169243_1331664314.mp4
            │       ├── 2201830969_398514950_125983425.mp4
            │       ├── 2201830969_398514950_3447021159.mp4
            │       ├── 2201830969_398514950_4144009089.mp4
            │       ├── 2201830969_4218360830_1789939690.mp4
            │       ├── 3163782288_524160878_1793580042.mp4
            │       └── partial_movie_file_list.txt
            └── sections
                ├── ElaborateSceneWithSections_0000.mp4
                ├── ElaborateSceneWithSections_0001.mp4
                ├── ElaborateSceneWithSections_0002.mp4
                └── ElaborateSceneWithSections.json

```


As you can see each section receives their own output video in the `sections` directory.
The JSON file in here contains some useful information for each section:



```
[
    {
        "name": "create square",
        "type": "default.normal",
        "video": "ElaborateSceneWithSections_0000.mp4",
        "codec_name": "h264",
        "width": 854,
        "height": 480,
        "avg_frame_rate": "15/1",
        "duration": "2.000000",
        "nb_frames": "30"
    },
    {
        "name": "transform to circle",
        "type": "default.normal",
        "video": "ElaborateSceneWithSections_0001.mp4",
        "codec_name": "h264",
        "width": 854,
        "height": 480,
        "avg_frame_rate": "15/1",
        "duration": "2.000000",
        "nb_frames": "30"
    },
    {
        "name": "fade out",
        "type": "default.normal",
        "video": "ElaborateSceneWithSections_0002.mp4",
        "codec_name": "h264",
        "width": 854,
        "height": 480,
        "avg_frame_rate": "15/1",
        "duration": "2.000000",
        "nb_frames": "30"
    }
]

```


This data can be used by third party applications, like a presentation system or automated video editing tool.


You can also skip rendering all animations belonging to a section like this:



```
def construct(self):
    self.next_section(skip_animations=True)
    # play some animations that shall be skipped...
    self.next_section()
    # play some animations that won't get skipped...

```




## Some command line flags[¶](#some-command-line-flags "Link to this heading")


When executing the command



```
manim -pql scene.py SquareToCircle

```


it specifies the scene to render. This is not necessary now. When a single
file contains only one `Scene` class, it will just render the `Scene`
class. When a single file contains more than one `Scene` class, manim will
let you choose a `Scene` class. If your file contains multiple `Scene`
classes, and you want to render them all, you can use the `-a` flag.


As discussed previously, the `-ql` specifies low render quality (854x480
15FPS). This does not look very good, but is very useful for rapid
prototyping and testing. The other options that specify render quality are
`-qm`, `-qh`, `-qp` and `-qk` for medium (1280x720 30FPS), high
(1920x1080 60FPS), 2k (2560x1440 60FPS) and 4k quality (3840x2160 60FPS),
respectively.


The `-p` flag plays the animation once it is rendered. If you want to open
the file browser at the location of the animation instead of playing it, you
can use the `-f` flag. You can also omit these two flags.


Finally, by default manim will output .mp4 files. If you want your animations
in .gif format instead, use the `--format gif` flag. The output files will
be in the same folder as the .mp4 files, and with the same name, but a
different file extension.


This was a quick review of some of the most frequent command\-line flags.
For a thorough review of all flags available, see the [thematic guide on
Manim’s configuration system](../guides/configuration.html).






---

# FAQ: General Usage



# FAQ: General Usage[¶](#faq-general-usage "Link to this heading")



## Why does Manim say that “there are no scenes inside that module”?[¶](#why-does-manim-say-that-there-are-no-scenes-inside-that-module "Link to this heading")


There are two main reasons why this error appears: if you have edited
the file containing your `Scene` class and forgot to save it, or if you
have accidentally passed the name of a wrong file to `manim`, this is
a likely outcome. Check that you have spelled everything correctly.


Otherwise, you are likely mixing up Manim versions. See [this FAQ answer](installation.html#different-versions)
for an explanation regarding why there are different versions. Under the
assumption that you are trying to use the `manim` executable from the terminal to run
a scene that has been written for the community version (i.e., there is
`from manim import *`, or more specifically `from manim import Scene`),
then this error indicates that the `manim` executable has been overwritten
by the one provided by `manimgl` (unfortunately, both `manim` and `manimgl`
provide a `manim` executable).


You can check whether this is the case by running `manim --version`, the output of
the community maintained version starts with `Manim Community v...`. If this is not
the case, you are running `manimgl`.


You can resolve this by either of the following steps:


* Un\- and reinstalling `manim`,
* using the `manimce` executable in place of the `manim` one,
* or replacing the call to the executable with a direct call to the
Python module via `python -m manim`.





---



## No matter what code I put in my file, Manim only renders a black frame! Why?[¶](#no-matter-what-code-i-put-in-my-file-manim-only-renders-a-black-frame-why "Link to this heading")


If you are using the usual pattern to write a `Scene`, i.e.,



```
class MyAwesomeScene(Scene):
    def construct(self):
        ...
        # your animation code

```


then double check whether you have spelled `construct` correctly.
If the method containing your code is not called `construct` (or
if you are not calling a different, custom method from `construct`),
Manim will not call your method and simply output a black frame.





---



## What are the default measurements for Manim’s scene?[¶](#what-are-the-default-measurements-for-manim-s-scene "Link to this heading")


The scene measures 8 units in height and has a default ratio of 16:9,
which means that it measures \\(8 \\cdot 16 / 9 \= 14 \+ 2/9\\) units in width.
The origin is in the center of the scene, which means that, for example, the
upper left corner of the scene has coordinates `[-7-1/9, 4, 0]`.





---



## How do I find out which keyword arguments I can pass when creating a `Mobject`?[¶](#how-do-i-find-out-which-keyword-arguments-i-can-pass-when-creating-a-mobject "Link to this heading")


Let us consider a specific example, like the [`Circle`](../reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle") class. When looking
at its documentation page, only two specific keyword arguments are listed
(`radius`, and `color`). Besides these concrete arguments, there is also a
catchall `**kwargs` argument which captures all other arguments that are passed
to `Circle`, and passes them on to the base class of [`Circle`](../reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle"), [`Arc`](../reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc").


The same holds for [`Arc`](../reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc"): some arguments are explicitly documented, and
there is again a catchall `**kwargs` argument that passes unprocessed arguments
to the next base class – and so on.


The most important keyword arguments relevant to styling your mobjects are the
ones that are documented for the base classes [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") and
[`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").





---



## Can Manim render a video with transparent background?[¶](#can-manim-render-a-video-with-transparent-background "Link to this heading")


Yes: simply pass the CLI flag `-t` (or its long form `--transparent`).
Note that the default video file format does not support transparency,
which is why Manim will output a `.mov` instead of a `.mp4` when
rendering with a transparent background. Other movie file formats
that support transparency can be obtained by passing
`--format=webm` or `--format=gif`.





---



## I have watched a video where a creator ran command X, but it does not work for me. Why?[¶](#i-have-watched-a-video-where-a-creator-ran-command-x-but-it-does-not-work-for-me-why "Link to this heading")


The video you have been watching is likely outdated. If you want to follow
along, you either need to use the same version used in the video, or
modify the code (in many cases it is just a method having been renamed etc.)
accordingly. Check the video description, in some cases creators point out
whether changes need to be applied to the code shown in the video.





---



## When using `Tex` or `MathTex`, some letters are missing. How can I fix this?[¶](#when-using-tex-or-mathtex-some-letters-are-missing-how-can-i-fix-this "Link to this heading")


It is possible that you have to (re)build some fonts used by LaTeX. For
some distributions, you can do this manually by running



```
fmtutil -sys --all

```


We recommend consulting the documentation of your LaTeX distribution
for more information.





---



## I want to translate some code from `manimgl` to `manim`, what do I do with `CONFIG` dictionaries?[¶](#i-want-to-translate-some-code-from-manimgl-to-manim-what-do-i-do-with-config-dictionaries "Link to this heading")


The community\-maintained version has dropped the use of `CONFIG` dictionaries very
early, with [version v0\.2\.0](../changelog/0.2.0-changelog.html) released in
January 2021\.


Before that, Manim’s classes basically processed `CONFIG` dictionaries
by mimicking inheritance (to properly process `CONFIG` dictionaries set
by parent classes) and then assigning all of the key\-value\-pairs in the
dictionary as attributes of the corresponding object.


In situations where there is not much inheritance going on,
or for any custom setting, you should set these attributes yourself.
For example, for an old\-style `Scene` with custom attributes like



```
class OldStyle(Scene):
    CONFIG = {"a": 1, "b": 2}

```


should be written as



```
class NewStyle(Scene):
    a = 1
    b = 2

```


In situations where values should be properly inherited, the arguments
should be added to the initialization function of the class. An old\-style
mobject `Thing` could look like



```
class Thing(VMobject):
    CONFIG = {
        "stroke_color": RED,
        "fill_opacity": 0.7,
        "my_awesome_argument": 42,
    }

```


where `stroke_color` and `fill_opacity` are arguments that concern the
parent class of `Thing`, and `my_awesome_argument` is a custom argument
that only concerns `Thing`. A version without `CONFIG` could look like this:



```
class Thing(VMobject):
    def __init__(
        self, stroke_color=RED, fill_opacity=0.7, my_awesome_argument=42, **kwargs
    ):
        self.my_awesome_argument = my_awesome_argument
        super().__init__(stroke_color=stroke_color, fill_opacity=fill_opacity, **kwargs)

```





---



## My installation does not support converting PDF to SVG, help?[¶](#my-installation-does-not-support-converting-pdf-to-svg-help "Link to this heading")


This is an issue with `dvisvgm`, the tool shipped with LaTeX that
transforms LaTeX output to a `.svg` file that
Manim can parse.


First, make sure your `dvisvgm` version is at least 2\.4 by
checking the output of



```
dvisvgm --version

```


If you do not know how to update `dvisvgm`, please refer to your
LaTeX distributions documentation (or the documentation of your
operating system, if `dvisvgm` was installed as a system package).


Second, check whether your `dvisvgm` supports PostScript specials. This is
needed to convert from PDF to SVG. Run:



```
dvisvgm -l

```


If the output to this command does **not** contain `ps  dvips PostScript specials`,
this is a bad sign. In this case, run



```
dvisvgm -h

```


If the output does **not** contain `--libgs=filename`, this means your
`dvisvgm` does not currently support PostScript. You must get another binary.


If, however, `--libgs=filename` appears in the help, that means that your
`dvisvgm` needs the Ghostscript library to support PostScript. Search for
`libgs.so` (on Linux, probably in `/usr/local/lib` or `/usr/lib`) or
`gsdll32.dll` (on 32\-bit Windows, probably in `C:\windows\system32`) or
`gsdll64.dll` (on 64\-bit Windows, also probably in `C:\windows\system32`)
or `libgsl.dylib` (on MacOS, probably in `/usr/local/lib` or
`/opt/local/lib`). Please look carefully, as the file might be located
elsewhere, e.g. in the directory where Ghostscript is installed.


When you have found the library, try (on MacOS or Linux)



```
export LIBGS=<path to your library including the file name>
dvisvgm -l

```


or (on Windows)



```
set LIBGS=<path to your library including the file name>
dvisvgm -l

```


You should now see `ps    dvips PostScript specials` in the output. Refer to
your operating system’s documentation to find out how you can set or export the
environment variable `LIBGS` automatically whenever you open a shell.


As a last check, you can run



```
dvisvgm -V1

```


(while still having `LIBGS` set to the correct path, of course.) If `dvisvgm`
can find your Ghostscript installation, it will be shown in the output together
with the version number.


If you do not have the necessary library on your system, please refer to your
operating system’s documentation to find out where you can get it and how you
have to install it.


If you are unable to solve your problem, check out the
[dvisvgm FAQ](https://dvisvgm.de/FAQ/).





---



## Where can I find more resources for learning Manim?[¶](#where-can-i-find-more-resources-for-learning-manim "Link to this heading")


In our [Discord server](https://manim.community/discord), we have the community\-maintained
`#beginner-resources` channel in which links to helpful learning resources are collected.
You are welcome to join our Discord and take a look yourself! If you have found some
guides or tutorials yourself that are not on our list yet, feel free to add them!






---

# Rendering Text and Formulas



# Rendering Text and Formulas[¶](#rendering-text-and-formulas "Link to this heading")


There are two different ways by which you can render **Text** in videos:


1. Using Pango ([`text_mobject`](../reference/manim.mobject.text.text_mobject.html#module-manim.mobject.text.text_mobject "manim.mobject.text.text_mobject"))
2. Using LaTeX ([`tex_mobject`](../reference/manim.mobject.text.tex_mobject.html#module-manim.mobject.text.tex_mobject "manim.mobject.text.tex_mobject"))


If you want to render simple text, you should use either [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or
[`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText"), or one of its derivatives like [`Paragraph`](../reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph").
See [Text Without LaTeX](#using-text-objects) for more information.


LaTeX should be used when you need mathematical typesetting. See
[Text With LaTeX](#rendering-with-latex) for more information.



## Text Without LaTeX[¶](#text-without-latex "Link to this heading")


The simplest way to add text to your animations is to use the [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")
class. It uses the [Pango library](https://pango.gnome.org) to render text. With Pango, you can also
render non\-English alphabets like 你好 or こんにちは or 안녕하세요 or
مرحبا بالعالم.


Here is a simple *Hello World* animation.



Example: HelloWorld [¶](#helloworld)

![../_images/HelloWorld-1.png](../_images/HelloWorld-1.png)

```
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)

```



```

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)


```
References: [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")


You can also use [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") which allows the use of PangoMarkup
(see the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") for details) to render text.
For example:



Example: SingleLineColor [¶](#singlelinecolor)

![../_images/SingleLineColor-1.png](../_images/SingleLineColor-1.png)

```
from manim import *

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)

```



```

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red except this', color=RED
        )
        self.add(text)


```
References: [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText")



### Working with [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")[¶](#working-with-text "Link to this heading")


This section explains the properties of [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") and how can it be used
in your animations.



#### Using Fonts[¶](#using-fonts "Link to this heading")


You can set a different font using `font`.



Note


The font used must be installed in your system, and Pango should know
about it. You can get a list of fonts using `manimpango.list_fonts()`.



```
>>> import manimpango
>>> manimpango.list_fonts()
[...]

```




Example: FontsExample [¶](#fontsexample)

![../_images/FontsExample-1.png](../_images/FontsExample-1.png)

```
from manim import *

class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)

```



```

class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)


```


#### Setting Slant and Weight[¶](#setting-slant-and-weight "Link to this heading")


Slant is the style of the Text, and it can be `NORMAL` (the default),
`ITALIC` or `OBLIQUE`. Usually, for many fonts both `ITALIC` and
`OBLIQUE` look similar, but `ITALIC` uses **Roman Style**, whereas
`OBLIQUE` uses **Italic Style**.


Weight specifies the boldness of a font. You can see a list of weights in
`manimpango.Weight`.



Example: SlantsExample [¶](#slantsexample)

![../_images/SlantsExample-1.png](../_images/SlantsExample-1.png)

```
from manim import *

class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)

```



```

class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)


```

Example: DifferentWeight [¶](#differentweight)

![../_images/DifferentWeight-1.png](../_images/DifferentWeight-1.png)

```
from manim import *

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))

```



```

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))


```


#### Using Colors[¶](#using-colors "Link to this heading")


You can set the color of the text using `color`:



Example: SimpleColor [¶](#simplecolor)

![../_images/SimpleColor-1.png](../_images/SimpleColor-1.png)

```
from manim import *

class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)

```



```

class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)


```
You can use utilities like `t2c` for coloring specific characters.
This may be problematic if your text contains ligatures
as explained in [Iterating Text](#iterating-text).


`t2c` accepts two types of dictionaries,


* The keys can contain indices like `[2:-1]` or `[4:8]`,
this works similar to how [slicing](https://realpython.com/python-strings/#string-slicing)
works in Python. The values should be the color of the Text from `Color`.
* The keys contain words or characters which should be colored separately
and the values should be the color from `Color`:



Example: Textt2cExample [¶](#textt2cexample)

![../_images/Textt2cExample-1.png](../_images/Textt2cExample-1.png)

```
from manim import *

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)

```



```

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)


```
If you want to avoid problems when using colors (due to ligatures), consider using
`MarkupText`.




#### Using Gradients[¶](#using-gradients "Link to this heading")


You can add a gradient using `gradient`. The value must
be an iterable of any length:



Example: GradientExample [¶](#gradientexample)

![../_images/GradientExample-1.png](../_images/GradientExample-1.png)

```
from manim import *

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)

```



```

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)


```
You can also use `t2g` for gradients with specific
characters of the text. It shares a similar syntax to [the
interface for colors](#using-colors):



Example: t2gExample [¶](#t2gexample)

![../_images/t2gExample-1.png](../_images/t2gExample-1.png)

```
from manim import *

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)

```



```

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)


```


#### Setting Line Spacing[¶](#setting-line-spacing "Link to this heading")


You can set the line spacing using `line_spacing`:



Example: LineSpacing [¶](#linespacing)

![../_images/LineSpacing-1.png](../_images/LineSpacing-1.png)

```
from manim import *

class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorld", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))

```



```

class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorld", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))


```


#### Disabling Ligatures[¶](#disabling-ligatures "Link to this heading")


By disabling ligatures you would get a one\-to\-one mapping between characters and
submobjects. This fixes the issues with coloring text.



Warning


Be aware that using this method with text that heavily depends on
ligatures (Arabic text) may yield unexpected results.



You can disable ligatures by passing `disable_ligatures` to
`Text`. For example:



Example: DisableLigature [¶](#disableligature)

![../_images/DisableLigature-1.png](../_images/DisableLigature-1.png)

```
from manim import *

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))

```



```

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))


```


#### Iterating [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")[¶](#iterating-text "Link to this heading")


Text objects behave like [`VGroups`](../reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"). Therefore, you can slice and index
the text.


For example, you can set each letter to different color by iterating it.



Example: IterateColor [¶](#iteratecolor)

![../_images/IterateColor-1.png](../_images/IterateColor-1.png)

```
from manim import *

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)

```



```

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)


```

Warning


Please note that [Ligature](https://en.wikipedia.org/wiki/Ligature_(writing)) can cause problems here. If you need a
one\-to\-one mapping of characters to submobjects you should pass
the `disable_ligatures` parameter to [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text").
See [Disabling Ligatures](#disable-ligatures).






### Working with [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText")[¶](#working-with-markuptext "Link to this heading")


MarkupText is similar to [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"), the only difference between them is
that this accepts and processes PangoMarkup (which is similar to
html), instead of just rendering plain text.


Consult the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") for more details
and further references about PangoMarkup.



Example: MarkupTest [¶](#markuptest)

![../_images/MarkupTest-1.png](../_images/MarkupTest-1.png)

```
from manim import *

class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)

```



```

class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'double green underline in red text except this',
            color=RED,
            font_size=34
        )
        self.add(text)


```



## Text With LaTeX[¶](#text-with-latex "Link to this heading")


Just as you can use [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") to add text to your videos, you can
use [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") to insert LaTeX.


For example,



Example: HelloLaTeX [¶](#hellolatex)

![../_images/HelloLaTeX-1.png](../_images/HelloLaTeX-1.png)

```
from manim import *

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)

```



```

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)


```

Note


Note that we are using a raw string (`r'...'`) instead of a regular string (`'...'`).
This is because TeX code uses a lot of special characters \- like `\` for example \- that
have special meaning within a regular python string. An alternative would have been to
write `\\` to escape the backslash: `Tex('\\LaTeX')`.




### Working with [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")[¶](#working-with-mathtex "Link to this heading")


Everything passed to [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") is in math mode by default. To be more precise,
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") is processed within an `align*` environment. You can achieve a
similar effect with [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") by enclosing your formula with `$` symbols:
`$\xrightarrow{x^6y^8}$`:



Example: MathTeXDemo [¶](#mathtexdemo)

![../_images/MathTeXDemo-1.png](../_images/MathTeXDemo-1.png)

```
from manim import *

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

```



```

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))


```


### LaTeX commands and keyword arguments[¶](#latex-commands-and-keyword-arguments "Link to this heading")


We can use any standard LaTeX commands in the AMS maths packages. Such
as the `mathtt` math\-text type or the `looparrowright` arrow.



Example: AMSLaTeX [¶](#amslatex)

![../_images/AMSLaTeX-1.png](../_images/AMSLaTeX-1.png)

```
from manim import *

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)

```



```

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


```
On the Manim side, the [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") class also accepts attributes to
change the appearance of the output. This is very similar to the
[`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") class. For example, the `color` keyword changes the
color of the TeX mobject.



Example: LaTeXAttributes [¶](#latexattributes)

![../_images/LaTeXAttributes-1.png](../_images/LaTeXAttributes-1.png)

```
from manim import *

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)

```



```

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)


```


### Extra LaTeX Packages[¶](#extra-latex-packages "Link to this heading")


Some commands require special packages to be loaded into the TeX template.
For example, to use the `mathscr` script, we need to add the `mathrsfs`
package. Since this package isn’t loaded into Manim’s tex template by default,
we have to add it manually.



Example: AddPackageLatex [¶](#addpackagelatex)

![../_images/AddPackageLatex-1.png](../_images/AddPackageLatex-1.png)

```
from manim import *

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)

```



```

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)


```


### Substrings and parts[¶](#substrings-and-parts "Link to this heading")


The TeX mobject can accept multiple strings as arguments. Afterwards you can
refer to the individual parts either by their index (like `tex[1]`), or by
selecting parts of the tex code. In this example, we set the color
of the `\bigstar` using `set_color_by_tex()`:



Example: LaTeXSubstrings [¶](#latexsubstrings)

![../_images/LaTeXSubstrings-1.png](../_images/LaTeXSubstrings-1.png)

```
from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)

```



```

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)


```
Note that `set_color_by_tex()` colors the entire substring containing
the Tex, not just the specific symbol or Tex expression. Consider the following example:



Example: IncorrectLaTeXSubstringColoring [¶](#incorrectlatexsubstringcoloring)

![../_images/IncorrectLaTeXSubstringColoring-1.png](../_images/IncorrectLaTeXSubstringColoring-1.png)

```
from manim import *

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

```



```

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)


```
As you can see, this colors the entire equation yellow, contrary to what
may be expected. To color only `x` yellow, we have to do the following:



Example: CorrectLaTeXSubstringColoring [¶](#correctlatexsubstringcoloring)

![../_images/CorrectLaTeXSubstringColoring-1.png](../_images/CorrectLaTeXSubstringColoring-1.png)

```
from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

```



```

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)


```
By setting `substrings_to_isolate` to `x`, we split up the
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") into substrings automatically and isolate the `x` components
into individual substrings. Only then can `set_color_by_tex()` be used
to achieve the desired result.


Note that Manim also supports a custom syntax that allows splitting
a TeX string into substrings easily: simply enclose parts of your formula
that you want to isolate with double braces. In the string
`MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")`, the rendered mobject
will consist of the substrings `a^2`, `+`, `b^2`, `=`, and `c^2`.
This makes transformations between similar text fragments easy
to write using [`TransformMatchingTex`](../reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex "manim.animation.transform_matching_parts.TransformMatchingTex").




### Using `index_labels` to work with complicated strings[¶](#using-index-labels-to-work-with-complicated-strings "Link to this heading")


You might sometimes be working with a very complicated [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") mobject
that makes it difficult to work with its individual components. This is
where the debugging function [`index_labels()`](../reference/manim.utils.debug.html#manim.utils.debug.index_labels "manim.utils.debug.index_labels") is very useful.


The method shows the index of a mobject’s submobjects, allowing you
to easily find the components of the mobject you would like to change.



Example: IndexLabelsMathTex [¶](#indexlabelsmathtex)

![../_images/IndexLabelsMathTex-1.png](../_images/IndexLabelsMathTex-1.png)

```
from manim import *

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)

```



```

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)


```


### LaTeX Maths Fonts \- The Template Library[¶](#latex-maths-fonts-the-template-library "Link to this heading")


Changing fonts in LaTeX when typesetting mathematical formulae is
trickier than regular text. It requires changing the template that is used
to compile the TeX. Manim comes with a collection of [`TexFontTemplates`](../reference/manim.utils.tex_templates.TexFontTemplates.html#manim.utils.tex_templates.TexFontTemplates "manim.utils.tex_templates.TexFontTemplates")
ready for you to use. These templates will all work in math mode:



Example: LaTeXMathFonts [¶](#latexmathfonts)

![../_images/LaTeXMathFonts-1.png](../_images/LaTeXMathFonts-1.png)

```
from manim import *

class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)

```



```

class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)


```
Manim also has a [`TexTemplateLibrary`](../reference/manim.utils.tex_templates.TexTemplateLibrary.html#manim.utils.tex_templates.TexTemplateLibrary "manim.utils.tex_templates.TexTemplateLibrary") containing the TeX
templates used by 3Blue1Brown. One example is the ctex template,
used for typesetting Chinese script. For this to work, the ctex LaTeX package
must be installed on your system. Furthermore, if you are only
typesetting Text, you probably do not need [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") at all, and
should use [`Text`](../reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") instead.



Example: LaTeXTemplateLibrary [¶](#latextemplatelibrary)

![../_images/LaTeXTemplateLibrary-1.png](../_images/LaTeXTemplateLibrary-1.png)

```
from manim import *

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)

```



```

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)


```


### Aligning formulae[¶](#aligning-formulae "Link to this heading")


[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") mobject is typeset in the LaTeX `align*`
environment. This means you can use the `&` alignment character
when typesetting multiline formulae:



Example: LaTeXAlignEnvironment [¶](#latexalignenvironment)

![../_images/LaTeXAlignEnvironment-1.png](../_images/LaTeXAlignEnvironment-1.png)

```
from manim import *

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)

```



```

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)


```





---

# Manim’s building blocks



# Manim’s building blocks[¶](#manim-s-building-blocks "Link to this heading")


This document explains the building blocks of manim and will give you all the
necessary tools to start producing your own videos.


Essentially, manim puts at your disposal three different concepts that you can
orchestrate together to produce mathematical animations: the
**mathematical object** (or **mobject** for short), the **animation**, and the
**scene**. As we will see in the following sections, each of these three
concepts is implemented in manim as a separate class: the [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"),
[`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"), and [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") classes.



Note


It is recommended that you read the tutorials [Quickstart](quickstart.html) and
[Manim’s Output Settings](output_and_config.html) before reading this page.




## Mobjects[¶](#mobjects "Link to this heading")


Mobjects are the basic building blocks for all manim animations. Each class
that derives from [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") represents an object that can be displayed
on the screen. For example, simple shapes such as [`Circle`](../reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle"),
[`Arrow`](../reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow"), and [`Rectangle`](../reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") are all mobjects. More complicated
constructs such as [`Axes`](../reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"), [`FunctionGraph`](../reference/manim.mobject.graphing.functions.FunctionGraph.html#manim.mobject.graphing.functions.FunctionGraph "manim.mobject.graphing.functions.FunctionGraph"), or
[`BarChart`](../reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart") are mobjects as well.


If you try to display an instance of [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") on the screen, you will only
see an empty frame. The reason is that the [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class is an
abstract base class of all other mobjects, i.e. it does not have any
pre\-determined visual shape that can be displayed on the screen. It is only the
skeleton of a thing that *could* be displayed. Therefore, you will rarely need
to use plain instances of [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"); instead, you will most likely
create instances of its derived classes. One of these derived classes is
[`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). The `V` stands for Vectorized Mobject. In essence, a
vmobject is a mobject that uses [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) to be displayed. Most of
the time, you will be dealing with vmobjects, though we will continue to use
the term “mobject” to refer to the class of shapes that can be displayed on the
screen, as it is more general.



Note


Any object that can be displayed on the screen is a `mobject`, even if
it is not necessarily *mathematical* in nature.




Tip


To see examples of classes derived from [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), see the
[`geometry`](../reference/manim.mobject.geometry.html#module-manim.mobject.geometry "manim.mobject.geometry") module. Most of these are in fact derived from
[`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") as well.




### Creating and displaying mobjects[¶](#creating-and-displaying-mobjects "Link to this heading")


As explained in [Quickstart](quickstart.html), usually all of the code in a manim
script is put inside the [`construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method of a [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") class.
To display a mobject on the screen, call the [`add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") method of the
containing [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene"). This is the principal way of displaying a mobject
on the screen when it is not being animated. To remove a mobject from the
screen, simply call the [`remove()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") method from the containing
[`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene").



Example: CreatingMobjects [¶](#creatingmobjects)



```
from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

```



```

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)


```


### Placing mobjects[¶](#placing-mobjects "Link to this heading")


Let’s define a new [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") called `Shapes` and [`add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add")
some mobjects to it. This script generates a static picture that displays a
circle, a square, and a triangle:



Example: Shapes [¶](#shapes)



```
from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)

```



```

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


```
By default, mobjects are placed at the center of coordinates, or *origin*, when
they are first created. They are also given some default colors. Further, the
`Shapes` scene places the mobjects by using the [`shift()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shift "manim.mobject.mobject.Mobject.shift") method. The
square is shifted one unit in the `UP` direction from the origin, while the
circle and triangle are shifted one unit `LEFT` and `RIGHT`, respectively.



Attention


Unlike other graphics software, manim places the center of
coordinates at the center of the screen. The positive vertical
direction is up, and the positive horizontal direction is right.
See also the constants `ORIGIN`, `UP`, `DOWN`, `LEFT`,
`RIGHT`, and others, defined in the [`constants`](../reference/manim.constants.html#module-manim.constants "manim.constants") module.



There are many other possible ways to place mobjects on the screen, for example
[`move_to()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to"), [`next_to()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.next_to "manim.mobject.mobject.Mobject.next_to"), and [`align_to()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_to "manim.mobject.mobject.Mobject.align_to"). The next scene
`MobjectPlacement` uses all three.



Example: MobjectPlacement [¶](#mobjectplacement)



```
from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)

```



```

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)


```
The [`move_to()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to") method uses absolute units (measured relative to the
`ORIGIN`), while [`next_to()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.next_to "manim.mobject.mobject.Mobject.next_to") uses relative units (measured from the
mobject passed as the first argument). `align_to()` uses `LEFT` not as
measuring units but as a way to determine the border to use for alignment. The
coordinates of the borders of a mobject are determined using an imaginary
bounding box around it.



Tip


Many methods in manim can be chained together. For example the two
lines



```
square = Square()
square.shift(LEFT)

```


can be replaced by



```
square = Square().shift(LEFT)

```


Technically, this is possible because most methods calls return the modified mobject.





### Styling mobjects[¶](#styling-mobjects "Link to this heading")


The following scene changes the default aesthetics of the mobjects.



Example: MobjectStyling [¶](#mobjectstyling)



```
from manim import *

class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)

```



```

class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)


```
This scene uses two of the main functions that change the visual style of a
mobject: `set_stroke()` and [`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_fill "manim.mobject.types.vectorized_mobject.VMobject.set_fill"). The former changes the
visual style of the mobject’s border while the latter changes the style of the
interior. By default, most mobjects have a fully transparent interior so you
must specify the `opacity` parameter to display the color. An
opacity of `1.0` means fully opaque, while `0.0` means fully transparent.


Only instances of [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") implement `set_stroke()` and
[`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_fill "manim.mobject.types.vectorized_mobject.VMobject.set_fill"). Instances of [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") implement
`set_color()` instead. The vast majority of pre\-defined classes
are derived from [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") so it is usually safe to assume that you
have access to `set_stroke()` and [`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_fill "manim.mobject.types.vectorized_mobject.VMobject.set_fill").




### Mobject on\-screen order[¶](#mobject-on-screen-order "Link to this heading")


The next scene is exactly the same as the `MobjectStyling` scene from the
previous section, except for exactly one line.



Example: MobjectZOrder [¶](#mobjectzorder)



```
from manim import *

class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)

```



```

class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)


```
The only difference here (besides the scene name) is the order in which the
mobjects are added to the scene. In `MobjectStyling`, we added them as
`add(circle, square, triangle)`, whereas in `MobjectZOrder` we add them as
`add(triangle, square, circle)`.


As you can see, the order of the arguments of [`add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") determines
the order that the mobjects are displayed on the screen, with the left\-most
arguments being put in the back.





## Animations[¶](#animations "Link to this heading")


At the heart of manim is animation. Generally, you can add an animation to
your scene by calling the [`play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") method.



Example: SomeAnimations [¶](#someanimations)



```
from manim import *

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)

```



```

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)


```
Put simply, animations are procedures that interpolate between two mobjects.
For example, `FadeIn(square)` starts with a fully transparent version of
`square` and ends with a fully opaque version, interpolating between them
by gradually increasing the opacity. [`FadeOut`](../reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut") works in the opposite
way: it interpolates from fully opaque to fully transparent. As another
example, [`Rotate`](../reference/manim.animation.rotation.Rotate.html#manim.animation.rotation.Rotate "manim.animation.rotation.Rotate") starts with the mobject passed to it as argument, and
ends with the same object but rotated by a certain amount, this time
interpolating the mobject’s angle instead of its opacity.



### Animating methods[¶](#animating-methods "Link to this heading")


Any property of a mobject that can be changed can be animated. In fact, any
method that changes a mobject’s property can be used as an animation, through
the use of [`animate()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate").



Example: AnimateExample [¶](#animateexample)



```
from manim import *

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)

```



```

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)


```
References: [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


[`animate()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") is a property of all mobjects that animates the methods that come
afterward. For example, `square.set_fill(WHITE)` sets the fill color of
the square, while `square.animate.set_fill(WHITE)` animates this action.




### Animation run time[¶](#animation-run-time "Link to this heading")


By default, any animation passed to `play()` lasts for exactly one second.
Use the `run_time` argument to control the duration.



Example: RunTime [¶](#runtime)



```
from manim import *

class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)

```



```

class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)


```


### Creating a custom animation[¶](#creating-a-custom-animation "Link to this heading")


Even though Manim has many built\-in animations, you will find times when you need to smoothly animate from one state of a [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to another.
If you find yourself in that situation, then you can define your own custom animation.
You start by extending the [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") class and overriding its [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject").
The [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") method receives alpha as a parameter that starts at 0 and changes throughout the animation.
So, you just have to manipulate self.mobject inside Animation according to the alpha value in its interpolate\_mobject method.
Then you get all the benefits of [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") such as playing it for different run times or using different rate functions.


Let’s say you start with a number and want to create a [`Transform`](../reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") animation that transforms it to a target number.
You can do it using [`FadeTransform`](../reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform"), which will fade out the starting number and fade in the target number.
But when we think about transforming a number from one to another, an intuitive way of doing it is by incrementing or decrementing it smoothly.
Manim has a feature that allows you to customize this behavior by defining your own custom animation.


You can start by creating your own `Count` class that extends [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").
The class can have a constructor with three arguments, a [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") Mobject, start, and end.
The constructor will pass the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") Mobject to the super constructor (in this case, the [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") constructor) and will set start and end.


The only thing that you need to do is to define how you want it to look at every step of the animation.
Manim provides you with the alpha value in the [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") method based on frame rate of video, rate function, and run time of animation played.
The alpha parameter holds a value between 0 and 1 representing the step of the currently playing animation.
For example, 0 means the beginning of the animation, 0\.5 means halfway through the animation, and 1 means the end of the animation.


In the case of the `Count` animation, you just have to figure out a way to determine the number to display at the given alpha value and then set that value in the [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") method of the `Count` animation.
Suppose you are starting at 50 and incrementing until the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") reaches 100 at the end of the animation.


* If alpha is 0, you want the value to be 50\.
* If alpha is 0\.5, you want the value to be 75\.
* If alpha is 1, you want the value to be 100\.


Generally, you start with the starting number and add only some part of the value to be increment according to the alpha value.
So, the logic of calculating the number to display at each step will be `50 + alpha * (100 - 50)`.
Once you set the calculated value for the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"), you are done.


Once you have defined your `Count` animation, you can play it in your [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") for any duration you want for any [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") with any rate function.



Example: CountingScene [¶](#countingscene)



```
from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()

```



```

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()


```
References: [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") [`play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play")




### Using coordinates of a mobject[¶](#using-coordinates-of-a-mobject "Link to this heading")


Mobjects contain points that define their boundaries.
These points can be used to add other mobjects respectively to each other,
e.g. by methods like [`get_center()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_center "manim.mobject.mobject.Mobject.get_center") , [`get_top()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_top "manim.mobject.mobject.Mobject.get_top")
and [`get_start()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start "manim.mobject.mobject.Mobject.get_start"). Here is an example of some important coordinates:



Example: MobjectExample [¶](#mobjectexample)

![../_images/MobjectExample-1.png](../_images/MobjectExample-1.png)

```
from manim import *

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

```



```

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)


```


### Transforming mobjects into other mobjects[¶](#transforming-mobjects-into-other-mobjects "Link to this heading")


It is also possible to transform a mobject into another mobject like this:



Example: ExampleTransform [¶](#exampletransform)



```
from manim import *

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))

```



```

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))


```
The Transform function maps points of the previous mobject to the points of the
next mobject.
This might result in strange behaviour, e.g. when the dots of one mobject are
arranged clockwise and the other points are arranged counterclockwise.
Here it might help to use the flip function and reposition the points via the
[roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html)
function of numpy:



Example: ExampleRotation [¶](#examplerotation)



```
from manim import *

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)

```



```

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)


```



## Scenes[¶](#scenes "Link to this heading")


The [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") class is the connective tissue of manim. Every mobject has
to be [`added`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") to a scene to be displayed, or [`removed`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") from it to cease being displayed. Every animation has to be
[`played`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") by a scene, and every time interval where no
animation occurs is determined by a call to [`wait()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait"). All of the
code of your video must be contained in the [`construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method of
a class that derives from [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene"). Finally, a single file may contain
multiple [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") subclasses if multiple scenes are to be
rendered at the same time.






---

# A deep dive into Manim’s internals



# A deep dive into Manim’s internals[¶](#a-deep-dive-into-manim-s-internals "Link to this heading")


**Author:** [Benjamin Hackl](https://benjamin-hackl.at)



Disclaimer


This guide reflects the state of the library as of version `v0.16.0`
and primarily treats the Cairo renderer. The situation in the latest
version of Manim might be different; in case of substantial deviations
we will add a note below.




## Introduction[¶](#introduction "Link to this heading")


Manim can be a wonderful library, if it behaves the way you would like it to,
and/or the way you expect it to. Unfortunately, this is not always the case
(as you probably know if you have played with some manimations yourself already).
To understand where things *go wrong*, digging through the library’s source code
is sometimes the only option – but in order to do that, you need to know where
to start digging.


This article is intended as some sort of life line through the render process.
We aim to give an appropriate amount of detail describing what happens when
Manim reads your scene code and produces the corresponding animation. Throughout
this article, we will focus on the following toy example:



```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))

```


Before we go into details or even look at the rendered output of this scene,
let us first describe verbally what happens in this *manimation*. In the first
three lines of the `construct` method, a [`Square`](../reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square") and a [`Circle`](../reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")
are initialized, then the square is added to the scene. The first frame of the
rendered output should thus show an orange square.


Then the actual animations happen: the square first transforms into a circle,
then a [`Dot`](../reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") is created (Where do you guess the dot is located when
it is first added to the scene? Answering this already requires detailed
knowledge about the render process.). The dot has an updater attached to it, and
as the circle moves right, the dot moves with it. In the end, all mobjects are
faded out.


Actually rendering the code yields the following video:



For this example, the output (fortunately) coincides with our expectations.




## Overview[¶](#overview "Link to this heading")


Because there is a lot of information in this article, here is a brief overview
discussing the contents of the following chapters on a very high level.


* [Preliminaries](#preliminaries): In this chapter we unravel all the steps that take place
to prepare a scene for rendering; right until the point where the user\-overridden
`construct` method is ran. This includes a brief discussion on using Manim’s CLI
versus other means of rendering (e.g., via Jupyter notebooks, or in your Python
script by calling the [`Scene.render()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render") method yourself).
* [Mobject Initialization](#mobject-initialization): For the second chapter we dive into creating and handling
Mobjects, the basic elements that should be displayed in our scene.
We discuss the [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") base class, how there are essentially
three different types of Mobjects, and then discuss the most important of them,
vectorized Mobjects. In particular, we describe the internal point data structure
that governs how the mechanism responsible for drawing the vectorized Mobject
to the screen sets the corresponding Bézier curves. We conclude the chapter
with a tour into [`Scene.add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add"), the bookkeeping mechanism controlling which
mobjects should be rendered.
* [Animations and the Render Loop](#animations-and-the-render-loop): And finally, in the last chapter we walk
through the instantiation of [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects (the blueprints that
hold information on how Mobjects should be modified when the render loop runs),
followed by a investigation of the infamous [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call. We will
see that there are three relevant parts in a [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call;
a part in which the passed animations and keyword arguments are processed
and prepared, followed by the actual “render loop” in which the library
steps through a time line and renders frame by frame. The final part
does some post\-processing to save a short video segment (“partial movie file”)
and cleanup for the next call to [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play"). In the end, after all of
[`Scene.construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") has been run, the library combines the partial movie
files to one video.


And with that, let us get *in medias res*.




## Preliminaries[¶](#preliminaries "Link to this heading")



### Importing the library[¶](#importing-the-library "Link to this heading")


Independent of how exactly you are telling your system
to render the scene, i.e., whether you run `manim -qm -p file_name.py ToyExample`, or
whether you are rendering the scene directly from the Python script via a snippet
like



```
with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ToyExample()
    scene.render()

```


or whether you are rendering the code in a Jupyter notebook, you are still telling your
python interpreter to import the library. The usual pattern used to do this is



```
from manim import *

```


which (while being a debatable strategy in general) imports a lot of classes and
functions shipped with the library and makes them available in your global name space.
I explicitly avoided stating that it imports **all** classes and functions of the
library, because it does not do that: Manim makes use of the practice described
in [Section 6\.4\.1 of the Python tutorial](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package),
and all module members that should be exposed to the user upon running the `*`\-import
are explicitly declared in the `__all__` variable of the module.


Manim also uses this strategy internally: taking a peek at the file that is run when
the import is called, `__init__.py` (see
[here](https://github.com/ManimCommunity/manim/blob/main/manim/__init__.py)),
you will notice that most of the code in that module is concerned with importing
members from various different submodules, again using `*`\-imports.



Hint


If you would ever contribute a new submodule to Manim, the main
`__init__.py` is where it would have to be listed in order to make its
members accessible to users after importing the library.



In that file, there is one particular import at the beginning of the file however,
namely:



```
from ._config import *

```


This initializes Manim’s global configuration system, which is used in various places
throughout the library. After the library runs this line, the current configuration
options are set. The code in there takes care of reading the options in your `.cfg`
files (all users have at least the global one that is shipped with the library)
as well as correctly handling command line arguments (if you used the CLI to render).


You can read more about the config system in the
[corresponding thematic guide](configuration.html), and if you are interested in learning
more about the internals of the configuration system and how it is initialized,
follow the code flow starting in [the config module’s init file](https://github.com/ManimCommunity/manim/blob/main/manim/_config/__init__.py).


Now that the library is imported, we can turn our attention to the next step:
reading your scene code (which is not particularly exciting, Python just creates
a new class `ToyExample` based on our code; Manim is virtually not involved
in that step, with the exception that `ToyExample` inherits from `Scene`).


However, with the `ToyExample` class created and ready to go, there is a new
excellent question to answer: how is the code in our `construct` method
actually executed?




### Scene instantiation and rendering[¶](#scene-instantiation-and-rendering "Link to this heading")


The answer to this question depends on how exactly you are running the code.
To make things a bit clearer, let us first consider the case that you
have created a file `toy_example.py` which looks like this:



```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))

with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ToyExample()
    scene.render()

```


With such a file, the desired scene is rendered by simply running this Python
script via `python toy_example.py`. Then, as described above, the library
is imported and Python has read and defined the `ToyExample` class (but,
read carefully: *no instance of this class has been created yet*).


At this point, the interpreter is about to enter the `tempconfig` context
manager. Even if you have not seen Manim’s `tempconfig` before, its name
already suggests what it does: it creates a copy of the current state of the
configuration, applies the changes to the key\-value pairs in the passed
dictionary, and upon leaving the context the original version of the
configuration is restored. TL;DR: it provides a fancy way of temporarily setting
configuration options.


Inside the context manager, two things happen: an actual `ToyExample`\-scene
object is instantiated, and the `render` method is called. Every way of using
Manim ultimately does something along of these lines, the library always instantiates
the scene object and then calls its `render` method. To illustrate that this
really is the case, let us briefly look at the two most common ways of rendering
scenes:


**Command Line Interface.** When using the CLI and running the command
`manim -qm -p toy_example.py ToyExample` in your terminal, the actual
entry point is Manim’s `__main__.py` file (located
[here](https://github.com/ManimCommunity/manim/blob/main/manim/__main__.py).
Manim uses [Click](https://click.palletsprojects.com/en/8.0.x/) to implement
the command line interface, and the corresponding code is located in Manim’s
`cli` module (<https://github.com/ManimCommunity/manim/tree/main/manim/cli>).
The corresponding code creating the scene class and calling its render method
is located [here](https://github.com/ManimCommunity/manim/blob/ac1ee9a683ce8b92233407351c681f7d71a4f2db/manim/cli/render/commands.py#L139-L141).


**Jupyter notebooks.** In Jupyter notebooks, the communication with the library
is handled by the `%%manim` magic command, which is implemented in the
`manim.utils.ipython_magic` module. There is
[`some documentation`](../reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic.manim "manim.utils.ipython_magic.ManimMagic.manim") available for the magic command,
and the code creating the scene class and calling its render method is located
[here](https://github.com/ManimCommunity/manim/blob/ac1ee9a683ce8b92233407351c681f7d71a4f2db/manim/utils/ipython_magic.py#L137-L138).


Now that we know that either way, a [`Scene`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") object is created, let us investigate
what Manim does when that happens. When instantiating our scene object



```
scene = ToyExample()

```


the `Scene.__init__` method is called, given that we did not implement our own initialization
method. Inspecting the corresponding code (see
[here](https://github.com/ManimCommunity/manim/blob/main/manim/scene/scene.py))
reveals that `Scene.__init__` first sets several attributes of the scene objects that do not
depend on any configuration options set in `config`. Then the scene inspects the value of
`config.renderer`, and based on its value, either instantiates a `CairoRenderer` or an
`OpenGLRenderer` object and assigns it to its `renderer` attribute.


The scene then asks its renderer to initialize the scene by calling



```
self.renderer.init_scene(self)

```


Inspecting both the default Cairo renderer and the OpenGL renderer shows that the `init_scene`
method effectively makes the renderer instantiate a [`SceneFileWriter`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") object, which
basically is Manim’s interface to `ffmpeg` and actually writes the movie file. The Cairo
renderer (see the implementation [here](https://github.com/ManimCommunity/manim/blob/main/manim/renderer/cairo_renderer.py)) does not require any further initialization. The OpenGL renderer
does some additional setup to enable the realtime rendering preview window, which we do not go
into detail further here.



Warning


Currently, there is a lot of interplay between a scene and its renderer. This is a flaw
in Manim’s current architecture, and we are working on reducing this interdependency to
achieve a less convoluted code flow.



After the renderer has been instantiated and initialized its file writer, the scene populates
further initial attributes (notable mention: the `mobjects` attribute which keeps track
of the mobjects that have been added to the scene). It is then done with its instantiation
and ready to be rendered.


The rest of this article is concerned with the last line in our toy example script:



```
scene.render()

```


This is where the actual magic happens.


Inspecting the [implementation of the render method](https://github.com/ManimCommunity/manim/blob/df1a60421ea1119cbbbd143ef288d294851baaac/manim/scene/scene.py#L211)
reveals that there are several hooks that can be used for pre\- or postprocessing
a scene. Unsurprisingly, [`Scene.render()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render") describes the full *render cycle*
of a scene. During this life cycle, there are three custom methods whose base
implementation is empty and that can be overwritten to suit your purposes. In
the order they are called, these customizable methods are:


* [`Scene.setup()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup"), which is intended for preparing and, well, *setting up*
the scene for your animation (e.g., adding initial mobjects, assigning custom
attributes to your scene class, etc.),
* [`Scene.construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct"), which is the *script* for your screen play and
contains programmatic descriptions of your animations, and
* [`Scene.tear_down()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down"), which is intended for any operations you might
want to run on the scene after the last frame has already been rendered
(for example, this could run some code that generates a custom thumbnail
for the video based on the state of the objects in the scene – this
hook is more relevant for situations where Manim is used within other
Python scripts).


After these three methods are run, the animations have been fully rendered,
and Manim calls `CairoRenderer.scene_finished()` to gracefully
complete the rendering process. This checks whether any animations have been
played – and if so, it tells the [`SceneFileWriter`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") to close the pipe
to `ffmpeg`. If not, Manim assumes that a static image should be output
which it then renders using the same strategy by calling the render loop
(see below) once.


**Back in our toy example,** the call to [`Scene.render()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render") first
triggers [`Scene.setup()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup") (which only consists of `pass`), followed by
a call of [`Scene.construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct"). At this point, our *animation script*
is run, starting with the initialization of `orange_square`.





## Mobject Initialization[¶](#mobject-initialization "Link to this heading")


Mobjects are, in a nutshell, the Python objects that represent all the
*things* we want to display in our scene. Before we follow our debugger
into the depths of mobject initialization code, it makes sense to
discuss Manim’s different types of Mobjects and their basic data
structure.



### What even is a Mobject?[¶](#what-even-is-a-mobject "Link to this heading")


[`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") stands for *mathematical object* or *Manim object*
(depends on who you ask 😄). The Python class [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") is
the base class for all objects that should be displayed on screen.
Looking at the [initialization method](https://github.com/ManimCommunity/manim/blob/5d72d9cfa2e3dd21c844b1da807576f5a7194fda/manim/mobject/mobject.py#L94)
of [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), you will find that not too much happens in there:


* some initial attribute values are assigned, like `name` (which makes the
render logs mention the name of the mobject instead of its type),
`submobjects` (initially an empty list), `color`, and some others.
* Then, two methods related to *points* are called: `reset_points`
followed by `generate_points`,
* and finally, `init_colors` is called.


Digging deeper, you will find that [`Mobject.reset_points()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.reset_points "manim.mobject.mobject.Mobject.reset_points") simply
sets the `points` attribute of the mobject to an empty NumPy vector,
while the other two methods, [`Mobject.generate_points()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.generate_points "manim.mobject.mobject.Mobject.generate_points") and
[`Mobject.init_colors()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.init_colors "manim.mobject.mobject.Mobject.init_colors") are just implemented as `pass`.


This makes sense: [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") is not supposed to be used as
an *actual* object that is displayed on screen; in fact the camera
(which we will discuss later in more detail; it is the class that is,
for the Cairo renderer, responsible for “taking a picture” of the
current scene) does not process “pure” [`Mobjects`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")
in any way, they *cannot* even appear in the rendered output.


This is where different types of mobjects come into play. Roughly
speaking, the Cairo renderer setup knows three different types of
mobjects that can be rendered:


* [`ImageMobject`](../reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject"), which represent images that you can display
in your scene,
* [`PMobject`](../reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject"), which are very special mobjects used to represent
point clouds; we will not discuss them further in this guide,
* [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"), which are *vectorized mobjects*, that is, mobjects
that consist of points that are connected via curves. These are pretty
much everywhere, and we will discuss them in detail in the next section.




### … and what are VMobjects?[¶](#and-what-are-vmobjects "Link to this heading")


As just mentioned, [`VMobjects`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") represent vectorized
mobjects. To render a [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"), the camera looks at the
`points` attribute of a [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") and divides it into sets
of four points each. Each of these sets is then used to construct a
cubic Bézier curve with the first and last entry describing the
end points of the curve (“anchors”), and the second and third entry
describing the control points in between (“handles”).



Hint


To learn more about Bézier curves, take a look at the excellent
online textbook [A Primer on Bézier curves](https://pomax.github.io/bezierinfo/)
by [Pomax](https://twitter.com/TheRealPomax) – there is a playground representing
cubic Bézier curves [in §1](https://pomax.github.io/bezierinfo/#introduction),
the red and yellow points are “anchors”, and the green and blue
points are “handles”.



In contrast to [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") can be displayed
on screen (even though, technically, it is still considered a base class).
To illustrate how points are processed, consider the following short example
of a [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with 8 points (and thus made out of 8/4 \= 2 cubic
Bézier curves). The resulting [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") is drawn in green.
The handles are drawn as red dots with a line to their closest anchor.



Example: VMobjectDemo [¶](#vmobjectdemo)

![../_images/VMobjectDemo-1.png](../_images/VMobjectDemo-1.png)

```
from manim import *

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve
            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)

```



```

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve
            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)


```

Warning


Manually setting the points of your [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") is usually
discouraged; there are specialized methods that can take care of
that for you – but it might be relevant when implementing your own,
custom [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").





### Squares and Circles: back to our Toy Example[¶](#squares-and-circles-back-to-our-toy-example "Link to this heading")


With a basic understanding of different types of mobjects,
and an idea of how vectorized mobjects are built we can now
come back to our toy example and the execution of the
[`Scene.construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method. In the first two lines
of our animation script, the `orange_square` and the
`blue_circle` are initialized.


When creating the orange square by running



```
Square(color=ORANGE, fill_opacity=0.5)

```


the initialization method of [`Square`](../reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square"),
`Square.__init__`, is called. [Looking at the
implementation](https://github.com/ManimCommunity/manim/blob/5d72d9cfa2e3dd21c844b1da807576f5a7194fda/manim/mobject/geometry/polygram.py#L607),
we can see that the `side_length` attribute of the square is set,
and then



```
super().__init__(height=side_length, width=side_length, **kwargs)

```


is called. This `super` call is the Python way of calling the
initialization function of the parent class. As [`Square`](../reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")
inherits from [`Rectangle`](../reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle"), the next method called
is `Rectangle.__init__`. There, only the first three lines
are really relevant for us:



```
super().__init__(UR, UL, DL, DR, color=color, **kwargs)
self.stretch_to_fit_width(width)
self.stretch_to_fit_height(height)

```


First, the initialization function of the parent class of
[`Rectangle`](../reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") – [`Polygon`](../reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") – is called. The
four positional arguments passed are the four corners of
the polygon: `UR` is up right (and equal to `UP + RIGHT`),
`UL` is up left (and equal to `UP + LEFT`), and so forth.
Before we follow our debugger deeper, let us observe what
happens with the constructed polygon: the remaining two lines
stretch the polygon to fit the specified width and height
such that a rectangle with the desired measurements is created.


The initialization function of [`Polygon`](../reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") is particularly
simple, it only calls the initialization function of its parent
class, [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"). There, we have almost reached the end
of the chain: [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") inherits from [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"),
whose initialization function mainly sets the values of some
attributes (quite similar to `Mobject.__init__`, but more specific
to the Bézier curves that make up the mobject).


After calling the initialization function of [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"),
the constructor of [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") also does something somewhat
odd: it sets the points (which, you might remember above, should
actually be set in a corresponding `generate_points` method
of [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")).



Warning


In several instances, the implementation of mobjects does
not really stick to all aspects of Manim’s interface. This
is unfortunate, and increasing consistency is something
that we actively work on. Help is welcome!



Without going too much into detail, [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") sets its
`points` attribute via `VMobject.start_new_path()`,
`VMobject.add_points_as_corners()`, which take care of
setting the quadruples of anchors and handles appropriately.
After the points are set, Python continues to process the
call stack until it reaches the method that was first called;
the initialization method of [`Square`](../reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square"). After this,
the square is initialized and assigned to the `orange_square`
variable.


The initialization of `blue_circle` is similar to the one of
`orange_square`, with the main difference being that the inheritance
chain of [`Circle`](../reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle") is different. Let us briefly follow the trace
of the debugger:


The implementation of `Circle.__init__()` immediately calls
the initialization method of [`Arc`](../reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc"), as a circle in Manim
is simply an arc with an angle of \\(\\tau \= 2\\pi\\). When
initializing the arc, some basic attributes are set (like
`Arc.radius`, `Arc.arc_center`, `Arc.start_angle`, and
`Arc.angle`), and then the initialization method of its
parent class, [`TipableVMobject`](../reference/manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject"), is called (which is
a rather abstract base class for mobjects which a arrow tip can
be attached to). Note that in contrast to [`Polygram`](../reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"),
this class does **not** preemptively generate the points of the circle.


After that, things are less exciting: [`TipableVMobject`](../reference/manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject") again
sets some attributes relevant for adding arrow tips, and afterwards
passes to the initialization method of [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). From there,
[`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") is initialized and [`Mobject.generate_points()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.generate_points "manim.mobject.mobject.Mobject.generate_points")
is called, which actually runs the method implemented in
[`Arc.generate_points()`](../reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc.generate_points "manim.mobject.geometry.arc.Arc.generate_points").


After both our `orange_square` and the `blue_circle` are initialized,
the square is actually added to the scene. The [`Scene.add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") method
is actually doing a few interesting things, so it is worth to dig a bit
deeper in the next section.




### Adding Mobjects to the Scene[¶](#adding-mobjects-to-the-scene "Link to this heading")


The code in our `construct` method that is run next is



```
self.add(orange_square)

```


From a high\-level point of view, [`Scene.add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") adds the
`orange_square` to the list of mobjects that should be rendered,
which is stored in the `mobjects` attribute of the scene. However,
it does so in a very careful way to avoid the situation that a mobject
is being added to the scene more than once. At a first glance, this
sounds like a simple task – the problem is that `Scene.mobjects`
is not a “flat” list of mobjects, but a list of mobjects which
might contain mobjects themselves, and so on.


Stepping through the code in [`Scene.add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add"), we see that first
it is checked whether we are currently using the OpenGL renderer
(which we are not) – adding mobjects to the scene works slightly
different (and actually easier!) for the OpenGL renderer. Then, the
code branch for the Cairo renderer is entered and the list of so\-called
foreground mobjects (which are rendered on top of all other mobjects)
is added to the list of passed mobjects. This is to ensure that the
foreground mobjects will stay above of the other mobjects, even after
adding the new ones. In our case, the list of foreground mobjects
is actually empty, and nothing changes.


Next, [`Scene.restructure_mobjects()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.restructure_mobjects "manim.scene.scene.Scene.restructure_mobjects") is called with the list
of mobjects to be added as the `to_remove` argument, which might
sound odd at first. Practically, this ensures that mobjects are not
added twice, as mentioned above: if they were present in the scene
`Scene.mobjects` list before (even if they were contained as a
child of some other mobject), they are first removed from the list.
The way `Scene.restrucutre_mobjects()` works is rather aggressive:
It always operates on a given list of mobjects; in the `add` method
two different lists occur: the default one, `Scene.mobjects` (no extra
keyword argument is passed), and `Scene.moving_mobjects` (which we will
discuss later in more detail). It iterates through all of the members of
the list, and checks whether any of the mobjects passed in `to_remove`
are contained as children (in any nesting level). If so, **their parent
mobject is deconstructed** and their siblings are inserted directly
one level higher. Consider the following example:



```
>>> from manim import Scene, Square, Circle, Group
>>> test_scene = Scene()
>>> mob1 = Square()
>>> mob2 = Circle()
>>> mob_group = Group(mob1, mob2)
>>> test_scene.add(mob_group)
<manim.scene.scene.Scene object at ...>
>>> test_scene.mobjects
[Group]
>>> test_scene.restructure_mobjects(to_remove=[mob1])
<manim.scene.scene.Scene object at ...>
>>> test_scene.mobjects
[Circle]

```


Note that the group is disbanded and the circle moves into the
root layer of mobjects in `test_scene.mobjects`.


After the mobject list is “restructured”, the mobject to be added
are simply appended to `Scene.mobjects`. In our toy example,
the `Scene.mobjects` list is actually empty, so the
`restructure_mobjects` method does not actually do anything. The
`orange_square` is simply added to `Scene.mobjects`, and as
the aforementioned `Scene.moving_mobjects` list is, at this point,
also still empty, nothing happens and [`Scene.add()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") returns.


We will hear more about the `moving_mobject` list when we discuss
the render loop. Before we do that, let us look at the next line
of code in our toy example, which includes the initialization of
an animation class,



```
ReplacementTransform(orange_square, blue_circle, run_time=3)

```


Hence it is time to talk about [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").





## Animations and the Render Loop[¶](#animations-and-the-render-loop "Link to this heading")



### Initializing animations[¶](#initializing-animations "Link to this heading")


Before we follow the trace of the debugger, let us briefly discuss
the general structure of the (abstract) base class [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").
An animation object holds all the information necessary for the renderer
to generate the corresponding frames. Animations (in the sense of
animation objects) in Manim are *always* tied to a specific mobject;
even in the case of [`AnimationGroup`](../reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup") (which you should actually
think of as an animation on a group of mobjects rather than a group
of animations). Moreover, except for in a particular special case,
the run time of animations is also fixed and known beforehand.


The initialization of animations actually is not very exciting,
`Animation.__init__()` merely sets some attributes derived
from the passed keyword arguments and additionally ensures that
the `Animation.starting_mobject` and `Animation.mobject`
attributes are populated. Once the animation is played, the
`starting_mobject` attribute holds an unmodified copy of the
mobject the animation is attached to; during the initialization
it is set to a placeholder mobject. The `mobject` attribute
is set to the mobject the animation is attached to.


Animations have a few special methods which are called during the
render loop:


* [`Animation.begin()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.begin "manim.animation.animation.Animation.begin"), which is called (as hinted by its name)
at the beginning of every animation, so before the first frame
is rendered. In it, all the required setup for the animation happens.
* [`Animation.finish()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish") is the counterpart to the `begin` method
which is called at the end of the life cycle of the animation (after
the last frame has been rendered).
* [`Animation.interpolate()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate "manim.animation.animation.Animation.interpolate") is the method that updates the mobject
attached to the animation to the corresponding animation completion
percentage. For example, if in the render loop,
`some_animation.interpolate(0.5)` is called, the attached mobject
will be updated to the state where 50% of the animation are completed.


We will discuss details about these and some further animation methods
once we walk through the actual render loop. For now, we continue with
our toy example and the code that is run when initializing the
[`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") animation.


The initialization method of [`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") only
consists of a call to the constructor of its parent class,
[`Transform`](../reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform"), with the additional keyword argument
`replace_mobject_with_target_in_scene` set to `True`.
[`Transform`](../reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") then sets attributes that control how the
points of the starting mobject are deformed into the points of
the target mobject, and then passes on to the initialization
method of [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"). Other basic properties of the
animation (like its `run_time`, the `rate_func`, etc.) are
processed there – and then the animation object is fully
initialized and ready to be played.




### The `play` call: preparing to enter Manim’s render loop[¶](#the-play-call-preparing-to-enter-manim-s-render-loop "Link to this heading")


We are finally there, the render loop is in our reach. Let us
walk through the code that is run when [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") is called.



Hint


Recall that this article is specifically about the Cairo renderer.
Up to here, things were more or less the same for the OpenGL renderer
as well; while some base mobjects might be different, the control flow
and lifecycle of mobjects is still more or less the same. There are more
substantial differences when it comes to the rendering loop.



As you will see when inspecting the method, [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") almost
immediately passes over to the `play` method of the renderer,
in our case `CairoRenderer.play`. The one thing [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play")
takes care of is the management of subcaptions that you might have
passed to it (see the the documentation of [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") and
[`Scene.add_subcaption()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "manim.scene.scene.Scene.add_subcaption") for more information).



Warning


As has been said before, the communication between scene and renderer
is not in a very clean state at this point, so the following paragraphs
might be confusing if you don’t run a debugger and step through the
code yourself a bit.



Inside `CairoRenderer.play()`, the renderer first checks whether
it may skip rendering of the current play call. This might happen, for example,
when `-s` is passed to the CLI (i.e., only the last frame should be rendered),
or when the `-n` flag is passed and the current play call is outside of the
specified render bounds. The “skipping status” is updated in form of the
call to `CairoRenderer.update_skipping_status()`.


Next, the renderer asks the scene to process the animations in the play
call so that renderer obtains all of the information it needs. To
be more concrete, [`Scene.compile_animation_data()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animation_data "manim.scene.scene.Scene.compile_animation_data") is called,
which then takes care of several things:


* The method processes all animations and the keyword arguments passed
to the initial [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call. In particular, this means
that it makes sure all arguments passed to the play call are actually
animations (or `.animate` syntax calls, which are also assembled to
be actual [`Animation`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")\-objects at that point). It also propagates
any animation\-related keyword arguments (like `run_time`,
or `rate_func`) passed to `Scene.play` to each individual
animation. The processed animations are then stored in the `animations`
attribute of the scene (which the renderer later reads…).
* It adds all mobjects to which the animations that are played are
bound to to the scene (provided the animation is not an mobject\-introducing
animation – for these, the addition to the scene happens later).
* In case the played animation is a [`Wait`](../reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait") animation (this is the
case in a [`Scene.wait()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") call), the method checks whether a static
image should be rendered, or whether the render loop should be processed
as usual (see [`Scene.should_update_mobjects()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.should_update_mobjects "manim.scene.scene.Scene.should_update_mobjects") for the exact conditions,
basically it checks whether there are any time\-dependent updater functions
and so on).
* Finally, the method determines the total run time of the play call (which
at this point is computed as the maximum of the run times of the passed
animations). This is stored in the `duration` attribute of the scene.


After the animation data has been compiled by the scene, the renderer
continues to prepare for entering the render loop. It now checks the
skipping status which has been determined before. If the renderer can
skip this play call, it does so: it sets the current play call hash (which
we will get back to in a moment) to `None` and increases the time of the
renderer by the determined animation run time.


Otherwise, the renderer checks whether or not Manim’s caching system should
be used. The idea of the caching system is simple: for every play call, a
hash value is computed, which is then stored and upon re\-rendering the scene,
the hash is generated again and checked against the stored value. If it is the
same, the cached output is reused, otherwise it is fully rerendered again.
We will not go into details of the caching system here; if you would like
to learn more, the [`get_hash_from_play_call()`](../reference/manim.utils.hashing.html#manim.utils.hashing.get_hash_from_play_call "manim.utils.hashing.get_hash_from_play_call") function in the
[`utils.hashing`](../reference/manim.utils.hashing.html#module-manim.utils.hashing "manim.utils.hashing") module is essentially the entry point to the caching
mechanism.


In the event that the animation has to be rendered, the renderer asks
its [`SceneFileWriter`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") to start a writing process. The process
is started by a call to `ffmpeg` and opens a pipe to which rendered
raw frames can be written. As long as the pipe is open, the process
can be accessed via the `writing_process` attribute of the file writer.
With the writing process in place, the renderer then asks the scene
to “begin” the animations.


First, it literally *begins* all of the animations by calling their
setup methods ([`Animation._setup_scene()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation._setup_scene "manim.animation.animation.Animation._setup_scene"), [`Animation.begin()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.begin "manim.animation.animation.Animation.begin")).
In doing so, the mobjects that are newly introduced by an animation
(like via [`Create`](../reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") etc.) are added to the scene. Furthermore, the
animation suspends updater functions being called on its mobject, and
it sets its mobject to the state that corresponds to the first frame
of the animation.


After this has happened for all animations in the current `play` call,
the Cairo renderer determines which of the scene’s mobjects can be
painted statically to the background, and which ones have to be
redrawn every frame. It does so by calling
`Scene.get_moving_and_static_mobjects()`, and the resulting
partition of mobjects is stored in the corresponding `moving_mobjects`
and `static_mobjects` attributes.



Note


The mechanism that determines static and moving mobjects is
specific for the Cairo renderer, the OpenGL renderer works differently.
Basically, moving mobjects are determined by checking whether they,
any of their children, or any of the mobjects “below” them (in the
sense of the order in which mobjects are processed in the scene)
either have an update function attached, or whether they appear
in one of the current animations. See the implementation of
[`Scene.get_moving_mobjects()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_moving_mobjects "manim.scene.scene.Scene.get_moving_mobjects") for more details.



Up to this very point, we did not actually render any (partial)
image or movie files from the scene yet. This is, however, about to change.
Before we enter the render loop, let us briefly revisit our toy
example and discuss how the generic [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call
setup looks like there.


For the call that plays the [`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform"), there
is no subcaption to be taken care of. The renderer then asks
the scene to compile the animation data: the passed argument
already is an animation (no additional preparations needed),
there is no need for processing any keyword arguments (as
we did not specify any additional ones to `play`). The
mobject bound to the animation, `orange_square`, is already
part of the scene (so again, no action taken). Finally, the run
time is extracted (3 seconds long) and stored in
`Scene.duration`. The renderer then checks whether it should
skip (it should not), then whether the animation is already
cached (it is not). The corresponding animation hash value is
determined and passed to the file writer, which then also calls
`ffmpeg` to start the writing process which waits for rendered
frames from the library.


The scene then `begin`s the animation: for the
[`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") this means that the animation populates
all of its relevant animation attributes (i.e., compatible copies
of the starting and the target mobject so that it can safely interpolate
between the two).


The mechanism determining static and moving mobjects considers
all of the scenes mobjects (at this point only the
`orange_square`), and determines that the `orange_square` is
bound to an animation that is currently played. As a result,
the square is classified as a “moving mobject”.


Time to render some frames.




### The render loop (for real this time)[¶](#the-render-loop-for-real-this-time "Link to this heading")


As mentioned above, due to the mechanism that determines static and moving
mobjects in the scene, the renderer knows which mobjects it can paint
statically to the background of the scene. Practically, this means that
it partially renders a scene (to produce a background image), and then
when iterating through the time progression of the animation only the
“moving mobjects” are re\-painted on top of the static background.


The renderer calls `CairoRenderer.save_static_frame_data()`, which
first checks whether there are currently any static mobjects, and if there
are, it updates the frame (only with the static mobjects; more about how
exactly this works in a moment) and then saves a NumPy array representing
the rendered frame in the `static_image` attribute. In our toy example,
there are no static mobjects, and so the `static_image` attribute is
simply set to `None`.


Next, the renderer asks the scene whether the current animation is
a “frozen frame” animation, which would mean that the renderer actually
does not have to repaint the moving mobjects in every frame of the time
progression. It can then just take the latest static frame, and display it
throughout the animation.



Note


An animation is considered a “frozen frame” animation if only a
static [`Wait`](../reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait") animation is played. See the description
of [`Scene.compile_animation_data()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animation_data "manim.scene.scene.Scene.compile_animation_data") above, or the
implementation of [`Scene.should_update_mobjects()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.should_update_mobjects "manim.scene.scene.Scene.should_update_mobjects") for
more details.



If this is not the case (just as in our toy example), the renderer
then calls the [`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") method, which is the
integral part of the render loop (in which the library steps through
the time progression of the animation and renders the corresponding
frames).


Within [`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal"), the following steps are performed:


* The scene determines the run time of the animations by calling
[`Scene.get_run_time()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_run_time "manim.scene.scene.Scene.get_run_time"). This method basically takes the maximum
`run_time` attribute of all of the animations passed to the
[`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call.
* Then the *time progression* is constructed via the (internal)
[`Scene._get_animation_time_progression()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene._get_animation_time_progression "manim.scene.scene.Scene._get_animation_time_progression") method, which wraps
the actual [`Scene.get_time_progression()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_time_progression "manim.scene.scene.Scene.get_time_progression") method. The time
progression is a `tqdm` [progress bar object](https://tqdm.github.io)
for an iterator over `np.arange(0, run_time, 1 / config.frame_rate)`. In
other words, the time progression holds the time stamps (relative to the
current animations, so starting at 0 and ending at the total animation run time,
with the step size determined by the render frame rate) of the timeline where
a new animation frame should be rendered.
* Then the scene iterates over the time progression: for each time stamp `t`,
`Scene.update_to_time()` is called, which …


	+ … first computes the time passed since the last update (which might be 0,
	especially for the initial call) and references it as `dt`,
	+ then (in the order in which the animations are passed to [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play"))
	calls [`Animation.update_mobjects()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.update_mobjects "manim.animation.animation.Animation.update_mobjects") to trigger all updater functions that
	are attached to the respective animation except for the “main mobject” of
	the animation (that is, for example, for [`Transform`](../reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") the unmodified
	copies of start and target mobject – see [`Animation.get_all_mobjects_to_update()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.get_all_mobjects_to_update "manim.animation.animation.Animation.get_all_mobjects_to_update")
	for more details),
	+ then the relative time progression with respect to the current animation
	is computed (`alpha = t / animation.run_time`), which is then used to
	update the state of the animation with a call to [`Animation.interpolate()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate "manim.animation.animation.Animation.interpolate").
	+ After all of the passed animations have been processed, the updater functions
	of all mobjects in the scene, all meshes, and finally those attached to
	the scene itself are run.


At this point, the internal (Python) state of all mobjects has been updated
to match the currently processed timestamp. If rendering should not be skipped,
then it is now time to *take a picture*!



Note


The update of the internal state (iteration over the time progression) happens
*always* once [`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") is entered. This ensures that even
if frames do not need to be rendered (because, e.g., the `-n` CLI flag has
been passed, something has been cached, or because we might be in a *Section*
with skipped rendering), updater functions still run correctly, and the state
of the first frame that *is* rendered is kept consistent.



To render an image, the scene calls the corresponding method of its renderer,
`CairoRenderer.render()` and passes just the list of *moving mobjects* (remember,
the *static mobjects* are assumed to have already been painted statically to
the background of the scene). All of the hard work then happens when the renderer
updates its current frame via a call to `CairoRenderer.update_frame()`:


First, the renderer prepares its [`Camera`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera") by checking whether the renderer
has a `static_image` different from `None` stored already. If so, it sets the
image as the *background image* of the camera via `Camera.set_frame_to_background()`,
and otherwise it just resets the camera via [`Camera.reset()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.reset "manim.camera.camera.Camera.reset"). The camera is then
asked to capture the scene with a call to [`Camera.capture_mobjects()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobjects "manim.camera.camera.Camera.capture_mobjects").


Things get a bit technical here, and at some point it is more efficient to
delve into the implementation – but here is a summary of what happens once the
camera is asked to capture the scene:


* First, a flat list of mobjects is created (so submobjects get extracted from
their parents). This list is then processed in groups of the same type of
mobjects (e.g., a batch of vectorized mobjects, followed by a batch of image mobjects,
followed by more vectorized mobjects, etc. – in many cases there will just be
one batch of vectorized mobjects).
* Depending on the type of the currently processed batch, the camera uses dedicated
*display functions* to convert the [`Mobject`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") Python object to
a NumPy array stored in the camera’s `pixel_array` attribute.
The most important example in that context is the display function for
vectorized mobjects, [`Camera.display_multiple_vectorized_mobjects()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_vectorized_mobjects "manim.camera.camera.Camera.display_multiple_vectorized_mobjects"),
or the more particular (in case you did not add a background image to your
[`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")), [`Camera.display_multiple_non_background_colored_vmobjects()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects "manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects").
This method first gets the current Cairo context, and then, for every (vectorized)
mobject in the batch, calls [`Camera.display_vectorized()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_vectorized "manim.camera.camera.Camera.display_vectorized"). There,
the actual background stroke, fill, and then stroke of the mobject is
drawn onto the context. See [`Camera.apply_stroke()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.apply_stroke "manim.camera.camera.Camera.apply_stroke") and
[`Camera.set_cairo_context_color()`](../reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_cairo_context_color "manim.camera.camera.Camera.set_cairo_context_color") for more details – but it does not get
much deeper than that, in the latter method the actual Bézier curves
determined by the points of the mobject are drawn; this is where the low\-level
interaction with Cairo happens.


After all batches have been processed, the camera has an image representation
of the Scene at the current time stamp in form of a NumPy array stored in its
`pixel_array` attribute. The renderer then takes this array and passes it to
its [`SceneFileWriter`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter"). This concludes one iteration of the render loop,
and once the time progression has been processed completely, a final bit
of cleanup is performed before the [`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") call is completed.


A TL;DR for the render loop, in the context of our toy example, reads as follows:


* The scene finds that a 3 second long animation (the [`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform")
changing the orange square to the blue circle) should be played. Given the requested
medium render quality, the frame rate is 30 frames per second, and so the time
progression with steps `[0, 1/30, 2/30, ..., 89/30]` is created.
* In the internal render loop, each of these time stamps is processed:
there are no updater functions, so effectively the scene updates the
state of the transformation animation to the desired time stamp (for example,
at time stamp `t = 45/30`, the animation is completed to a rate of
`alpha = 0.5`).
* Then the scene asks the renderer to do its job. The renderer asks its camera
to capture the scene, the only mobject that needs to be processed at this point
is the main mobject attached to the transformation; the camera converts the
current state of the mobject to entries in a NumPy array. The renderer passes
this array to the file writer.
* At the end of the loop, 90 frames have been passed to the file writer.




### Completing the render loop[¶](#completing-the-render-loop "Link to this heading")


The last few steps in the [`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") call are not too
exciting: for every animation, the corresponding [`Animation.finish()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish")
and [`Animation.clean_up_from_scene()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.clean_up_from_scene "manim.animation.animation.Animation.clean_up_from_scene") methods are called.



Note


Note that as part of [`Animation.finish()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish"), the [`Animation.interpolate()`](../reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.interpolate "manim.animation.animation.Animation.interpolate")
method is called with an argument of 1\.0 – you might have noticed already that
the last frame of an animation can sometimes be a bit off or incomplete.
This is by current design! The last frame rendered in the render loop (and displayed
for a duration of `1 / frame_rate` seconds in the rendered video) corresponds to
the state of the animation `1 / frame_rate` seconds before it ends. To display
the final frame as well in the video, we would need to append another `1 / frame_rate`
seconds to the video – which would then mean that a 1 second rendered Manim video
would be slightly longer than 1 second. We decided against this at some point.



In the end, the time progression is closed (which completes the displayed progress bar)
in the terminal. With the closing of the time progression, the
[`Scene.play_internal()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") call is completed, and we return to the renderer,
which now orders the [`SceneFileWriter`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") to close the movie pipe that has
been opened for this animation: a partial movie file is written.


This pretty much concludes the walkthrough of a `Scene.play` call,
and actually there is not too much more to say for our toy example either: at
this point, a partial movie file that represents playing the
[`ReplacementTransform`](../reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") has been written. The initialization of
the [`Dot`](../reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") happens analogous to the initialization of `blue_circle`,
which has been discussed above. The [`Mobject.add_updater()`](../reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater") call literally
just attaches a function to the `updaters` attribute of the `small_dot`. And
the remaining [`Scene.play()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") and [`Scene.wait()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") calls follow the
exact same procedure as discussed in the render loop section above; each such call
produces a corresponding partial movie file.


Once the [`Scene.construct()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method has been fully processed (and thus all
of the corresponding partial movie files have been written), the
scene calls its cleanup method [`Scene.tear_down()`](../reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down"), and then
asks its renderer to finish the scene. The renderer, in turn, asks
its scene file writer to wrap things up by calling [`SceneFileWriter.finish()`](../reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.finish "manim.scene.scene_file_writer.SceneFileWriter.finish"),
which triggers the combination of the partial movie files into the final product.


And there you go! This is a more or less detailed description of how Manim works
under the hood. While we did not discuss every single line of code in detail
in this walkthrough, it should still give you a fairly good idea of how the general
structural design of the library and at least the Cairo rendering flow in particular
looks like.







---

