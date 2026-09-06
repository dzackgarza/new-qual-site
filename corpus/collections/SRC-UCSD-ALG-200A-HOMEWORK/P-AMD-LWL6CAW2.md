---
schema: qual/card@1
id: P-AMD-LWL6CAW2
kind: problem
title: A normal Hall subgroup is unique among subgroups of its order
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    The official UCSD Math 200A Fall 2016 Homework 1 assigns Dummit--Foote
    Section 3.2 Exercises 18 and 19. Exercise 19 is the stated uniqueness
    result, following the coprime order/index lemma of Exercise 18.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For an arbitrary subgroup H of order |N|, restricted the quotient map
    G -> G/N to H. Its image order divides both |H| = |N| and [G:N], so
    coprimality forces a trivial image; hence H lies in N and equality of
    finite orders gives H = N.
---

::: {.problem}
Given: $|G| < \infty, N \normal G, (|N|, [G:N]) =1$

Show: $N$ is the unique subgroup of order $|N|$
:::

::: {.solution}
Let $H\le G$ be any subgroup with $|H|=|N|$, and let
\[
\pi:G\longrightarrow G/N
\]
be the quotient homomorphism.

<1>1. The integer $|\pi(H)|$ divides $|N|$.
::: {.proof}
The restriction
\[
\pi|_H:H\longrightarrow G/N
\]
has kernel $H\cap N$.
Hence the first isomorphism theorem gives
\[
\pi(H)\cong H/(H\cap N).
\]
Therefore
\[
|\pi(H)|=[H:H\cap N]\mid |H|=|N|.
\]
:::

<1>2. The integer $|\pi(H)|$ divides $[G:N]$.
::: {.proof}
The image $\pi(H)$ is a subgroup of the finite group $G/N$.
By Lagrange's theorem,
\[
|\pi(H)|\mid |G/N|=[G:N].
\]
:::

<1>3. The subgroup $H$ is contained in $N$.
::: {.proof}
By <1>1 and <1>2, $|\pi(H)|$ divides both $|N|$ and $[G:N]$.
Since
\[
\gcd(|N|,[G:N])=1,
\]
we have $|\pi(H)|=1$.
Thus $\pi(H)=\{N\}$, so every $h\in H$ lies in
\[
\ker\pi=N.
\]
Hence $H\le N$.
:::

<1>4. Therefore $H=N$.
::: {.proof}
By <1>3, $H\le N$, while by assumption
\[
|H|=|N|<\infty.
\]
A subgroup of a finite group having the same order as the whole group is the whole group.
Hence $H=N$.
Since $H$ was arbitrary among subgroups of order $|N|$, $N$ is the unique subgroup of $G$ of that order.
:::
:::
