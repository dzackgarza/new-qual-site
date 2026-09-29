---
schema: qual/card@1
id: P-BERK85S-01
kind: problem
title: Increasing derivative implies monotonicity of $f(x)/x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Reviewed the later Berkeley Fall 2010 solution of the same positive-x
    claim. Replaced its unjustified strict inequality by the non-strict
    inequality implied by monotonicity and separately checked the endpoint
    value g(0)=f'(0).
---

::: {.problem}
Let $f:[0,\infty)\to\mathbb R$ be continuous and differentiable, with $f(0)=0$, and suppose $f'$ is increasing on $[0,\infty)$. Prove that
\[
g(x)=
\begin{cases}
f(x)/x,&x>0,\\
f'(0),&x=0
\end{cases}
\]
is increasing.
:::

::: {.solution}
::: pf

::: {.pf-step #mvt-inequality}
For every $x>0$,
$$
\frac{f(x)}{x}\leq f'(x).
$$

::: pf-proof
Fix $x>0$. By the mean value theorem applied to $f$ on $[0,x]$, there is
$c\in(0,x)$ such that
$$
f'(c)
=
\frac{f(x)-f(0)}{x-0}
=
\frac{f(x)}{x}.
$$
Since $f'$ is increasing and $c<x$,
$$
f'(c)\leq f'(x).
$$
Substitution gives the claim.
:::

:::

::: {.pf-step #g-prime-nonnegative}
For every $x>0$,
$$
g'(x)\geq0.
$$

::: pf-proof
For $x>0$,
$$
\begin{aligned}
g'(x)
&=
\frac{x f'(x)-f(x)}{x^2}\\
&=
\frac{f'(x)-f(x)/x}{x}.
\end{aligned}
$$
The numerator is nonnegative by step [](#mvt-inequality){.pf-ref}, and $x>0$.
:::

:::

::: {.pf-step #g-increasing-positive}
The function $g$ is increasing on $(0,\infty)$.

::: pf-proof
By step [](#g-prime-nonnegative){.pf-ref}, $g'(x)\geq0$ throughout $(0,\infty)$. The standard
monotonicity theorem for differentiable functions therefore gives that
$g$ is increasing there.
:::

:::

::: {.pf-step #g-zero-bound}
For every $x>0$,
$$
g(0)\leq g(x).
$$

::: pf-proof
The point $c\in(0,x)$ furnished by the mean value theorem in step [](#mvt-inequality){.pf-ref}
satisfies
$$
g(x)
=
\frac{f(x)}x
=
f'(c).
$$
Since $0<c$ and $f'$ is increasing on $[0,\infty)$,
$$
f'(0)\leq f'(c).
$$
By the definition of $g(0)$, this is exactly $g(0)\leq g(x)$.
:::

:::

::: {.pf-step #conclusion-boxed}
Therefore
$$
\boxed{g\text{ is increasing on }[0,\infty)}.
$$

::: pf-proof
Step [](#g-increasing-positive){.pf-ref} compares any two positive arguments, and step [](#g-zero-bound){.pf-ref} compares
$0$ with every positive argument.
:::

:::

::: pf-qed
Step [](#conclusion-boxed){.pf-ref} is the required conclusion.
:::

:::
:::
