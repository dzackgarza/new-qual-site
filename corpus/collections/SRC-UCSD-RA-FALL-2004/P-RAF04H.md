---
schema: qual/card@1
id: P-RAF04H
kind: problem
title: "Iterated integral operators produce a uniformly convergent subsequence (Arzela-Ascoli)"
classification:
  areas:
  - real-analysis
  topics:
  - Arzela-Ascoli Theorem
  - Compact Operators
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $G : \mathbb{R} \to \mathbb{R}$ be a bounded Borel measurable function.
Define $f_0(t) = 1$ and $f_n : [-1, 1] \to \mathbb{R}$ inductively by
$$
f_{n+1}(t) = 1 + \int_0^t G(f_n(\tau)) \, d\tau.
$$

Show:

(a) $f_n$ are well defined and $f_n \in C([-1, 1], \mathbb{R})$ for all $n$.

(b) The sequence $\{f_n\}_{n=1}^\infty$ has a uniformly convergent subsequence.
:::

::: solution
<1>1. Prove that the recursion is well defined and produces continuous functions.
::: proof
Let
\[
M:=\sup_{x\in\mathbb R}|G(x)|<\infty.
\]
The function $f_0\equiv1$ is continuous. Suppose inductively that $f_n$ is continuous. Then $f_n$ is Borel measurable, so the composition $G\circ f_n$ is Borel measurable. It is also bounded by $M$, hence integrable on $[-1,1]$.

Therefore
\[
f_{n+1}(t)=1+\int_0^t G(f_n(\tau))\,d\tau
\]
is well defined for every $t\in[-1,1]$. In fact it is absolutely continuous, hence continuous. By induction, every $f_n$ is well defined and belongs to $C([-1,1])$.
:::

<1>2. Establish uniform boundedness and equicontinuity.
::: proof
For $n\ge0$ and $t\in[-1,1]$,
\[
|f_{n+1}(t)|
\le 1+\int_0^t|G(f_n(\tau))|\,|d\tau|
\le 1+M.
\]
Also, for $s,t\in[-1,1]$,
\[
\begin{aligned}
|f_{n+1}(t)-f_{n+1}(s)|
&=\left|\int_s^t G(f_n(\tau))\,d\tau\right|\\
&\le M|t-s|.
\end{aligned}
\]
Thus $(f_n)_{n\ge1}$ is uniformly bounded and equi-Lipschitz, hence equicontinuous.
:::

<1>3. Apply Arzelà--Ascoli.
::: proof
The domain $[-1,1]$ is compact. By Step 2, the family $\{f_n:n\ge1\}$ is uniformly bounded and equicontinuous. The Arzelà--Ascoli theorem therefore implies that every sequence in this family has a uniformly convergent subsequence. In particular,
\[
\boxed{\{f_n\}_{n=1}^\infty\text{ has a uniformly convergent subsequence}.}
\]
:::
:::
