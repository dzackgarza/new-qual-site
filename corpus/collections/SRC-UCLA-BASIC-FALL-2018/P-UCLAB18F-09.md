---
schema: qual/card@1
id: P-UCLAB18F-09
kind: problem
title: Decomposition relative to two independent linear functionals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $f,g:\RR^n\to\RR$ be linearly independent linear maps.
Show that for every $v\in\RR^n$ there are $v_1,v_2\in\RR^n$ such that
$$
v=v_1+v_2,\qquad f(v)=f(v_1),\qquad g(v)=g(v_2).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The restriction of $g$ to $\ker f$ is not the zero functional.


::: pf-proof

Suppose instead that
$$
g(w)=0
$$
for every
$$
w\in\ker f.
$$
Since $f$ and $g$ are linearly independent, in particular
$$
f\ne0.
$$
Choose
$$
u\in\RR^n
$$
with
$$
f(u)\ne0.
$$

For arbitrary
$$
x\in\RR^n,
$$
define
$$
w
=
x-\frac{f(x)}{f(u)}u.
$$
Then
$$
f(w)
=
f(x)-\frac{f(x)}{f(u)}f(u)
=0,
$$
so
$$
w\in\ker f.
$$
By the supposition,
$$
g(w)=0.
$$
Therefore
$$
g(x)
=
\frac{g(u)}{f(u)}f(x)
$$
for every $x$.
Thus
$$
g
=
\frac{g(u)}{f(u)}\,f,
$$
contradicting linear independence.

:::

:::

::: {.pf-step #s1-2}

Choose
$$
w\in\ker f
$$
such that
$$
g(w)\ne0.
$$


::: pf-proof

Such a vector exists by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Given
$$
v\in\RR^n,
$$
define
$$
v_2
=
\frac{g(v)}{g(w)}\,w
$$
and
$$
v_1=v-v_2.
$$


::: pf-proof

The denominator is nonzero by step [](#s1-2){.pf-ref}, so the definitions make sense.

:::

:::

::: {.pf-step #s1-4}

One has
$$
g(v_2)=g(v).
$$


::: pf-proof

By linearity,
$$
g(v_2)
=
\frac{g(v)}{g(w)}g(w)
=
g(v).
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
f(v_1)=f(v).
$$


::: pf-proof

Since
$$
w\in\ker f,
$$
step [](#s1-3){.pf-ref} gives
$$
f(v_2)
=
\frac{g(v)}{g(w)}f(w)
=0.
$$
Hence
$$
f(v_1)
=
f(v-v_2)
=
f(v)-f(v_2)
=
f(v).
$$

:::

:::

::: {.pf-step #s1-6}

The vectors $v_1,v_2$ satisfy all three required identities.


::: pf-proof

By definition in step [](#s1-3){.pf-ref},
$$
v=v_1+v_2.
$$
Step [](#s1-5){.pf-ref} gives
$$
f(v)=f(v_1),
$$
and step [](#s1-4){.pf-ref} gives
$$
g(v)=g(v_2).
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the required decomposition for arbitrary $v$.

:::

:::

:::
