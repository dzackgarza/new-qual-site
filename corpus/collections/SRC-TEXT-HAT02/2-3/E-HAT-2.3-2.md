---
schema: qual/card@1
id: E-HAT-2.3-2
kind: problem
title: Candidate homology theory $\Pi_i \tilde{H}_i(X)/\oplus_i \tilde{H}_i(X)$ satisfies all axioms except wedge axiom
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.3, Exercise 2; the candidate and the example of the infinite wedge match the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the four axioms: homotopy invariance is immediate; exactness follows from exactness of
    products and of direct sums together with the snake lemma on $0\to\bigoplus_i\tilde
    H_i\to\prod_i\tilde H_i\to Q\to0$; the dimension step is now stated for a point, and $S^0$
    gives the same conclusion because only $\tilde H_0$ is nonzero there, where product and sum
    coincide; and the wedge axiom fails on $\bigvee_{j\ge1}S^j$, whose reduced $H_i$ is $\ZZ$ for
    every $i\ge1$ while each summand $S^j$ has $Q=0$.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    The dimension step's mechanism is now certified in the form the card uses, with the finiteness
    hypothesis explicit: proofs/cards/FamilyQuotient.lean proves that when the family $(f_i)$ is
    carried by a finite set of indices, the canonical map $\bigoplus_i f_i\to\prod_i f_i$ is
    surjective (`directSumToPi_surjective_of_finite_support`), so the quotient
    $\prod_i f_i\big/\bigoplus_i f_i$ is trivial (`quotient_subsingleton_of_finite_support`), with
    the point case and the $S^0$ case (exactly one nonzero index) as corollaries. What is certified
    is the vanishing of the quotient under finite support, not an isomorphism between the sum and
    the product, and nothing is asserted for families with infinite support, where the map is not
    surjective in general beneath the card's wedge-axiom step. The identification of the $f_i$ with
    reduced homology groups is not formalized.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 2 of §2.3 as printed on p. 165. The candidate Q(X) = prod/oplus is
    independent of n, vanishes for finite-dimensional X because the family has finite support,
    and fails the wedge axiom on the wedge of one sphere in each positive degree, where every
    H_i is Z; homotopy invariance and exactness hold, the latter by the snake lemma applied to
    the quotient sequence for the three terms, products and direct sums of exact sequences being
    exact. The exactness axiom is now cited to p. 160. The S^0 step was reworded: what the
    dimension step needs is the finite-support surjectivity of oplus -> prod, which is what
    proofs/cards/FamilyQuotient.lean certifies (quotient_subsingleton_of_finite_support); the
    earlier sentence invoking an isomorphism of sum and product blurred that. What is not
    covered: the identification of the f_i with reduced homology groups is not formalized, as the
    README for that certificate says.
---

::: {.problem}
Define a candidate for a reduced homology theory on CW complexes by $\tilde{h}_n(X) = \Pi_i \tilde{H}_i(X) / \oplus_i \tilde{H}_i(X)$.
Thus $\tilde{h}_n(X)$ is independent of $n$ and is zero if $X$ is finite-dimensional, but is not identically zero, for example for $X = \vee_i S^i$.
Show that the axioms for a homology theory are satisfied except that the wedge axiom fails.
:::

::: {.solution}
Put
$$
Q(X)=\prod_{i\in\ZZ}\widetilde H_i(X)\big/\bigoplus_{i\in\ZZ}\widetilde H_i(X),
\qquad \widetilde h_n(X)=Q(X).
$$

::: pf

::: pf-step

Homotopy invariance holds.

::: pf-proof

A homotopy equivalence induces isomorphisms on every reduced homology group, hence on their product, their direct sum, and therefore on the quotient $Q(X)$.

:::

:::

::: pf-step

Exactness holds, with all connecting maps induced coordinatewise from ordinary homology.

::: pf-proof

For a cofibration sequence $A\to X\to X/A$, ordinary reduced homology gives a long exact sequence, which is axiom (2) of p. 160. Reindexing turns the connecting map into a degree-preserving map between the products defining $Q$. Products of exact sequences of abelian groups are exact, and so are direct sums. Applying the snake lemma to
$$
0\to\bigoplus_i\widetilde H_i(-)\to\prod_i\widetilde H_i(-)\to Q(-)\to0
$$
for the three terms of the cofibration sequence gives exactness for $Q$.

:::

:::

::: pf-step

The dimension axiom holds.

::: pf-proof

A point has every reduced homology group zero, so $Q(\mathrm{pt})=0$ and $\widetilde h_n(\mathrm{pt})=0$ for all $n$. The reduced homology of $S^0$ is zero in every degree except $0$, where it is $\ZZ$. There the family has finite support, so the direct sum already fills the product and the quotient $Q(S^0)$ is trivial; this finite-support implication, that the canonical map $\bigoplus_i f_i\to\prod_i f_i$ is surjective when all but finitely many $f_i$ vanish, is what `proofs/cards/FamilyQuotient.lean` certifies, and it is exactly what the vanishing of the quotient needs. That file does not assert that the sum and the product are isomorphic for a family with infinite support, and there the quotient need not vanish — which is the failure exhibited in the next step.

:::

:::

::: pf-step

The wedge axiom fails.

::: pf-proof

Let
$$
X=\bigvee_{j\ge1}S^j.
$$
Then $\widetilde H_i(X)\cong\ZZ$ for every $i\ge1$, so
$$
Q(X)\cong\prod_{i\ge1}\ZZ\big/\bigoplus_{i\ge1}\ZZ\ne0.
$$
But each individual sphere $S^j$ is finite-dimensional, hence $Q(S^j)=0$. Therefore
$$
\bigoplus_j\widetilde h_n(S^j)=0
$$
while $\widetilde h_n(\bigvee_jS^j)\ne0$.

:::

:::

:::

Thus the candidate satisfies the reduced homology axioms except the infinite wedge axiom.
:::
