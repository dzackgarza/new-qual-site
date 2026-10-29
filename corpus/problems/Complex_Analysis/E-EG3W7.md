---
schema: qual/card@1
id: E-EG3W7
kind: problem
title: Isolated zeros of $f'$, and $f'=g'$ implies $f-g$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
  - Identity Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Let $\Omega \subseteq \CC$ be a connected open region.

(1) Prove that if $f: \Omega \to \CC$ is a non-constant holomorphic function, then $f'$ is holomorphic on $\Omega$ and the zeros of $f'$ are isolated in $\Omega$.

(2) Prove that if $f, g: \Omega \to \CC$ are holomorphic functions satisfying $f'(z) = g'(z)$ for all $z \in \Omega$, then $f(z) - g(z) = C$ for some constant $C \in \CC$.
:::

::: {.solution}

::: pf

::: pf-step
(1) $f'$ is holomorphic on $\Omega$ and its zeros are isolated.

::: pf-proof
The derivative of a holomorphic function is holomorphic.
If the zeros of $f'$ had an accumulation point in $\Omega$, the identity theorem on the connected set $\Omega$ would give $f'\equiv0$.
A holomorphic function with zero derivative on a connected open set is constant, which contradicts the hypothesis.
:::

:::

::: pf-step
(2) $f-g=C$ for some $C\in\CC$.

::: pf-proof
Put $h=f-g$. Then $h$ is holomorphic and $h'=f'-g'=0$ on $\Omega$, so $h$ is constant on the connected set $\Omega$.
:::

:::

:::

:::
