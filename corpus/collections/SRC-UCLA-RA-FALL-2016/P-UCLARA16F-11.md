---
schema: qual/card@1
id: P-UCLARA16F-11
kind: problem
title: Entire functions with $f(z)f(1/z)$ bounded are monomials
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Suppose $f:\CC\to\CC$ is holomorphic and the function
$$
z\longmapsto g(z)=f(z)f(1/z)
$$
is bounded on $\CC\setminus\{0\}$.

(a) Show that if $f(0)\ne0$, then $f$ is constant.

(b) Show that if $f(0)=0$, then there exist $n\in\NN$ and $a\in\CC$ such that $f(z)=az^n$ for all $z\in\CC$.
:::

::: {.solution}

Assume
$$
|f(z)f(1/z)|\le M
$$
for every $z\ne0$.

## Part (a)

Assume
$$
f(0)\ne0.
$$

::: pf

::: {.pf-step #s1-1}

Since $f$ is continuous at $0$,
$$
\boxed{
f(1/z)\to f(0)}
$$
as $|z|\to\infty$.


::: pf-proof

As $|z|\to\infty$,
$$
1/z\to0.
$$
Apply continuity of the entire function $f$.

:::

:::

::: {.pf-step #s1-2}

There exists $R>0$ such that for $|z|\ge R$,
$$
\boxed{
|f(1/z)|\ge\frac{|f(0)|}{2}>0}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, choose $R$ so large that
$$
|f(1/z)-f(0)|
<
\frac{|f(0)|}{2}
$$
whenever $|z|\ge R$. The reverse triangle inequality gives
$$
|f(1/z)|
\ge
|f(0)|
-
|f(1/z)-f(0)|
>
\frac{|f(0)|}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

Hence for $|z|\ge R$,
$$
\boxed{
|f(z)|
\le
\frac{2M}{|f(0)|}}.
$$


::: pf-proof

By hypothesis,
$$
|f(z)|\,|f(1/z)|
\le
M.
$$
Use the lower bound from step [](#s1-2){.pf-ref} and divide.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is bounded on the closed disk
$$
\{|z|\le R\}.
$$


::: pf-proof

The entire function $f$ is continuous, and the closed disk is compact.

:::

:::

::: pf-step

Therefore $f$ is bounded on all of $\CC$.


::: pf-proof

Use step [](#s1-3){.pf-ref} outside the disk and step [](#s1-4){.pf-ref} inside.

:::

:::

::: {.pf-step #s1-6}

By Liouville's theorem,
$$
\boxed{
f\text{ is constant}.}
$$


::: pf-proof

An entire bounded function is constant.

:::

:::

::: pf-step

If
$$
f\equiv0,
$$
then the desired conclusion holds.


::: pf-proof

Choose any $n\in\NN$ and set
$$
a=0.
$$
Then
$$
f(z)=az^n=0.
$$

:::

:::

::: {.pf-step #s1-8}

There exists a unique integer
$$
n\ge1
$$
and an entire function $h$ such that
$$
\boxed{
f(z)=z^n h(z)}
$$
and
$$
\boxed{
h(0)\ne0}.
$$


::: pf-proof

Since $f$ is nonzero entire and vanishes at $0$, the zero at $0$ has finite positive order $n$. Dividing the Taylor series by $z^n$ gives an entire function $h$ with nonzero constant term.

:::

:::

::: pf-step

For $z\ne0$,
$$
f(1/z)
=
z^{-n}h(1/z).
$$


::: pf-proof

Apply the factorization from step [](#s1-8){.pf-ref} at the point $1/z$.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
f(z)f(1/z)
=
h(z)h(1/z)}
$$
for every $z\ne0$.


::: pf-proof

Multiply
$$
z^nh(z)
$$
by
$$
z^{-n}h(1/z).
$$
The powers of $z$ cancel.

:::

:::

::: {.pf-step #s1-11}

The function
$$
z\longmapsto h(z)h(1/z)
$$
is bounded on $\CC\setminus\{0\}$.


::: pf-proof

By step [](#s1-10){.pf-ref}, it is exactly the originally bounded function
$$
f(z)f(1/z).
$$

:::

:::

::: pf-step

Since
$$
h(0)\ne0,
$$
part (a) applies to $h$.


::: pf-proof

The function $h$ is entire by step [](#s1-8){.pf-ref}, its value at $0$ is nonzero, and its product
$$
h(z)h(1/z)
$$
is bounded by step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Hence
$$
\boxed{
h(z)\equiv a}
$$
for some $a\in\CC$.


::: pf-proof

Apply step [](#s1-6){.pf-ref} to $h$.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
f(z)=az^n}
$$
for all $z\in\CC$.


::: pf-proof

Substitute the constant $h\equiv a$ from step [](#s1-13){.pf-ref} into
$$
f(z)=z^nh(z).
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} proves part (b).

:::

:::

:::
