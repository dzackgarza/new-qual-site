---
schema: qual/card@1
id: PR-TNFL4
kind: proposition
title: Integration by parts for indefinite integrals of $L^1$ functions
slogan: 'For $f,g\in L^1([0,1])$ with indefinite integrals $F,G$ from $0$, $\int_0^1 Fg=F(1)G(1)-\int_0^1 fG$.'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.proposition}
Let $f,g\in L^1([0,1])$ and put
$$
F(x)\coloneqq\int_{0}^{x} f(y) \,dy, \qquad G(x)\coloneqq\int_{0}^{x} g(y) \,dy \qquad (0\leq x\leq1).
$$
Then
$$
\int_{0}^{1} F(x) g(x) \,dx=F(1) G(1)-\int_{0}^{1} f(x) G(x) \,dx .
$$
:::

::: {.proof}
Let $T\coloneqq\theset{(x,y) \suchthat 0 \le y \le x \le 1}$.
By Tonelli's theorem, $\iint_T \abs{f(y)}\abs{g(x)}\,dy\,dx \le \norm{f}_1\norm{g}_1 < \infty$, so Fubini's theorem lets us integrate $f(y)g(x)$ over $T$ in either order:
$$
\int_0^1 F(x)g(x)\,dx = \int_0^1\int_0^x f(y)g(x)\,dy\,dx = \int_0^1 f(y)\int_y^1 g(x)\,dx\,dy = \int_0^1 f(y)\big(G(1) - G(y)\big)\,dy .
$$
Since $\int_0^1 f = F(1)$, the right side is $F(1)G(1) - \int_0^1 fG$.
:::
