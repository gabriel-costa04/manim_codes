
import numpy as np
from manim import config, Rectangle, VGroup

from manim_codes.config.theme import (
    GREEN,
    BLUE,
    CYAN,
    YELLOW,
)

# ============================================================
# CONFIGURAÇÃO DO CANVAS
# ============================================================

config.pixel_width = 1080
config.pixel_height = 1920

config.frame_width = 9
config.frame_height = 16

FRAME_WIDTH = config.frame_width
FRAME_HEIGHT = config.frame_height

# ============================================================
# ÁREA SEGURA
# ============================================================

# Percentuais medidos a partir das bordas da tela.
# São margens conservadoras para vídeos verticais.
# Devem ser verificadas nas plataformas de destino.

SAFE_LEFT = 8
SAFE_RIGHT = 20
SAFE_TOP = 10
SAFE_BOTTOM = 18

SAFE_X_MIN = SAFE_LEFT
SAFE_X_MAX = 100 - SAFE_RIGHT

SAFE_Y_MIN = SAFE_TOP
SAFE_Y_MAX = 100 - SAFE_BOTTOM

SAFE_WIDTH = FRAME_WIDTH * (
    (SAFE_X_MAX - SAFE_X_MIN) / 100
)

SAFE_HEIGHT = FRAME_HEIGHT * (
    (SAFE_Y_MAX - SAFE_Y_MIN) / 100
)

# ============================================================
# REGIÕES DE CONTEÚDO
# ============================================================

# Percentuais verticais relativos à tela inteira.
# Os intervalos deixam pequenos espaços entre as regiões.

HEADER_TOP = 10
HEADER_BOTTOM = 21

MAIN_TOP = 23
MAIN_BOTTOM = 67

CAPTION_TOP = 70
CAPTION_BOTTOM = 82

# ============================================================
# CONVERSÃO DE COORDENADAS
# ============================================================

def pct_to_point(x_pct: float, y_pct: float) -> np.ndarray:
    """
    Converte percentuais da tela em coordenadas Manim.

    Origem percentual: canto superior esquerdo.
    (0, 0)   -> canto superior esquerdo
    (100,100)-> canto inferior direito
    """

    x = (x_pct / 100 - 0.5) * FRAME_WIDTH
    y = (0.5 - y_pct / 100) * FRAME_HEIGHT

    return np.array([x, y, 0.0])


def safe_point(x_pct: float, y_pct: float) -> np.ndarray:
    """
    Posiciona um ponto dentro da área segura.

    x_pct e y_pct variam de 0 a 100 e são relativos
    à própria área segura.
    """

    x = SAFE_X_MIN + (x_pct / 100) * (
        SAFE_X_MAX - SAFE_X_MIN
    )

    y = SAFE_Y_MIN + (y_pct / 100) * (
        SAFE_Y_MAX - SAFE_Y_MIN
    )

    return pct_to_point(x, y)


def region_point(
    x_pct: float,
    y_pct: float,
    y_top: float,
    y_bottom: float,
) -> np.ndarray:
    """
    Posiciona um ponto dentro de uma região vertical.

    x_pct: percentual horizontal relativo à tela.
    y_pct: percentual vertical relativo à região.
    """

    y = y_top + (y_pct / 100) * (y_bottom - y_top)

    return pct_to_point(x_pct, y)


# ============================================================
# CENTROS DAS REGIÕES
# ============================================================

SAFE_CENTER = safe_point(50, 50)

HEADER_CENTER = region_point(
    44, 50, HEADER_TOP, HEADER_BOTTOM
)

MAIN_CENTER = region_point(
    44, 50, MAIN_TOP, MAIN_BOTTOM
)

CAPTION_CENTER = region_point(
    44, 50, CAPTION_TOP, CAPTION_BOTTOM
)

# ============================================================
# DIMENSÕES ÚTEIS
# ============================================================

# Largura máxima recomendada para objetos de texto.
# O valor é menor que a largura da área segura para
# deixar espaço adicional nas laterais.

TEXT_MAX_WIDTH = SAFE_WIDTH * 0.95

# Altura aproximada disponível em cada região.

HEADER_HEIGHT = FRAME_HEIGHT * (
    (HEADER_BOTTOM - HEADER_TOP) / 100
)

MAIN_HEIGHT = FRAME_HEIGHT * (
    (MAIN_BOTTOM - MAIN_TOP) / 100
)

CAPTION_HEIGHT = FRAME_HEIGHT * (
    (CAPTION_BOTTOM - CAPTION_TOP) / 100
)

# ============================================================
# GUIAS VISUAIS PARA DEBUG
# ============================================================

def safe_area_guide():
    """Retângulo que delimita a área segura."""

    center = pct_to_point(
        (SAFE_X_MIN + SAFE_X_MAX) / 2,
        (SAFE_Y_MIN + SAFE_Y_MAX) / 2,
    )

    return Rectangle(
        width=SAFE_WIDTH,
        height=SAFE_HEIGHT,
        color=GREEN,
        stroke_width=2,
        stroke_opacity=0.7,
    ).move_to(center)


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
            height=FRAME_HEIGHT * (bottom - top) / 100,
            stroke_color=color,
            stroke_width=2,
            stroke_opacity=0.7,
        )

        rect.move_to(
            pct_to_point(
                (SAFE_X_MIN + SAFE_X_MAX) / 2,
                (top + bottom) / 2,
            )
        )

        zones.add(rect)

    return zones
