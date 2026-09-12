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
Let $\Omega \subseteq \mathbb{C}$ be a connected open region.
(1) Prove that if $f: \Omega \to \mathbb{C}$ is a non-constant holomorphic function, then $f'$ is holomorphic on $\Omega$ and the zeros of $f'$ are **isolated** in $\Omega$.
(2) Prove that if $f, g: \Omega \to \mathbb{C}$ are holomorphic functions satisfying $f'(z) = g'(z)$ for all $z \in \Omega$, then $f(z) - g(z) = C$ for some constant $C \in \mathbb{C}$.
:::

::: solution
Because $f$ is holomorphic, $f'$ is holomorphic.

If the zeros of $f'$ had an accumulation point in $\Omega$, the identity theorem would give
\[
f'\equiv0.
\]
A holomorphic function with zero derivative on a connected domain is constant, contradicting the hypothesis. Hence the zeros of $f'$ are isolated.

For the second statement, let
\[
h=f-g.
\]
Then $h$ is holomorphic and
\[
h'=f'-g'=0.
\]
Therefore $h$ is constant on the connected domain $\Omega$. Thus
\[
f-g=C
\]
for some $C\in\mathbb C$.
:::
