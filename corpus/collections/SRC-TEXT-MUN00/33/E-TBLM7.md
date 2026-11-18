---
schema: qual/card@1
id: E-TBLM7
kind: problem
title: Locally compact Hausdorff spaces are completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.7, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844), and
    "Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 33.7, printed p. 9
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 33 Exercise 7, printed p. 213, Theorem 29.1 (the one-point compactification is compact
    Hausdorff), Theorem 32.3 and Theorem 33.1. Moller's chain is the card's: a locally compact
    Hausdorff space is an open subspace of its compact Hausdorff one-point compactification, a
    subspace of a normal space, a subspace of a completely regular space, and a subspace of a
    completely regular space is completely regular. The card runs the same argument through
    Urysohn's lemma applied to the closed set A union {infinity}. No correction to the mathematics
    was needed.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same argument, with the vague clause replaced: the
    closedness of A u {infinity} in X* is now derived from clause (1) of the description of the topology
    of X* in Step 2 of the proof of Theorem 29.1, rather than from the phrase "open in X*, away from the
    point at infinity". The separating function is also oriented as the book's definition wants it --- 1
    at the point, 0 on the closed set --- where the earlier prose produced 0 and 1 the other way round
    without saying which convention it was following. Nothing else was changed; the statement was
    checked against Munkres, Topology (2000), Section 33 Exercise 7, printed p. 213.
---

::: {.exercise}

Show that every locally compact Hausdorff space is completely regular.
:::

::: {.solution}

The argument is the one of **Jesper Michael Moller, "Solutions to exercises in Munkres", file S33.pdf, Exercise 33.7, page 2 of the file** (`tmp/sources/munkres-solutions-poulsen-S33.pdf`), which runs through the one-point compactification, as does that of **"Doug's World", "Munkres - Topology - Chapter 4 Solutions", Problem 33.7, printed p. 9** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`); the card applies Urysohn's lemma to the pair $\theset{x}$ and $A\cup\theset{\infty}$ directly instead of separating the pair by the normality of a subspace. One phrase of the earlier prose is replaced by the argument: it said $A\cup\theset{\infty}$ is closed in $X^{*}$ "because its complement $X-A$ is open in $X$, hence open in $X^{*}$ away from the point at infinity", which is right in substance and vague in expression, so the card now names the clause of Theorem 29.1 that puts an open set of $X$ into $X^{*}$.

The statement was checked against Munkres, *Topology* (2000), §33 Exercise 7, printed p. 213, with the definition of complete regularity on printed p. 211, the Urysohn lemma (Theorem 33.1) on printed p. 207, Theorem 32.3 on printed p. 202 and Theorem 29.1 on printed p. 183, whose Step 2 describes the topology of $X^{*}$. Throughout, $X$ is a locally compact Hausdorff space, $X^{*}=X\cup\theset{\infty}$ is its one-point compactification, and complete regularity is as defined on printed p. 211: one-point sets are closed and each point can be separated from a closed set not containing it by a continuous map to $[0,1]$ taking the value $1$ at the point and $0$ on the set.

::: pf

::: {.pf-step #exists}

$X^{*}$ exists and is a compact Hausdorff space in which $X$ is a subspace with $X^{*}-X=\theset{\infty}$.

::: pf-proof

$X$ is locally compact Hausdorff, so Theorem 29.1 (printed p. 183) supplies a space $Y$ containing $X$ as a subspace, with $Y-X$ a single point and $Y$ compact Hausdorff; that space is $X^{*}$.

:::

:::

::: {.pf-step #topology}

Every set open in $X$ is open in $X^{*}$, and $X$ itself is open in $X^{*}$.

::: pf-proof

By the construction in Step 2 of the proof of Theorem 29.1 (printed p. 184) the open sets of $X^{*}$ are (1) the sets $U$ that are open in $X$ and (2) the sets $X^{*}-C$ with $C$ a compact subspace of $X$. So an open set of $X$ is open in $X^{*}$ by clause (1), and $X$ is open in $X$ and therefore open in $X^{*}$ by the same clause.

:::

:::

::: {.pf-step #closed}

$A\cup\theset{\infty}$ is closed in $X^{*}$.

::: pf-proof

$A$ is closed in $X$, so $X-A$ is open in $X$, hence open in $X^{*}$ by step [](#topology){.pf-ref}. Its complement in $X^{*}$ is $(X\cup\theset{\infty})-(X-A)=A\cup\theset{\infty}$, so that set is closed in $X^{*}$.

:::

:::

::: {.pf-step #pair}

$\theset{x}$ and $A\cup\theset{\infty}$ are disjoint closed sets of $X^{*}$.

::: pf-proof

$X^{*}$ is Hausdorff by step [](#exists){.pf-ref}, so its one-point sets are closed (Theorem 17.8, printed p. 99). The set $A\cup\theset{\infty}$ is closed by step [](#closed){.pf-ref}. They are disjoint because $x\in X-A$, so $x\notin A$, and $x\neq\infty$.

:::

:::

::: {.pf-step #normal}

$X^{*}$ is normal.

::: pf-proof

A compact Hausdorff space is normal (Theorem 32.3, printed p. 202), and $X^{*}$ is compact Hausdorff by step [](#exists){.pf-ref}.

:::

:::

::: {.pf-step #urysohn}

There is a continuous $F\colon X^{*}\to[0,1]$ with $F=0$ on $A\cup\theset{\infty}$ and $F(x)=1$.

::: pf-proof

By the Urysohn lemma (Theorem 33.1, printed p. 207), in a normal space any two disjoint closed sets can be separated by a continuous map to $[0,1]$ taking the value $0$ on the first and $1$ on the second. Apply it to the disjoint closed sets of step [](#pair){.pf-ref}, with $A\cup\theset{\infty}$ first and $\theset{x}$ second.

:::

:::

::: {.pf-step #restriction}

The restriction $f$ of $F$ to $X$ is continuous and satisfies $f=0$ on $A$ and $f(x)=1$.

::: pf-proof

The restriction of a continuous map to a subspace is continuous (Theorem 18.2(d), printed p. 107). Both $x$ and every point of $A$ lie in $X$, so the values are those computed in step [](#urysohn){.pf-ref}.

:::

:::

::: pf-step

Therefore $X$ is completely regular.

::: pf-proof

Let $x\in X$ and let $A$ be a closed subset of $X$ with $x\notin A$; steps [](#urysohn){.pf-ref} and [](#restriction){.pf-ref} produce a continuous $f\colon X\to[0,1]$ with $f(x)=1$ and $f(A)=\theset{0}$, which is the separating function the definition on printed p. 211 requires. One-point sets in $X$ are closed because $X$ is Hausdorff. So $X$ is completely regular.

:::

:::

:::

:::
