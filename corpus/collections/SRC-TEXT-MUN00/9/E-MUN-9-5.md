---
schema: qual/card@1
id: E-MUN-9-5
kind: problem
title: Right inverses from surjections via the axiom of choice
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 5; the stored statement matches.
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
    Read against Munkres, Topology (2000), §9 Exercise 5, printed p. 61; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.5, printed pp. 104-105 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his: choose from the family of nonempty fibres. Part (b) is his too, and so is the answer that no choice is needed there, since only one element of A is chosen and the rest of the left inverse is forced by injectivity. No defect found.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 9.5, printed pp. 104-105); statement unchanged. In (a) the nonemptiness of the fibres is a separate step, because that is precisely the hypothesis the choice axiom needs. In (b) the well-definedness of g -- single-valued, exhaustive and exclusive on the two cases, with the uniqueness supplied by injectivity -- is a step of its own, and the answer to the book's question is its own step. Pages added and checked against the retained PDF: left and right inverses on printed p. 21, the choice axiom on printed p. 60, the exercise on printed p. 63.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 9.5, printed pp. 104-105); statement unchanged. In (a) the disjointness and nonemptiness of the fibres is its own step, since Munkres states the choice axiom for disjoint families and both clauses are needed to apply it; the passage from the chosen set C to the function h is then written out. In (b) the well-definedness of g is its own step, and the answer to the book's question is its own step. Pages checked against the retained PDF: left and right inverses on printed p. 21, the choice axiom on printed p. 59, the exercise on printed p. 62.

---

::: {.exercise}

(a) Use the choice axiom to show that if $f: A \to B$ is surjective, then $f$ has a right inverse $h: B \to A$ .

(b) Show that if $f: A \to B$ is injective and $A$ is not empty, then $f$ has a left inverse.
Is the axiom of choice needed?

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.5** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice from the fibres in (a) and the forced left inverse in (b) are his.

Throughout, $f^{-1}(\{b\})=\{a\in A:f(a)=b\}$ is the fibre of $f$ over $b$, a right inverse of $f$ is a map $h:B\to A$ with $f\circ h=i_B$, and a left inverse is a map $g:B\to A$ with $g\circ f=i_A$ (§2 Exercise 5). Munkres states the choice axiom for a collection of **disjoint** nonempty sets: there is a set meeting each member in exactly one point (§9). The exercise is on printed p. 62.

::: pf

::: {.pf-step #right-inverse}
(a) A surjection $f:A\to B$ has a right inverse, by the choice axiom.

::: pf-proof

::: {.pf-step #fibres}
The family of fibres is a collection of pairwise disjoint nonempty sets.

::: pf-proof
If $a\in f^{-1}(\{b\})\cap f^{-1}(\{b'\})$ then $b=f(a)=b'$, so distinct fibres are disjoint. Each is nonempty: as $f$ is surjective, for each $b\in B$ there is $a\in A$ with $f(a)=b$, that is $a\in f^{-1}(\{b\})$.

:::

:::

::: {.pf-step #choice}
There is a set $C$ meeting each fibre in exactly one point, and the rule $h(b)=$ that point is a map $B\to A$ with $f(h(b))=b$.

::: pf-proof
By step [](#fibres){.pf-ref} the choice axiom applies to the collection $\mathcal{A}=\{f^{-1}(\{b\}):b\in B\}$ of disjoint nonempty sets and gives a set $C$ with exactly one element in each member. The members are indexed by $b$, distinct $b$ giving distinct fibres, so $C\cap f^{-1}(\{b\})=\{h(b)\}$ defines a function $h:B\to A$; and $h(b)\in f^{-1}(\{b\})$ says exactly $f(h(b))=b$, that is $f\circ h=i_B$.

:::

:::

:::

:::

::: {.pf-step #left-inverse}
(b) An injection $f:A\to B$ with $A\neq\varnothing$ has a left inverse.

::: pf-proof

::: {.pf-step #definition}
Fixing $a_0\in A$, the rule that sends $b$ to the unique $a$ with $f(a)=b$ when $b\in f(A)$, and to $a_0$ otherwise, is a well-defined function $g:B\to A$.

::: pf-proof
$A\neq\varnothing$, so $a_0$ can be chosen; this is the only choice made. If $b\in f(A)$ there is $a$ with $f(a)=b$, and it is unique because $f$ is injective: $f(a)=f(a')=b$ gives $a=a'$. The cases $b\in f(A)$ and $b\notin f(A)$ are exhaustive and mutually exclusive, so $g$ is defined on all of $B$ and single-valued.

:::

:::

::: {.pf-step #composite}
$g\circ f=i_A$.

::: pf-proof
For $a\in A$ the element $f(a)$ lies in $f(A)$, so by step [](#definition){.pf-ref} $g(f(a))$ is the unique $a'$ with $f(a')=f(a)$, namely $a$ itself.

:::

:::

:::

:::

::: {.pf-step #no-choice}
The axiom of choice is not needed in (b).

::: pf-proof
In (b) one element $a_0$ is chosen from the single nonempty set $A$; every value of $g$ on $f(A)$ is then forced by injectivity, and the value off $f(A)$ is the fixed $a_0$. So no selection from an arbitrary family of nonempty sets is made, which is what the choice axiom supplies. In (a), by contrast, one point is selected from each of the possibly infinitely many fibres, and that is exactly a choice from a disjoint family.

:::

:::

:::

:::
