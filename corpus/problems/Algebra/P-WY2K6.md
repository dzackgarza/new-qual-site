---
schema: qual/card@1
id: P-WY2K6
kind: problem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (asks
    for the statement and the proof; both delivered, no repair needed), and the
    existing prose solution against a fresh re-derivation: x ~ y iff x^{-1}y in H
    is an equivalence relation — reflexive by e in H, symmetric because subgroups
    are closed under inverses, transitive because they are closed under products;
    the class of g is gH; hence the left cosets partition G; and h |-> gh is a
    bijection H -> gH, injective by left cancellation, so every coset has |H|
    elements; summing over the index gives |G| = [G:H]|H|. Correct. The prose
    stated the three equivalence-relation axioms in one phrase and the bijectivity
    in one phrase; both are now spelled out with their reasons. No source solution
    is retained for this card, so no source comparison was made. What was not
    checked: any printed source.

---

::: {.problem}
State and prove **Lagrange's Theorem** for finite groups: if $G$ is a finite group and $H \le G$ is a subgroup, then $\cardinality{H}$ divides $\cardinality{G}$ and $\cardinality{G} = [G : H] \cdot \cardinality{H}$.
:::

::: {.solution}
Let $G$ be a finite group with identity $e$, let $H\leq G$ be a subgroup, and let $[G:H]$ denote the number of left cosets $gH=\theset{gh:h\in H}$ of $H$ in $G$.

::: pf

::: {.pf-step #equivalence}
The relation $x\sim y\iff x^{-1}y\in H$ is an equivalence relation on $G$.

::: pf-proof
Reflexive: $x^{-1}x=e\in H$ because $H$ contains the identity. Symmetric: if $x^{-1}y\in H$ then $y^{-1}x=(x^{-1}y)^{-1}\in H$, since a subgroup is closed under inverses. Transitive: if $x^{-1}y\in H$ and $y^{-1}z\in H$ then $x^{-1}z=(x^{-1}y)(y^{-1}z)\in H$, since a subgroup is closed under multiplication.
:::

:::

::: {.pf-step #cosets}
The class of $g\in G$ under $\sim$ is $gH$; hence the left cosets of $H$ partition $G$ and $G$ is the disjoint union of its $[G:H]$ left cosets.

::: pf-proof
$x$ is in the class of $g$ iff $g^{-1}x\in H$ iff $x=gh$ for some $h\in H$ iff $x\in gH$. The classes of an equivalence relation partition the set, and they are exactly the left cosets, so the left cosets are pairwise disjoint and cover $G$; their number is $[G:H]$, so choosing one representative $g_i$ from each gives $G=\bigsqcup_{i=1}^{[G:H]}g_iH$.
:::

:::

::: {.pf-step #size}
Every left coset has exactly $\cardinality{H}$ elements.

::: pf-proof
For $g\in G$ the map $\varphi\colon H\to gH$, $\varphi(h)=gh$, is surjective by the definition of $gH$, and injective because $gh_1=gh_2$ implies $h_1=h_2$ after multiplying on the left by $g^{-1}$. A bijection between finite sets makes them have the same number of elements, so $\abs{gH}=\abs{H}$.
:::

:::

::: {.pf-step}
$\cardinality{G}=[G:H]\cardinality{H}$, and in particular $\cardinality{H}$ divides $\cardinality{G}$.

::: pf-proof
By step [](#cosets){.pf-ref} $G$ is the disjoint union of its $[G:H]$ left cosets, so $\abs{G}$ is the sum of their sizes, each of which is $\abs{H}$ by step [](#size){.pf-ref}:
$$\cardinality{G}=\sum_{i=1}^{[G:H]}\abs{g_iH}=[G:H]\,\cardinality{H}.$$
Since $[G:H]$ is an integer, $\cardinality{H}$ divides $\cardinality{G}$, with quotient the index.
:::

:::

:::
:::
