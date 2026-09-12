---
schema: qual/card@1
id: P-RAF04E
kind: problem
title: "Convergence of complex measures: total variation summability and domination by a positive measure"
classification:
  areas:
  - real-analysis
  topics:
  - Complex Measures
  - Total Variation
  - Measure Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose that $\{\nu_n\}_{n=1}^\infty$ are complex measures and $\mu$ is a finite positive measure on a measurable space $(X, \mathcal{M})$.
Further let $|\nu_n|$ denote the total variation measure associated to $\nu_n$.

(a) If $\sum_{n=1}^\infty |\nu_n|(X) < \infty$, then $\nu := \sum_{n=1}^\infty \nu_n$ is a complex measure.

(b) If $|\nu_n(A)| \leq \mu(A)$ and $\nu(A) := \lim_{n \to \infty} \nu_n(A)$ exists for all $A \in \mathcal{M}$, then $\nu : \mathcal{M} \to \mathbb{C}$ is a complex measure.
:::

::: solution
<1>1. Prove part (a).
::: proof
For every $A\in\mathcal M$,
\[
|\nu_n(A)|\le |\nu_n|(A)\le |\nu_n|(X).
\]
Hence
\[
\sum_{n=1}^\infty |\nu_n(A)|<\infty,
\]
so
\[
\nu(A):=\sum_{n=1}^\infty\nu_n(A)
\]
is well defined.

Let $(A_k)_{k\ge1}$ be pairwise disjoint and put $A=\bigcup_{k\ge1}A_k$. Then
\[
\begin{aligned}
\sum_{n=1}^\infty\sum_{k=1}^\infty |\nu_n(A_k)|
&\le \sum_{n=1}^\infty\sum_{k=1}^\infty |\nu_n|(A_k)\\
&=\sum_{n=1}^\infty |\nu_n|(A)\\
&\le\sum_{n=1}^\infty |\nu_n|(X)<\infty.
\end{aligned}
\]
Thus the double series is absolutely convergent, so its order may be interchanged. Using countable additivity of each $\nu_n$,
\[
\begin{aligned}
\nu(A)
&=\sum_{n=1}^\infty \nu_n(A)
=\sum_{n=1}^\infty\sum_{k=1}^\infty\nu_n(A_k)\\
&=\sum_{k=1}^\infty\sum_{n=1}^\infty\nu_n(A_k)
=\sum_{k=1}^\infty\nu(A_k).
\end{aligned}
\]
Hence $\nu$ is a complex measure.
:::

<1>2. Prove finite additivity and domination in part (b).
::: proof
Since $|\nu_n(A)|\le\mu(A)$ for every $n$,
\[
|\nu(A)|\le\mu(A)
\]
by passage to the limit.

If $A,B\in\mathcal M$ are disjoint, then
\[
\begin{aligned}
\nu(A\cup B)
&=\lim_{n\to\infty}\nu_n(A\cup B)\\
&=\lim_{n\to\infty}\bigl(\nu_n(A)+\nu_n(B)\bigr)\\
&=\nu(A)+\nu(B).
\end{aligned}
\]
Thus $\nu$ is finitely additive.
:::

<1>3. Upgrade finite additivity to countable additivity.
::: proof
Let $(A_k)_{k\ge1}$ be pairwise disjoint, let
\[
A=\bigcup_{k=1}^\infty A_k,
\qquad
B_N=\bigcup_{k>N}A_k.
\]
Finite additivity gives
\[
\nu(A)=\sum_{k=1}^N\nu(A_k)+\nu(B_N).
\]
Therefore
\[
\left|\nu(A)-\sum_{k=1}^N\nu(A_k)\right|
=|\nu(B_N)|
\le\mu(B_N).
\]
The sets $B_N$ decrease to the empty set. Since $\mu$ is finite,
\[
\mu(B_N)\longrightarrow0.
\]
Hence
\[
\nu(A)=\sum_{k=1}^\infty\nu(A_k).
\]
Thus $\nu$ is countably additive and therefore a complex measure.
:::
:::
