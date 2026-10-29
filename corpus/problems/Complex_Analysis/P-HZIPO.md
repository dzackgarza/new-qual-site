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
$$
\forall a\in \DD, \qquad {\abs{f'(a)} \over 1 - \abs{f(a)}^2 } \leq {1 \over 1 - \abs{a}^2}
.$$
:::

::: {.solution}
For $w\in\DD$ write $\phi_w(z) \coloneqq \dfrac{z - w}{1 - \bar w z}$. It is a Möbius automorphism of $\DD$ with $\phi_w(w)=0$, inverse $\phi_w^{-1}(z)=\dfrac{z+w}{1+\bar w z}$, and derivative $\phi_w'(z)=\dfrac{1-\abs w^2}{(1-\bar w z)^2}$.

::: pf

::: {.pf-step #schwarz-bound}
$F \coloneqq \phi_{f(a)} \circ f \circ \phi_a^{-1}$ is an analytic self-map of $\DD$ with $F(0)=0$, so $\abs{F'(0)}\le 1$.

::: pf-proof
$F$ is a composition of analytic self-maps of $\DD$, and $F(0)=\phi_{f(a)}(f(a))=0$. Schwarz's lemma gives the bound.
:::

:::

::: {.pf-step #F-prime}
$F'(0) = f'(a)\,\dfrac{1 - \abs a^2}{1 - \abs{f(a)}^2}$.

::: pf-proof
By the chain rule, $F'(0)=\phi_{f(a)}'(f(a))\,f'(a)\,(\phi_a^{-1})'(0)$. Here $\phi_{f(a)}'(f(a)) = \frac{1}{1-\abs{f(a)}^2}$, and differentiating $\phi_a^{-1}$ gives $(\phi_a^{-1})'(0) = 1-\abs a^2$.
:::

:::

::: pf-step
$\dfrac{\abs{f'(a)}}{1 - \abs{f(a)}^2} \leq \dfrac{1}{1 - \abs a^2}$.

::: pf-proof
Steps [](#schwarz-bound){.pf-ref} and [](#F-prime){.pf-ref} give $\abs{f'(a)}\frac{1 - \abs a^2}{1 - \abs{f(a)}^2}\le 1$. Divide by $1-\abs a^2>0$.
:::

:::

:::

:::
