---
schema: qual/card@1
id: P-RASP22A
kind: problem
title: "True/false on integral inequalities, L^2 convergence, and Radon measures"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Determine if each of the following statements is true or false.

1. If $f, g : \mathbb{R} \to \mathbb{R}$ belong to $L^1(\mathbb{R})$ and satisfy $\int_{-\infty}^{x} f(t)\,dt \leq \int_{-\infty}^{x} g(t)\,dt$ for all $x \in \mathbb{R}$, then $f \leq g$ almost everywhere.

2. Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and let $f_n \in L^2(X)$ be a sequence.
   If $\sup_{n \in \mathbb{N}} \|f_n\|_2 < \infty$ and $f_n \to f$ almost everywhere, then $\int_X f_n\,d\mu \to \int_X f\,d\mu$.

3. Let $\mu$ be a Radon measure on an LCH space $X$ and let $A$ be an open subset of $X$.
   Define $\mu_A(E) = \mu(A \cap E)$.
   Then $\mu_A$ is a Radon measure.
:::


::: solution
<1>1. Statement 1 is false.
::: proof
Take $g=0$ and
\[
f=-\mathbf1_{(0,1)}+\mathbf1_{(1,2)}.
\]
Then $f,g\in L^1(\mathbb R)$. Its cumulative integral is
\[
\int_{-\infty}^x f(t)\,dt
=
\begin{cases}
0,&x\le0,\\
-x,&0<x\le1,\\
x-2,&1<x\le2,\\
0,&x>2,
\end{cases}
\]
which is always $\le0=\int_{-\infty}^xg$. But $f=1>0=g$ on $(1,2)$. Thus the asserted pointwise a.e. order does not follow.
:::

<1>2. Statement 2 is true.
::: proof
Let
\[
M:=\sup_n\|f_n\|_2<\infty.
\]
By Fatou,
\[
\|f\|_2^2\le\liminf_n\|f_n\|_2^2\le M^2,
\]
so $f\in L^2(X)$. Since $\mu(X)<\infty$, for every measurable $E$,
\[
\int_E|f_n|\,d\mu
\le \|f_n\|_2\mu(E)^{1/2}
\le M\mu(E)^{1/2}.
\]
Thus $(f_n)$ is uniformly integrable in $L^1$. Since $f_n\to f$ almost everywhere, it also converges to $f$ in measure. Vitali's theorem therefore gives
\[
\|f_n-f\|_1\to0.
\]
Hence
\[
\left|\int_Xf_n\,d\mu-\int_Xf\,d\mu\right|
\le\|f_n-f\|_1\to0.
\]
:::

<1>3. Statement 3 is true.
::: proof
Because $A$ is open, it is Borel, so $\mu_A(E)=\mu(A\cap E)$ defines a Borel measure. If $K\subseteq X$ is compact, then
\[
\mu_A(K)=\mu(A\cap K)\le\mu(K)<\infty,
\]
so $\mu_A$ is finite on compact sets.

Let $E$ be Borel. Since $\mu$ is Radon,
\[
\mu_A(E)=\mu(A\cap E)
=\sup\{\mu(K):K\subseteq A\cap E,\ K\text{ compact}\}.
\]
For every such $K$, $\mu_A(K)=\mu(K)$. Therefore
\[
\mu_A(E)
=\sup\{\mu_A(K):K\subseteq E,\ K\text{ compact}\}.
\]
Thus $\mu_A$ is inner regular and finite on compact sets, hence Radon.
:::
:::
