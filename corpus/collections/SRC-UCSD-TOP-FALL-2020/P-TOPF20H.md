---
schema: qual/card@1
id: P-TOPF20H
kind: problem
title: "A CW complex with finite nontrivial pi_1 and no higher homotopy cannot be finite"
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Euler Characteristic
  - Universal Cover
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $X$ be a connected CW complex such that $\pi_1(X)$ is a nontrivial finite group and $\pi_k(X) = 0$ for any $k \geq 2$.
Show that $X$ can not be a finite CW complex.
(Namely, $X$ must have infinitely many cells.)
Hint: Compute the Euler characteristic of the universal covering space.
:::

::: solution
**Goal:** Show that a finite connected CW complex cannot satisfy both
 finite nontrivial $\pi_1(X)$ and trivial higher homotopy groups.

<1> Assume $X$ is finite and let $\widetilde X$ be its universal cover.
    *Proof:* $\pi_1(X)$ acts freely on $\widetilde X$ by deck transformations.

<1> Claim: $\widetilde X$ is contractible.
    <2>1. Since $\widetilde X$ is a universal cover, $\pi_1(\widetilde X)=0$.
    <2>2. For $k\ge2$, covering space theory gives
        $$
        \pi_k(\widetilde X)\cong \pi_k(X)=0.
        $$
        Hence every homotopy group of $\widetilde X$ is zero.
    <2>3. As a CW complex, Whitehead implies $\widetilde X$ is contractible.

<1> Claim: the covering has finite degree.
    *Proof:* $\deg(p)=|\pi_1(X)|$, and this is finite and at least $2$ because $\pi_1(X)$ is nontrivial finite.

<1> Claim: $\widetilde X$ has finitely many cells.
    <2>1. If $X$ has finitely many $n$-cells $c_n$, each lifts to exactly $|\pi_1(X)|$ $n$-cells in $\widetilde X$.
    <2>2. So $\widetilde X$ is also a finite CW complex.

<1> Claim: Euler characteristics conflict.
    <2>1. For a finite CW complex, $\chi(\widetilde X)=\sum_n(-1)^n |\widetilde c_n|$ is an integer.
    <2>2. Because the cover is finite of degree $d=|\pi_1(X)|$ and cell lifts are disjoint by sheets,
        $$
        |\widetilde c_n|=d\,c_n,\qquad
        \chi(\widetilde X)=d\,\chi(X).
        $$
    <2>3. Contractibility gives $\chi(\widetilde X)=1$, so $d\,\chi(X)=1$.
    <2>4. The integer $\chi(X)$ cannot satisfy this when $d\ge2$.
        Indeed $1/d\notin\mathbb Z$, contradiction.

<1> Therefore $X$ cannot be a finite CW complex.

Authored by **Codex 5.3 Spark Extra High**.
:::
