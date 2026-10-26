---
schema: qual/card@1
id: P-TRIV-RA59
kind: problem
title: Solutions of the exponential functional equation $f(x)f(y)=f(x+y)$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 59, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find all differentiable solutions of the equation $f ( x ) f ( y ) = f ( x + y )$ . Find all continuous solutions of the same equation.
:::

Assume $f:\mathbb R\to\mathbb R$.

::: pf

::: pf-step

Every solution satisfies
$$
f(0)\in\{0,1\}.
$$


::: pf-proof

Set $x=y=0$ in the functional equation:
$$
f(0)^2=f(0).
$$
Thus
$$
f(0)(f(0)-1)=0.
$$

:::

:::

::: pf-step

If
$$
f(0)=0,
$$
then
$$
f\equiv0.
$$


::: pf-proof

For every $x$,
$$
f(x)
=
f(x+0)
=
f(x)f(0)
=0.
$$

:::

:::

::: pf-step

Every nonzero solution therefore satisfies
$$
f(0)=1
$$
and
$$
f(x)\neq0
$$
for every $x$.


::: pf-proof

If the solution is not identically zero, step <1>2 excludes $f(0)=0$, so
$f(0)=1$. Also
$$
1
=
f(0)
=
f(x)f(-x),
$$
which forces $f(x)\neq0$.

:::

:::

::: pf-step

Suppose $f$ is differentiable and nonzero. Then
$$
f'(x)
=
f'(0)f(x).
$$


::: pf-proof

Fix $x$ and write
$$
f(x+h)=f(x)f(h).
$$
Then
$$
\frac{f(x+h)-f(x)}h
=
f(x)
\frac{f(h)-1}{h},
$$
using $f(0)=1$ from step <1>3. Let $h\to0$:
$$
f'(x)=f(x)f'(0).
$$

:::

:::

::: pf-step

Hence every differentiable nonzero solution is
$$
f(x)=e^{cx}
$$
for some $c\in\mathbb R$.


::: pf-proof

Put
$$
c=f'(0).
$$
Step <1>4 gives the initial-value problem
$$
f'=cf,
\qquad
f(0)=1.
$$
Its unique solution is
$$
f(x)=e^{cx}.
$$

:::

:::

::: pf-step

Therefore the differentiable solutions are exactly
$$
\boxed{f\equiv0}
$$
and
$$
\boxed{f(x)=e^{cx},\quad c\in\mathbb R}.
$$


::: pf-proof

Steps <1>2 and <1>5 show necessity. Conversely, the zero function satisfies
the equation, and
$$
e^{cx}e^{cy}=e^{c(x+y)}
$$
for every $c$.

:::

:::

::: pf-step

Now suppose only that $f$ is continuous and nonzero. Then
$$
f(x)>0
$$
for every $x$.


::: pf-proof

By step <1>3, $f$ never vanishes. Moreover,
$$
f(x)
=
f\left(\frac x2+\frac x2\right)
=
f\left(\frac x2\right)^2
>0.
$$

:::

:::

::: pf-step

Define
$$
g(x)=\log f(x).
$$
Then $g$ is continuous and satisfies
$$
g(x+y)=g(x)+g(y).
$$


::: pf-proof

Step <1>7 makes the logarithm well-defined. Continuity of $f$ and of the
logarithm gives continuity of $g$. The functional equation gives
$$
\begin{aligned}
g(x+y)
&=
\log f(x+y)\\
&=
\log(f(x)f(y))\\
&=
g(x)+g(y).
\end{aligned}
$$

:::

:::

::: pf-step

Every continuous additive function has the form
$$
g(x)=cx
$$
for some $c\in\mathbb R$.


::: pf-proof

Let
$$
c=g(1).
$$
Additivity gives
$$
g(n)=nc
$$
for integers $n$, and then
$$
g\left(\frac mn\right)
=
\frac mn c
$$
for rationals $m/n$. For arbitrary $x\in\mathbb R$, choose rationals
$q_j\to x$. Continuity gives
$$
g(x)
=
\lim_j g(q_j)
=
\lim_j cq_j
=
cx.
$$

:::

:::

::: pf-step

Hence every continuous nonzero solution is
$$
f(x)=e^{cx}.
$$


::: pf-proof

By steps <1>8--<1>9,
$$
\log f(x)=cx.
$$
Exponentiate.

:::

:::

::: pf-step

Therefore the continuous solutions are again exactly
$$
\boxed{f\equiv0}
$$
and
$$
\boxed{f(x)=e^{cx},\quad c\in\mathbb R}.
$$


::: pf-proof

Step <1>2 handles the zero solution and step <1>10 handles every nonzero
continuous solution. The converse verification is the same as in step <1>6.

:::

:::

::: pf-qed

Steps <1>6 and <1>11 classify the differentiable and continuous solutions,
respectively.

:::

:::
