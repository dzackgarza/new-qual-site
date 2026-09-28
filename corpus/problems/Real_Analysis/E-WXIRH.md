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

::: {.exercise}
\[
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y \\ 
\implies
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
.\]

:::

::: {.solution}
Let $f, g \in L^1[0,1]$ and let $T = \theset{(x,y) : 0 \le y \le x \le 1}$.

<1>1. $\iint_{T} |f(y)||g(x)|\,dy\,dx \le \|f\|_1\|g\|_1 < \infty$.

::: {.proof}
By Tonelli's theorem, $\iint_T |f(y)||g(x)|\,dy\,dx \le \int_0^1\int_0^1 |f(y)||g(x)|\,dy\,dx = \|f\|_1\|g\|_1$.
:::

<1>2. $\int_0^1 F(x)g(x)\,dx = \int_0^1 f(y)\big(G(1) - G(y)\big)\,dy$.

::: {.proof}
By the definition of $F$, $\int_0^1 F(x)g(x)\,dx = \int_0^1\int_0^x f(y)g(x)\,dy\,dx$. By step <1>1, Fubini's theorem allows integrating over $T$ in the other order, with $y \in [0,1]$ and $x \in [y,1]$, giving $\int_0^1 f(y)\int_y^1 g(x)\,dx\,dy$. Finally $\int_y^1 g = G(1) - G(y)$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2 and $F(1) = \int_0^1 f$, $\int_0^1 Fg = G(1)\int_0^1 f - \int_0^1 fG = F(1)G(1) - \int_0^1 fG$.
:::
:::
