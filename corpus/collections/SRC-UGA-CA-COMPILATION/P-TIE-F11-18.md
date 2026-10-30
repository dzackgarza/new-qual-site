---
schema: qual/card@1
id: P-TIE-F11-18
kind: problem
title: Goursat's theorem with a bounded isolated singularity
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 18.
---

::: {.problem}
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a point $z_{0}$ inside $\Omega$. Show that if $f(z)$ is bounded near $z_{0}$, then $\int_{\Delta} f(z) \, dz = 0$ for all triangles $\Delta$ in $\Omega$.
:::

::: {.solution}

Let $z_0\in\Omega$ be the possible singular point.

::: pf

::: pf-step

Define
$$
h(z)
\coloneqq
\begin{cases}
(z-z_0)^2f(z),&z\ne z_0,\\
0,&z=z_0.
\end{cases}
$$
Then $h$ is analytic on all of $\Omega$ and
$$
h(z_0)=h'(z_0)=0.
$$


::: pf-proof

Away from $z_0$, the function $h$ is a product of analytic functions. Near $z_0$, choose $M>0$ such that
$$
\abs{f(z)}\le M
$$
for all punctured-neighborhood points sufficiently close to $z_0$. Then
$$
\frac{h(z)-h(z_0)}{z-z_0}
=(z-z_0)f(z),
$$
so
$$
\abs{\frac{h(z)-h(z_0)}{z-z_0}}
\le
M\abs{z-z_0}
\longrightarrow0
$$
as $z\to z_0$. Hence $h$ is complex differentiable at $z_0$ and $h'(z_0)=0$. Thus $h$ is analytic throughout $\Omega$.

:::

:::

::: {.pf-step #s1-2}

The function $f$ extends analytically across $z_0$.


::: pf-proof

Since $h$ is analytic at $z_0$ and
$$
h(z_0)=h'(z_0)=0,
$$
its Taylor expansion at $z_0$ has no constant or linear term. Therefore, on some disk centered at $z_0$,
$$
h(z)
=(z-z_0)^2g(z)
$$
for an analytic function $g$. For $z\ne z_0$ in that disk,
$$
g(z)
=
\frac{h(z)}{(z-z_0)^2}
=
f(z).
$$
Define
$$
\widetilde f(z_0)\coloneqq g(z_0),
\qquad
\widetilde f(z)\coloneqq f(z)
\quad(z\ne z_0).
$$
Then $\widetilde f$ is analytic on all of $\Omega$ and agrees with $f$ away from $z_0$.

:::

:::

::: {.pf-step #s1-3}

For every triangle $\Delta$ whose closed interior lies in $\Omega$,
$$
\boxed{
\int_{\partial\Delta}f(z)\,dz=0.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $\widetilde f$ is analytic on $\Omega$. Cauchy--Goursat therefore gives
$$
\int_{\partial\Delta}\widetilde f(z)\,dz=0.
$$
If $z_0\notin\partial\Delta$, then $f=\widetilde f$ everywhere on the contour. If $z_0\in\partial\Delta$, changing the value of a bounded integrand at the single point $z_0$ does not change the contour integral. Thus
$$
\int_{\partial\Delta}f(z)\,dz
=
\int_{\partial\Delta}\widetilde f(z)\,dz
=0.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the required vanishing for every triangle in $\Omega$.

:::

:::

:::
