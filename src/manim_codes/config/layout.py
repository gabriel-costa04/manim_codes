
import numpy as np
from manim import config, Rectangle, VGroup

from manim_codes.config.theme import GREEN, BLUE, CYAN, YELLOW

# ============================================================
# CONFIGURAÇÃO DO CANVAS
# ============================================================

config.pixel_width = 1080
config.pixel_height = 1920

config.frame_width = 9
config.frame_height = 16

FRAME_WIDTH = config.frame_width
FRAME_HEIGHT = config.frame_height

PIXEL_WIDTH = config.pixel_width
PIXEL_HEIGHT = config.pixel_height

# ============================================================
# MARGENS PROIBIDAS — MEDIDAS EMPIRICAMENTE
# ============================================================

SAFE_LEFT_PX = 0
SAFE_RIGHT_PX = 120
SAFE_TOP_PX = 220
SAFE_BOTTOM_PX = 420

SAFE_X_MIN_PX = SAFE_LEFT_PX
SAFE_X_MAX_PX = PIXEL_WIDTH - SAFE_RIGHT_PX

SAFE_Y_MIN_PX = SAFE_TOP_PX
SAFE_Y_MAX_PX = PIXEL_HEIGHT - SAFE_BOTTOM_PX

# ============================================================
# CONVERSÃO PIXEL -> MANIM
# ============================================================

PIXEL_TO_UNIT_X = FRAME_WIDTH / PIXEL_WIDTH
PIXEL_TO_UNIT_Y = FRAME_HEIGHT / PIXEL_HEIGHT


def pixel_to_point(x_px: float, y_px: float) -> np.ndarray:
    """
    Converte coordenadas em pixels para coordenadas Manim.

    Origem em pixels: canto superior esquerdo.
    """

    x = (x_px / PIXEL_WIDTH - 0.5) * FRAME_WIDTH
    y = (0.5 - y_px / PIXEL_HEIGHT) * FRAME_HEIGHT

    return np.array([x, y, 0.0])


def pct_to_point(x_pct: float, y_pct: float) -> np.ndarray:
    """
    Converte percentuais da tela inteira para coordenadas Manim.
    """

    return pixel_to_point(
        x_pct * PIXEL_WIDTH / 100,
        y_pct * PIXEL_HEIGHT / 100,
    )


# ============================================================
# DIMENSÕES DA ÁREA SEGURA
# ============================================================

SAFE_WIDTH_PX = SAFE_X_MAX_PX - SAFE_X_MIN_PX
SAFE_HEIGHT_PX = SAFE_Y_MAX_PX - SAFE_Y_MIN_PX

SAFE_WIDTH = SAFE_WIDTH_PX * PIXEL_TO_UNIT_X
SAFE_HEIGHT = SAFE_HEIGHT_PX * PIXEL_TO_UNIT_Y

SAFE_LEFT = SAFE_LEFT_PX / PIXEL_WIDTH * 100
SAFE_RIGHT = SAFE_RIGHT_PX / PIXEL_WIDTH * 100
SAFE_TOP = SAFE_TOP_PX / PIXEL_HEIGHT * 100
SAFE_BOTTOM = SAFE_BOTTOM_PX / PIXEL_HEIGHT * 100

SAFE_CENTER = pixel_to_point(
    (SAFE_X_MIN_PX + SAFE_X_MAX_PX) / 2,
    (SAFE_Y_MIN_PX + SAFE_Y_MAX_PX) / 2,
)

# ============================================================
# POSICIONAMENTO RELATIVO À ÁREA SEGURA
# ============================================================

def safe_point(x_pct: float, y_pct: float) -> np.ndarray:
    """
    Posiciona um ponto dentro da área segura.

    x_pct e y_pct variam de 0 a 100 e são relativos
    à área segura, não à tela inteira.
    """

    x_px = SAFE_X_MIN_PX + x_pct / 100 * SAFE_WIDTH_PX
    y_px = SAFE_Y_MIN_PX + y_pct / 100 * SAFE_HEIGHT_PX

    return pixel_to_point(x_px, y_px)


def safe_region_point(
    x_pct: float,
    y_pct: float,
    y_top_pct: float,
    y_bottom_pct: float,
) -> np.ndarray:
    """
    Posiciona um ponto em uma região vertical da área segura.

    y_top_pct e y_bottom_pct são percentuais da altura útil.
    """

    y_relative = (
        y_top_pct + y_pct / 100 * (y_bottom_pct - y_top_pct)
    )

    return safe_point(x_pct, y_relative)


# ============================================================
# CENTROS E DIMENSÕES ÚTEIS
# ============================================================

SAFE_CENTER = safe_point(50, 50)

# Regiões relativas à área segura.
HEADER_TOP = 0
HEADER_BOTTOM = 17

MAIN_TOP = 19
MAIN_BOTTOM = 76

CAPTION_TOP = 79
CAPTION_BOTTOM = 100

HEADER_CENTER = safe_region_point(
    50, 50, HEADER_TOP, HEADER_BOTTOM
)

MAIN_CENTER = safe_region_point(
    50, 50, MAIN_TOP, MAIN_BOTTOM
)

CAPTION_CENTER = safe_region_point(
    50, 50, CAPTION_TOP, CAPTION_BOTTOM
)

# Largura máxima recomendada para textos.
TEXT_MAX_WIDTH = SAFE_WIDTH * 0.95

HEADER_HEIGHT = SAFE_HEIGHT * (
    HEADER_BOTTOM - HEADER_TOP
) / 100

MAIN_HEIGHT = SAFE_HEIGHT * (
    MAIN_BOTTOM - MAIN_TOP
) / 100

CAPTION_HEIGHT = SAFE_HEIGHT * (
    CAPTION_BOTTOM - CAPTION_TOP
) / 100

# ============================================================
# GUIAS VISUAIS PARA DEBUG
# ============================================================

def safe_area_guide():
    """Mostra a área segura medida empiricamente."""

    return Rectangle(
        width=SAFE_WIDTH,
        height=SAFE_HEIGHT,
        color=GREEN,
        stroke_width=2,
        stroke_opacity=0.8,
    ).move_to(SAFE_CENTER)


def zone_guide():
    """Mostra as regiões de título, conteúdo e legenda."""

    zones = VGroup()

    definitions = [
        (HEADER_TOP, HEADER_BOTTOM, BLUE),
        (MAIN_TOP, MAIN_BOTTOM, CYAN),
        (CAPTION_TOP, CAPTION_BOTTOM, YELLOW),
    ]

    for top, bottom, color in definitions:
        rect = Rectangle(
            width=TEXT_MAX_WIDTH,
            height=SAFE_HEIGHT * (bottom - top) / 100,
            stroke_color=color,
            stroke_width=2,
            stroke_opacity=0.7,
        )

        rect.move_to(
            safe_region_point(50, 50, top, bottom)
        )

        zones.add(rect)

    return zones
