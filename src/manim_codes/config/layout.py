import warnings

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
# LIMITES FÍSICOS DA ÁREA SEGURA (VALORES OFICIAIS)
# ============================================================

SAFE_LEFT_PX = 0
SAFE_RIGHT_PX = 120
SAFE_TOP_PX = 220
SAFE_BOTTOM_PX = 120 #420

SAFE_X_MIN_PX = SAFE_LEFT_PX
SAFE_X_MAX_PX = PIXEL_WIDTH - SAFE_RIGHT_PX

SAFE_Y_MIN_PX = SAFE_TOP_PX
SAFE_Y_MAX_PX = PIXEL_HEIGHT - SAFE_BOTTOM_PX

# ============================================================
# MARGEM INTERNA DA ÁREA DE CONTEÚDO
# ============================================================
# A área de conteúdo adiciona uma folga visual extra dentro da área
# segura para que textos e equações não fiquem colados às bordas.

CONTENT_MARGIN_LEFT_PX = 40
CONTENT_MARGIN_RIGHT_PX = 0 #40
CONTENT_MARGIN_TOP_PX = 30
CONTENT_MARGIN_BOTTOM_PX = 40

CONTENT_X_MIN_PX = SAFE_X_MIN_PX + CONTENT_MARGIN_LEFT_PX
CONTENT_X_MAX_PX = SAFE_X_MAX_PX - CONTENT_MARGIN_RIGHT_PX
CONTENT_Y_MIN_PX = SAFE_Y_MIN_PX + CONTENT_MARGIN_TOP_PX
CONTENT_Y_MAX_PX = SAFE_Y_MAX_PX - CONTENT_MARGIN_BOTTOM_PX

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


def point_to_pixel(point: np.ndarray) -> np.ndarray:
    """Converte um ponto Manim para coordenadas em pixels."""

    x_px = (point[0] / FRAME_WIDTH + 0.5) * PIXEL_WIDTH
    y_px = (0.5 - point[1] / FRAME_HEIGHT) * PIXEL_HEIGHT

    return np.array([x_px, y_px, 0.0])


def pct_to_point(x_pct: float, y_pct: float) -> np.ndarray:
    """Converte percentuais da tela inteira para coordenadas Manim."""

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

CONTENT_WIDTH_PX = CONTENT_X_MAX_PX - CONTENT_X_MIN_PX
CONTENT_HEIGHT_PX = CONTENT_Y_MAX_PX - CONTENT_Y_MIN_PX

CONTENT_WIDTH = CONTENT_WIDTH_PX * PIXEL_TO_UNIT_X
CONTENT_HEIGHT = CONTENT_HEIGHT_PX * PIXEL_TO_UNIT_Y

CONTENT_CENTER = pixel_to_point(
    (CONTENT_X_MIN_PX + CONTENT_X_MAX_PX) / 2,
    (CONTENT_Y_MIN_PX + CONTENT_Y_MAX_PX) / 2,
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

    y_relative = y_top_pct + y_pct / 100 * (y_bottom_pct - y_top_pct)

    return safe_point(x_pct, y_relative)


def content_point(x_pct: float, y_pct: float) -> np.ndarray:
    """Posiciona um ponto dentro da área de conteúdo, com margem interna."""

    x_px = CONTENT_X_MIN_PX + x_pct / 100 * CONTENT_WIDTH_PX
    y_px = CONTENT_Y_MIN_PX + y_pct / 100 * CONTENT_HEIGHT_PX

    return pixel_to_point(x_px, y_px)


# ============================================================
# VALIDAÇÃO E POSICIONAMENTO COM BOUNDING BOX
# ============================================================

def object_bounds_px(mobj):
    """Retorna os limites do objeto em pixels: left, right, bottom, top."""

    if not hasattr(mobj, "get_left") or not hasattr(mobj, "get_right"):
        raise TypeError(f"Objeto '{type(mobj).__name__}' não possui bounding box legível.")

    left = point_to_pixel(mobj.get_left())[0]
    right = point_to_pixel(mobj.get_right())[0]
    bottom = point_to_pixel(mobj.get_bottom())[1]
    top = point_to_pixel(mobj.get_top())[1]

    return left, right, bottom, top


def validate_object_in_area(mobj, *, area: str = "content", padding: float = 0, warn: bool = True) -> bool:
    """
    Verifica se o bounding box inteiro do objeto permanece dentro da área permitida.

    area='safe' usa os limites físicos oficiais.
    area='content' usa a área de conteúdo com margem adicional.
    """

    if area == "safe":
        x_min_px, x_max_px = SAFE_X_MIN_PX + padding, SAFE_X_MAX_PX - padding
        y_min_px, y_max_px = SAFE_Y_MIN_PX + padding, SAFE_Y_MAX_PX - padding
    elif area == "content":
        x_min_px, x_max_px = CONTENT_X_MIN_PX + padding, CONTENT_X_MAX_PX - padding
        y_min_px, y_max_px = CONTENT_Y_MIN_PX + padding, CONTENT_Y_MAX_PX - padding
    else:
        raise ValueError("area deve ser 'safe' ou 'content'.")

    left, right, bottom, top = object_bounds_px(mobj)
    inside = left >= x_min_px and right <= x_max_px and bottom >= y_min_px and top <= y_max_px

    if not inside and warn:
        warnings.warn(
            f"Objeto {type(mobj).__name__} está fora da área {area}. "
            f"Bounds: left={left:.1f}, right={right:.1f}, bottom={bottom:.1f}, top={top:.1f}; "
            f"Limites: x=[{x_min_px:.1f}, {x_max_px:.1f}], y=[{y_min_px:.1f}, {y_max_px:.1f}]",
            stacklevel=2,
        )

    return inside


def place_in_safe_area(mobj, x_pct: float = 50, y_pct: float = 50, *, area: str = "content", padding: float = 0, warn: bool = True):
    """
    Posiciona um objeto considerando a sua bounding box e mantém o objeto inteiro dentro da área especificada.

    x_pct e y_pct são percentuais relativos à área escolhida.
    """

    if area == "safe":
        x_min_px, x_max_px = SAFE_X_MIN_PX + padding, SAFE_X_MAX_PX - padding
        y_min_px, y_max_px = SAFE_Y_MIN_PX + padding, SAFE_Y_MAX_PX - padding
    elif area == "content":
        x_min_px, x_max_px = CONTENT_X_MIN_PX + padding, CONTENT_X_MAX_PX - padding
        y_min_px, y_max_px = CONTENT_Y_MIN_PX + padding, CONTENT_Y_MAX_PX - padding
    else:
        raise ValueError("area deve ser 'safe' ou 'content'.")

    target_x_px = x_min_px + x_pct / 100 * (x_max_px - x_min_px)
    target_y_px = y_min_px + y_pct / 100 * (y_max_px - y_min_px)
    target_point = pixel_to_point(target_x_px, target_y_px)

    mobj.move_to(target_point)

    left, right, bottom, top = object_bounds_px(mobj)
    shift_x = 0.0
    shift_y = 0.0

    if left < x_min_px:
        shift_x = x_min_px - left
    elif right > x_max_px:
        shift_x = x_max_px - right

    if bottom < y_min_px:
        shift_y = y_min_px - bottom
    elif top > y_max_px:
        shift_y = y_max_px - top

    if shift_x or shift_y:
        mobj.shift(
            np.array([
                shift_x * PIXEL_TO_UNIT_X,
                -shift_y * PIXEL_TO_UNIT_Y,
                0.0,
            ])
        )

    if warn:
        validate_object_in_area(mobj, area=area, padding=padding, warn=True)

    return mobj


# ============================================================
# CENTROS E DIMENSÕES ÚTEIS
# ============================================================

SAFE_CENTER = safe_point(50, 50)
CONTENT_CENTER = content_point(50, 50)

# Regiões relativas à área segura.
HEADER_TOP = 0
HEADER_BOTTOM = 17

MAIN_TOP = 19
MAIN_BOTTOM = 76

CAPTION_TOP = 79
CAPTION_BOTTOM = 100

HEADER_CENTER = safe_region_point(50, 50, HEADER_TOP, HEADER_BOTTOM)
MAIN_CENTER = safe_region_point(50, 50, MAIN_TOP, MAIN_BOTTOM)
CAPTION_CENTER = safe_region_point(50, 50, CAPTION_TOP, CAPTION_BOTTOM)

# Largura máxima recomendada para textos.
TEXT_MAX_WIDTH = CONTENT_WIDTH * 0.95

HEADER_HEIGHT = SAFE_HEIGHT * (HEADER_BOTTOM - HEADER_TOP) / 100
MAIN_HEIGHT = SAFE_HEIGHT * (MAIN_BOTTOM - MAIN_TOP) / 100
CAPTION_HEIGHT = SAFE_HEIGHT * (CAPTION_BOTTOM - CAPTION_TOP) / 100

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


def content_area_guide():
    """Mostra a área de conteúdo com margem interna adicional."""

    return Rectangle(
        width=CONTENT_WIDTH,
        height=CONTENT_HEIGHT,
        color=BLUE,
        stroke_width=2,
        stroke_opacity=0.8,
    ).move_to(CONTENT_CENTER)


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

        rect.move_to(safe_region_point(50, 50, top, bottom))
        zones.add(rect)

    return zones
