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
Let $f ( z )$ be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside Ω. Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.
:::

::: {.solution}
Let $z_0$ be the possible exceptional point.

<1>1. There exist $r>0$ and $M>0$ such that
$$
|f(z)|\le M
$$
whenever
$$
0<|z-z_0|<r.
$$

::: {.proof}
This is precisely the hypothesis that $f$ is bounded near $z_0$.
:::

<1>2. Define
$$
g(z)=
\begin{cases}
(z-z_0)^2f(z),&z\ne z_0,\\
0,&z=z_0.
\end{cases}
$$
Then $g$ is analytic on all of $\Omega$.

::: {.proof}
Away from $z_0$, the function is a product of analytic functions. At $z_0$,
$$
\frac{g(z)-g(z_0)}{z-z_0}
=(z-z_0)f(z).
$$
By step <1>1,
$$
|(z-z_0)f(z)|
\le
M|z-z_0|
\longrightarrow0
$$
as $z\to z_0$. Hence $g$ is differentiable at $z_0$ and
$$
g'(z_0)=0.
$$
Thus $g$ is analytic throughout $\Omega$.
:::

<1>3. The function $g$ has a zero of order at least $2$ at $z_0$.

::: {.proof}
By definition,
$$
g(z_0)=0,
$$
and step <1>2 gives
$$
g'(z_0)=0.
$$
The Taylor expansion of $g$ at $z_0$ therefore has no constant or linear term, so
$$
g(z)=(z-z_0)^2h(z)
$$
for some analytic function $h$ near $z_0$.
:::

<1>4. The function $f$ has a removable singularity at $z_0$.

::: {.proof}
For $0<|z-z_0|<r$, steps <1>2 and <1>3 give
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

<1>5. For every triangle $\Delta$ whose closed interior lies in $\Omega$,
$$
\boxed{\int_{\partial\Delta}f(z)\,dz=0}.
$$

::: {.proof}
By step <1>4, $f$ may be regarded as analytic on all of $\Omega$. Goursat's theorem applied
to the triangle $\Delta$ then gives
$$
\int_{\partial\Delta}f(z)\,dz=0.
$$
This is the triangle integral denoted $\int_\Delta f(z)\,dz$ in the source.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required assertion.
:::
:::
