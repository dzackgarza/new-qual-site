---
schema: qual/card@1
id: P-RASP20A
kind: problem
title: "True/false on measure approximation, derivative measurability, pigeonhole, and closedness"
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
  note: Checked against Problem 1 of the official UCSD Spring 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Determine if each of the following statements is true or false.

(1) Let $E$ be a Lebesgue-measurable subset of $\mathbb{R}$.
For each $k \in \mathbb{N}$, let $E_k = \{x \in \mathbb{R} : \operatorname{dist}(x, E) < 1/k\}$.
Then $\lim_{k \to \infty} m(E_k) = m(E)$.

(2) If $f : (0,1) \to \mathbb{R}$ is differentiable at each point $x \in (0,1)$, then the derivative $f' : (0,1) \to \mathbb{R}$ is Borel-measurable on $(0,1)$.

(3) Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) = 1$.
Let $E_j \in \mathcal{M}$ ($j = 1, \ldots, n$). Let $q$ be an integer such that $1 \leq q \leq n$.
Assume that any $x \in X$ belongs to at least $q$ of these subsets $E_1, \ldots, E_n$.
Then there exists $j_0$ such that $\mu(E_{j_0}) \geq q/n$.

(4) The space $C([0,1])$ is a closed subspace of $L^1([0,1], m)$ with respect to the $L^1$-norm.
:::


::: solution
<1>1. Statement (1) is false.
::: proof
Take
\[
E=\mathbb Q\cap[0,1].
\]
Then \(E\) is Lebesgue measurable and \(m(E)=0\), but it is dense in \([0,1]\). Hence
\[
\operatorname{dist}(x,E)=\operatorname{dist}(x,[0,1]),
\]
so
\[
E_k=(-1/k,1+1/k).
\]
Therefore
\[
m(E_k)=1+2/k\longrightarrow1\ne0=m(E).
\]
Thus the assertion is false.
:::

<1>2. Statement (2) is true.
::: proof
A differentiable function is continuous, hence Borel measurable. For each \(n\ge2\), define the Borel function
\[
q_n(x)=
\begin{cases}
n\bigl(f(x+1/n)-f(x)\bigr),&x<1-1/n,\\
n\bigl(f(x)-f(x-1/n)\bigr),&x\ge1-1/n.
\end{cases}
\]
For each fixed \(x\in(0,1)\), eventually \(x<1-1/n\), and differentiability gives
\[
q_n(x)\longrightarrow f'(x).
\]
Thus \(f'\) is a pointwise limit of Borel functions and is therefore Borel measurable.
:::

<1>3. Statement (3) is true.
::: proof
The hypothesis says
\[
\sum_{j=1}^n\mathbf1_{E_j}(x)\ge q
\qquad\text{for every }x\in X.
\]
Integrating,
\[
\sum_{j=1}^n\mu(E_j)
=\int_X\sum_{j=1}^n\mathbf1_{E_j}\,d\mu
\ge q\mu(X)=q.
\]
Hence at least one term satisfies
\[
\boxed{\mu(E_{j_0})\ge q/n.}
\]
:::

<1>4. Statement (4) is false.
::: proof
Let
\[
f=\mathbf1_{[0,1/2]}.
\]
Continuous piecewise-linear functions obtained by smoothing the jump on an interval of width \(1/n\) converge to \(f\) in \(L^1([0,1])\). Thus \(f\) lies in the \(L^1\)-closure of \(C([0,1])\).

But the \(L^1\)-class of \(f\) has no continuous representative: any continuous representative equal to \(1\) almost everywhere on \((0,1/2)\) must equal \(1\) everywhere there by continuity, and similarly must equal \(0\) everywhere on \((1/2,1)\), contradicting continuity at \(1/2\). Hence \(f\notin C([0,1])\) as an \(L^1\)-class.

Therefore \(C([0,1])\) is not closed in \(L^1([0,1])\).
:::
:::
