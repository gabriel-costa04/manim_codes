from manim import *

from manim_codes.config.layout import place_in_safe_area
from manim_codes.config.theme import GREEN


def build_conclusao(scene):
    """Cena final: resposta e alternativa correta."""

    final_result = scene.equation(
        r"\boxed{\vec v_{\mathrm{aviao/ar}}="
        r"(170,\ 220,\ 11)\ \mathrm{km/h}}",
        size=34,
    )
    place_in_safe_area(final_result, x_pct=50, y_pct=26, area="content")
    scene.add_fixed_in_frame_mobjects(final_result)
    scene.play(Write(final_result), run_time=1.2)

    alternative = Text(
        "ALTERNATIVA D",
        font_size=42,
        color=GREEN,
        weight=BOLD,
    )
    place_in_safe_area(alternative, x_pct=50, y_pct=8, area="content")
    scene.add_fixed_in_frame_mobjects(alternative)
    scene.play(FadeIn(alternative, scale=1.2), run_time=0.8)

    scene.move_camera(zoom=1.05, run_time=1.5)
    scene.wait(1.5)
