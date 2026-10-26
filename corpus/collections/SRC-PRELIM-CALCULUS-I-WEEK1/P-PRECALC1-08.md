---
schema: qual/card@1
id: P-PRECALC1-08
kind: problem
title: Mean value bound on $f(0)$ from $f(3)=5$ and $f'\ge1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the map from R to R of Problem 8 on page 2 of Week1_solns.pdf.
---

::: {.problem}
If $f : \mathbb{R} \to \mathbb{R}$ is continuously differentiable on $(-1, 4)$ with $f(3) = 5$ and $f'(x) \geq 1$ for all $x \in (-1, 4)$, what is the greatest possible value of $f(0)$?
:::

::: pf

::: pf-step

By the fundamental theorem of calculus,
\[
\boxed{
f(3)-f(0)
=
\int_0^3 f'(x)\,dx}.
\]


::: pf-proof

The function \(f\) is continuously differentiable on an interval containing
\([0,3]\), so the fundamental theorem applies.

:::

:::

::: pf-step

Since
\[
f'(x)\ge1
\]
for every \(x\in[0,3]\),
\[
\int_0^3 f'(x)\,dx
\ge
\int_0^3 1\,dx.
\]


::: pf-proof

Integrating a pointwise inequality preserves the inequality.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(3)-f(0)\ge3}.
\]


::: pf-proof

By step <1>2,
\[
\int_0^3 f'(x)\,dx
\ge
3.
\]
Use step <1>1.

:::

:::

::: pf-step

Since
\[
f(3)=5,
\]
one has
\[
5-f(0)\ge3.
\]


::: pf-proof

Substitute the given value into step <1>3.

:::

:::

::: pf-step

Hence
\[
\boxed{
f(0)\le2}.
\]


::: pf-proof

Rearrange step <1>4.

:::

:::

::: pf-step

Define
\[
g(x)=x+2.
\]


::: pf-proof

This is a continuously differentiable function on \(\mathbb R\).

:::

:::

::: pf-step

The function \(g\) satisfies
\[
\boxed{
g'(x)=1\ge1}
\]
for every \(x\).


::: pf-proof

Differentiate \(g(x)=x+2\).

:::

:::

::: pf-step

It also satisfies
\[
\boxed{
g(3)=5}.
\]


::: pf-proof

\[
g(3)=3+2=5.
\]

:::

:::

::: pf-step

Finally,
\[
\boxed{
g(0)=2}.
\]


::: pf-proof

\[
g(0)=0+2=2.
\]

:::

:::

::: pf-step

Therefore the bound in step <1>5 is attained.


::: pf-proof

Steps <1>6--<1>9 exhibit an admissible function with \(f(0)=2\).

:::

:::

::: pf-step

Hence the greatest possible value is
\[
\boxed{2}.
\]


::: pf-proof

Step <1>5 gives the upper bound, and step <1>10 shows it is sharp.

:::

:::

::: pf-qed

Step <1>11 is the requested value.

:::

:::
