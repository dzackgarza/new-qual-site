---
schema: qual/card@1
id: E-KIH81
kind: problem
title: Maximal collections with the finite intersection property
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 4, "Solution to Problem p235, #1", PDF pp. 1-2
    (tmp/sources/munkres-solutions-zinger-mat530-ps4.pdf, downloaded from
    https://www.math.stonybrook.edu/~azinger/mat530/ps4sol.pdf; the sheet carries no printed page
    numbers, so the PDF page is the locator). Checked against Munkres, Topology (2000), Section 37
    Exercise 1, printed p. 235, with Theorem 17.5 (closure via neighbourhoods), Lemma 37.1 (existence of
    a maximal collection) and Lemma 37.2(a) and (b). What was repaired: the card's stored statement read
    "if X is Hausdorff", replacing the book's printed "$T_1$ axiom" -- a change of the printed statement,
    not a proof of it -- and the book's printed statement is false: on an infinite set with the finite
    complement topology, which is $T_1$, the collection of all nonempty open sets has the finite
    intersection property, any maximal $\mathcal D$ containing it consists of dense sets, and
    $\bigcap_{D\in\mathcal D}\overline D=X$. The card now states the exercise as printed, records that
    counterexample (it is the sheet's, which also records that the first edition printed the Hausdorff
    hypothesis), and proves the Hausdorff form of (c), which is what the argument needs. Parts (a) and (b)
    are the sheet's, as is the answer to the printed question that the first implication is the one using
    maximality. Not checked here: the counterexample is checked against the definition and not against
    Munkres's errata list, which is not among the retained files.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the three parts as the top-level steps and (c) as
    the QED step. Re-checked each: (a) forward uses Lemma 37.2(a) to put the finite intersection in
    $\mathcal{D}$, then maximality on $\mathcal{D}\cup\{U\}$, and backward uses only the finite
    intersection property; (b) is Lemma 37.2(b) with $A$ meeting every member; and (c) holds
    the counterexample on an infinite cofinite space, where the collection of all nonempty open
    sets has the finite intersection property and any maximal $\mathcal{D}$ above it consists of
    dense sets, against the Hausdorff argument in which two disjoint neighbourhoods both lie in
    $\mathcal{D}$. The statement is the printed §37 Exercise 1 on p. 235, including its $T_1$
    hypothesis, and the false form is recorded rather than silently repaired. Not claimed: a check
    of the book's errata for the $T_1$/$T_2$ discrepancy, and no published argument beyond the
    retained sheet.
---

::: {.exercise}

Let $X$ be a space.
Let $\mathcal{D}$ be a collection of subsets of $X$ that is maximal with respect to the finite intersection property.

(a) Show that $x \in \overline{D}$ for every $D \in \mathcal{D}$ if and only if every neighborhood of $x$ belongs to $\mathcal{D}$.
Which implication uses maximality of $\mathcal{D}$?

(b) Let $D \in \mathcal{D}$.
Show that if $A \supset D$, then $A \in \mathcal{D}$.

(c) Show that if $X$ satisfies the $T_{1}$ axiom, there is at most one point belonging to $\bigcap_{D \in \mathcal{D}} \overline{D}$.
:::

::: {.solution}
Parts (a) and (b), the counterexample in (c) and the Hausdorff form of (c) are the argument of the retained published solution, Aleksey Zinger, *MAT 530: Topology & Geometry, I*, Fall 2005, Problem Set 4, "Solution to Problem p235, \#1", PDF pp. 1--2 (`tmp/sources/munkres-solutions-zinger-mat530-ps4.pdf`); the sheet carries no printed page numbers, so the PDF page is the locator. The printed hypothesis of (c) is $T_1$, and as printed the assertion is false; step [](#part-c){.pf-ref} records the counterexample and proves the Hausdorff form.

::: pf

::: {.pf-step #part-a}
(a) For $x\in X$: $x\in\overline{D}$ for every $D\in\mathcal{D}$ if and only if every neighbourhood of $x$ belongs to $\mathcal{D}$; the implication from the closures to the neighbourhoods is the one that uses maximality.

:::: pf-proof

::: {.pf-step #closures-to-neighbourhoods}
If $x\in\overline{D}$ for all $D\in\mathcal{D}$, then every neighbourhood $U$ of $x$ lies in $\mathcal{D}$.

::: pf-proof
Let $U$ be a neighbourhood of $x$ and $D_1,\ldots,D_n\in\mathcal{D}$. By Lemma 37.2(a) the finite intersection $D=D_1\cap\cdots\cap D_n$ lies in $\mathcal{D}$, so $x\in\overline{D}$; since $U$ is a neighbourhood of $x$ it meets $D$, that is $U\cap D_1\cap\cdots\cap D_n\ne\varnothing$. Hence $\mathcal{D}\cup\{U\}$ has the finite intersection property, and by maximality of $\mathcal{D}$ one has $U\in\mathcal{D}$. This is the only place where maximality is used.
:::

:::

::: {.pf-step #neighbourhoods-to-closures}
If every neighbourhood of $x$ lies in $\mathcal{D}$, then $x\in\overline{D}$ for all $D\in\mathcal{D}$.

::: pf-proof
Let $D\in\mathcal{D}$ and let $U$ be a neighbourhood of $x$. Then $U\in\mathcal{D}$ by hypothesis, so $U\cap D\ne\varnothing$ because $\mathcal{D}$ has the finite intersection property. Every neighbourhood of $x$ meets $D$, so $x\in\overline{D}$.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) If $D\in\mathcal{D}$ and $A\supset D$, then $A\in\mathcal{D}$.

::: pf-proof
Let $E\in\mathcal{D}$. Since $\mathcal{D}$ has the finite intersection property and $D,E\in\mathcal{D}$, the intersection $D\cap E$ is nonempty; as $D\subseteq A$, also $A\cap E\ne\varnothing$. So $A$ meets every element of $\mathcal{D}$, and Lemma 37.2(b) gives $A\in\mathcal{D}$.
:::

:::

::: {.pf-step #part-c}
(c) As printed, with the $T_1$ axiom, the assertion is false; with the Hausdorff axiom in its place there is at most one point in $\bigcap_{D\in\mathcal{D}}\overline{D}$.

:::: pf-proof

::: {.pf-step #t1-counterexample}
There is a $T_1$ space and a maximal $\mathcal{D}$ on it with $\bigcap_{D\in\mathcal{D}}\overline{D}$ having more than one point.

::: pf-proof
Let $X$ be an infinite set with the finite complement topology, in which the nonempty open sets are the cofinite ones. It is $T_1$, since its one-point sets are closed. Let $\mathcal{A}$ be the collection of all nonempty open sets of $X$; finitely many cofinite sets have cofinite intersection, which is nonempty because $X$ is infinite, so $\mathcal{A}$ has the finite intersection property, and by Lemma 37.1 there is $\mathcal{D}\supseteq\mathcal{A}$ maximal with respect to that property. Every nonempty open set of $X$ lies in $\mathcal{A}\subseteq\mathcal{D}$, and every $D\in\mathcal{D}$ meets every element of $\mathcal{D}$, hence meets every nonempty open set; so $\overline{D}=X$ for every $D\in\mathcal{D}$ and $\bigcap_{D\in\mathcal{D}}\overline{D}=X$, which has more than one point.
:::

:::

::: {.pf-step #hausdorff-form}
If $X$ is Hausdorff, then $\bigcap_{D\in\mathcal{D}}\overline{D}$ has at most one point.

::: pf-proof
Suppose $x\ne y$ both lie in the intersection. Hausdorffness gives disjoint neighbourhoods $U$ of $x$ and $V$ of $y$, and by step [](#neighbourhoods-to-closures){.pf-ref} both $U$ and $V$ lie in $\mathcal{D}$; but $U\cap V=\varnothing$, contradicting the finite intersection property.
:::

:::

::: {.pf-step}
(c) The $T_1$ hypothesis of the printed statement must be read as Hausdorff, and then the conclusion of (c) holds.

::: pf-proof
The printed statement is refuted by step [](#t1-counterexample){.pf-ref}, while step [](#hausdorff-form){.pf-ref} proves the claim under the Hausdorff axiom, which is what the argument needs and which the first edition of the book printed. Parts (a) and (b) are steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref}, so the exercise printed on p. 235 is answered as printed, with the counterexample that shows its part (c) false as stated.
:::

:::

:::

:::

:::
:::
