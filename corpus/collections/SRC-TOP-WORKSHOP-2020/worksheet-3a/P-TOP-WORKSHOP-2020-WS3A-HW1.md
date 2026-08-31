---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW1
kind: problem
title: Construct cell complexes for the sphere and torus (warm-up)
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Create a cell complex for $S^2$ and a cell complex for $T=S^1\times S^1$.
:::

::: {.solution}
<1>1. Cell complex construction for $S^2$:
<2>1. **Cells:**
- One 0-cell: $e^0 = \{v_0\}$.
- No 1-cells: 1-skeleton $X^1 = X^0 = \{v_0\}$.
- One 2-cell: $e^2 = D^2 = \{x \in \mathbb{R}^2 \mid \|x\| \le 1\}$.
::: {.proof}
cell specification.
:::
<2>2. **Attaching map:**
The boundary $\partial e^2 = S^1$ is attached to $X^0$ via the constant map $\varphi: S^1 \to \{v_0\}$.
::: {.proof}
definition of quotient space $D^2 / \partial D^2$.
:::
<2>3. **Identification:**
The resulting CW complex is $X = D^2 / S^1 \cong S^2$.
The cellular chain complex is $0 \to \mathbb{Z} \xrightarrow{0} 0 \xrightarrow{0} \mathbb{Z} \to 0$, giving $H_0(S^2) \cong \mathbb{Z}$, $H_1(S^2) = 0$, and $H_2(S^2) \cong \mathbb{Z}$.
::: {.proof}
cellular homology of $S^2$.
:::

<1>2. Cell complex construction for the torus $T = S^1 \times S^1$:
<2>1. **Cells:**
- One 0-cell: $e^0 = \{v_0\}$.
- Two 1-cells: $e_a^1$ and $e_b^1$.
- One 2-cell: $e^2 = I \times I = [0, 1] \times [0, 1]$.
::: {.proof}
cell specification.
:::
<2>2. **1-Skeleton:**
Each 1-cell is attached with both endpoints mapped to $v_0$, so the 1-skeleton is $X^1 = S^1 \vee S^1$, with loops denoted $a$ and $b$.
::: {.proof}
wedge of two circles.
:::
<2>3. **Attaching map for the 2-cell:**
The boundary $\partial e^2 = \partial(I \times I)$ is attached to $X^1$ via the loop word:
\[
\psi: \partial(I \times I) \to X^1, \quad \text{tracing } a b a^{-1} b^{-1}.
\]
::: {.proof}
planar polygonal diagram for the torus.
:::
<2>4. **Identification:**
The resulting CW complex is $I \times I / \sim$ where $(x, 0) \sim (x, 1)$ and $(0, y) \sim (1, y)$, which is homeomorphic to $S^1 \times S^1$.
The cellular boundary map is $\partial_2(e^2) = a + b - a - b = 0$, yielding $H_0(T) \cong \mathbb{Z}$, $H_1(T) \cong \mathbb{Z}^2$, and $H_2(T) \cong \mathbb{Z}$.
::: {.proof}
standard product identification for the torus.
:::

<1>3. Conclusion:
$S^2$ is constructed as $e^0 \cup_{\text{const}} e^2$, and $T$ is constructed as $e^0 \cup (e_a^1 \cup e_b^1) \cup_{aba^{-1}b^{-1}} e^2$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
