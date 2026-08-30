---
schema: qual/card@1
id: P-2XYZ3
kind: problem
title: Finite division rings are fields, and an infinite noncommutative example
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Rings
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Prove that any finite division ring is a field (that is, prove commutativity).
Give an example of a (necessarily infinite) division ring which is NOT a field.
:::

::: solution
**Goal:** Show finite division rings are commutative and supply a noncommutative infinite example.

<1> Let $D$ be a finite division ring.
    By Wedderburn’s little theorem, every finite division ring is commutative.
    Hence $D$ is a finite field.

<1> For a noncommutative infinite division ring, take the quaternion algebra
    $$
    \mathbb H=\{a+bi+cj+dk: a,b,c,d\in\mathbb R,\ i^2=j^2=k^2=ijk=-1\}.
    $$
    It is a division ring and not commutative because $ij=-ji$.

Authored by **Codex 5.3 Spark Extra High**.
:::
