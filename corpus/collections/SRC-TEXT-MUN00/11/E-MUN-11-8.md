---
schema: qual/card@1
id: E-MUN-11-8
kind: problem
title: Every vector space has a basis, by Zorn's lemma
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
    Read against Munkres, Topology (2000), §11 Exercise 8, printed p. 71; the three parts
    and the definitions of span, independence and basis are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.8,
    printed pp. 126-127 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his
    argument that a relation with a nonzero coefficient at v can be solved for v; (b)
    applies Zorn's lemma to the independent sets, whose unions are independent because
    a linear relation involves finitely many vectors; (c) is maximality plus (a).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 11.8, printed
    pp. 126-127. Checked against Munkres §11 Exercise 8, whose number is read from the collection
    index. Each step re-read: (a) splits on whether the coefficient of v vanishes, and the
    nonzero case writes v as a combination of A; (b) the union of a chain of independent sets is
    independent because a finite relation touches finitely many members, which lie in the largest
    since the family is nested; (c) a maximal independent set spans, since otherwise adjoining a
    vector stays independent. Not claimed: any statement about the cardinality of a basis, which is
    a different exercise.
---

::: {.exercise}

A typical use of Zorn's lemma in algebra is the proof that every vector space has a basis. Recall that if $A$ is a subset of the vector space $V$, we say a vector belongs to the span of $A$ if it equals a finite linear combination of elements of $A$. The set $A$ is independent if the only finite linear combination of elements of $A$ that equals the zero vector is the trivial one having all coefficients zero. If $A$ is independent and if every vector in $V$ belongs to the span of $A$, then $A$ is a basis for $V$.

(a) If $A$ is independent and $v \in V$ does not belong to the span of $A$, show $A \cup \{v\}$ is independent.

(b) Show the collection of all independent sets in $V$ has a maximal element.

(c) Show that $V$ has a basis.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.8, printed pp. 126--127 (`tmp/sources/munkres-solutions-whitman.pdf`); the three parts are his. It is checked against Munkres, Topology (2000), §11 Exercise 8.

::: pf

::: {.pf-step #parta}
If $A$ is independent and $v\notin\operatorname{span}(A)$ then $A\cup\{v\}$ is independent.

:::: pf-proof

::: {.pf-step #relation}
Let $\sum_{a\in F}\lambda_{a}a+\lambda v=0$ be a finite linear relation with $F\subseteq A$ finite.

::: pf-proof
This is the general form of a finite linear combination of elements of $A\cup\{v\}$: at most one coefficient is attached to $v$, and the rest to finitely many elements of $A$.
:::

:::

::: {.pf-step #lambda0}
If $\lambda=0$ then every $\lambda_{a}=0$.

::: pf-proof
The relation becomes $\sum_{a\in F}\lambda_{a}a=0$, a finite linear relation among elements of the independent set $A$.
:::

:::

::: {.pf-step #lambdanonzero}
If $\lambda\ne0$ then $v\in\operatorname{span}(A)$, contrary to hypothesis.

::: pf-proof
Solving for $v$ gives $v=-\sum_{a\in F}(\lambda_{a}/\lambda)a$, a finite linear combination of elements of $A$.
:::

:::

::: {.pf-step}
$A\cup\{v\}$ is independent.

::: pf-proof
The only finite linear relation is the trivial one, by steps [](#lambda0){.pf-ref} and [](#lambdanonzero){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #partb}
The collection of independent sets has a maximal element.

::: pf-proof
Order the collection $\mathcal I$ of independent subsets of $V$ by inclusion, and let $\mathcal B\subseteq\mathcal I$ be a chain. Its union $U=\bigcup_{B\in\mathcal B}B$ is independent: a finite linear relation involves finitely many vectors, each lying in some member of $\mathcal B$, and finitely many members of a chain lie in the largest of them, which is independent, so all coefficients vanish. Thus $U\in\mathcal I$ and $U$ contains every $B\in\mathcal B$, so $U$ is an upper bound; Zorn's lemma applies and gives a maximal independent set $A$.
:::

:::

::: {.pf-step #partc}
$V$ has a basis.

::: pf-proof
Let $A$ be maximal independent, from step [](#partb){.pf-ref}. If some $v\in V$ lay outside $\operatorname{span}(A)$, then $A\cup\{v\}$ would be independent by step [](#parta){.pf-ref} and would strictly contain $A$, contradicting maximality. Hence every vector lies in the span of $A$, and an independent spanning set is a basis.
:::

:::

::: {.pf-step}
Every vector space has a basis.

::: pf-proof
Steps [](#parta){.pf-ref}, [](#partb){.pf-ref} and [](#partc){.pf-ref} are parts (a), (b) and (c):
$$
\boxed{\text{every vector space }V\text{ has a basis, by Zorn's lemma applied to independent sets ordered by inclusion}.}
$$
The hypothesis of Zorn's lemma is verified in step [](#partb){.pf-ref} for an arbitrary chain, and maximality is used only through step [](#parta){.pf-ref}.
:::

:::

:::
:::
