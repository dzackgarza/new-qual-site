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
Part (a). Suppose first that $x\in\overline D$ for every $D\in\mathcal D$ and let $U$ be a neighbourhood of $x$. Take $D_1,\dots,D_n\in\mathcal D$; by Lemma 37.2(a) the finite intersection $D=D_1\cap\cdots\cap D_n$ belongs to $\mathcal D$, and $x\in\overline D$, so $U$ meets $D$ and hence $U\cap D_1\cap\cdots\cap D_n\ne\varnothing$. Thus $\mathcal D\cup\{U\}$ has the finite intersection property, and by maximality $U\in\mathcal D$.

Conversely, suppose every neighbourhood of $x$ belongs to $\mathcal D$. If $D\in\mathcal D$ and $U$ is a neighbourhood of $x$, then $U,D\in\mathcal D$, so $U\cap D\ne\varnothing$ by the finite intersection property; hence $x\in\overline D$.

The implication from $x\in\overline D$ for all $D$ to "every neighbourhood of $x$ is in $\mathcal D$" is the one that uses maximality; the converse uses only the finite intersection property.

Part (b). Let $D\in\mathcal D$ and $A\supset D$. Since $D$ has the finite intersection property, $D$ meets every element of $\mathcal D$, and then so does $A\supset D$; by Lemma 37.2(b), $A\in\mathcal D$.

Part (c). As printed, with the $T_1$ axiom, the assertion is false. Let $X$ be an infinite set with the finite complement topology; it is $T_1$. The collection $\mathcal A$ of all nonempty open sets of $X$ has the finite intersection property, since the intersection of finitely many cofinite sets is cofinite and $X$ is infinite, so by Lemma 37.1 there is a collection $\mathcal D\supset\mathcal A$ maximal with respect to the finite intersection property. Every $D\in\mathcal D$ meets every nonempty open set, because each such set lies in $\mathcal D$; hence $\overline D=X$ for every $D\in\mathcal D$ and
$$
\bigcap_{D\in\mathcal D}\overline D=X,
$$
which has more than one point. What the argument of part (c) needs is the Hausdorff axiom, and with it the conclusion holds: if $x\ne y$ both lie in $\bigcap_{D\in\mathcal D}\overline D$, choose disjoint neighbourhoods $U$ of $x$ and $V$ of $y$; by part (a) both belong to $\mathcal D$, contradicting the finite intersection property since $U\cap V=\varnothing$. So the printed $T_1$ hypothesis must be read as Hausdorff, and the first edition of the book printed the Hausdorff hypothesis.
:::
