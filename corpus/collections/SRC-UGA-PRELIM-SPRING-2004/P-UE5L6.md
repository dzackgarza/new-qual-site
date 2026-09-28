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
<1>1. The function $f$ is differentiable and satisfies
\[
f'(x)=3f(x)
\]
for every $x\in\mathbb R$.
::: {.proof}
Because $f$ is continuous, the function $3f$ is continuous. By the Fundamental Theorem of Calculus,
\[
F(x)=\int_0^x 3f(t)\,dt
\]
is differentiable and $F'(x)=3f(x)$. Since the given equation is $f(x)=5+F(x)$, the function $f$ is differentiable and $f'(x)=3f(x)$.
:::

<1>2. The initial value is
\[
f(0)=5.
\]
::: {.proof}
Substituting $x=0$ into the integral equation gives
\[
f(0)=5+\int_0^0 3f(t)\,dt=5.
\]
:::

<1>3. The only differentiable function satisfying <1>1 and <1>2 is
\[
f(x)=5e^{3x}.
\]
::: {.proof}
Define $h(x)=e^{-3x}f(x)$. Then
\[
h'(x)=e^{-3x}(f'(x)-3f(x))=0,
\]
so $h$ is constant. Since $h(0)=f(0)=5$, we have $h(x)=5$ for all $x$, hence $f(x)=5e^{3x}$.
:::

<1>4. This function indeed satisfies the original integral equation.
::: {.proof}
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
