---
schema: qual/card@1
id: P-TIE-S15-34
kind: problem
title: Sup norm on a smaller disk bounded by the $L^1$ norm for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 34.
---

::: {.problem}
Let f be holomorphic in a neighborhood of $D _ { r } ( z _ { 0 } )$ . Show that for any $s < r ,$ , there exists a constant $c > 0$ such that

$$
\| f \| _ { ( \infty , s ) } \leq c \| f \| _ { ( 1 , r ) } ,
$$

where $\| f \| _ { ( \infty , s ) } = \operatorname* { s u p } _ { z \in D _ { s } ( z _ { 0 } ) } | f ( z ) | { \mathrm { ~ a n d ~ } } \| f \| _ { ( 1 , r ) } = \int _ { D _ { r } ( z _ { 0 } ) } | f ( z ) | d x d y .$
:::

Set
$$
\rho\coloneqq r-s>0.
$$

::: pf

::: pf-step

If $z\in D_s(z_0)$, then
$$
D_\rho(z)\subset D_r(z_0).
$$


::: pf-proof

For $w\in D_\rho(z)$,
$$
\abs{w-z_0}
\le
\abs{w-z}+\abs{z-z_0}
<
\rho+s
=
r.
$$
Hence $w\in D_r(z_0)$.

:::

:::

::: pf-step

For every $z\in D_s(z_0)$,
$$
\abs{f(z)}
\le
\frac1{\pi\rho^2}
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w).
$$


::: pf-proof

For each $0<t<\rho$, Cauchy's integral formula on the circle
$$
\abs{w-z}=t
$$
gives
$$
\abs{f(z)}
\le
\frac1{2\pi}
\int_0^{2\pi}
\abs{f(z+te^{i\theta})}\,d\theta.
$$
Multiply by $2t$ and integrate from $0$ to $\rho$:
$$
\abs{f(z)}
\int_0^\rho2t\,dt
\le
\frac1\pi
\int_0^\rho
\int_0^{2\pi}
\abs{f(z+te^{i\theta})}
t\,d\theta\,dt.
$$
The left factor is $\rho^2$, while the double integral is the polar-coordinate expression for
$$
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w).
$$
Division by $\rho^2$ proves the estimate.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\norm{f}_{(\infty,s)}
\le
\frac1{\pi(r-s)^2}
\norm{f}_{(1,r)}.
}
$$


::: pf-proof

By step <1>1,
$$
D_\rho(z)\subset D_r(z_0).
$$
Hence step <1>2 gives
$$
\abs{f(z)}
\le
\frac1{\pi(r-s)^2}
\int_{D_r(z_0)}
\abs{f(w)}\,dA(w)
$$
for every $z\in D_s(z_0)$. Taking the supremum over $z$ gives the displayed inequality.

:::

:::

::: pf-qed

Step <1>3 proves the result with
$$
\boxed{
c=\frac1{\pi(r-s)^2}>0.
}
$$

:::

:::
