---
schema: qual/card@1
id: E-FGRFM
kind: problem
title: Metrizability of the one-point compactification
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S34.pdf, Exercise 34.5 (Theorem 3), page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S34.pdf, Internet Archive snapshot 20180827202044), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 34.5 with Propositions 5 and
    6, printed pp. 10-11 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against
    Munkres, Topology (2000), Section 34 Exercise 5, printed p. 218, Theorem 29.1, Theorem 29.2 and
    Exercise 30.4. Both implications are true, and the card's proof is Moller's: for a countable
    basis B, the neighbourhoods of infinity in the one-point compactification are the complements of
    compact sets, a countable basis of open sets with compact closures gives a countable increasing
    cover by compact sets, and a compact set lies in one of them; hence a countable basis of Y, and
    Y is compact Hausdorff, so Theorem 34.3 applies. Conversely a compact metrizable Y is second
    countable and X is an open subspace. What was corrected: Moller writes "For each point x in C
    there is a basis neighborhood Ux in B such that U is compact [Thm 29.3]", leaving the letter U
    undefined, and his 29.3 is a mis-citation -- Corollary 29.3 is about closed and open subspaces
    of a locally compact space, and the statement used is Theorem 29.2; the card states the cover by relatively compact basis elements, which is Exercise
    30.4's argument applied pointwise.
---

::: {.exercise}

Let $X$ be a locally compact Hausdorff space.
Let $Y$ be the one-point compactification of $X$.
Is it true that if $X$ has a countable basis, then $Y$ is metrizable?
Is it true that if $Y$ is metrizable, then $X$ has a countable basis?
:::

::: {.solution}
Both implications are true.

Assume first that $X$ has a countable basis. Since $X$ is locally compact Hausdorff, each point has a relatively compact open neighborhood. Refining the given countable basis, choose a countable cover
$$
U_1,U_2,\dots
$$
of $X$ by open sets with compact closures. Put
$$
K_n=\overline{U_1}\cup\cdots\cup\overline{U_n}.
$$
Then each $K_n$ is compact and $K_n\subset K_{n+1}$, while $\bigcup_nK_n=X$. If $K\subset X$ is compact, the open cover $\{U_n\}$ of $K$ has a finite subcover, hence $K\subset K_N$ for some $N$. Therefore the neighborhoods
$$
Y\setminus K_n
$$
form a countable local basis at the point at infinity in the one-point compactification $Y$. Together with a countable basis for $X$, they give a countable basis for $Y$. Since $Y$ is compact Hausdorff, the compact-Hausdorff metrization theorem yields that $Y$ is metrizable.

Conversely, if $Y$ is metrizable, then compactness of $Y$ implies $Y$ is second countable: for each $n$, choose a finite $1/n$-net and take balls with rational radii around the countable union of all chosen centers. Since $X=Y\setminus\{\infty\}$ is an open subspace, it inherits a countable basis.
:::
