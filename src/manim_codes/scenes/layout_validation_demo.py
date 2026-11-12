from manim import *

from manim_codes.config.layout import place_in_safe_area, validate_object_in_area


class LayoutValidationDemo(ThreeDScene):
    """Demonstração do sistema de posicionamento seguro do projeto."""

    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=0.8)

        title = Text("TÍTULO", font_size=40, color=WHITE)
        formula = MathTex(r"\vec v = \frac{\Delta \vec r}{\Delta t}", font_size=34)

        place_in_safe_area(title, x_pct=50, y_pct=12, area="content")
        place_in_safe_area(formula, x_pct=50, y_pct=30, area="content")

        self.add_fixed_in_frame_mobjects(title, formula)
        self.play(FadeIn(title), FadeIn(formula), run_time=1)
        self.wait(1)

        assert validate_object_in_area(title, area="content", warn=False)
        assert validate_object_in_area(formula, area="content", warn=False)
