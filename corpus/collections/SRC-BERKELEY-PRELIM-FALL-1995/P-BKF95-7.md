---
schema: qual/card@1
id: P-BKF95-7
kind: problem
title: Coefficients of a Hadamard product from a contour integral
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Expanded both entire functions on the unit contour and integrated the
    absolutely convergent double series termwise; only terms with matching
    indices have nonzero contour integral.
---

::: {.problem}
Let
\[
g(z)=\sum_{n=0}^\infty g_nz^n,
\qquad
h(z)=\sum_{n=0}^\infty h_nz^n
\]
be entire.
Find a formula for the coefficients $f_n$ in the Taylor expansion at $0$ of
\[
f(z)=\frac1{2\pi i}\int_{|w|=1}g(z/w)h(w)\frac{dw}{w}.
\]
:::

::: {.solution}
<1>1. For each fixed $z\in\CC$ and every $w$ with $\abs{w}=1$,
$$
g(z/w)
=
\sum_{n=0}^{\infty}g_nz^nw^{-n}
$$
and
$$
h(w)
=
\sum_{m=0}^{\infty}h_mw^m,
$$
with both series absolutely and uniformly convergent on the unit circle.

::: {.proof}
Because $g$ is entire, its power series converges absolutely at
$\abs{z}$:
$$
\sum_{n=0}^{\infty}\abs{g_n}\abs{z}^n<\infty.
$$
For $\abs{w}=1$,
$$
\abs{g_nz^nw^{-n}}
=
\abs{g_n}\abs{z}^n,
$$
so the Weierstrass $M$-test gives uniform absolute convergence of the first
series. Likewise, entire-ness of $h$ gives
$$
\sum_{m=0}^{\infty}\abs{h_m}<\infty,
$$
and the $M$-test gives uniform absolute convergence of the second series on
$\abs{w}=1$.
:::

<1>2. The product admits the uniformly absolutely convergent expansion
$$
g(z/w)h(w)
=
\sum_{n,m\geq0}
g_nh_mz^nw^{m-n}
$$
on $\abs{w}=1$.

::: {.proof}
By step <1>1,
$$
\sum_{n,m\geq0}
\abs{g_nh_mz^nw^{m-n}}
=
\left(
\sum_{n\geq0}\abs{g_n}\abs{z}^n
\right)
\left(
\sum_{m\geq0}\abs{h_m}
\right)
<\infty,
$$
uniformly for $\abs{w}=1$. Hence the double series converges uniformly and
absolutely there and represents the product.
:::

<1>3. One has
$$
f(z)
=
\sum_{n=0}^{\infty}g_nh_nz^n.
$$

::: {.proof}
By step <1>2, termwise contour integration is valid:
$$
\begin{aligned}
f(z)
&=
\sum_{n,m\geq0}
g_nh_mz^n
\frac1{2\pi i}
\int_{\abs{w}=1}
w^{m-n-1}\,dw.
\end{aligned}
$$
The standard contour integral gives
$$
\frac1{2\pi i}
\int_{\abs{w}=1}
w^{m-n-1}\,dw
=
\begin{cases}
1,&m=n,\\
0,&m\neq n.
\end{cases}
$$
Therefore only the terms with $m=n$ survive, yielding the displayed
series.
:::

<1>4. The Taylor coefficients of $f$ at the origin are
$$
\boxed{f_n=g_nh_n}.
$$

::: {.proof}
Step <1>3 is already the Taylor expansion of $f$ in powers of $z$, so its
$n$th coefficient is $g_nh_n$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested formula.
:::
:::
