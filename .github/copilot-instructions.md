# Projeto Dois Físicos e um Vetor — Instruções para o Copilot

## 1. Objetivo do projeto

Este projeto reúne códigos reutilizáveis para produzir animações científicas destinadas ao canal **Dois Físicos e um Vetor**.

Os vídeos têm duas aplicações principais:

- Divulgação científica: explicações visuais de conceitos de física, astronomia e matemática.
- Resolução de questões: explicações didáticas de questões do ENEM e outros exames.

O objetivo é produzir animações visualmente claras, cientificamente corretas, bem organizadas e adequadas principalmente a vídeos verticais curtos.

Ao escrever ou modificar qualquer código, priorize a clareza visual, a precisão científica, a legibilidade e a reutilização de componentes.

---

## 2. Tecnologias e ambiente

- Python 3.10 ou superior.
- Python utilizado atualmente no ambiente: 3.10.12.
- Manim Community Edition (Manim CE), versão 0.19.1.
- NumPy.
- FFmpeg.
- LaTeX, para renderização de expressões matemáticas.
- Gerenciador de ambiente e dependências: `uv`.

### Regras

- Usar exclusivamente Manim Community Edition, nunca ManimGL.
- Não utilizar APIs inexistentes ou incompatíveis com a versão instalada.
- Antes de sugerir funcionalidades específicas, verificar sua compatibilidade com Manim CE 0.19.1.
- Não atualizar dependências ou versões sem necessidade.
- Não modificar `pyproject.toml`, `uv.lock` ou `.python-version` sem justificativa.
- Executar os comandos pelo ambiente do projeto, preferencialmente com `uv run`.
- Evitar dependências externas quando o próprio Manim ou Python já oferecem a funcionalidade necessária.

---

## 3. Formato e configuração dos vídeos

### Formato padrão

Os vídeos devem ser produzidos prioritariamente no formato vertical 9:16.

- Resolução: 1080 × 1920 pixels.
- `config.pixel_width = 1080`
- `config.pixel_height = 1920`
- `config.frame_width = 9`
- `config.frame_height = 16`

A configuração do canvas deve estar centralizada em:

`src/manim_codes/config/layout.py`

Não repetir configurações de resolução e dimensões do frame em cada arquivo de animação, exceto quando houver uma necessidade específica e documentada.

A configuração global deve ser importada de `layout.py`.

Não assumir que o formato horizontal 16:9 é o padrão. Caso um vídeo exija outro formato, a alteração deve ser explícita e isolada.

---

## 4. Identidade visual

A identidade visual deve seguir a paleta institucional do canal, definida em:

`src/manim_codes/config/theme.py`

### Cores institucionais

- Roxo: `PURPLE = "#1D0055"`
- Creme: `IVORY = "#FEFAF1"`
- Preto/carvão: `BACKGROUND = "#1B1B1B"`

### Cores complementares

- Ciano: `CYAN = "#43BCCD"`
- Laranja: `ORANGE = "#F28C45"`
- Amarelo: `YELLOW = "#F2C94C"`
- Coral: `CORAL = "#E87970"`
- Azul: `BLUE = "#8195D6"`

### Cores semânticas

- Verde: `GREEN = "#83D99A"`
- Vermelho: `RED = "#E87970"`

### Cores de interface

- Texto principal: `TEXT_PRIMARY = IVORY`
- Texto secundário: `TEXT_SECONDARY = "#B8B5C0"`
- Eixos: `AXIS = "#A6A1AD"`
- Grades: `GRID = "#494550"`

### Convenções obrigatórias

1. Utilizar `BACKGROUND` como fundo padrão.
2. Utilizar `IVORY` para textos, títulos e equações principais.
3. Utilizar `TEXT_SECONDARY` para informações secundárias, unidades, observações e legendas auxiliares.
4. Utilizar `YELLOW` para resultados, números e informações de maior destaque.
5. Utilizar `CYAN`, `ORANGE`, `BLUE` e `GREEN` para distinguir grandezas físicas, vetores, curvas e componentes de diagramas.
6. Utilizar `AXIS` e `GRID` para eixos cartesianos, grades e linhas auxiliares.
7. Utilizar `RED` para alertas, erros e resultados negativos.

### Separação entre cores de texto e cores de diagramas

Não utilizar indiscriminadamente as mesmas cores para textos, vetores e eixos.

A cor de um vetor deve identificar a grandeza física representada. A cor de um eixo deve identificar a estrutura de referência do sistema de coordenadas.

Portanto:

- Eixos devem ser discretos, preferencialmente em `AXIS`.
- Grades devem ser ainda mais discretas, em `GRID`.
- Vetores devem utilizar cores de destaque.
- Textos explicativos devem permanecer predominantemente em `IVORY`.
- Informações secundárias devem utilizar `TEXT_SECONDARY`.
- Resultados importantes podem utilizar `YELLOW`.

Não colorir uma equação inteira com a cor de um vetor apenas porque a equação descreve aquele vetor. Quando necessário, destacar somente o símbolo ou termo correspondente.

Evitar excesso de cores simultâneas. A cor deve comunicar informação, e não funcionar apenas como decoração.

---

## 5. Layout e zonas seguras

O layout padrão dos vídeos verticais utiliza medidas de margens empiricamente verificadas em uma tela de 1080 × 1920 pixels.

Essas medidas são obrigatórias e estão centralizadas em `src/manim_codes/config/layout.py`.

### Margens proibidas

- Superior: 220 px (Y: 0–220).
- Inferior: 420 px (Y: 1500–1920).
- Direita: 120 px (X: 960–1080).
- Esquerda: 0 px (X: 0).

### Área segura

- Largura: 960 px.
- Altura: 1280 px.
- Limites horizontais: X = 0–960 px.
- Limites verticais: Y = 220–1500 px.

A área segura é assimétrica: começa na borda esquerda e não deve ser centralizada horizontalmente no frame inteiro.

### Regras obrigatórias

1. Não posicionar informações essenciais fora da área segura.
2. Não reservar margem esquerda adicional sem uma necessidade específica.
3. Não utilizar os antigos valores de margens percentuais como referência.
4. Utilizar `safe_point()` para posicionar elementos dentro da área segura.
5. Utilizar `safe_region_point()` para distribuir elementos entre as regiões de título, conteúdo e legenda.
6. Verificar a caixa delimitadora completa dos objetos, não apenas seus centros.
7. Textos, equações e títulos devem respeitar `TEXT_MAX_WIDTH`.
8. Não utilizar `to_edge(UP)` ou `to_edge(DOWN)` como substitutos do posicionamento na área segura.
9. Conferir o vídeo renderizado na resolução final.
10. Tratar essas margens como limites de segurança, e não como recomendação para ocupar toda a área disponível.

### Organização interna da área segura

Distribuir os elementos em três regiões:

- Cabeçalho: 0–17% da altura útil.
- Conteúdo principal: 19–76% da altura útil.
- Legendas e informações auxiliares: 79–100% da altura útil.

Manter espaços entre as regiões e evitar sobreposição.

A área segura deve ser utilizada como referência para todas as animações verticais, inclusive cenas tridimensionais com textos fixos na tela.

---

## 6. Hierarquia visual e tipografia

Toda animação deve possuir uma hierarquia visual clara.

Ordem de prioridade:

1. Informação principal ou fenômeno físico.
2. Título ou pergunta que contextualiza a animação.
3. Equações e resultados.
4. Legendas e explicações secundárias.
5. Elementos auxiliares, grades e eixos.

Não utilizar o mesmo tamanho, peso e destaque para todos os elementos.

### Regras

- Títulos devem ser claramente identificáveis.
- Equações principais devem ser legíveis em telas pequenas.
- Textos auxiliares não devem competir com a animação.
- Evitar blocos longos de texto.
- Evitar excesso de informações simultâneas.
- Manter consistência de fontes e tamanhos ao longo do vídeo.
- Utilizar negrito com moderação.
- Conferir se os caracteres matemáticos e símbolos estão sendo renderizados corretamente.

Quando necessário, utilizar `scale_to_fit_width()` para impedir que textos ultrapassem a largura disponível.

Entretanto, não reduzir automaticamente textos a tamanhos muito pequenos. Se um texto não couber, reorganizar o layout ou dividir a informação.

---

## 7. Cenas tridimensionais

Cenas que utilizam `ThreeDScene` exigem atenção especial ao posicionamento dos elementos.

### Elementos tridimensionais

Vetores, eixos, objetos físicos e trajetórias devem pertencer ao espaço tridimensional e acompanhar a câmera.

### Elementos fixos na tela

Títulos, legendas, equações e informações que não devem acompanhar a rotação da câmera devem ser adicionados com:

`self.add_fixed_in_frame_mobjects()`

Esses elementos devem ser posicionados de acordo com as regiões seguras definidas em `layout.py`.

### Regras

- Não misturar coordenadas do espaço 3D com coordenadas fixas da tela sem compreender a diferença.
- Não presumir que objetos posicionados em coordenadas tridimensionais permanecerão visualmente na mesma posição após movimentos de câmera.
- Evitar que rótulos de eixos fiquem cortados ou sobrepostos após a projeção.
- Conferir o resultado após cada mudança significativa de `phi`, `theta` ou `zoom`.
- Evitar que títulos e fórmulas cubram a região principal do diagrama.
- Preferir textos fixos na tela para informações que precisam permanecer legíveis durante rotações.
- Conferir a sobreposição entre objetos fixos e objetos tridimensionais em diferentes ângulos de câmera.

---

## 8. Organização do código

O projeto deve manter uma arquitetura modular, evitando arquivos excessivamente grandes e código duplicado.

Estrutura principal:

- `config/`: identidade visual, layout e tipografia.
- `components/`: objetos e elementos visuais reutilizáveis.
- `scenes/`: animações e vídeos.
- `utils/`: funções auxiliares genéricas.

### Configuração

Manter as configurações em arquivos separados:

- `theme.py`: cores e identidade visual.
- `layout.py`: canvas, margens, regiões e posicionamento.
- `typography.py`: convenções de tipografia, caso sejam necessárias.

### Componentes

Criar componentes reutilizáveis quando houver repetição real de elementos.

Exemplos:

- Equações e expressões matemáticas.
- Sistemas de coordenadas.
- Vetores e diagramas.
- Gráficos.
- Elementos de física.
- Textos e legendas.

Não criar abstrações desnecessárias para elementos utilizados uma única vez.

### Cenas

Cada vídeo deve ter sua própria pasta dentro da categoria correspondente.

Exemplo:

`src/manim_codes/scenes/questoes/composicao_velocidades_aviao/`

Os arquivos de um vídeo podem ser organizados em:

- `main.py`: classe principal de renderização.
- `scene_01_intro.py`: introdução.
- `scene_02_conceitos.py`: apresentação dos conceitos.
- `scene_03_resolucao.py`: desenvolvimento da solução.
- `scene_04_conclusao.py`: conclusão.

### Organização das cenas narrativas

Como padrão, utilizar uma única classe `Scene` ou `ThreeDScene` principal para cada vídeo.

As partes narrativas devem ser organizadas em funções Python separadas, que recebem o objeto `scene` como argumento.

Isso permite:

- Preservar objetos entre partes do vídeo.
- Criar transições contínuas.
- Evitar cortes desnecessários.
- Renderizar o vídeo como uma única sequência.

Cada função deve deixar explícito quais objetos adiciona, remove ou mantém para a próxima parte.

Utilizar classes `Scene` independentes quando houver uma razão concreta para renderizar e editar os segmentos separadamente.

---

## 9. Diretrizes matemáticas e científicas

A precisão científica é obrigatória.

Antes de implementar uma animação:

1. Interpretar corretamente o fenômeno ou problema.
2. Identificar os conceitos físicos envolvidos.
3. Conferir as equações utilizadas.
4. Verificar unidades e conversões.
5. Identificar claramente os dados fornecidos e as incógnitas.
6. Conferir os cálculos numéricos.
7. Verificar se a representação visual corresponde à interpretação física.

### Equações

- Não alterar unidades sem justificativa.
- Não omitir fatores ou constantes relevantes.
- Utilizar notação matemática consistente.
- Evitar simplificações que alterem o significado físico.
- Não apresentar resultados intermediários como resultados finais.
- Conferir sinais, direções e sentidos de vetores.
- Diferenciar claramente escala física e escala visual.

### Diagramas e gráficos

- Os eixos devem ter identificação quando necessário.
- Vetores devem ter direção, sentido e magnitude coerentes.
- As escalas visuais devem ser documentadas quando não forem proporcionais às grandezas físicas.
- Não representar relações quantitativas de forma enganosa.
- Evitar gráficos sem unidades ou sem identificação adequada.

Se houver uma inconsistência no enunciado ou na interpretação física, apontá-la antes de produzir a animação.

---

## 10. Diretrizes de animação

As animações devem ser progressivas e didáticas.

- Introduzir elementos conforme eles se tornam relevantes.
- Evitar colocar todos os objetos simultaneamente na tela.
- Utilizar transições coerentes com a narrativa.
- Evitar movimentos excessivamente rápidos.
- Não utilizar efeitos apenas por estética quando prejudicarem a compreensão.
- Garantir que o espectador tenha tempo para interpretar equações e resultados.
- Utilizar `FadeIn`, `FadeOut`, `Create`, `Write`, `Transform` e outras animações conforme a função narrativa.
- Evitar transições abruptas quando os elementos deveriam estar conectados conceitualmente.

Cada movimento deve ter uma finalidade didática.

---

## 11. Uso de recursos externos

Arquivos de imagem, áudio, fontes, SVGs e outros recursos devem ficar organizados em `assets/`.

Evitar caminhos absolutos que dependam de uma máquina específica.

Preferir caminhos relativos ao projeto, construídos de maneira robusta com `pathlib`.

Não presumir que um arquivo externo existe. Verificar sua presença antes de utilizá-lo.

---

## 12. Fluxo obrigatório de trabalho

Para cada novo vídeo ou animação, seguir este processo:

### Etapa 1 — Análise

- Interpretar o problema ou fenômeno.
- Verificar a correção científica.
- Identificar os elementos que precisam ser representados.

### Etapa 2 — Planejamento visual

- Definir a narrativa.
- Dividir a animação em partes.
- Determinar quais elementos aparecem em cada momento.
- Planejar a posição dos títulos, diagramas, equações e legendas.
- Definir a função das cores.

### Etapa 3 — Implementação

- Reutilizar configurações e componentes existentes.
- Manter o código modular.
- Evitar duplicação.
- Respeitar as regiões seguras.
- Utilizar a identidade visual do projeto.

### Etapa 4 — Renderização preliminar

Renderizar em qualidade baixa ou intermediária para verificar rapidamente o funcionamento.

Utilizar comandos compatíveis com Manim CE 0.19.1.

### Etapa 5 — Inspeção obrigatória

Assistir ao vídeo renderizado, não apenas verificar se o código executou.

Conferir:

- Textos muito altos ou muito baixos.
- Elementos próximos das margens.
- Sobreposição de textos, vetores, eixos e diagramas.
- Legibilidade das equações.
- Hierarquia visual.
- Contraste entre textos e fundo.
- Uso correto das cores.
- Consistência dos tamanhos de fonte.
- Cortes de objetos.
- Movimentos de câmera.
- Transições.
- Ritmo da animação.
- Correção física e matemática.

### Etapa 6 — Correção

Corrigir todos os problemas identificados.

Não considerar uma animação concluída apenas porque o código foi executado sem erros.

### Etapa 7 — Renderização final

Somente após a inspeção e correção, produzir a versão final na resolução e qualidade desejadas.

---

## 13. Checklist obrigatório antes de finalizar

Antes de considerar qualquer animação pronta, verificar:

### Visual

- [ ] Todos os textos estão dentro das regiões seguras.
- [ ] Nenhum texto está excessivamente próximo do topo ou da base.
- [ ] Títulos, equações e legendas possuem hierarquia visual.
- [ ] Textos não competem com vetores e eixos.
- [ ] Eixos possuem cor discreta.
- [ ] Vetores possuem cores distintas e semanticamente coerentes.
- [ ] Resultados importantes estão destacados.
- [ ] Nenhum objeto está cortado.
- [ ] Não existem sobreposições involuntárias.
- [ ] A animação é legível em uma tela de celular.

### Científico

- [ ] Equações estão corretas.
- [ ] Unidades estão corretas.
- [ ] Conversões estão corretas.
- [ ] Direções e sentidos dos vetores estão corretos.
- [ ] Diagramas representam corretamente o fenômeno.
- [ ] Escalas visuais estão justificadas.

### Técnico

- [ ] O código utiliza Manim CE.
- [ ] O código é compatível com a versão instalada.
- [ ] Não existem erros de execução.
- [ ] Não existem dependências desnecessárias.
- [ ] O vídeo foi efetivamente renderizado.
- [ ] O vídeo foi inspecionado visualmente.
- [ ] Os problemas encontrados foram corrigidos.

**Regra final: nenhuma animação deve ser considerada concluída sem inspeção do vídeo renderizado. A ausência de erros no código não garante a qualidade visual do resultado.**