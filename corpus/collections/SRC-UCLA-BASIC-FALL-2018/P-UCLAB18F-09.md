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
Let $f,g:\mathbb R^n\to\mathbb R$ be linearly independent linear maps.
Show that for every $v\in\mathbb R^n$ there are $v_1,v_2\in\mathbb R^n$ such that
\[
v=v_1+v_2,\qquad f(v)=f(v_1),\qquad g(v)=g(v_2).
\]
:::

::: {.solution}
<1>1. The restriction of $g$ to $\ker f$ is not the zero functional.

::: {.proof}
Suppose instead that
\[
g(w)=0
\]
for every
\[
w\in\ker f.
\]
Since $f$ and $g$ are linearly independent, in particular
\[
f\ne0.
\]
Choose
\[
u\in\mathbb R^n
\]
with
\[
f(u)\ne0.
\]

For arbitrary
\[
x\in\mathbb R^n,
\]
define
\[
w
=
x-\frac{f(x)}{f(u)}u.
\]
Then
\[
f(w)
=
f(x)-\frac{f(x)}{f(u)}f(u)
=0,
\]
so
\[
w\in\ker f.
\]
By the supposition,
\[
g(w)=0.
\]
Therefore
\[
g(x)
=
\frac{g(u)}{f(u)}f(x)
\]
for every $x$.
Thus
\[
g
=
\frac{g(u)}{f(u)}\,f,
\]
contradicting linear independence.
:::

<1>2. Choose
\[
w\in\ker f
\]
such that
\[
g(w)\ne0.
\]

::: {.proof}
Such a vector exists by step <1>1.
:::

<1>3. Given
\[
v\in\mathbb R^n,
\]
define
\[
v_2
=
\frac{g(v)}{g(w)}\,w
\]
and
\[
v_1=v-v_2.
\]

::: {.proof}
The denominator is nonzero by step <1>2, so the definitions make sense.
:::

<1>4. One has
\[
g(v_2)=g(v).
\]

::: {.proof}
By linearity,
\[
g(v_2)
=
\frac{g(v)}{g(w)}g(w)
=
g(v).
\]
:::

<1>5. One has
\[
f(v_1)=f(v).
\]

::: {.proof}
Since
\[
w\in\ker f,
\]
step <1>3 gives
\[
f(v_2)
=
\frac{g(v)}{g(w)}f(w)
=0.
\]
Hence
\[
f(v_1)
=
f(v-v_2)
=
f(v)-f(v_2)
=
f(v).
\]
:::

<1>6. The vectors $v_1,v_2$ satisfy all three required identities.

::: {.proof}
By definition in step <1>3,
\[
v=v_1+v_2.
\]
Step <1>5 gives
\[
f(v)=f(v_1),
\]
and step <1>4 gives
\[
g(v)=g(v_2).
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the required decomposition for arbitrary $v$.
:::
:::
