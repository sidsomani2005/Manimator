# ReplacementTransform
class ReplacementTransform(Transform):
    def __init__(self, mobject, target_mobject, **kwargs):
        super().__init__(mobject, target_mobject, **kwargs)

# Restore  
class Restore(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.saved_state
        super().__init__(mobject, target, **kwargs)

# ScaleInPlace
class ScaleInPlace(Transform):
    def __init__(self, mobject, scale_factor, **kwargs):
        self.scale_factor = scale_factor
        super().__init__(mobject, **kwargs)

    def create_target(self):
        target = self.mobject.copy()
        target.scale(self.scale_factor)
        return target

# ShrinkToCenter
class ShrinkToCenter(Transform):
    def create_target(self):
        return self.mobject.scale(0)

# Swap
class Swap(Transform):
    def __init__(self, mobject1, mobject2, **kwargs):
        self.mobject1 = mobject1
        self.mobject2 = mobject2
        Transform.__init__(self, mobject1, **kwargs)

# Transform
class Transform(Animation):
    def __init__(
        self,
        mobject,
        target_mobject=None,
        path_func=None,
        path_arc=0,
        path_arc_axis=OUT,
        replace_mobject_with_target_in_scene=False,
        **kwargs
    ):
        self.path_arc = path_arc
        self.path_func = path_func
        self.path_arc_axis = path_arc_axis
        self.replace_mobject_with_target_in_scene = replace_mobject_with_target_in_scene
        super().__init__(mobject, **kwargs)
        self.target_mobject = target_mobject
        self.init_path_func()

# TransformAnimations  
class TransformAnimations(Transform):
    def __init__(self, start_anim, end_anim, rate_func=smooth, **kwargs):
        self.start_anim = start_anim
        self.end_anim = end_anim
        if "run_time" not in kwargs:
            kwargs["run_time"] = max(
                start_anim.get_run_time(),
                end_anim.get_run_time()
            )
        super().__init__(
            start_anim.mobject,
            end_anim.mobject,
            rate_func=rate_func,
            **kwargs
        )

# TransformFromCopy
class TransformFromCopy(Transform):
    def __init__(self, mobject, target_mobject, **kwargs):
        super().__init__(mobject.copy(), target_mobject, **kwargs)

# ApplyComplexFunction  
class ApplyComplexFunction(ApplyMethod):
    def __init__(self, function, mobject=None, **kwargs):
        self.function = function
        super().__init__(mobject.apply_complex_function, function, **kwargs)

# create_target
def create_target(self):
    return self.mobject.copy()

# path_arc
path_arc = 0

# path_func  
def path_func(start, end, alpha):
    return interpolate(start, end, alpha)

# initialize_matrix
def initialize_matrix(self, matrix):
    matrix = np.array(matrix)
    if matrix.shape == (2, 2):
        self.matrix = np.identity(3)
        self.matrix[:2, :2] = matrix
    elif matrix.shape == (3, 3):
        self.matrix = matrix
    else:
        raise ValueError("Matrix has bad dimensions")
    return self

# add
def add(self, *mobjects):
    self.submobjects += list(mobjects)
    return self

# add_animation_override  
def add_animation_override(self, animation_class, animation_overrider):
    self.animation_overrides[animation_class] = animation_overrider
    return self

    # add_background_rectangle
def add_background_rectangle(self, color=None, opacity=0.75, **kwargs):
    # Creates a BackgroundRectangle mobject and adds it behind the given mobject
    from manim.mobject.geometry.shape_matchers import BackgroundRectangle
    self.background_rectangle = BackgroundRectangle(
        self, color=color, fill_opacity=opacity, **kwargs
    )
    self.add_to_back(self.background_rectangle)
    return self

# add_background_rectangle_to_family_members_with_points  
def add_background_rectangle_to_family_members_with_points(self, **kwargs):
    for mob in self.family_members_with_points():
        mob.add_background_rectangle(**kwargs)
    return self

# add_background_rectangle_to_submobjects
def add_background_rectangle_to_submobjects(self, **kwargs):
    for submob in self.submobjects:
        submob.add_background_rectangle(**kwargs)
    return self

# add_n_more_submobjects
def add_n_more_submobjects(self, n):
    curr = len(self.submobjects)
    if n > 0:
        self.add(*self.get_group_class()(*[
            self.copy() for _ in range(n)
        ]))
    return self

# add_to_back
def add_to_back(self, *mobjects):
    self.remove(*mobjects)
    self.submobjects = list(mobjects) + self.submobjects
    return self

# add_updater
def add_updater(self, update_function, index=None, call_updater=True):
    if index is None:
        self.updaters.append(update_function)
    else:
        self.updaters.insert(index, update_function)
    if call_updater:
        self.update()
    return self

# align_data
def align_data(self, mobject):
    # Align data between two mobjects
    self.null_point_align(mobject)
    self.align_family(mobject)
    for mob1, mob2 in zip(self.family_members_with_points(), mobject.family_members_with_points()):
        mob1.align_points(mob2)
    return self

# align_on_border
def align_on_border(self, direction, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER):
    """
    Direction just needs to be a vector pointing towards side or
    corner in the 2d plane.
    """
    target_point = self.get_critical_point(direction)
    point_to_align = self.get_critical_point(direction)
    shift_val = target_point - point_to_align - buff * np.array(direction)
    shift_val = shift_val * abs(np.sign(direction))
    self.shift(shift_val)
    return self

# align_points
def align_points(self, mobject):
    max_len = max(self.get_num_points(), mobject.get_num_points())
    for mob in (self, mobject):
        mob.resize_points(max_len, resize_func=resize_preserving_order)
    return self

# align_points_with_larger
def align_points_with_larger(self, larger_mobject):
    assert(isinstance(larger_mobject, VMobject))
    self.align_family(larger_mobject)
    for sm1, sm2 in zip(self.get_family(), larger_mobject.get_family()):
        sm1.align_points(sm2)
    return self

# align_submobjects
def align_submobjects(self, mobject):
    mob1 = self
    mob2 = mobject
    n1 = len(mob1.submobjects)
    n2 = len(mob2.submobjects)
    mob1.add_n_more_submobjects(max(0, n2 - n1))
    mob2.add_n_more_submobjects(max(0, n1 - n2))
    return self

# align_to
def align_to(self, mobject_or_point, direction=ORIGIN, alignment_vect=UP):
    """
    Examples:
    mob1.align_to(mob2, UP) moves mob1 vertically so that its
    top edge lines ups with mob2's top edge.

    mob1.align_to(mob2, alignment_vect = RIGHT) moves mob1
    horizontally so that it's center is directly above/below
    the center of mob2
    """
    if isinstance(mobject_or_point, Mobject):
        point = mobject_or_point.get_critical_point(direction)
    else:
        point = mobject_or_point

    for dim in range(self.dim):
        if direction[dim] != 0:
            self.set_coord(point[dim], dim, direction)
    return self

# animation_override_for
def animation_override_for(self, animation_class):
    def decorator(animation_method):
        self.animation_overrides[animation_class] = animation_method
        return animation_method
    return decorator

# apply_complex_function
def apply_complex_function(self, function, **kwargs):
    def R3_func(point):
        x, y, z = point
        xy_complex = function(complex(x, y))
        return [
            xy_complex.real,
            xy_complex.imag,
            z
        ]
    return self.apply_function(R3_func, **kwargs)

# apply_function
def apply_function(self, function, **kwargs):
    for mob in self.family_members_with_points():
        arrs = mob.get_points()
        mob.set_points(np.apply_along_axis(function, 1, arrs))
    return self

# apply_function_to_position
def apply_function_to_position(self, function):
    self.move_to(function(self.get_center()))
    return self

# apply_function_to_submobject_positions
def apply_function_to_submobject_positions(self, function):
    for submob in self.submobjects:
        submob.apply_function_to_position(function)
    return self

# apply_matrix
def apply_matrix(self, matrix, **kwargs):
    return self.apply_function(
        lambda p: np.dot(p, matrix.T),
        **kwargs
    )

# apply_over_attr_arrays
def apply_over_attr_arrays(self, func):
    for attr in self.get_array_attrs():
        setattr(self, attr, func(getattr(self, attr)))
    return self

# apply_points_function_about_point
def apply_points_function_about_point(self, func, about_point=None, **kwargs):
    if about_point is None:
        about_point = self.get_center()
    self.shift(-about_point)
    self.apply_points_function(func, **kwargs)
    self.shift(about_point)
    return self

    # apply_to_family
def apply_to_family(self, func, *args, **kwargs):
    for mob in self.family_members_with_points():
        func(mob, *args, **kwargs)
    return self

# arrange
def arrange(self, direction=RIGHT, center=True, **kwargs):
    for m1, m2 in zip(self.submobjects, self.submobjects[1:]):
        m2.next_to(m1, direction, **kwargs)
    if center:
        self.center()
    return self

# arrange_in_grid
def arrange_in_grid(
    self, n_rows=None, n_cols=None, buff=None, h_buff=None, v_buff=None, 
    aligned_edge=ORIGIN, fill_rows_first=True
):
    submobs = self.submobjects
    if n_rows is None and n_cols is None:
        n_rows = int(np.sqrt(len(submobs)))
    if n_rows is None:
        n_rows = len(submobs) // n_cols
    if n_cols is None:
        n_cols = len(submobs) // n_rows
    
    if buff is not None:
        h_buff = buff
        v_buff = buff
    else:
        if h_buff is None:
            h_buff = self[0].get_width()
        if v_buff is None:
            v_buff = self[0].get_height()
    
    grid = np.arange(n_rows * n_cols).reshape((n_rows, n_cols))
    if not fill_rows_first:
        grid = grid.T
    
    for i, submob in enumerate(submobs):
        if i >= grid.size:
            submob.set_opacity(0)
            continue
        x, y = grid.flat[i] % n_cols, grid.flat[i] // n_cols
        submob.move_to(ORIGIN + x*h_buff*RIGHT + y*v_buff*DOWN)
    
    self.move_to(ORIGIN)
    return self

# arrange_submobjects  
def arrange_submobjects(self, *args, **kwargs):
    self.submobjects.sort(key=lambda m: m.get_center()[0])
    self.arrange(*args, **kwargs)
    return self

# become
def become(self, mobject):
    self.align_data(mobject)
    for sm1, sm2 in zip(self.get_family(), mobject.get_family()):
        sm1.points = np.array(sm2.points)
    return self

# center
def center(self):
    self.shift(-self.get_center())
    return self

# clear_updaters
def clear_updaters(self, recursive=True):
    self.updaters = []
    if recursive:
        for submob in self.submobjects:
            submob.clear_updaters(recursive=True)
    return self

# copy
def copy(self):
    return self.deepcopy()

# fade
def fade(self, darkness=0.5, family=True):
    self.set_opacity(1 - darkness, family=family)

# fade_to
def fade_to(self, darkness, alpha):
    return self.set_opacity(
        interpolate(self.get_opacity(), 1 - darkness, alpha)
    )

# family_members_with_points
def family_members_with_points(self):
    return [m for m in self.get_family() if m.has_points()]

# flip
def flip(self, axis=UP, **kwargs):
    return self.rotate(TAU / 2, axis, **kwargs)

# generate_points
def generate_points(self):
    self.points = np.zeros((0, 3))
    return self

# begin  
def begin(self):
    self.starting_mobject = self.mobject.copy()
    if self.suspend_mobject_updating:
        self.mobject.suspend_updating()
    self.interpolate(0)

# clean_up_from_scene
def clean_up_from_scene(self, scene):
    if self.is_remover():
        scene.remove(self.mobject)

# create_target
def create_target(self):
    return self.mobject.copy()

# get_all_families_zipped  
def get_all_families_zipped(self):
    return zip(*[
        mob.family_members_with_points()
        for mob in [
            self.mobject,
            self.starting_mobject,
            self.target_mobject
        ]
    ])

# get_all_mobjects
def get_all_mobjects(self):
    return [
        self.mobject, 
        self.starting_mobject,
        self.target_mobject
    ]

# get_all_mobjects_to_update
def get_all_mobjects_to_update(self):
    return self.get_family()

# get_rate_func
def get_rate_func(self):
    return self.rate_func

# get_run_time  
def get_run_time(self):
    return self.run_time


    # get_sub_alpha
def get_sub_alpha(self, alpha, index, num_submobjects):
    # Compute the sub-alpha for a submobject based on the overall alpha
    lag_ratio = self.lag_ratio
    full_length = (num_submobjects - 1) * lag_ratio + 1
    value = alpha * full_length
    return max(0, min(1, (value - index * lag_ratio) / (1 - lag_ratio)))

# interpolate  
def interpolate(self, alpha):
    self.interpolate_mobject(self.rate_func(alpha))

# interpolate_mobject
def interpolate_mobject(self, alpha):
    families = list(self.get_all_families_zipped())
    for i, mobs in enumerate(families):
        sub_alpha = self.get_sub_alpha(alpha, i, len(families))
        self.interpolate_submobject(*mobs, sub_alpha)

# interpolate_submobject
def interpolate_submobject(self, submob, start, end, sub_alpha):
    submob.interpolate(start, end, sub_alpha, self.path_func)

# is_introducer
def is_introducer(self):
    return isinstance(self, (ShowCreation, Write, GrowFromCenter))

# is_remover  
def is_remover(self):
    return self.remover

# set_name
def set_name(self, name):
    self.name = name
    return self

# set_rate_func  
def set_rate_func(self, rate_func):
    self.rate_func = rate_func
    return self

# set_run_time
def set_run_time(self, run_time):
    self.run_time = run_time
    return self

# update_mobjects
def update_mobjects(self, dt):
    for mob in self.get_all_mobjects():
        mob.update(dt)

# full_family_become_partial
def full_family_become_partial(self, family, alpha):
    for mob in family:
        mob.become_partial(self, alpha)

# update_boundary_copies
def update_boundary_copies(self):
    for submob in self.submobjects:
        submob.update_boundary_copies()
    self.update_boundary_copy()

# change_bar_values
def change_bar_values(self, values):
    for bar, value in zip(self.bars, values):
        bar.set_value(value)

# get_bar_labels
def get_bar_labels(self):
    return VGroup(*[
        bar.get_label() for bar in self.bars
    ])

# update_path
def update_path(self):
    self.path.set_points(self.trace.get_points())

# fit_to_coordinate_system  
def fit_to_coordinate_system(self, coord_sys):
    self.apply_function(
        lambda p: coord_sys.coords_to_point(*p[:coord_sys.dim])
    )
    return self

# get_colored_background_image
def get_colored_background_image(self, color=None):
    if color is None:
        color = self.default_color
    return ImageMobject(color_gradient([color, BLACK], 200))

# get_nudge_updater
def get_nudge_updater(self, dt):
    def updater(mob):
        mob.nudge(dt)
    return updater

# get_vectorized_rgba_gradient_function
def get_vectorized_rgba_gradient_function(self, min_value=0, max_value=1):
    colors = self.color_lookup_table
    rgbas = np.array([color_to_rgba(c) for c in colors])
    return get_vectorized_rgba_gradient_function(
        rgbas, min_value, max_value
    )

# nudge
def nudge(self, dt):
    self.shift(self.velocity * dt)

# nudge_submobjects  
def nudge_submobjects(self, dt):
    for submob in self.submobjects:
        submob.nudge(dt)

# scale_func
def scale_func(self, scale_factor):
    self.scale(scale_factor)

# shift_func  
def shift_func(self, vector):
    self.shift(vector)

# start_submobject_movement
def start_submobject_movement(self):
    for submob in self.submobjects:
        submob.start_movement()

        # stop_submobject_movement
def stop_submobject_movement(self):
    for submob in self.submobjects:
        submob.movement_updater = None

# get_default_tip_length
def get_default_tip_length(self):
    return self.tip_length

# get_normal_vector
def get_normal_vector(self):
    p1, p2 = self.get_start_and_end()
    return normalize(rotate_vector(p2 - p1, TAU / 4))

# reset_normal_vector
def reset_normal_vector(self):
    self.normal_vector = self.get_normal_vector()

# scale
def scale(self, scale_factor, **kwargs):
    self.apply_points_function(
        lambda points: scale_factor * points, **kwargs
    )
    return self

# sort_submobjects
def sort_submobjects(self, point_to_num_func=lambda p: p[0], submob_func=None):
    if submob_func is None:
        submob_func = lambda m: point_to_num_func(m.get_center())
    self.submobjects.sort(key=submob_func)
    return self

# space_out_submobjects
def space_out_submobjects(self, factor=1.5, **kwargs):
    self.scale(factor, **kwargs)
    for submob in self.submobjects:
        submob.scale(1. / factor)
    return self

# split
def split(self):
    return self.submobjects

# stretch
def stretch(self, factor, dim, **kwargs):
    def func(p):
        p[dim] *= factor
        return p
    self.apply_points_function(func, **kwargs)
    return self

# stretch_about_point
def stretch_about_point(self, factor, dim, point):
    return self.apply_points_function(
        lambda p: stretch_array(p, factor, dim, point),
        about_point=point
    )

# stretch_to_fit_depth
def stretch_to_fit_depth(self, depth, **kwargs):
    return self.stretch_to_fit_dimension(depth, 2, **kwargs)

# stretch_to_fit_height
def stretch_to_fit_height(self, height, **kwargs):
    return self.stretch_to_fit_dimension(height, 1, **kwargs)

# stretch_to_fit_width
def stretch_to_fit_width(self, width, **kwargs):
    return self.stretch_to_fit_dimension(width, 0, **kwargs)

# surround
def surround(self, mobject_or_point, dim_to_match=0, stretch=False, buff=MED_SMALL_BUFF):
    if isinstance(mobject_or_point, Mobject):
        mob = mobject_or_point
        target_point = mob.get_center()
    else:
        target_point = mobject_or_point
    if stretch:
        self.stretch_to_fit_width(mob.length_over_dim(dim_to_match))
    else:
        self.rescale_to_fit(mob.length_over_dim(dim_to_match), dim_to_match)
    self.shift(target_point - self.get_center())
    self.shift_onto_screen(buff=buff)
    return self

# suspend_updating
def suspend_updating(self, recursive=True):
    self.updating_suspended = True
    if recursive:
        for submob in self.submobjects:
            submob.suspend_updating(recursive)
    return self

# throw_error_if_no_points
def throw_error_if_no_points(self):
    if self.get_num_points() == 0:
        caller_name = sys._getframe(1).f_code.co_name
        raise Exception(f"Cannot call Mobject.{caller_name} for a Mobject with no points")

# to_corner
def to_corner(self, corner=LEFT+DOWN, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER):
    return self.align_on_border(corner, buff)

# to_edge
def to_edge(self, edge=LEFT, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER):
    return self.align_on_border(edge, buff)

# to_original_color
def to_original_color(self):
    self.set_color(self.color)
    return self

# update
def update(self, dt=0):
    if not self.updating_suspended:
        for updater in self.updaters:
            updater(self, dt)
    return self

# update_active_animation
def update_active_animation(self, alpha):
    if self.active_animation:
        self.active_animation.update_mobject(alpha)

# begin
def begin(self):
    self.starting_mobject = self.mobject.copy()
    if self.suspend_mobject_updating:
        self.mobject.suspend_updating()
    self.interpolate(0)

# finish
def finish(self):
    self.interpolate(1)
    if self.suspend_mobject_updating:
        self.mobject.resume_updating()

# next_animation
def next_animation(self):
    if self.animation_index < len(self.animations):
        self.animation_index += 1
        self.current_animation = self.animations[self.animation_index]
        self.current_animation.begin()

# update_mobjects
def update_mobjects(self, dt):
    for animation in self.animations:
        animation.update_mobjects(dt)