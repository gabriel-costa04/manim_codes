from manim import *

from manim_codes.config.layout import place_in_safe_area
from manim_codes.config.theme import CORAL, GREEN, ORANGE


def build_vento_e_composicao(scene):
    """Apresenta o vetor do vento e a composição vetorial."""

    title = scene.show_caption("O vento também possui velocidade")

    # Componentes do vento
    wind_velocity = (60, -40, -2)

    p0 = scene.origin
    px = scene.point(90, 0, 0)
    py = scene.point(0, -60, 0)
    pz = scene.point(0, 0, -5)
    pxyz = scene.point(*wind_velocity)

    wind_x = scene.make_vector(
        p0, px, CORAL, thickness=0.035
    )

    wind_y = scene.make_vector(
        p0, py, CORAL, thickness=0.035
    )

    wind_z = scene.make_vector(
        p0, pz, CORAL, thickness=0.035
    )

    # Apresentação progressiva das componentes
    scene.play(FadeIn(wind_x), run_time=0.9)
    scene.wait(0.4)

    scene.play(FadeIn(wind_y), run_time=0.9)
    scene.wait(0.4)

    scene.play(FadeIn(wind_z), run_time=0.9)
    scene.wait(0.8)

    # Identificação matemática das componentes
    wind_components = VGroup(
        scene.equation(r"+30\ \mathrm{km/h}\quad\mathrm{Leste}", size=27),
        scene.equation(r"-20\ \mathrm{km/h}\quad\mathrm{Sul}", size=27),
        scene.equation(r"-1\ \mathrm{km/h}\quad\mathrm{Baixo}", size=27),
    )

    wind_components.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    place_in_safe_area(
        wind_components,
        x_pct=40,
        y_pct=70,
        area="content",
    )

    scene.add_fixed_in_frame_mobjects(wind_components)
    scene.play(FadeIn(wind_components), run_time=0.8)
    scene.wait(1)

    # Vetor resultante do vento
    wind_arrow = scene.make_vector(
        p0,
        pxyz,
        ORANGE,
        thickness=0.045,
    )

    scene.play(
        FadeOut(wind_x),
        FadeOut(wind_y),
        FadeOut(wind_z),
        FadeIn(wind_arrow),
        run_time=1,
    )

    wind_formula = scene.equation(
        r"\vec v_{\mathrm{ar/solo}}="
        r"(30,\ -20,\ -1)\ \mathrm{km/h}",
        size=32,
    )

    place_in_safe_area(
        wind_formula,
        x_pct=50,
        y_pct=20,
        area="text",
    )

    scene.add_fixed_in_frame_mobjects(wind_formula)
    scene.play(Write(wind_formula), run_time=0.8)
    scene.wait(1)

    scene.play(
        FadeOut(wind_components),
        FadeOut(wind_formula),
        FadeOut(wind_arrow),
        run_time=0.5,
    )

    scene.wait(0.5)
    scene.hide_caption(title)