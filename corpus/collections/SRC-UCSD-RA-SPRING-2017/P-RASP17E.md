---
schema: qual/card@1
id: P-RASP17E
kind: problem
title: "Dilations of R^2 act isometrically on L^2 and continuously as t approaches 1"
classification:
  areas:
  - real-analysis
  topics:
  - L2 Spaces
  - Change of Variables
  - Density Arguments
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
For $t > 0$, let $A_t = \begin{pmatrix} t & 0 \\ 0 & t^{-1} \end{pmatrix}$ and for $f : \mathbb{R}^2 \to \mathbb{C}$ let $T_t f(x) = f(A_t x)$ for $x \in \mathbb{R}^2$.

1. Show $\|T_t f\|_2 = \|f\|_2$ for all $f \in L^2(\mathbb{R}^2, m)$.

2. Explain why $\lim_{t \to 1} \|T_t f - f\|_2 = 0$ for all $f \in C_c(\mathbb{R}^2)$.

3. Show $\lim_{t \to 1} \|T_t f - f\|_2 = 0$ for all $f \in L^2(\mathbb{R}^2, m)$.
:::

::: {.solution}
**Part 1.**

<1>1. $\det A_t = t \cdot t^{-1} = 1$.
::: {.proof}
compute the determinant.
:::

<1>2. Hence $\|T_t f\|_2^2 = \int |f(A_t x)|^2\,dx = \int |f(y)|^2 |\det A_t^{-1}|\,dy = \int |f(y)|^2\,dy = \|f\|_2^2$.
::: {.proof}
change of variables $y = A_t x$, with Jacobian $|\det A_t| = 1$.
:::

<1>3. Hence $\|T_t f\|_2 = \|f\|_2$.
::: {.proof}
<1>2.
:::

**Part 2.**

<1>1. For $f \in C_c(\mathbb{R}^2)$, $f$ is uniformly continuous.
::: {.proof}
continuous functions with compact support are uniformly continuous.
:::

<1>2. As $t \to 1$, $A_t \to I$, so $A_t x \to x$ uniformly on compact sets.
::: {.proof}
<1>1.
:::

<1>3. Hence $T_t f(x) = f(A_t x) \to f(x)$ uniformly, and since $f$ has compact support, $\|T_t f - f\|_2 \to 0$.
::: {.proof}
<1>2 and the dominated convergence theorem (the support is bounded).
:::

**Part 3.**

<1>1. $C_c(\mathbb{R}^2)$ is dense in $L^2(\mathbb{R}^2)$.
::: {.proof}
standard density result.
:::

<1>2. For $f \in L^2$ and $\varepsilon > 0$, choose $g \in C_c$ with $\|f - g\|_2 < \varepsilon/3$.
::: {.proof}
<1>1.
:::

<1>3. $\|T_t f - f\|_2 \le \|T_t(f - g)\|_2 + \|T_t g - g\|_2 + \|g - f\|_2 = \|f - g\|_2 + \|T_t g - g\|_2 + \|g - f\|_2$.
::: {.proof}
triangle inequality and part 1 (isometry).
:::

<1>4. For $t$ close to $1$, $\|T_t g - g\|_2 < \varepsilon/3$ (by part 2), so $\|T_t f - f\|_2 < \varepsilon$.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Hence $\lim_{t \to 1} \|T_t f - f\|_2 = 0$.
::: {.proof}
<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>3 (1), <1>3 (2), <1>5 (3).
:::
:::
