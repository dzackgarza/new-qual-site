---
schema: qual/card@1
id: P-AMH-ALG-SG16-09
kind: problem
title: Homomorphisms from a group of order 144 to a group of order 25 are trivial
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(January 2012) Let $G$ and $H$ be groups.
Recall that a homomorphism $\varphi:G\to H$ is said to be trivial if $\varphi(g)=e_H$ for all $g\in G$.
If $|G|=144$ and $|H|=25$, prove that any homomorphism $\varphi:G\to H$ is trivial.
:::

::: {.solution}
Proof.
Giveng∈G. By Lagrange’s Theorem for G, we have g144 =eG Since φ is a homomorphism, we have (φ(g))144 =φ(g144) =φ(eG) =eH. Thus, φ(g), which is an element of H, has ﬁnite order m = o(φ(g)) that divides 144. On the other hand, by Lagrange’s Theorem forH, we also havem|25, since|H| = 25. Thus, m is a common divisor of 144 = 2432 and 25 = 52. Since gcd(144, 25) = gcd(2432, 52) = 1, we must have o ( φ(g) ) = 1. Thus, φ(g) =eH, as desired.
QED
:::
