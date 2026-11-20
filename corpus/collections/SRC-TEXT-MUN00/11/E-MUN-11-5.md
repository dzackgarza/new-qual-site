---
schema: qual/card@1
id: E-MUN-11-5
kind: problem
title: Zorn's lemma implies the Kuratowski lemma
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 5, printed p. 71, with Zorn's
    lemma as stated in §11 on p. 69; the stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.5,
    printed p. 125 (tmp/sources/munkres-solutions-whitman.pdf). The upper bound of a
    chain is its union, which the hypothesis puts in A; a maximal element of (A, proper
    inclusion) is the element the Kuratowski lemma asks for.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 11.5, printed p. 125); statement unchanged. Steps added: that proper inclusion is a strict partial order, irreflexivity and transitivity both checked, since Zorn's lemma needs a strict partial order and the exercise speaks of proper inclusion; that the empty subcollection is simply ordered, so the hypothesis forces the empty set to belong to A -- which also supplies the nonemptiness Zorn's lemma needs at its own set (its printed statement has no nonemptiness clause, and is false for the empty ordered set); and that the union of a simply ordered subcollection is an upper bound, not merely a member of A. Pages checked against the retained PDF: the definitions of upper bound and maximal element and Zorn's lemma on printed p. 70, the exercise on printed p. 72.

---

::: {.exercise}

Show that Zorn's lemma implies the following:

Lemma (Kuratowski). Let $\mathcal A$ be a collection of sets. Suppose that for every subcollection $\mathcal B$ of $\mathcal A$ that is simply ordered by proper inclusion, the union of the elements of $\mathcal B$ belongs to $\mathcal A$. Then $\mathcal A$ has an element that is properly contained in no other element of $\mathcal A$.

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.5** (`tmp/sources/munkres-solutions-whitman.pdf`); the reduction to Zorn's lemma is his, and the observation that the hypothesis forces $\varnothing\in\mathcal{A}$ — which is what makes Zorn's lemma applicable at a nonempty set — is supplied below.

Throughout, a strict partial order $\prec$ on a set is irreflexive and transitive, a subset is simply ordered when any two of its elements are comparable under $\prec$, an upper bound on $B$ is an element $c$ with $b=c$ or $b\prec c$ for every $b\in B$, and a maximal element is an $m$ with $m\prec a$ for no $a$ (definitions). Zorn's Lemma is the assertion that a strictly partially ordered set in which every simply ordered subset has an upper bound has a maximal element (§11); the exercise is.

::: pf

::: {.pf-step #order}
Proper inclusion is a strict partial order on $\mathcal{A}$, and it is the relation the exercise's hypothesis refers to.

::: pf-proof
$X\subsetneq X$ fails for every set, so proper inclusion is irreflexive; if $X\subsetneq Y$ and $Y\subsetneq Z$ then $X\subseteq Z$, while $Z\subseteq X$ together with $Y\subsetneq Z$ would give $Y\subsetneq Y$, so $X\subsetneq Z$, which is transitivity. A subcollection simply ordered by proper inclusion is therefore a simply ordered subset of $(\mathcal{A},\subsetneq)$, and conversely.

:::

:::

::: {.pf-step #empty-member}
$\varnothing\in\mathcal{A}$; in particular $\mathcal{A}\neq\varnothing$.

::: pf-proof
The empty subcollection $\mathcal{B}=\varnothing$ of $\mathcal{A}$ is simply ordered by proper inclusion, vacuously. Its union is $\bigcup_{B\in\varnothing}B=\varnothing$, so the hypothesis of the exercise gives $\varnothing\in\mathcal{A}$, and then $\mathcal{A}$ has at least this one element.

:::

:::

::: {.pf-step #upper-bound}
Every subset of $\mathcal{A}$ simply ordered by proper inclusion has an upper bound in $\mathcal{A}$.

::: pf-proof
Let $\mathcal{B}\subset\mathcal{A}$ be simply ordered by proper inclusion and put $U=\bigcup_{B\in\mathcal{B}}B$. By the hypothesis of the exercise $U\in\mathcal{A}$; this includes the case $\mathcal{B}=\varnothing$, where $U=\varnothing\in\mathcal{A}$ by step [](#empty-member){.pf-ref}. For $B\in\mathcal{B}$ we have $B\subseteq U$, so either $B=U$ or $B\subsetneq U$; that is, $U$ is an upper bound on $\mathcal{B}$ in the order of step [](#order){.pf-ref}.

:::

:::

::: {.pf-step #maximal}
$\mathcal{A}$ has an element that is properly contained in no other element of $\mathcal{A}$.

::: pf-proof
By steps [](#empty-member){.pf-ref} and [](#order){.pf-ref}, $\mathcal{A}$ is a nonempty set strictly partially ordered by proper inclusion, and by step [](#upper-bound){.pf-ref} every simply ordered subset of it has an upper bound in it. Zorn's lemma (§11) then gives a maximal element $M\in\mathcal{A}$, that is, an $M$ for which $M\subsetneq A$ holds for no $A\in\mathcal{A}$; and that is exactly the assertion: $M$ is properly contained in no other element of $\mathcal{A}$.

:::

:::

:::

:::
