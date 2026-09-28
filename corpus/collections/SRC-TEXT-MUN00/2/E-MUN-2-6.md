---
schema: qual/card@1
id: E-MUN-2-6
kind: problem
title: Restricting domain and range to obtain a bijection
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $f: \mathbb{R} \to \mathbb{R}$ be the function $f(x) = x^3 - x$ . By restricting the domain and range of $f$ appropriately, obtain from $f$ a bijective function $g$ . Draw the graphs of $g$ and $g^{-1}$ . (There are several possible choices for $g$ .)
:::

::: {.solution}
Put $c=1/\sqrt3$, so that $f(c)=c^3-c=\frac1{3\sqrt3}-\frac1{\sqrt3}=-\frac2{3\sqrt3}$.

<1>1. $f$ is strictly increasing on $[c,\infty)$.

::: {.proof}
$f'(x)=3x^2-1>0$ for $x>c$.
:::

<1>2. $f([c,\infty))=[-\frac2{3\sqrt3},\infty)$.

::: {.proof}
By step <1>1, $f(x)\ge f(c)$ for $x\ge c$.
Since $f$ is continuous and $f(x)\to\infty$ as $x\to\infty$, the intermediate value theorem gives every value $y\ge f(c)$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2,
$$
\boxed{g\colon[1/\sqrt3,\infty)\to[-2/(3\sqrt3),\infty),\quad g(x)=x^3-x}
$$
is injective and surjective.
Its graph is the part of the cubic $y=x^3-x$ to the right of the local minimum $(c,f(c))$, and the graph of $g^{-1}$ is its reflection in the line $y=x$.
:::
:::
