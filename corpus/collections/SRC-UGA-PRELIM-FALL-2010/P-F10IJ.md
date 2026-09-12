---
schema: qual/card@1
id: P-F10IJ
kind: problem
title: Injectivity of $g\circ f$ versus injectivity of $f$ and $g$
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Suppose $f: A \to B$ and $g: B \to C$ are functions.
Prove or give a counterexample:

a. If $f$ and $g$ are injective (one-to-one), then $g \circ f$ is injective.

b. If $g \circ f$ is injective, then $f$ and $g$ are injective.
:::

::: solution
(a) True. If $(g\circ f)(a_1)=(g\circ f)(a_2)$, injectivity of $g$ gives $f(a_1)=f(a_2)$, and injectivity of $f$ then gives $a_1=a_2$.

(b) False as stated. Injectivity of $g\circ f$ does force $f$ to be injective: if $f(a_1)=f(a_2)$, then $(g\circ f)(a_1)=(g\circ f)(a_2)$, hence $a_1=a_2$.

But it need not force $g$ to be injective on all of $B$. Let
\[
A=\{0\},\quad B=\{0,1\},\quad C=\{0\},
\]
let $f(0)=0$, and let $g(0)=g(1)=0$. Then $g\circ f$ is injective because its domain has one element, but $g$ is not injective.
:::
