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

::: {.problem}
Suppose $f, g: A \to A$ are functions with $f \circ g$ injective.

a) Prove that $g$ must be injective.

b) Give an example to show that $f$ need not be injective.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
$g$ is injective.

::: pf-proof

::: {.pf-step #p1-1-1}
Suppose $g(x) = g(y)$ for $x, y \in A$.

::: pf-proof
take two elements with equal image under $g$.
:::

:::

::: {.pf-step #p1-1-2}
Then $(f \circ g)(x) = f(g(x)) = f(g(y)) = (f \circ g)(y)$.

::: pf-proof
apply $f$ to both sides of $g(x) = g(y)$.
:::

:::

::: {.pf-step #p1-1-3}
Since $f \circ g$ is injective, $x = y$.

::: pf-proof
injectivity of $f \circ g$ applied to step [](#p1-1-2){.pf-ref}.
:::

:::

::: pf-step
Hence $g(x) = g(y)$ implies $x = y$, so $g$ is injective.

::: pf-proof
Steps [](#p1-1-1){.pf-ref}, [](#p1-1-2){.pf-ref} and [](#p1-1-3){.pf-ref}.
:::

:::

:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #p2-1}
Take $A = \NN$ (or any set with at least two elements), and define $g(n) = 2n$ and $f(n) = \lfloor n/2 \rfloor$.

::: pf-proof

::: pf-step
$g$ is injective.

::: pf-proof
$2n = 2m$ implies $n = m$.
:::

:::

::: pf-step
$f \circ g = \id_{\NN}$.

::: pf-proof
$(f \circ g)(n) = f(2n) = \lfloor 2n/2 \rfloor = n$.
:::

:::

::: pf-step
Hence $f \circ g$ is injective.

::: pf-proof
the identity is injective.
:::

:::

::: pf-step
But $f$ is not injective.

::: pf-proof
$f(0) = 0$ and $f(1) = 0$, yet $0 \neq 1$.
:::

:::

:::

:::

::: pf-qed
Step [](#p2-1){.pf-ref} gives an example where $f \circ g$ is injective but $f$ is not.
:::

:::
:::
