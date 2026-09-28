---
schema: qual/card@1
id: P-AZOFF-D04
kind: problem
title: Limits of entire functions converging uniformly on line segments
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    Direct text extraction from the retained PDF confirms that the final
    clause reads f_n -> g uniformly on each compact subset of C. The earlier
    card transcription had dropped the arrow.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used rectangles with polygonal boundary. Uniform convergence on each of
    the four boundary segments is uniform on the whole boundary, so Cauchy's
    formula passes to the pointwise limit and makes g holomorphic inside.
    For a compact set strictly inside such a rectangle, subtracting the two
    Cauchy formulas gives a uniform estimate by the boundary sup norm.
---

::: {.problem}
Suppose $\left( f _ { n } \right)$ is a sequence of functions which are entire (=analytic throughout the complex plane).
Suppose $\left( f _ { n } \right)$ converges pointwise to a function $g : \mathbb { C } \to \mathbb { C }$ and the convergence is uniform on each line segment in $\CC$. Show that $g$ is entire and that $f _ { n } \to g$ uniformly on each compact subset of $\mathbb { C }$
:::

::: {.solution}
<1>1. If $R$ is any closed rectangle in $\CC$, then
$$
f_n\longrightarrow g
$$
uniformly on $\partial R$.

::: {.proof}
The boundary $\partial R$ is the union of four line segments. By hypothesis,
$f_n\to g$ uniformly on each of those four segments. Given
$\varepsilon>0$, choose an index for each side after which the error is
smaller than $\varepsilon$, and take the maximum of those four indices. That
single index works on all of $\partial R$.
:::

<1>2. If $z$ lies in the interior of a rectangle $R$, then
$$
g(z)
=
\frac{1}{2\pi i}
\int_{\partial R}
\frac{g(\zeta)}{\zeta-z}\,d\zeta.
$$

::: {.proof}
For every $n$, Cauchy's integral formula gives
$$
f_n(z)
=
\frac{1}{2\pi i}
\int_{\partial R}
\frac{f_n(\zeta)}{\zeta-z}\,d\zeta.
$$
By step <1>1,
$$
\sup_{\zeta\in\partial R}
\abs{f_n(\zeta)-g(\zeta)}
\longrightarrow0.
$$
Since
$$
\delta_z=\operatorname{dist}(z,\partial R)>0,
$$
we have
$$
\begin{aligned}
&\left|
\int_{\partial R}
\frac{f_n(\zeta)-g(\zeta)}{\zeta-z}\,d\zeta
\right|\\
&\qquad\leq
\frac{\operatorname{length}(\partial R)}{\delta_z}
\sup_{\zeta\in\partial R}
\abs{f_n(\zeta)-g(\zeta)}
\longrightarrow0.
\end{aligned}
$$
The left side of Cauchy's formula satisfies
$$
f_n(z)\longrightarrow g(z)
$$
by the pointwise hypothesis. Passing to the limit gives the displayed
formula.
:::

<1>3. The function $g$ is holomorphic in the interior of every rectangle
$R$.

::: {.proof}
For a fixed rectangle, define
$$
G_R(z)
=
\frac{1}{2\pi i}
\int_{\partial R}
\frac{g(\zeta)}{\zeta-z}\,d\zeta,
\qquad
z\in\operatorname{int}R.
$$
The same difference-quotient argument as for the Cauchy kernel gives
$$
G_R'(z)
=
\frac{1}{2\pi i}
\int_{\partial R}
\frac{g(\zeta)}{(\zeta-z)^2}\,d\zeta.
$$
Indeed, for $h$ small enough the denominators stay uniformly bounded away
from zero on the compact boundary $\partial R$, so the difference-quotient
integrands converge uniformly.

Thus $G_R$ is holomorphic in $\operatorname{int}R$. Step <1>2 gives
$$
g(z)=G_R(z)
$$
there, so $g$ is holomorphic in the interior of $R$.
:::

<1>4. The function $g$ is entire.

::: {.proof}
Fix any $z_0\in\CC$ and choose a rectangle whose interior contains $z_0$.
Step <1>3 shows that $g$ is holomorphic on a neighborhood of $z_0$. Since
$z_0$ was arbitrary, $g$ is holomorphic on all of $\CC$.
:::

<1>5. Let $K\subseteq\CC$ be compact. There is a closed rectangle $R$ such
that
$$
K\subseteq\operatorname{int}R
$$
and
$$
\delta=\operatorname{dist}(K,\partial R)>0.
$$

::: {.proof}
Since $K$ is compact, it is bounded. Choose a rectangle whose sides lie
strictly outside a large disk containing $K$. Then $K$ lies in its interior.
The disjoint compact sets $K$ and $\partial R$ have positive distance, which
is the stated $\delta$.
:::

<1>6. For every $z\in K$,
$$
\abs{f_n(z)-g(z)}
\leq
\frac{\operatorname{length}(\partial R)}{2\pi\delta}
\sup_{\zeta\in\partial R}
\abs{f_n(\zeta)-g(\zeta)}.
$$

::: {.proof}
By Cauchy's integral formula for $f_n$ and step <1>2 for $g$,
$$
f_n(z)-g(z)
=
\frac{1}{2\pi i}
\int_{\partial R}
\frac{f_n(\zeta)-g(\zeta)}{\zeta-z}\,d\zeta.
$$
For
$$
z\in K,
\qquad
\zeta\in\partial R,
$$
step <1>5 gives
$$
\abs{\zeta-z}\geq\delta.
$$
Estimating the contour integral therefore gives the displayed inequality.
:::

<1>7. The convergence
$$
f_n\longrightarrow g
$$
is uniform on every compact subset of $\CC$.

::: {.proof}
For the rectangle from step <1>5, step <1>1 gives
$$
\sup_{\zeta\in\partial R}
\abs{f_n(\zeta)-g(\zeta)}
\longrightarrow0.
$$
The constant in step <1>6 is independent of $z\in K$. Hence
$$
\sup_{z\in K}\abs{f_n(z)-g(z)}
\longrightarrow0.
$$
Since $K$ was arbitrary, the convergence is uniform on every compact subset
of $\CC$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 proves that $g$ is entire, and step <1>7 proves compact-uniform
convergence.
:::
:::
