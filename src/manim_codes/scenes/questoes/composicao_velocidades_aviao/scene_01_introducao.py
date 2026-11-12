from manim import *

from manim_codes.config.theme import IVORY, ORANGE


def build_intro(scene):
    """Cena introdutória: sistema de coordenadas, avião e vento."""

    scene.play(
        Create(scene.axes),
        run_time=1.5,
    )

    axis_labels = VGroup(
        Text("LESTE", font_size=22, color=IVORY)
        .move_to(scene.axes.c2p(4.3, 0, 0) + RIGHT * 0.2),
        Text("NORTE", font_size=22, color=IVORY)
        .move_to(scene.axes.c2p(0, 4.3, 0) + UP * 0.2),
        Text("ALTITUDE", font_size=22, color=IVORY)
        .move_to(scene.axes.c2p(0, 0, 2.2) + RIGHT * 0.4),
    )

    scene.play(FadeIn(axis_labels), run_time=0.8)

    plane = Arrow3D(
        start=scene.axes.c2p(0, 0, 0.3),
        end=scene.axes.c2p(0.7, 0.7, 0.3),
        color=IVORY,
        thickness=0.06,
    )

    scene.play(FadeIn(plane), run_time=0.8)

    wind_particles = VGroup()
    for i in range(5):
        particle = Sphere(
            radius=0.045,
            color=ORANGE,
            resolution=(8, 8),
        )
        particle.move_to(scene.point(-0.4 + i * 0.12, 0.8 - i * 0.1, 0.5))
        wind_particles.add(particle)

    scene.play(FadeIn(wind_particles), run_time=0.5)

    title = scene.show_caption(
        "Como chegar ao destino apesar do vento?",
        size=29,
    )

    scene.wait(1)
    scene.hide_caption(title)
