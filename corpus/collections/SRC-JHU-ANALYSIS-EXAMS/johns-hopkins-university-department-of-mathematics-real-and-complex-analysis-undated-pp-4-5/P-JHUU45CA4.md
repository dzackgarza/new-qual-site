---
schema: qual/card@1
id: P-JHUU45CA4
kind: problem
title: Bergman space is a Hilbert space
classification:
  areas:
  - complex-analysis
  topics:
  - Bergman Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the arbitrary open set, area integral and inner product with Problem 7 of the undated JHU exam on pages 4–5."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked positive definiteness for actual holomorphic functions, the disk mean-square estimate, uniform convergence on compact subsets, and both Fatou arguments proving completeness without assuming a holomorphic representative of an L2 limit."
---

Let $U \subseteq \mathbb{C}$ be an open set and

$$A^2(U) = \{ f \text{ holomorphic on } U : \int_U |f(z)|^2 \, dx \, dy < \infty \}.$$

Define

$$(f, g) = \int_U f(z) \overline{g(z)} \, dx \, dy, \quad \forall f, g \in A^2(U).$$

Prove that $A^2(U)$ is a Hilbert space when equipped with this inner product.

::: solution
Write $dA=dx\,dy$ and $\|f\|_2=(\int_U|f|^2\,dA)^{1/2}$.
If $U$ is empty, the space consists of the unique empty
function and is the zero Hilbert space. Assume $U\ne\varnothing$.

<1>1. The displayed formula is an inner product on $A^2(U)$.

::: proof
Linear combinations remain holomorphic, and
$|af+bg|^2\leq2|a|^2|f|^2+2|b|^2|g|^2$ proves their
square integrability. Thus $A^2(U)$ is a complex vector space.
Cauchy–Schwarz gives
$\int_U|f\overline g|\,dA\leq\|f\|_2\|g\|_2$, so the
inner product is finite [@Fol13]. Linearity in the first
variable and conjugate symmetry follow from the integral.

If $f(a)\ne0$ at some $a\in U$, continuity gives a disk
inside $U$ on which $|f|\geq|f(a)|/2>0$. Its positive
area makes $\int_U|f|^2\,dA>0$. Hence zero norm forces
the holomorphic function itself to be zero everywhere,
not just almost everywhere. This proves positive definiteness.
:::

<1>2. The $L^2$ norm controls uniform convergence on each compact subset.

::: proof
Let $h$ be holomorphic on $U$, and suppose
$\overline{D(a,r)}\subset U$. Cauchy's formula and
Cauchy–Schwarz on each circle of radius $0<\rho<r$ give
$$
|h(a)|^2\leq\frac1{2\pi}\int_0^{2\pi}
|h(a+\rho e^{it})|^2\,dt
$$
[@SS03]. Multiply by $2\pi\rho$ and integrate from
zero to $r$. Polar coordinates yield
$$
\pi r^2|h(a)|^2\leq\int_{D(a,r)}|h|^2\,dA.
$$
For a nonempty compact $K\subset U$, choose one $r>0$
such that $\overline{D(a,r)}\subset U$ for every $a\in K$.
Such an $r$ exists by compactness and openness; when
$U\ne\mathbb C$, take less than the positive distance
from $K$ to the closed complement, and otherwise take $r=1$.
It follows that
$$
\sup_{a\in K}|h(a)|\leq\frac1{\sqrt\pi r}\|h\|_2.
$$
Apply this to differences of elements of $A^2(U)$.
:::

<1>3. Every Cauchy sequence in $A^2(U)$ converges in its norm.

::: proof
Let $(f_n)$ be such a sequence. Step <1>2 makes it
uniformly Cauchy on each compact subset of $U$. Completeness
of $\mathbb C$ gives a pointwise limit $f$, and the same
Cauchy estimates show that convergence is uniform on each
compact subset. The local uniform limit of holomorphic
functions is holomorphic [@SS03]. Thus $f$ is holomorphic on $U$.

The norms $\|f_n\|_2$ are bounded because the sequence
is Cauchy. Fatou's lemma gives
$$
\int_U|f|^2\,dA\leq\liminf_{n\to\infty}\|f_n\|_2^2<\infty,
$$
so $f\in A^2(U)$ [@Fol13]. Given $\varepsilon>0$,
choose $N$ such that $\|f_n-f_m\|_2<\varepsilon$ for
$n,m\geq N$. For fixed $n\geq N$, apply Fatou again:
$$
\|f_n-f\|_2^2\leq\liminf_{m\to\infty}\|f_n-f_m\|_2^2
\leq\varepsilon^2.
$$
Therefore $f_n\to f$ in norm. The inner-product space
is complete, hence is a Hilbert space.
:::
:::
