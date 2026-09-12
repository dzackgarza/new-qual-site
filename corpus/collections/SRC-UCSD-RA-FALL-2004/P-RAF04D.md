---
schema: qual/card@1
id: P-RAF04D
kind: problem
title: "Pointwise limit of bounded linear operators between Banach spaces is bounded"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Bounded Operators
  - Uniform Boundedness Principle
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose $T_n : X \to Y$ for $n \in \mathbb{N}$ is a sequence of bounded linear operators between two Banach spaces $X$ and $Y$.
Further assume that $\lim_{n \to \infty} T_n x$ exists for all $x \in X$.
Show that $Tx := \lim_{n \to \infty} T_n x$ defines a bounded linear operator from $X$ to $Y$.
:::

::: solution
<1>1. The pointwise limit is linear.
::: proof
For $x,y\in X$ and scalars $a,b$,
\[
\begin{aligned}
T(ax+by)
&=\lim_{n\to\infty}T_n(ax+by)\\
&=\lim_{n\to\infty}\bigl(aT_nx+bT_ny\bigr)\\
&=aTx+bTy.
\end{aligned}
\]
Thus $T:X\to Y$ is linear.
:::

<1>2. The family $(T_n)$ is uniformly bounded in operator norm.
::: proof
For every fixed $x\in X$, the sequence $(T_nx)$ converges in $Y$, hence is bounded. Therefore
\[
\sup_n\|T_nx\|_Y<\infty
\qquad\text{for every }x\in X.
\]
Since $X$ is Banach, the Uniform Boundedness Principle applies and gives a constant $C<\infty$ such that
\[
\sup_n\|T_n\|_{X\to Y}\le C.
\]
:::

<1>3. The pointwise limit is bounded.
::: proof
For every $x\in X$,
\[
\|Tx\|_Y
=\left\|\lim_{n\to\infty}T_nx\right\|_Y
=\lim_{n\to\infty}\|T_nx\|_Y
\le C\|x\|_X.
\]
Hence $T$ is bounded and
\[
\|T\|_{X\to Y}\le C.
\]
Thus $T$ is a bounded linear operator from $X$ to $Y$.
:::
:::
