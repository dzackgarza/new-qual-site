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

::: {.problem}
Problem 4. Suppose that $f : D _ { 1 } ( 0 ) \to \mathbb { C }$ is a one-to-one holomorphic function with $\Omega = f \left( D _ { 1 } ( 0 ) \right)$ Let $g : D _ { 1 } ( 0 ) \to \Omega$ be another holomorphic function with $g ( 0 ) = f ( 0 )$ . Show that for each $0 \leq r < 1$ $g \left( D _ { r } ( 0 ) \right) \subset f \left( D _ { r } ( 0 ) \right)$ .
:::

::: {.solution}
<1>1. $h\da f^{-1}\circ g$ is a holomorphic self-map of $D_1(0)$ with $h(0)=0$.

::: {.proof}
An injective holomorphic map has nonvanishing derivative and open image, so $f^{-1}\colon\Omega\to D_1(0)$ is holomorphic. Then $h$ is holomorphic, and $h(0)=f^{-1}(f(0))=0$.
:::

<1>2. $\abs{h(z)}\le\abs z$ on $D_1(0)$.

::: {.proof}
This is the Schwarz lemma applied to $h$, using step <1>1.
:::

<1>3. Q.E.D.

::: {.proof}
For $\abs z<r$, step <1>2 gives $h(z)\in D_r(0)$, so $g(z)=f(h(z))\in f(D_r(0))$.
:::
:::
