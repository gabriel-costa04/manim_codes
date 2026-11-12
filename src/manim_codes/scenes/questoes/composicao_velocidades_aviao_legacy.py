from manim import *

# Importando as cores do tema
from manim_codes.config.theme import BACKGROUND, BLUE, GREEN, IVORY, ORANGE

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

    def construct(self):

        # ----------------------------------------------------
        # SISTEMA DE COORDENADAS
        # ----------------------------------------------------

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.82
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

        # Conversão dos valores físicos para coordenadas visuais.
        # O eixo Z possui escala ampliada para melhorar a leitura.

        def point(x, y, z):
            return self.axes.c2p(
                x * SCALE_XY,
                y * SCALE_XY,
                z * SCALE_Z
            )

        self.point = point

        # ----------------------------------------------------
        # ELEMENTOS AUXILIARES
        # ----------------------------------------------------

        def make_vector(start, end, color, thickness=0.035):

            return Arrow3D(
                start=start,
                end=end,
                color=color,
                thickness=thickness,
            )

        def caption(text, size=32):

            return Text(
                text,
                font_size=size,
                color=IVORY,
                weight=BOLD,
            ).to_edge(UP, buff=0.65)

        def equation(tex, size=35):

            return MathTex(
                tex,
                font_size=size,
                color=IVORY,
            )

        def show_caption(text, size=32):

            new_caption = caption(text, size)

            self.add_fixed_in_frame_mobjects(new_caption)

            self.play(
                FadeIn(new_caption),
                run_time=0.5
            )

            return new_caption

        def hide_caption(obj):

            self.play(
                FadeOut(obj),
                run_time=0.35
            )

        # ====================================================
        # CENA 1 — O PROBLEMA: AVIÃO E VENTO
        # TEMPO APROXIMADO: 0–6 s
        # ====================================================

        self.play(
            Create(self.axes),
            run_time=1.5
        )

        # Identificação dos eixos

        axis_labels = VGroup(
            Text("LESTE", font_size=22, color=IVORY)
                .move_to(self.axes.c2p(4.3, 0, 0) + RIGHT * 0.2),

            Text("NORTE", font_size=22, color=IVORY)
                .move_to(self.axes.c2p(0, 4.3, 0) + UP * 0.2),

            Text("ALTITUDE", font_size=22, color=IVORY)
                .move_to(self.axes.c2p(0, 0, 2.2) + RIGHT * 0.4),
        )

        self.play(
            FadeIn(axis_labels),
            run_time=0.8
        )

        # Representação simplificada do avião

        plane = Arrow3D(
            start=self.axes.c2p(0, 0, 0.3),
            end=self.axes.c2p(0.7, 0.7, 0.3),
            color=IVORY,
            thickness=0.06,
        )

        self.play(
            FadeIn(plane),
            run_time=0.8
        )

        # Partículas representando o vento

        wind_particles = VGroup()

        for i in range(5):

            particle = Sphere(
                radius=0.045,
                color=ORANGE,
                resolution=(8, 8),
            )

            particle.move_to(
                point(-0.4 + i * 0.12, 0.8 - i * 0.1, 0.5)
            )

            wind_particles.add(particle)

        self.play(
            FadeIn(wind_particles),
            run_time=0.5
        )

        title = show_caption(
            "Como chegar ao destino apesar do vento?",
            size=29
        )

        self.wait(1)

        hide_caption(title)

        # ====================================================
        # CENA 2 — TRAJETÓRIA DESEJADA
        # TEMPO APROXIMADO: 6–15 s
        # ====================================================

        self.move_camera(
            phi=65 * DEGREES,
            theta=-55 * DEGREES,
            zoom=0.95,
            run_time=1.5
        )

        title = show_caption("A trajetória desejada")

        # Deslocamento total

        destination = self.axes.c2p(3.6, 3.6, 1.5)

        displacement = Arrow3D(
            start=self.origin,
            end=destination,
            color=IVORY,
            thickness=0.04,
        )

        self.play(
            FadeIn(displacement),
            run_time=1.5
        )

        # Componentes do deslocamento

        p_x = self.axes.c2p(3.6, 0, 0)
        p_xy = self.axes.c2p(3.6, 3.6, 0)
        component_x = DashedLine(
            self.origin,
            p_x,
            color=BLUE,
            stroke_width=4,
        )

        component_y = DashedLine(
            p_x,
            p_xy,
            color=GREEN,
            stroke_width=4,
        )

        component_z = DashedLine(
            p_xy,
            destination,
            color=ORANGE,
            stroke_width=4,
        )

        self.play(
            Create(component_x),
            Create(component_y),
            Create(component_z),
            run_time=1.8
        )

        # Distâncias e tempo

        distances = VGroup(
            Text("20 km Leste", font_size=24, color=BLUE),
            Text("20 km Norte", font_size=24, color=GREEN),
            Text("1 km acima", font_size=24, color=ORANGE),
        )

        distances.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        distances.to_edge(DOWN, buff=2.1)

        self.add_fixed_in_frame_mobjects(distances)

        time_label = Text(
            "Tempo disponível: 6 minutos",
            font_size=27,
            color=IVORY,
            weight=BOLD,
        ).to_edge(DOWN, buff=1.1)

        self.add_fixed_in_frame_mobjects(time_label)

        self.play(
            FadeIn(distances),
            FadeIn(time_label),
            run_time=0.8
        )

        self.wait(1)

        hide_caption(title)

        # ====================================================
        # CENA 3 — VELOCIDADE DESEJADA
        # TEMPO APROXIMADO: 15–25 s
        # ====================================================

        self.play(
            FadeOut(displacement),
            FadeOut(component_x),
            FadeOut(component_y),
            FadeOut(component_z),
            run_time=0.5
        )

        self.play(
            FadeOut(distances),
            FadeOut(time_label),
            run_time=0.4
        )

        title = show_caption("Calculando a velocidade desejada")

        formula = equation(
            r"\vec v_{\mathrm{solo}}="
            r"\frac{\Delta\vec r}{\Delta t}",
            size=38
        )

        formula.to_edge(DOWN, buff=1.5)

        self.add_fixed_in_frame_mobjects(formula)

        self.play(
            Write(formula),
            run_time=1
        )

        conversion = equation(
            r"6\ \mathrm{min}=0{,}1\ \mathrm{h}",
            size=36
        )

        conversion.next_to(formula, UP, buff=0.5)

        self.add_fixed_in_frame_mobjects(conversion)

        self.play(
            Write(conversion),
            run_time=0.8
        )

        # Componentes da velocidade

        components = VGroup(
            equation(r"v_x=\frac{20}{0{,}1}=200", size=32),
            equation(r"v_y=\frac{20}{0{,}1}=200", size=32),
            equation(r"v_z=\frac{1}{0{,}1}=10", size=32),
        )

        components.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25
        )

        components.move_to(ORIGIN)

        self.add_fixed_in_frame_mobjects(components)

        self.play(
            FadeIn(components),
            run_time=1
        )

        self.wait(0.8)

        self.play(
            FadeOut(formula),
            FadeOut(conversion),
            FadeOut(components),
            run_time=0.5
        )

        # Vetor da velocidade desejada

        ground_velocity = (200, 200, 10)

        ground_arrow = make_vector(
            self.origin,
            point(*ground_velocity),
            BLUE
        )

        self.play(
            FadeIn(ground_arrow),
            run_time=1.5
        )

        ground_result = equation(
            r"\vec v_{\mathrm{aviao/solo}}="
            r"(200,\ 200,\ 10)\ \mathrm{km/h}",
            size=31
        )

        ground_result.to_edge(DOWN, buff=1.2)

        self.add_fixed_in_frame_mobjects(ground_result)

        self.play(
            Write(ground_result),
            run_time=0.8
        )

        self.wait(0.5)

        hide_caption(title)

        # ====================================================
        # CENA 4 — O VETOR DO VENTO
        # TEMPO APROXIMADO: 25–37 s
        # ====================================================

        title = show_caption("O vento também possui velocidade")

        wind_velocity = (30, -20, -1)

        wind_arrow = make_vector(
            self.origin,
            point(*wind_velocity),
            ORANGE
        )

        self.play(
            FadeIn(wind_arrow),
            run_time=1.2
        )

        wind_formula = equation(
            r"\vec v_{\mathrm{ar/solo}}="
            r"(30,\ -20,\ -1)\ \mathrm{km/h}",
            size=32
        )

        wind_formula.to_edge(DOWN, buff=1.2)

        self.add_fixed_in_frame_mobjects(wind_formula)

        self.play(
            Write(wind_formula),
            run_time=0.8
        )

        # Componentes do vento

        wind_components = VGroup(
            equation(r"+30\ \mathrm{km/h}\quad\mathrm{Leste}", size=27),
            equation(r"-20\ \mathrm{km/h}\quad\mathrm{Sul}", size=27),
            equation(r"-1\ \mathrm{km/h}\quad\mathrm{Baixo}", size=27),
        )

        wind_components.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.2
        )

        wind_components.move_to(ORIGIN)

        self.add_fixed_in_frame_mobjects(wind_components)

        self.play(
            FadeIn(wind_components),
            run_time=0.8
        )

        self.wait(0.8)

        self.play(
            FadeOut(wind_components),
            FadeOut(wind_formula),
            run_time=0.5
        )

        self.wait(0.5)

        hide_caption(title)

        # ====================================================
        # CENA 5 — COMPOSIÇÃO VETORIAL
        # TEMPO APROXIMADO: 37–50 s
        # ====================================================

        title = show_caption("Compensando a ação do vento")

        # Equação inicial

        equation_sum = equation(
            r"\vec v_{\mathrm{solo}}="
            r"\vec v_{\mathrm{aviao/ar}}+"
            r"\vec v_{\mathrm{ar/solo}}",
            size=31
        )

        equation_sum.to_edge(DOWN, buff=1.2)

        self.add_fixed_in_frame_mobjects(equation_sum)

        self.play(
            Write(equation_sum),
            run_time=1
        )

        self.wait(0.7)

        equation_sub = equation(
            r"\vec v_{\mathrm{aviao/ar}}="
            r"\vec v_{\mathrm{solo}}-"
            r"\vec v_{\mathrm{ar/solo}}",
            size=31
        )

        equation_sub.move_to(equation_sum)

        self.play(
            Transform(equation_sum, equation_sub),
            run_time=1
        )

        # Resultado matemático

        air_velocity = (170, 220, 11)

        calculations = VGroup(
            equation(r"v_x=200-30=170", size=31),
            equation(r"v_y=200-(-20)=220", size=31),
            equation(r"v_z=10-(-1)=11", size=31),
        )

        calculations.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25
        )

        calculations.move_to(ORIGIN)

        self.add_fixed_in_frame_mobjects(calculations)

        self.play(
            FadeIn(calculations),
            run_time=1
        )

        self.wait(1)

        self.play(
            FadeOut(calculations),
            FadeOut(equation_sum),
            run_time=0.5
        )

        # ----------------------------------------------------
        # COMPOSIÇÃO PONTA-COM-CAUDA
        # ----------------------------------------------------

        # Vetor verde: velocidade do avião em relação ao ar

        air_arrow = make_vector(
            self.origin,
            point(*air_velocity),
            GREEN,
            thickness=0.045
        )

        self.play(
            FadeIn(air_arrow),
            run_time=1.2
        )

        # Transladar o vetor do vento para a ponta do vetor verde.
        # Assim, a soma ponta-com-cauda termina na ponta do vetor azul.

        wind_translated = make_vector(
            point(*air_velocity),
            point(*ground_velocity),
            ORANGE,
            thickness=0.045
        )

        self.play(
            FadeIn(wind_translated),
            run_time=1.2
        )

        self.wait(0.8)

        # ----------------------------------------------------
        # CENA 6 — RESPOSTA
        # TEMPO APROXIMADO: 50–60 s
        # ----------------------------------------------------

        hide_caption(title)

        # Fórmula final

        final_result = equation(
            r"\boxed{\vec v_{\mathrm{aviao/ar}}="
            r"(170,\ 220,\ 11)\ \mathrm{km/h}}",
            size=34
        )

        final_result.to_edge(DOWN, buff=1.5)

        self.add_fixed_in_frame_mobjects(final_result)

        self.play(
            Write(final_result),
            run_time=1.2
        )

        alternative = Text(
            "ALTERNATIVA D",
            font_size=42,
            color=GREEN,
            weight=BOLD,
        )

        alternative.to_edge(DOWN, buff=0.5)

        self.add_fixed_in_frame_mobjects(alternative)

        self.play(
            FadeIn(alternative, scale=1.2),
            run_time=0.8
        )

        # Aproximação final da câmera

        self.move_camera(
            zoom=1.05,
            run_time=1.5
        )

        self.wait(1.5)