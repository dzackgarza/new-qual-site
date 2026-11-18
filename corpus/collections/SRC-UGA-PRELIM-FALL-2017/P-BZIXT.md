---
schema: qual/card@1
id: P-BZIXT
kind: problem
title: A left inverse forces $f$ injective and $g$ surjective, but neither need be
  bijective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: composing with g
    gives injectivity of f, the element f(x) is a preimage under g, and the example
    X = {1}, Y = {1,2}, f(1) = 1, g(1) = g(2) = 1 satisfies g o f = id_X with f not
    surjective and g not injective. The statement is true as printed; the witness in part
    (c) is now checked condition by condition rather than asserted. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Let $X$ and $Y$ be sets, and let $f:X\to Y$ and $g:Y\to X$ satisfy
$$
g(f(x))=x
$$
for every $x\in X$.

(a) Show that $f$ is injective.

(b) Show that $g$ is surjective.

(c) Give an example in which neither $f$ nor $g$ is bijective.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Throughout, $f:X\to Y$ and $g:Y\to X$ satisfy $g(f(x))=x$ for every $x\in X$.

::: pf

::: {.pf-step #injective}
(a) $f$ is injective.

::: pf-proof
If $f(x_1)=f(x_2)$ then applying $g$ to both sides and using the hypothesis gives $x_1=g(f(x_1))=g(f(x_2))=x_2$.
:::

:::

::: {.pf-step #surjective}
(b) $g$ is surjective.

::: pf-proof
Let $x\in X$. The element $y\coloneqq f(x)$ lies in $Y$ and satisfies $g(y)=x$ by hypothesis, so $x$ lies in the image of $g$; $x$ was arbitrary.
:::

:::

::: {.pf-step}
(c) There are sets and maps as above with neither $f$ nor $g$ bijective.

::: pf-proof
Take $X=\{1\}$, $Y=\{1,2\}$, $f(1)=1$ and $g(1)=g(2)=1$. Then $g(f(1))=g(1)=1$, so $g\circ f=\operatorname{id}_X$. The element $2\in Y$ is not in the image of $f$, so $f$ is not surjective; and $g(1)=g(2)$ with $1\ne2$, so $g$ is not injective. Hence neither map is bijective, while by parts (a) and (b) $f$ is injective and $g$ surjective.
:::

:::

:::
:::
