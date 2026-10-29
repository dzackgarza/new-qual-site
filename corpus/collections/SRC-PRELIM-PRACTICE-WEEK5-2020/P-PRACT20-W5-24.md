---
schema: qual/card@1
id: P-PRACT20-W5-24
kind: problem
title: Harmonic conjugate of $2x+3y$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 24).
---

::: {.problem}
If $f(z) = (2x + 3y) + i\,g(x, y)$ is analytic and $g(2, 3) = 1$, what is $g(x, y)$?
:::

::: {.solution}

Let
$$
u(x,y)=2x+3y,
\qquad
v(x,y)=g(x,y).
$$

::: pf

::: pf-step

The Cauchy--Riemann equations give
$$
g_y=2
\qquad\text{and}\qquad
g_x=-3.
$$


::: pf-proof

Since $f=u+iv$ is analytic,
$$
u_x=v_y
\qquad\text{and}\qquad
u_y=-v_x.
$$
Here
$$
u_x=2,
\qquad
u_y=3,
$$
so
$$
g_y=v_y=2
$$
and
$$
g_x=v_x=-3.
$$

:::

:::

::: {.pf-step #s1-2}

There is a real constant $C$ such that
$$
g(x,y)=-3x+2y+C.
$$


::: pf-proof

Integrating
$$
g_x=-3
$$
with respect to $x$ gives
$$
g(x,y)=-3x+h(y)
$$
for some function $h$. Differentiating with respect to $y$ and using
$g_y=2$ yields
$$
h'(y)=2,
$$
so
$$
h(y)=2y+C.
$$

:::

:::

::: {.pf-step #s1-3}

The condition $g(2,3)=1$ gives
$$
C=1.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
1=g(2,3)
=-3(2)+2(3)+C
=C.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{g(x,y)=-3x+2y+1}.
$$


::: pf-proof

Substitute the value of $C$ from step [](#s1-3){.pf-ref} into the formula from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required harmonic conjugate.

:::

:::

:::
