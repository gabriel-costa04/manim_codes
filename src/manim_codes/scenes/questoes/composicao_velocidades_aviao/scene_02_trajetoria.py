from manim import *

from manim_codes.config.layout import safe_point
from manim_codes.config.theme import BLUE, GREEN, IVORY, ORANGE


def build_trajetoria(scene):
    """Cena com a trajetória desejada e componentes do deslocamento."""

    scene.move_camera(
        phi=65 * DEGREES,
        theta=-55 * DEGREES,
        zoom=0.95,
        run_time=1.5,
    )

    title = scene.show_caption("A trajetória desejada")

    destination = scene.axes.c2p(3.6, 3.6, 1.5)
    displacement = Arrow3D(
        start=scene.origin,
        end=destination,
        color=IVORY,
        thickness=0.04,
    )

    scene.play(FadeIn(displacement), run_time=1.5)

    p_x = scene.axes.c2p(3.6, 0, 0)
    p_xy = scene.axes.c2p(3.6, 3.6, 0)

    component_x = DashedLine(scene.origin, p_x, color=BLUE, stroke_width=4)
    component_y = DashedLine(p_x, p_xy, color=GREEN, stroke_width=4)
    component_z = DashedLine(p_xy, destination, color=ORANGE, stroke_width=4)

    scene.displacement = displacement
    scene.component_x = component_x
    scene.component_y = component_y
    scene.component_z = component_z

    scene.play(
        Create(component_x),
        Create(component_y),
        Create(component_z),
        run_time=1.8,
    )

    distances = VGroup(
        Text("20 km Leste", font_size=24, color=BLUE),
        Text("20 km Norte", font_size=24, color=GREEN),
        Text("1 km acima", font_size=24, color=ORANGE),
    )
    distances.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    distances.move_to(safe_point(24, 82))

    scene.add_fixed_in_frame_mobjects(distances)
    scene.distances = distances

    time_label = Text(
        "Tempo disponível: 6 minutos",
        font_size=27,
        color=IVORY,
        weight=BOLD,
    ).move_to(safe_point(48, 12))

    scene.add_fixed_in_frame_mobjects(time_label)
    scene.time_label = time_label

    scene.play(FadeIn(distances), FadeIn(time_label), run_time=0.8)
    scene.wait(1)
    scene.hide_caption(title)
