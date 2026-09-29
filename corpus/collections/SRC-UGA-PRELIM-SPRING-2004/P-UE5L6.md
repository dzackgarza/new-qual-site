---
schema: qual/card@1
id: P-UE5L6
kind: problem
title: Continuous solutions of $f(x)=5+\int_0^x 3f(t)\,dt$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Suppose $f$ is a continuous function satisfying the equation $f(x) = 5 + \int_0^x 3f(t)\,dt$ for all real $x$.
Argue that $f$ must be differentiable and then find all such function(s) explicitly.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f$ is differentiable and satisfies
\[
f'(x)=3f(x)
\]
for every $x\in\mathbb R$.

::: pf-proof

Because $f$ is continuous, the function $3f$ is continuous. By the Fundamental Theorem of Calculus,
\[
F(x)=\int_0^x 3f(t)\,dt
\]
is differentiable and $F'(x)=3f(x)$. Since the given equation is $f(x)=5+F(x)$, the function $f$ is differentiable and $f'(x)=3f(x)$.

:::

:::

::: {.pf-step #s2}

The initial value is
\[
f(0)=5.
\]

::: pf-proof

Substituting $x=0$ into the integral equation gives
\[
f(0)=5+\int_0^0 3f(t)\,dt=5.
\]

:::

:::

::: pf-step

The only differentiable function satisfying steps [](#s1){.pf-ref} and [](#s2){.pf-ref} is
\[
f(x)=5e^{3x}.
\]

::: pf-proof

Define $h(x)=e^{-3x}f(x)$. Then
\[
h'(x)=e^{-3x}(f'(x)-3f(x))=0,
\]
so $h$ is constant. Since $h(0)=f(0)=5$, we have $h(x)=5$ for all $x$, hence $f(x)=5e^{3x}$.

:::

:::

::: pf-step

This function indeed satisfies the original integral equation.

::: pf-proof

For $f(x)=5e^{3x}$,
\[
5+\int_0^x 3f(t)\,dt
=5+15\int_0^x e^{3t}\,dt
=5+5(e^{3x}-1)
=5e^{3x}
=f(x).
\]

:::

:::

:::

:::
