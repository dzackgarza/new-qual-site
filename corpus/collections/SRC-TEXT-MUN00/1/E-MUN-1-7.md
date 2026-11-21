---
schema: qual/card@1
id: E-MUN-1-7
kind: problem
title: Expressing sets using union, intersection, and difference
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 7, printed p. 15; D, E and F are
    stored exactly as the book writes them, including the implication in F rather than a
    set difference.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.7,
    printed pp. 8-9 (tmp/sources/munkres-solutions-whitman.pdf). His answers are
    D = A meet (B union C), E = (A meet B) union C and F = A - (B - C); the chain of
    equivalences for F on the card is his, and so is the remark that D and E are not
    equal in general although they look alike. Added the equivalent form
    (A - B) union (A meet C) of F, which is the same set written without using the
    preceding difference.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps without changing the mathematics: the two
    translations, the implication rewriting, the two forms of F, and the example separating D from
    E are Whitman's (Exercises 1.6-1.7, printed pp. 8-9), as the card already cites. Checked: each
    equivalence elementwise. Not checked: the cited pages, because tmp/sources holds no copy of
    the Whitman manual in this VM, and no copy of Munkres's text is retained either (the
    collection is one of the ad-text-mun00 blocked ones), so the printed exercise and pages were
    not re-read; the statement is the one the card records from the book.
---

::: {.exercise}

Given sets $A, B$, and $C$, express each of the following sets in terms of $A, B$, and $C$, using the symbols $\cup, \cap,$ and $-$.
$$
D = \{x \mid x \in A \text{ and } (x \in B \text{ or } x \in C) \},
$$
$$
E = \{x \mid (x \in A \text{ and } x \in B) \text{ or } x \in C \},
$$
$$
F = \{x \mid x \in A \text{ and } (x \in B \Rightarrow x \in C) \}.
$$
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.7, printed ps 8-9, which the card cites; it is restructured into numbered steps below. The notation is Munkres's: $A-B$ is the set of elements of $A$ that are not in $B$, and the three sets are defined by the displayed conditions.

::: pf

::: {.pf-step #d}

$D=A\cap(B\cup C)$.

::: pf-proof

$x\in D$ holds exactly when $x\in A$ and ($x\in B$ or $x\in C$), which is the defining condition of $A\cap(B\cup C)$.

:::

:::

::: {.pf-step #e}

$E=(A\cap B)\cup C$.

::: pf-proof

$x\in E$ holds exactly when ($x\in A$ and $x\in B$) or $x\in C$, which is the defining condition of the union of $A\cap B$ with $C$.

:::

:::

::: {.pf-step #impl}

$x\in B\Rightarrow x\in C$ is equivalent to $x\notin B$ or $x\in C$.

::: pf-proof

An implication is false only when its antecedent holds and its conclusion fails; so it holds exactly when the antecedent fails or the conclusion holds.

:::

:::

::: {.pf-step #f}

$F=A-(B-C)$.

::: pf-proof

By step [](#impl){.pf-ref}, $x\in F$ holds exactly when $x\in A$ and not ($x\in B$ and $x\notin C$), that is, when $x\in A$ and $x\notin B-C$; that is the defining condition of $A-(B-C)$.

:::

:::

::: {.pf-step #alt}

Equivalently $F=(A-B)\cup(A\cap C)$.

::: pf-proof

For $x\in A$, the condition 'not ($x\in B$ and $x\notin C$)' is '$x\notin B$ or $x\in C$', which describes $(A-B)\cup(A\cap C)$; the two expressions therefore have the same elements.

:::

:::

::: {.pf-step #distinct}

$D$ and $E$ are not equal in general.

::: pf-proof

Take $A=B=\set{1}$ and $C=\set{2}$: then $D=A\cap(B\cup C)=\set{1}$ while $E=(A\cap B)\cup C=\set{1,2}$. The two sets look alike but differ in the placement of the parenthesis, which the published solution warns of and the card records here.

:::

:::

:::

:::
