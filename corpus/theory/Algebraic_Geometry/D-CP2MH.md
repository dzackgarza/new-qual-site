---
schema: qual/card@1
id: D-CP2MH
kind: definition
title: Projective varieties and homogeneous ideals
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Homogeneous Ideals
  - Varieties
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
prompts:
- What is a projective variety?
- Why must the defining polynomials be homogeneous?
- Which homogeneous ideals correspond to which closed subsets of $\PP^n$?
---

::: {.definition title="Projective variety"}
A subset of $\PP^n$ is **closed** if it is $V(T)$ for a set $T$ of homogeneous elements of $S \da k[x_0,\ldots,x_n]$.
A **projective variety** is an irreducible closed subset of $\PP^n$; a **quasi-projective variety** is an open subset of one.
:::

::: {.remark}
Homogeneity is forced, not stylistic: a point of $\PP^n$ is a line through the origin, so $f(p)$ is only well defined up to the scaling $f(\lambda p) = \lambda^{\deg f} f(p)$, and only the condition $f(p) = 0$ survives it.
An inhomogeneous $f$ has no vanishing locus in $\PP^n$ at all.

The correspondence transfers with one defect.
The **irrelevant ideal** $S_+ = (x_0,\ldots,x_n)$ is homogeneous and radical, and $V(S_+) = \emptyset$, so it shares its vanishing locus with $(1)$.
The projective Nullstellensatz reads: for a homogeneous ideal $J$, $V(J) = \emptyset$ exactly when $\sqrt{J} \supseteq S_+$, and otherwise $I(V(J)) = \sqrt{J}$.
:::
