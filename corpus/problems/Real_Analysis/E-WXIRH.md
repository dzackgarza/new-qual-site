---
schema: qual/card@1
id: E-WXIRH
kind: problem
title: Integration by parts, special case
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

:::{.exercise}
\[
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y \\ 
\implies
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
.\]

:::

::: {.solution}
<1>1. The double integral $\iint_{0 \le y \le x \le 1} |f(y)||g(x)|\,dy\,dx$ is finite.
    ::: {.proof}
    Tonelli: $\int_0^1\int_0^x |f(y)||g(x)|\,dy\,dx \le \int_0^1\int_0^1 |f(y)||g(x)|\,dy\,dx = \|f\|_1\|g\|_1 < \infty$; in particular the hypothesis of Fubini is satisfied for $f(y)g(x)$.
    :::

<1>2. $\int_0^1 F(x)g(x)\,dx = \iint_{0 \le y \le x \le 1} f(y)g(x)\,dy\,dx$.
    ::: {.proof}
    $F(x) = \int_0^x f(y)\,dy$, so $\int_0^1 F(x)g(x)\,dx = \int_0^1\int_0^x f(y)g(x)\,dy\,dx$; Fubini applies by <1>1.
    :::

<1>3. $\iint_{0 \le y \le x \le 1} f(y)g(x)\,dy\,dx = \int_0^1 f(y)\int_y^1 g(x)\,dx\,dy$.
    ::: {.proof}
    interchange the order of integration (Fubini); the region $\{0 \le y \le x \le 1\}$ can be sliced horizontally as $\{(x,y) : 0 \le y \le 1,\ y \le x \le 1\}$.
    :::

<1>4. $\int_y^1 g(x)\,dx = G(1) - G(y)$.
    ::: {.proof}
    $G(1) = \int_0^1 g$ and $G(y) = \int_0^y g$; additivity of the integral.
    :::

<1>5. Q.E.D.
    ::: {.proof}
    $\int_0^1 F g = \int_0^1 f(y)(G(1) - G(y))\,dy = G(1)\int_0^1 f - \int_0^1 fG = F(1)G(1) - \int_0^1 fG$, using $F(1) = \int_0^1 f$.
    :::
:::
