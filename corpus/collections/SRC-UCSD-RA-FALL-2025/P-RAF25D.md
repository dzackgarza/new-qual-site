---
schema: qual/card@1
id: P-RAF25D
kind: problem
title: "Orthogonal projection onto the mean-zero subspace of L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Orthogonal Projection
  - L2 Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\Omega$ be a bounded, Lebesgue measurable subset of $\mathbb{R}^n$ such that $L^n(\Omega) > 0$, where $L^n$ is the Lebesgue measure on $\mathbb{R}^n$.
Let
$$
C := \left\{f \in L^2(\Omega) : \int_\Omega f(x) \, dx = 0\right\}.
$$

(1) Prove that $C$ is a closed subspace of $L^2(\Omega)$.

(2) Prove that for every $g \in L^2(\Omega)$ we have
$$
P_C(g) = g - \frac{1}{L^n(\Omega)} \int_\Omega g(x) \, dx,
$$
where $P_C(g)$ denotes the orthogonal projection of $g$ onto $C$.

(3) Prove that $C^\perp = \{g \in L^2(\Omega) : g = c \text{ a.e. in } \Omega \text{ for some } c \in \mathbb{C}\}$.
:::

::: solution
<1>1. Prove that $C$ is a closed subspace.
::: proof
Define
\[
L:L^2(\Omega)\to\mathbb C,
\qquad
L(f):=\int_\Omega f(x)\,dx.
\]
Since $\Omega$ is bounded, $L^n(\Omega)<\infty$, and Cauchy--Schwarz gives
\[
|L(f)|
\le L^n(\Omega)^{1/2}\|f\|_2.
\]
Thus $L$ is continuous. Moreover
\[
C=\ker L,
\]
so $C$ is a closed linear subspace of $L^2(\Omega)$.
:::

<1>2. Compute the orthogonal projection.
::: proof
For $g\in L^2(\Omega)$, set
\[
m_g:=\frac1{L^n(\Omega)}\int_\Omega g(x)\,dx
\]
and
\[
h:=g-m_g.
\]
Then
\[
\int_\Omega h
=\int_\Omega g-m_gL^n(\Omega)
=0,
\]
so $h\in C$.

Also $g-h=m_g$ is a constant function. For every $v\in C$,
\[
\langle g-h,v\rangle
=m_g\int_\Omega\overline{v(x)}\,dx
=0.
\]
Thus $g-h\in C^\perp$. By the characterization of orthogonal projection,
\[
\boxed{
P_C(g)
=g-\frac1{L^n(\Omega)}\int_\Omega g(x)\,dx.}
\]
:::

<1>3. Identify $C^\perp$.
::: proof
Every constant function belongs to $C^\perp$ by the calculation in Step 2. Conversely, let $g\in C^\perp$. By Step 2,
\[
g=P_C(g)+(g-P_C(g)),
\]
with
\[
P_C(g)\in C,
\qquad
g-P_C(g)\text{ constant}.
\]
Since $g\in C^\perp$ and $g-P_C(g)\in C^\perp$, their difference
\[
P_C(g)
\]
lies in $C\cap C^\perp=\{0\}$. Hence $g=g-P_C(g)$ is constant almost everywhere.

Therefore
\[
\boxed{
C^\perp
=\{g\in L^2(\Omega):g=c\text{ a.e. for some }c\in\mathbb C\}.}
\]
:::
:::
