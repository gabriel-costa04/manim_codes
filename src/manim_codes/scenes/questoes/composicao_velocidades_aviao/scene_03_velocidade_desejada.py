from manim import *

from manim_codes.config.layout import place_in_safe_area
from manim_codes.config.theme import BLUE


def build_velocidade_desejada(scene):
    """Cena do cálculo da velocidade desejada e do vetor resultante."""

    scene.play(
        FadeOut(scene.displacement),
        FadeOut(scene.component_x),
        FadeOut(scene.component_y),
        FadeOut(scene.component_z),
        run_time=0.5,
    )

    scene.play(
        FadeOut(scene.distances),
        FadeOut(scene.time_label),
        run_time=0.4,
    )

    title = scene.show_caption("Calculando a velocidade desejada")

    formula = scene.equation(
        r"\vec v_{\mathrm{solo}}="
        r"\frac{\Delta\vec r}{\Delta t}",
        size=38,
    )
    place_in_safe_area(formula, x_pct=50, y_pct=30, area="content")
    scene.add_fixed_in_frame_mobjects(formula)
    scene.play(Write(formula), run_time=1)

    conversion = scene.equation(r"6\ \mathrm{min}=0{,}1\ \mathrm{h}", size=36)
    place_in_safe_area(conversion, x_pct=50, y_pct=63, area="content")
    scene.add_fixed_in_frame_mobjects(conversion)
    scene.play(Write(conversion), run_time=0.8)

    components = VGroup(
        scene.equation(r"v_x=\frac{20}{0{,}1}=200", size=32),
        scene.equation(r"v_y=\frac{20}{0{,}1}=200", size=32),
        scene.equation(r"v_z=\frac{1}{0{,}1}=10", size=32),
    )
    components.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    place_in_safe_area(components, x_pct=42, y_pct=50, area="content")
    scene.add_fixed_in_frame_mobjects(components)
    scene.play(FadeIn(components), run_time=1)
    scene.wait(0.8)
    scene.play(
        FadeOut(formula),
        FadeOut(conversion),
        FadeOut(components),
        run_time=0.5,
    )

    ground_velocity = (200, 200, 10)
    ground_arrow = scene.make_vector(scene.origin, scene.point(*ground_velocity), BLUE)
    scene.play(FadeIn(ground_arrow), run_time=1.5)

    ground_result = scene.equation(
        r"\vec v_{\mathrm{aviao/solo}}="
        r"(200,\ 200,\ 10)\ \mathrm{km/h}",
        size=31,
    )
    place_in_safe_area(ground_result, x_pct=50, y_pct=24, area="content")
    scene.add_fixed_in_frame_mobjects(ground_result)
    scene.play(Write(ground_result), run_time=0.8)
    scene.wait(0.5)
    scene.hide_caption(title)
