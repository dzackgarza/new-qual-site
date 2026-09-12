---
schema: qual/card@1
id: E-AMD-AY43ETMO
kind: problem
title: $A_n$ is simple for $n\geq 5$
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Argue that $A_n$ is simple for $n \geq 5$.
:::

::: {.solution}
We prove by induction on \(n\ge5\) that \(A_n\) is simple.

<1>1. The group \(A_5\) is simple.
::: {.proof}
Its conjugacy classes have sizes
\[
1,\ 15,\ 20,\ 12,\ 12.
\]
A normal subgroup is a union of conjugacy classes containing the identity, and its order must divide \(60\). No proper nontrivial sum of these class sizes containing \(1\) divides \(60\). Hence the only normal subgroups are \(1\) and \(A_5\).
:::

<1>2. Assume \(n\ge6\) and \(A_{n-1}\) is simple. Let \(N\trianglelefteq A_n\) be nontrivial.
::: {.proof}
For each point \(i\), let
\[
H_i=\operatorname{Stab}_{A_n}(i)\cong A_{n-1}.
\]
Then \(N\cap H_i\trianglelefteq H_i\), so by induction
\[
N\cap H_i=1\quad\text{or}\quad H_i.
\]
If \(N\cap H_i=H_i\) for some \(i\), then \(N\) contains a \(3\)-cycle. All \(3\)-cycles are conjugate in \(A_n\), and they generate \(A_n\), so \(N=A_n\).

Suppose instead that \(N\cap H_i=1\) for every \(i\). Then every nonidentity element of \(N\) is fixed-point-free. Choose \(1\ne\sigma\in N\).

For \(n\ge7\), choose \(a\) with \(\sigma(a)=b\ne a\), and choose distinct points \(c,d\) outside \({a,b}\). Put \(\tau=(a\ c\ d)\). Then \(\sigma\tau\sigma^{-1}\) is supported on \(\{b,\sigma(c),\sigma(d)\}\), whereas \(\tau\) is supported on \(\{a,c,d\}\). These supports are different because the former contains \(b\) and the latter does not. Hence \(\tau\) does not commute with \(\sigma\). Then
\[
\rho=\sigma\tau\sigma^{-1}\tau^{-1}\in N
\]
is nontrivial. Its support is contained in the union of the supports of the two \(3\)-cycles \(\sigma\tau\sigma^{-1}\) and \(\tau^{-1}\), hence has size at most \(6<n\). Thus \(\rho\) fixes a point, contradicting \(N\cap H_i=1\).

For \(n=6\), a fixed-point-free even permutation has cycle type \((3)(3)\) or \((4)(2)\). After relabeling, in the first case take \(\sigma=(1\ 2\ 3)(4\ 5\ 6)\) and \(S=\{1,2,4\}\); then \(\sigma(S)=\{2,3,5\}\). In the second case take \(\sigma=(1\ 2\ 3\ 4)(5\ 6)\) and \(S=\{1,2,5\}\); then \(\sigma(S)=\{2,3,6\}\). Thus in either case \(S\cap\sigma(S)\ne\varnothing\) but \(S\ne\sigma(S)\). Let \(\tau\) be a \(3\)-cycle supported on \(S\). Then \(\sigma\tau\sigma^{-1}\ne\tau\), so the same commutator \(\rho\) is nontrivial, and its support is contained in \(S\cup\sigma(S)\), which has \(5\) points. Hence \(\rho\) fixes a point, again a contradiction.

Therefore some \(N\cap H_i\) is nontrivial, and the first paragraph gives \(N=A_n\).
:::

Thus \(A_n\) is simple for every \(n\ge5\).
:::
