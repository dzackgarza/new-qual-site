---
schema: qual/card@1
id: P-S04FG
kind: problem
title: If $f\circ g$ is injective then $g$ is injective, but $f$ need not be
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Suppose $f, g: A \to A$ are functions with $f \circ g$ injective.

a) Prove that $g$ must be injective.

b) Give an example to show that $f$ need not be injective.
:::

::: {.solution}
**Part (a).**

<1>1. $g$ is injective.
<2>1. Suppose $g(x) = g(y)$ for $x, y \in A$.
::: {.proof}
take two elements with equal image under $g$.
:::
<2>2. Then $(f \circ g)(x) = f(g(x)) = f(g(y)) = (f \circ g)(y)$.
::: {.proof}
apply $f$ to both sides of $g(x) = g(y)$.
:::
<2>3. Since $f \circ g$ is injective, $x = y$.
::: {.proof}
injectivity of $f \circ g$ applied to <2>2.
:::
<2>4. Hence $g(x) = g(y)$ implies $x = y$, so $g$ is injective.
::: {.proof}
<2>1–<2>3.
:::

**Part (b).**

<1>1. Take $A = \NN$ (or any set with at least two elements), and define $g(n) = 2n$ and $f(n) = \lfloor n/2 \rfloor$.
<2>1. $g$ is injective.
::: {.proof}
$2n = 2m$ implies $n = m$.
:::
<2>2. $f \circ g = \id_{\NN}$.
::: {.proof}
$(f \circ g)(n) = f(2n) = \lfloor 2n/2 \rfloor = n$.
:::
<2>3. Hence $f \circ g$ is injective.
::: {.proof}
the identity is injective.
:::
<2>4. But $f$ is not injective.
::: {.proof}
$f(0) = 0$ and $f(1) = 0$, yet $0 \neq 1$.
:::

<1>2. Q.E.D.
::: {.proof}
<1>1 gives an example where $f \circ g$ is injective but $f$ is not.
:::
:::
