---
schema: qual/card@1
id: E-PYCIE
kind: problem
title: Closed subspaces of $\RR^N$ have dimension at most $N$
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 10, printed p. 317, with Theorem 50.6 and the
    argument of Theorem 50.1. What was corrected: the first step said only that R^N "has covering dimension N"
    and called this a standard computation, without a proof and with an equality the book never proves; it now
    says what is true and available, that the construction in the proof of Theorem 50.6 gives, for every delta,
    an open cover of R^N of order N+1 by sets of diameter less than delta, whence dimension at most N. The
    second step is the closed-subspace argument of Theorem 50.1 and is now labelled as such.
---

::: {.exercise}

Corollary.
Every closed subspace of $\RR^N$ has topological dimension at most $N$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\RR^N$ has covering dimension at most $N$.

::: pf-proof

This is Theorem 50.6's construction, which is Example 3 generalized: for each $\delta>0$ the proof exhibits an open cover of $\RR^N$ of order $N+1$ whose elements have diameter less than $\delta$, by scaling the cover built from the unit cubes, their faces and the balls about the lattice points. Since any open cover of $\RR^N$ has a Lebesgue number, such covers refine it, so $\dim\RR^N\le N$.

:::

:::

::: {.pf-step #s2}

A closed subspace $A$ of a space $X$ with $\dim X \le N$ has $\dim A \le N$.

::: pf-proof

Let $\mathcal{U}$ be an open cover of $A$. Each $U \in \mathcal{U}$ is $A \cap U'$ for some open $U' \subseteq X$. The sets $U'$ together with $X \setminus A$ form an open cover of $X$, which has an open refinement $\mathcal{V}$ of order at most $N + 1$. The sets $V \cap A$, $V \in \mathcal{V}$, form an open cover of $A$ of order at most $N + 1$; each $V$ meeting $A$ lies in some $U'$, since $X \setminus A$ misses $A$, so $V \cap A$ lies in the corresponding $U$.

:::

:::

::: pf-qed

Apply step [](#s2){.pf-ref} to $X = \RR^N$, using step [](#s1){.pf-ref}; step [](#s2){.pf-ref} is the argument of Theorem 50.1.

:::

:::

:::
