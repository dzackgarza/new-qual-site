---
schema: qual/card@1
id: P-RAF21A
kind: problem
title: "Differentiable with derivative zero off a small exceptional set: when is f constant?"
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Borel Sets
  - Measure Zero Sets
  - Cantor Function
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UCSD Fall 2021 real-analysis exam source and remediated the existing malformed solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f \in C(\mathbb{R})$ and let $A \subseteq\mathbb{R}$ be a Borel set such that $f$ is differentiable at each $x \in \mathbb{R} \setminus A$ and $f'(x) = 0$ for all such $x$.

(a) If $A$ is closed and countable, show that $f$ is constant.

(b) If $A$ has Lebesgue measure $0$, must $f$ be constant?
Prove or find a counterexample.
:::

::: solution
<1>1. Prove part (a).
::: proof
Let $I$ be any connected component of $\mathbb R\setminus A$. Since $A$ is closed, $I$ is an open interval. On $I$, the function $f$ is differentiable and $f'=0$, so the mean value theorem shows that $f$ is constant on $I$.

Fix $u<v$. The complement $[u,v]\setminus A$ is a countable union of pairwise disjoint open intervals, and $f$ is constant on each such interval. Since $A\cap[u,v]$ is countable, the set
\[
f([u,v])
\]
is therefore countable: it is contained in the union of the countable set $f(A\cap[u,v])$ and one value for each component of $[u,v]\setminus A$.

But $f([u,v])$ is connected because $f$ is continuous and $[u,v]$ is connected. A connected countable subset of $\mathbb R$ is a singleton. Hence $f(u)=f(v)$. Since $u<v$ were arbitrary, $f$ is constant on $\mathbb R$.
:::

<1>2. Give a counterexample for part (b).
::: proof
No. Let $C$ be the middle-third Cantor set and let $F:[0,1]\to[0,1]$ be the Cantor--Lebesgue function. Extend $F$ to a continuous function on $\mathbb R$ by setting $F(x)=0$ for $x\le0$ and $F(x)=1$ for $x\ge1$.

The function is constant on every connected component of $\mathbb R\setminus C$, so it is differentiable there with derivative $0$. The Cantor set $C$ has Lebesgue measure $0$, but $F$ is not constant since $F(0)=0$ and $F(1)=1$. Thus a null exceptional set does not force constancy.
:::
:::
