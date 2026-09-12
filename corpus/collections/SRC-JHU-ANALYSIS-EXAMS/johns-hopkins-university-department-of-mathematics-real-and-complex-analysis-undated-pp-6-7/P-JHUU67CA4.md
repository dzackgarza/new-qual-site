---
schema: qual/card@1
id: P-JHUU67CA4
kind: problem
title: Bergman space embedding, normal family, and removable singularity
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
  note: "Compared all three requests with Problem 7 of the undated JHU exam on pages 6–7, retaining arbitrary open sets and the square-integrable punctured-disk hypothesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the uniform disk-radius constant, normality also on disconnected open sets, and the vanishing local L2 mass needed to obtain zf(z) tending to zero rather than merely boundedness."
---

Let $U$ be an open subset of $\mathbb{C}$.
We use the notation

$$\|f\|_{L^2(U)} = \left(\int_U |f|^2 \, dx \, dy\right)^{1/2}.$$

- Let $f : U \to \mathbb{C}$ be a holomorphic function.
  Show that for any compact set $K \subset U$, there is a constant $C_K$ such that

$$\sup_{z \in K} |f(z)| \leq C_K \|f\|_{L^2(U)}.$$

- Prove that $\{f \text{ is holomorphic on } U : \|f\|_{L^2(U)} \leq 1\}$ is a normal family.

- Suppose $U$ is the punctured disc $D(0,1) \setminus \{0\}$.
  If $f$ is holomorphic on $U$ and $\|f\|_{L^2(U)} < \infty$, prove that $z = 0$ is a removable singularity of $f$.

::: solution
Write $dA=dx\,dy$. Normality here means that every sequence
has a subsequence converging uniformly on compact subsets
to a finite holomorphic function.

<1>1. A disk contained in $U$ gives a pointwise mean-square estimate.

::: proof
Suppose $\overline{D(a,r)}\subset U$. For $0<\rho<r$,
Cauchy's formula at the center and Cauchy–Schwarz give
$$
f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+\rho e^{it})\,dt,
\qquad
|f(a)|^2\leq\frac1{2\pi}\int_0^{2\pi}|f(a+\rho e^{it})|^2\,dt
$$
[@SS03; @Fol13]. Multiplying by $2\pi\rho$ and integrating
over $0<\rho<r$ yields, by polar coordinates,
$$
\pi r^2|f(a)|^2\leq\int_{D(a,r)}|f|^2\,dA.
$$
:::

<1>2. The required compact-set bound holds with a constant independent of $f$.

::: proof
For nonempty compact $K\subset U$, choose $r>0$ with
$\overline{D(a,r)}\subset U$ for all $a\in K$.
If $U\ne\mathbb C$, take half the distance from $K$ to
the closed set $\mathbb C\setminus U$; this distance is
positive by compactness and openness. For $U=\mathbb C$,
take $r=1$. Step <1>1 gives
$$
\sup_{a\in K}|f(a)|\leq\frac1{\sqrt\pi r}\|f\|_{L^2(U)}.
$$
Thus $C_K=1/(\sqrt\pi r)$ works. If the norm is infinite,
the inequality holds in the extended sense. For empty
$K$ the pointwise assertion has no points to check.
:::

<1>3. The family with $L^2$ norm at most one is normal on $U$.

::: proof
Step <1>2 makes this family uniformly bounded on every
compact subset of $U$. Montel's theorem gives normality
[@SS03]. This also applies when $U$ is disconnected:
its components are open and each contains a point with
rational real and imaginary parts, so there are at most
countably many components. Apply the theorem to each
component and take a diagonal subsequence. Every compact
subset of $U$ meets only finitely many components, since
the components form an open cover of that compact set.
The diagonal subsequence therefore converges uniformly
on every compact subset of $U$, to the componentwise
holomorphic limit. When $U$ is empty the assertion is immediate.

In fact the limit remains in the family: pointwise
convergence and Fatou's lemma give
$\int_U|f|^2\,dA\leq\liminf_j\int_U|f_{n_j}|^2\,dA\leq1$
[@Fol13].
:::

<1>4. Square integrability makes the isolated singularity removable.

::: proof
Now let $U=\{0<|z|<1\}$ and $\int_U|f|^2\,dA<\infty$.
For $0<|a|<1/2$, the closed disk of radius $r=|a|/2$
centered at $a$ lies in $U$. Step <1>1 implies
$$
|a|^2|f(a)|^2
\leq\frac4\pi\int_{D(a,|a|/2)}|f|^2\,dA
\leq\frac4\pi\int_{0<|z|<3|a|/2}|f(z)|^2\,dA.
$$
The last integral tends to zero as $a\to0$. To see this,
the indicators of shrinking punctured disks tend pointwise
to zero on $U$ and are dominated by one; dominated
convergence applies to the integrable function $|f|^2$
[@Fol13]. Hence $af(a)\to0$.

The function $h(z)=zf(z)$ is holomorphic on the punctured
disk and tends to zero at the puncture. The removable
singularity theorem extends it holomorphically with $h(0)=0$
[@SS03]. Its Taylor series is divisible by $z$, so
$h(z)=zF(z)$ for a holomorphic $F$ near zero. For $z\ne0$,
this $F$ equals $f$. It supplies the required holomorphic
extension across zero.
:::
:::
