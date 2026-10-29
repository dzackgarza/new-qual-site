---
schema: qual/card@1
id: P-5U7QZ
kind: problem
title: A sharp bound on $\abs{f'(0)}$ for maps to the right half-plane with $f(0)=2$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $\HH_R\coloneqq\{w\in\CC:\Re w>0\}$.
Suppose $f:\DD\to\HH_R$ is analytic and satisfies $f(0)=2$.
Find a sharp upper bound for $\abs{f'(0)}$, and prove it is sharp by example.
:::

::: {.solution}
Let $\HH$ be the upper half-plane, and let
$$
r(w)=\frac{i}{2}w:\HH_R\to\HH,
\qquad
C(w)=\frac{w-i}{w+i}:\HH\to\DD.
$$

::: pf

::: {.pf-step #schwarz}
$F\coloneqq C\circ r\circ f:\DD\to\DD$ satisfies $F(0)=0$ and $\abs{F'(0)}\le1$.

::: pf-proof
$r$ maps $\HH_R$ into $\HH$ because $\Im\bigl(\tfrac{i}{2}w\bigr) = \tfrac12\Re w$, and the Cayley map $C$ maps $\HH$ into $\DD$.
Since $r(2)=i$ and $C(i)=0$, $F(0)=0$.
Schwarz's lemma gives $\abs{F'(0)}\le1$.
:::

:::

::: pf-step
$\boxed{\abs{f'(0)}\le4}$.

::: pf-proof
By the chain rule, $F'(0)=C'(i)\cdot\frac{i}{2}\cdot f'(0)$.
Since $C'(w)=\frac{2i}{(w+i)^2}$, $\abs{C'(i)}=\frac12$, so $\abs{F'(0)}=\frac14\abs{f'(0)}$.
Step [](#schwarz){.pf-ref} gives $\abs{f'(0)}\le4$.
:::

:::

::: pf-step
The bound is attained.

::: pf-proof
For $\abs{\lambda}=1$, the map
$$
f(z)=2\,\frac{1+\lambda z}{1-\lambda z}
$$
sends $\DD$ biholomorphically onto $\HH_R$, satisfies $f(0)=2$, and has $f'(0)=4\lambda$, so $\abs{f'(0)}=4$.
:::

:::

:::

:::
