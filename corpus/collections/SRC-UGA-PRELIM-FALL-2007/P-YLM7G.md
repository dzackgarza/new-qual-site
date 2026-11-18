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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for both parts. Part (a) is the two choice steps in order; part (b) is a counterexample whose failure of surjectivity is checked at the explicit element 1 of B, and whose surjectivity is checked through the fact that C is a singleton, so the only map B -> C is constant at 0. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; part (b) is false as claimed and the counterexample given is correct.
---

::: {.problem}
Suppose $A$, $B$, and $C$ are sets, and $f: B \to C$ and $g: A \to B$ are functions.

(a) Prove that if $f$ and $g$ are surjective (onto), then so is $f \circ g$.

(b) Prove or give a counterexample: If $g$ is not surjective, then $f \circ g$ is not surjective.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #parta}
If $f:B\to C$ and $g:A\to B$ are surjective, then $f\circ g:A\to C$ is surjective.

::: pf-proof
Let $c\in C$. Because $f$ is surjective there is $b\in B$ with $f(b)=c$, and because $g$ is surjective there is $a\in A$ with $g(a)=b$. Then $(f\circ g)(a)=f\big(g(a)\big)=f(b)=c$. So every element of $C$ is a value of $f\circ g$.
:::

:::

::: {.pf-step #counterexample}
With $A=\{0\}$, $B=\{0,1\}$, $C=\{0\}$, $g(0)=0$ and $f$ the unique map $B\to C$, the map $g$ is not surjective and $f\circ g$ is surjective.

::: pf-proof
$g$ is not surjective because $1\in B$ and $g(0)=0\ne1$. The only map $B\to C$ is the constant map at $0$, since $C=\{0\}$; so $f\circ g$ is the constant map $A\to C$ at $0$, whose image is $\{0\}=C$, hence surjective.
:::

:::

::: {.pf-step}
Claim (b) is false: a non-surjective $g$ can compose with $f$ to a surjection.

::: pf-proof
Step [](#counterexample){.pf-ref} exhibits such a pair of functions, so the implication asserted in (b) fails for at least one instance. Part (a) is step [](#parta){.pf-ref}.
:::

:::

:::
:::
