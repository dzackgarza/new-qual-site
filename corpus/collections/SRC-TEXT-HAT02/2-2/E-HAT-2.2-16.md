---
schema: qual/card@1
id: E-HAT-2.2-16
kind: problem
title: Ranks of simplicial chain groups of $\Delta^n$ and homology of skeleta
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 16; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular-chain proof checked.
---

::: {.problem}
Let $\Delta^n = [\nu_0, \cdots, \nu_n]$ have its natural $\Delta$-complex structure with $k$ simplices $[\nu_{i_0}, \cdots, \nu_{i_k}]$ for $i_0 < \cdots < i_k$.
Compute the ranks of the simplicial (or cellular) chain groups $\Delta_i(\Delta^n)$ and the subgroups of cycles and boundaries.
[Hint: Pascal's triangle.] Apply this to show that the $k$ skeleton of $\Delta^n$ has homology groups $\tilde{H}_i((\Delta^n)^k)$ equal to 0 for $i < k$, and free of rank $\binom{n}{k+1}$ for $i = k$.
:::

::: {.solution}
For the standard simplex $\Delta^n$, the group of $i$-chains is free on the $(i+1)$-element subsets of its $n+1$ vertices. Hence
\[
\operatorname{rank} C_i(\Delta^n)=\binom{n+1}{i+1}.
\]

<1>1. In the reduced simplicial chain complex of $\Delta^n$,
\[
\operatorname{rank} Z_i
=
\operatorname{rank} B_i
=
\binom{n}{i+1}
\qquad (0\le i\le n).
\]
Here $\binom{n}{n+1}=0$.
::: {.proof}
The simplex is contractible, so its reduced chain complex is exact. Thus
\[
Z_i=B_i
\]
for all $i\ge0$. Since
\[
0\to Z_i\to C_i\xrightarrow{\partial_i}B_{i-1}\to0
\]
is exact, ranks satisfy
\[
\operatorname{rank} Z_i
=
\binom{n+1}{i+1}-\operatorname{rank} B_{i-1}.
\]
Starting with
\[
\operatorname{rank}B_{-1}=1
\]
in the augmented complex and using Pascal's identity gives inductively
\[
\operatorname{rank}Z_i
=
\binom{n+1}{i+1}-\binom{n}{i}
=
\binom{n}{i+1}.
\]
Exactness gives the same formula for $B_i$.
:::

<1>2. In the ordinary chain complex,
\[
\operatorname{rank}Z_0=n+1,
\qquad
\operatorname{rank}B_0=n,
\]
and for $i\ge1$ the formulas of <1>1 remain valid.
::: {.proof}
Ordinarily $\partial_0=0$, so $Z_0=C_0$ has rank $n+1$. The augmentation kernel has rank $n$, and because $\Delta^n$ is connected this kernel is $B_0$. For $i\ge1$, reduced and ordinary chains agree.
:::

Now let
\[
K=(\Delta^n)^k
\]
be the $k$-skeleton.

<1>3. For $i<k$,
\[
\widetilde H_i(K)=0.
\]
::: {.proof}
In degrees at most $k$, the chain groups and boundary maps of $K$ agree with those of the full simplex. If $i<k$, then both $C_i$ and $C_{i+1}$ are present, so
\[
Z_i(K)=Z_i(\Delta^n),
\qquad
B_i(K)=B_i(\Delta^n).
\]
Since the full simplex has zero reduced homology, the quotient $Z_i/B_i$ is zero.
:::

<1>4. In degree $k$,
\[
\widetilde H_k(K)\cong\mathbb Z^{\binom{n}{k+1}}.
\]
::: {.proof}
There are no $(k+1)$-chains in the $k$-skeleton, so
\[
B_k(K)=0.
\]
On the other hand the boundary map out of $C_k$ is unchanged, hence
\[
Z_k(K)=Z_k(\Delta^n).
\]
By <1>1 this is free of rank
\[
\binom{n}{k+1}.
\]
Therefore
\[
\boxed{
\widetilde H_i((\Delta^n)^k)=
\begin{cases}
0,&i<k,\\
\mathbb Z^{\binom{n}{k+1}},&i=k.
\end{cases}}
\]
:::
:::
