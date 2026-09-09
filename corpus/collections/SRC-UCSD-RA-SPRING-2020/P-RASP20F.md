---
schema: qual/card@1
id: P-RASP20F
kind: problem
title: "Hausdorff moment problem characterization via polynomial inequalities"
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
  note: Checked against Problem 6 of the official UCSD Spring 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\{c_n\} \in \mathbb{R}$ ($n = 0, 1, 2, \ldots$). Prove that the following two conditions (1) and (2) are equivalent:

(1) There exists a signed Radon measure $\mu$ on $[0,1]$ such that
$$
\int_{[0,1]} t^n\,d\mu(t) = c_n \qquad (n = 0, 1, \ldots);
$$

(2) There exists $M \geq 0$ such that for any $N \in \mathbb{N}$ and any $a_n \in \mathbb{R}$ ($n = 0, \ldots, N$),
$$
\left|\sum_{n=0}^{N} a_n c_n\right| \leq M \max_{0 \leq t \leq 1} \left|\sum_{n=0}^{N} a_n t^n\right|.
$$
:::


::: solution
<1>1. Prove that (1) implies (2).
::: proof
Assume there is a signed Radon measure \(\mu\) on \([0,1]\) with
\[
\int_0^1 t^n\,d\mu(t)=c_n.
\]
Let
\[
p(t)=\sum_{n=0}^N a_nt^n.
\]
Then
\[
\sum_{n=0}^N a_nc_n
=\int_0^1 p(t)\,d\mu(t).
\]
Therefore
\[
\left|\sum_{n=0}^N a_nc_n\right|
\le \int_0^1|p|\,d|\mu|
\le |\mu|([0,1])\,\|p\|_\infty.
\]
Thus (2) holds with
\[
M=|\mu|([0,1]).
\]
:::

<1>2. Define a bounded linear functional on polynomials from (2).
::: proof
Assume (2). For a polynomial
\[
p(t)=\sum_{n=0}^N a_nt^n,
\]
define
\[
L(p):=\sum_{n=0}^N a_nc_n.
\]
The monomial representation of a polynomial is unique, so \(L\) is well defined and linear. Condition (2) gives
\[
|L(p)|\le M\|p\|_\infty.
\]
Hence \(L\) is bounded on the polynomial subspace of \(C([0,1])\).
:::

<1>3. Extend the functional and represent it by a signed Radon measure.
::: proof
By the Weierstrass approximation theorem, polynomials are uniformly dense in \(C([0,1])\). Since \(L\) is bounded in the uniform norm, it extends uniquely by continuity to a bounded linear functional
\[
\widetilde L:C([0,1])\to\mathbb R.
\]
By the Riesz--Markov representation theorem, there is a unique finite signed Radon measure \(\mu\) on \([0,1]\) such that
\[
\widetilde L(f)=\int_0^1 f(t)\,d\mu(t)
\qquad(f\in C([0,1])).
\]
Applying this to \(f(t)=t^n\) gives
\[
\int_0^1 t^n\,d\mu(t)
=\widetilde L(t^n)
=L(t^n)
=c_n
\]
for every \(n\ge0\). Thus (1) holds.

Therefore conditions (1) and (2) are equivalent.
:::
:::
