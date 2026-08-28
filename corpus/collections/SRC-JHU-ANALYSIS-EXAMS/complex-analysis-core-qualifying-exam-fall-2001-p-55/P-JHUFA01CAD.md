---
schema: qual/card@1
id: P-JHUFA01CAD
kind: problem
title: 'Schwarz-Pick: holomorphic self-map of disk maps smaller disks into smaller disks'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Problem 4. Suppose that $f : D _ { 1 } ( 0 ) \to \mathbb { C }$ is a one-to-one holomorphic function with $\Omega = f \left( D _ { 1 } ( 0 ) \right)$ Let $g : D _ { 1 } ( 0 ) \to \Omega$ be another holomorphic function with $g ( 0 ) = f ( 0 )$ . Show that for each $0 \leq r < 1$ $g \left( D _ { r } ( 0 ) \right) \subset f \left( D _ { r } ( 0 ) \right)$ .

::: {.solution}
**Goal.** For $f: D_1(0) \to \CC$ one-to-one holomorphic with $\Omega = f(D_1(0))$, and $g: D_1(0) \to \Omega$ holomorphic with $g(0) = f(0)$, show $g(D_r(0)) \subseteq f(D_r(0))$ for every $0 \le r < 1$.

<1>1. $f^{-1}: \Omega \to D_1(0)$ is holomorphic.
Proof: $f$ is one-to-one and holomorphic with nonvanishing derivative (a one-to-one holomorphic map has $f' \neq 0$ everywhere), so the inverse function theorem gives a holomorphic inverse.

<1>2. Define $h \definedas f^{-1} \circ g: D_1(0) \to D_1(0)$; then $h$ is holomorphic and $h(0) = 0$.
Proof: $h$ is a composition of holomorphic maps, and $h(0) = f^{-1}(g(0)) = f^{-1}(f(0)) = 0$.

<1>3. $\abs{h(z)} \le \abs z$ for all $z \in D_1(0)$.
Proof: the Schwarz lemma applied to the holomorphic self-map $h$ of the unit disk with $h(0) = 0$.

<1>4. $h(D_r(0)) \subseteq D_r(0)$ for each $0 \le r < 1$.
Proof: if $\abs z < r$, then $\abs{h(z)} \le \abs z < r$ by <1>3.

<1>5. $g(D_r(0)) \subseteq f(D_r(0))$.
Proof: for $z \in D_r(0)$, $g(z) = f(h(z))$ with $h(z) \in D_r(0)$ by <1>4, so $g(z) \in f(D_r(0))$.

<1>6. Q.E.D.
Proof: <1>5 is the claim, for arbitrary $0 \le r < 1$.
:::
