---
schema: qual/card@1
id: P-XKFPD
kind: problem
title: Bessel's inequality and reconstruction from an orthonormal sequence
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
relations:
- kind: related-to
  target: P-FCOU3
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(u_n)_{n=1}^\infty$ be an orthonormal sequence in a Hilbert space $H$.

(a) For $x\in H$, prove that for every $N$,
\[
\left\|x-\sum_{n=1}^{N}\langle x,u_n\rangle u_n\right\|_H^2
=
\|x\|_H^2-
\sum_{n=1}^{N}|\langle x,u_n\rangle|^2,
\]
and deduce Bessel's inequality
\[
\sum_{n=1}^{\infty}|\langle x,u_n\rangle|^2\le \|x\|_H^2.
\]

(b) If $(a_n)\in\ell^2(\mathbb N)$, prove that there is $x\in H$ such that
\[
\langle x,u_n\rangle=a_n
\quad\text{for every }n,
\]
and $x$ may be chosen so that
\[
\|x\|_H=\left(\sum_{n=1}^{\infty}|a_n|^2\right)^{1/2}.
\]

(c) Prove that if $(u_n)$ is complete, then Bessel's inequality is an equality.
:::

::: solution
<1>1. Prove the finite orthogonal-projection identity and Bessel's inequality.
::: proof
Set
\[
s_N:=\sum_{n=1}^N\langle x,u_n\rangle u_n.
\]
For each $1\le k\le N$,
\[
\langle x-s_N,u_k\rangle
=
\langle x,u_k\rangle-
\sum_{n=1}^N\langle x,u_n\rangle\langle u_n,u_k\rangle
=0.
\]
Thus $x-s_N$ is orthogonal to $s_N$. By Pythagoras,
\[
\|x\|^2
=
\|x-s_N\|^2+\|s_N\|^2.
\]
Since the $u_n$ are orthonormal,
\[
\|s_N\|^2
=
\sum_{n=1}^N|\langle x,u_n\rangle|^2.
\]
Therefore
\[
\left\|x-\sum_{n=1}^{N}\langle x,u_n\rangle u_n\right\|^2
=
\|x\|^2-
\sum_{n=1}^{N}|\langle x,u_n\rangle|^2.
\]
The left side is nonnegative, so
\[
\sum_{n=1}^{N}|\langle x,u_n\rangle|^2\le\|x\|^2
\]
for every $N$. Letting $N\to\infty$ gives
\[
\boxed{
\sum_{n=1}^{\infty}|\langle x,u_n\rangle|^2\le\|x\|^2.}
\]
:::

<1>2. Reconstruct a vector from square-summable coefficients.
::: proof
Let $(a_n)\in\ell^2$ and define
\[
S_N:=\sum_{n=1}^N a_nu_n.
\]
For $M>N$, orthonormality gives
\[
\|S_M-S_N\|^2
=
\sum_{n=N+1}^M|a_n|^2.
\]
Since $(a_n)\in\ell^2$, the right side tends to $0$ as $M,N\to\infty$. Hence $(S_N)$ is Cauchy. Completeness of $H$ gives some $x\in H$ with
\[
S_N\to x.
\]
For each fixed $k$, continuity of the inner product yields
\[
\langle x,u_k\rangle
=
\lim_{N\to\infty}\langle S_N,u_k\rangle
=a_k.
\]
Also
\[
\|x\|^2
=
\lim_{N\to\infty}\|S_N\|^2
=
\sum_{n=1}^{\infty}|a_n|^2.
\]
Thus $x$ has the required coefficients and norm.
:::

<1>3. Prove Parseval's identity when the orthonormal sequence is complete.
::: proof
Fix $x\in H$. By Bessel's inequality, the coefficient sequence
\[
a_n:=\langle x,u_n\rangle
\]
belongs to $\ell^2$. By Step 2, the series
\[
s:=\sum_{n=1}^{\infty}a_nu_n
\]
converges in $H$. For every $k$,
\[
\langle x-s,u_k\rangle
=
a_k-a_k=0.
\]
Thus $x-s$ is orthogonal to every $u_k$. Completeness of the orthonormal sequence means that the only vector orthogonal to every $u_k$ is $0$, so $x=s$. Therefore Step 2 gives
\[
\boxed{
\|x\|^2=
\sum_{n=1}^{\infty}|\langle x,u_n\rangle|^2.}
\]
:::
:::
