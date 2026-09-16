---
schema: qual/card@1
id: P-YLM7G
kind: problem
title: Composition of surjections is surjective, but the converse fails
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

::: {.problem}
Suppose $A$, $B$, and $C$ are sets, and $f: B \to C$ and $g: A \to B$ are functions.

a. Prove that if $f$ and $g$ are surjective (onto), then so is $f \circ g$.

b. Prove or give a counterexample: If $g$ is not surjective, then $f \circ g$ is not surjective.
:::

::: {.solution}
If $f$ and $g$ are surjective and $c\in C$, choose $b\in B$ with $f(b)=c$, then choose $a\in A$ with $g(a)=b$. Hence $(f\circ g)(a)=c$, so $f\circ g$ is surjective.

The converse claim is false. Let
\[
A=\{0\},\qquad B=\{0,1\},\qquad C=\{0\},
\]
let $g(0)=0$, and let $f$ be the unique map $B\to C$. Then $g$ is not surjective, while $f\circ g:A\to C$ is surjective.
:::
