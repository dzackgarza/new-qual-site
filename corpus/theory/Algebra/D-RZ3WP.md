---
schema: qual/card@1
id: D-RZ3WP
kind: definition
title: Evaluation of a polynomial at an element of a ring
prompts:
- What is evaluation of a polynomial at an element of a ring?
- What is a root of a polynomial over a ring?
classification:
  areas: [algebra]
  topics: [Polynomials]
relations:
- kind: uses
  target: D-GURUB
review: draft
---

::: {.definition}
Let $R$ be a commutative [[D-GURUB|ring]] with identity and let $a\in R$.
\dfn{Evaluation at $a$} is the ring homomorphism $R[x]\to R$ that fixes $R$ and sends $x$ to $a$, so that a polynomial $f=\sum_{i=0}^n c_ix^i$ is sent to
$$
f(a)\coloneqq\sum_{i=0}^n c_ia^i.
$$
The element $a$ is a \dfn{root} of $f$ when $f(a)=0$, and the kernel of evaluation at $a$ is the ideal of polynomials of which $a$ is a root.
:::

::: {.remark}
The factor theorem makes that kernel principal: $f(a)=0$ if and only if $f=(x-a)g$ for some $g\in R[x]$, by dividing $f$ by the monic polynomial $x-a$, so evaluation at $a$ has kernel $\generators{x-a}$.
:::
