from manim import *

from manim_codes.config.layout import TEXT_MAX_WIDTH, place_in_safe_area
from manim_codes.config.theme import BACKGROUND, IVORY

try:
    from manim_codes.scenes.questoes.composicao_velocidades_aviao.scene_01_introducao import build_intro
    from manim_codes.scenes.questoes.composicao_velocidades_aviao.scene_02_trajetoria import build_trajetoria
    from manim_codes.scenes.questoes.composicao_velocidades_aviao.scene_03_velocidade_desejada import build_velocidade_desejada
    from manim_codes.scenes.questoes.composicao_velocidades_aviao.scene_04_vento_e_composicao import build_vento_e_composicao
    from manim_codes.scenes.questoes.composicao_velocidades_aviao.scene_05_conclusao import build_conclusao
except ModuleNotFoundError:
    from .scene_01_introducao import build_intro
    from .scene_02_trajetoria import build_trajetoria
    from .scene_03_velocidade_desejada import build_velocidade_desejada
    from .scene_04_vento_e_composicao import build_vento_e_composicao
    from .scene_05_conclusao import build_conclusao

# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BACKGROUND

# Escalas visuais
SCALE_XY = 0.018
SCALE_Z = 0.15


class ComposicaoVelocidadesAviao(ThreeDScene):
    """Animação modular da composição de velocidades de um avião."""

    def construct(self):
        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.82,
        )

        self.axes = ThreeDAxes(
            x_range=[-1, 4.5, 1],
            y_range=[-1, 4.5, 1],
            z_range=[-1, 2.5, 1],
            x_length=5,
            y_length=5,
            z_length=3.2,
            axis_config={
                "color": IVORY,
                "stroke_width": 2,
                "include_numbers": False,
            },
        )

        self.origin = self.axes.c2p(0, 0, 0)

        def point(x, y, z):
            return self.axes.c2p(
                x * SCALE_XY,
                y * SCALE_XY,
                z * SCALE_Z,
            )

        self.point = point

        def make_vector(start, end, color, thickness=0.035):
            return Arrow3D(
                start=start,
                end=end,
                color=color,
                thickness=thickness,
            )

        def caption(text, size=32):
            caption_obj = Text(
                text,
                font_size=size,
                color=IVORY,
                weight=BOLD,
            )
            target_width = TEXT_MAX_WIDTH * 0.72
            caption_obj.scale_to_fit_width(target_width)
            return place_in_safe_area(caption_obj, x_pct=50, y_pct=12, area="content")

        def equation(tex, size=35):
            return MathTex(
                tex,
                font_size=size,
                color=IVORY,
            )

        self.make_vector = make_vector
        self.equation = equation
        self.caption = caption

        def show_caption(text, size=32):
            caption_obj = caption(text, size)
            self.add_fixed_in_frame_mobjects(caption_obj)
            self.play(FadeIn(caption_obj), run_time=0.5)
            return caption_obj

        def hide_caption(obj):
            self.play(FadeOut(obj), run_time=0.35)

        self.show_caption = show_caption
        self.hide_caption = hide_caption

        build_intro(self)
        build_trajetoria(self)
        build_velocidade_desejada(self)
        build_vento_e_composicao(self)
        build_conclusao(self)


if __name__ == "__main__":
    from manim import main
    main()
