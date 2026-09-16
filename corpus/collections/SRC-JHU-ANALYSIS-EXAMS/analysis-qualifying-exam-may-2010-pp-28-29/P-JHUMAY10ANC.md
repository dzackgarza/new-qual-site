---
schema: qual/card@1
id: P-JHUMAY10ANC
kind: problem
title: "The Bergman space of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Bergman Space
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both the compact point-evaluation estimate and closed-subspace conclusion with May 2010 problem 3 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the uniform disk radius, the mean-square estimate and identification of the locally uniform holomorphic limit with the prescribed L2 equivalence class."
---

::: {.problem}
3. Let $\mathcal { O } ( D )$ denote the space of holomorphic functions on the unit disk D and let

$$
{ \mathcal H } = { \mathcal O } ( D ) \cap L ^ { 2 } ( D ) = \left\{ f \in { \mathcal O } ( D ) : \int _ { D } | f | ^ { 2 } d x d y < + \infty \right\} .
$$

a) Show that for all compact sets $K \subset D$ , there is a constant $C _ { K } \in \mathbb { R } ^ { + }$ such that

$$
\operatorname* { s u p } _ { z \in K } | f ( z ) | \leq C _ { K } \| f \| _ { L ^ { 2 } ( D ) } .
$$

b) Show that H is a closed subspace of $L ^ { 2 } ( D )$ and hence is a Hilbert space.
:::

::: solution
Write $dA=dx\,dy$. We identify each function in $\mathcal H$
with its almost-everywhere class in $L^2(D)$. This is
injective: a continuous function nonzero at a point is
bounded away from zero on a small disk of positive area,
so cannot be zero almost everywhere.

<1>1. A disk contained in $D$ gives an $L^2$ point-evaluation estimate.
::: proof
For $\overline{D(a,r)}\subset D$ and $0<\rho<r$,
Cauchy's formula at the center and Cauchy–Schwarz give
$$
|f(a)|^2\leq\frac1{2\pi}\int_0^{2\pi}
|f(a+\rho e^{it})|^2\,dt
$$
[@SS03; @Fol13]. Multiply by $2\pi\rho$ and integrate
from zero to $r$. Polar coordinates yield
$$
\pi r^2|f(a)|^2\leq\int_{D(a,r)}|f(z)|^2\,dA(z).
$$
For nonempty compact $K\subset D$, set
$r=(1-\max_{a\in K}|a|)/2>0$. The closed radius-$r$
disk about every $a\in K$ is contained in $D$. Therefore
$$
\sup_{a\in K}|f(a)|\leq C_K\|f\|_{L^2(D)},
\qquad C_K=\frac1{\sqrt\pi r}.
$$
For the empty compact set the bound has no points to
check, and any positive $C_K$ suffices. This proves (a).
:::

<1>2. An $L^2$ limit of elements of $\mathcal H$ has a holomorphic representative.
::: proof
Suppose $f_n\in\mathcal H$ and $f_n\to F$ in $L^2(D)$.
Choose a measurable representative of $F$. The sequence
is Cauchy in $L^2$, so step <1>1 applied to $f_n-f_m$
makes it uniformly Cauchy on each compact subset of $D$.
Completeness of $\mathbb C$ gives a pointwise limit $f$,
and the same estimates give uniform convergence on every
compact set. The local uniform limit theorem makes $f$
holomorphic on $D$ [@SS03].

Pointwise convergence and Fatou's lemma give
$$
\int_D|f-F|^2\,dA
\leq\liminf_{n\to\infty}\int_D|f_n-F|^2\,dA=0
$$
[@Fol13]. Thus $f=F$ almost everywhere, so $f$ belongs
to $\mathcal H$ and represents the given $L^2$ limit.
:::

<1>3. The space $\mathcal H$ is a closed linear subspace and is complete.
::: proof
Linear combinations of its functions are holomorphic
and square integrable, so it is a linear subspace of
$L^2(D)$. Step <1>2 proves that this subspace is closed.
The space $L^2(D)$ is Hilbert [@Fol13]; a Cauchy sequence
in a closed subspace converges in the ambient Hilbert
space and has its limit in that subspace. Therefore
$\mathcal H$, with the inherited inner product, is a
Hilbert space. This proves (b).
:::
:::
