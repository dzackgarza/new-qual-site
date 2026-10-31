---
schema: qual/card@1
id: P-PRECALC1-08
kind: problem
title: Mean value bound on $f(0)$ from $f(3)=5$ and $f'\ge1$
classification:
  areas:
  - prelim
  topics:
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the map from R to R of Problem 8 on page 2 of Week1_solns.pdf.
---

::: {.problem}
If $f : \RR \to \RR$ is continuously differentiable on $(-1, 4)$ with $f(3) = 5$ and $f'(x) \geq 1$ for all $x \in (-1, 4)$, what is the greatest possible value of $f(0)$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

By the fundamental theorem of calculus,
$$
\boxed{
f(3)-f(0)
=
\int_0^3 f'(x)\,dx}.
$$


::: pf-proof

The function $f$ is continuously differentiable on an interval containing
$[0,3]$, so the fundamental theorem applies.

:::

:::

::: {.pf-step #s1-2}

Since
$$
f'(x)\ge1
$$
for every $x\in[0,3]$,
$$
\int_0^3 f'(x)\,dx
\ge
\int_0^3 1\,dx.
$$


::: pf-proof

Integrating a pointwise inequality preserves the inequality.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
f(3)-f(0)\ge3}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\int_0^3 f'(x)\,dx
\ge
3.
$$
Use step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Since
$$
f(3)=5,
$$
one has
$$
5-f(0)\ge3.
$$


::: pf-proof

Substitute the given value into step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
f(0)\le2}.
$$


::: pf-proof

Rearrange step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Define
$$
g(x)=x+2.
$$


::: pf-proof

This is a continuously differentiable function on $\RR$.

:::

:::

::: {.pf-step #s1-7}

The function $g$ satisfies
$$
\boxed{
g'(x)=1\ge1}
$$
for every $x$.


::: pf-proof

Differentiate $g(x)=x+2$.

:::

:::

::: {.pf-step #s1-8}

It also satisfies
$$
\boxed{
g(3)=5}.
$$


::: pf-proof

$$
g(3)=3+2=5.
$$

:::

:::

::: {.pf-step #s1-9}

Finally,
$$
\boxed{
g(0)=2}.
$$


::: pf-proof

$$
g(0)=0+2=2.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore the bound in step [](#s1-5){.pf-ref} is attained.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} exhibit an admissible function with $f(0)=2$.

:::

:::

::: {.pf-step #s1-11}

Hence the greatest possible value is
$$
\boxed{2}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives the upper bound, and step [](#s1-10){.pf-ref} shows it is sharp.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the requested value.

:::

:::

:::
