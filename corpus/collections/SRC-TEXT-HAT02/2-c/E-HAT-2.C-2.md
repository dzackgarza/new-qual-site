---
schema: qual/card@1
id: E-HAT-2.C-2
kind: exercise
title: 'Lefschetz fixed point theorem: map $S^n \to S^n$ has fixed point unless degree equals antipodal degree'
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Degree Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Use the Lefschetz fixed point theorem to show that a map $S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $x \mapsto -x$.

::: solution
**Goal:** Use Lefschetz to force a fixed point when degree is not that of the antipodal map.

<1> Let $f\colon S^n\to S^n$ have degree $d$.
    *Proof:*
    <2>1. For homology, $H_0(S^n)\cong\ZZ$ and $H_n(S^n)\cong\ZZ$, and other homology groups vanish.
    <2>2. The induced maps are
        $$f_\ast|_{H_0}=\id,\qquad f_\ast|_{H_n}=\times d.$$
    <2>3. The Lefschetz number is
        $$L(f)=\operatorname{tr}(f_\ast|_{H_0})+(-1)^n\operatorname{tr}(f_\ast|_{H_n})
        =1+(-1)^n d.$$

<1> Apply the theorem.
    *Proof:*
    <2>1. If $d\neq (-1)^{n+1}$, then $L(f)\neq0$.
    <2>2. Lefschetz fixed point theorem gives a fixed point for $f$.
    <2>3. The antipodal map has degree $(-1)^{n+1}$ and has no fixed point.

<1> Therefore: a fixed-point-free map can occur only when $\deg f = \deg(\text{antipodal})=(-1)^{n+1}$.

Authored by **Codex 5.3 Spark Extra High**.
:::
