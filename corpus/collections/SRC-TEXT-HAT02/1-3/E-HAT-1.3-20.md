---
schema: qual/card@1
id: E-HAT-1.3-20
kind: exercise
title: "Nonnormal covering spaces of the Klein bottle"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Construct nonnormal covering spaces of the Klein bottle by a Klein bottle and by a torus.

::: solution
**Goal:** Give explicit nonnormal subgroups of $\pi_1(K)$.

Let
$$
\pi_1(K)=\langle a,b\mid a b a^{-1}=b^{-1}\rangle.
$$

<1> Nonnormal cover by a Klein bottle.
    *Proof:*
    <2>1. Let
        $$
        H_K=\langle a, b^2\rangle.
        $$
    <2>2. Compute
        $$
        a(b^2)a^{-1}=(aba^{-1})^2=b^{-2}.
        $$
        Hence
        $$
        H_K\cong\langle a,b^2\mid ab^2a^{-1}=b^{-2}\rangle,
        $$
        so $H_K$ is a Klein bottle group and is the fundamental group of a Klein-bottle cover of $K$.
    <2>3. Not normal: since
        $$
        b\cdot b^2\cdot b^{-1}=b\notin H_K,
        $$
        the subgroup is not normal.

<1> Nonnormal cover by a torus.
    *Proof:*
    <2>1. Let
        $$
        H_T=\langle a^2,b^2\rangle.
        $$
    <2>2. Using the relation $a b a^{-1}=b^{-1}$,
        $$
        a^2b^2a^{-2}=b^2.
        $$
        Hence every element of $H_T$ commutes, so $H_T\cong\mathbb Z^2$.
    <2>3. Not normal:
        $$
        b a^2 b^{-1}=a^2b^{-3}\notin H_T
        $$
        Since elements of $H_T$ have even powers of both $a$ and $b$, $a^2b^{-3}\notin H_T$.
    <2>4. Consider
        $$
        \pi_1(K)\twoheadrightarrow (\mathbf Z/2)\times (\mathbf Z/2),\qquad
        a^m b^n\mapsto (m\bmod 2,n\bmod 2).
        $$
        Because the relation $ab a^{-1}=b^{-1}$ preserves both parities, this is a well-defined quotient and
        $$
        H_T=\ker(\pi_1(K)\to (\mathbf Z/2)\times (\mathbf Z/2)).
        $$
        Therefore $[\pi_1(K):H_T]=4$, so the corresponding cover is finite and has torus as total space.

<1> Therefore both nonnormal covering spaces requested exist.

Authored by **Codex 5.3 Spark Extra High**.
:::
