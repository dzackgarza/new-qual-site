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
---

::: {.exercise}

A typical use of Zorn's lemma in algebra is the proof that every vector space has a basis. Recall that if $A$ is a subset of the vector space $V$, we say a vector belongs to the span of $A$ if it equals a finite linear combination of elements of $A$. The set $A$ is independent if the only finite linear combination of elements of $A$ that equals the zero vector is the trivial one having all coefficients zero. If $A$ is independent and if every vector in $V$ belongs to the span of $A$, then $A$ is a basis for $V$.

(a) If $A$ is independent and $v \in V$ does not belong to the span of $A$, show $A \cup \{v\}$ is independent.

(b) Show the collection of all independent sets in $V$ has a maximal element.

(c) Show that $V$ has a basis.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.8, printed pp. 126--127** (`tmp/sources/munkres-solutions-whitman.pdf`); the three arguments below are his.

(a) Let $\sum_{a\in F}\lambda_a a+\lambda v=0$ be a finite linear relation, $F\subset A$ finite. If $\lambda=0$ then all $\lambda_a=0$ because $A$ is independent. If $\lambda\ne0$ then
$$
v=-\sum_{a\in F}\frac{\lambda_a}{\lambda}\,a
$$
lies in the span of $A$, contrary to hypothesis. So the trivial relation is the only one and $A\cup\{v\}$ is independent.

(b) Order the collection $\mathcal I$ of independent subsets of $V$ by inclusion and let $\mathcal B\subset\mathcal I$ be simply ordered. Its union $U=\bigcup_{B\in\mathcal B}B$ is independent: a finite linear relation involves finitely many vectors, which lie in finitely many members of $\mathcal B$, hence in the largest of them since these are nested, and that member is independent, so all coefficients vanish. So $U\in\mathcal I$ is an upper bound of $\mathcal B$, and Zorn's lemma gives a maximal independent set $A$.

(c) Let $A$ be maximal independent. If some $v\in V$ were outside the span of $A$, then by (a) $A\cup\{v\}$ would be independent and properly contain $A$, contradicting maximality. Hence every vector of $V$ lies in the span of $A$, and $A$ is a basis.
:::
