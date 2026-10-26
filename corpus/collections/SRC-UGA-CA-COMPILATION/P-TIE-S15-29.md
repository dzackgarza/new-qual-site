---
schema: qual/card@1
id: P-TIE-S15-29
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 29.
---

::: {.problem}
Let f be holomorphic in a neighborhood of $D _ { r } ( z _ { 0 } )$ . Show that for any $s < r .$ , there exists a constant $c > 0$ such that

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

::: {.pf-step #s1-1}

If $z\in D_s(z_0)$, then
$$
D_\rho(z)\subset D_r(z_0).
$$


::: pf-proof

If $w\in D_\rho(z)$, then
$$
\abs{w-z_0}
\le
\abs{w-z}+\abs{z-z_0}
<
\rho+s
=
r.
$$
Thus $w\in D_r(z_0)$.

:::

:::

::: {.pf-step #s1-2}

For every $z\in D_s(z_0)$ and every $0<t<\rho$,
$$
\abs{f(z)}
\le
\frac1{2\pi}
\int_0^{2\pi}
\abs{f(z+te^{i\theta})}\,d\theta.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the circle
$$
\abs{w-z}=t
$$
lies in the region where $f$ is holomorphic. Cauchy's integral formula gives
$$
f(z)
=
\frac1{2\pi}
\int_0^{2\pi}
f(z+te^{i\theta})\,d\theta.
$$
Taking absolute values yields the estimate.

:::

:::

::: {.pf-step #s1-3}

For every $z\in D_s(z_0)$,
$$
\abs{f(z)}
\le
\frac1{\pi\rho^2}
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w).
$$


::: pf-proof

Multiply the estimate in step [](#s1-2){.pf-ref} by $2t$ and integrate from $0$ to $\rho$:
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
The left factor is
$$
\rho^2,
$$
while the double integral is
$$
\int_{D_\rho(z)}
\abs{f(w)}\,dA(w).
$$
Division by $\rho^2$ gives the result.

:::

:::

::: {.pf-step #s1-4}

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

By step [](#s1-1){.pf-ref},
$$
D_\rho(z)\subset D_r(z_0),
$$
so step [](#s1-3){.pf-ref} gives
$$
\abs{f(z)}
\le
\frac1{\pi(r-s)^2}
\int_{D_r(z_0)}
\abs{f(w)}\,dA(w)
$$
for every $z\in D_s(z_0)$. Taking the supremum over $z$ yields the displayed inequality.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the assertion with
$$
\boxed{
c=\frac1{\pi(r-s)^2}>0.
}
$$

:::

:::
