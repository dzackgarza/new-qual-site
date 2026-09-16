---
schema: qual/card@1
id: T-CRVMINMOD
kind: theorem
title: Every curve has a unique smooth projective model
classification:
  areas:
  - algebraic-geometry
  topics:
  - Curves
  - Birational Geometry
  - Function Fields
relations:
- kind: related-to
  target: T-SRFCAST
review: draft
prompts:
- What is the minimal model theorem for curves?
---

::: {.theorem title="Minimal model theorem for curves"}
Let $k$ be an algebraically closed field.
The following categories are equivalent:

1. smooth projective curves over $k$ with dominant morphisms;
2. quasiprojective curves over $k$ with dominant rational maps;
3. finitely generated field extensions $K/k$ of transcendence degree $1$, with $k$-algebra homomorphisms, with arrows reversed.

In particular every curve is birational to a smooth projective curve, unique up to isomorphism, and two smooth projective curves are birational exactly when they are isomorphic.
:::

::: {.remark}
The smooth projective model of the function field $K$ is built from its discrete valuation rings: its closed points are the DVRs of $K$ containing $k$, and the normalization of any projective model of $K$ realizes it.
A rational map from a smooth curve to a projective variety extends to a morphism, by the valuative criterion applied at each point, which is why birational smooth projective curves are isomorphic.
In dimension $2$ this uniqueness fails: blowing up a point gives a birational smooth projective surface that is not isomorphic, and minimal models are reached by contracting $(-1)$-curves.
:::
