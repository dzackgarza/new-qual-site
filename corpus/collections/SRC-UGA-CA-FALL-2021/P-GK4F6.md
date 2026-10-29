---
schema: qual/card@1
id: P-GK4F6
kind: problem
title: The integral $\int_\gamma F(w)/(w-z)\,dw$ is holomorphic off $\gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $\gamma(t)$ be a piecewise smooth curve in $\CC, t \in[0,1]$. Let $F(w)$ be a continuous function on $\gamma$. Show that $f(z)$ defined by
\[
f(z):=\int_{\gamma} \frac{F(w)}{w-z} d w
\]
is analytic on the complement of the curve $\gamma$.

:::

::: {.solution}

Let $K=\gamma([0,1])$ and $U=\CC\setminus K$. The compactness of $K$ implies that $U$ is open. Let $L$ be the length of the piecewise smooth curve $\gamma$.

::: pf

::: {.pf-step #s1-1}

For every $z_0\in U$, the derivative exists and equals
\[
\boxed{f'(z_0)=\int_\gamma\frac{F(w)}{(w-z_0)^2}\,dw}.
\]


::: pf-proof

Fix $z_0\in U$ and let $d=\operatorname{dist}(z_0,K)>0$. For $0<|h|<d/2$, subtraction of the two integrals yields
\[
\frac{f(z_0+h)-f(z_0)}{h}
=\int_\gamma\frac{F(w)}{(w-z_0-h)(w-z_0)}\,dw.
\]
For every $w\in K$, the difference between the integrand on the right and $F(w)/(w-z_0)^2$ is bounded in absolute value by
\[
\frac{2\|F\|_{\infty,K}|h|}{d^3}.
\]
The integral of that difference therefore has absolute value at most $2L\|F\|_{\infty,K}|h|/d^3$, which tends to zero with $h$. This proves the asserted derivative formula.

:::

:::

::: {.pf-step #s1-2}

The function $f$ is holomorphic on $U$.


::: pf-proof

Step [](#s1-1){.pf-ref} establishes complex differentiability at every point of the open set $U$. Hence $f$ is holomorphic on $U$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the assertion.

:::

:::

:::
