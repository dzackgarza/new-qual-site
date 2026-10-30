---
schema: qual/card@1
id: P-TIE-F09-16
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 16.
---

::: {.problem}
Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a point $z_{0}$ inside $\Omega$. Show that if $f(z)$ is bounded near $z_{0}$, then $\int_{\Delta} f(z) \, dz = 0$ for all triangles $\Delta$ in $\Omega$.
:::

::: {.solution}

Let $z_0$ be the possible exceptional point.

::: pf

::: {.pf-step #s1-1}

There exist $r>0$ and $M>0$ such that
$$
\abs{f(z)}\le M
$$
whenever
$$
0<\abs{z-z_0}<r.
$$


::: pf-proof

This is precisely the hypothesis that $f$ is bounded near $z_0$.

:::

:::

::: {.pf-step #s1-2}

Define
$$
g(z)=
\begin{cases}
(z-z_0)^2f(z),&z\ne z_0,\\
0,&z=z_0.
\end{cases}
$$
Then $g$ is analytic on all of $\Omega$.


::: pf-proof

Away from $z_0$, the function is a product of analytic functions. At $z_0$,
$$
\frac{g(z)-g(z_0)}{z-z_0}
=(z-z_0)f(z).
$$
By step [](#s1-1){.pf-ref},
$$
\abs{(z-z_0)f(z)}
\le
M\abs{z-z_0}
\longrightarrow0
$$
as $z\to z_0$. Hence $g$ is differentiable at $z_0$ and
$$
g'(z_0)=0.
$$
Thus $g$ is analytic throughout $\Omega$.

:::

:::

::: {.pf-step #s1-3}

The function $g$ has a zero of order at least $2$ at $z_0$.


::: pf-proof

By definition,
$$
g(z_0)=0,
$$
and step [](#s1-2){.pf-ref} gives
$$
g'(z_0)=0.
$$
The Taylor expansion of $g$ at $z_0$ therefore has no constant or linear term, so
$$
g(z)=(z-z_0)^2h(z)
$$
for some analytic function $h$ near $z_0$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ has a removable singularity at $z_0$.


::: pf-proof

For $0<\abs{z-z_0}<r$, steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give
$$
(z-z_0)^2f(z)
=
g(z)
=(z-z_0)^2h(z).
$$
Hence
$$
f(z)=h(z)
$$
on the punctured neighborhood. Defining
$$
f(z_0)=h(z_0)
$$
therefore extends $f$ analytically across $z_0$.

:::

:::

::: {.pf-step #s1-5}

For every triangle $\Delta$ whose closed interior lies in $\Omega$,
$$
\boxed{\int_{\partial\Delta}f(z)\,dz=0}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $f$ may be regarded as analytic on all of $\Omega$. Goursat's theorem applied
to the triangle $\Delta$ then gives
$$
\int_{\partial\Delta}f(z)\,dz=0.
$$
This is the triangle integral denoted $\int_\Delta f(z)\,dz$ in the source.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required assertion.

:::

:::

:::
