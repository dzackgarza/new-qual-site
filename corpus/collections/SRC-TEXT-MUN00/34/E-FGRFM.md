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

The retained published solutions are **Jesper Michael Moller, "Solutions to exercises in Munkres", S34.pdf, Exercise 34.5 (Theorem 3), page 1 of the file** (`tmp/sources/munkres-solutions-poulsen-S34.pdf`) and **"Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 34.5 with Propositions 5 and 6, printed pp. 10--11** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`); both answers are yes and the argument below is Moller's, with the exhaustion by compact sets, the countable base at infinity and the two metrizability steps as separate steps. Two points are the card's own: Moller leaves the letter $U$ undefined in "there is a basis neighborhood $U_{x}$ in $\mathcal{B}$ such that $U$ is compact" and cites Corollary 29.3, which concerns subspaces of a locally compact space rather than this statement, the relevant result being Theorem 29.2 — so the card states the cover by relatively compact *basic* open sets explicitly; and it separates the two directions rather than running them together.

Let $X$ be locally compact Hausdorff with one-point compactification $Y=X\cup\{\infty\}$.

::: pf

::: {.pf-step #exhaust}
If $X$ has a countable basis, then $X=\bigcup_{n}K_{n}$ with each $K_{n}$ compact, $K_{n}\subseteq K_{n+1}$, and every compact subset of $X$ lying in some $K_{n}$.

::: pf-proof
Each point of $X$ has an open neighbourhood with compact closure (local compactness, Theorem 29.1's setting). From the countable basis choose a countable family $\theset{U_{n}}$ of such open sets with compact closures covering $X$ — possible since the basis is countable and only the basic sets with compact closure are needed. Put $K_{n}=\overline{U_{1}}\cup\cdots\cup\overline{U_{n}}$, compact and increasing, with union $X$. If $K\subseteq X$ is compact, the $U_{n}$ cover $K$, so finitely many cover it and $K\subseteq K_{N}$ for that $N$.
:::

:::

::: {.pf-step #base-at-infinity}
The sets $Y\setminus K_{n}$ form a countable neighbourhood base at $\infty$.

::: pf-proof
Each $Y\setminus K_{n}$ is open in $Y$ because $K_{n}$ is compact hence closed in $X$ (Theorem 26.3), and it contains $\infty$. If $V$ is a neighbourhood of $\infty$ in $Y$, then $Y\setminus V$ is a compact subset of $X$, hence lies in some $K_{N}$ by step [](#exhaust){.pf-ref}, giving $\infty\in Y\setminus K_{N}\subseteq V$.
:::

:::

::: {.pf-step #first}
If $X$ has a countable basis then $Y$ is metrizable.

::: pf-proof
$Y$ is compact Hausdorff (Theorem 29.1). A base for $Y$ is obtained from a countable base for $X$ together with the countable family of step [](#base-at-infinity){.pf-ref}, so $Y$ is second countable. A compact Hausdorff space with a countable base is metrizable by the Urysohn metrization theorem (Theorem 34.1).
:::

:::

::: {.pf-step #second}
If $Y$ is metrizable then $X$ has a countable basis.

::: pf-proof
A metrizable compact space is second countable, and a subspace of a second-countable space is second countable (Theorem 30.2); $X$ is a subspace of $Y$, so it has a countable basis.
:::

:::

::: {.pf-qed}
Both questions have the answer yes: the first by step [](#first){.pf-ref} and the second by step [](#second){.pf-ref}.
:::

:::

:::
