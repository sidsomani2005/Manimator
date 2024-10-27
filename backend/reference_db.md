# Reference Manual


# Reference Manual[¶](#reference-manual "Link to this heading")


This reference manual details modules, functions, and variables included in
Manim, describing what they are and what they do. For learning how to use
Manim, see [Tutorials](tutorials/index.html). For a list of changes since the last release, see
the [Changelog](changelog.html).


Warning


The pages linked to here are currently a work in progress.


## Inheritance Graphs[¶](#inheritance-graphs "Link to this heading")


### Animations[¶](#animations "Link to this heading")


Inheritance diagram of manim.animation.animation, manim.animation.changing, manim.animation.composition, manim.animation.creation, manim.animation.fading, manim.animation.growing, manim.animation.indication, manim.animation.movement, manim.animation.numbers, manim.animation.rotation, manim.animation.specialized, manim.animation.speedmodifier, manim.animation.transform, manim.animation.transform\_matching\_parts, manim.animation.updaters.mobject\_update\_utils, manim.animation.updaters.update


### Cameras[¶](#cameras "Link to this heading")


Inheritance diagram of manim.camera.camera, manim.camera.mapping\_camera, manim.camera.moving\_camera, manim.camera.multi\_camera, manim.camera.three\_d\_camera


### Mobjects[¶](#mobjects "Link to this heading")


Inheritance diagram of manim.mobject.frame, manim.mobject.geometry.arc, manim.mobject.geometry.boolean\_ops, manim.mobject.geometry.line, manim.mobject.geometry.polygram, manim.mobject.geometry.shape\_matchers, manim.mobject.geometry.tips, manim.mobject.graph, manim.mobject.graphing.coordinate\_systems, manim.mobject.graphing.functions, manim.mobject.graphing.number\_line, manim.mobject.graphing.probability, manim.mobject.graphing.scale, manim.mobject.logo, manim.mobject.matrix, manim.mobject.mobject, manim.mobject.table, manim.mobject.three\_d.polyhedra, manim.mobject.three\_d.three\_d\_utils, manim.mobject.three\_d.three\_dimensions, manim.mobject.svg.brace, manim.mobject.svg.svg\_mobject, manim.mobject.text.code\_mobject, manim.mobject.text.numbers, manim.mobject.text.tex\_mobject, manim.mobject.text.text\_mobject, manim.mobject.types.image\_mobject, manim.mobject.types.point\_cloud\_mobject, manim.mobject.types.vectorized\_mobject, manim.mobject.value\_tracker, manim.mobject.vector\_field


### Scenes[¶](#scenes "Link to this heading")


Inheritance diagram of manim.scene.moving\_camera\_scene, manim.scene.scene, manim.scene.scene\_file\_writer, manim.scene.three\_d\_scene, manim.scene.vector\_space\_scene, manim.scene.zoomed\_scene


## Module Index[¶](#module-index "Link to this heading")


* [Animations](reference_index/animations.html)
	+ [animation](reference/manim.animation.animation.html)
		- [Animation](reference/manim.animation.animation.Animation.html)
		- [Wait](reference/manim.animation.animation.Wait.html)
		- [`override_animation()`](reference/manim.animation.animation.html#manim.animation.animation.override_animation)
		- [`prepare_animation()`](reference/manim.animation.animation.html#manim.animation.animation.prepare_animation)
	+ [changing](reference/manim.animation.changing.html)
		- [AnimatedBoundary](reference/manim.animation.changing.AnimatedBoundary.html)
		- [TracedPath](reference/manim.animation.changing.TracedPath.html)
	+ [composition](reference/manim.animation.composition.html)
		- [AnimationGroup](reference/manim.animation.composition.AnimationGroup.html)
		- [LaggedStart](reference/manim.animation.composition.LaggedStart.html)
		- [LaggedStartMap](reference/manim.animation.composition.LaggedStartMap.html)
		- [Succession](reference/manim.animation.composition.Succession.html)
	+ [creation](reference/manim.animation.creation.html)
		- [AddTextLetterByLetter](reference/manim.animation.creation.AddTextLetterByLetter.html)
		- [AddTextWordByWord](reference/manim.animation.creation.AddTextWordByWord.html)
		- [Create](reference/manim.animation.creation.Create.html)
		- [DrawBorderThenFill](reference/manim.animation.creation.DrawBorderThenFill.html)
		- [RemoveTextLetterByLetter](reference/manim.animation.creation.RemoveTextLetterByLetter.html)
		- [ShowIncreasingSubsets](reference/manim.animation.creation.ShowIncreasingSubsets.html)
		- [ShowPartial](reference/manim.animation.creation.ShowPartial.html)
		- [ShowSubmobjectsOneByOne](reference/manim.animation.creation.ShowSubmobjectsOneByOne.html)
		- [SpiralIn](reference/manim.animation.creation.SpiralIn.html)
		- [Uncreate](reference/manim.animation.creation.Uncreate.html)
		- [Unwrite](reference/manim.animation.creation.Unwrite.html)
		- [Write](reference/manim.animation.creation.Write.html)
	+ [fading](reference/manim.animation.fading.html)
		- [FadeIn](reference/manim.animation.fading.FadeIn.html)
		- [FadeOut](reference/manim.animation.fading.FadeOut.html)
	+ [growing](reference/manim.animation.growing.html)
		- [GrowArrow](reference/manim.animation.growing.GrowArrow.html)
		- [GrowFromCenter](reference/manim.animation.growing.GrowFromCenter.html)
		- [GrowFromEdge](reference/manim.animation.growing.GrowFromEdge.html)
		- [GrowFromPoint](reference/manim.animation.growing.GrowFromPoint.html)
		- [SpinInFromNothing](reference/manim.animation.growing.SpinInFromNothing.html)
	+ [indication](reference/manim.animation.indication.html)
		- [ApplyWave](reference/manim.animation.indication.ApplyWave.html)
		- [Circumscribe](reference/manim.animation.indication.Circumscribe.html)
		- [Flash](reference/manim.animation.indication.Flash.html)
		- [FocusOn](reference/manim.animation.indication.FocusOn.html)
		- [Indicate](reference/manim.animation.indication.Indicate.html)
		- [ShowPassingFlash](reference/manim.animation.indication.ShowPassingFlash.html)
		- [ShowPassingFlashWithThinningStrokeWidth](reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html)
		- [Wiggle](reference/manim.animation.indication.Wiggle.html)
	+ [movement](reference/manim.animation.movement.html)
		- [ComplexHomotopy](reference/manim.animation.movement.ComplexHomotopy.html)
		- [Homotopy](reference/manim.animation.movement.Homotopy.html)
		- [MoveAlongPath](reference/manim.animation.movement.MoveAlongPath.html)
		- [PhaseFlow](reference/manim.animation.movement.PhaseFlow.html)
		- [SmoothedVectorizedHomotopy](reference/manim.animation.movement.SmoothedVectorizedHomotopy.html)
	+ [numbers](reference/manim.animation.numbers.html)
		- [ChangeDecimalToValue](reference/manim.animation.numbers.ChangeDecimalToValue.html)
		- [ChangingDecimal](reference/manim.animation.numbers.ChangingDecimal.html)
	+ [rotation](reference/manim.animation.rotation.html)
		- [Rotate](reference/manim.animation.rotation.Rotate.html)
		- [Rotating](reference/manim.animation.rotation.Rotating.html)
	+ [specialized](reference/manim.animation.specialized.html)
		- [Broadcast](reference/manim.animation.specialized.Broadcast.html)
	+ [speedmodifier](reference/manim.animation.speedmodifier.html)
		- [ChangeSpeed](reference/manim.animation.speedmodifier.ChangeSpeed.html)
	+ [transform](reference/manim.animation.transform.html)
		- [ApplyComplexFunction](reference/manim.animation.transform.ApplyComplexFunction.html)
		- [ApplyFunction](reference/manim.animation.transform.ApplyFunction.html)
		- [ApplyMatrix](reference/manim.animation.transform.ApplyMatrix.html)
		- [ApplyMethod](reference/manim.animation.transform.ApplyMethod.html)
		- [ApplyPointwiseFunction](reference/manim.animation.transform.ApplyPointwiseFunction.html)
		- [ApplyPointwiseFunctionToCenter](reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html)
		- [ClockwiseTransform](reference/manim.animation.transform.ClockwiseTransform.html)
		- [CounterclockwiseTransform](reference/manim.animation.transform.CounterclockwiseTransform.html)
		- [CyclicReplace](reference/manim.animation.transform.CyclicReplace.html)
		- [FadeToColor](reference/manim.animation.transform.FadeToColor.html)
		- [FadeTransform](reference/manim.animation.transform.FadeTransform.html)
		- [FadeTransformPieces](reference/manim.animation.transform.FadeTransformPieces.html)
		- [MoveToTarget](reference/manim.animation.transform.MoveToTarget.html)
		- [ReplacementTransform](reference/manim.animation.transform.ReplacementTransform.html)
		- [Restore](reference/manim.animation.transform.Restore.html)
		- [ScaleInPlace](reference/manim.animation.transform.ScaleInPlace.html)
		- [ShrinkToCenter](reference/manim.animation.transform.ShrinkToCenter.html)
		- [Swap](reference/manim.animation.transform.Swap.html)
		- [Transform](reference/manim.animation.transform.Transform.html)
		- [TransformAnimations](reference/manim.animation.transform.TransformAnimations.html)
		- [TransformFromCopy](reference/manim.animation.transform.TransformFromCopy.html)
	+ [transform\_matching\_parts](reference/manim.animation.transform_matching_parts.html)
		- [TransformMatchingAbstractBase](reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html)
		- [TransformMatchingShapes](reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html)
		- [TransformMatchingTex](reference/manim.animation.transform_matching_parts.TransformMatchingTex.html)
	+ [updaters](reference/manim.animation.updaters.html)
		- [Modules](reference/manim.animation.updaters.html#modules)
* [Cameras](reference_index/cameras.html)
	+ [camera](reference/manim.camera.camera.html)
		- [BackgroundColoredVMobjectDisplayer](reference/manim.camera.camera.BackgroundColoredVMobjectDisplayer.html)
		- [Camera](reference/manim.camera.camera.Camera.html)
	+ [mapping\_camera](reference/manim.camera.mapping_camera.html)
		- [MappingCamera](reference/manim.camera.mapping_camera.MappingCamera.html)
		- [OldMultiCamera](reference/manim.camera.mapping_camera.OldMultiCamera.html)
		- [SplitScreenCamera](reference/manim.camera.mapping_camera.SplitScreenCamera.html)
	+ [moving\_camera](reference/manim.camera.moving_camera.html)
		- [MovingCamera](reference/manim.camera.moving_camera.MovingCamera.html)
	+ [multi\_camera](reference/manim.camera.multi_camera.html)
		- [MultiCamera](reference/manim.camera.multi_camera.MultiCamera.html)
	+ [three\_d\_camera](reference/manim.camera.three_d_camera.html)
		- [ThreeDCamera](reference/manim.camera.three_d_camera.ThreeDCamera.html)
* [Configuration](reference_index/configuration.html)
	+ [Module Index](reference_index/configuration.html#module-index)
		- [\_config](reference/manim._config.html)
		- [utils](reference/manim._config.utils.html)
		- [logger\_utils](reference/manim._config.logger_utils.html)
* [Mobjects](reference_index/mobjects.html)
	+ [frame](reference/manim.mobject.frame.html)
		- [FullScreenRectangle](reference/manim.mobject.frame.FullScreenRectangle.html)
		- [ScreenRectangle](reference/manim.mobject.frame.ScreenRectangle.html)
	+ [geometry](reference/manim.mobject.geometry.html)
		- [Modules](reference/manim.mobject.geometry.html#modules)
	+ [graph](reference/manim.mobject.graph.html)
		- [`NxGraph`](reference/manim.mobject.graph.html#manim.mobject.graph.NxGraph)
		- [DiGraph](reference/manim.mobject.graph.DiGraph.html)
		- [GenericGraph](reference/manim.mobject.graph.GenericGraph.html)
		- [Graph](reference/manim.mobject.graph.Graph.html)
		- [LayoutFunction](reference/manim.mobject.graph.LayoutFunction.html)
	+ [graphing](reference/manim.mobject.graphing.html)
		- [Modules](reference/manim.mobject.graphing.html#modules)
	+ [logo](reference/manim.mobject.logo.html)
		- [ManimBanner](reference/manim.mobject.logo.ManimBanner.html)
	+ [matrix](reference/manim.mobject.matrix.html)
		- [DecimalMatrix](reference/manim.mobject.matrix.DecimalMatrix.html)
		- [IntegerMatrix](reference/manim.mobject.matrix.IntegerMatrix.html)
		- [Matrix](reference/manim.mobject.matrix.Matrix.html)
		- [MobjectMatrix](reference/manim.mobject.matrix.MobjectMatrix.html)
		- [`get_det_text()`](reference/manim.mobject.matrix.html#manim.mobject.matrix.get_det_text)
		- [`matrix_to_mobject()`](reference/manim.mobject.matrix.html#manim.mobject.matrix.matrix_to_mobject)
		- [`matrix_to_tex_string()`](reference/manim.mobject.matrix.html#manim.mobject.matrix.matrix_to_tex_string)
	+ [mobject](reference/manim.mobject.mobject.html)
		- [`TimeBasedUpdater`](reference/manim.mobject.mobject.html#manim.mobject.mobject.TimeBasedUpdater)
		- [`NonTimeBasedUpdater`](reference/manim.mobject.mobject.html#manim.mobject.mobject.NonTimeBasedUpdater)
		- [`Updater`](reference/manim.mobject.mobject.html#manim.mobject.mobject.Updater)
		- [Group](reference/manim.mobject.mobject.Group.html)
		- [Mobject](reference/manim.mobject.mobject.Mobject.html)
		- [`override_animate()`](reference/manim.mobject.mobject.html#manim.mobject.mobject.override_animate)
	+ [svg](reference/manim.mobject.svg.html)
		- [Modules](reference/manim.mobject.svg.html#modules)
	+ [table](reference/manim.mobject.table.html)
		- [DecimalTable](reference/manim.mobject.table.DecimalTable.html)
		- [IntegerTable](reference/manim.mobject.table.IntegerTable.html)
		- [MathTable](reference/manim.mobject.table.MathTable.html)
		- [MobjectTable](reference/manim.mobject.table.MobjectTable.html)
		- [Table](reference/manim.mobject.table.Table.html)
	+ [text](reference/manim.mobject.text.html)
		- [Modules](reference/manim.mobject.text.html#modules)
	+ [three\_d](reference/manim.mobject.three_d.html)
		- [Modules](reference/manim.mobject.three_d.html#modules)
	+ [types](reference/manim.mobject.types.html)
		- [Modules](reference/manim.mobject.types.html#modules)
	+ [utils](reference/manim.mobject.utils.html)
		- [`get_mobject_class()`](reference/manim.mobject.utils.html#manim.mobject.utils.get_mobject_class)
		- [`get_point_mobject_class()`](reference/manim.mobject.utils.html#manim.mobject.utils.get_point_mobject_class)
		- [`get_vectorized_mobject_class()`](reference/manim.mobject.utils.html#manim.mobject.utils.get_vectorized_mobject_class)
	+ [value\_tracker](reference/manim.mobject.value_tracker.html)
		- [ComplexValueTracker](reference/manim.mobject.value_tracker.ComplexValueTracker.html)
		- [ValueTracker](reference/manim.mobject.value_tracker.ValueTracker.html)
	+ [vector\_field](reference/manim.mobject.vector_field.html)
		- [ArrowVectorField](reference/manim.mobject.vector_field.ArrowVectorField.html)
		- [StreamLines](reference/manim.mobject.vector_field.StreamLines.html)
		- [VectorField](reference/manim.mobject.vector_field.VectorField.html)
* [Scenes](reference_index/scenes.html)
	+ [moving\_camera\_scene](reference/manim.scene.moving_camera_scene.html)
		- [MovingCameraScene](reference/manim.scene.moving_camera_scene.MovingCameraScene.html)
	+ [section](reference/manim.scene.section.html)
		- [DefaultSectionType](reference/manim.scene.section.DefaultSectionType.html)
		- [Section](reference/manim.scene.section.Section.html)
	+ [scene](reference/manim.scene.scene.html)
		- [RerunSceneHandler](reference/manim.scene.scene.RerunSceneHandler.html)
		- [Scene](reference/manim.scene.scene.Scene.html)
	+ [scene\_file\_writer](reference/manim.scene.scene_file_writer.html)
		- [SceneFileWriter](reference/manim.scene.scene_file_writer.SceneFileWriter.html)
	+ [three\_d\_scene](reference/manim.scene.three_d_scene.html)
		- [SpecialThreeDScene](reference/manim.scene.three_d_scene.SpecialThreeDScene.html)
		- [ThreeDScene](reference/manim.scene.three_d_scene.ThreeDScene.html)
	+ [vector\_space\_scene](reference/manim.scene.vector_space_scene.html)
		- [LinearTransformationScene](reference/manim.scene.vector_space_scene.LinearTransformationScene.html)
		- [VectorScene](reference/manim.scene.vector_space_scene.VectorScene.html)
	+ [zoomed\_scene](reference/manim.scene.zoomed_scene.html)
		- [ZoomedScene](reference/manim.scene.zoomed_scene.ZoomedScene.html)
* [Utilities and other modules](reference_index/utilities_misc.html)
	+ [Module Index](reference_index/utilities_misc.html#module-index)
		- [bezier](reference/manim.utils.bezier.html)
		- [color](reference/manim.utils.color.html)
		- [commands](reference/manim.utils.commands.html)
		- [config\_ops](reference/manim.utils.config_ops.html)
		- [constants](reference/manim.constants.html)
		- [debug](reference/manim.utils.debug.html)
		- [deprecation](reference/manim.utils.deprecation.html)
		- [docbuild](reference/manim.utils.docbuild.html)
		- [hashing](reference/manim.utils.hashing.html)
		- [images](reference/manim.utils.images.html)
		- [ipython\_magic](reference/manim.utils.ipython_magic.html)
		- [iterables](reference/manim.utils.iterables.html)
		- [paths](reference/manim.utils.paths.html)
		- [rate\_functions](reference/manim.utils.rate_functions.html)
		- [simple\_functions](reference/manim.utils.simple_functions.html)
		- [sounds](reference/manim.utils.sounds.html)
		- [space\_ops](reference/manim.utils.space_ops.html)
		- [testing](reference/manim.utils.testing.html)
		- [tex](reference/manim.utils.tex.html)
		- [tex\_file\_writing](reference/manim.utils.tex_file_writing.html)
		- [tex\_templates](reference/manim.utils.tex_templates.html)
		- [typing](reference/manim.typing.html)



---

# Animation


# Animation[¶](#animation "Link to this heading")


Qualified name: `manim.animation.animation.Animation`


*class* Animation(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/animation.html#Animation)[¶](#manim.animation.animation.Animation "Link to this definition")
Bases: `object`


An animation.


Animations have a fixed time span.


Parameters:
* **mobject** – The mobject to be animated. This is not required for all types of animations.
* **lag\_ratio** – 

Defines the delay after which the animation is applied to submobjects. This lag
is relative to the duration of the animation.


This does not influence the total
runtime of the animation. Instead the runtime of individual animations is
adjusted so that the complete animation has the defined run time.
* **run\_time** – The duration of the animation in seconds.
* **rate\_func** – 

The function defining the animation progress based on the relative runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")) .


For example `rate_func(0.5)` is the proportion of the animation that is done
after half of the animations run time.


Return type:
Self


reverse\_rate\_functionReverses the rate function of the animation. Setting `reverse_rate_function`
does not have any effect on `remover` or `introducer`. These need to be
set explicitly if an introducer\-animation should be turned into a remover one
and vice versa.


nameThe name of the animation. This gets displayed while rendering the animation.
Defaults to \<class\-name\>(\<Mobject\-name\>).


removerWhether the given mobject should be removed from the scene after this animation.


suspend\_mobject\_updatingWhether updaters of the mobject should be suspended during the animation.


Note


In the current implementation of this class, the specified rate function is applied
within [`Animation.interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") call as part of the call to
`Animation.interpolate_submobject()`. For subclasses of [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation")
that are implemented by overriding [`interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject"), the rate function
has to be applied manually (e.g., by passing `self.rate_func(alpha)` instead
of just `alpha`).


Examples


Example: LagRatios [¶](#lagratios)


```
from manim import *

class LagRatios(Scene):
    def construct(self):
        ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

        # Create dot groups
        group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
        groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
        self.add(groups)

        # Label groups
        self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
        for group, ratio in zip(groups, ratios):
            self.add(Text(str(ratio), font_size=36).next_to(group, UP))

        #Animate groups with different lag_ratios
        self.play(AnimationGroup(*[
            group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
            for group, ratio in zip(groups, ratios)
        ]))

        # lag_ratio also works recursively on nested submobjects:
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))

```


```

class LagRatios(Scene):
    def construct(self):
        ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

        # Create dot groups
        group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
        groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
        self.add(groups)

        # Label groups
        self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
        for group, ratio in zip(groups, ratios):
            self.add(Text(str(ratio), font_size=36).next_to(group, UP))

        #Animate groups with different lag_ratios
        self.play(AnimationGroup(*[
            group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
            for group, ratio in zip(groups, ratios)
        ]))

        # lag_ratio also works recursively on nested submobjects:
        self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))


```
Methods


| [`begin`](#manim.animation.animation.Animation.begin "manim.animation.animation.Animation.begin") | Begin the animation. |
| --- | --- |
| [`clean_up_from_scene`](#manim.animation.animation.Animation.clean_up_from_scene "manim.animation.animation.Animation.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`copy`](#manim.animation.animation.Animation.copy "manim.animation.animation.Animation.copy") | Create a copy of the animation. |
| `create_starting_mobject` |  |
| [`finish`](#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish") | Finish the animation. |
| `get_all_families_zipped` |  |
| [`get_all_mobjects`](#manim.animation.animation.Animation.get_all_mobjects "manim.animation.animation.Animation.get_all_mobjects") | Get all mobjects involved in the animation. |
| [`get_all_mobjects_to_update`](#manim.animation.animation.Animation.get_all_mobjects_to_update "manim.animation.animation.Animation.get_all_mobjects_to_update") | Get all mobjects to be updated during the animation. |
| [`get_rate_func`](#manim.animation.animation.Animation.get_rate_func "manim.animation.animation.Animation.get_rate_func") | Get the rate function of the animation. |
| [`get_run_time`](#manim.animation.animation.Animation.get_run_time "manim.animation.animation.Animation.get_run_time") | Get the run time of the animation. |
| [`get_sub_alpha`](#manim.animation.animation.Animation.get_sub_alpha "manim.animation.animation.Animation.get_sub_alpha") | Get the animation progress of any submobjects subanimation. |
| [`interpolate`](#manim.animation.animation.Animation.interpolate "manim.animation.animation.Animation.interpolate") | Set the animation progress. |
| [`interpolate_mobject`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") | Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation") based on alpha value. |
| `interpolate_submobject` |  |
| [`is_introducer`](#manim.animation.animation.Animation.is_introducer "manim.animation.animation.Animation.is_introducer") | Test if the animation is an introducer. |
| [`is_remover`](#manim.animation.animation.Animation.is_remover "manim.animation.animation.Animation.is_remover") | Test if the animation is a remover. |
| [`set_name`](#manim.animation.animation.Animation.set_name "manim.animation.animation.Animation.set_name") | Set the name of the animation. |
| [`set_rate_func`](#manim.animation.animation.Animation.set_rate_func "manim.animation.animation.Animation.set_rate_func") | Set the rate function of the animation. |
| [`set_run_time`](#manim.animation.animation.Animation.set_run_time "manim.animation.animation.Animation.set_run_time") | Set the run time of the animation. |
| [`update_mobjects`](#manim.animation.animation.Animation.update_mobjects "manim.animation.animation.Animation.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |


\_setup\_scene(*scene*)[\[source]](../_modules/manim/animation/animation.html#Animation._setup_scene)[¶](#manim.animation.animation.Animation._setup_scene "Link to this definition")
Setup up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.


This includes to [`add()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None


begin()[\[source]](../_modules/manim/animation/animation.html#Animation.begin)[¶](#manim.animation.animation.Animation.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


clean\_up\_from\_scene(*scene*)[\[source]](../_modules/manim/animation/animation.html#Animation.clean_up_from_scene)[¶](#manim.animation.animation.Animation.clean_up_from_scene "Link to this definition")
Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.


This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None


copy()[\[source]](../_modules/manim/animation/animation.html#Animation.copy)[¶](#manim.animation.animation.Animation.copy "Link to this definition")
Create a copy of the animation.


Returns:
A copy of `self`


Return type:
[Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")


finish()[\[source]](../_modules/manim/animation/animation.html#Animation.finish)[¶](#manim.animation.animation.Animation.finish "Link to this definition")
Finish the animation.


This method gets called when the animation is over.


Return type:
None


get\_all\_mobjects()[\[source]](../_modules/manim/animation/animation.html#Animation.get_all_mobjects)[¶](#manim.animation.animation.Animation.get_all_mobjects "Link to this definition")
Get all mobjects involved in the animation.


Ordering must match the ordering of arguments to interpolate\_submobject


Returns:
The sequence of mobjects.


Return type:
Sequence\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


get\_all\_mobjects\_to\_update()[\[source]](../_modules/manim/animation/animation.html#Animation.get_all_mobjects_to_update)[¶](#manim.animation.animation.Animation.get_all_mobjects_to_update "Link to this definition")
Get all mobjects to be updated during the animation.


Returns:
The list of mobjects to be updated during the animation.


Return type:
List\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


get\_rate\_func()[\[source]](../_modules/manim/animation/animation.html#Animation.get_rate_func)[¶](#manim.animation.animation.Animation.get_rate_func "Link to this definition")
Get the rate function of the animation.


Returns:
The rate function of the animation.


Return type:
Callable\[\[float], float]


get\_run\_time()[\[source]](../_modules/manim/animation/animation.html#Animation.get_run_time)[¶](#manim.animation.animation.Animation.get_run_time "Link to this definition")
Get the run time of the animation.


Returns:
The time the animation takes in seconds.


Return type:
float


get\_sub\_alpha(*alpha*, *index*, *num\_submobjects*)[\[source]](../_modules/manim/animation/animation.html#Animation.get_sub_alpha)[¶](#manim.animation.animation.Animation.get_sub_alpha "Link to this definition")
Get the animation progress of any submobjects subanimation.


Parameters:
* **alpha** (*float*) – The overall animation progress
* **index** (*int*) – The index of the subanimation.
* **num\_submobjects** (*int*) – The total count of subanimations.


Returns:
The progress of the subanimation.


Return type:
float


interpolate(*alpha*)[\[source]](../_modules/manim/animation/animation.html#Animation.interpolate)[¶](#manim.animation.animation.Animation.interpolate "Link to this definition")
Set the animation progress.


This method gets called for every frame during an animation.


Parameters:
**alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.


Return type:
None


interpolate\_mobject(*alpha*)[\[source]](../_modules/manim/animation/animation.html#Animation.interpolate_mobject)[¶](#manim.animation.animation.Animation.interpolate_mobject "Link to this definition")
Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation") based on alpha value.


Parameters:
**alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha\-values of 0, 0\.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.


Return type:
None


is\_introducer()[\[source]](../_modules/manim/animation/animation.html#Animation.is_introducer)[¶](#manim.animation.animation.Animation.is_introducer "Link to this definition")
Test if the animation is an introducer.


Returns:
`True` if the animation is an introducer, `False` otherwise.


Return type:
bool


is\_remover()[\[source]](../_modules/manim/animation/animation.html#Animation.is_remover)[¶](#manim.animation.animation.Animation.is_remover "Link to this definition")
Test if the animation is a remover.


Returns:
`True` if the animation is a remover, `False` otherwise.


Return type:
bool


set\_name(*name*)[\[source]](../_modules/manim/animation/animation.html#Animation.set_name)[¶](#manim.animation.animation.Animation.set_name "Link to this definition")
Set the name of the animation.


Parameters:
**name** (*str*) – The new name of the animation.


Returns:
`self`


Return type:
[Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")


set\_rate\_func(*rate\_func*)[\[source]](../_modules/manim/animation/animation.html#Animation.set_rate_func)[¶](#manim.animation.animation.Animation.set_rate_func "Link to this definition")
Set the rate function of the animation.


Parameters:
**rate\_func** (*Callable**\[**\[**float**]**,* *float**]*) – The new function defining the animation progress based on the
relative runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")).


Returns:
`self`


Return type:
[Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")


set\_run\_time(*run\_time*)[\[source]](../_modules/manim/animation/animation.html#Animation.set_run_time)[¶](#manim.animation.animation.Animation.set_run_time "Link to this definition")
Set the run time of the animation.


Parameters:
* **run\_time** (*float*) – The new time the animation should take in seconds.
* **note::** (*..*) – The run\_time of an animation should not be changed while it is already
running.


Returns:
`self`


Return type:
[Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")


update\_mobjects(*dt*)[\[source]](../_modules/manim/animation/animation.html#Animation.update_mobjects)[¶](#manim.animation.animation.Animation.update_mobjects "Link to this definition")
Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.


Parameters:
**dt** (*float*)


Return type:
None



---

# Wait


# Wait[¶](#wait "Link to this heading")


Qualified name: `manim.animation.animation.Wait`


*class* Wait(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/animation.html#Wait)[¶](#manim.animation.animation.Wait "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


A “no operation” animation.


Parameters:
* **run\_time** (*float*) – The amount of time that should pass.
* **stop\_condition** (*Callable**\[**\[**]**,* *bool**]* *\|* *None*) – A function without positional arguments that evaluates to a boolean.
The function is evaluated after every new frame has been rendered.
Playing the animation stops after the return value is truthy, or
after the specified `run_time` has passed.
* **frozen\_frame** (*bool* *\|* *None*) – Controls whether or not the wait animation is static, i.e., corresponds
to a frozen frame. If `False` is passed, the render loop still
progresses through the animation as usual and (among other things)
continues to call updater functions. If `None` (the default value),
the [`Scene.play()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call tries to determine whether the Wait call
can be static or not itself via `Scene.should_mobjects_update()`.
* **kwargs** – Keyword arguments to be passed to the parent class, [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*)


Methods


| [`begin`](#manim.animation.animation.Wait.begin "manim.animation.animation.Wait.begin") | Begin the animation. |
| --- | --- |
| [`clean_up_from_scene`](#manim.animation.animation.Wait.clean_up_from_scene "manim.animation.animation.Wait.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](#manim.animation.animation.Wait.finish "manim.animation.animation.Wait.finish") | Finish the animation. |
| [`interpolate`](#manim.animation.animation.Wait.interpolate "manim.animation.animation.Wait.interpolate") | Set the animation progress. |
| [`update_mobjects`](#manim.animation.animation.Wait.update_mobjects "manim.animation.animation.Wait.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |


begin()[\[source]](../_modules/manim/animation/animation.html#Wait.begin)[¶](#manim.animation.animation.Wait.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


clean\_up\_from\_scene(*scene*)[\[source]](../_modules/manim/animation/animation.html#Wait.clean_up_from_scene)[¶](#manim.animation.animation.Wait.clean_up_from_scene "Link to this definition")
Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.


This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None


finish()[\[source]](../_modules/manim/animation/animation.html#Wait.finish)[¶](#manim.animation.animation.Wait.finish "Link to this definition")
Finish the animation.


This method gets called when the animation is over.


Return type:
None


interpolate(*alpha*)[\[source]](../_modules/manim/animation/animation.html#Wait.interpolate)[¶](#manim.animation.animation.Wait.interpolate "Link to this definition")
Set the animation progress.


This method gets called for every frame during an animation.


Parameters:
**alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.


Return type:
None


update\_mobjects(*dt*)[\[source]](../_modules/manim/animation/animation.html#Wait.update_mobjects)[¶](#manim.animation.animation.Wait.update_mobjects "Link to this definition")
Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.


Parameters:
**dt** (*float*)


Return type:
None



---

# changing


# changing[¶](#module-manim.animation.changing "Link to this heading")


Animation of a mobject boundary and tracing of points.


Classes


| [`AnimatedBoundary`](manim.animation.changing.AnimatedBoundary.html#manim.animation.changing.AnimatedBoundary "manim.animation.changing.AnimatedBoundary") | Boundary of a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with animated color change. |
| --- | --- |
| [`TracedPath`](manim.animation.changing.TracedPath.html#manim.animation.changing.TracedPath "manim.animation.changing.TracedPath") | Traces the path of a point returned by a function call. |



---

# AnimatedBoundary


# AnimatedBoundary[¶](#animatedboundary "Link to this heading")


Qualified name: `manim.animation.changing.AnimatedBoundary`


*class* AnimatedBoundary(*vmobject, colors\=\[ManimColor('\#29ABCA'), ManimColor('\#9CDCEB'), ManimColor('\#236B8E'), ManimColor('\#736357')], max\_stroke\_width\=3, cycle\_rate\=0\.5, back\_and\_forth\=True, draw\_rate\_func\=\<function smooth\>, fade\_rate\_func\=\<function smooth\>, \*\*kwargs*)[\[source]](../_modules/manim/animation/changing.html#AnimatedBoundary)[¶](#manim.animation.changing.AnimatedBoundary "Link to this definition")
Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")


Boundary of a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with animated color change.


Examples


Example: AnimatedBoundaryExample [¶](#animatedboundaryexample)


```
from manim import *

class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)

```


```

class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)


```
Methods


| `full_family_become_partial` |  |
| --- | --- |
| `update_boundary_copies` |  |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*vmobject, colors\=\[ManimColor('\#29ABCA'), ManimColor('\#9CDCEB'), ManimColor('\#236B8E'), ManimColor('\#736357')], max\_stroke\_width\=3, cycle\_rate\=0\.5, back\_and\_forth\=True, draw\_rate\_func\=\<function smooth\>, fade\_rate\_func\=\<function smooth\>, \*\*kwargs*)[¶](#manim.animation.changing.AnimatedBoundary._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.



---

# TracedPath


# TracedPath[¶](#tracedpath "Link to this heading")


Qualified name: `manim.animation.changing.TracedPath`


*class* TracedPath(*traced\_point\_func*, *stroke\_width\=2*, *stroke\_color\=ManimColor('\#FFFFFF')*, *dissipating\_time\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/changing.html#TracedPath)[¶](#manim.animation.changing.TracedPath "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


Traces the path of a point returned by a function call.


Parameters:
* **traced\_point\_func** (*Callable*) – The function to be traced.
* **stroke\_width** (*float*) – The width of the trace.
* **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of the trace.
* **dissipating\_time** (*float* *\|* *None*) – The time taken for the path to dissipate. Default set to `None`
which disables dissipation.


Examples


Example: TracedPathExample [¶](#tracedpathexample)


```
from manim import *

class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)

```


```

class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)


```

Example: DissipatingPathExample [¶](#dissipatingpathexample)


```
from manim import *

class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.wait()

```


```

class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.wait()


```
Methods


| `update_path` |  |
| --- | --- |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*traced\_point\_func*, *stroke\_width\=2*, *stroke\_color\=ManimColor('\#FFFFFF')*, *dissipating\_time\=None*, *\*\*kwargs*)[¶](#manim.animation.changing.TracedPath._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **traced\_point\_func** (*Callable*)
* **stroke\_width** (*float*)
* **stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*)
* **dissipating\_time** (*float* *\|* *None*)



---

# composition


# composition[¶](#module-manim.animation.composition "Link to this heading")


Tools for displaying multiple animations at once.


Classes


| [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup") | Plays a group or series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"). |
| --- | --- |
| [`LaggedStart`](manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart") | Adjusts the timing of a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") according to `lag_ratio`. |
| [`LaggedStartMap`](manim.animation.composition.LaggedStartMap.html#manim.animation.composition.LaggedStartMap "manim.animation.composition.LaggedStartMap") | Plays a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") while mapping a function to submobjects. |
| [`Succession`](manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") | Plays a series of animations in succession. |



---

# AnimationGroup


# AnimationGroup[¶](#animationgroup "Link to this heading")


Qualified name: `manim.animation.composition.AnimationGroup`


*class* AnimationGroup(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup)[¶](#manim.animation.composition.AnimationGroup "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


Plays a group or series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").


Parameters:
* **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") *\|* *Iterable**\[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]* *\|* *types.GeneratorType**\[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – Sequence of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.
* **group** ([*Group*](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group") *\|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") *\|* *OpenGLGroup* *\|* *OpenGLVGroup*) – A group of multiple [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **run\_time** (*float* *\|* *None*) – The duration of the animation in seconds.
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*) – The function defining the animation progress based on the relative
runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")) .
* **lag\_ratio** (*float*) – 

Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
`n.nn` means the next animation will play when `nnn%` of the current animation has played.
Defaults to 0\.0, meaning that all animations will be played together.


This does not influence the total runtime of the animation. Instead the runtime
of individual animations is adjusted so that the complete animation has the defined
run time.


Methods


| [`begin`](#manim.animation.composition.AnimationGroup.begin "manim.animation.composition.AnimationGroup.begin") | Begin the animation. |
| --- | --- |
| [`build_animations_with_timings`](#manim.animation.composition.AnimationGroup.build_animations_with_timings "manim.animation.composition.AnimationGroup.build_animations_with_timings") | Creates a list of triplets of the form (anim, start\_time, end\_time). |
| [`clean_up_from_scene`](#manim.animation.composition.AnimationGroup.clean_up_from_scene "manim.animation.composition.AnimationGroup.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](#manim.animation.composition.AnimationGroup.finish "manim.animation.composition.AnimationGroup.finish") | Finish the animation. |
| [`get_all_mobjects`](#manim.animation.composition.AnimationGroup.get_all_mobjects "manim.animation.composition.AnimationGroup.get_all_mobjects") | Get all mobjects involved in the animation. |
| [`init_run_time`](#manim.animation.composition.AnimationGroup.init_run_time "manim.animation.composition.AnimationGroup.init_run_time") | Calculates the run time of the animation, if different from `run_time`. |
| [`interpolate`](#manim.animation.composition.AnimationGroup.interpolate "manim.animation.composition.AnimationGroup.interpolate") | Set the animation progress. |
| [`update_mobjects`](#manim.animation.composition.AnimationGroup.update_mobjects "manim.animation.composition.AnimationGroup.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |


\_setup\_scene(*scene*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup._setup_scene)[¶](#manim.animation.composition.AnimationGroup._setup_scene "Link to this definition")
Setup up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.


This includes to [`add()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.


Parameters:
**scene** – The scene the animation should be cleaned up from.


Return type:
None


begin()[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.begin)[¶](#manim.animation.composition.AnimationGroup.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


build\_animations\_with\_timings()[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.build_animations_with_timings)[¶](#manim.animation.composition.AnimationGroup.build_animations_with_timings "Link to this definition")
Creates a list of triplets of the form (anim, start\_time, end\_time).


Return type:
None


clean\_up\_from\_scene(*scene*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.clean_up_from_scene)[¶](#manim.animation.composition.AnimationGroup.clean_up_from_scene "Link to this definition")
Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.


This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None


finish()[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.finish)[¶](#manim.animation.composition.AnimationGroup.finish "Link to this definition")
Finish the animation.


This method gets called when the animation is over.


Return type:
None


get\_all\_mobjects()[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.get_all_mobjects)[¶](#manim.animation.composition.AnimationGroup.get_all_mobjects "Link to this definition")
Get all mobjects involved in the animation.


Ordering must match the ordering of arguments to interpolate\_submobject


Returns:
The sequence of mobjects.


Return type:
Sequence\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


init\_run\_time(*run\_time*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.init_run_time)[¶](#manim.animation.composition.AnimationGroup.init_run_time "Link to this definition")
Calculates the run time of the animation, if different from `run_time`.


Parameters:
**run\_time** – The duration of the animation in seconds.


Returns:
The duration of the animation in seconds.


Return type:
run\_time


interpolate(*alpha*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.interpolate)[¶](#manim.animation.composition.AnimationGroup.interpolate "Link to this definition")
Set the animation progress.


This method gets called for every frame during an animation.


Parameters:
**alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.


Return type:
None


update\_mobjects(*dt*)[\[source]](../_modules/manim/animation/composition.html#AnimationGroup.update_mobjects)[¶](#manim.animation.composition.AnimationGroup.update_mobjects "Link to this definition")
Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.


Parameters:
**dt** (*float*)


Return type:
None



---

# LaggedStart


# LaggedStart[¶](#laggedstart "Link to this heading")


Qualified name: `manim.animation.composition.LaggedStart`


*class* LaggedStart(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/composition.html#LaggedStart)[¶](#manim.animation.composition.LaggedStart "Link to this definition")
Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")


Adjusts the timing of a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") according to `lag_ratio`.


Parameters:
* **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – Sequence of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.
* **lag\_ratio** (*float*) – 

Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
`n.nn` means the next animation will play when `nnn%` of the current animation has played.
Defaults to 0\.05, meaning that the next animation will begin when 5% of the current
animation has played.


This does not influence the total runtime of the animation. Instead the runtime
of individual animations is adjusted so that the complete animation has the defined
run time.


Examples


Example: LaggedStartExample [¶](#laggedstartexample)


```
from manim import *

class LaggedStartExample(Scene):
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP * 2,
            end=LEFT + DOWN * 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT * 4),
            dot2.animate.shift(RIGHT * 4),
            dot3.animate.shift(RIGHT * 4),
            lag_ratio=0.25,
            run_time=4
        ))

```


```

class LaggedStartExample(Scene):
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP * 2,
            end=LEFT + DOWN * 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT * 4),
            dot2.animate.shift(RIGHT * 4),
            dot3.animate.shift(RIGHT * 4),
            lag_ratio=0.25,
            run_time=4
        ))


```
Methods



---

# LaggedStartMap


# LaggedStartMap[¶](#laggedstartmap "Link to this heading")


Qualified name: `manim.animation.composition.LaggedStartMap`


*class* LaggedStartMap(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/composition.html#LaggedStartMap)[¶](#manim.animation.composition.LaggedStartMap "Link to this definition")
Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart")


Plays a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") while mapping a function to submobjects.


Parameters:
* **AnimationClass** (*Callable**\[**...**,* [*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") to apply to mobject.
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") whose submobjects the animation, and optionally the function,
are to be applied.
* **arg\_creator** (*Callable**\[**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *str**]*) – Function which will be applied to [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **run\_time** (*float*) – The duration of the animation in seconds.


Examples


Example: LaggedStartMapExample [¶](#laggedstartmapexample)


```
from manim import *

class LaggedStartMapExample(Scene):
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            *[Dot(radius=0.16) for _ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 2
            ))

```


```

class LaggedStartMapExample(Scene):
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            *[Dot(radius=0.16) for _ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 2
            ))


```
Methods



---

# Succession


# Succession[¶](#succession "Link to this heading")


Qualified name: `manim.animation.composition.Succession`


*class* Succession(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/composition.html#Succession)[¶](#manim.animation.composition.Succession "Link to this definition")
Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")


Plays a series of animations in succession.


Parameters:
* **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – Sequence of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.
* **lag\_ratio** (*float*) – 

Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
`n.nn` means the next animation will play when `nnn%` of the current animation has played.
Defaults to 1\.0, meaning that the next animation will begin when 100% of the current
animation has played.


This does not influence the total runtime of the animation. Instead the runtime
of individual animations is adjusted so that the complete animation has the defined
run time.


Examples


Example: SuccessionExample [¶](#successionexample)


```
from manim import *

class SuccessionExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))

```


```

class SuccessionExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))


```
Methods


| [`begin`](#manim.animation.composition.Succession.begin "manim.animation.composition.Succession.begin") | Begin the animation. |
| --- | --- |
| [`finish`](#manim.animation.composition.Succession.finish "manim.animation.composition.Succession.finish") | Finish the animation. |
| [`interpolate`](#manim.animation.composition.Succession.interpolate "manim.animation.composition.Succession.interpolate") | Set the animation progress. |
| [`next_animation`](#manim.animation.composition.Succession.next_animation "manim.animation.composition.Succession.next_animation") | Proceeds to the next animation. |
| `update_active_animation` |  |
| [`update_mobjects`](#manim.animation.composition.Succession.update_mobjects "manim.animation.composition.Succession.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |


\_setup\_scene(*scene*)[\[source]](../_modules/manim/animation/composition.html#Succession._setup_scene)[¶](#manim.animation.composition.Succession._setup_scene "Link to this definition")
Setup up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.


This includes to [`add()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.


Parameters:
**scene** – The scene the animation should be cleaned up from.


Return type:
None


begin()[\[source]](../_modules/manim/animation/composition.html#Succession.begin)[¶](#manim.animation.composition.Succession.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


finish()[\[source]](../_modules/manim/animation/composition.html#Succession.finish)[¶](#manim.animation.composition.Succession.finish "Link to this definition")
Finish the animation.


This method gets called when the animation is over.


Return type:
None


interpolate(*alpha*)[\[source]](../_modules/manim/animation/composition.html#Succession.interpolate)[¶](#manim.animation.composition.Succession.interpolate "Link to this definition")
Set the animation progress.


This method gets called for every frame during an animation.


Parameters:
**alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.


Return type:
None


next\_animation()[\[source]](../_modules/manim/animation/composition.html#Succession.next_animation)[¶](#manim.animation.composition.Succession.next_animation "Link to this definition")
Proceeds to the next animation.


This method is called right when the active animation finishes.


Return type:
None


update\_mobjects(*dt*)[\[source]](../_modules/manim/animation/composition.html#Succession.update_mobjects)[¶](#manim.animation.composition.Succession.update_mobjects "Link to this definition")
Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.


Parameters:
**dt** (*float*)


Return type:
None



---

# creation


# creation[¶](#module-manim.animation.creation "Link to this heading")


Animate the display or removal of a mobject from a scene.


Classes


| [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter") | Show a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") letter by letter on the scene. |
| --- | --- |
| [`AddTextWordByWord`](manim.animation.creation.AddTextWordByWord.html#manim.animation.creation.AddTextWordByWord "manim.animation.creation.AddTextWordByWord") | Show a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") word by word on the scene. |
| [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") | Incrementally show a VMobject. |
| [`DrawBorderThenFill`](manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill") | Draw the border first and then show the fill. |
| [`RemoveTextLetterByLetter`](manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter "manim.animation.creation.RemoveTextLetterByLetter") | Remove a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") letter by letter from the scene. |
| [`ShowIncreasingSubsets`](manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets "manim.animation.creation.ShowIncreasingSubsets") | Show one submobject at a time, leaving all previous ones displayed on screen. |
| [`ShowPartial`](manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial") | Abstract class for Animations that show the VMobject partially. |
| [`ShowSubmobjectsOneByOne`](manim.animation.creation.ShowSubmobjectsOneByOne.html#manim.animation.creation.ShowSubmobjectsOneByOne "manim.animation.creation.ShowSubmobjectsOneByOne") | Show one submobject at a time, removing all previously displayed ones from screen. |
| [`SpiralIn`](manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn "manim.animation.creation.SpiralIn") | Create the Mobject with sub\-Mobjects flying in on spiral trajectories. |
| [`Uncreate`](manim.animation.creation.Uncreate.html#manim.animation.creation.Uncreate "manim.animation.creation.Uncreate") | Like [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") but in reverse. |
| [`Unwrite`](manim.animation.creation.Unwrite.html#manim.animation.creation.Unwrite "manim.animation.creation.Unwrite") | Simulate erasing by hand a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). |
| [`Write`](manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write") | Simulate hand\-writing a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or hand\-drawing a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). |



---

# Create


# Create[¶](#create "Link to this heading")


Qualified name: `manim.animation.creation.Create`


*class* Create(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/creation.html#Create)[¶](#manim.animation.creation.Create "Link to this definition")
Bases: [`ShowPartial`](manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial")


Incrementally show a VMobject.


Parameters:
* **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *OpenGLVMobject* *\|* *OpenGLSurface*) – The VMobject to animate.
* **lag\_ratio** (*float*)
* **introducer** (*bool*)


Raises:
**TypeError** – If `mobject` is not an instance of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


Examples


Example: CreateScene [¶](#createscene)


```
from manim import *

class CreateScene(Scene):
    def construct(self):
        self.play(Create(Square()))

```


```

class CreateScene(Scene):
    def construct(self):
        self.play(Create(Square()))


```

See also


[`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")


Methods



---

# DrawBorderThenFill


# DrawBorderThenFill[¶](#drawborderthenfill "Link to this heading")


Qualified name: `manim.animation.creation.DrawBorderThenFill`


*class* DrawBorderThenFill(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill)[¶](#manim.animation.creation.DrawBorderThenFill "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


Draw the border first and then show the fill.


Examples


Example: ShowDrawBorderThenFill [¶](#showdrawborderthenfill)


```
from manim import *

class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))

```


```

class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))


```
Methods


| [`begin`](#manim.animation.creation.DrawBorderThenFill.begin "manim.animation.creation.DrawBorderThenFill.begin") | Begin the animation. |
| --- | --- |
| [`get_all_mobjects`](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "manim.animation.creation.DrawBorderThenFill.get_all_mobjects") | Get all mobjects involved in the animation. |
| `get_outline` |  |
| `get_stroke_color` |  |
| `interpolate_submobject` |  |


Parameters:
* **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *OpenGLVMobject*)
* **run\_time** (*float*)
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*)
* **stroke\_width** (*float*)
* **stroke\_color** (*str*)
* **draw\_border\_animation\_config** (*dict*)
* **fill\_animation\_config** (*dict*)
* **introducer** (*bool*)


begin()[\[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill.begin)[¶](#manim.animation.creation.DrawBorderThenFill.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


get\_all\_mobjects()[\[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill.get_all_mobjects)[¶](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "Link to this definition")
Get all mobjects involved in the animation.


Ordering must match the ordering of arguments to interpolate\_submobject


Returns:
The sequence of mobjects.


Return type:
Sequence\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]



---

# SpiralIn


# SpiralIn[¶](#spiralin "Link to this heading")


Qualified name: `manim.animation.creation.SpiralIn`


*class* SpiralIn(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/creation.html#SpiralIn)[¶](#manim.animation.creation.SpiralIn "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


Create the Mobject with sub\-Mobjects flying in on spiral trajectories.


Parameters:
* **shapes** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobject on which to be operated.
* **scale\_factor** (*float*) – The factor used for scaling the effect.
* **fade\_in\_fraction** – Fractional duration of initial fade\-in of sub\-Mobjects as they fly inward.


Examples


Example: SpiralInExample [¶](#spiralinexample)


```
from manim import *

class SpiralInExample(Scene):
    def construct(self):
        pi = MathTex(r"\pi").scale(7)
        pi.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
        square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
        shapes = VGroup(pi, circle, square)
        self.play(SpiralIn(shapes))

```


```

class SpiralInExample(Scene):
    def construct(self):
        pi = MathTex(r"\pi").scale(7)
        pi.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
        square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
        shapes = VGroup(pi, circle, square)
        self.play(SpiralIn(shapes))


```
Methods


| [`interpolate_mobject`](#manim.animation.creation.SpiralIn.interpolate_mobject "manim.animation.creation.SpiralIn.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |
| --- | --- |


interpolate\_mobject(*alpha*)[\[source]](../_modules/manim/animation/creation.html#SpiralIn.interpolate_mobject)[¶](#manim.animation.creation.SpiralIn.interpolate_mobject "Link to this definition")
Interpolates the mobject of the `Animation` based on alpha value.


Parameters:
**alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha\-values of 0, 0\.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.


Return type:
None



---

# Write


# Write[¶](#write "Link to this heading")


Qualified name: `manim.animation.creation.Write`


*class* Write(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/creation.html#Write)[¶](#manim.animation.creation.Write "Link to this definition")
Bases: [`DrawBorderThenFill`](manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill")


Simulate hand\-writing a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or hand\-drawing a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


Examples


Example: ShowWrite [¶](#showwrite)


```
from manim import *

class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144)))

```


```

class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144)))


```

Example: ShowWriteReversed [¶](#showwritereversed)


```
from manim import *

class ShowWriteReversed(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))

```


```

class ShowWriteReversed(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))


```
Tests


Check that creating empty [`Write`](#manim.animation.creation.Write "manim.animation.creation.Write") animations works:


```
>>> from manim import Write, Text
>>> Write(Text(''))
Write(Text(''))

```


Methods


| [`begin`](#manim.animation.creation.Write.begin "manim.animation.creation.Write.begin") | Begin the animation. |
| --- | --- |
| [`finish`](#manim.animation.creation.Write.finish "manim.animation.creation.Write.finish") | Finish the animation. |
| `reverse_submobjects` |  |


Parameters:
* **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *OpenGLVMobject*)
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*)
* **reverse** (*bool*)


begin()[\[source]](../_modules/manim/animation/creation.html#Write.begin)[¶](#manim.animation.creation.Write.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


finish()[\[source]](../_modules/manim/animation/creation.html#Write.finish)[¶](#manim.animation.creation.Write.finish "Link to this definition")
Finish the animation.


This method gets called when the animation is over.


Return type:
None



---

# Unwrite


# Unwrite[¶](#unwrite "Link to this heading")


Qualified name: `manim.animation.creation.Unwrite`


*class* Unwrite(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/creation.html#Unwrite)[¶](#manim.animation.creation.Unwrite "Link to this definition")
Bases: [`Write`](manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")


Simulate erasing by hand a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


Parameters:
* **reverse** (*bool*) – Set True to have the animation start erasing from the last submobject first.
* **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*)


Examples


Example: UnwriteReverseTrue [¶](#unwritereversetrue)


```
from manim import *

class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))

```


```

class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))


```

Example: UnwriteReverseFalse [¶](#unwritereversefalse)


```
from manim import *

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text, reverse=False))

```


```

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text, reverse=False))


```
Methods



---

# FadeIn


# FadeIn[¶](#fadein "Link to this heading")


Qualified name: `manim.animation.fading.FadeIn`


*class* FadeIn(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/fading.html#FadeIn)[¶](#manim.animation.fading.FadeIn "Link to this definition")
Bases: `_Fade`


Fade in [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s.


Parameters:
* **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be faded in.
* **shift** – The vector by which the mobject shifts while being faded in.
* **target\_position** – The position from which the mobject starts while being faded in. In case
another mobject is given as target position, its center is used.
* **scale** – The factor by which the mobject is scaled initially before being rescaling to
its original size while being faded in.


Examples


Example: FadeInExample [¶](#fadeinexample)


```
from manim import *

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeIn with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeIn(tex[0]),
            FadeIn(tex[1], shift=DOWN),
            FadeIn(tex[2], target_position=dot),
            FadeIn(tex[3], scale=1.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

```


```

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeIn with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeIn(tex[0]),
            FadeIn(tex[1], shift=DOWN),
            FadeIn(tex[2], target_position=dot),
            FadeIn(tex[3], scale=1.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


```
Methods


| `create_starting_mobject` |  |
| --- | --- |
| `create_target` |  |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# FadeOut


# FadeOut[¶](#fadeout "Link to this heading")


Qualified name: `manim.animation.fading.FadeOut`


*class* FadeOut(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/fading.html#FadeOut)[¶](#manim.animation.fading.FadeOut "Link to this definition")
Bases: `_Fade`


Fade out [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s.


Parameters:
* **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be faded out.
* **shift** – The vector by which the mobject shifts while being faded out.
* **target\_position** – The position to which the mobject moves while being faded out. In case another
mobject is given as target position, its center is used.
* **scale** – The factor by which the mobject is scaled while being faded out.


Examples


Example: FadeInExample [¶](#fadeinexample)


```
from manim import *

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeOut with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeOut(tex[0]),
            FadeOut(tex[1], shift=DOWN),
            FadeOut(tex[2], target_position=dot),
            FadeOut(tex[3], scale=0.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

```


```

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeOut with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeOut(tex[0]),
            FadeOut(tex[1], shift=DOWN),
            FadeOut(tex[2], target_position=dot),
            FadeOut(tex[3], scale=0.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


```
Methods


| [`clean_up_from_scene`](#manim.animation.fading.FadeOut.clean_up_from_scene "manim.animation.fading.FadeOut.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| --- | --- |
| `create_target` |  |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |


clean\_up\_from\_scene(*scene\=None*)[\[source]](../_modules/manim/animation/fading.html#FadeOut.clean_up_from_scene)[¶](#manim.animation.fading.FadeOut.clean_up_from_scene "Link to this definition")
Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.


This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None



---

# GrowArrow


# GrowArrow[¶](#growarrow "Link to this heading")


Qualified name: `manim.animation.growing.GrowArrow`


*class* GrowArrow(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/growing.html#GrowArrow)[¶](#manim.animation.growing.GrowArrow "Link to this definition")
Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")


Introduce an [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") by growing it from its start toward its tip.


Parameters:
* **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow to be introduced.
* **point\_color** (*str*) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.


Examples


Example: GrowArrowExample [¶](#growarrowexample)


```
from manim import *

class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))

```


```

class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))


```
Methods


| `create_starting_mobject` |  |
| --- | --- |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# Rotate


# Rotate[¶](#rotate "Link to this heading")


Qualified name: `manim.animation.rotation.Rotate`


*class* Rotate(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/rotation.html#Rotate)[¶](#manim.animation.rotation.Rotate "Link to this definition")
Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")


Animation that rotates a Mobject.


Parameters:
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be rotated.
* **angle** (*float*) – The rotation angle.
* **axis** (*np.ndarray*) – The rotation axis as a numpy vector.
* **about\_point** (*Sequence**\[**float**]* *\|* *None*) – The rotation center.
* **about\_edge** (*Sequence**\[**float**]* *\|* *None*) – If `about_point` is `None`, this argument specifies
the direction of the bounding box point to be taken as
the rotation center.


Examples


Example: UsingRotate [¶](#usingrotate)


```
from manim import *

class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )

```


```

class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )


```
Methods


| `create_target` |  |
| --- | --- |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# Rotating


# Rotating[¶](#rotating "Link to this heading")


Qualified name: `manim.animation.rotation.Rotating`


*class* Rotating(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/rotation.html#Rotating)[¶](#manim.animation.rotation.Rotating "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


Methods


| [`interpolate_mobject`](#manim.animation.rotation.Rotating.interpolate_mobject "manim.animation.rotation.Rotating.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |
| --- | --- |


Parameters:
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **axis** (*np.ndarray*)
* **radians** (*np.ndarray*)
* **about\_point** (*np.ndarray* *\|* *None*)
* **about\_edge** (*np.ndarray* *\|* *None*)
* **run\_time** (*float*)
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*)


interpolate\_mobject(*alpha*)[\[source]](../_modules/manim/animation/rotation.html#Rotating.interpolate_mobject)[¶](#manim.animation.rotation.Rotating.interpolate_mobject "Link to this definition")
Interpolates the mobject of the `Animation` based on alpha value.


Parameters:
**alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha\-values of 0, 0\.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.


Return type:
None



---

# transform


# transform[¶](#module-manim.animation.transform "Link to this heading")


Animations transforming one mobject into another.


Classes


| [`ApplyComplexFunction`](manim.animation.transform.ApplyComplexFunction.html#manim.animation.transform.ApplyComplexFunction "manim.animation.transform.ApplyComplexFunction") |  |
| --- | --- |
| [`ApplyFunction`](manim.animation.transform.ApplyFunction.html#manim.animation.transform.ApplyFunction "manim.animation.transform.ApplyFunction") |  |
| [`ApplyMatrix`](manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix "manim.animation.transform.ApplyMatrix") | Applies a matrix transform to an mobject. |
| [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod") | Animates a mobject by applying a method. |
| [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction") | Animation that applies a pointwise function to a mobject. |
| [`ApplyPointwiseFunctionToCenter`](manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter "manim.animation.transform.ApplyPointwiseFunctionToCenter") |  |
| [`ClockwiseTransform`](manim.animation.transform.ClockwiseTransform.html#manim.animation.transform.ClockwiseTransform "manim.animation.transform.ClockwiseTransform") | Transforms the points of a mobject along a clockwise oriented arc. |
| [`CounterclockwiseTransform`](manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform "manim.animation.transform.CounterclockwiseTransform") | Transforms the points of a mobject along a counterclockwise oriented arc. |
| [`CyclicReplace`](manim.animation.transform.CyclicReplace.html#manim.animation.transform.CyclicReplace "manim.animation.transform.CyclicReplace") | An animation moving mobjects cyclically. |
| [`FadeToColor`](manim.animation.transform.FadeToColor.html#manim.animation.transform.FadeToColor "manim.animation.transform.FadeToColor") | Animation that changes color of a mobject. |
| [`FadeTransform`](manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform") | Fades one mobject into another. |
| [`FadeTransformPieces`](manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces "manim.animation.transform.FadeTransformPieces") | Fades submobjects of one mobject into submobjects of another one. |
| [`MoveToTarget`](manim.animation.transform.MoveToTarget.html#manim.animation.transform.MoveToTarget "manim.animation.transform.MoveToTarget") | Transforms a mobject to the mobject stored in its `target` attribute. |
| [`ReplacementTransform`](manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform") | Replaces and morphs a mobject into a target mobject. |
| [`Restore`](manim.animation.transform.Restore.html#manim.animation.transform.Restore "manim.animation.transform.Restore") | Transforms a mobject to its last saved state. |
| [`ScaleInPlace`](manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace "manim.animation.transform.ScaleInPlace") | Animation that scales a mobject by a certain factor. |
| [`ShrinkToCenter`](manim.animation.transform.ShrinkToCenter.html#manim.animation.transform.ShrinkToCenter "manim.animation.transform.ShrinkToCenter") | Animation that makes a mobject shrink to center. |
| [`Swap`](manim.animation.transform.Swap.html#manim.animation.transform.Swap "manim.animation.transform.Swap") |  |
| [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") | A Transform transforms a Mobject into a target Mobject. |
| [`TransformAnimations`](manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations "manim.animation.transform.TransformAnimations") |  |
| [`TransformFromCopy`](manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy "manim.animation.transform.TransformFromCopy") | Performs a reversed Transform |



---

# ApplyComplexFunction


# ApplyComplexFunction[¶](#applycomplexfunction "Link to this heading")


Qualified name: `manim.animation.transform.ApplyComplexFunction`


*class* ApplyComplexFunction(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#ApplyComplexFunction)[¶](#manim.animation.transform.ApplyComplexFunction "Link to this definition")
Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")


Methods


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |


Parameters:
* **function** (*types.MethodType*)
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))



---

# ApplyFunction


# ApplyFunction[¶](#applyfunction "Link to this heading")


Qualified name: `manim.animation.transform.ApplyFunction`


*class* ApplyFunction(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#ApplyFunction)[¶](#manim.animation.transform.ApplyFunction "Link to this definition")
Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")


Methods


| `create_target` |  |
| --- | --- |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |


Parameters:
* **function** (*types.MethodType*)
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))



---

# ApplyMatrix


# ApplyMatrix[¶](#applymatrix "Link to this heading")


Qualified name: `manim.animation.transform.ApplyMatrix`


*class* ApplyMatrix(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#ApplyMatrix)[¶](#manim.animation.transform.ApplyMatrix "Link to this definition")
Bases: [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction")


Applies a matrix transform to an mobject.


Parameters:
* **matrix** (*np.ndarray*) – The transformation matrix.
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **about\_point** (*np.ndarray*) – The origin point for the transform. Defaults to `ORIGIN`.
* **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction").


Examples


Example: ApplyMatrixExample [¶](#applymatrixexample)


```
from manim import *

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

```


```

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))


```
Methods


| `initialize_matrix` |  |
| --- | --- |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# ApplyMethod


# ApplyMethod[¶](#applymethod "Link to this heading")


Qualified name: `manim.animation.transform.ApplyMethod`


*class* ApplyMethod(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#ApplyMethod)[¶](#manim.animation.transform.ApplyMethod "Link to this definition")
Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")


Animates a mobject by applying a method.


Note that only the method needs to be passed to this animation,
it is not required to pass the corresponding mobject. Furthermore,
this animation class only works if the method returns the modified
mobject.


Parameters:
* **method** (*Callable*) – The method that will be applied in the animation.
* **args** – Any positional arguments to be passed when applying the method.
* **kwargs** – Any keyword arguments passed to [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").


Methods


| `check_validity_of_input` |  |
| --- | --- |
| `create_target` |  |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# ApplyPointwiseFunction


# ApplyPointwiseFunction[¶](#applypointwisefunction "Link to this heading")


Qualified name: `manim.animation.transform.ApplyPointwiseFunction`


*class* ApplyPointwiseFunction(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#ApplyPointwiseFunction)[¶](#manim.animation.transform.ApplyPointwiseFunction "Link to this definition")
Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")


Animation that applies a pointwise function to a mobject.


Examples


Example: WarpSquare [¶](#warpsquare)


```
from manim import *

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()

```


```

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()


```
Methods


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |


Parameters:
* **function** (*types.MethodType*)
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **run\_time** (*float*)



---

# CyclicReplace


# CyclicReplace[¶](#cyclicreplace "Link to this heading")


Qualified name: `manim.animation.transform.CyclicReplace`


*class* CyclicReplace(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#CyclicReplace)[¶](#manim.animation.transform.CyclicReplace "Link to this definition")
Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")


An animation moving mobjects cyclically.


In particular, this means: the first mobject takes the place
of the second mobject, the second one takes the place of
the third mobject, and so on. The last mobject takes the
place of the first one.


Parameters:
* **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – List of mobjects to be transformed.
* **path\_arc** (*float*) – The angle of the arc (in radians) that the mobjects will follow to reach
their target.
* **kwargs** – Further keyword arguments that are passed to [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").


Examples


Example: CyclicReplaceExample [¶](#cyclicreplaceexample)


```
from manim import *

class CyclicReplaceExample(Scene):
    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(), Star())
        group.arrange(RIGHT)
        self.add(group)

        for _ in range(4):
            self.play(CyclicReplace(*group))

```


```

class CyclicReplaceExample(Scene):
    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(), Star())
        group.arrange(RIGHT)
        self.add(group)

        for _ in range(4):
            self.play(CyclicReplace(*group))


```
Methods


| `create_target` |  |
| --- | --- |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |



---

# Transform


# Transform[¶](#transform "Link to this heading")


Qualified name: `manim.animation.transform.Transform`


*class* Transform(*mobject\=None*, *\*args*, *use\_override\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/animation/transform.html#Transform)[¶](#manim.animation.transform.Transform "Link to this definition")
Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")


A Transform transforms a Mobject into a target Mobject.


Parameters:
* **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *\|* *None*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed. It will be mutated to become the `target_mobject`.
* **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *\|* *None*) – The target of the transformation.
* **path\_func** (*Callable* *\|* *None*) – A function defining the path that the points of the `mobject` are being moved
along until they match the points of the `target_mobject`, see [`utils.paths`](manim.utils.paths.html#module-manim.utils.paths "manim.utils.paths").
* **path\_arc** (*float*) – The arc angle (in radians) that the points of `mobject` will follow to reach
the points of the target if using a circular path arc, see `path_arc_centers`.
See also [`manim.utils.paths.path_along_arc()`](manim.utils.paths.html#manim.utils.paths.path_along_arc "manim.utils.paths.path_along_arc").
* **path\_arc\_axis** (*np.ndarray*) – The axis to rotate along if using a circular path arc, see `path_arc_centers`.
* **path\_arc\_centers** (*np.ndarray*) – 

The center of the circular arcs along which the points of `mobject` are
moved by the transformation.


If this is set and `path_func` is not set, then a `path_along_circles` path will be generated
using the `path_arc` parameters and stored in `path_func`. If `path_func` is set, this and the
other `path_arc` fields are set as attributes, but a `path_func` is not generated from it.
* **replace\_mobject\_with\_target\_in\_scene** (*bool*) – 

Controls which mobject is replaced when the transformation is complete.


If set to True, `mobject` will be removed from the scene and `target_mobject` will
replace it. Otherwise, `target_mobject` is never added and `mobject` just takes its shape.


Examples


Example: TransformPathArc [¶](#transformpatharc)


```
from manim import *

class TransformPathArc(Scene):
    def construct(self):
        def make_arc_path(start, end, arc_angle):
            points = []
            p_fn = path_along_arc(arc_angle)
            # alpha animates between 0.0 and 1.0, where 0.0
            # is the beginning of the animation and 1.0 is the end.
            for alpha in range(0, 11):
                points.append(p_fn(start, end, alpha / 10.0))
            path = VMobject(stroke_color=YELLOW)
            path.set_points_smoothly(points)
            return path

        left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
        # Positive angles move counter-clockwise, negative angles move clockwise.
        examples = [-90, 0, 30, 90, 180, 270]
        anims = []
        for idx, angle in enumerate(examples):
            left_c = left.copy().shift((3 - idx) * UP)
            left_c.fill_color = colors[idx]
            right_c = left_c.copy().shift(4 * RIGHT)
            path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                     arc_angle=angle * DEGREES)
            desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
            # Make the circles in front of the text in front of the arcs.
            self.add(
                path_arc.set_z_index(1),
                desc.set_z_index(2),
                left_c.set_z_index(3),
            )
            anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

        self.play(*anims, run_time=2)
        self.wait()

```


```

class TransformPathArc(Scene):
    def construct(self):
        def make_arc_path(start, end, arc_angle):
            points = []
            p_fn = path_along_arc(arc_angle)
            # alpha animates between 0.0 and 1.0, where 0.0
            # is the beginning of the animation and 1.0 is the end.
            for alpha in range(0, 11):
                points.append(p_fn(start, end, alpha / 10.0))
            path = VMobject(stroke_color=YELLOW)
            path.set_points_smoothly(points)
            return path

        left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
        # Positive angles move counter-clockwise, negative angles move clockwise.
        examples = [-90, 0, 30, 90, 180, 270]
        anims = []
        for idx, angle in enumerate(examples):
            left_c = left.copy().shift((3 - idx) * UP)
            left_c.fill_color = colors[idx]
            right_c = left_c.copy().shift(4 * RIGHT)
            path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                     arc_angle=angle * DEGREES)
            desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
            # Make the circles in front of the text in front of the arcs.
            self.add(
                path_arc.set_z_index(1),
                desc.set_z_index(2),
                left_c.set_z_index(3),
            )
            anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

        self.play(*anims, run_time=2)
        self.wait()


```
Methods


| [`begin`](#manim.animation.transform.Transform.begin "manim.animation.transform.Transform.begin") | Begin the animation. |
| --- | --- |
| [`clean_up_from_scene`](#manim.animation.transform.Transform.clean_up_from_scene "manim.animation.transform.Transform.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| `create_target` |  |
| `get_all_families_zipped` |  |
| [`get_all_mobjects`](#manim.animation.transform.Transform.get_all_mobjects "manim.animation.transform.Transform.get_all_mobjects") | Get all mobjects involved in the animation. |
| `interpolate_submobject` |  |


Attributes


| `path_arc` |  |
| --- | --- |
| `path_func` |  |


begin()[\[source]](../_modules/manim/animation/transform.html#Transform.begin)[¶](#manim.animation.transform.Transform.begin "Link to this definition")
Begin the animation.


This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.


Return type:
None


clean\_up\_from\_scene(*scene*)[\[source]](../_modules/manim/animation/transform.html#Transform.clean_up_from_scene)[¶](#manim.animation.transform.Transform.clean_up_from_scene "Link to this definition")
Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.


This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.


Parameters:
**scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.


Return type:
None


get\_all\_mobjects()[\[source]](../_modules/manim/animation/transform.html#Transform.get_all_mobjects)[¶](#manim.animation.transform.Transform.get_all_mobjects "Link to this definition")
Get all mobjects involved in the animation.


Ordering must match the ordering of arguments to interpolate\_submobject


Returns:
The sequence of mobjects.


Return type:
Sequence\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]



---

# Mobjects


# Mobjects[¶](#mobjects "Link to this heading")


| [`frame`](../reference/manim.mobject.frame.html#module-manim.mobject.frame "manim.mobject.frame") | Special rectangles. |
| --- | --- |
| [`geometry`](../reference/manim.mobject.geometry.html#module-manim.mobject.geometry "manim.mobject.geometry") | Various geometric Mobjects. |
| [`graph`](../reference/manim.mobject.graph.html#module-manim.mobject.graph "manim.mobject.graph") | Mobjects used to represent mathematical graphs (think graph theory, not plotting). |
| [`graphing`](../reference/manim.mobject.graphing.html#module-manim.mobject.graphing "manim.mobject.graphing") | Coordinate systems and function graphing related mobjects. |
| [`logo`](../reference/manim.mobject.logo.html#module-manim.mobject.logo "manim.mobject.logo") | Utilities for Manim's logo and banner. |
| [`matrix`](../reference/manim.mobject.matrix.html#module-manim.mobject.matrix "manim.mobject.matrix") | Mobjects representing matrices. |
| [`mobject`](../reference/manim.mobject.mobject.html#module-manim.mobject.mobject "manim.mobject.mobject") | Base classes for objects that can be displayed. |
| [`svg`](../reference/manim.mobject.svg.html#module-manim.mobject.svg "manim.mobject.svg") | Mobjects related to SVG images. |
| [`table`](../reference/manim.mobject.table.html#module-manim.mobject.table "manim.mobject.table") | Mobjects representing tables. |
| [`text`](../reference/manim.mobject.text.html#module-manim.mobject.text "manim.mobject.text") | Mobjects used to display Text using Pango or LaTeX. |
| [`three_d`](../reference/manim.mobject.three_d.html#module-manim.mobject.three_d "manim.mobject.three_d") | Three\-dimensional mobjects. |
| [`types`](../reference/manim.mobject.types.html#module-manim.mobject.types "manim.mobject.types") | Specialized mobject base classes. |
| [`utils`](../reference/manim.mobject.utils.html#module-manim.mobject.utils "manim.mobject.utils") | Utilities for working with mobjects. |
| [`value_tracker`](../reference/manim.mobject.value_tracker.html#module-manim.mobject.value_tracker "manim.mobject.value_tracker") | Simple mobjects that can be used for storing (and updating) a value. |
| [`vector_field`](../reference/manim.mobject.vector_field.html#module-manim.mobject.vector_field "manim.mobject.vector_field") | Mobjects representing vector fields. |



---

# FullScreenRectangle


# FullScreenRectangle[¶](#fullscreenrectangle "Link to this heading")


Qualified name: `manim.mobject.frame.FullScreenRectangle`


*class* FullScreenRectangle(*\*\*kwargs*)[\[source]](../_modules/manim/mobject/frame.html#FullScreenRectangle)[¶](#manim.mobject.frame.FullScreenRectangle "Link to this definition")
Bases: [`ScreenRectangle`](manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle "manim.mobject.frame.ScreenRectangle")


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `aspect_ratio` | The aspect ratio. |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*\*kwargs*)[¶](#manim.mobject.frame.FullScreenRectangle._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.



---

# ScreenRectangle


# ScreenRectangle[¶](#screenrectangle "Link to this heading")


Qualified name: `manim.mobject.frame.ScreenRectangle`


*class* ScreenRectangle(*aspect\_ratio\=1\.7777777777777777*, *height\=4*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/frame.html#ScreenRectangle)[¶](#manim.mobject.frame.ScreenRectangle "Link to this definition")
Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| [`aspect_ratio`](#manim.mobject.frame.ScreenRectangle.aspect_ratio "manim.mobject.frame.ScreenRectangle.aspect_ratio") | The aspect ratio. |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*aspect\_ratio\=1\.7777777777777777*, *height\=4*, *\*\*kwargs*)[¶](#manim.mobject.frame.ScreenRectangle._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


*property* aspect\_ratio[¶](#manim.mobject.frame.ScreenRectangle.aspect_ratio "Link to this definition")
The aspect ratio.


When set, the width is stretched to accommodate
the new aspect ratio.



---

# geometry


# geometry[¶](#module-manim.mobject.geometry "Link to this heading")


Various geometric Mobjects.


## Modules[¶](#modules "Link to this heading")


| [`arc`](manim.mobject.geometry.arc.html#module-manim.mobject.geometry.arc "manim.mobject.geometry.arc") | Mobjects that are curved. |
| --- | --- |
| [`boolean_ops`](manim.mobject.geometry.boolean_ops.html#module-manim.mobject.geometry.boolean_ops "manim.mobject.geometry.boolean_ops") | Boolean operations for two\-dimensional mobjects. |
| [`labeled`](manim.mobject.geometry.labeled.html#module-manim.mobject.geometry.labeled "manim.mobject.geometry.labeled") | Mobjects that inherit from lines and contain a label along the length. |
| [`line`](manim.mobject.geometry.line.html#module-manim.mobject.geometry.line "manim.mobject.geometry.line") | Mobjects that are lines or variations of them. |
| [`polygram`](manim.mobject.geometry.polygram.html#module-manim.mobject.geometry.polygram "manim.mobject.geometry.polygram") | Mobjects that are simple geometric shapes. |
| [`shape_matchers`](manim.mobject.geometry.shape_matchers.html#module-manim.mobject.geometry.shape_matchers "manim.mobject.geometry.shape_matchers") | Mobjects used to mark and annotate other mobjects. |
| [`tips`](manim.mobject.geometry.tips.html#module-manim.mobject.geometry.tips "manim.mobject.geometry.tips") | A collection of tip mobjects for use with [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject"). |



---

# Arc


# Arc[¶](#arc "Link to this heading")


Qualified name: `manim.mobject.geometry.arc.Arc`


*class* Arc(*radius\=1\.0*, *start\_angle\=0*, *angle\=1\.5707963267948966*, *num\_components\=9*, *arc\_center\=array(\[0\., 0\., 0\.])*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/arc.html#Arc)[¶](#manim.mobject.geometry.arc.Arc "Link to this definition")
Bases: [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject")


A circular arc.


Examples


A simple arc of angle Pi.


Example: ArcExample [¶](#arcexample)

![../_images/ArcExample-1.png](../_images/ArcExample-1.png)

```
from manim import *

class ArcExample(Scene):
    def construct(self):
        self.add(Arc(angle=PI))

```


```

class ArcExample(Scene):
    def construct(self):
        self.add(Arc(angle=PI))


```
Methods


| [`generate_points`](#manim.mobject.geometry.arc.Arc.generate_points "manim.mobject.geometry.arc.Arc.generate_points") | Initializes `points` and therefore the shape. |
| --- | --- |
| [`get_arc_center`](#manim.mobject.geometry.arc.Arc.get_arc_center "manim.mobject.geometry.arc.Arc.get_arc_center") | Looks at the normals to the first two anchors, and finds their intersection points |
| `init_points` |  |
| `move_arc_center_to` |  |
| `stop_angle` |  |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


Parameters:
* **radius** (*float*)
* **start\_angle** (*float*)
* **angle** (*float*)
* **num\_components** (*int*)
* **arc\_center** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))


\_original\_\_init\_\_(*radius\=1\.0*, *start\_angle\=0*, *angle\=1\.5707963267948966*, *num\_components\=9*, *arc\_center\=array(\[0\., 0\., 0\.])*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Arc._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **radius** (*float*)
* **start\_angle** (*float*)
* **angle** (*float*)
* **num\_components** (*int*)
* **arc\_center** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))


generate\_points()[\[source]](../_modules/manim/mobject/geometry/arc.html#Arc.generate_points)[¶](#manim.mobject.geometry.arc.Arc.generate_points "Link to this definition")
Initializes `points` and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.


Return type:
None


get\_arc\_center(*warning\=True*)[\[source]](../_modules/manim/mobject/geometry/arc.html#Arc.get_arc_center)[¶](#manim.mobject.geometry.arc.Arc.get_arc_center "Link to this definition")
Looks at the normals to the first two
anchors, and finds their intersection points


Parameters:
**warning** (*bool*)


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")



---

# ArcBetweenPoints


# ArcBetweenPoints[¶](#arcbetweenpoints "Link to this heading")


Qualified name: `manim.mobject.geometry.arc.ArcBetweenPoints`


*class* ArcBetweenPoints(*start*, *end*, *angle\=1\.5707963267948966*, *radius\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/arc.html#ArcBetweenPoints)[¶](#manim.mobject.geometry.arc.ArcBetweenPoints "Link to this definition")
Bases: [`Arc`](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")


Inherits from Arc and additionally takes 2 points between which the arc is spanned.


Example


Example: ArcBetweenPointsExample [¶](#arcbetweenpointsexample)


```
from manim import *

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))

```


```

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


Parameters:
* **start** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **end** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **angle** (*float*)
* **radius** (*float*)


\_original\_\_init\_\_(*start*, *end*, *angle\=1\.5707963267948966*, *radius\=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.ArcBetweenPoints._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **start** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **end** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **angle** (*float*)
* **radius** (*float*)


Return type:
None



---

# ArcPolygon


# ArcPolygon[¶](#arcpolygon "Link to this heading")


Qualified name: `manim.mobject.geometry.arc.ArcPolygon`


*class* ArcPolygon(*\*vertices*, *angle\=0\.7853981633974483*, *radius\=None*, *arc\_config\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/arc.html#ArcPolygon)[¶](#manim.mobject.geometry.arc.ArcPolygon "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


A generalized polygon allowing for points to be connected with arcs.


This version tries to stick close to the way `Polygon` is used. Points
can be passed to it directly which are used to generate the according arcs
(using [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints")). An angle or radius can be passed to it to
use across all arcs, but to configure arcs individually an `arc_config` list
has to be passed with the syntax explained below.


Parameters:
* **vertices** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")) – A list of vertices, start and end points for the arc segments.
* **angle** (*float*) – The angle used for constructing the arcs. If no other parameters
are set, this angle is used to construct all arcs.
* **radius** (*float* *\|* *None*) – The circle radius used to construct the arcs. If specified,
overrides the specified `angle`.
* **arc\_config** (*list**\[**dict**]* *\|* *None*) – When passing a `dict`, its content will be passed as keyword
arguments to [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints"). Otherwise, a list
of dictionaries containing values that are passed as keyword
arguments for every individual arc can be passed.
* **kwargs** – Further keyword arguments that are passed to the constructor of
[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").


arcs[¶](#manim.mobject.geometry.arc.ArcPolygon.arcs "Link to this definition")
The arcs created from the input parameters:


```
>>> from manim import ArcPolygon
>>> ap = ArcPolygon([0, 0, 0], [2, 0, 0], [0, 2, 0])
>>> ap.arcs
[ArcBetweenPoints, ArcBetweenPoints, ArcBetweenPoints]

```


Type:
`list`


Tip


Two instances of [`ArcPolygon`](#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon") can be transformed properly into one
another as well. Be advised that any arc initialized with `angle=0`
will actually be a straight line, so if a straight section should seamlessly
transform into an arced section or vice versa, initialize the straight section
with a negligible angle instead (such as `angle=0.0001`).


Note


There is an alternative version ([`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.html#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs")) that is instantiated
with pre\-defined arcs.


See also


[`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.html#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs")


Examples


Example: SeveralArcPolygons [¶](#severalarcpolygons)


```
from manim import *

class SeveralArcPolygons(Scene):
    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    arc_config=[{'radius': 1.7, 'color': RED},
                                    {'angle': 20*DEGREES, 'color': BLUE},
                                    {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()

```


```

class SeveralArcPolygons(Scene):
    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    arc_config=[{'radius': 1.7, 'color': RED},
                                    {'angle': 20*DEGREES, 'color': BLUE},
                                    {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()


```
For further examples see [`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.html#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs").


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*vertices*, *angle\=0\.7853981633974483*, *radius\=None*, *arc\_config\=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.ArcPolygon._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **vertices** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **angle** (*float*)
* **radius** (*float* *\|* *None*)
* **arc\_config** (*list**\[**dict**]* *\|* *None*)


Return type:
None



---

# ArcPolygonFromArcs


# ArcPolygonFromArcs[¶](#arcpolygonfromarcs "Link to this heading")


Qualified name: `manim.mobject.geometry.arc.ArcPolygonFromArcs`


*class* ArcPolygonFromArcs(*\*arcs*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/arc.html#ArcPolygonFromArcs)[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


A generalized polygon allowing for points to be connected with arcs.


This version takes in pre\-defined arcs to generate the arcpolygon and introduces
little new syntax. However unlike `Polygon` it can’t be created with points
directly.


For proper appearance the passed arcs should connect seamlessly:
`[a,b][b,c][c,a]`


If there are any gaps between the arcs, those will be filled in
with straight lines, which can be used deliberately for any straight
sections. Arcs can also be passed as straight lines such as an arc
initialized with `angle=0`.


Parameters:
* **arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") *\|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints")) – These are the arcs from which the arcpolygon is assembled.
* **kwargs** – Keyword arguments that are passed to the constructor of
[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"). Affects how the ArcPolygon itself is drawn,
but doesn’t affect passed arcs.


arcs[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs.arcs "Link to this definition")
The arcs used to initialize the ArcPolygonFromArcs:


```
>>> from manim import ArcPolygonFromArcs, Arc, ArcBetweenPoints
>>> ap = ArcPolygonFromArcs(Arc(), ArcBetweenPoints([1,0,0], [0,1,0]), Arc())
>>> ap.arcs
[Arc, ArcBetweenPoints, Arc]

```


Tip


Two instances of [`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon") can be transformed properly into
one another as well. Be advised that any arc initialized with `angle=0`
will actually be a straight line, so if a straight section should seamlessly
transform into an arced section or vice versa, initialize the straight
section with a negligible angle instead (such as `angle=0.0001`).


Note


There is an alternative version ([`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon")) that can be instantiated
with points.


See also


[`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon")


Examples


One example of an arcpolygon is the Reuleaux triangle.
Instead of 3 straight lines connecting the outer points,
a Reuleaux triangle has 3 arcs connecting those points,
making a shape with constant width.


Passed arcs are stored as submobjects in the arcpolygon.
This means that the arcs are changed along with the arcpolygon,
for example when it’s shifted, and these arcs can be manipulated
after the arcpolygon has been initialized.


Also both the arcs contained in an [`ArcPolygonFromArcs`](#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs"), as well as the
arcpolygon itself are drawn, which affects draw time in [`Create`](manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")
for example. In most cases the arcs themselves don’t
need to be drawn, in which case they can be passed as invisible.


Example: ArcPolygonExample [¶](#arcpolygonexample)


```
from manim import *

class ArcPolygonExample(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 0}
        poly_conf = {"stroke_width": 10, "stroke_color": BLUE,
              "fill_opacity": 1, "color": PURPLE}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)

```


```

class ArcPolygonExample(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 0}
        poly_conf = {"stroke_width": 10, "stroke_color": BLUE,
              "fill_opacity": 1, "color": PURPLE}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)


```
The arcpolygon itself can also be hidden so that instead only the contained
arcs are drawn. This can be used to easily debug arcs or to highlight them.


Example: ArcPolygonExample2 [¶](#arcpolygonexample2)


```
from manim import *

class ArcPolygonExample2(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
            "fill_opacity": 0.5, "color": GREEN}
        poly_conf = {"color": None}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)

```


```

class ArcPolygonExample2(Scene):
    def construct(self):
        arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
            "fill_opacity": 0.5, "color": GREEN}
        poly_conf = {"color": None}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*arcs*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.ArcPolygonFromArcs._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
**arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") *\|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints"))


Return type:
None



---

# LabeledArrow


# LabeledArrow[¶](#labeledarrow "Link to this heading")


Qualified name: `manim.mobject.geometry.labeled.LabeledArrow`


*class* LabeledArrow(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/labeled.html#LabeledArrow)[¶](#manim.mobject.geometry.labeled.LabeledArrow "Link to this definition")
Bases: [`LabeledLine`](manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine"), [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")


Constructs an arrow containing a label box somewhere along its length.
This class inherits its label properties from LabeledLine, so the main parameters controlling it are the same.


Parameters:
* **label** (*str* *\|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *\|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *\|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed on the line.
* **label\_position** (*float* *\|* *optional*) – A ratio in the range \[0\-1] to indicate the position of the label with respect to the length of the line. Default value is 0\.5\.
* **font\_size** (*float* *\|* *optional*) – Control font size for the label. This parameter is only used when label is of type str.
* **label\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *optional*) – The color of the label’s text. This parameter is only used when label is of type str.
* **label\_frame** (*Bool* *\|* *optional*) – Add a SurroundingRectangle frame to the label box.
* **frame\_fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *optional*) – Background color to fill the label box. If no value is provided, the background color of the canvas will be used.
* **frame\_fill\_opacity** (*float* *\|* *optional*) – Determine the opacity of the label box by passing a value in the range \[0\-1], where 0 indicates complete transparency and 1 means full opacity.


See also


[`LabeledLine`](manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine")


Examples


Example: LabeledArrowExample [¶](#labeledarrowexample)

![../_images/LabeledArrowExample-1.png](../_images/LabeledArrowExample-1.png)

```
from manim import *

class LabeledArrowExample(Scene):
    def construct(self):
        l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

        self.add(l_arrow)

```


```

class LabeledArrowExample(Scene):
    def construct(self):
        l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

        self.add(l_arrow)


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*args*, *\*\*kwargs*)[¶](#manim.mobject.geometry.labeled.LabeledArrow._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Return type:
None



---

# LabeledLine


# LabeledLine[¶](#labeledline "Link to this heading")


Qualified name: `manim.mobject.geometry.labeled.LabeledLine`


*class* LabeledLine(*label*, *label\_position\=0\.5*, *font\_size\=48*, *label\_color\=ManimColor('\#FFFFFF')*, *label\_frame\=True*, *frame\_fill\_color\=None*, *frame\_fill\_opacity\=1*, *\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/labeled.html#LabeledLine)[¶](#manim.mobject.geometry.labeled.LabeledLine "Link to this definition")
Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


Constructs a line containing a label box somewhere along its length.


Parameters:
* **label** (*str* *\|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *\|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *\|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed on the line.
* **label\_position** (*float* *\|* *optional*) – A ratio in the range \[0\-1] to indicate the position of the label with respect to the length of the line. Default value is 0\.5\.
* **font\_size** (*float* *\|* *optional*) – Control font size for the label. This parameter is only used when label is of type str.
* **label\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *optional*) – The color of the label’s text. This parameter is only used when label is of type str.
* **label\_frame** (*Bool* *\|* *optional*) – Add a SurroundingRectangle frame to the label box.
* **frame\_fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *optional*) – Background color to fill the label box. If no value is provided, the background color of the canvas will be used.
* **frame\_fill\_opacity** (*float* *\|* *optional*) – Determine the opacity of the label box by passing a value in the range \[0\-1], where 0 indicates complete transparency and 1 means full opacity.
* **seealso::** (*..*) – [`LabeledArrow`](manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow "manim.mobject.geometry.labeled.LabeledArrow")


Examples


Example: LabeledLineExample [¶](#labeledlineexample)

![../_images/LabeledLineExample-1.png](../_images/LabeledLineExample-1.png)

```
from manim import *

class LabeledLineExample(Scene):
    def construct(self):
        line = LabeledLine(
            label          = '0.5',
            label_position = 0.8,
            font_size      = 20,
            label_color    = WHITE,
            label_frame    = True,

            start=LEFT+DOWN,
            end=RIGHT+UP)

        line.set_length(line.get_length() * 2)
        self.add(line)

```


```

class LabeledLineExample(Scene):
    def construct(self):
        line = LabeledLine(
            label          = '0.5',
            label_position = 0.8,
            font_size      = 20,
            label_color    = WHITE,
            label_frame    = True,

            start=LEFT+DOWN,
            end=RIGHT+UP)

        line.set_length(line.get_length() * 2)
        self.add(line)


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*label*, *label\_position\=0\.5*, *font\_size\=48*, *label\_color\=ManimColor('\#FFFFFF')*, *label\_frame\=True*, *frame\_fill\_color\=None*, *frame\_fill\_opacity\=1*, *\*args*, *\*\*kwargs*)[¶](#manim.mobject.geometry.labeled.LabeledLine._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **label** (*str* *\|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *\|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *\|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
* **label\_position** (*float*)
* **font\_size** (*float*)
* **label\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
* **label\_frame** (*bool*)
* **frame\_fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
* **frame\_fill\_opacity** (*float*)


Return type:
None



---

# Arrow


# Arrow[¶](#arrow "Link to this heading")


Qualified name: `manim.mobject.geometry.line.Arrow`


*class* Arrow(*\*args*, *stroke\_width\=6*, *buff\=0\.25*, *max\_tip\_length\_to\_length\_ratio\=0\.25*, *max\_stroke\_width\_to\_length\_ratio\=5*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow)[¶](#manim.mobject.geometry.line.Arrow "Link to this definition")
Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


An arrow.


Parameters:
* **args** – Arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").
* **stroke\_width** (*float*) – The thickness of the arrow. Influenced by `max_stroke_width_to_length_ratio`.
* **buff** (*float*) – The distance of the arrow from its start and end points.
* **max\_tip\_length\_to\_length\_ratio** (*float*) – `tip_length` scales with the length of the arrow. Increasing this ratio raises the max value of `tip_length`.
* **max\_stroke\_width\_to\_length\_ratio** (*float*) – `stroke_width` scales with the length of the arrow. Increasing this ratio ratios the max value of `stroke_width`.
* **kwargs** – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").


See also


`ArrowTip`
`CurvedArrow`


Examples


Example: ArrowExample [¶](#arrowexample)

![../_images/ArrowExample-1.png](../_images/ArrowExample-1.png)

```
from manim import *

from manim.mobject.geometry.tips import ArrowSquareTip
class ArrowExample(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)

        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        self.add(Group(g1, g2, g3).arrange(buff=2))

```


```

from manim.mobject.geometry.tips import ArrowSquareTip
class ArrowExample(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)

        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        self.add(Group(g1, g2, g3).arrange(buff=2))


```

Example: ArrowExample [¶](#arrowexample)

![../_images/ArrowExample-2.png](../_images/ArrowExample-2.png)

```
from manim import *

class ArrowExample(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)

```


```

class ArrowExample(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)


```
Methods


| [`get_default_tip_length`](#manim.mobject.geometry.line.Arrow.get_default_tip_length "manim.mobject.geometry.line.Arrow.get_default_tip_length") | Returns the default tip\_length of the arrow. |
| --- | --- |
| [`get_normal_vector`](#manim.mobject.geometry.line.Arrow.get_normal_vector "manim.mobject.geometry.line.Arrow.get_normal_vector") | Returns the normal of a vector. |
| [`reset_normal_vector`](#manim.mobject.geometry.line.Arrow.reset_normal_vector "manim.mobject.geometry.line.Arrow.reset_normal_vector") | Resets the normal of a vector |
| [`scale`](#manim.mobject.geometry.line.Arrow.scale "manim.mobject.geometry.line.Arrow.scale") | Scale an arrow, but keep stroke width and arrow tip size fixed. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*args*, *stroke\_width\=6*, *buff\=0\.25*, *max\_tip\_length\_to\_length\_ratio\=0\.25*, *max\_stroke\_width\_to\_length\_ratio\=5*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.Arrow._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **stroke\_width** (*float*)
* **buff** (*float*)
* **max\_tip\_length\_to\_length\_ratio** (*float*)
* **max\_stroke\_width\_to\_length\_ratio** (*float*)


Return type:
None


\_set\_stroke\_width\_from\_length()[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow._set_stroke_width_from_length)[¶](#manim.mobject.geometry.line.Arrow._set_stroke_width_from_length "Link to this definition")
Sets stroke width based on length.


Return type:
Self


get\_default\_tip\_length()[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow.get_default_tip_length)[¶](#manim.mobject.geometry.line.Arrow.get_default_tip_length "Link to this definition")
Returns the default tip\_length of the arrow.


Examples


```
>>> Arrow().get_default_tip_length()
0.35

```


Return type:
float


get\_normal\_vector()[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow.get_normal_vector)[¶](#manim.mobject.geometry.line.Arrow.get_normal_vector "Link to this definition")
Returns the normal of a vector.


Examples


```
>>> np.round(Arrow().get_normal_vector()) + 0. # add 0. to avoid negative 0 in output
array([ 0.,  0., -1.])

```


Return type:
[*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")


reset\_normal\_vector()[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow.reset_normal_vector)[¶](#manim.mobject.geometry.line.Arrow.reset_normal_vector "Link to this definition")
Resets the normal of a vector


Return type:
Self


scale(*factor*, *scale\_tips\=False*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/line.html#Arrow.scale)[¶](#manim.mobject.geometry.line.Arrow.scale "Link to this definition")
Scale an arrow, but keep stroke width and arrow tip size fixed.


See also


[`scale()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale")


Examples


```
>>> arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> scaled_arrow = arrow.scale(2)
>>> np.round(scaled_arrow.get_start_and_end(), 8) + 0
array([[-2., -2.,  0.],
       [ 2.,  2.,  0.]])
>>> arrow.tip.length == scaled_arrow.tip.length
True

```


Manually scaling the object using the default method
[`scale()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale") does not have the same properties:


```
>>> new_arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> another_scaled_arrow = VMobject.scale(new_arrow, 2)
>>> another_scaled_arrow.tip.length == arrow.tip.length
False

```


Parameters:
* **factor** (*float*)
* **scale\_tips** (*bool*)


Return type:
Self



---

# DoubleArrow


# DoubleArrow[¶](#doublearrow "Link to this heading")


Qualified name: `manim.mobject.geometry.line.DoubleArrow`


*class* DoubleArrow(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/line.html#DoubleArrow)[¶](#manim.mobject.geometry.line.DoubleArrow "Link to this definition")
Bases: [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")


An arrow with tips on both ends.


Parameters:
* **args** – Arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")
* **kwargs** – Additional arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")


See also


`ArrowTip`
`CurvedDoubleArrow`


Examples


Example: DoubleArrowExample [¶](#doublearrowexample)

![../_images/DoubleArrowExample-1.png](../_images/DoubleArrowExample-1.png)

```
from manim import *

from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)

```


```

from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)


```

Example: DoubleArrowExample2 [¶](#doublearrowexample2)

![../_images/DoubleArrowExample2-1.png](../_images/DoubleArrowExample2-1.png)

```
from manim import *

class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)

```


```

class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*args*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.DoubleArrow._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Return type:
None



---

# TangentLine


# TangentLine[¶](#tangentline "Link to this heading")


Qualified name: `manim.mobject.geometry.line.TangentLine`


*class* TangentLine(*vmob*, *alpha*, *length\=1*, *d\_alpha\=1e\-06*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/geometry/line.html#TangentLine)[¶](#manim.mobject.geometry.line.TangentLine "Link to this definition")
Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


Constructs a line tangent to a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") at a specific point.


Parameters:
* **vmob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject on which the tangent line is drawn.
* **alpha** (*float*) – How far along the shape that the line will be constructed. range: 0\-1\.
* **length** (*float*) – Length of the tangent line.
* **d\_alpha** (*float*) – The `dx` value
* **kwargs** – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


See also


[`point_from_proportion()`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion "manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion")


Examples


Example: TangentLineExample [¶](#tangentlineexample)

![../_images/TangentLineExample-1.png](../_images/TangentLineExample-1.png)

```
from manim import *

class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
        line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
        self.add(circle, line_1, line_2)

```


```

class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
        line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
        self.add(circle, line_1, line_2)


```
Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*vmob*, *alpha*, *length\=1*, *d\_alpha\=1e\-06*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.TangentLine._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **vmob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
* **alpha** (*float*)
* **length** (*float*)
* **d\_alpha** (*float*)


Return type:
None



---

# polygram


# polygram[¶](#module-manim.mobject.geometry.polygram "Link to this heading")


Mobjects that are simple geometric shapes.


Classes


| [`Cutout`](manim.mobject.geometry.polygram.Cutout.html#manim.mobject.geometry.polygram.Cutout "manim.mobject.geometry.polygram.Cutout") | A shape with smaller cutouts. |
| --- | --- |
| [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") | A shape consisting of one closed loop of vertices. |
| [`Polygram`](manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") | A generalized [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon"), allowing for disconnected sets of edges. |
| [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") | A quadrilateral with two sets of parallel sides. |
| [`RegularPolygon`](manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon") | An n\-sided regular [`Polygon`](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon"). |
| [`RegularPolygram`](manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram") | A [`Polygram`](manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") with regularly spaced vertices. |
| [`RoundedRectangle`](manim.mobject.geometry.polygram.RoundedRectangle.html#manim.mobject.geometry.polygram.RoundedRectangle "manim.mobject.geometry.polygram.RoundedRectangle") | A rectangle with rounded corners. |
| [`Square`](manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square") | A rectangle with equal side lengths. |
| [`Star`](manim.mobject.geometry.polygram.Star.html#manim.mobject.geometry.polygram.Star "manim.mobject.geometry.polygram.Star") | A regular polygram without the intersecting lines. |
| [`Triangle`](manim.mobject.geometry.polygram.Triangle.html#manim.mobject.geometry.polygram.Triangle "manim.mobject.geometry.polygram.Triangle") | An equilateral triangle. |



---

# DiGraph


# DiGraph[¶](#digraph "Link to this heading")


Qualified name: `manim.mobject.graph.DiGraph`


*class* DiGraph(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[\[source]](../_modules/manim/mobject/graph.html#DiGraph)[¶](#manim.mobject.graph.DiGraph "Link to this definition")
Bases: [`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")


A directed graph.


Note


In contrast to undirected graphs, the order in which vertices in a given
edge are specified is relevant here.


See also


[`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")


Parameters:
* **vertices** (*list**\[**Hashable**]*) – A list of vertices. Must be hashable elements.
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
and `v` are vertices. The edge is directed from `u` to `v`.
* **labels** (*bool* *\|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
the vertices are not labeled; if `True` they are labeled using their
names (as specified in `vertices`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
custom labels can be specified by passing a dictionary whose keys are
the vertices, and whose values are the corresponding vertex labels
(rendered via, e.g., [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")).
* **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.
* **layout** (*LayoutName* *\|* *dict**\[**Hashable**,* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]* *\|* [*LayoutFunction*](manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
`"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
for automatic vertex positioning using `networkx`
(see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
for more details), or a dictionary specifying a coordinate (value)
for each vertex (key) for manual positioning.
* **layout\_config** (*dict* *\|* *None*) – Only for automatically generated layouts. A dictionary whose entries
are passed as keyword arguments to the automatic layout algorithm
specified via `layout` of `networkx`.
The `tree` layout also accepts a special parameter `vertex_spacing`
passed as a keyword argument inside the `layout_config` dictionary.
Passing a tuple `(space_x, space_y)` as this argument overrides
the value of `layout_scale` and ensures that vertices are arranged
in a way such that the centers of siblings in the same layer are
at least `space_x` units apart horizontally, and neighboring layers
are spaced `space_y` units vertically.
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*) – The scale of automatically generated layouts: the vertices will
be arranged such that the coordinates are located within the
interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
and the second in `[-scale_y, scale_y]`. Default: 2\.
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
* **vertex\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`, or a dictionary whose keys
are the vertices, and whose values are dictionaries containing keyword
arguments for the mobject related to the corresponding vertex.
* **vertex\_mobjects** (*dict* *\|* *None*) – A dictionary whose keys are the vertices, and whose values are
mobjects to be used as vertices. Passing vertices here overrides
all other configuration options for a vertex.
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
* **edge\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary whose
keys are the edges, and whose values are dictionaries containing
keyword arguments for the mobject related to the corresponding edge.
You can further customize the tip by adding a `tip_config` dictionary
for global styling, or by adding the dict to a specific `edge_config`.
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)


Examples


Example: MovingDiGraph [¶](#movingdigraph)


```
from manim import *

class MovingDiGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

        g = DiGraph(vertices, edges)

        self.add(g)
        self.play(
            g[1].animate.move_to([1, 1, 1]),
            g[2].animate.move_to([-1, 1, 2]),
            g[3].animate.move_to([1, -1, -1]),
            g[4].animate.move_to([-1, -1, 0]),
        )
        self.wait()

```


```

class MovingDiGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

        g = DiGraph(vertices, edges)

        self.add(g)
        self.play(
            g[1].animate.move_to([1, 1, 1]),
            g[2].animate.move_to([-1, 1, 2]),
            g[3].animate.move_to([1, -1, -1]),
            g[4].animate.move_to([-1, -1, 0]),
        )
        self.wait()


```
You can customize the edges and arrow tips globally or locally.


Example: CustomDiGraph [¶](#customdigraph)


```
from manim import *

class CustomDiGraph(Scene):
    def construct(self):
        vertices = [i for i in range(5)]
        edges = [
            (0, 1),
            (1, 2),
            (3, 2),
            (3, 4),
        ]

        edge_config = {
            "stroke_width": 2,
            "tip_config": {
                "tip_shape": ArrowSquareTip,
                "tip_length": 0.15,
            },
            (3, 4): {
                "color": RED,
                "tip_config": {"tip_length": 0.25, "tip_width": 0.25}
            },
        }

        g = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            edge_config=edge_config,
        ).scale(1.4)

        self.play(Create(g))
        self.wait()

```


```

class CustomDiGraph(Scene):
    def construct(self):
        vertices = [i for i in range(5)]
        edges = [
            (0, 1),
            (1, 2),
            (3, 2),
            (3, 4),
        ]

        edge_config = {
            "stroke_width": 2,
            "tip_config": {
                "tip_shape": ArrowSquareTip,
                "tip_length": 0.15,
            },
            (3, 4): {
                "color": RED,
                "tip_config": {"tip_length": 0.25, "tip_width": 0.25}
            },
        }

        g = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            edge_config=edge_config,
        ).scale(1.4)

        self.play(Create(g))
        self.wait()


```
Since this implementation respects the labels boundary you can also use
it for an undirected moving graph with labels.


Example: UndirectedMovingDiGraph [¶](#undirectedmovingdigraph)


```
from manim import *

class UndirectedMovingDiGraph(Scene):
    def construct(self):
        vertices = [i for i in range(5)]
        edges = [
            (0, 1),
            (1, 2),
            (3, 2),
            (3, 4),
        ]

        edge_config = {
            "stroke_width": 2,
            "tip_config": {"tip_length": 0, "tip_width": 0},
            (3, 4): {"color": RED},
        }

        g = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            edge_config=edge_config,
        ).scale(1.4)

        self.play(Create(g))
        self.wait()

        self.play(
            g[1].animate.move_to([1, 1, 1]),
            g[2].animate.move_to([-1, 1, 2]),
            g[3].animate.move_to([-1.5, -1.5, -1]),
            g[4].animate.move_to([1, -2, -1]),
        )
        self.wait()

```


```

class UndirectedMovingDiGraph(Scene):
    def construct(self):
        vertices = [i for i in range(5)]
        edges = [
            (0, 1),
            (1, 2),
            (3, 2),
            (3, 4),
        ]

        edge_config = {
            "stroke_width": 2,
            "tip_config": {"tip_length": 0, "tip_width": 0},
            (3, 4): {"color": RED},
        }

        g = DiGraph(
            vertices,
            edges,
            labels=True,
            layout="circular",
            edge_config=edge_config,
        ).scale(1.4)

        self.play(Create(g))
        self.wait()

        self.play(
            g[1].animate.move_to([1, 1, 1]),
            g[2].animate.move_to([-1, 1, 2]),
            g[3].animate.move_to([-1.5, -1.5, -1]),
            g[4].animate.move_to([1, -2, -1]),
        )
        self.wait()


```
Methods


| [`update_edges`](#manim.mobject.graph.DiGraph.update_edges "manim.mobject.graph.DiGraph.update_edges") | Updates the edges to stick at their corresponding vertices. |
| --- | --- |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


*static* \_empty\_networkx\_graph()[\[source]](../_modules/manim/mobject/graph.html#DiGraph._empty_networkx_graph)[¶](#manim.mobject.graph.DiGraph._empty_networkx_graph "Link to this definition")
Return an empty networkx graph for the given graph type.


Return type:
*DiGraph*


\_original\_\_init\_\_(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[¶](#manim.mobject.graph.DiGraph._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **vertices** (*list**\[**Hashable**]*)
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **labels** (*bool* *\|* *dict*)
* **label\_fill\_color** (*str*)
* **layout** (*Literal**\[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *\|* *dict**\[**\~typing.Hashable**,* *\~manim.typing.Point3D**]* *\|* *\~manim.mobject.graph.LayoutFunction*)
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*)
* **layout\_config** (*dict* *\|* *None*)
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **vertex\_config** (*dict* *\|* *None*)
* **vertex\_mobjects** (*dict* *\|* *None*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)
* **edge\_config** (*dict* *\|* *None*)


Return type:
None


\_populate\_edge\_dict(*edges*, *edge\_type*)[\[source]](../_modules/manim/mobject/graph.html#DiGraph._populate_edge_dict)[¶](#manim.mobject.graph.DiGraph._populate_edge_dict "Link to this definition")
Helper method for populating the edges of the graph.


Parameters:
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)


update\_edges(*graph*)[\[source]](../_modules/manim/mobject/graph.html#DiGraph.update_edges)[¶](#manim.mobject.graph.DiGraph.update_edges "Link to this definition")
Updates the edges to stick at their corresponding vertices.


Arrow tips need to be repositioned since otherwise they can be
deformed.



---

# GenericGraph


# GenericGraph[¶](#genericgraph "Link to this heading")


Qualified name: `manim.mobject.graph.GenericGraph`


*class* GenericGraph(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph)[¶](#manim.mobject.graph.GenericGraph "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


Abstract base class for graphs (that is, a collection of vertices
connected with edges).


Graphs can be instantiated by passing both a list of (distinct, hashable)
vertex names, together with list of edges (as tuples of vertex names). See
the examples for concrete implementations of this class for details.


Note


This implementation uses updaters to make the edges move with
the vertices.


See also


[`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"), [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph")


Parameters:
* **vertices** (*list**\[**Hashable**]*) – A list of vertices. Must be hashable elements.
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
and `v` are vertices.
* **labels** (*bool* *\|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
the vertices are not labeled; if `True` they are labeled using their
names (as specified in `vertices`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
custom labels can be specified by passing a dictionary whose keys are
the vertices, and whose values are the corresponding vertex labels
(rendered via, e.g., [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")).
* **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.
* **layout** (*LayoutName* *\|* *dict**\[**Hashable**,* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]* *\|* [*LayoutFunction*](manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
`"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
for automatic vertex positioning primarily using `networkx`
(see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
for more details), a dictionary specifying a coordinate (value)
for each vertex (key) for manual positioning, or a .:class:\~.LayoutFunction with a user\-defined automatic layout.
* **layout\_config** (*dict* *\|* *None*) – Only for automatic layouts. A dictionary whose entries
are passed as keyword arguments to the named layout or automatic layout function
specified via `layout`.
The `tree` layout also accepts a special parameter `vertex_spacing`
passed as a keyword argument inside the `layout_config` dictionary.
Passing a tuple `(space_x, space_y)` as this argument overrides
the value of `layout_scale` and ensures that vertices are arranged
in a way such that the centers of siblings in the same layer are
at least `space_x` units apart horizontally, and neighboring layers
are spaced `space_y` units vertically.
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*) – The scale of automatically generated layouts: the vertices will
be arranged such that the coordinates are located within the
interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
and the second in `[-scale_y, scale_y]`. Default: 2\.
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
* **vertex\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`, or a dictionary whose keys
are the vertices, and whose values are dictionaries containing keyword
arguments for the mobject related to the corresponding vertex.
* **vertex\_mobjects** (*dict* *\|* *None*) – A dictionary whose keys are the vertices, and whose values are
mobjects to be used as vertices. Passing vertices here overrides
all other configuration options for a vertex.
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
* **edge\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary whose
keys are the edges, and whose values are dictionaries containing
keyword arguments for the mobject related to the corresponding edge.
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)


Methods


| [`add_edges`](#manim.mobject.graph.GenericGraph.add_edges "manim.mobject.graph.GenericGraph.add_edges") | Add new edges to the graph. |
| --- | --- |
| [`add_vertices`](#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices") | Add a list of vertices to the graph. |
| [`change_layout`](#manim.mobject.graph.GenericGraph.change_layout "manim.mobject.graph.GenericGraph.change_layout") | Change the layout of this graph. |
| [`from_networkx`](#manim.mobject.graph.GenericGraph.from_networkx "manim.mobject.graph.GenericGraph.from_networkx") | Build a [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a given `networkx` graph. |
| [`remove_edges`](#manim.mobject.graph.GenericGraph.remove_edges "manim.mobject.graph.GenericGraph.remove_edges") | Remove several edges from the graph. |
| [`remove_vertices`](#manim.mobject.graph.GenericGraph.remove_vertices "manim.mobject.graph.GenericGraph.remove_vertices") | Remove several vertices from the graph. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_add\_edge(*edge*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *edge\_config\=None*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._add_edge)[¶](#manim.mobject.graph.GenericGraph._add_edge "Link to this definition")
Add a new edge to the graph.


Parameters:
* **edge** (*tuple**\[**Hashable**,* *Hashable**]*) – The edge (as a tuple of vertex identifiers) to be added. If a non\-existing
vertex is passed, a new vertex with default settings will be created. Create
new vertices yourself beforehand to customize them.
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
* **edge\_config** (*dict* *\|* *None*) – A dictionary containing keyword arguments to be passed
to the class specified via `edge_type`.


Returns:
A group containing all newly added vertices and edges.


Return type:
[Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")


\_add\_vertex(*vertex*, *position\=None*, *label\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobject\=None*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._add_vertex)[¶](#manim.mobject.graph.GenericGraph._add_vertex "Link to this definition")
Add a vertex to the graph.


Parameters:
* **vertex** (*Hashable*) – A hashable vertex identifier.
* **position** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") *\|* *None*) – The coordinates where the new vertex should be added. If `None`, the center
of the graph is used.
* **label** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
the vertex is not labeled; if `True` it is labeled using its
names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
any [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.
* **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `label`.
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
* **vertex\_config** (*dict* *\|* *None*) – A dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`.
* **vertex\_mobject** (*dict* *\|* *None*) – The mobject to be used as the vertex. Overrides all other
vertex customization options.


Return type:
[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


*static* \_empty\_networkx\_graph()[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._empty_networkx_graph)[¶](#manim.mobject.graph.GenericGraph._empty_networkx_graph "Link to this definition")
Return an empty networkx graph for the given graph type.


Return type:
*Graph*


\_original\_\_init\_\_(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[¶](#manim.mobject.graph.GenericGraph._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **vertices** (*list**\[**Hashable**]*)
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **labels** (*bool* *\|* *dict*)
* **label\_fill\_color** (*str*)
* **layout** (*Literal**\[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *\|* *dict**\[**\~typing.Hashable**,* *\~manim.typing.Point3D**]* *\|* *\~manim.mobject.graph.LayoutFunction*)
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*)
* **layout\_config** (*dict* *\|* *None*)
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **vertex\_config** (*dict* *\|* *None*)
* **vertex\_mobjects** (*dict* *\|* *None*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)
* **edge\_config** (*dict* *\|* *None*)


Return type:
None


\_populate\_edge\_dict(*edges*, *edge\_type*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._populate_edge_dict)[¶](#manim.mobject.graph.GenericGraph._populate_edge_dict "Link to this definition")
Helper method for populating the edges of the graph.


Parameters:
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)


\_remove\_edge(*edge*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._remove_edge)[¶](#manim.mobject.graph.GenericGraph._remove_edge "Link to this definition")
Remove an edge from the graph.


Parameters:
**edge** (*tuple**\[**Hashable**]*) – The edge (i.e., a tuple of vertex identifiers) to be removed from the graph.


Returns:
The removed edge.


Return type:
[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


\_remove\_vertex(*vertex*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph._remove_vertex)[¶](#manim.mobject.graph.GenericGraph._remove_vertex "Link to this definition")
Remove a vertex (as well as all incident edges) from the graph.


Parameters:
**vertex** – The identifier of a vertex to be removed.


Returns:
A mobject containing all removed objects.


Return type:
[Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")


add\_edges(*\*edges*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *edge\_config\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.add_edges)[¶](#manim.mobject.graph.GenericGraph.add_edges "Link to this definition")
Add new edges to the graph.


Parameters:
* **edges** (*tuple**\[**Hashable**,* *Hashable**]*) – Edges (as tuples of vertex identifiers) to be added. If a non\-existing
vertex is passed, a new vertex with default settings will be created. Create
new vertices yourself beforehand to customize them.
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
* **edge\_config** (*dict* *\|* *None*) – A dictionary either containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary
whose keys are the edge tuples, and whose values are dictionaries
containing keyword arguments to be passed for the construction
of the corresponding edge.
* **kwargs** – Any further keyword arguments are passed to [`add_vertices()`](#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices")
which is used to create new vertices in the passed edges.


Returns:
A group containing all newly added vertices and edges.


Return type:
[Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")


add\_vertices(*\*vertices*, *positions\=None*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.add_vertices)[¶](#manim.mobject.graph.GenericGraph.add_vertices "Link to this definition")
Add a list of vertices to the graph.


Parameters:
* **vertices** (*Hashable*) – Hashable vertex identifiers.
* **positions** (*dict* *\|* *None*) – A dictionary specifying the coordinates where the new vertices should be added.
If `None`, all vertices are created at the center of the graph.
* **labels** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
the vertex is not labeled; if `True` it is labeled using its
names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
any [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.
* **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
* **vertex\_config** (*dict* *\|* *None*) – A dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`.
* **vertex\_mobjects** (*dict* *\|* *None*) – A dictionary whose keys are the vertex identifiers, and whose
values are mobjects that should be used as vertices. Overrides
all other vertex customization options.
* **self** ([*Graph*](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"))


change\_layout(*layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *partitions\=None*, *root\_vertex\=None*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.change_layout)[¶](#manim.mobject.graph.GenericGraph.change_layout "Link to this definition")
Change the layout of this graph.


See the documentation of [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") for details about the
keyword arguments.


Examples


Example: ChangeGraphLayout [¶](#changegraphlayout)


```
from manim import *

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()

```


```

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()


```

Parameters:
* **layout** (*Literal**\[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *\|* *dict**\[**\~typing.Hashable**,* *\~manim.typing.Point3D**]* *\|* *\~manim.mobject.graph.LayoutFunction*)
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*)
* **layout\_config** (*dict**\[**str**,* *Any**]* *\|* *None*)
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)


Return type:
[*Graph*](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")


*classmethod* from\_networkx(*nxgraph*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.from_networkx)[¶](#manim.mobject.graph.GenericGraph.from_networkx "Link to this definition")
Build a [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a
given `networkx` graph.


Parameters:
* **nxgraph** (*Graph* *\|* *DiGraph*) – A `networkx` graph or digraph.
* **\*\*kwargs** – Keywords to be passed to the constructor of [`Graph`](manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph").


Examples


Example: ImportNetworkxGraph [¶](#importnetworkxgraph)


```
from manim import *

import networkx as nx

nxgraph = nx.erdos_renyi_graph(14, 0.5)

class ImportNetworkxGraph(Scene):
    def construct(self):
        G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
        self.play(Create(G))
        self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                         3*UP*np.sin(ind/7 * PI))
                    for ind, v in enumerate(G.vertices)])
        self.play(Uncreate(G))

```


```

import networkx as nx

nxgraph = nx.erdos_renyi_graph(14, 0.5)

class ImportNetworkxGraph(Scene):
    def construct(self):
        G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
        self.play(Create(G))
        self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                         3*UP*np.sin(ind/7 * PI))
                    for ind, v in enumerate(G.vertices)])
        self.play(Uncreate(G))


```


remove\_edges(*\*edges*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.remove_edges)[¶](#manim.mobject.graph.GenericGraph.remove_edges "Link to this definition")
Remove several edges from the graph.


Parameters:
**edges** (*tuple**\[**Hashable**]*) – Edges to be removed from the graph.


Returns:
A group containing all removed edges.


Return type:
[Group](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")


remove\_vertices(*\*vertices*)[\[source]](../_modules/manim/mobject/graph.html#GenericGraph.remove_vertices)[¶](#manim.mobject.graph.GenericGraph.remove_vertices "Link to this definition")
Remove several vertices from the graph.


Parameters:
**vertices** – Vertices to be removed from the graph.


Examples


```
>>> G = Graph([1, 2, 3], [(1, 2), (2, 3)])
>>> removed = G.remove_vertices(2, 3); removed
VGroup(Line, Line, Dot, Dot)
>>> G
Undirected graph on 1 vertices and 0 edges

```



---

# Graph


# Graph[¶](#graph "Link to this heading")


Qualified name: `manim.mobject.graph.Graph`


*class* Graph(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[\[source]](../_modules/manim/mobject/graph.html#Graph)[¶](#manim.mobject.graph.Graph "Link to this definition")
Bases: [`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")


An undirected graph (vertices connected with edges).


The graph comes with an updater which makes the edges stick to
the vertices when moved around. See [`DiGraph`](manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") for
a version with directed edges.


See also


[`GenericGraph`](manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")


Parameters:
* **vertices** (*list**\[**Hashable**]*) – A list of vertices. Must be hashable elements.
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
and `v` are vertices. The vertex order is irrelevant.
* **labels** (*bool* *\|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
the vertices are not labeled; if `True` they are labeled using their
names (as specified in `vertices`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
custom labels can be specified by passing a dictionary whose keys are
the vertices, and whose values are the corresponding vertex labels
(rendered via, e.g., [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")).
* **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.
* **layout** (*LayoutName* *\|* *dict**\[**Hashable**,* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]* *\|* [*LayoutFunction*](manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
`"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
for automatic vertex positioning using `networkx`
(see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
for more details), or a dictionary specifying a coordinate (value)
for each vertex (key) for manual positioning.
* **layout\_config** (*dict* *\|* *None*) – Only for automatically generated layouts. A dictionary whose entries
are passed as keyword arguments to the automatic layout algorithm
specified via `layout` of `networkx`.
The `tree` layout also accepts a special parameter `vertex_spacing`
passed as a keyword argument inside the `layout_config` dictionary.
Passing a tuple `(space_x, space_y)` as this argument overrides
the value of `layout_scale` and ensures that vertices are arranged
in a way such that the centers of siblings in the same layer are
at least `space_x` units apart horizontally, and neighboring layers
are spaced `space_y` units vertically.
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*) – The scale of automatically generated layouts: the vertices will
be arranged such that the coordinates are located within the
interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
and the second in `[-scale_y, scale_y]`. Default: 2\.
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying vertices in the scene.
* **vertex\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`, or a dictionary whose keys
are the vertices, and whose values are dictionaries containing keyword
arguments for the mobject related to the corresponding vertex.
* **vertex\_mobjects** (*dict* *\|* *None*) – A dictionary whose keys are the vertices, and whose values are
mobjects to be used as vertices. Passing vertices here overrides
all other configuration options for a vertex.
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – The mobject class used for displaying edges in the scene.
* **edge\_config** (*dict* *\|* *None*) – Either a dictionary containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary whose
keys are the edges, and whose values are dictionaries containing
keyword arguments for the mobject related to the corresponding edge.
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)


Examples


First, we create a small graph and demonstrate that the edges move
together with the vertices.


Example: MovingVertices [¶](#movingvertices)


```
from manim import *

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()

```


```

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()


```
There are several automatic positioning algorithms to choose from:


Example: GraphAutoPosition [¶](#graphautoposition)

![../_images/GraphAutoPosition-1.png](../_images/GraphAutoPosition-1.png)

```
from manim import *

class GraphAutoPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))

```


```

class GraphAutoPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))


```
Vertices can also be positioned manually:


Example: GraphManualPosition [¶](#graphmanualposition)

![../_images/GraphManualPosition-1.png](../_images/GraphManualPosition-1.png)

```
from manim import *

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)

```


```

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)


```
The vertices in graphs can be labeled, and configurations for vertices
and edges can be modified both by default and for specific vertices and
edges.


Note


In `edge_config`, edges can be passed in both directions: if
`(u, v)` is an edge in the graph, both `(u, v)` as well
as `(v, u)` can be used as keys in the dictionary.


Example: LabeledModifiedGraph [¶](#labeledmodifiedgraph)

![../_images/LabeledModifiedGraph-1.png](../_images/LabeledModifiedGraph-1.png)

```
from manim import *

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)

```


```

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)


```
You can also lay out a partite graph on columns by specifying
a list of the vertices on each side and choosing the partite layout.


Note


All vertices in your graph which are not listed in any of the partitions
are collected in their own partition and rendered in the rightmost column.


Example: PartiteGraph [¶](#partitegraph)

![../_images/PartiteGraph-1.png](../_images/PartiteGraph-1.png)

```
from manim import *

import networkx as nx

class PartiteGraph(Scene):
    def construct(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        G.add_edges_from([(0, 2), (0,3), (1, 2)])
        graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
        self.play(Create(graph))

```


```

import networkx as nx

class PartiteGraph(Scene):
    def construct(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        G.add_edges_from([(0, 2), (0,3), (1, 2)])
        graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
        self.play(Create(graph))


```
The representation of a linear artificial neural network is facilitated
by the use of the partite layout and defining partitions for each layer.


Example: LinearNN [¶](#linearnn)

![../_images/LinearNN-1.png](../_images/LinearNN-1.png)

```
from manim import *

class LinearNN(Scene):
    def construct(self):
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # the number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3,
            vertex_config={'radius': 0.20},
        )
        self.add(graph)

```


```

class LinearNN(Scene):
    def construct(self):
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # the number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3,
            vertex_config={'radius': 0.20},
        )
        self.add(graph)


```
The custom tree layout can be used to show the graph
by distance from the root vertex. You must pass the root vertex
of the tree.


Example: Tree [¶](#tree)


```
from manim import *

import networkx as nx

class Tree(Scene):
    def construct(self):
        G = nx.Graph()

        G.add_node("ROOT")

        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)

            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

        self.play(Create(
            Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))

```


```

import networkx as nx

class Tree(Scene):
    def construct(self):
        G = nx.Graph()

        G.add_node("ROOT")

        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)

            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

        self.play(Create(
            Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))


```
The following code sample illustrates the use of the `vertex_spacing`
layout parameter specific to the `"tree"` layout. As mentioned
above, setting `vertex_spacing` overrides the specified value
for `layout_scale`, and as such it is harder to control the size
of the mobject. However, we can adjust the captured frame and
zoom out by using a [`MovingCameraScene`](manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene"):


```
class LargeTreeGeneration(MovingCameraScene):
    DEPTH = 4
    CHILDREN_PER_VERTEX = 3
    LAYOUT_CONFIG = {"vertex_spacing": (0.5, 1)}
    VERTEX_CONF = {"radius": 0.25, "color": BLUE_B, "fill_opacity": 1}

    def expand_vertex(self, g, vertex_id: str, depth: int):
        new_vertices = [f"{vertex_id}/{i}" for i in range(self.CHILDREN_PER_VERTEX)]
        new_edges = [(vertex_id, child_id) for child_id in new_vertices]
        g.add_edges(
            *new_edges,
            vertex_config=self.VERTEX_CONF,
            positions={
                k: g.vertices[vertex_id].get_center() + 0.1 * DOWN for k in new_vertices
            },
        )
        if depth < self.DEPTH:
            for child_id in new_vertices:
                self.expand_vertex(g, child_id, depth + 1)

        return g

    def construct(self):
        g = Graph(["ROOT"], [], vertex_config=self.VERTEX_CONF)
        g = self.expand_vertex(g, "ROOT", 1)
        self.add(g)

        self.play(
            g.animate.change_layout(
                "tree",
                root_vertex="ROOT",
                layout_config=self.LAYOUT_CONFIG,
            )
        )
        self.play(self.camera.auto_zoom(g, margin=1), run_time=0.5)

```


Methods


| `update_edges` |  |
| --- | --- |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


*static* \_empty\_networkx\_graph()[\[source]](../_modules/manim/mobject/graph.html#Graph._empty_networkx_graph)[¶](#manim.mobject.graph.Graph._empty_networkx_graph "Link to this definition")
Return an empty networkx graph for the given graph type.


Return type:
*Graph*


\_original\_\_init\_\_(*vertices*, *edges*, *labels\=False*, *label\_fill\_color\=ManimColor('\#000000')*, *layout\='spring'*, *layout\_scale\=2*, *layout\_config\=None*, *vertex\_type\=\<class 'manim.mobject.geometry.arc.Dot'\>*, *vertex\_config\=None*, *vertex\_mobjects\=None*, *edge\_type\=\<class 'manim.mobject.geometry.line.Line'\>*, *partitions\=None*, *root\_vertex\=None*, *edge\_config\=None*)[¶](#manim.mobject.graph.Graph._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **vertices** (*list**\[**Hashable**]*)
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **labels** (*bool* *\|* *dict*)
* **label\_fill\_color** (*str*)
* **layout** (*Literal**\[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *\|* *dict**\[**\~typing.Hashable**,* *\~manim.typing.Point3D**]* *\|* *\~manim.mobject.graph.LayoutFunction*)
* **layout\_scale** (*float* *\|* *tuple**\[**float**,* *float**,* *float**]*)
* **layout\_config** (*dict* *\|* *None*)
* **vertex\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **vertex\_config** (*dict* *\|* *None*)
* **vertex\_mobjects** (*dict* *\|* *None*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
* **partitions** (*list**\[**list**\[**Hashable**]**]* *\|* *None*)
* **root\_vertex** (*Hashable* *\|* *None*)
* **edge\_config** (*dict* *\|* *None*)


Return type:
None


\_populate\_edge\_dict(*edges*, *edge\_type*)[\[source]](../_modules/manim/mobject/graph.html#Graph._populate_edge_dict)[¶](#manim.mobject.graph.Graph._populate_edge_dict "Link to this definition")
Helper method for populating the edges of the graph.


Parameters:
* **edges** (*list**\[**tuple**\[**Hashable**,* *Hashable**]**]*)
* **edge\_type** (*type**\[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)



---

# LayoutFunction


# LayoutFunction[¶](#layoutfunction "Link to this heading")


Qualified name: `manim.mobject.graph.LayoutFunction`


*class* LayoutFunction(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graph.html#LayoutFunction)[¶](#manim.mobject.graph.LayoutFunction "Link to this definition")
Bases: `Protocol`


A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`.


Note


The layout function must be a pure function, i.e., it must not modify the graph passed to it.


Examples


Here is an example that arranges nodes in an n x m grid in sorted order.


Example: CustomLayoutExample [¶](#customlayoutexample)

![../_images/CustomLayoutExample-1.png](../_images/CustomLayoutExample-1.png)

```
from manim import *

class CustomLayoutExample(Scene):
    def construct(self):
        import numpy as np
        import networkx as nx

        # create custom layout
        def custom_layout(
            graph: nx.Graph,
            scale: float | tuple[float, float, float] = 2,
            n: int | None = None,
            *args: Any,
            **kwargs: Any,
        ):
            nodes = sorted(list(graph))
            height = len(nodes) // n
            return {
                node: (scale * np.array([
                    (i % n) - (n-1)/2,
                    -(i // n) + height/2,
                    0
                ])) for i, node in enumerate(graph)
            }

        # draw graph
        n = 4
        graph = Graph(
            [i for i in range(4 * 2 - 1)],
            [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (4, 5), (5, 6)],
            labels=True,
            layout=custom_layout,
            layout_config={'n': n}
        )
        self.add(graph)

```


```

class CustomLayoutExample(Scene):
    def construct(self):
        import numpy as np
        import networkx as nx

        # create custom layout
        def custom_layout(
            graph: nx.Graph,
            scale: float | tuple[float, float, float] = 2,
            n: int | None = None,
            *args: Any,
            **kwargs: Any,
        ):
            nodes = sorted(list(graph))
            height = len(nodes) // n
            return {
                node: (scale * np.array([
                    (i % n) - (n-1)/2,
                    -(i // n) + height/2,
                    0
                ])) for i, node in enumerate(graph)
            }

        # draw graph
        n = 4
        graph = Graph(
            [i for i in range(4 * 2 - 1)],
            [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (4, 5), (5, 6)],
            labels=True,
            layout=custom_layout,
            layout_config={'n': n}
        )
        self.add(graph)


```
Several automatic layouts are provided by manim, and can be used by passing their name as the `layout` parameter to `change_layout()`.
Alternatively, a custom layout function can be passed to `change_layout()` as the `layout` parameter. Such a function must adhere to the [`LayoutFunction`](#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction") protocol.


The [`LayoutFunction`](#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction") s provided by manim are illustrated below:


* Circular Layout: places the vertices on a circle


Example: CircularLayout [¶](#circularlayout)

![../_images/CircularLayout-1.png](../_images/CircularLayout-1.png)

```
from manim import *

class CircularLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="circular",
            labels=True
        )
        self.add(graph)

```


```

class CircularLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="circular",
            labels=True
        )
        self.add(graph)


```
* Kamada Kawai Layout: tries to place the vertices such that the given distances between them are respected


Example: KamadaKawaiLayout [¶](#kamadakawailayout)

![../_images/KamadaKawaiLayout-1.png](../_images/KamadaKawaiLayout-1.png)

```
from manim import *

class KamadaKawaiLayout(Scene):
    def construct(self):
        from collections import defaultdict
        distances: dict[int, dict[int, float]] = defaultdict(dict)

        # set desired distances
        distances[1][2] = 1  # distance between vertices 1 and 2 is 1
        distances[2][3] = 1  # distance between vertices 2 and 3 is 1
        distances[3][4] = 2  # etc
        distances[4][5] = 3
        distances[5][6] = 5
        distances[6][1] = 8

        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
            layout="kamada_kawai",
            layout_config={"dist": distances},
            layout_scale=4,
            labels=True
        )
        self.add(graph)

```


```

class KamadaKawaiLayout(Scene):
    def construct(self):
        from collections import defaultdict
        distances: dict[int, dict[int, float]] = defaultdict(dict)

        # set desired distances
        distances[1][2] = 1  # distance between vertices 1 and 2 is 1
        distances[2][3] = 1  # distance between vertices 2 and 3 is 1
        distances[3][4] = 2  # etc
        distances[4][5] = 3
        distances[5][6] = 5
        distances[6][1] = 8

        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
            layout="kamada_kawai",
            layout_config={"dist": distances},
            layout_scale=4,
            labels=True
        )
        self.add(graph)


```
* Partite Layout: places vertices into distinct partitions


Example: PartiteLayout [¶](#partitelayout)

![../_images/PartiteLayout-1.png](../_images/PartiteLayout-1.png)

```
from manim import *

class PartiteLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="partite",
            layout_config={"partitions": [[1,2],[3,4],[5,6]]},
            labels=True
        )
        self.add(graph)

```


```

class PartiteLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="partite",
            layout_config={"partitions": [[1,2],[3,4],[5,6]]},
            labels=True
        )
        self.add(graph)


```
* Planar Layout: places vertices such that edges do not cross


Example: PlanarLayout [¶](#planarlayout)

![../_images/PlanarLayout-1.png](../_images/PlanarLayout-1.png)

```
from manim import *

class PlanarLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="planar",
            layout_scale=4,
            labels=True
        )
        self.add(graph)

```


```

class PlanarLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="planar",
            layout_scale=4,
            labels=True
        )
        self.add(graph)


```
* Random Layout: randomly places vertices


Example: RandomLayout [¶](#randomlayout)

![../_images/RandomLayout-1.png](../_images/RandomLayout-1.png)

```
from manim import *

class RandomLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="random",
            labels=True
        )
        self.add(graph)

```


```

class RandomLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="random",
            labels=True
        )
        self.add(graph)


```
* Shell Layout: places vertices in concentric circles


Example: ShellLayout [¶](#shelllayout)

![../_images/ShellLayout-1.png](../_images/ShellLayout-1.png)

```
from manim import *

class ShellLayout(Scene):
    def construct(self):
        nlist = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3), (8, 3), (8, 1), (9, 1)],
            layout="shell",
            layout_config={"nlist": nlist},
            labels=True
        )
        self.add(graph)

```


```

class ShellLayout(Scene):
    def construct(self):
        nlist = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3), (8, 3), (8, 1), (9, 1)],
            layout="shell",
            layout_config={"nlist": nlist},
            labels=True
        )
        self.add(graph)


```
* Spectral Layout: places vertices using the eigenvectors of the graph Laplacian (clusters nodes which are an approximation of the ratio cut)


Example: SpectralLayout [¶](#spectrallayout)

![../_images/SpectralLayout-1.png](../_images/SpectralLayout-1.png)

```
from manim import *

class SpectralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spectral",
            labels=True
        )
        self.add(graph)

```


```

class SpectralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spectral",
            labels=True
        )
        self.add(graph)


```
* Sprial Layout: places vertices in a spiraling pattern


Example: SpiralLayout [¶](#spirallayout)

![../_images/SpiralLayout-1.png](../_images/SpiralLayout-1.png)

```
from manim import *

class SpiralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spiral",
            labels=True
        )
        self.add(graph)

```


```

class SpiralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spiral",
            labels=True
        )
        self.add(graph)


```
* Spring Layout: places nodes according to the Fruchterman\-Reingold force\-directed algorithm (attempts to minimize edge length while maximizing node separation)


Example: SpringLayout [¶](#springlayout)

![../_images/SpringLayout-1.png](../_images/SpringLayout-1.png)

```
from manim import *

class SpringLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spring",
            labels=True
        )
        self.add(graph)

```


```

class SpringLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spring",
            labels=True
        )
        self.add(graph)


```
* Tree Layout: places vertices into a tree with a root node and branches (can only be used with legal trees)


Example: TreeLayout [¶](#treelayout)

![../_images/TreeLayout-1.png](../_images/TreeLayout-1.png)

```
from manim import *

class TreeLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7],
            [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)],
            layout="tree",
            layout_config={"root_vertex": 1},
            labels=True
        )
        self.add(graph)

```


```

class TreeLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7],
            [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)],
            layout="tree",
            layout_config={"root_vertex": 1},
            labels=True
        )
        self.add(graph)


```
Methods



---

# FunctionGraph


# FunctionGraph[¶](#functiongraph "Link to this heading")


Qualified name: `manim.mobject.graphing.functions.FunctionGraph`


*class* FunctionGraph(*function*, *x\_range\=None*, *color\=ManimColor('\#FFFF00')*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/functions.html#FunctionGraph)[¶](#manim.mobject.graphing.functions.FunctionGraph "Link to this definition")
Bases: [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction")


A [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction") that spans the length of the scene by default.


Examples


Example: ExampleFunctionGraph [¶](#examplefunctiongraph)

![../_images/ExampleFunctionGraph-1.png](../_images/ExampleFunctionGraph-1.png)

```
from manim import *

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)

```


```

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)


```
Methods


| `get_function` |  |
| --- | --- |
| `get_point_from_function` |  |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*function*, *x\_range\=None*, *color\=ManimColor('\#FFFF00')*, *\*\*kwargs*)[¶](#manim.mobject.graphing.functions.FunctionGraph._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.



---

# ImplicitFunction


# ImplicitFunction[¶](#implicitfunction "Link to this heading")


Qualified name: `manim.mobject.graphing.functions.ImplicitFunction`


*class* ImplicitFunction(*func*, *x\_range\=None*, *y\_range\=None*, *min\_depth\=5*, *max\_quads\=1500*, *use\_smoothing\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/functions.html#ImplicitFunction)[¶](#manim.mobject.graphing.functions.ImplicitFunction "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


An implicit function.


Parameters:
* **func** (*Callable**\[**\[**float**,* *float**]**,* *float**]*) – The implicit function in the form `f(x, y) = 0`.
* **x\_range** (*Sequence**\[**float**]* *\|* *None*) – The x min and max of the function.
* **y\_range** (*Sequence**\[**float**]* *\|* *None*) – The y min and max of the function.
* **min\_depth** (*int*) – The minimum depth of the function to calculate.
* **max\_quads** (*int*) – The maximum number of quads to use.
* **use\_smoothing** (*bool*) – Whether or not to smoothen the curves.
* **kwargs** – Additional parameters to pass into `VMobject`


Note


A small `min_depth` \\(d\\) means that some small details might
be ignored if they don’t cross an edge of one of the
\\(4^d\\) uniform quads.


The value of `max_quads` strongly corresponds to the
quality of the curve, but a higher number of quads
may take longer to render.


Examples


Example: ImplicitFunctionExample [¶](#implicitfunctionexample)

![../_images/ImplicitFunctionExample-1.png](../_images/ImplicitFunctionExample-1.png)

```
from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)

```


```

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)


```
Methods


| [`generate_points`](#manim.mobject.graphing.functions.ImplicitFunction.generate_points "manim.mobject.graphing.functions.ImplicitFunction.generate_points") | Initializes `points` and therefore the shape. |
| --- | --- |
| [`init_points`](#manim.mobject.graphing.functions.ImplicitFunction.init_points "manim.mobject.graphing.functions.ImplicitFunction.init_points") | Initializes `points` and therefore the shape. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*func*, *x\_range\=None*, *y\_range\=None*, *min\_depth\=5*, *max\_quads\=1500*, *use\_smoothing\=True*, *\*\*kwargs*)[¶](#manim.mobject.graphing.functions.ImplicitFunction._original__init__ "Link to this definition")
An implicit function.


Parameters:
* **func** (*Callable**\[**\[**float**,* *float**]**,* *float**]*) – The implicit function in the form `f(x, y) = 0`.
* **x\_range** (*Sequence**\[**float**]* *\|* *None*) – The x min and max of the function.
* **y\_range** (*Sequence**\[**float**]* *\|* *None*) – The y min and max of the function.
* **min\_depth** (*int*) – The minimum depth of the function to calculate.
* **max\_quads** (*int*) – The maximum number of quads to use.
* **use\_smoothing** (*bool*) – Whether or not to smoothen the curves.
* **kwargs** – Additional parameters to pass into `VMobject`


Note


A small `min_depth` \\(d\\) means that some small details might
be ignored if they don’t cross an edge of one of the
\\(4^d\\) uniform quads.


The value of `max_quads` strongly corresponds to the
quality of the curve, but a higher number of quads
may take longer to render.


Examples


Example: ImplicitFunctionExample [¶](#implicitfunctionexample)

![../_images/ImplicitFunctionExample-2.png](../_images/ImplicitFunctionExample-2.png)

```
from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)

```


```

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)


```


generate\_points()[\[source]](../_modules/manim/mobject/graphing/functions.html#ImplicitFunction.generate_points)[¶](#manim.mobject.graphing.functions.ImplicitFunction.generate_points "Link to this definition")
Initializes `points` and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.


init\_points()[¶](#manim.mobject.graphing.functions.ImplicitFunction.init_points "Link to this definition")
Initializes `points` and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.



---

# ParametricFunction


# ParametricFunction[¶](#parametricfunction "Link to this heading")


Qualified name: `manim.mobject.graphing.functions.ParametricFunction`


*class* ParametricFunction(*function*, *t\_range\=(0*, *1\)*, *scaling\=\<manim.mobject.graphing.scale.LinearBase object\>*, *dt\=1e\-08*, *discontinuities\=None*, *use\_smoothing\=True*, *use\_vectorized\=False*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/functions.html#ParametricFunction)[¶](#manim.mobject.graphing.functions.ParametricFunction "Link to this definition")
Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


A parametric curve.


Parameters:
* **function** (*Callable**\[**\[**float**]**,* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]*) – The function to be plotted in the form of `(lambda t: (x(t), y(t), z(t)))`
* **t\_range** ([*Point2D*](manim.typing.html#manim.typing.Point2D "manim.typing.Point2D") *\|* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")) – Determines the length that the function spans in the form of (t\_min, t\_max, step\=0\.01\). By default `[0, 1]`
* **scaling** (*\_ScaleBase*) – Scaling class applied to the points of the function. Default of [`LinearBase`](manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase "manim.mobject.graphing.scale.LinearBase").
* **use\_smoothing** (*bool*) – Whether to interpolate between the points of the function after they have been created.
(Will have odd behaviour with a low number of points)
* **use\_vectorized** (*bool*) – Whether to pass in the generated t value array to the function as `[t_0, t_1, ...]`.
Only use this if your function supports it. Output should be a numpy array
of shape `[[x_0, x_1, ...], [y_0, y_1, ...], [z_0, z_1, ...]]` but `z` can
also be 0 if the Axes is 2D
* **discontinuities** (*Iterable**\[**float**]* *\|* *None*) – Values of t at which the function experiences discontinuity.
* **dt** (*float*) – The left and right tolerance for the discontinuities.


Examples


Example: PlotParametricFunction [¶](#plotparametricfunction)

![../_images/PlotParametricFunction-1.png](../_images/PlotParametricFunction-1.png)

```
from manim import *

class PlotParametricFunction(Scene):
    def func(self, t):
        return (np.sin(2 * t), np.sin(3 * t), 0)

    def construct(self):
        func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))

```


```

class PlotParametricFunction(Scene):
    def func(self, t):
        return (np.sin(2 * t), np.sin(3 * t), 0)

    def construct(self):
        func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))


```

Example: ThreeDParametricSpring [¶](#threedparametricspring)

![../_images/ThreeDParametricSpring-1.png](../_images/ThreeDParametricSpring-1.png)

```
from manim import *

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: (
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()

```


```

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: (
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()


```

Attention


If your function has discontinuities, you’ll have to specify the location
of the discontinuities manually. See the following example for guidance.


Example: DiscontinuousExample [¶](#discontinuousexample)

![../_images/DiscontinuousExample-1.png](../_images/DiscontinuousExample-1.png)

```
from manim import *

class DiscontinuousExample(Scene):
    def construct(self):
        ax1 = NumberPlane((-3, 3), (-4, 4))
        ax2 = NumberPlane((-3, 3), (-4, 4))
        VGroup(ax1, ax2).arrange()
        discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
        incorrect = ax1.plot(discontinuous_function, color=RED)
        correct = ax2.plot(
            discontinuous_function,
            discontinuities=[-2, 2],  # discontinuous points
            dt=0.1,  # left and right tolerance of discontinuity
            color=GREEN,
        )
        self.add(ax1, ax2, incorrect, correct)

```


```

class DiscontinuousExample(Scene):
    def construct(self):
        ax1 = NumberPlane((-3, 3), (-4, 4))
        ax2 = NumberPlane((-3, 3), (-4, 4))
        VGroup(ax1, ax2).arrange()
        discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
        incorrect = ax1.plot(discontinuous_function, color=RED)
        correct = ax2.plot(
            discontinuous_function,
            discontinuities=[-2, 2],  # discontinuous points
            dt=0.1,  # left and right tolerance of discontinuity
            color=GREEN,
        )
        self.add(ax1, ax2, incorrect, correct)


```
Methods


| [`generate_points`](#manim.mobject.graphing.functions.ParametricFunction.generate_points "manim.mobject.graphing.functions.ParametricFunction.generate_points") | Initializes `points` and therefore the shape. |
| --- | --- |
| `get_function` |  |
| `get_point_from_function` |  |
| [`init_points`](#manim.mobject.graphing.functions.ParametricFunction.init_points "manim.mobject.graphing.functions.ParametricFunction.init_points") | Initializes `points` and therefore the shape. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*function*, *t\_range\=(0*, *1\)*, *scaling\=\<manim.mobject.graphing.scale.LinearBase object\>*, *dt\=1e\-08*, *discontinuities\=None*, *use\_smoothing\=True*, *use\_vectorized\=False*, *\*\*kwargs*)[¶](#manim.mobject.graphing.functions.ParametricFunction._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **function** (*Callable**\[**\[**float**]**,* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]*)
* **t\_range** ([*Point2D*](manim.typing.html#manim.typing.Point2D "manim.typing.Point2D") *\|* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **scaling** (*\_ScaleBase*)
* **dt** (*float*)
* **discontinuities** (*Iterable**\[**float**]* *\|* *None*)
* **use\_smoothing** (*bool*)
* **use\_vectorized** (*bool*)


generate\_points()[\[source]](../_modules/manim/mobject/graphing/functions.html#ParametricFunction.generate_points)[¶](#manim.mobject.graphing.functions.ParametricFunction.generate_points "Link to this definition")
Initializes `points` and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.


init\_points()[¶](#manim.mobject.graphing.functions.ParametricFunction.init_points "Link to this definition")
Initializes `points` and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.



---

# NumberLine


# NumberLine[¶](#numberline "Link to this heading")


Qualified name: `manim.mobject.graphing.number\_line.NumberLine`


*class* NumberLine(*x\_range\=None*, *length\=None*, *unit\_size\=1*, *include\_ticks\=True*, *tick\_size\=0\.1*, *numbers\_with\_elongated\_ticks\=None*, *longer\_tick\_multiple\=2*, *exclude\_origin\_tick\=False*, *rotation\=0*, *stroke\_width\=2\.0*, *include\_tip\=False*, *tip\_width\=0\.35*, *tip\_height\=0\.35*, *tip\_shape\=None*, *include\_numbers\=False*, *font\_size\=36*, *label\_direction\=array(\[ 0\.*, *\-1\.*, *0\.])*, *label\_constructor\=\<class 'manim.mobject.text.tex\_mobject.MathTex'\>*, *scaling\=\<manim.mobject.graphing.scale.LinearBase object\>*, *line\_to\_number\_buff\=0\.25*, *decimal\_number\_config\=None*, *numbers\_to\_exclude\=None*, *numbers\_to\_include\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine)[¶](#manim.mobject.graphing.number_line.NumberLine "Link to this definition")
Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


Creates a number line with tick marks.


Parameters:
* **x\_range** (*Sequence**\[**float**]* *\|* *None*) – The `[x_min, x_max, x_step]` values to create the line.
* **length** (*float* *\|* *None*) – The length of the number line.
* **unit\_size** (*float*) – The distance between each tick of the line. Overwritten by `length`, if specified.
* **include\_ticks** (*bool*) – Whether to include ticks on the number line.
* **tick\_size** (*float*) – The length of each tick mark.
* **numbers\_with\_elongated\_ticks** (*Iterable**\[**float**]* *\|* *None*) – An iterable of specific values with elongated ticks.
* **longer\_tick\_multiple** (*int*) – Influences how many times larger elongated ticks are than regular ticks (2 \= 2x).
* **rotation** (*float*) – The angle (in radians) at which the line is rotated.
* **stroke\_width** (*float*) – The thickness of the line.
* **include\_tip** (*bool*) – Whether to add a tip to the end of the line.
* **tip\_width** (*float*) – The width of the tip.
* **tip\_height** (*float*) – The height of the tip.
* **tip\_shape** (*type**\[*[*ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")*]* *\|* *None*) – The mobject class used to construct the tip, or `None` (the
default) for the default arrow tip. Passed classes have to inherit
from [`ArrowTip`](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip").
* **include\_numbers** (*bool*) – Whether to add numbers to the tick marks. The number of decimal places is determined
by the step size, this default can be overridden by `decimal_number_config`.
* **scaling** (*\_ScaleBase*) – The way the `x_range` is value is scaled, i.e. [`LogBase`](manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase "manim.mobject.graphing.scale.LogBase") for a logarithmic numberline. Defaults to [`LinearBase`](manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase "manim.mobject.graphing.scale.LinearBase").
* **font\_size** (*float*) – The size of the label mobjects. Defaults to 36\.
* **label\_direction** (*Sequence**\[**float**]*) – The specific position to which label mobjects are added on the line.
* **label\_constructor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – Determines the mobject class that will be used to construct the labels of the number line.
* **line\_to\_number\_buff** (*float*) – The distance between the line and the label mobject.
* **decimal\_number\_config** (*dict* *\|* *None*) – Arguments that can be passed to [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") to influence number mobjects.
* **numbers\_to\_exclude** (*Iterable**\[**float**]* *\|* *None*) – An explicit iterable of numbers to not be added to the number line.
* **numbers\_to\_include** (*Iterable**\[**float**]* *\|* *None*) – An explicit iterable of numbers to add to the number line
* **kwargs** – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").
* **exclude\_origin\_tick** (*bool*)


Note


Number ranges that include both negative and positive values will be generated
from the 0 point, and may not include a tick at the min / max
values as the tick locations are dependent on the step size.


Examples


Example: NumberLineExample [¶](#numberlineexample)

![../_images/NumberLineExample-1.png](../_images/NumberLineExample-1.png)

```
from manim import *

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        num6 = l1.numbers[8]
        num6.set_color(RED)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
        self.add(line_group)

```


```

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        num6 = l1.numbers[8]
        num6.set_color(RED)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
        self.add(line_group)


```
Methods


| [`add_labels`](#manim.mobject.graphing.number_line.NumberLine.add_labels "manim.mobject.graphing.number_line.NumberLine.add_labels") | Adds specifically positioned labels to the [`NumberLine`](#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") using a `dict`. |
| --- | --- |
| [`add_numbers`](#manim.mobject.graphing.number_line.NumberLine.add_numbers "manim.mobject.graphing.number_line.NumberLine.add_numbers") | Adds [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects representing their position at each tick of the number line. |
| [`add_ticks`](#manim.mobject.graphing.number_line.NumberLine.add_ticks "manim.mobject.graphing.number_line.NumberLine.add_ticks") | Adds ticks to the number line. |
| `get_labels` |  |
| [`get_number_mobject`](#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "manim.mobject.graphing.number_line.NumberLine.get_number_mobject") | Generates a positioned [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobject generated according to `label_constructor`. |
| `get_number_mobjects` |  |
| [`get_tick`](#manim.mobject.graphing.number_line.NumberLine.get_tick "manim.mobject.graphing.number_line.NumberLine.get_tick") | Generates a tick and positions it along the number line. |
| `get_tick_marks` |  |
| [`get_tick_range`](#manim.mobject.graphing.number_line.NumberLine.get_tick_range "manim.mobject.graphing.number_line.NumberLine.get_tick_range") | Generates the range of values on which labels are plotted based on the `x_range` attribute of the number line. |
| `get_unit_size` |  |
| `get_unit_vector` |  |
| [`n2p`](#manim.mobject.graphing.number_line.NumberLine.n2p "manim.mobject.graphing.number_line.NumberLine.n2p") | Abbreviation for [`number_to_point()`](#manim.mobject.graphing.number_line.NumberLine.number_to_point "manim.mobject.graphing.number_line.NumberLine.number_to_point"). |
| [`number_to_point`](#manim.mobject.graphing.number_line.NumberLine.number_to_point "manim.mobject.graphing.number_line.NumberLine.number_to_point") | Accepts a value along the number line and returns a point with respect to the scene. |
| [`p2n`](#manim.mobject.graphing.number_line.NumberLine.p2n "manim.mobject.graphing.number_line.NumberLine.p2n") | Abbreviation for [`point_to_number()`](#manim.mobject.graphing.number_line.NumberLine.point_to_number "manim.mobject.graphing.number_line.NumberLine.point_to_number"). |
| [`point_to_number`](#manim.mobject.graphing.number_line.NumberLine.point_to_number "manim.mobject.graphing.number_line.NumberLine.point_to_number") | Accepts a point with respect to the scene and returns a float along the number line. |
| `rotate_about_number` |  |
| `rotate_about_zero` |  |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_create\_label\_tex(*label\_tex*, *label\_constructor\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine._create_label_tex)[¶](#manim.mobject.graphing.number_line.NumberLine._create_label_tex "Link to this definition")
Checks if the label is a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"), otherwise, creates a
label by passing `label_tex` to `label_constructor`.


Parameters:
* **label\_tex** (*str* *\|* *float* *\|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The label for which a mobject should be created. If the label already
is a mobject, no new mobject is created.
* **label\_constructor** (*Callable* *\|* *None*) – Optional. A class or function returning a mobject when
passing `label_tex` as an argument. If `None` is passed
(the default), the label constructor from the `label_constructor`
attribute is used.


Returns:
The label.


Return type:
[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


\_original\_\_init\_\_(*x\_range\=None*, *length\=None*, *unit\_size\=1*, *include\_ticks\=True*, *tick\_size\=0\.1*, *numbers\_with\_elongated\_ticks\=None*, *longer\_tick\_multiple\=2*, *exclude\_origin\_tick\=False*, *rotation\=0*, *stroke\_width\=2\.0*, *include\_tip\=False*, *tip\_width\=0\.35*, *tip\_height\=0\.35*, *tip\_shape\=None*, *include\_numbers\=False*, *font\_size\=36*, *label\_direction\=array(\[ 0\.*, *\-1\.*, *0\.])*, *label\_constructor\=\<class 'manim.mobject.text.tex\_mobject.MathTex'\>*, *scaling\=\<manim.mobject.graphing.scale.LinearBase object\>*, *line\_to\_number\_buff\=0\.25*, *decimal\_number\_config\=None*, *numbers\_to\_exclude\=None*, *numbers\_to\_include\=None*, *\*\*kwargs*)[¶](#manim.mobject.graphing.number_line.NumberLine._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **x\_range** (*Sequence**\[**float**]* *\|* *None*)
* **length** (*float* *\|* *None*)
* **unit\_size** (*float*)
* **include\_ticks** (*bool*)
* **tick\_size** (*float*)
* **numbers\_with\_elongated\_ticks** (*Iterable**\[**float**]* *\|* *None*)
* **longer\_tick\_multiple** (*int*)
* **exclude\_origin\_tick** (*bool*)
* **rotation** (*float*)
* **stroke\_width** (*float*)
* **include\_tip** (*bool*)
* **tip\_width** (*float*)
* **tip\_height** (*float*)
* **tip\_shape** (*type**\[*[*ArrowTip*](manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")*]* *\|* *None*)
* **include\_numbers** (*bool*)
* **font\_size** (*float*)
* **label\_direction** (*Sequence**\[**float**]*)
* **label\_constructor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
* **scaling** (*\_ScaleBase*)
* **line\_to\_number\_buff** (*float*)
* **decimal\_number\_config** (*dict* *\|* *None*)
* **numbers\_to\_exclude** (*Iterable**\[**float**]* *\|* *None*)
* **numbers\_to\_include** (*Iterable**\[**float**]* *\|* *None*)


add\_labels(*dict\_values*, *direction\=None*, *buff\=None*, *font\_size\=None*, *label\_constructor\=None*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_labels)[¶](#manim.mobject.graphing.number_line.NumberLine.add_labels "Link to this definition")
Adds specifically positioned labels to the [`NumberLine`](#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") using a `dict`.
The labels can be accessed after creation via `self.labels`.


Parameters:
* **dict\_values** (*dict**\[**float**,* *str* *\|* *float* *\|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – A dictionary consisting of the position along the number line and the mobject to be added:
`{1: Tex("Monday"), 3: Tex("Tuesday")}`. `label_constructor` will be used
to construct the labels if the value is not a mobject (`str` or `float`).
* **direction** (*Sequence**\[**float**]*) – Determines the direction at which the label is positioned next to the line.
* **buff** (*float* *\|* *None*) – The distance of the label from the line.
* **font\_size** (*float* *\|* *None*) – The font size of the mobject to be positioned.
* **label\_constructor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label.
Defaults to the `label_constructor` attribute of the number line
if not specified.


Raises:
**AttributeError** – If the label does not have a `font_size` attribute, an `AttributeError` is raised.


add\_numbers(*x\_values\=None*, *excluding\=None*, *font\_size\=None*, *label\_constructor\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_numbers)[¶](#manim.mobject.graphing.number_line.NumberLine.add_numbers "Link to this definition")
Adds [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects representing their position
at each tick of the number line. The numbers can be accessed after creation
via `self.numbers`.


Parameters:
* **x\_values** (*Iterable**\[**float**]* *\|* *None*) – An iterable of the values used to position and create the labels.
Defaults to the output produced by [`get_tick_range()`](#manim.mobject.graphing.number_line.NumberLine.get_tick_range "manim.mobject.graphing.number_line.NumberLine.get_tick_range")
* **excluding** (*Iterable**\[**float**]* *\|* *None*) – A list of values to exclude from `x_values`.
* **font\_size** (*float* *\|* *None*) – The font size of the labels. Defaults to the `font_size` attribute
of the number line.
* **label\_constructor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label.
Defaults to the `label_constructor` attribute of the number line
if not specified.


add\_ticks()[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_ticks)[¶](#manim.mobject.graphing.number_line.NumberLine.add_ticks "Link to this definition")
Adds ticks to the number line. Ticks can be accessed after creation
via `self.ticks`.


get\_number\_mobject(*x*, *direction\=None*, *buff\=None*, *font\_size\=None*, *label\_constructor\=None*, *\*\*number\_config*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_number_mobject)[¶](#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "Link to this definition")
Generates a positioned [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobject
generated according to `label_constructor`.


Parameters:
* **x** (*float*) – The x\-value at which the mobject should be positioned.
* **direction** (*Sequence**\[**float**]* *\|* *None*) – Determines the direction at which the label is positioned next to the line.
* **buff** (*float* *\|* *None*) – The distance of the label from the line.
* **font\_size** (*float* *\|* *None*) – The font size of the label mobject.
* **label\_constructor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *\|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label.
Defaults to the `label_constructor` attribute of the number line
if not specified.


Returns:
The positioned mobject.


Return type:
[`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber")


get\_tick(*x*, *size\=None*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_tick)[¶](#manim.mobject.graphing.number_line.NumberLine.get_tick "Link to this definition")
Generates a tick and positions it along the number line.


Parameters:
* **x** (*float*) – The position of the tick.
* **size** (*float* *\|* *None*) – The factor by which the tick is scaled.


Returns:
A positioned tick.


Return type:
[`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")


get\_tick\_range()[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_tick_range)[¶](#manim.mobject.graphing.number_line.NumberLine.get_tick_range "Link to this definition")
Generates the range of values on which labels are plotted based on the
`x_range` attribute of the number line.


Returns:
A numpy array of floats represnting values along the number line.


Return type:
np.ndarray


n2p(*number*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.n2p)[¶](#manim.mobject.graphing.number_line.NumberLine.n2p "Link to this definition")
Abbreviation for [`number_to_point()`](#manim.mobject.graphing.number_line.NumberLine.number_to_point "manim.mobject.graphing.number_line.NumberLine.number_to_point").


Parameters:
**number** (*float* *\|* *ndarray*)


Return type:
*ndarray*


number\_to\_point(*number*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.number_to_point)[¶](#manim.mobject.graphing.number_line.NumberLine.number_to_point "Link to this definition")
Accepts a value along the number line and returns a point with
respect to the scene.


Parameters:
**number** (*float* *\|* *ndarray*) – The value to be transformed into a coordinate. Or a list of values.


Returns:
A point with respect to the scene’s coordinate system. Or a list of points.


Return type:
np.ndarray


Examples


```
>>> from manim import NumberLine
>>> number_line = NumberLine()
>>> number_line.number_to_point(0)
array([0., 0., 0.])
>>> number_line.number_to_point(1)
array([1., 0., 0.])
>>> number_line.number_to_point([1,2,3])
array([[1., 0., 0.],
       [2., 0., 0.],
       [3., 0., 0.]])

```


p2n(*point*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.p2n)[¶](#manim.mobject.graphing.number_line.NumberLine.p2n "Link to this definition")
Abbreviation for [`point_to_number()`](#manim.mobject.graphing.number_line.NumberLine.point_to_number "manim.mobject.graphing.number_line.NumberLine.point_to_number").


Parameters:
**point** (*Sequence**\[**float**]*)


Return type:
float


point\_to\_number(*point*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#NumberLine.point_to_number)[¶](#manim.mobject.graphing.number_line.NumberLine.point_to_number "Link to this definition")
Accepts a point with respect to the scene and returns
a float along the number line.


Parameters:
**point** (*Sequence**\[**float**]*) – A sequence of values consisting of `(x_coord, y_coord, z_coord)`.


Returns:
A float representing a value along the number line.


Return type:
float


Examples


```
>>> from manim import NumberLine
>>> number_line = NumberLine()
>>> number_line.point_to_number((0,0,0))
0.0
>>> number_line.point_to_number((1,0,0))
1.0
>>> number_line.point_to_number([[0.5,0,0],[1,0,0],[1.5,0,0]])
array([0.5, 1. , 1.5])

```



---

# UnitInterval


# UnitInterval[¶](#unitinterval "Link to this heading")


Qualified name: `manim.mobject.graphing.number\_line.UnitInterval`


*class* UnitInterval(*unit\_size\=10*, *numbers\_with\_elongated\_ticks\=None*, *decimal\_number\_config\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/number_line.html#UnitInterval)[¶](#manim.mobject.graphing.number_line.UnitInterval "Link to this definition")
Bases: [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*unit\_size\=10*, *numbers\_with\_elongated\_ticks\=None*, *decimal\_number\_config\=None*, *\*\*kwargs*)[¶](#manim.mobject.graphing.number_line.UnitInterval._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.



---

# BarChart


# BarChart[¶](#barchart "Link to this heading")


Qualified name: `manim.mobject.graphing.probability.BarChart`


*class* BarChart(*values*, *bar\_names\=None*, *y\_range\=None*, *x\_length\=None*, *y\_length\=None*, *bar\_colors\=\['\#003f5c', '\#58508d', '\#bc5090', '\#ff6361', '\#ffa600']*, *bar\_width\=0\.6*, *bar\_fill\_opacity\=0\.7*, *bar\_stroke\_width\=3*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart)[¶](#manim.mobject.graphing.probability.BarChart "Link to this definition")
Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")


Creates a bar chart. Inherits from [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"), so it shares its methods
and attributes. Each axis inherits from [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine"), so pass in `x_axis_config`/`y_axis_config`
to control their attributes.


Parameters:
* **values** (*MutableSequence**\[**float**]*) – A sequence of values that determines the height of each bar. Accepts negative values.
* **bar\_names** (*Sequence**\[**str**]* *\|* *None*) – A sequence of names for each bar. Does not have to match the length of `values`.
* **y\_range** (*Sequence**\[**float**]* *\|* *None*) – The y\_axis range of values. If `None`, the range will be calculated based on the
min/max of `values` and the step will be calculated based on `y_length`.
* **x\_length** (*float* *\|* *None*) – The length of the x\-axis. If `None`, it is automatically calculated based on
the number of values and the width of the screen.
* **y\_length** (*float* *\|* *None*) – The length of the y\-axis.
* **bar\_colors** (*Iterable**\[**str**]*) – The color for the bars. Accepts a sequence of colors (can contain just one item).
If the length of\`\`bar\_colors\`\` does not match that of `values`,
intermediate colors will be automatically determined.
* **bar\_width** (*float*) – The length of a bar. Must be between 0 and 1\.
* **bar\_fill\_opacity** (*float*) – The fill opacity of the bars.
* **bar\_stroke\_width** (*float*) – The stroke width of the bars.


Examples


Example: BarChartExample [¶](#barchartexample)

![../_images/BarChartExample-1.png](../_images/BarChartExample-1.png)

```
from manim import *

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.add(chart, c_bar_lbls)

```


```

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.add(chart, c_bar_lbls)


```
Methods


| [`change_bar_values`](#manim.mobject.graphing.probability.BarChart.change_bar_values "manim.mobject.graphing.probability.BarChart.change_bar_values") | Updates the height of the bars of the chart. |
| --- | --- |
| [`get_bar_labels`](#manim.mobject.graphing.probability.BarChart.get_bar_labels "manim.mobject.graphing.probability.BarChart.get_bar_labels") | Annotates each bar with its corresponding value. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_add\_x\_axis\_labels()[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._add_x_axis_labels)[¶](#manim.mobject.graphing.probability.BarChart._add_x_axis_labels "Link to this definition")
Essentially :meth\`:\~.NumberLine.add\_labels\`, but differs in that
the direction of the label with respect to the x\_axis changes to UP or DOWN
depending on the value.


UP for negative values and DOWN for positive values.


\_create\_bar(*bar\_number*, *value*)[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._create_bar)[¶](#manim.mobject.graphing.probability.BarChart._create_bar "Link to this definition")
Creates a positioned bar on the chart.


Parameters:
* **bar\_number** (*int*) – Determines the x\-position of the bar.
* **value** (*float*) – The value that determines the height of the bar.


Returns:
A positioned rectangle representing a bar on the chart.


Return type:
[Rectangle](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")


\_original\_\_init\_\_(*values*, *bar\_names\=None*, *y\_range\=None*, *x\_length\=None*, *y\_length\=None*, *bar\_colors\=\['\#003f5c', '\#58508d', '\#bc5090', '\#ff6361', '\#ffa600']*, *bar\_width\=0\.6*, *bar\_fill\_opacity\=0\.7*, *bar\_stroke\_width\=3*, *\*\*kwargs*)[¶](#manim.mobject.graphing.probability.BarChart._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **values** (*MutableSequence**\[**float**]*)
* **bar\_names** (*Sequence**\[**str**]* *\|* *None*)
* **y\_range** (*Sequence**\[**float**]* *\|* *None*)
* **x\_length** (*float* *\|* *None*)
* **y\_length** (*float* *\|* *None*)
* **bar\_colors** (*Iterable**\[**str**]*)
* **bar\_width** (*float*)
* **bar\_fill\_opacity** (*float*)
* **bar\_stroke\_width** (*float*)


\_update\_colors()[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._update_colors)[¶](#manim.mobject.graphing.probability.BarChart._update_colors "Link to this definition")
Initialize the colors of the bars of the chart.


Sets the color of `self.bars` via `self.bar_colors`.


Primarily used when the bars are initialized with `self._add_bars`
or updated via `self.change_bar_values`.


change\_bar\_values(*values*, *update\_colors\=True*)[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart.change_bar_values)[¶](#manim.mobject.graphing.probability.BarChart.change_bar_values "Link to this definition")
Updates the height of the bars of the chart.


Parameters:
* **values** (*Iterable**\[**float**]*) – The values that will be used to update the height of the bars.
Does not have to match the number of bars.
* **update\_colors** (*bool*) – Whether to re\-initalize the colors of the bars based on `self.bar_colors`.


Examples


Example: ChangeBarValuesExample [¶](#changebarvaluesexample)

![../_images/ChangeBarValuesExample-1.png](../_images/ChangeBarValuesExample-1.png)

```
from manim import *

class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        chart = BarChart(
            values,
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )
        self.add(chart)

        chart.change_bar_values(list(reversed(values)))
        self.add(chart.get_bar_labels(font_size=24))

```


```

class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        chart = BarChart(
            values,
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )
        self.add(chart)

        chart.change_bar_values(list(reversed(values)))
        self.add(chart.get_bar_labels(font_size=24))


```


get\_bar\_labels(*color\=None*, *font\_size\=24*, *buff\=0\.25*, *label\_constructor\=\<class 'manim.mobject.text.tex\_mobject.Tex'\>*)[\[source]](../_modules/manim/mobject/graphing/probability.html#BarChart.get_bar_labels)[¶](#manim.mobject.graphing.probability.BarChart.get_bar_labels "Link to this definition")
Annotates each bar with its corresponding value. Use `self.bar_labels` to access the
labels after creation.


Parameters:
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of each label. By default `None` and is based on the parent’s bar color.
* **font\_size** (*float*) – The font size of each label.
* **buff** (*float*) – The distance from each label to its bar. By default 0\.4\.
* **label\_constructor** (*type**\[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The Mobject class to construct the labels, by default [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex").


Examples


Example: GetBarLabelsExample [¶](#getbarlabelsexample)

![../_images/GetBarLabelsExample-1.png](../_images/GetBarLabelsExample-1.png)

```
from manim import *

class GetBarLabelsExample(Scene):
    def construct(self):
        chart = BarChart(values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], y_range=[0, 10, 1])

        c_bar_lbls = chart.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

        self.add(chart, c_bar_lbls)

```


```

class GetBarLabelsExample(Scene):
    def construct(self):
        chart = BarChart(values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], y_range=[0, 10, 1])

        c_bar_lbls = chart.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

        self.add(chart, c_bar_lbls)


```



---

# LinearBase


# LinearBase[¶](#linearbase "Link to this heading")


Qualified name: `manim.mobject.graphing.scale.LinearBase`


*class* LinearBase(*scale\_factor\=1\.0*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase)[¶](#manim.mobject.graphing.scale.LinearBase "Link to this definition")
Bases: `_ScaleBase`


The default scaling class.


Parameters:
**scale\_factor** (*float*) – The slope of the linear function, by default 1\.0


Methods


| [`function`](#manim.mobject.graphing.scale.LinearBase.function "manim.mobject.graphing.scale.LinearBase.function") | Multiplies the value by the scale factor. |
| --- | --- |
| [`inverse_function`](#manim.mobject.graphing.scale.LinearBase.inverse_function "manim.mobject.graphing.scale.LinearBase.inverse_function") | Inverse of function. |


function(*value*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase.function)[¶](#manim.mobject.graphing.scale.LinearBase.function "Link to this definition")
Multiplies the value by the scale factor.


Parameters:
**value** (*float*) – Value to be multiplied by the scale factor.


Return type:
float


inverse\_function(*value*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LinearBase.inverse_function)[¶](#manim.mobject.graphing.scale.LinearBase.inverse_function "Link to this definition")
Inverse of function. Divides the value by the scale factor.


Parameters:
**value** (*float*) – value to be divided by the scale factor.


Return type:
float



---

# LogBase


# LogBase[¶](#logbase "Link to this heading")


Qualified name: `manim.mobject.graphing.scale.LogBase`


*class* LogBase(*base\=10*, *custom\_labels\=True*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LogBase)[¶](#manim.mobject.graphing.scale.LogBase "Link to this definition")
Bases: `_ScaleBase`


Scale for logarithmic graphs/functions.


Parameters:
* **base** (*float*) – The base of the log, by default 10\.
* **custom\_labels** (*bool*) – For use with [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"):
Whether or not to include `LaTeX` axis labels, by default True.


Examples


```
func = ParametricFunction(lambda x: x, scaling=LogBase(base=2))

```


Methods


| [`function`](#manim.mobject.graphing.scale.LogBase.function "manim.mobject.graphing.scale.LogBase.function") | Scales the value to fit it to a logarithmic scale.\`\`self.function(5\)\=\=10\*\*5\`\` |
| --- | --- |
| [`get_custom_labels`](#manim.mobject.graphing.scale.LogBase.get_custom_labels "manim.mobject.graphing.scale.LogBase.get_custom_labels") | Produces custom [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`. |
| [`inverse_function`](#manim.mobject.graphing.scale.LogBase.inverse_function "manim.mobject.graphing.scale.LogBase.inverse_function") | Inverse of `function`. |


function(*value*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.function)[¶](#manim.mobject.graphing.scale.LogBase.function "Link to this definition")
Scales the value to fit it to a logarithmic scale.\`\`self.function(5\)\=\=10\*\*5\`\`


Parameters:
**value** (*float*)


Return type:
float


get\_custom\_labels(*val\_range*, *unit\_decimal\_places\=0*, *\*\*base\_config*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.get_custom_labels)[¶](#manim.mobject.graphing.scale.LogBase.get_custom_labels "Link to this definition")
Produces custom [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`.


Parameters:
* **val\_range** (*Iterable**\[**float**]*) – The iterable of values used to create the labels. Determines the exponent.
* **unit\_decimal\_places** (*int*) – The number of decimal places to include in the exponent
* **base\_config** (*dict**\[**str**,* *Any**]*) – Additional arguments to be passed to [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").


Return type:
list\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


inverse\_function(*value*)[\[source]](../_modules/manim/mobject/graphing/scale.html#LogBase.inverse_function)[¶](#manim.mobject.graphing.scale.LogBase.inverse_function "Link to this definition")
Inverse of `function`. The value must be greater than 0


Parameters:
**value** (*float*)


Return type:
float



---

# Group


# Group[¶](#group "Link to this heading")


Qualified name: `manim.mobject.mobject.Group`


*class* Group(*\*mobjects*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Group)[¶](#manim.mobject.mobject.Group "Link to this definition")
Bases: [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Groups together multiple [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Notes


When adding the same mobject more than once, repetitions are ignored.
Use [`Mobject.copy()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") to create a separate copy which can then
be added to the group.


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*mobjects*, *\*\*kwargs*)[¶](#manim.mobject.mobject.Group._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Return type:
None



---

# Mobject


# Mobject[¶](#mobject "Link to this heading")


Qualified name: `manim.mobject.mobject.Mobject`


*class* Mobject(*color\=ManimColor('\#FFFFFF')*, *name\=None*, *dim\=3*, *target\=None*, *z\_index\=0*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject)[¶](#manim.mobject.mobject.Mobject "Link to this definition")
Bases: `object`


Mathematical Object: base class for objects that can be displayed on screen.


There is a compatibility layer that allows for
getting and setting generic attributes with `get_*`
and `set_*` methods. See [`set()`](#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") for more details.


Parameters:
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *list**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*)
* **name** (*str* *\|* *None*)
* **dim** (*int*)
* **z\_index** (*float*)


submobjects[¶](#manim.mobject.mobject.Mobject.submobjects "Link to this definition")
The contained objects.


Type:
List\[[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


points[¶](#manim.mobject.mobject.Mobject.points "Link to this definition")
The points of the objects.


See also


[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")


Type:
`numpy.ndarray`


Methods


| [`add`](#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add") | Add mobjects as submobjects. |
| --- | --- |
| [`add_animation_override`](#manim.mobject.mobject.Mobject.add_animation_override "manim.mobject.mobject.Mobject.add_animation_override") | Add an animation override. |
| [`add_background_rectangle`](#manim.mobject.mobject.Mobject.add_background_rectangle "manim.mobject.mobject.Mobject.add_background_rectangle") | Add a BackgroundRectangle as submobject. |
| `add_background_rectangle_to_family_members_with_points` |  |
| `add_background_rectangle_to_submobjects` |  |
| `add_n_more_submobjects` |  |
| [`add_to_back`](#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back") | Add all passed mobjects to the back of the submobjects. |
| [`add_updater`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater") | Add an update function to this mobject. |
| [`align_data`](#manim.mobject.mobject.Mobject.align_data "manim.mobject.mobject.Mobject.align_data") | Aligns the data of this mobject with another mobject. |
| [`align_on_border`](#manim.mobject.mobject.Mobject.align_on_border "manim.mobject.mobject.Mobject.align_on_border") | Direction just needs to be a vector pointing towards side or corner in the 2d plane. |
| `align_points` |  |
| `align_points_with_larger` |  |
| `align_submobjects` |  |
| [`align_to`](#manim.mobject.mobject.Mobject.align_to "manim.mobject.mobject.Mobject.align_to") | Aligns mobject to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction. |
| [`animation_override_for`](#manim.mobject.mobject.Mobject.animation_override_for "manim.mobject.mobject.Mobject.animation_override_for") | Returns the function defining a specific animation override for this class. |
| [`apply_complex_function`](#manim.mobject.mobject.Mobject.apply_complex_function "manim.mobject.mobject.Mobject.apply_complex_function") | Applies a complex function to a [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| `apply_function` |  |
| `apply_function_to_position` |  |
| `apply_function_to_submobject_positions` |  |
| `apply_matrix` |  |
| `apply_over_attr_arrays` |  |
| `apply_points_function_about_point` |  |
| [`apply_to_family`](#manim.mobject.mobject.Mobject.apply_to_family "manim.mobject.mobject.Mobject.apply_to_family") | Apply a function to `self` and every submobject with points recursively. |
| [`arrange`](#manim.mobject.mobject.Mobject.arrange "manim.mobject.mobject.Mobject.arrange") | Sorts [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to each other on screen. |
| [`arrange_in_grid`](#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid") | Arrange submobjects in a grid. |
| [`arrange_submobjects`](#manim.mobject.mobject.Mobject.arrange_submobjects "manim.mobject.mobject.Mobject.arrange_submobjects") | Arrange the position of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") with a small buffer. |
| [`become`](#manim.mobject.mobject.Mobject.become "manim.mobject.mobject.Mobject.become") | Edit points, colors and submobjects to be identical to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`center`](#manim.mobject.mobject.Mobject.center "manim.mobject.mobject.Mobject.center") | Moves the center of the mobject to the center of the scene. |
| [`clear_updaters`](#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters") | Remove every updater. |
| [`copy`](#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") | Create and return an identical copy of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") including all [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| `fade` |  |
| `fade_to` |  |
| `family_members_with_points` |  |
| [`flip`](#manim.mobject.mobject.Mobject.flip "manim.mobject.mobject.Mobject.flip") | Flips/Mirrors an mobject about its center. |
| [`generate_points`](#manim.mobject.mobject.Mobject.generate_points "manim.mobject.mobject.Mobject.generate_points") | Initializes [`points`](#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") and therefore the shape. |
| `generate_target` |  |
| [`get_all_points`](#manim.mobject.mobject.Mobject.get_all_points "manim.mobject.mobject.Mobject.get_all_points") | Return all points from this mobject and all submobjects. |
| `get_array_attrs` |  |
| [`get_bottom`](#manim.mobject.mobject.Mobject.get_bottom "manim.mobject.mobject.Mobject.get_bottom") | Get bottom Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| `get_boundary_point` |  |
| [`get_center`](#manim.mobject.mobject.Mobject.get_center "manim.mobject.mobject.Mobject.get_center") | Get center Point3Ds |
| `get_center_of_mass` |  |
| [`get_color`](#manim.mobject.mobject.Mobject.get_color "manim.mobject.mobject.Mobject.get_color") | Returns the color of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_coord`](#manim.mobject.mobject.Mobject.get_coord "manim.mobject.mobject.Mobject.get_coord") | Meant to generalize `get_x`, `get_y` and `get_z` |
| [`get_corner`](#manim.mobject.mobject.Mobject.get_corner "manim.mobject.mobject.Mobject.get_corner") | Get corner Point3Ds for certain direction. |
| [`get_critical_point`](#manim.mobject.mobject.Mobject.get_critical_point "manim.mobject.mobject.Mobject.get_critical_point") | Picture a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`get_edge_center`](#manim.mobject.mobject.Mobject.get_edge_center "manim.mobject.mobject.Mobject.get_edge_center") | Get edge Point3Ds for certain direction. |
| [`get_end`](#manim.mobject.mobject.Mobject.get_end "manim.mobject.mobject.Mobject.get_end") | Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends. |
| `get_extremum_along_dim` |  |
| `get_family` |  |
| `get_family_updaters` |  |
| `get_group_class` |  |
| `get_image` |  |
| [`get_left`](#manim.mobject.mobject.Mobject.get_left "manim.mobject.mobject.Mobject.get_left") | Get left Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_merged_array`](#manim.mobject.mobject.Mobject.get_merged_array "manim.mobject.mobject.Mobject.get_merged_array") | Return all of a given attribute from this mobject and all submobjects. |
| [`get_midpoint`](#manim.mobject.mobject.Mobject.get_midpoint "manim.mobject.mobject.Mobject.get_midpoint") | Get Point3Ds of the middle of the path that forms the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`get_mobject_type_class`](#manim.mobject.mobject.Mobject.get_mobject_type_class "manim.mobject.mobject.Mobject.get_mobject_type_class") | Return the base class of this mobject type. |
| [`get_nadir`](#manim.mobject.mobject.Mobject.get_nadir "manim.mobject.mobject.Mobject.get_nadir") | Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| `get_num_points` |  |
| `get_pieces` |  |
| [`get_point_mobject`](#manim.mobject.mobject.Mobject.get_point_mobject "manim.mobject.mobject.Mobject.get_point_mobject") | The simplest [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self. |
| `get_points_defining_boundary` |  |
| [`get_right`](#manim.mobject.mobject.Mobject.get_right "manim.mobject.mobject.Mobject.get_right") | Get right Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_start`](#manim.mobject.mobject.Mobject.get_start "manim.mobject.mobject.Mobject.get_start") | Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts. |
| [`get_start_and_end`](#manim.mobject.mobject.Mobject.get_start_and_end "manim.mobject.mobject.Mobject.get_start_and_end") | Returns starting and ending point of a stroke as a `tuple`. |
| [`get_time_based_updaters`](#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters") | Return all updaters using the `dt` parameter. |
| [`get_top`](#manim.mobject.mobject.Mobject.get_top "manim.mobject.mobject.Mobject.get_top") | Get top Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_updaters`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters") | Return all updaters. |
| [`get_x`](#manim.mobject.mobject.Mobject.get_x "manim.mobject.mobject.Mobject.get_x") | Returns x Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| [`get_y`](#manim.mobject.mobject.Mobject.get_y "manim.mobject.mobject.Mobject.get_y") | Returns y Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| [`get_z`](#manim.mobject.mobject.Mobject.get_z "manim.mobject.mobject.Mobject.get_z") | Returns z Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| `get_z_index_reference_point` |  |
| [`get_zenith`](#manim.mobject.mobject.Mobject.get_zenith "manim.mobject.mobject.Mobject.get_zenith") | Get zenith Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`has_no_points`](#manim.mobject.mobject.Mobject.has_no_points "manim.mobject.mobject.Mobject.has_no_points") | Check if [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *does not* contains points. |
| [`has_points`](#manim.mobject.mobject.Mobject.has_points "manim.mobject.mobject.Mobject.has_points") | Check if [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") contains points. |
| [`has_time_based_updater`](#manim.mobject.mobject.Mobject.has_time_based_updater "manim.mobject.mobject.Mobject.has_time_based_updater") | Test if `self` has a time based updater. |
| [`init_colors`](#manim.mobject.mobject.Mobject.init_colors "manim.mobject.mobject.Mobject.init_colors") | Initializes the colors. |
| [`insert`](#manim.mobject.mobject.Mobject.insert "manim.mobject.mobject.Mobject.insert") | Inserts a mobject at a specific position into self.submobjects |
| [`interpolate`](#manim.mobject.mobject.Mobject.interpolate "manim.mobject.mobject.Mobject.interpolate") | Turns this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") into an interpolation between `mobject1` and `mobject2`. |
| `interpolate_color` |  |
| [`invert`](#manim.mobject.mobject.Mobject.invert "manim.mobject.mobject.Mobject.invert") | Inverts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| `is_off_screen` |  |
| [`length_over_dim`](#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim") | Measure the length of an [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction. |
| [`match_color`](#manim.mobject.mobject.Mobject.match_color "manim.mobject.mobject.Mobject.match_color") | Match the color with the color of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_coord`](#manim.mobject.mobject.Mobject.match_coord "manim.mobject.mobject.Mobject.match_coord") | Match the Point3Ds with the Point3Ds of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_depth`](#manim.mobject.mobject.Mobject.match_depth "manim.mobject.mobject.Mobject.match_depth") | Match the depth with the depth of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_dim_size`](#manim.mobject.mobject.Mobject.match_dim_size "manim.mobject.mobject.Mobject.match_dim_size") | Match the specified dimension with the dimension of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_height`](#manim.mobject.mobject.Mobject.match_height "manim.mobject.mobject.Mobject.match_height") | Match the height with the height of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_points`](#manim.mobject.mobject.Mobject.match_points "manim.mobject.mobject.Mobject.match_points") | Edit points, positions, and submobjects to be identical to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), while keeping the style unchanged. |
| [`match_updaters`](#manim.mobject.mobject.Mobject.match_updaters "manim.mobject.mobject.Mobject.match_updaters") | Match the updaters of the given mobject. |
| [`match_width`](#manim.mobject.mobject.Mobject.match_width "manim.mobject.mobject.Mobject.match_width") | Match the width with the width of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_x`](#manim.mobject.mobject.Mobject.match_x "manim.mobject.mobject.Mobject.match_x") | Match x coord. |
| [`match_y`](#manim.mobject.mobject.Mobject.match_y "manim.mobject.mobject.Mobject.match_y") | Match y coord. |
| [`match_z`](#manim.mobject.mobject.Mobject.match_z "manim.mobject.mobject.Mobject.match_z") | Match z coord. |
| [`move_to`](#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to") | Move center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to certain Point3D. |
| [`next_to`](#manim.mobject.mobject.Mobject.next_to "manim.mobject.mobject.Mobject.next_to") | Move this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to another's [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or Point3D. |
| `nonempty_submobjects` |  |
| [`null_point_align`](#manim.mobject.mobject.Mobject.null_point_align "manim.mobject.mobject.Mobject.null_point_align") | If a [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") with points is being aligned to one without, treat both as groups, and push the one with points into its own submobjects list. |
| `point_from_proportion` |  |
| `pose_at_angle` |  |
| `proportion_from_point` |  |
| `push_self_into_submobjects` |  |
| `put_start_and_end_on` |  |
| [`reduce_across_dimension`](#manim.mobject.mobject.Mobject.reduce_across_dimension "manim.mobject.mobject.Mobject.reduce_across_dimension") | Find the min or max value from a dimension across all points in this and submobjects. |
| [`remove`](#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove") | Remove [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| [`remove_updater`](#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater") | Remove an updater. |
| [`repeat`](#manim.mobject.mobject.Mobject.repeat "manim.mobject.mobject.Mobject.repeat") | This can make transition animations nicer |
| `repeat_submobject` |  |
| `replace` |  |
| `rescale_to_fit` |  |
| [`reset_points`](#manim.mobject.mobject.Mobject.reset_points "manim.mobject.mobject.Mobject.reset_points") | Sets [`points`](#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") to be an empty array. |
| [`restore`](#manim.mobject.mobject.Mobject.restore "manim.mobject.mobject.Mobject.restore") | Restores the state that was previously saved with [`save_state()`](#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state"). |
| [`resume_updating`](#manim.mobject.mobject.Mobject.resume_updating "manim.mobject.mobject.Mobject.resume_updating") | Enable updating from updaters and animations. |
| `reverse_points` |  |
| [`rotate`](#manim.mobject.mobject.Mobject.rotate "manim.mobject.mobject.Mobject.rotate") | Rotates the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about a certain point. |
| [`rotate_about_origin`](#manim.mobject.mobject.Mobject.rotate_about_origin "manim.mobject.mobject.Mobject.rotate_about_origin") | Rotates the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about the ORIGIN, which is at \[0,0,0]. |
| [`save_image`](#manim.mobject.mobject.Mobject.save_image "manim.mobject.mobject.Mobject.save_image") | Saves an image of only this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") at its position to a png file. |
| [`save_state`](#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state") | Save the current state (position, color \& size). |
| [`scale`](#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale") | Scale the size by a factor. |
| [`scale_to_fit_depth`](#manim.mobject.mobject.Mobject.scale_to_fit_depth "manim.mobject.mobject.Mobject.scale_to_fit_depth") | Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth while keeping width/height proportional. |
| [`scale_to_fit_height`](#manim.mobject.mobject.Mobject.scale_to_fit_height "manim.mobject.mobject.Mobject.scale_to_fit_height") | Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height while keeping width/depth proportional. |
| [`scale_to_fit_width`](#manim.mobject.mobject.Mobject.scale_to_fit_width "manim.mobject.mobject.Mobject.scale_to_fit_width") | Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width while keeping height/depth proportional. |
| [`set`](#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") | Sets attributes. |
| [`set_color`](#manim.mobject.mobject.Mobject.set_color "manim.mobject.mobject.Mobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
| [`set_color_by_gradient`](#manim.mobject.mobject.Mobject.set_color_by_gradient "manim.mobject.mobject.Mobject.set_color_by_gradient") | param colors: The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN). |
| `set_colors_by_radial_gradient` |  |
| `set_coord` |  |
| [`set_default`](#manim.mobject.mobject.Mobject.set_default "manim.mobject.mobject.Mobject.set_default") | Sets the default values of keyword arguments. |
| `set_submobject_colors_by_gradient` |  |
| `set_submobject_colors_by_radial_gradient` |  |
| [`set_x`](#manim.mobject.mobject.Mobject.set_x "manim.mobject.mobject.Mobject.set_x") | Set x value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`) |
| [`set_y`](#manim.mobject.mobject.Mobject.set_y "manim.mobject.mobject.Mobject.set_y") | Set y value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`) |
| [`set_z`](#manim.mobject.mobject.Mobject.set_z "manim.mobject.mobject.Mobject.set_z") | Set z value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`) |
| [`set_z_index`](#manim.mobject.mobject.Mobject.set_z_index "manim.mobject.mobject.Mobject.set_z_index") | Sets the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")'s `z_index` to the value specified in z\_index\_value. |
| [`set_z_index_by_z_Point3D`](#manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D "manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D") | Sets the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")'s z Point3D to the value of `z_index`. |
| [`shift`](#manim.mobject.mobject.Mobject.shift "manim.mobject.mobject.Mobject.shift") | Shift by the given vectors. |
| `shift_onto_screen` |  |
| `show` |  |
| [`shuffle`](#manim.mobject.mobject.Mobject.shuffle "manim.mobject.mobject.Mobject.shuffle") | Shuffles the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| [`shuffle_submobjects`](#manim.mobject.mobject.Mobject.shuffle_submobjects "manim.mobject.mobject.Mobject.shuffle_submobjects") | Shuffles the order of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") |
| [`sort`](#manim.mobject.mobject.Mobject.sort "manim.mobject.mobject.Mobject.sort") | Sorts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") by a function defined by `submob_func`. |
| [`sort_submobjects`](#manim.mobject.mobject.Mobject.sort_submobjects "manim.mobject.mobject.Mobject.sort_submobjects") | Sort the [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") |
| `space_out_submobjects` |  |
| `split` |  |
| `stretch` |  |
| `stretch_about_point` |  |
| [`stretch_to_fit_depth`](#manim.mobject.mobject.Mobject.stretch_to_fit_depth "manim.mobject.mobject.Mobject.stretch_to_fit_depth") | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth, not keeping width/height proportional. |
| [`stretch_to_fit_height`](#manim.mobject.mobject.Mobject.stretch_to_fit_height "manim.mobject.mobject.Mobject.stretch_to_fit_height") | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height, not keeping width/depth proportional. |
| [`stretch_to_fit_width`](#manim.mobject.mobject.Mobject.stretch_to_fit_width "manim.mobject.mobject.Mobject.stretch_to_fit_width") | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width, not keeping height/depth proportional. |
| `surround` |  |
| [`suspend_updating`](#manim.mobject.mobject.Mobject.suspend_updating "manim.mobject.mobject.Mobject.suspend_updating") | Disable updating from updaters and animations. |
| `throw_error_if_no_points` |  |
| [`to_corner`](#manim.mobject.mobject.Mobject.to_corner "manim.mobject.mobject.Mobject.to_corner") | Moves this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given corner of the screen. |
| [`to_edge`](#manim.mobject.mobject.Mobject.to_edge "manim.mobject.mobject.Mobject.to_edge") | Moves this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given edge of the screen, without affecting its position in the other dimension. |
| `to_original_color` |  |
| [`update`](#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update") | Apply all updaters. |


Attributes


| [`animate`](#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| [`depth`](#manim.mobject.mobject.Mobject.depth "manim.mobject.mobject.Mobject.depth") | The depth of the mobject. |
| [`height`](#manim.mobject.mobject.Mobject.height "manim.mobject.mobject.Mobject.height") | The height of the mobject. |
| [`width`](#manim.mobject.mobject.Mobject.width "manim.mobject.mobject.Mobject.width") | The width of the mobject. |


*classmethod* \_add\_intrinsic\_animation\_overrides()[\[source]](../_modules/manim/mobject/mobject.html#Mobject._add_intrinsic_animation_overrides)[¶](#manim.mobject.mobject.Mobject._add_intrinsic_animation_overrides "Link to this definition")
Initializes animation overrides marked with the [`override_animation()`](manim.animation.animation.html#manim.animation.animation.override_animation "manim.animation.animation.override_animation")
decorator.


Return type:
None


add(*\*mobjects*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.add)[¶](#manim.mobject.mobject.Mobject.add "Link to this definition")
Add mobjects as submobjects.


The mobjects are added to [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").


Subclasses of mobject may implement `+` and `+=` dunder methods.


Parameters:
**mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Raises:
* **ValueError** – When a mobject tries to add itself.
* **TypeError** – When trying to add an object that is not an instance of [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Notes


A mobject cannot contain itself, and it cannot contain a submobject
more than once. If the parent mobject is displayed, the newly\-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).


See also


[`remove()`](#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove"), [`add_to_back()`](#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back")


Examples


```
>>> outer = Mobject()
>>> inner = Mobject()
>>> outer = outer.add(inner)

```


Duplicates are not added again:


```
>>> outer = outer.add(inner)
>>> len(outer.submobjects)
1

```


Adding an object to itself raises an error:


```
>>> outer.add(outer)
Traceback (most recent call last):
...
ValueError: Mobject cannot contain self

```


A given mobject cannot be added as a submobject
twice to some parent:


```
>>> parent = Mobject(name="parent")
>>> child = Mobject(name="child")
>>> parent.add(child, child)
[...] WARNING  ...
parent
>>> parent.submobjects
[child]

```


*classmethod* add\_animation\_override(*animation\_class*, *override\_func*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.add_animation_override)[¶](#manim.mobject.mobject.Mobject.add_animation_override "Link to this definition")
Add an animation override.


This does not apply to subclasses.


Parameters:
* **animation\_class** (*type**\[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – The animation type to be overridden
* **override\_func** ([*FunctionOverride*](manim.typing.html#manim.typing.FunctionOverride "manim.typing.FunctionOverride")) – The function returning an animation replacing the default animation. It gets
passed the parameters given to the animation constructor.


Raises:
**MultiAnimationOverrideException** – If the overridden animation was already overridden.


Return type:
None


add\_background\_rectangle(*color\=None*, *opacity\=0\.75*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.add_background_rectangle)[¶](#manim.mobject.mobject.Mobject.add_background_rectangle "Link to this definition")
Add a BackgroundRectangle as submobject.


The BackgroundRectangle is added behind other submobjects.


This can be used to increase the mobjects visibility in front of a noisy background.


Parameters:
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of the BackgroundRectangle
* **opacity** (*float*) – The opacity of the BackgroundRectangle
* **kwargs** – Additional keyword arguments passed to the BackgroundRectangle constructor


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`add_to_back()`](#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back"), [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle")


add\_to\_back(*\*mobjects*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.add_to_back)[¶](#manim.mobject.mobject.Mobject.add_to_back "Link to this definition")
Add all passed mobjects to the back of the submobjects.


If [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") already contains the given mobjects, they just get moved
to the back instead.


Parameters:
**mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Note


Technically, this is done by adding (or moving) the mobjects to
the head of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). The head of this list is rendered
first, which places the corresponding mobjects behind the
subsequent list members.


Raises:
* **ValueError** – When a mobject tries to add itself.
* **TypeError** – When trying to add an object that is not an instance of [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


Notes


A mobject cannot contain itself, and it cannot contain a submobject
more than once. If the parent mobject is displayed, the newly\-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).


See also


[`remove()`](#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove"), [`add()`](#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add")


add\_updater(*update\_function*, *index\=None*, *call\_updater\=False*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.add_updater)[¶](#manim.mobject.mobject.Mobject.add_updater "Link to this definition")
Add an update function to this mobject.


Update functions, or updaters in short, are functions that are applied to the
Mobject in every frame.


Parameters:
* **update\_function** ([*Updater*](manim.mobject.mobject.html#manim.mobject.mobject.Updater "manim.mobject.mobject.Updater")) – The update function to be added.
Whenever [`update()`](#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update") is called, this update function gets called using
`self` as the first parameter.
The updater can have a second parameter `dt`. If it uses this parameter,
it gets called using a second value `dt`, usually representing the time
in seconds since the last call of [`update()`](#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update").
* **index** (*int* *\|* *None*) – The index at which the new updater should be added in `self.updaters`.
In case `index` is `None` the updater will be added at the end.
* **call\_updater** (*bool*) – Whether or not to call the updater initially. If `True`, the updater will
be called using `dt=0`.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Examples


Example: NextToUpdater [¶](#nexttoupdater)


```
from manim import *

class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))

```


```

class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))


```

Example: DtUpdater [¶](#dtupdater)


```
from manim import *

class DtUpdater(Scene):
    def construct(self):
        square = Square()

        #Let the square rotate 90° per second
        square.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(square)
        self.wait(2)

```


```

class DtUpdater(Scene):
    def construct(self):
        square = Square()

        #Let the square rotate 90° per second
        square.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(square)
        self.wait(2)


```

See also


[`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters"), [`remove_updater()`](#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater"), [`UpdateFromFunc`](manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc "manim.animation.updaters.update.UpdateFromFunc")


align\_data(*mobject*, *skip\_point\_alignment\=False*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.align_data)[¶](#manim.mobject.mobject.Mobject.align_data "Link to this definition")
Aligns the data of this mobject with another mobject.


Afterwards, the two mobjects will have the same number of submobjects
(see `align_submobjects()`), the same parent structure (see
[`null_point_align()`](#manim.mobject.mobject.Mobject.null_point_align "manim.mobject.mobject.Mobject.null_point_align")). If `skip_point_alignment` is false,
they will also have the same number of points (see [`align_points()`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.align_points "manim.mobject.types.vectorized_mobject.VMobject.align_points")).


Parameters:
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The other mobject this mobject should be aligned to.
* **skip\_point\_alignment** (*bool*) – Controls whether or not the computationally expensive
point alignment is skipped (default: False).


Return type:
None


align\_on\_border(*direction*, *buff\=0\.5*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.align_on_border)[¶](#manim.mobject.mobject.Mobject.align_on_border "Link to this definition")
Direction just needs to be a vector pointing towards side or
corner in the 2d plane.


Parameters:
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **buff** (*float*)


Return type:
Self


align\_to(*mobject\_or\_point*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.align_to)[¶](#manim.mobject.mobject.Mobject.align_to "Link to this definition")
Aligns mobject to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction.


Examples:
mob1\.align\_to(mob2, UP) moves mob1 vertically so that its
top edge lines ups with mob2’s top edge.


Parameters:
* **mobject\_or\_point** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *\|* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


*property* animate*: \_AnimationBuilder \| Self*[¶](#manim.mobject.mobject.Mobject.animate "Link to this definition")
Used to animate the application of any method of `self`.


Any method called on `animate` is converted to an animation of applying
that method on the mobject itself.


For example, `square.set_fill(WHITE)` sets the fill color of a square,
while `square.animate.set_fill(WHITE)` animates this action.


Multiple methods can be put in a single animation once via chaining:


```
self.play(my_mobject.animate.shift(RIGHT).rotate(PI))

```


Warning


Passing multiple animations for the same [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in one
call to [`play()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") is discouraged and will most likely
not work properly. Instead of writing an animation like


```
self.play(my_mobject.animate.shift(RIGHT), my_mobject.animate.rotate(PI))

```


make use of method chaining.


Keyword arguments that can be passed to [`Scene.play()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") can be passed
directly after accessing `.animate`, like so:


```
self.play(my_mobject.animate(rate_func=linear).shift(RIGHT))

```


This is especially useful when animating simultaneous `.animate` calls that
you want to behave differently:


```
self.play(
    mobject1.animate(run_time=2).rotate(PI),
    mobject2.animate(rate_func=there_and_back).shift(RIGHT),
)

```


See also


[`override_animate()`](manim.mobject.mobject.html#manim.mobject.mobject.override_animate "manim.mobject.mobject.override_animate")


Examples


Example: AnimateExample [¶](#animateexample)


```
from manim import *

class AnimateExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI / 2))
        self.play(Uncreate(s))

```


```

class AnimateExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI / 2))
        self.play(Uncreate(s))


```

Example: AnimateChainExample [¶](#animatechainexample)


```
from manim import *

class AnimateChainExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))

```


```

class AnimateChainExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))


```

Example: AnimateWithArgsExample [¶](#animatewithargsexample)


```
from manim import *

class AnimateWithArgsExample(Scene):
    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )

```


```

class AnimateWithArgsExample(Scene):
    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )


```

Warning


`.animate`will interpolate the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") between its points prior to
`.animate` and its points after applying `.animate` to it. This may
result in unexpected behavior when attempting to interpolate along paths,
or rotations.
If you want animations to consider the points between, consider using
[`ValueTracker`](manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker") with updaters instead.


*classmethod* animation\_override\_for(*animation\_class*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.animation_override_for)[¶](#manim.mobject.mobject.Mobject.animation_override_for "Link to this definition")
Returns the function defining a specific animation override for this class.


Parameters:
**animation\_class** (*type**\[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – The animation class for which the override function should be returned.


Returns:
The function returning the override animation or `None` if no such animation
override is defined.


Return type:
Optional\[Callable\[\[[Mobject](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), …], [Animation](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")]]


apply\_complex\_function(*function*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.apply_complex_function)[¶](#manim.mobject.mobject.Mobject.apply_complex_function "Link to this definition")
Applies a complex function to a [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
The x and y Point3Ds correspond to the real and imaginary parts respectively.


Example


Example: ApplyFuncExample [¶](#applyfuncexample)


```
from manim import *

class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)

```


```

class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)


```

Parameters:
**function** (*Callable**\[**\[**complex**]**,* *complex**]*)


Return type:
Self


apply\_to\_family(*func*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.apply_to_family)[¶](#manim.mobject.mobject.Mobject.apply_to_family "Link to this definition")
Apply a function to `self` and every submobject with points recursively.


Parameters:
**func** (*Callable**\[**\[*[*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *None**]*) – The function to apply to each mobject. `func` gets passed the respective
(sub)mobject as parameter.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


`family_members_with_points()`


arrange(*direction\=array(\[1\., 0\., 0\.])*, *buff\=0\.25*, *center\=True*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.arrange)[¶](#manim.mobject.mobject.Mobject.arrange "Link to this definition")
Sorts [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to each other on screen.


Examples


Example: Example [¶](#example)

![../_images/Example-1.png](../_images/Example-1.png)

```
from manim import *

class Example(Scene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)

```


```

class Example(Scene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)


```

Parameters:
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **buff** (*float*)
* **center** (*bool*)


Return type:
Self


arrange\_in\_grid(*rows\=None*, *cols\=None*, *buff\=0\.25*, *cell\_alignment\=array(\[0\., 0\., 0\.])*, *row\_alignments\=None*, *col\_alignments\=None*, *row\_heights\=None*, *col\_widths\=None*, *flow\_order\='rd'*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.arrange_in_grid)[¶](#manim.mobject.mobject.Mobject.arrange_in_grid "Link to this definition")
Arrange submobjects in a grid.


Parameters:
* **rows** (*int* *\|* *None*) – The number of rows in the grid.
* **cols** (*int* *\|* *None*) – The number of columns in the grid.
* **buff** (*float* *\|* *tuple**\[**float**,* *float**]*) – The gap between grid cells. To specify a different buffer in the horizontal and
vertical directions, a tuple of two values can be given \- `(row, col)`.
* **cell\_alignment** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The way each submobject is aligned in its grid cell.
* **row\_alignments** (*str* *\|* *None*) – The vertical alignment for each row (top to bottom). Accepts the following characters: `"u"` \-
up, `"c"` \- center, `"d"` \- down.
* **col\_alignments** (*str* *\|* *None*) – The horizontal alignment for each column (left to right). Accepts the following characters `"l"` \- left,
`"c"` \- center, `"r"` \- right.
* **row\_heights** (*Iterable**\[**float* *\|* *None**]* *\|* *None*) – Defines a list of heights for certain rows (top to bottom). If the list contains
`None`, the corresponding row will fit its height automatically based
on the highest element in that row.
* **col\_widths** (*Iterable**\[**float* *\|* *None**]* *\|* *None*) – Defines a list of widths for certain columns (left to right). If the list contains `None`, the
corresponding column will fit its width automatically based on the widest element in that column.
* **flow\_order** (*str*) – The order in which submobjects fill the grid. Can be one of the following values:
“rd”, “dr”, “ld”, “dl”, “ru”, “ur”, “lu”, “ul”. (“rd” \-\> fill rightwards then downwards)


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Raises:
* **ValueError** – If `rows` and `cols` are too small to fit all submobjects.
* **ValueError** – If `cols`, `col_alignments` and `col_widths` or `rows`,
 `row_alignments` and `row_heights` have mismatching sizes.


Notes


If only one of `cols` and `rows` is set implicitly, the other one will be chosen big
enough to fit all submobjects. If neither is set, they will be chosen to be about the same,
tending towards `cols` \> `rows` (simply because videos are wider than they are high).


If both `cell_alignment` and `row_alignments` / `col_alignments` are
defined, the latter has higher priority.


Examples


Example: ExampleBoxes [¶](#exampleboxes)

![../_images/ExampleBoxes-1.png](../_images/ExampleBoxes-1.png)

```
from manim import *

class ExampleBoxes(Scene):
    def construct(self):
        boxes=VGroup(*[Square() for s in range(0,6)])
        boxes.arrange_in_grid(rows=2, buff=0.1)
        self.add(boxes)

```


```

class ExampleBoxes(Scene):
    def construct(self):
        boxes=VGroup(*[Square() for s in range(0,6)])
        boxes.arrange_in_grid(rows=2, buff=0.1)
        self.add(boxes)


```

Example: ArrangeInGrid [¶](#arrangeingrid)

![../_images/ArrangeInGrid-1.png](../_images/ArrangeInGrid-1.png)

```
from manim import *

class ArrangeInGrid(Scene):
    def construct(self):
        boxes = VGroup(*[
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))
            for i in range(24)
        ])
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr"
        )

```


```

class ArrangeInGrid(Scene):
    def construct(self):
        boxes = VGroup(*[
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))
            for i in range(24)
        ])
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr"
        )


```


arrange\_submobjects(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.arrange_submobjects)[¶](#manim.mobject.mobject.Mobject.arrange_submobjects "Link to this definition")
Arrange the position of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") with a small buffer.


Examples


Example: ArrangeSumobjectsExample [¶](#arrangesumobjectsexample)

![../_images/ArrangeSumobjectsExample-1.png](../_images/ArrangeSumobjectsExample-1.png)

```
from manim import *

class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)

```


```

class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)


```

Return type:
Self


become(*mobject*, *match\_height\=False*, *match\_width\=False*, *match\_depth\=False*, *match\_center\=False*, *stretch\=False*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.become)[¶](#manim.mobject.mobject.Mobject.become "Link to this definition")
Edit points, colors and submobjects to be identical
to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Note


If both match\_height and match\_width are `True` then the transformed [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")
will match the height first and then the width.


Parameters:
* **match\_height** (*bool*) – Whether or not to preserve the height of the original
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **match\_width** (*bool*) – Whether or not to preserve the width of the original
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **match\_depth** (*bool*) – Whether or not to preserve the depth of the original
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **match\_center** (*bool*) – Whether or not to preserve the center of the original
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **stretch** (*bool*) – Whether or not to stretch the target mobject to match the
the proportions of the original [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


Examples


Example: BecomeScene [¶](#becomescene)


```
from manim import *

class BecomeScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)

```


```

class BecomeScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)


```
The following examples illustrate how mobject measurements
change when using the `match_...` and `stretch` arguments.
We start with a rectangle that is 2 units high and 4 units wide,
which we want to turn into a circle of radius 3:


```
>>> from manim import Rectangle, Circle
>>> import numpy as np
>>> rect = Rectangle(height=2, width=4)
>>> circ = Circle(radius=3)

```


With `stretch=True`, the target circle is deformed to match
the proportions of the rectangle, which results in the target
mobject being an ellipse with height 2 and width 4\. We can
check that the resulting points satisfy the ellipse equation
\\(x^2/a^2 \+ y^2/b^2 \= 1\\) with \\(a \= 4/2\\) and \\(b \= 2/2\\)
being the semi\-axes:


```
>>> result = rect.copy().become(circ, stretch=True)
>>> result.height, result.width
(2.0, 4.0)
>>> ellipse_points = np.array(result.get_anchors())
>>> ellipse_eq = np.sum(ellipse_points**2 * [1/4, 1, 0], axis=1)
>>> np.allclose(ellipse_eq, 1)
True

```


With `match_height=True` and `match_width=True` the circle is
scaled such that the height or the width of the rectangle will
be preserved, respectively.
The points of the resulting mobject satisfy the circle equation
\\(x^2 \+ y^2 \= r^2\\) for the corresponding radius \\(r\\):


```
>>> result = rect.copy().become(circ, match_height=True)
>>> result.height, result.width
(2.0, 2.0)
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 1)
True
>>> result = rect.copy().become(circ, match_width=True)
>>> result.height, result.width
(4.0, 4.0)
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 2**2)
True

```


With `match_center=True`, the resulting mobject is moved such that
its center is the same as the center of the original mobject:


```
>>> rect = rect.shift(np.array([0, 1, 0]))
>>> np.allclose(rect.get_center(), circ.get_center())
False
>>> result = rect.copy().become(circ, match_center=True)
>>> np.allclose(rect.get_center(), result.get_center())
True

```


center()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.center)[¶](#manim.mobject.mobject.Mobject.center "Link to this definition")
Moves the center of the mobject to the center of the scene.


Returns:
The centered mobject.


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


clear\_updaters(*recursive\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.clear_updaters)[¶](#manim.mobject.mobject.Mobject.clear_updaters "Link to this definition")
Remove every updater.


Parameters:
**recursive** (*bool*) – Whether to recursively call `clear_updaters` on all submobjects.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`remove_updater()`](#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater"), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")


copy()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.copy)[¶](#manim.mobject.mobject.Mobject.copy "Link to this definition")
Create and return an identical copy of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") including all
[`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").


Returns:
The copy.


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Note


The clone is initially not visible in the Scene, even if the original was.


*property* depth*: float*[¶](#manim.mobject.mobject.Mobject.depth "Link to this definition")
The depth of the mobject.


Return type:
`float`


See also


[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")


flip(*axis\=array(\[0\., 1\., 0\.])*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.flip)[¶](#manim.mobject.mobject.Mobject.flip "Link to this definition")
Flips/Mirrors an mobject about its center.


Examples


Example: FlipExample [¶](#flipexample)

![../_images/FlipExample-1.png](../_images/FlipExample-1.png)

```
from manim import *

class FlipExample(Scene):
    def construct(self):
        s= Line(LEFT, RIGHT+UP).shift(4*LEFT)
        self.add(s)
        s2= s.copy().flip()
        self.add(s2)

```


```

class FlipExample(Scene):
    def construct(self):
        s= Line(LEFT, RIGHT+UP).shift(4*LEFT)
        self.add(s)
        s2= s.copy().flip()
        self.add(s2)


```

Parameters:
**axis** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


generate\_points()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.generate_points)[¶](#manim.mobject.mobject.Mobject.generate_points "Link to this definition")
Initializes [`points`](#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") and therefore the shape.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.


Return type:
None


get\_all\_points()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_all_points)[¶](#manim.mobject.mobject.Mobject.get_all_points "Link to this definition")
Return all points from this mobject and all submobjects.


May contain duplicates; the order is in a depth\-first (pre\-order)
traversal of the submobjects.


Return type:
[*Point3D\_Array*](manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")


get\_bottom()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_bottom)[¶](#manim.mobject.mobject.Mobject.get_bottom "Link to this definition")
Get bottom Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_center()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_center)[¶](#manim.mobject.mobject.Mobject.get_center "Link to this definition")
Get center Point3Ds


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_color()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_color)[¶](#manim.mobject.mobject.Mobject.get_color "Link to this definition")
Returns the color of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Examples


```
>>> from manim import Square, RED
>>> Square(color=RED).get_color() == RED
True

```


Return type:
[*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")


get\_coord(*dim*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_coord)[¶](#manim.mobject.mobject.Mobject.get_coord "Link to this definition")
Meant to generalize `get_x`, `get_y` and `get_z`


Parameters:
* **dim** (*int*)
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


get\_corner(*direction*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_corner)[¶](#manim.mobject.mobject.Mobject.get_corner "Link to this definition")
Get corner Point3Ds for certain direction.


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_critical\_point(*direction*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_critical_point)[¶](#manim.mobject.mobject.Mobject.get_critical_point "Link to this definition")
Picture a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). Such a box has
9 ‘critical points’: 4 corners, 4 edge center, the
center. This returns one of them, along the given direction.


```
sample = Arc(start_angle=PI/7, angle = PI/5)

# These are all equivalent
max_y_1 = sample.get_top()[1]
max_y_2 = sample.get_critical_point(UP)[1]
max_y_3 = sample.get_extremum_along_dim(dim=1, key=1)

```


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_edge\_center(*direction*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_edge_center)[¶](#manim.mobject.mobject.Mobject.get_edge_center "Link to this definition")
Get edge Point3Ds for certain direction.


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_end()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_end)[¶](#manim.mobject.mobject.Mobject.get_end "Link to this definition")
Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends.


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_left()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_left)[¶](#manim.mobject.mobject.Mobject.get_left "Link to this definition")
Get left Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_merged\_array(*array\_attr*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_merged_array)[¶](#manim.mobject.mobject.Mobject.get_merged_array "Link to this definition")
Return all of a given attribute from this mobject and all submobjects.


May contain duplicates; the order is in a depth\-first (pre\-order)
traversal of the submobjects.


Parameters:
**array\_attr** (*str*)


Return type:
*ndarray*


get\_midpoint()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_midpoint)[¶](#manim.mobject.mobject.Mobject.get_midpoint "Link to this definition")
Get Point3Ds of the middle of the path that forms the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Examples


Example: AngleMidPoint [¶](#anglemidpoint)

![../_images/AngleMidPoint-1.png](../_images/AngleMidPoint-1.png)

```
from manim import *

class AngleMidPoint(Scene):
    def construct(self):
        line1 = Line(ORIGIN, 2*RIGHT)
        line2 = Line(ORIGIN, 2*RIGHT).rotate_about_origin(80*DEGREES)

        a = Angle(line1, line2, radius=1.5, other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)

        self.add(line1, line2, a, d)
        self.wait()

```


```

class AngleMidPoint(Scene):
    def construct(self):
        line1 = Line(ORIGIN, 2*RIGHT)
        line2 = Line(ORIGIN, 2*RIGHT).rotate_about_origin(80*DEGREES)

        a = Angle(line1, line2, radius=1.5, other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)

        self.add(line1, line2, a, d)
        self.wait()


```

Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


*static* get\_mobject\_type\_class()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_mobject_type_class)[¶](#manim.mobject.mobject.Mobject.get_mobject_type_class "Link to this definition")
Return the base class of this mobject type.


Return type:
type\[[*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


get\_nadir()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_nadir)[¶](#manim.mobject.mobject.Mobject.get_nadir "Link to this definition")
Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_point\_mobject(*center\=None*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_point_mobject)[¶](#manim.mobject.mobject.Mobject.get_point_mobject "Link to this definition")
The simplest [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self.
Should by a point of the appropriate type


get\_right()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_right)[¶](#manim.mobject.mobject.Mobject.get_right "Link to this definition")
Get right Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_start()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_start)[¶](#manim.mobject.mobject.Mobject.get_start "Link to this definition")
Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts.


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_start\_and\_end()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_start_and_end)[¶](#manim.mobject.mobject.Mobject.get_start_and_end "Link to this definition")
Returns starting and ending point of a stroke as a `tuple`.


Return type:
tuple\[[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"), [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")]


get\_time\_based\_updaters()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_time_based_updaters)[¶](#manim.mobject.mobject.Mobject.get_time_based_updaters "Link to this definition")
Return all updaters using the `dt` parameter.


The updaters use this parameter as the input for difference in time.


Returns:
The list of time based updaters.


Return type:
List\[`Callable`]


See also


[`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters"), [`has_time_based_updater()`](#manim.mobject.mobject.Mobject.has_time_based_updater "manim.mobject.mobject.Mobject.has_time_based_updater")


get\_top()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_top)[¶](#manim.mobject.mobject.Mobject.get_top "Link to this definition")
Get top Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


get\_updaters()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_updaters)[¶](#manim.mobject.mobject.Mobject.get_updaters "Link to this definition")
Return all updaters.


Returns:
The list of updaters.


Return type:
List\[`Callable`]


See also


[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_time_based_updaters()`](#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters")


get\_x(*direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_x)[¶](#manim.mobject.mobject.Mobject.get_x "Link to this definition")
Returns x Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*ManimFloat*](manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat")


get\_y(*direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_y)[¶](#manim.mobject.mobject.Mobject.get_y "Link to this definition")
Returns y Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*ManimFloat*](manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat")


get\_z(*direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_z)[¶](#manim.mobject.mobject.Mobject.get_z "Link to this definition")
Returns z Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`


Parameters:
**direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
[*ManimFloat*](manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat")


get\_zenith()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.get_zenith)[¶](#manim.mobject.mobject.Mobject.get_zenith "Link to this definition")
Get zenith Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Return type:
[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")


has\_no\_points()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.has_no_points)[¶](#manim.mobject.mobject.Mobject.has_no_points "Link to this definition")
Check if [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *does not* contains points.


Return type:
bool


has\_points()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.has_points)[¶](#manim.mobject.mobject.Mobject.has_points "Link to this definition")
Check if [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") contains points.


Return type:
bool


has\_time\_based\_updater()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.has_time_based_updater)[¶](#manim.mobject.mobject.Mobject.has_time_based_updater "Link to this definition")
Test if `self` has a time based updater.


Returns:
`True` if at least one updater uses the `dt` parameter, `False`
otherwise.


Return type:
`bool`


See also


[`get_time_based_updaters()`](#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters")


*property* height*: float*[¶](#manim.mobject.mobject.Mobject.height "Link to this definition")
The height of the mobject.


Return type:
`float`


Examples


Example: HeightExample [¶](#heightexample)


```
from manim import *

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()

```


```

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()


```

See also


[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")


init\_colors()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.init_colors)[¶](#manim.mobject.mobject.Mobject.init_colors "Link to this definition")
Initializes the colors.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.


Return type:
None


insert(*index*, *mobject*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.insert)[¶](#manim.mobject.mobject.Mobject.insert "Link to this definition")
Inserts a mobject at a specific position into self.submobjects


Effectively just calls `self.submobjects.insert(index, mobject)`,
where `self.submobjects` is a list.


Highly adapted from `Mobject.add`.


Parameters:
* **index** (*int*) – The index at which
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be inserted.


Return type:
None


interpolate(*mobject1*, *mobject2*, *alpha*, *path\_func\=\<function interpolate\>*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.interpolate)[¶](#manim.mobject.mobject.Mobject.interpolate "Link to this definition")
Turns this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") into an interpolation between `mobject1`
and `mobject2`.


Examples


Example: DotInterpolation [¶](#dotinterpolation)

![../_images/DotInterpolation-1.png](../_images/DotInterpolation-1.png)

```
from manim import *

class DotInterpolation(Scene):
    def construct(self):
        dotR = Dot(color=DARK_GREY)
        dotR.shift(2 * RIGHT)
        dotL = Dot(color=WHITE)
        dotL.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)

```


```

class DotInterpolation(Scene):
    def construct(self):
        dotR = Dot(color=DARK_GREY)
        dotR.shift(2 * RIGHT)
        dotL = Dot(color=WHITE)
        dotL.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)


```

Parameters:
* **mobject1** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **mobject2** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **alpha** (*float*)
* **path\_func** ([*PathFuncType*](manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType"))


Return type:
Self


invert(*recursive\=False*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.invert)[¶](#manim.mobject.mobject.Mobject.invert "Link to this definition")
Inverts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").


Parameters:
**recursive** (*bool*) – If `True`, all submobject lists of this mobject’s family are inverted.


Return type:
None


Examples


Example: InvertSumobjectsExample [¶](#invertsumobjectsexample)


```
from manim import *

class InvertSumobjectsExample(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))

```


```

class InvertSumobjectsExample(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))


```


length\_over\_dim(*dim*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.length_over_dim)[¶](#manim.mobject.mobject.Mobject.length_over_dim "Link to this definition")
Measure the length of an [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction.


Parameters:
**dim** (*int*)


Return type:
float


match\_color(*mobject*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_color)[¶](#manim.mobject.mobject.Mobject.match_color "Link to this definition")
Match the color with the color of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_coord(*mobject*, *dim*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_coord)[¶](#manim.mobject.mobject.Mobject.match_coord "Link to this definition")
Match the Point3Ds with the Point3Ds of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **dim** (*int*)
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


match\_depth(*mobject*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_depth)[¶](#manim.mobject.mobject.Mobject.match_depth "Link to this definition")
Match the depth with the depth of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_dim\_size(*mobject*, *dim*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_dim_size)[¶](#manim.mobject.mobject.Mobject.match_dim_size "Link to this definition")
Match the specified dimension with the dimension of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **dim** (*int*)


Return type:
Self


match\_height(*mobject*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_height)[¶](#manim.mobject.mobject.Mobject.match_height "Link to this definition")
Match the height with the height of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_points(*mobject*, *copy\_submobjects\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_points)[¶](#manim.mobject.mobject.Mobject.match_points "Link to this definition")
Edit points, positions, and submobjects to be identical
to another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), while keeping the style unchanged.


Examples


Example: MatchPointsScene [¶](#matchpointsscene)


```
from manim import *

class MatchPointsScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)

```


```

class MatchPointsScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)


```

Parameters:
* **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **copy\_submobjects** (*bool*)


Return type:
Self


match\_updaters(*mobject*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_updaters)[¶](#manim.mobject.mobject.Mobject.match_updaters "Link to this definition")
Match the updaters of the given mobject.


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject whose updaters get matched.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Note


All updaters from submobjects are removed, but only updaters of the given
mobject are matched, not those of it’s submobjects.


See also


[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`clear_updaters()`](#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters")


match\_width(*mobject*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_width)[¶](#manim.mobject.mobject.Mobject.match_width "Link to this definition")
Match the width with the width of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_x(*mobject*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_x)[¶](#manim.mobject.mobject.Mobject.match_x "Link to this definition")
Match x coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_y(*mobject*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_y)[¶](#manim.mobject.mobject.Mobject.match_y "Link to this definition")
Match y coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


match\_z(*mobject*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.match_z)[¶](#manim.mobject.mobject.Mobject.match_z "Link to this definition")
Match z coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:
Self


move\_to(*point\_or\_mobject*, *aligned\_edge\=array(\[0\., 0\., 0\.])*, *coor\_mask\=array(\[1, 1, 1])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.move_to)[¶](#manim.mobject.mobject.Mobject.move_to "Link to this definition")
Move center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to certain Point3D.


Parameters:
* **point\_or\_mobject** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") *\|* [*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
* **aligned\_edge** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **coor\_mask** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


next\_to(*mobject\_or\_point*, *direction\=array(\[1\., 0\., 0\.])*, *buff\=0\.25*, *aligned\_edge\=array(\[0\., 0\., 0\.])*, *submobject\_to\_align\=None*, *index\_of\_submobject\_to\_align\=None*, *coor\_mask\=array(\[1, 1, 1])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.next_to)[¶](#manim.mobject.mobject.Mobject.next_to "Link to this definition")
Move this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to another’s [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or Point3D.


Examples


Example: GeometricShapes [¶](#geometricshapes)

![../_images/GeometricShapes-1.png](../_images/GeometricShapes-1.png)

```
from manim import *

class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)

```


```

class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)


```

Parameters:
* **mobject\_or\_point** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *\|* [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **buff** (*float*)
* **aligned\_edge** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **submobject\_to\_align** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *\|* *None*)
* **index\_of\_submobject\_to\_align** (*int* *\|* *None*)
* **coor\_mask** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


null\_point\_align(*mobject*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.null_point_align)[¶](#manim.mobject.mobject.Mobject.null_point_align "Link to this definition")
If a [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") with points is being aligned to
one without, treat both as groups, and push
the one with points into its own submobjects
list.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
**mobject** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


reduce\_across\_dimension(*reduce\_func*, *dim*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.reduce_across_dimension)[¶](#manim.mobject.mobject.Mobject.reduce_across_dimension "Link to this definition")
Find the min or max value from a dimension across all points in this and submobjects.


Parameters:
* **reduce\_func** (*Callable*)
* **dim** (*int*)


remove(*\*mobjects*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.remove)[¶](#manim.mobject.mobject.Mobject.remove "Link to this definition")
Remove [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").


The mobjects are removed from [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"), if they exist.


Subclasses of mobject may implement `-` and `-=` dunder methods.


Parameters:
**mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to remove.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`add()`](#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add")


remove\_updater(*update\_function*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.remove_updater)[¶](#manim.mobject.mobject.Mobject.remove_updater "Link to this definition")
Remove an updater.


If the same updater is applied multiple times, every instance gets removed.


Parameters:
**update\_function** ([*Updater*](manim.mobject.mobject.html#manim.mobject.mobject.Updater "manim.mobject.mobject.Updater")) – The update function to be removed.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`clear_updaters()`](#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters"), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")


repeat(*count*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.repeat)[¶](#manim.mobject.mobject.Mobject.repeat "Link to this definition")
This can make transition animations nicer


Parameters:
**count** (*int*)


Return type:
Self


reset\_points()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.reset_points)[¶](#manim.mobject.mobject.Mobject.reset_points "Link to this definition")
Sets [`points`](#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") to be an empty array.


Return type:
None


restore()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.restore)[¶](#manim.mobject.mobject.Mobject.restore "Link to this definition")
Restores the state that was previously saved with [`save_state()`](#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state").


Return type:
Self


resume\_updating(*recursive\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.resume_updating)[¶](#manim.mobject.mobject.Mobject.resume_updating "Link to this definition")
Enable updating from updaters and animations.


Parameters:
**recursive** (*bool*) – Whether to recursively enable updating on all submobjects.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`suspend_updating()`](#manim.mobject.mobject.Mobject.suspend_updating "manim.mobject.mobject.Mobject.suspend_updating"), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater")


rotate(*angle*, *axis\=array(\[0\., 0\., 1\.])*, *about\_point\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.rotate)[¶](#manim.mobject.mobject.Mobject.rotate "Link to this definition")
Rotates the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about a certain point.


Parameters:
* **angle** (*float*)
* **axis** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **about\_point** ([*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") *\|* *None*)


Return type:
Self


rotate\_about\_origin(*angle*, *axis\=array(\[0\., 0\., 1\.])*, *axes\=\[]*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.rotate_about_origin)[¶](#manim.mobject.mobject.Mobject.rotate_about_origin "Link to this definition")
Rotates the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about the ORIGIN, which is at \[0,0,0].


Parameters:
* **angle** (*float*)
* **axis** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


save\_image(*name\=None*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.save_image)[¶](#manim.mobject.mobject.Mobject.save_image "Link to this definition")
Saves an image of only this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") at its position to a png
file.


Parameters:
**name** (*str* *\|* *None*)


Return type:
None


save\_state()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.save_state)[¶](#manim.mobject.mobject.Mobject.save_state "Link to this definition")
Save the current state (position, color \& size). Can be restored with [`restore()`](#manim.mobject.mobject.Mobject.restore "manim.mobject.mobject.Mobject.restore").


Return type:
Self


scale(*scale\_factor*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.scale)[¶](#manim.mobject.mobject.Mobject.scale "Link to this definition")
Scale the size by a factor.


Default behavior is to scale about the center of the mobject.


Parameters:
* **scale\_factor** (*float*) – The scaling factor \\(\\alpha\\). If \\(0 \< \|\\alpha\| \< 1\\), the mobject
will shrink, and for \\(\|\\alpha\| \> 1\\) it will grow. Furthermore,
if \\(\\alpha \< 0\\), the mobject is also flipped.
* **kwargs** – Additional keyword arguments passed to
`apply_points_function_about_point()`.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Examples


Example: MobjectScaleExample [¶](#mobjectscaleexample)

![../_images/MobjectScaleExample-1.png](../_images/MobjectScaleExample-1.png)

```
from manim import *

class MobjectScaleExample(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)

```


```

class MobjectScaleExample(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)


```

See also


[`move_to()`](#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to")


scale\_to\_fit\_depth(*depth*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_depth)[¶](#manim.mobject.mobject.Mobject.scale_to_fit_depth "Link to this definition")
Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth while keeping width/height proportional.


Parameters:
**depth** (*float*)


Return type:
Self


scale\_to\_fit\_height(*height*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_height)[¶](#manim.mobject.mobject.Mobject.scale_to_fit_height "Link to this definition")
Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height while keeping width/depth proportional.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
**height** (*float*)


Examples


```
>>> from manim import *
>>> sq = Square()
>>> sq.width
2.0
>>> sq.scale_to_fit_height(5)
Square
>>> sq.height
5.0
>>> sq.width
5.0

```


scale\_to\_fit\_width(*width*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_width)[¶](#manim.mobject.mobject.Mobject.scale_to_fit_width "Link to this definition")
Scales the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width while keeping height/depth proportional.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
**width** (*float*)


Examples


```
>>> from manim import *
>>> sq = Square()
>>> sq.height
2.0
>>> sq.scale_to_fit_width(5)
Square
>>> sq.width
5.0
>>> sq.height
5.0

```


set(*\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set)[¶](#manim.mobject.mobject.Mobject.set "Link to this definition")
Sets attributes.


I.e. `my_mobject.set(foo=1)` applies `my_mobject.foo = 1`.


This is a convenience to be used along with [`animate`](#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") to
animate setting attributes.


In addition to this method, there is a compatibility
layer that allows `get_*` and `set_*` methods to
get and set generic attributes. For instance:


```
>>> mob = Mobject()
>>> mob.set_foo(0)
Mobject
>>> mob.get_foo()
0
>>> mob.foo
0

```


This compatibility layer does not interfere with any
`get_*` or `set_*` methods that are explicitly
defined.


Warning


This compatibility layer is for backwards compatibility
and is not guaranteed to stay around. Where applicable,
please prefer getting/setting attributes normally or with
the [`set()`](#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") method.


Parameters:
**\*\*kwargs** – The attributes and corresponding values to set.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Examples


```
>>> mob = Mobject()
>>> mob.set(foo=0)
Mobject
>>> mob.foo
0

```


set\_color(*color\=ManimColor('\#FFFF00')*, *family\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_color)[¶](#manim.mobject.mobject.Mobject.set_color "Link to this definition")
Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color


Parameters:
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
* **family** (*bool*)


Return type:
Self


set\_color\_by\_gradient(*\*colors*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_color_by_gradient)[¶](#manim.mobject.mobject.Mobject.set_color_by_gradient "Link to this definition")

Parameters:
* **colors** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN).
* **ManimColor.parse****(****color****)** (*self.color \=*)
* **self** (*return*)


Return type:
Self


*classmethod* set\_default(*\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_default)[¶](#manim.mobject.mobject.Mobject.set_default "Link to this definition")
Sets the default values of keyword arguments.


If this method is called without any additional keyword
arguments, the original default values of the initialization
method of this class are restored.


Parameters:
**kwargs** – Passing any keyword argument will update the default
values of the keyword arguments of the initialization
function of this class.


Return type:
None


Examples


```
>>> from manim import Square, GREEN
>>> Square.set_default(color=GREEN, fill_opacity=0.25)
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#83C167'), 0.25)
>>> Square.set_default()
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#FFFFFF'), 0.0)

```


Example: ChangedDefaultTextcolor [¶](#changeddefaulttextcolor)

![../_images/ChangedDefaultTextcolor-1.png](../_images/ChangedDefaultTextcolor-1.png)

```
from manim import *

config.background_color = WHITE

class ChangedDefaultTextcolor(Scene):
    def construct(self):
        Text.set_default(color=BLACK)
        self.add(Text("Changing default values is easy!"))

        # we revert the colour back to the default to prevent a bug in the docs.
        Text.set_default(color=WHITE)

```


```

config.background_color = WHITE

class ChangedDefaultTextcolor(Scene):
    def construct(self):
        Text.set_default(color=BLACK)
        self.add(Text("Changing default values is easy!"))

        # we revert the colour back to the default to prevent a bug in the docs.
        Text.set_default(color=WHITE)


```


set\_x(*x*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_x)[¶](#manim.mobject.mobject.Mobject.set_x "Link to this definition")
Set x value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`)


Parameters:
* **x** (*float*)
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


set\_y(*y*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_y)[¶](#manim.mobject.mobject.Mobject.set_y "Link to this definition")
Set y value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`)


Parameters:
* **y** (*float*)
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


set\_z(*z*, *direction\=array(\[0\., 0\., 0\.])*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_z)[¶](#manim.mobject.mobject.Mobject.set_z "Link to this definition")
Set z value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (`int` or `float`)


Parameters:
* **z** (*float*)
* **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:
Self


set\_z\_index(*z\_index\_value*, *family\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_z_index)[¶](#manim.mobject.mobject.Mobject.set_z_index "Link to this definition")
Sets the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")’s `z_index` to the value specified in z\_index\_value.


Parameters:
* **z\_index\_value** (*float*) – The new value of `z_index` set.
* **family** (*bool*) – If `True`, the `z_index` value of all submobjects is also set.


Returns:
The Mobject itself, after `z_index` is set. For chaining purposes. (Returns self.)


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Examples


Example: SetZIndex [¶](#setzindex)

![../_images/SetZIndex-1.png](../_images/SetZIndex-1.png)

```
from manim import *

class SetZIndex(Scene):
    def construct(self):
        text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1', color = PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1) # z_index = 0

        # Displaying order is now defined by z_index values
        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)

```


```

class SetZIndex(Scene):
    def construct(self):
        text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1', color = PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1) # z_index = 0

        # Displaying order is now defined by z_index values
        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)


```


set\_z\_index\_by\_z\_Point3D()[\[source]](../_modules/manim/mobject/mobject.html#Mobject.set_z_index_by_z_Point3D)[¶](#manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D "Link to this definition")
Sets the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")’s z Point3D to the value of `z_index`.


Returns:
The Mobject itself, after `z_index` is set. (Returns self.)


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


shift(*\*vectors*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.shift)[¶](#manim.mobject.mobject.Mobject.shift "Link to this definition")
Shift by the given vectors.


Parameters:
**vectors** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – Vectors to shift by. If multiple vectors are given, they are added
together.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`move_to()`](#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to")


shuffle(*recursive\=False*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.shuffle)[¶](#manim.mobject.mobject.Mobject.shuffle "Link to this definition")
Shuffles the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").


Parameters:
**recursive** (*bool*)


Return type:
None


shuffle\_submobjects(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.shuffle_submobjects)[¶](#manim.mobject.mobject.Mobject.shuffle_submobjects "Link to this definition")
Shuffles the order of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects")


Examples


Example: ShuffleSubmobjectsExample [¶](#shufflesubmobjectsexample)


```
from manim import *

class ShuffleSubmobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2= s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))

```


```

class ShuffleSubmobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2= s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))


```

Return type:
None


sort(*point\_to\_num\_func\=\<function Mobject.\<lambda\>\>*, *submob\_func\=None*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.sort)[¶](#manim.mobject.mobject.Mobject.sort "Link to this definition")
Sorts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") by a function defined by `submob_func`.


Parameters:
* **point\_to\_num\_func** (*Callable**\[**\[*[*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")*]**,* [*ManimInt*](manim.typing.html#manim.typing.ManimInt "manim.typing.ManimInt")*]*)
* **submob\_func** (*Callable**\[**\[*[*Mobject*](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* [*ManimInt*](manim.typing.html#manim.typing.ManimInt "manim.typing.ManimInt")*]* *\|* *None*)


Return type:
Self


sort\_submobjects(*\*args*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.sort_submobjects)[¶](#manim.mobject.mobject.Mobject.sort_submobjects "Link to this definition")
Sort the [`submobjects`](#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects")


Return type:
Self


stretch\_to\_fit\_depth(*depth*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_depth)[¶](#manim.mobject.mobject.Mobject.stretch_to_fit_depth "Link to this definition")
Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth, not keeping width/height proportional.


Parameters:
**depth** (*float*)


Return type:
Self


stretch\_to\_fit\_height(*height*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_height)[¶](#manim.mobject.mobject.Mobject.stretch_to_fit_height "Link to this definition")
Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height, not keeping width/depth proportional.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
**height** (*float*)


Examples


```
>>> from manim import *
>>> sq = Square()
>>> sq.width
2.0
>>> sq.stretch_to_fit_height(5)
Square
>>> sq.height
5.0
>>> sq.width
2.0

```


stretch\_to\_fit\_width(*width*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_width)[¶](#manim.mobject.mobject.Mobject.stretch_to_fit_width "Link to this definition")
Stretches the [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width, not keeping height/depth proportional.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
**width** (*float*)


Examples


```
>>> from manim import *
>>> sq = Square()
>>> sq.height
2.0
>>> sq.stretch_to_fit_width(5)
Square
>>> sq.width
5.0
>>> sq.height
2.0

```


suspend\_updating(*recursive\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.suspend_updating)[¶](#manim.mobject.mobject.Mobject.suspend_updating "Link to this definition")
Disable updating from updaters and animations.


Parameters:
**recursive** (*bool*) – Whether to recursively suspend updating on all submobjects.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`resume_updating()`](#manim.mobject.mobject.Mobject.resume_updating "manim.mobject.mobject.Mobject.resume_updating"), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater")


to\_corner(*corner\=array(\[\-1\., \-1\., 0\.])*, *buff\=0\.5*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.to_corner)[¶](#manim.mobject.mobject.Mobject.to_corner "Link to this definition")
Moves this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given corner of the screen.


Returns:
The newly positioned mobject.


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
* **corner** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **buff** (*float*)


Examples


Example: ToCornerExample [¶](#tocornerexample)

![../_images/ToCornerExample-1.png](../_images/ToCornerExample-1.png)

```
from manim import *

class ToCornerExample(Scene):
    def construct(self):
        c = Circle()
        c.to_corner(UR)
        t = Tex("To the corner!")
        t2 = MathTex("x^3").shift(DOWN)
        self.add(c,t,t2)
        t.to_corner(DL, buff=0)
        t2.to_corner(UL, buff=1.5)

```


```

class ToCornerExample(Scene):
    def construct(self):
        c = Circle()
        c.to_corner(UR)
        t = Tex("To the corner!")
        t2 = MathTex("x^3").shift(DOWN)
        self.add(c,t,t2)
        t.to_corner(DL, buff=0)
        t2.to_corner(UL, buff=1.5)


```


to\_edge(*edge\=array(\[\-1\., 0\., 0\.])*, *buff\=0\.5*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.to_edge)[¶](#manim.mobject.mobject.Mobject.to_edge "Link to this definition")
Moves this [`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given edge of the screen,
without affecting its position in the other dimension.


Returns:
The newly positioned mobject.


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


Parameters:
* **edge** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
* **buff** (*float*)


Examples


Example: ToEdgeExample [¶](#toedgeexample)

![../_images/ToEdgeExample-1.png](../_images/ToEdgeExample-1.png)

```
from manim import *

class ToEdgeExample(Scene):
    def construct(self):
        tex_top = Tex("I am at the top!")
        tex_top.to_edge(UP)
        tex_side = Tex("I am moving to the side!")
        c = Circle().shift(2*DOWN)
        self.add(tex_top, tex_side)
        tex_side.to_edge(LEFT)
        c.to_edge(RIGHT, buff=0)

```


```

class ToEdgeExample(Scene):
    def construct(self):
        tex_top = Tex("I am at the top!")
        tex_top.to_edge(UP)
        tex_side = Tex("I am moving to the side!")
        c = Circle().shift(2*DOWN)
        self.add(tex_top, tex_side)
        tex_side.to_edge(LEFT)
        c.to_edge(RIGHT, buff=0)


```


update(*dt\=0*, *recursive\=True*)[\[source]](../_modules/manim/mobject/mobject.html#Mobject.update)[¶](#manim.mobject.mobject.Mobject.update "Link to this definition")
Apply all updaters.


Does nothing if updating is suspended.


Parameters:
* **dt** (*float*) – The parameter `dt` to pass to the update functions. Usually this is the
time in seconds since the last call of `update`.
* **recursive** (*bool*) – Whether to recursively update all submobjects.


Returns:
`self`


Return type:
[`Mobject`](#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")


See also


[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")


*property* width*: float*[¶](#manim.mobject.mobject.Mobject.width "Link to this definition")
The width of the mobject.


Return type:
`float`


Examples


Example: WidthExample [¶](#widthexample)


```
from manim import *

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()

```


```

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()


```

See also


[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")



---

# MathTex


# MathTex[¶](#mathtex "Link to this heading")


Qualified name: `manim.mobject.text.tex\_mobject.MathTex`


*class* MathTex(*\*tex\_strings*, *arg\_separator\=' '*, *substrings\_to\_isolate\=None*, *tex\_to\_color\_map\=None*, *tex\_environment\='align\*'*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex)[¶](#manim.mobject.text.tex_mobject.MathTex "Link to this definition")
Bases: [`SingleStringMathTex`](manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex")


A string compiled with LaTeX in math mode.


Examples


Example: Formula [¶](#formula)

![../_images/Formula-1.png](../_images/Formula-1.png)

```
from manim import *

class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)

```


```

class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)


```
Tests


Check that creating a [`MathTex`](#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") works:


```
>>> MathTex('a^2 + b^2 = c^2') 
MathTex('a^2 + b^2 = c^2')

```


Check that double brace group splitting works correctly:


```
>>> t1 = MathTex('{{ a }} + {{ b }} = {{ c }}') 
>>> len(t1.submobjects) 
5
>>> t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}") 
>>> len(t2.submobjects) 
1

```


Methods


| `get_part_by_tex` |  |
| --- | --- |
| `get_parts_by_tex` |  |
| `index_of_part` |  |
| `index_of_part_by_tex` |  |
| `set_color_by_tex` |  |
| `set_color_by_tex_to_color_map` |  |
| [`set_opacity_by_tex`](#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex") | Sets the opacity of the tex specified. |
| `sort_alphabetically` |  |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `font_size` | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


Parameters:
* **arg\_separator** (*str*)
* **substrings\_to\_isolate** (*Iterable**\[**str**]* *\|* *None*)
* **tex\_to\_color\_map** (*dict**\[**str**,* [*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")*]*)
* **tex\_environment** (*str*)


\_break\_up\_by\_substrings()[\[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex._break_up_by_substrings)[¶](#manim.mobject.text.tex_mobject.MathTex._break_up_by_substrings "Link to this definition")
Reorganize existing submobjects one layer
deeper based on the structure of tex\_strings (as a list
of tex\_strings)


\_original\_\_init\_\_(*\*tex\_strings*, *arg\_separator\=' '*, *substrings\_to\_isolate\=None*, *tex\_to\_color\_map\=None*, *tex\_environment\='align\*'*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.MathTex._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **arg\_separator** (*str*)
* **substrings\_to\_isolate** (*Iterable**\[**str**]* *\|* *None*)
* **tex\_to\_color\_map** (*dict**\[**str**,* [*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")*]*)
* **tex\_environment** (*str*)


set\_opacity\_by\_tex(*tex*, *opacity\=0\.5*, *remaining\_opacity\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex.set_opacity_by_tex)[¶](#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "Link to this definition")
Sets the opacity of the tex specified. If ‘remaining\_opacity’ is specified,
then the remaining tex will be set to that opacity.


Parameters:
* **tex** (*str*) – The tex to set the opacity of.
* **opacity** (*float*) – Default 0\.5\. The opacity to set the tex to
* **remaining\_opacity** (*float*) – Default None. The opacity to set the remaining tex to.
If None, then the remaining tex will not be changed



---

# SingleStringMathTex


# SingleStringMathTex[¶](#singlestringmathtex "Link to this heading")


Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`


*class* SingleStringMathTex(*tex\_string*, *stroke\_width\=0*, *should\_center\=True*, *height\=None*, *organize\_left\_to\_right\=False*, *tex\_environment\='align\*'*, *tex\_template\=None*, *font\_size\=48*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex "Link to this definition")
Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")


Elementary building block for rendering text with LaTeX.


Tests


Check that creating a [`SingleStringMathTex`](#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex") object works:


```
>>> SingleStringMathTex('Test') 
SingleStringMathTex('Test')

```


Methods


| `get_tex_string` |  |
| --- | --- |
| [`init_colors`](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors") | Initializes the colors. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| [`font_size`](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "manim.mobject.text.tex_mobject.SingleStringMathTex.font_size") | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


Parameters:
* **tex\_string** (*str*)
* **stroke\_width** (*float*)
* **should\_center** (*bool*)
* **height** (*float* *\|* *None*)
* **organize\_left\_to\_right** (*bool*)
* **tex\_environment** (*str*)
* **tex\_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") *\|* *None*)
* **font\_size** (*float*)


\_original\_\_init\_\_(*tex\_string*, *stroke\_width\=0*, *should\_center\=True*, *height\=None*, *organize\_left\_to\_right\=False*, *tex\_environment\='align\*'*, *tex\_template\=None*, *font\_size\=48*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **tex\_string** (*str*)
* **stroke\_width** (*float*)
* **should\_center** (*bool*)
* **height** (*float* *\|* *None*)
* **organize\_left\_to\_right** (*bool*)
* **tex\_environment** (*str*)
* **tex\_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") *\|* *None*)
* **font\_size** (*float*)


\_remove\_stray\_braces(*tex*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex._remove_stray_braces)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex._remove_stray_braces "Link to this definition")
Makes [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") resilient to unmatched braces.


This is important when the braces in the TeX code are spread over
multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.


*property* font\_size[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "Link to this definition")
The font size of the tex mobject.


init\_colors(*propagate\_colors\=True*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex.init_colors)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "Link to this definition")
Initializes the colors.


Gets called upon creation. This is an empty method that can be implemented by
subclasses.



---

# Tex


# Tex[¶](#tex "Link to this heading")


Qualified name: `manim.mobject.text.tex\_mobject.Tex`


*class* Tex(*\*tex\_strings*, *arg\_separator\=''*, *tex\_environment\='center'*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/text/tex_mobject.html#Tex)[¶](#manim.mobject.text.tex_mobject.Tex "Link to this definition")
Bases: [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")


A string compiled with LaTeX in normal mode.


Tests


Check whether writing a LaTeX string works:


```
>>> Tex('The horse does not eat cucumber salad.') 
Tex('The horse does not eat cucumber salad.')

```


Methods


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `font_size` | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*\*tex\_strings*, *arg\_separator\=''*, *tex\_environment\='center'*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.Tex._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.



---

# ArrowVectorField


# ArrowVectorField[¶](#arrowvectorfield "Link to this heading")


Qualified name: `manim.mobject.vector\_field.ArrowVectorField`


*class* ArrowVectorField(*func, color\=None, color\_scheme\=None, min\_color\_scheme\_value\=0, max\_color\_scheme\_value\=2, colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')], x\_range\=None, y\_range\=None, z\_range\=None, three\_dimensions\=False, length\_func\=\<function ArrowVectorField.\<lambda\>\>, opacity\=1\.0, vector\_config\=None, \*\*kwargs*)[\[source]](../_modules/manim/mobject/vector_field.html#ArrowVectorField)[¶](#manim.mobject.vector_field.ArrowVectorField "Link to this definition")
Bases: [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")


A [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") represented by a set of change vectors.


Vector fields are always based on a function defining the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") at every position.
The values of this functions is displayed as a grid of vectors.
By default the color of each vector is determined by it’s magnitude.
Other color schemes can be used however.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*) – The function defining the rate of change at every position of the vector field.
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of the vector field. If set, position\-specific coloring is disabled.
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.
* **min\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.
* **max\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – The colors defining the color gradient of the vector field.
* **x\_range** (*Sequence**\[**float**]*) – A sequence of x\_min, x\_max, delta\_x
* **y\_range** (*Sequence**\[**float**]*) – A sequence of y\_min, y\_max, delta\_y
* **z\_range** (*Sequence**\[**float**]*) – A sequence of z\_min, z\_max, delta\_z
* **three\_dimensions** (*bool*) – Enables three\_dimensions. Default set to False, automatically turns True if
z\_range is not None.
* **length\_func** (*Callable**\[**\[**float**]**,* *float**]*) – The function determining the displayed size of the vectors. The actual size
of the vector is passed, the returned value will be used as display size for the
vector. By default this is used to cap the displayed size of vectors to reduce the clutter.
* **opacity** (*float*) – The opacity of the arrows.
* **vector\_config** (*dict* *\|* *None*) – Additional arguments to be passed to the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") constructor
* **kwargs** – Additional arguments to be passed to the [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") constructor


Examples


Example: BasicUsage [¶](#basicusage)

![../_images/BasicUsage-1.png](../_images/BasicUsage-1.png)

```
from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))

```


```

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))


```

Example: SizingAndSpacing [¶](#sizingandspacing)


```
from manim import *

class SizingAndSpacing(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()

```


```

class SizingAndSpacing(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()


```

Example: Coloring [¶](#coloring)

![../_images/Coloring-1.png](../_images/Coloring-1.png)

```
from manim import *

class Coloring(Scene):
    def construct(self):
        func = lambda pos: pos - LEFT * 5
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
        max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
        vf = ArrowVectorField(
            func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf, min_radius, max_radius)

```


```

class Coloring(Scene):
    def construct(self):
        func = lambda pos: pos - LEFT * 5
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
        max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
        vf = ArrowVectorField(
            func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf, min_radius, max_radius)


```
Methods


| [`get_vector`](#manim.mobject.vector_field.ArrowVectorField.get_vector "manim.mobject.vector_field.ArrowVectorField.get_vector") | Creates a vector in the vector field. |
| --- | --- |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*func, color\=None, color\_scheme\=None, min\_color\_scheme\_value\=0, max\_color\_scheme\_value\=2, colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')], x\_range\=None, y\_range\=None, z\_range\=None, three\_dimensions\=False, length\_func\=\<function ArrowVectorField.\<lambda\>\>, opacity\=1\.0, vector\_config\=None, \*\*kwargs*)[¶](#manim.mobject.vector_field.ArrowVectorField._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*)
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*)
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*)
* **min\_color\_scheme\_value** (*float*)
* **max\_color\_scheme\_value** (*float*)
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*)
* **x\_range** (*Sequence**\[**float**]*)
* **y\_range** (*Sequence**\[**float**]*)
* **z\_range** (*Sequence**\[**float**]*)
* **three\_dimensions** (*bool*)
* **length\_func** (*Callable**\[**\[**float**]**,* *float**]*)
* **opacity** (*float*)
* **vector\_config** (*dict* *\|* *None*)


get\_vector(*point*)[\[source]](../_modules/manim/mobject/vector_field.html#ArrowVectorField.get_vector)[¶](#manim.mobject.vector_field.ArrowVectorField.get_vector "Link to this definition")
Creates a vector in the vector field.


The created vector is based on the function of the vector field and is
rooted in the given point. Color and length fit the specifications of
this vector field.


Parameters:
**point** (*ndarray*) – The root point of the vector.



---

# StreamLines


# StreamLines[¶](#streamlines "Link to this heading")


Qualified name: `manim.mobject.vector\_field.StreamLines`


*class* StreamLines(*func*, *color\=None*, *color\_scheme\=None*, *min\_color\_scheme\_value\=0*, *max\_color\_scheme\_value\=2*, *colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')]*, *x\_range\=None*, *y\_range\=None*, *z\_range\=None*, *three\_dimensions\=False*, *noise\_factor\=None*, *n\_repeats\=1*, *dt\=0\.05*, *virtual\_time\=3*, *max\_anchors\_per\_line\=100*, *padding\=3*, *stroke\_width\=1*, *opacity\=1*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/vector_field.html#StreamLines)[¶](#manim.mobject.vector_field.StreamLines "Link to this definition")
Bases: [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")


StreamLines represent the flow of a [`VectorField`](manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") using the trace of moving agents.


Vector fields are always based on a function defining the vector at every position.
The values of this functions is displayed by moving many agents along the vector field
and showing their trace.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*) – The function defining the rate of change at every position of the vector field.
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of the vector field. If set, position\-specific coloring is disabled.
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.
* **min\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.
* **max\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – The colors defining the color gradient of the vector field.
* **x\_range** (*Sequence**\[**float**]*) – A sequence of x\_min, x\_max, delta\_x
* **y\_range** (*Sequence**\[**float**]*) – A sequence of y\_min, y\_max, delta\_y
* **z\_range** (*Sequence**\[**float**]*) – A sequence of z\_min, z\_max, delta\_z
* **three\_dimensions** (*bool*) – Enables three\_dimensions. Default set to False, automatically turns True if
z\_range is not None.
* **noise\_factor** (*float* *\|* *None*) – The amount by which the starting position of each agent is altered along each axis. Defaults to `delta_y / 2` if not defined.
* **n\_repeats** – The number of agents generated at each starting point.
* **dt** – The factor by which the distance an agent moves per step is stretched. Lower values result in a better approximation of the trajectories in the vector field.
* **virtual\_time** – The time the agents get to move in the vector field. Higher values therefore result in longer stream lines. However, this whole time gets simulated upon creation.
* **max\_anchors\_per\_line** – The maximum number of anchors per line. Lines with more anchors get reduced in complexity, not in length.
* **padding** – The distance agents can move out of the generation area before being terminated.
* **stroke\_width** – The stroke with of the stream lines.
* **opacity** – The opacity of the stream lines.


Examples


Example: BasicUsage [¶](#basicusage)

![../_images/BasicUsage-2.png](../_images/BasicUsage-2.png)

```
from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(StreamLines(func))

```


```

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(StreamLines(func))


```

Example: SpawningAndFlowingArea [¶](#spawningandflowingarea)

![../_images/SpawningAndFlowingArea-1.png](../_images/SpawningAndFlowingArea-1.png)

```
from manim import *

class SpawningAndFlowingArea(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )

        spawning_area = Rectangle(width=6, height=4)
        flowing_area = Rectangle(width=8, height=6)
        labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        self.add(stream_lines, spawning_area, flowing_area, *labels)

```


```

class SpawningAndFlowingArea(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )

        spawning_area = Rectangle(width=6, height=4)
        flowing_area = Rectangle(width=8, height=6)
        labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        self.add(stream_lines, spawning_area, flowing_area, *labels)


```
Methods


| [`create`](#manim.mobject.vector_field.StreamLines.create "manim.mobject.vector_field.StreamLines.create") | The creation animation of the stream lines. |
| --- | --- |
| [`end_animation`](#manim.mobject.vector_field.StreamLines.end_animation "manim.mobject.vector_field.StreamLines.end_animation") | End the stream line animation smoothly. |
| [`start_animation`](#manim.mobject.vector_field.StreamLines.start_animation "manim.mobject.vector_field.StreamLines.start_animation") | Animates the stream lines using an updater. |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*func*, *color\=None*, *color\_scheme\=None*, *min\_color\_scheme\_value\=0*, *max\_color\_scheme\_value\=2*, *colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')]*, *x\_range\=None*, *y\_range\=None*, *z\_range\=None*, *three\_dimensions\=False*, *noise\_factor\=None*, *n\_repeats\=1*, *dt\=0\.05*, *virtual\_time\=3*, *max\_anchors\_per\_line\=100*, *padding\=3*, *stroke\_width\=1*, *opacity\=1*, *\*\*kwargs*)[¶](#manim.mobject.vector_field.StreamLines._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*)
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*)
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*)
* **min\_color\_scheme\_value** (*float*)
* **max\_color\_scheme\_value** (*float*)
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*)
* **x\_range** (*Sequence**\[**float**]*)
* **y\_range** (*Sequence**\[**float**]*)
* **z\_range** (*Sequence**\[**float**]*)
* **three\_dimensions** (*bool*)
* **noise\_factor** (*float* *\|* *None*)


create(*lag\_ratio\=None*, *run\_time\=None*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/vector_field.html#StreamLines.create)[¶](#manim.mobject.vector_field.StreamLines.create "Link to this definition")
The creation animation of the stream lines.


The stream lines appear in random order.


Parameters:
* **lag\_ratio** (*float* *\|* *None*) – The lag ratio of the animation.
If undefined, it will be selected so that the total animation length is 1\.5 times the run time of each stream line creation.
* **run\_time** (*Callable**\[**\[**float**]**,* *float**]* *\|* *None*) – The run time of every single stream line creation. The runtime of the whole animation might be longer due to the lag\_ratio.
If undefined, the virtual time of the stream lines is used as run time.


Returns:
The creation animation of the stream lines.


Return type:
[`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")


Examples


Example: StreamLineCreation [¶](#streamlinecreation)


```
from manim import *

class StreamLineCreation(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()

```


```

class StreamLineCreation(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()


```


end\_animation()[\[source]](../_modules/manim/mobject/vector_field.html#StreamLines.end_animation)[¶](#manim.mobject.vector_field.StreamLines.end_animation "Link to this definition")
End the stream line animation smoothly.


Returns an animation resulting in fully displayed stream lines without a noticeable cut.


Returns:
The animation fading out the running stream animation.


Return type:
[`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")


Raises:
**ValueError** – if no stream line animation is running


Examples


Example: EndAnimation [¶](#endanimation)


```
from manim import *

class EndAnimation(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())

```


```

class EndAnimation(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())


```


start\_animation(*warm\_up\=True*, *flow\_speed\=1*, *time\_width\=0\.3*, *rate\_func\=\<function linear\>*, *line\_animation\_class\=\<class 'manim.animation.indication.ShowPassingFlash'\>*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/vector_field.html#StreamLines.start_animation)[¶](#manim.mobject.vector_field.StreamLines.start_animation "Link to this definition")
Animates the stream lines using an updater.


The stream lines will continuously flow


Parameters:
* **warm\_up** (*bool*) – If True the animation is initialized line by line. Otherwise it starts with all lines shown.
* **flow\_speed** (*float*) – At flow\_speed\=1 the distance the flow moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of this flow.
* **time\_width** (*float*) – The proportion of the stream line shown while being animated
* **rate\_func** (*Callable**\[**\[**float**]**,* *float**]*) – The rate function of each stream line flashing
* **line\_animation\_class** (*type**\[*[*ShowPassingFlash*](manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")*]*) – The animation class being used


Return type:
None


Examples


Example: ContinuousMotion [¶](#continuousmotion)


```
from manim import *

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

```


```

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)


```



---

# VectorField


# VectorField[¶](#vectorfield "Link to this heading")


Qualified name: `manim.mobject.vector\_field.VectorField`


*class* VectorField(*func*, *color\=None*, *color\_scheme\=None*, *min\_color\_scheme\_value\=0*, *max\_color\_scheme\_value\=2*, *colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')]*, *\*\*kwargs*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField)[¶](#manim.mobject.vector_field.VectorField "Link to this definition")
Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")


A vector field.


Vector fields are based on a function defining a vector at every position.
This class does by default not include any visible elements but provides
methods to move other [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s along the vector field.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*) – The function defining the rate of change at every position of the VectorField.
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*) – The color of the vector field. If set, position\-specific coloring is disabled.
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.
* **min\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.
* **max\_color\_scheme\_value** (*float*) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – The colors defining the color gradient of the vector field.
* **kwargs** – Additional arguments to be passed to the [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") constructor


Methods


| [`fit_to_coordinate_system`](#manim.mobject.vector_field.VectorField.fit_to_coordinate_system "manim.mobject.vector_field.VectorField.fit_to_coordinate_system") | Scale the vector field to fit a coordinate system. |
| --- | --- |
| [`get_colored_background_image`](#manim.mobject.vector_field.VectorField.get_colored_background_image "manim.mobject.vector_field.VectorField.get_colored_background_image") | Generate an image that displays the vector field. |
| [`get_nudge_updater`](#manim.mobject.vector_field.VectorField.get_nudge_updater "manim.mobject.vector_field.VectorField.get_nudge_updater") | Get an update function to move a [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field. |
| [`get_vectorized_rgba_gradient_function`](#manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function "manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function") | Generates a gradient of rgbas as a numpy array |
| [`nudge`](#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") | Nudge a [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field. |
| [`nudge_submobjects`](#manim.mobject.vector_field.VectorField.nudge_submobjects "manim.mobject.vector_field.VectorField.nudge_submobjects") | Apply a nudge along the vector field to all submobjects. |
| [`scale_func`](#manim.mobject.vector_field.VectorField.scale_func "manim.mobject.vector_field.VectorField.scale_func") | Scale a vector field function. |
| [`shift_func`](#manim.mobject.vector_field.VectorField.shift_func "manim.mobject.vector_field.VectorField.shift_func") | Shift a vector field function. |
| [`start_submobject_movement`](#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement") | Start continuously moving all submobjects along the vector field. |
| [`stop_submobject_movement`](#manim.mobject.vector_field.VectorField.stop_submobject_movement "manim.mobject.vector_field.VectorField.stop_submobject_movement") | Stops the continuous movement started using [`start_submobject_movement()`](#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement"). |


Attributes


| `animate` | Used to animate the application of any method of `self`. |
| --- | --- |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |


\_original\_\_init\_\_(*func*, *color\=None*, *color\_scheme\=None*, *min\_color\_scheme\_value\=0*, *max\_color\_scheme\_value\=2*, *colors\=\[ManimColor('\#236B8E'), ManimColor('\#83C167'), ManimColor('\#FFFF00'), ManimColor('\#FC6255')]*, *\*\*kwargs*)[¶](#manim.mobject.vector_field.VectorField._original__init__ "Link to this definition")
Initialize self. See help(type(self)) for accurate signature.


Parameters:
* **func** (*Callable**\[**\[**np.ndarray**]**,* *np.ndarray**]*)
* **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *\|* *None*)
* **color\_scheme** (*Callable**\[**\[**np.ndarray**]**,* *float**]* *\|* *None*)
* **min\_color\_scheme\_value** (*float*)
* **max\_color\_scheme\_value** (*float*)
* **colors** (*Sequence**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*)


fit\_to\_coordinate\_system(*coordinate\_system*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.fit_to_coordinate_system)[¶](#manim.mobject.vector_field.VectorField.fit_to_coordinate_system "Link to this definition")
Scale the vector field to fit a coordinate system.


This method is useful when the vector field is defined in a coordinate system
different from the one used to display the vector field.


This method can only be used once because it transforms the origin of each vector.


Parameters:
**coordinate\_system** ([*CoordinateSystem*](manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem "manim.mobject.graphing.coordinate_systems.CoordinateSystem")) – The coordinate system to fit the vector field to.


get\_colored\_background\_image(*sampling\_rate\=5*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.get_colored_background_image)[¶](#manim.mobject.vector_field.VectorField.get_colored_background_image "Link to this definition")
Generate an image that displays the vector field.


The color at each position is calculated by passing the positing through a
series of steps:
Calculate the vector field function at that position, map that vector to a
single value using self.color\_scheme and finally generate a color from
that value using the color gradient.


Parameters:
**sampling\_rate** (*int*) – The stepsize at which pixels get included in the image. Lower values give
more accurate results, but may take a long time to compute.


Returns:
The vector field image.


Return type:
Image.Imgae


get\_nudge\_updater(*speed\=1*, *pointwise\=False*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.get_nudge_updater)[¶](#manim.mobject.vector_field.VectorField.get_nudge_updater "Link to this definition")
Get an update function to move a [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field.


When used with [`add_updater()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), the mobject will move along the vector field, where its speed is determined by the magnitude of the vector field.


Parameters:
* **speed** (*float*) – At speed\=1 the distance a mobject moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of such a mobject.
* **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:
The update function.


Return type:
Callable\[\[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), float], [Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]


get\_vectorized\_rgba\_gradient\_function(*start*, *end*, *colors*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.get_vectorized_rgba_gradient_function)[¶](#manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function "Link to this definition")
Generates a gradient of rgbas as a numpy array


Parameters:
* **start** (*float*) – start value used for inverse interpolation at [`inverse_interpolate()`](manim.utils.bezier.html#manim.utils.bezier.inverse_interpolate "manim.utils.bezier.inverse_interpolate")
* **end** (*float*) – end value used for inverse interpolation at [`inverse_interpolate()`](manim.utils.bezier.html#manim.utils.bezier.inverse_interpolate "manim.utils.bezier.inverse_interpolate")
* **colors** (*Iterable**\[*[*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")*]*) – list of colors to generate the gradient


Return type:
function to generate the gradients as numpy arrays representing rgba values


nudge(*mob*, *dt\=1*, *substeps\=1*, *pointwise\=False*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.nudge)[¶](#manim.mobject.vector_field.VectorField.nudge "Link to this definition")
Nudge a [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field.


Parameters:
* **mob** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to move along the vector field
* **dt** (*float*) – A scalar to the amount the mobject is moved along the vector field.
The actual distance is based on the magnitude of the vector field.
* **substeps** (*int*) – The amount of steps the whole nudge is divided into. Higher values
give more accurate approximations.
* **pointwise** (*bool*) – Whether to move the mobject along the vector field. If False the
vector field takes effect on the center of the given
[`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). If True the vector field takes effect on the
points of the individual points of the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"),
potentially distorting it.


Returns:
This vector field.


Return type:
[VectorField](#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")


Examples


Example: Nudging [¶](#nudging)


```
from manim import *

class Nudging(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )
        self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)

        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)

        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(circle, dot)
        self.wait(6)

```


```

class Nudging(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )
        self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)

        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)

        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(circle, dot)
        self.wait(6)


```


nudge\_submobjects(*dt\=1*, *substeps\=1*, *pointwise\=False*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.nudge_submobjects)[¶](#manim.mobject.vector_field.VectorField.nudge_submobjects "Link to this definition")
Apply a nudge along the vector field to all submobjects.


Parameters:
* **dt** (*float*) – A scalar to the amount the mobject is moved along the vector field.
The actual distance is based on the magnitude of the vector field.
* **substeps** (*int*) – The amount of steps the whole nudge is divided into. Higher values
give more accurate approximations.
* **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:
This vector field.


Return type:
[VectorField](#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")


*static* scale\_func(*func*, *scalar*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.scale_func)[¶](#manim.mobject.vector_field.VectorField.scale_func "Link to this definition")
Scale a vector field function.


Parameters:
* **func** (*Callable**\[**\[**ndarray**]**,* *ndarray**]*) – The function defining a vector field.
* **scalar** (*float*) – The scalar to be applied to the vector field.


Return type:
*Callable*\[\[*ndarray*], *ndarray*]


Examples


Example: ScaleVectorFieldFunction [¶](#scalevectorfieldfunction)


```
from manim import *

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()

```


```

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()


```

Returns:
The scaled vector field function.


Return type:
Callable\[\[np.ndarray], np.ndarray]


Parameters:
* **func** (*Callable**\[**\[**ndarray**]**,* *ndarray**]*)
* **scalar** (*float*)


*static* shift\_func(*func*, *shift\_vector*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.shift_func)[¶](#manim.mobject.vector_field.VectorField.shift_func "Link to this definition")
Shift a vector field function.


Parameters:
* **func** (*Callable**\[**\[**ndarray**]**,* *ndarray**]*) – The function defining a vector field.
* **shift\_vector** (*ndarray*) – The shift to be applied to the vector field.


Returns:
The shifted vector field function.


Return type:
Callable\[\[np.ndarray], np.ndarray]


start\_submobject\_movement(*speed\=1*, *pointwise\=False*)[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.start_submobject_movement)[¶](#manim.mobject.vector_field.VectorField.start_submobject_movement "Link to this definition")
Start continuously moving all submobjects along the vector field.


Calling this method multiple times will result in removing the previous updater created by this method.


Parameters:
* **speed** (*float*) – The speed at which to move the submobjects. See [`get_nudge_updater()`](#manim.mobject.vector_field.VectorField.get_nudge_updater "manim.mobject.vector_field.VectorField.get_nudge_updater") for details.
* **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:
This vector field.


Return type:
[VectorField](#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")


stop\_submobject\_movement()[\[source]](../_modules/manim/mobject/vector_field.html#VectorField.stop_submobject_movement)[¶](#manim.mobject.vector_field.VectorField.stop_submobject_movement "Link to this definition")
Stops the continuous movement started using [`start_submobject_movement()`](#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement").


Returns:
This vector field.


Return type:
[VectorField](#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")



---

