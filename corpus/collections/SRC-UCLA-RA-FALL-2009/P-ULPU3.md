---
schema: qual/card@1
id: P-ULPU3
kind: problem
title: Herglotz's theorem for positive harmonic functions on the disc
classification:
  areas:
  - real-analysis
  topics:
  - Harmonic Functions
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 6 of the UCLA Analysis Qualifying Exam, Fall 2009, from the collection provenance PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Corrected the boundary measures to dmu_R=(2*pi)^{-1}h(Re^{itheta})dtheta,
    so their masses equal h(0). Extracted a weak-* convergent subsequence and
    handled the varying Poisson kernels by uniform convergence plus the uniform
    mass bound, rather than incorrectly applying weak-* convergence to varying
    test functions.
---

::: {.problem}
The Poisson kernel for $0\le \rho<1$ is the $2\pi$-periodic function on $\mathbb{R}$ defined by $$P_\rho(\theta) = \text{Re}\left(\frac{1+\rho e^{i\theta}}{1-\rho e^{i\theta}}\right).$$ For functions $h$ continuous on and harmonic inside the closed disc of radius $R$ about the origin one has $$h(re^{i\eta}) = \frac{1}{2\pi}\int_0^{2\pi} P_{r/R}(\eta-\theta) h(Re^{i\theta})\,d\theta.$$ Assume that $h$ is harmonic and positive on $\mathbb{D}$.
Prove that there exists a positive Borel measure $\mu$ on $[0,2\pi]$ such that for all $re^{i\eta}\in\mathbb{D}$ one has $$h(re^{i\eta}) = \int_0^{2\pi} P_r(\eta-\theta)\,d\mu(\theta).$$
:::

::: {.solution}
Choose a sequence
\[
0<R_1<R_2<\cdots<1,
\qquad
R_j\longrightarrow1.
\]
For example, one may take $R_j=1-1/(j+1)$.

<1>1. Define a positive Borel measure $\mu_j$ on $[0,2\pi]$ by
\[
d\mu_j(\theta)
=\frac1{2\pi}h(R_je^{i\theta})\,d\theta.
\]
Then
\[
\mu_j([0,2\pi])=h(0)
\]
for every $j$.
::: {.proof}
The function
\[
\theta\longmapsto h(R_je^{i\theta})
\]
is continuous and positive, so the displayed density defines a positive finite Borel measure.

Apply the given Poisson formula with $r=0$.
Since
\[
P_0\equiv1,
\]
we obtain the mean-value identity
\[
h(0)
=\frac1{2\pi}\int_0^{2\pi}h(R_je^{i\theta})\,d\theta
=\mu_j([0,2\pi]).
\]
:::

<1>2. After passing to a subsequence, the measures $\mu_j$ converge weak-* to a finite positive Borel measure $\mu$ on $[0,2\pi]$.
::: {.proof}
By the Riesz representation theorem, finite signed Borel measures on the compact interval $[0,2\pi]$ identify with the dual space
\[
C([0,2\pi])^*.
\]
For a positive measure, its dual norm is its total mass.
Hence <1>1 gives the uniform bound
\[
\|\mu_j\|=h(0).
\]

Banach--Alaoglu makes this bounded set weak-* compact.
Because $C([0,2\pi])$ is separable, bounded weak-* compact subsets of its dual are metrizable, so the sequence has a weak-* convergent subsequence.
Relabel it as $(\mu_j)$ and denote its weak-* limit by a functional $L$.

If $\varphi\in C([0,2\pi])$ satisfies $\varphi\ge0$, then
\[
L(\varphi)
=\lim_{j\to\infty}\int\varphi\,d\mu_j
\ge0.
\]
Thus $L$ is a positive functional.
By the Riesz representation theorem it is integration against a positive finite Borel measure $\mu$.
Therefore
\[
\int\varphi\,d\mu_j
\longrightarrow
\int\varphi\,d\mu
\]
for every fixed continuous $\varphi$.
:::

<1>3. Fix $0\le r<1$ and $\eta\in\mathbb R$.
For all sufficiently large $j$, so that $r<R_j$, the given Poisson formula yields
\[
h(re^{i\eta})
=\int_0^{2\pi}P_{r/R_j}(\eta-\theta)\,d\mu_j(\theta).
\]
::: {.proof}
For large $j$ we have $R_j>r$.
Applying the formula supplied in the problem at radius $R_j$ gives
\[
h(re^{i\eta})
=\frac1{2\pi}\int_0^{2\pi}
P_{r/R_j}(\eta-\theta)h(R_je^{i\theta})\,d\theta.
\]
The definition of $\mu_j$ in <1>1 turns this exactly into the displayed identity.
:::

<1>4. The functions
\[
\varphi_j(\theta)=P_{r/R_j}(\eta-\theta)
\]
converge uniformly on $[0,2\pi]$ to
\[
\varphi(\theta)=P_r(\eta-\theta).
\]
::: {.proof}
Since $R_j\to1$,
\[
\frac r{R_j}\longrightarrow r.
\]
Choose $q$ with
\[
r<q<1.
\]
For all sufficiently large $j$,
\[
0\le r/R_j\le q.
\]
The explicit Poisson kernel
\[
P_\rho(t)
=\operatorname{Re}\frac{1+\rho e^{it}}{1-\rho e^{it}}
=\frac{1-\rho^2}{1-2\rho\cos t+\rho^2}
\]
is continuous on the compact set
\[
[0,q]\times[0,2\pi].
\]
It is therefore uniformly continuous there.
Hence convergence of the parameter $r/R_j\to r$ implies uniform convergence in $\theta$.
:::

<1>5. One has
\[
\int_0^{2\pi}\varphi_j\,d\mu_j
\longrightarrow
\int_0^{2\pi}\varphi\,d\mu.
\]
::: {.proof}
Write
\[
\begin{aligned}
\left|\int\varphi_j\,d\mu_j-\int\varphi\,d\mu\right|
&\le
\left|\int(\varphi_j-\varphi)\,d\mu_j\right|
+\left|\int\varphi\,d\mu_j-\int\varphi\,d\mu\right|\\
&\le
\|\varphi_j-\varphi\|_\infty\mu_j([0,2\pi])
+\left|\int\varphi\,d\mu_j-\int\varphi\,d\mu\right|.
\end{aligned}
\]
By <1>1, the masses in the first term equal the fixed number $h(0)$, and by <1>4 the uniform norm tends to $0$.
The second term tends to $0$ by weak-* convergence from <1>2, since $\varphi$ is fixed and continuous.
Thus the entire expression tends to $0$.
:::

<1>6. The measure $\mu$ from <1>2 satisfies
\[
\boxed{
h(re^{i\eta})
=\int_0^{2\pi}P_r(\eta-\theta)\,d\mu(\theta)
}
\]
for every $re^{i\eta}\in\mathbb D$.
::: {.proof}
For fixed $r,\eta$, the left side of the identity in <1>3 is independent of $j$.
Taking $j\to\infty$ and applying <1>5 gives
\[
h(re^{i\eta})
=\int_0^{2\pi}P_r(\eta-\theta)\,d\mu(\theta).
\]
Since $r<1$ and $\eta$ were arbitrary, the representation holds throughout the open unit disk.
:::
:::
