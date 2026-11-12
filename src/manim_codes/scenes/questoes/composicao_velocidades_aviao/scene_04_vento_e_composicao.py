from manim import *

from manim_codes.config.layout import safe_point
from manim_codes.config.theme import GREEN, ORANGE


def build_vento_e_composicao(scene):
    """Apresenta o vetor do vento e a composição vetorial."""

    title = scene.show_caption("O vento também possui velocidade")

    wind_velocity = (30, -20, -1)
    wind_arrow = scene.make_vector(scene.origin, scene.point(*wind_velocity), ORANGE)
    scene.play(FadeIn(wind_arrow), run_time=1.2)

    wind_formula = scene.equation(
        r"\vec v_{\mathrm{ar/solo}}="
        r"(30,\ -20,\ -1)\ \mathrm{km/h}",
        size=32,
    )
    wind_formula.move_to(safe_point(50, 24))
    scene.add_fixed_in_frame_mobjects(wind_formula)
    scene.play(Write(wind_formula), run_time=0.8)

    wind_components = VGroup(
        scene.equation(r"+30\ \mathrm{km/h}\quad\mathrm{Leste}", size=27),
        scene.equation(r"-20\ \mathrm{km/h}\quad\mathrm{Sul}", size=27),
        scene.equation(r"-1\ \mathrm{km/h}\quad\mathrm{Baixo}", size=27),
    )
    wind_components.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    wind_components.move_to(safe_point(40, 52))
    scene.add_fixed_in_frame_mobjects(wind_components)
    scene.play(FadeIn(wind_components), run_time=0.8)
    scene.wait(0.8)
    scene.play(FadeOut(wind_components), FadeOut(wind_formula), run_time=0.5)
    scene.wait(0.5)
    scene.hide_caption(title)

    title = scene.show_caption("Compensando a ação do vento")

    equation_sum = scene.equation(
        r"\vec v_{\mathrm{solo}}="
        r"\vec v_{\mathrm{aviao/ar}}+"
        r"\vec v_{\mathrm{ar/solo}}",
        size=31,
    )
    equation_sum.move_to(safe_point(50, 22))
    scene.add_fixed_in_frame_mobjects(equation_sum)
    scene.play(Write(equation_sum), run_time=1)
    scene.wait(0.7)

    equation_sub = scene.equation(
        r"\vec v_{\mathrm{aviao/ar}}="
        r"\vec v_{\mathrm{solo}}-"
        r"\vec v_{\mathrm{ar/solo}}",
        size=31,
    )
    equation_sub.move_to(equation_sum)
    scene.play(Transform(equation_sum, equation_sub), run_time=1)

    air_velocity = (170, 220, 11)
    calculations = VGroup(
        scene.equation(r"v_x=200-30=170", size=31),
        scene.equation(r"v_y=200-(-20)=220", size=31),
        scene.equation(r"v_z=10-(-1)=11", size=31),
    )
    calculations.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    calculations.move_to(safe_point(38, 50))
    scene.add_fixed_in_frame_mobjects(calculations)
    scene.play(FadeIn(calculations), run_time=1)
    scene.wait(1)
    scene.play(FadeOut(calculations), FadeOut(equation_sum), run_time=0.5)

    air_arrow = scene.make_vector(scene.origin, scene.point(*air_velocity), GREEN, thickness=0.045)
    scene.play(FadeIn(air_arrow), run_time=1.2)

    wind_translated = scene.make_vector(
        scene.point(*air_velocity),
        scene.point(*((200, 200, 10))),
        ORANGE,
        thickness=0.045,
    )

    scene.play(FadeIn(wind_translated), run_time=1.2)
    scene.wait(0.8)
    scene.hide_caption(title)
