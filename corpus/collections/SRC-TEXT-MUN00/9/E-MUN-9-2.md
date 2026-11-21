---
schema: qual/card@1
id: E-MUN-9-2
kind: problem
title: Choice functions for countable collections
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 2, printed p. 61; the four collections (a)-(d) are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.2, printed pp. 101-102 (tmp/sources/munkres-solutions-whitman.pdf). His lemma gives a choice function for the nonempty subsets of any countable set by pulling back the least element of the image, which yields (a), (b) and (c); for (d) he argues that a choice function on the nonempty subsets of X^omega would well-order [0,1], which nobody has produced, and concludes that no explicit one is at hand. The card's (b) writes the listing 0,1,-1,2,-2,... rather than quoting countability of Z.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2, one step per part, with the definition of
    a choice function read from the book's Lemma 9.2 at tmp/sources/munkres-2000-topology.md
    (printed p. 59) and the implication used in (d) cited to the Chapter 1 Supplementary
    Exercises, Exercise 7 (printed pp. 73-74). The card's answers are unchanged, including
    (d)'s reading that a choice function for all nonempty subsets of X^omega amounts to a
    well-ordering of X^omega. The printed pages of the retained solution were not re-read in
    this pass; its citation is the earlier event's, and the section's exercise page was not
    re-read either.
---

::: {.exercise}

Find if possible a choice function for each of the following collections, without using the choice axiom:

(a) The collection $\mathcal{A}$ of nonempty subsets of $\ZZ_{+}$ .

(b) The collection $\mathcal B$ of nonempty subsets of $\ZZ$.

(c) The collection $\mathcal C$ of nonempty subsets of $\QQ$.

(d) The collection $\mathcal{D}$ of nonempty subsets of $X^{\omega}$, where $X = \{0,1\}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.2, printed pp. 101--102** (`tmp/sources/munkres-solutions-whitman.pdf`); the device of his lemma, which pulls back the least element of the image in $\ZZ_{+}$, is the one used in (a)--(c), and his reading of (d) is the one stated.

A choice function for a collection $\mathcal{B}$ of nonempty sets is a function $c$ on $\mathcal{B}$ with $c(B)\in B$ for every $B\in\mathcal{B}$ (Lemma 9.2, printed p. 59).

::: pf

::: {.pf-step #zplus}
The collection $\mathcal{A}$ of nonempty subsets of $\ZZ_{+}$ has a choice function, namely $A\mapsto\min A$.

::: pf-proof
$\ZZ_{+}$ is well ordered, so every nonempty $A\subseteq\ZZ_{+}$ has a least element, and $\min A\in A$; the assignment $A\mapsto\min A$ is therefore a function on $\mathcal{A}$ taking each $A$ to one of its elements. No choice principle enters: the least element is determined by the well-ordering of $\ZZ_{+}$, which Munkres derives from the principle of induction in §4.
:::

:::

::: {.pf-step #zintegers}
The collection $\mathcal{B}$ of nonempty subsets of $\ZZ$ has a choice function.

::: pf-proof
List the integers as $0,1,-1,2,-2,\dots$, that is, put $e(1)=0$, $e(2k)=k$ and $e(2k+1)=-k$ for $k\ge1$; the map $e:\ZZ_{+}\to\ZZ$ is onto, because $0=e(1)$, $k=e(2k)$ for $k>0$ and $-k=e(2k+1)$. For nonempty $B\subseteq\ZZ$ the set $\{n\in\ZZ_{+}\mid e(n)\in B\}$ is nonempty, so it has a least element $n_{B}$, and $B\mapsto e(n_{B})$ is a function on $\mathcal{B}$ whose value at $B$ lies in $B$. So it is a choice function, built from the explicit listing and the well-ordering of $\ZZ_{+}$ alone.
:::

:::

::: {.pf-step #rationals}
The collection $\mathcal{C}$ of nonempty subsets of $\QQ$ has a choice function.

::: pf-proof
Enumerate $\QQ$ as in [[E-MUN-7-1]] and write the enumeration as $q_{1},q_{2},\dots$. For nonempty $C\subseteq\QQ$ the set $\{n\in\ZZ_{+}\mid q_{n}\in C\}$ is nonempty, so it has a least element $n_{C}$, and $C\mapsto q_{n_{C}}$ is a function on $\mathcal{C}$ whose value at $C$ lies in $C$. As in steps [](#zplus){.pf-ref} and [](#zintegers){.pf-ref}, the only inputs are the explicit enumeration and the well-ordering of $\ZZ_{+}$.
:::

:::

::: {.pf-step #cantor}
For $\mathcal{D}$, the collection of nonempty subsets of $X^{\omega}$ with $X=\{0,1\}$, the device of the preceding steps is unavailable, so no choice function is exhibited without a choice principle.

::: pf-proof
Steps [](#zplus){.pf-ref}, [](#zintegers){.pf-ref} and [](#rationals){.pf-ref} each took the least element of a set inside an explicit well-ordering or enumeration of the ambient set. The coordinatewise order on $X^{\omega}$ is not a well-ordering — the sequences $1000\cdots$ and $0100\cdots$ are incomparable — so it supplies no least element to take, and no enumeration of $X^{\omega}$ is at hand. A choice function for all nonempty subsets of a set is exactly the hypothesis from which the well-ordering theorem is derived: the supplementary exercises of Chapter 1 establish the equivalence of the choice axiom and the well-ordering theorem (printed pp. 73--74), the proof fixing a choice function $c$ for the nonempty subsets of a set $X$ and well-ordering $X$ by transfinite recursion over towers. So a choice function for all nonempty subsets of $X^{\omega}$ would well-order $X^{\omega}$, and conversely a well-ordering of $X^{\omega}$ yields a choice function by least elements, exactly as in step [](#zplus){.pf-ref}. The existence of either is what the axiom of choice supplies and what cannot be concluded in ZF; hence (d) is not answered in the manner of (a)--(c), which is the answer this card records.
:::

:::

:::
:::
