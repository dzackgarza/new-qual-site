---
schema: qual/card@1
id: P-HZIPO
kind: problem
title: Schwarz–Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $f:\DD\to \DD$ is analytic.
Prove that 
\[  
\forall a\in \DD, \qquad {\abs{f'(a)} \over 1 - \abs{f(a)}^2 } \leq {1 \over 1 - \abs{a}^2}
.\]
:::

::: {.solution}
**Goal:** Prove the Schwarz--Pick inequality: if $f: \DD \to \DD$ is analytic, then for every $a \in \DD$,
$$\frac{\abs{f'(a)}}{1 - \abs{f(a)}^2} \leq \frac{1}{1 - \abs a^2}.$$

::: pf

::: pf-step
Recall the automorphism $\phi_a(z) := \frac{z - a}{1 - \bar a z}$ of $\DD$, which maps $a$ to $0$.

::: pf-proof
$\phi_a$ is a M\"obius map taking $\DD$ onto $\DD$ (its pole $1/\bar a$ lies outside the unit disk) and $\phi_a(a) = 0$; its inverse is $\phi_a^{-1}(w) = \frac{w + a}{1 + \bar a w}$.
:::

:::

::: pf-step
Define $F := \phi_{f(a)} \circ f \circ \phi_a^{-1}$; then $F: \DD \to \DD$ is analytic and $F(0) = 0$.

::: pf-proof
$\phi_{f(a)}(f(\phi_a^{-1}(0))) = \phi_{f(a)}(f(a)) = 0$, using $\phi_a^{-1}(0) = a$.
:::

:::

::: {.pf-step #schwarz-bound}
By Schwarz's lemma, $\abs{F'(0)} \leq 1$.

::: pf-proof
Schwarz lemma applies to the analytic map $F: \DD \to \DD$ with $F(0) = 0$.
:::

:::

::: pf-step
Compute $F'(0)$ by the chain rule.

::: pf-proof

::: {.pf-step #chain-rule-expression}
$F'(0) = \phi_{f(a)}'(f(a)) \cdot f'(a) \cdot (\phi_a^{-1})'(0)$.

::: pf-proof
Chain rule for the composition $\phi_{f(a)} \circ f \circ \phi_a^{-1}$.
:::

:::

::: {.pf-step #phi-derivative}
$\phi_w'(z) = \frac{1 - \abs w^2}{(1 - \bar w z)^2}$, so $\phi_{f(a)}'(f(a)) = \frac{1}{1 - \abs{f(a)}^2}$.

::: pf-proof
Differentiate $\phi_w$; at $z = w$ the denominator is $1 - \abs w^2$.
:::

:::

::: {.pf-step #phi-inverse-derivative}
$(\phi_a^{-1})'(0) = 1 - \abs a^2$.

::: pf-proof
$\phi_a^{-1}(w) = \frac{w + a}{1 + \bar a w}$; differentiate and evaluate at $w = 0$: $\frac{1 \cdot 1 - (0 + a)\bar a}{1^2} = 1 - \abs a^2$.
:::

:::

::: {.pf-step #F-prime-formula}
Hence $F'(0) = f'(a) \cdot \frac{1 - \abs a^2}{1 - \abs{f(a)}^2}$.

::: pf-proof
Steps [](#chain-rule-expression){.pf-ref}, [](#phi-derivative){.pf-ref} and [](#phi-inverse-derivative){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #combined-inequality}
Combine with Schwarz's lemma.

::: pf-proof

::: pf-step
$\abs{f'(a)} \cdot \frac{1 - \abs a^2}{1 - \abs{f(a)}^2} \leq 1$.

::: pf-proof
Step [](#schwarz-bound){.pf-ref} and step [](#F-prime-formula){.pf-ref}.
:::

:::

::: pf-step
Divide by the positive quantity $1 - \abs a^2$.

::: pf-proof
$\abs a < 1$, so $1 - \abs a^2 > 0$.
:::

:::

:::

:::

::: pf-qed
Step [](#combined-inequality){.pf-ref} gives $\frac{\abs{f'(a)}}{1 - \abs{f(a)}^2} \leq \frac{1}{1 - \abs a^2}$.
:::

:::

:::
