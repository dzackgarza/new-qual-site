---
schema: qual/card@1
id: P-AMD-RH63H3SP
kind: problem
title: Finite-index subgroup cores and orders of simple groups
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Simple Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 7(a)-(b).
    Corrected the reversed index notation: the source assumes [G:H]=n and asks
    that [G:core(H)] divide n!.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Used the left action on the n cosets G/H. Its permutation representation
    has kernel core(H), so G/core(H) is isomorphic to a subgroup of S_n and
    its order divides n!. If G is simple, the properness of H forces the core
    to be trivial, giving |G| dividing n!.
---

::: {.problem}
Let $H<G$ be a proper subgroup of finite index
\[
[G:H]=n.
\]

1. Prove that
   \[
   [G:\operatorname{core}(H)]\mid n!.
   \]

2. If $G$ is simple, prove that
   \[
   |G|\mid n!,
   \]
   and in particular that $G$ is finite.
:::

::: {.solution}
Let
\[
\rho:G\longrightarrow\operatorname{Sym}(G/H)
\]
be the permutation representation afforded by left multiplication on the set of left cosets of $H$.

<1>1. The set $G/H$ has cardinality $n$, so
\[
\operatorname{Sym}(G/H)\cong S_n.
\]
::: {.proof}
By hypothesis,
\[
[G:H]=n.
\]
Thus there are exactly $n$ left cosets of $H$ in $G$, and the symmetric group on that set is isomorphic to $S_n$.
:::

<1>2. The kernel of $\rho$ is $\operatorname{core}(H)$.
::: {.proof}
This is the kernel characterization of the normal core: an element $x\in G$ acts trivially on every left coset exactly when
\[
x\in\bigcap_{g\in G}gHg^{-1}
=\operatorname{core}(H).
\]
Hence
\[
\ker\rho=\operatorname{core}(H).
\]
:::

<1>3. We have
\[
[G:\operatorname{core}(H)]\mid n!.
\]
::: {.proof}
By the first isomorphism theorem and <1>2,
\[
G/\operatorname{core}(H)\cong\rho(G).
\]
By <1>1,
\[
\rho(G)\le S_n.
\]
Therefore Lagrange's theorem gives
\[
|\rho(G)|\mid|S_n|=n!.
\]
Since
\[
|\rho(G)|
=|G/\operatorname{core}(H)|
=[G:\operatorname{core}(H)],
\]
the desired divisibility follows.
:::

<1>4. If $G$ is simple, then $\operatorname{core}(H)=\{e\}$.
::: {.proof}
The subgroup $\operatorname{core}(H)$ is normal in $G$ and satisfies
\[
\operatorname{core}(H)\le H<G.
\]
Thus it is a proper normal subgroup of $G$.
Since $G$ is simple, it must be trivial:
\[
\operatorname{core}(H)=\{e\}.
\]
:::

<1>5. If $G$ is simple, then $|G|\mid n!$ and $G$ is finite.
::: {.proof}
By <1>4,
\[
[G:\operatorname{core}(H)]
=[G:\{e\}]
=|G|.
\]
Applying <1>3 gives
\[
|G|\mid n!.
\]
In particular, $|G|\le n!<\infty$, so $G$ is finite.
:::
:::
