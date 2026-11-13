from pathlib import Path
from manim import *

from manim_codes.config.theme import IVORY, ORANGE, GREEN


def build_intro(scene):
    """Cena introdutória: sistema de coordenadas, avião e vento."""

    scene.play(
        Create(scene.axes),
        run_time=1.5,
    )

    x_offset = scene.axes.c2p(0.2, 0, 0) - scene.axes.c2p(0, 0, 0)
    y_offset = scene.axes.c2p(0, 0.2, 0) - scene.axes.c2p(0, 0, 0)
    z_offset = scene.axes.c2p(0, 0, 0.5) - scene.axes.c2p(0, 0, 0)

    axis_labels = VGroup(
        Text("LESTE", font_size=22, color=IVORY)
        .move_to(scene.axes.x_axis.get_end() - z_offset),

        Text("NORTE", font_size=22, color=IVORY)
        .move_to(scene.axes.y_axis.get_end() + z_offset),

        Text("ALTITUDE", font_size=22, color=IVORY)
        .move_to(scene.axes.z_axis.get_end() + z_offset),
    )

    scene.add_fixed_orientation_mobjects(*axis_labels)

    scene.play(FadeIn(axis_labels), run_time=0.8)

    # Avião
    plane_path = Path(__file__).resolve().parents[4] / "assets" / "svg" / "plane.svg"

    plane = SVGMobject(
        str(plane_path),
        height=0.7,
    )

    plane.set_color(GREEN)

    plane.move_to(
        scene.axes.c2p(0, 0, 0)
    )

    plane.rotate(-70 * DEGREES)

    scene.add_fixed_orientation_mobjects(plane)

    scene.play(
        FadeIn(plane),
        run_time=0.8,
    )

    # wind_particles = VGroup()
    # for i in range(5):
    #     particle = Sphere(
    #         radius=0.045,
    #         color=ORANGE,
    #         resolution=(8, 8),
    #     )
    #     particle.move_to(scene.point(-0.4 + i * 0.12, 0.8 - i * 0.1, 0.5))
    #     wind_particles.add(particle)

    # scene.play(FadeIn(wind_particles), run_time=0.5)

    # title = scene.show_caption(
    #     "Como chegar ao destino apesar do vento?",
    #     size=29,
    # )

    # scene.wait(1)
    # scene.hide_caption(title)
