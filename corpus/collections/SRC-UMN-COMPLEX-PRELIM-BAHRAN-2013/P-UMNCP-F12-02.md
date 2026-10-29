---
schema: qual/card@1
id: P-UMNCP-F12-02
kind: problem
title: Analyticity from analytic square and cube
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2012, 2 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let $f$ be a complex-valued function on the unit disk $\DD$. Suppose both
$$
g=f^2\qquad\text{and}\qquad h=f^3
$$
are analytic.
Prove that $f$ is analytic.
:::

::: {.solution}

The analytic functions
$$
g=f^2
\qquad\text{and}\qquad
h=f^3
$$
satisfy the pointwise identity
$$
\boxed{h^2=g^3}
$$
on $\DD$.

::: pf

::: {.pf-step #s1-1}

On the open set
$$
U
\coloneqq
\{z\in\DD:g(z)\ne0\},
$$
one has
$$
\boxed{f=\frac hg}.
$$


::: pf-proof

If
$$
g(z)=f(z)^2\ne0,
$$
then
$$
f(z)\ne0.
$$
Hence
$$
\frac{h(z)}{g(z)}
=
\frac{f(z)^3}{f(z)^2}
=
f(z).
$$

:::

:::

::: {.pf-step #s1-2}

Let
$$
a\in\DD
$$
be a zero of $g$. Then
$$
f(a)=0
$$
and
$$
h(a)=0.
$$


::: pf-proof

Since
$$
g(a)=f(a)^2=0,
$$
one has
$$
f(a)=0.
$$
Then
$$
h(a)=f(a)^3=0.
$$

:::

:::

::: {.pf-step #s1-3}

If $g$ is not identically zero near $a$ and
$$
\operatorname{ord}_a(g)=m,
\qquad
\operatorname{ord}_a(h)=n,
$$
then
$$
\boxed{2n=3m}.
$$


::: pf-proof

The identity
$$
h^2=g^3
$$
holds between analytic functions. The order of vanishing of a product is additive, so
$$
\operatorname{ord}_a(h^2)=2n
$$
and
$$
\operatorname{ord}_a(g^3)=3m.
$$
Equality of the functions forces equality of the orders.

:::

:::

::: {.pf-step #s1-4}

At every zero $a$ of $g$ that is not contained in a neighborhood on which $g\equiv0$,
$$
\frac hg
$$
has a removable singularity and its holomorphic extension vanishes at $a$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
n=\frac32m.
$$
Since
$$
m\ge1,
$$
one has
$$
n-m=\frac m2>0.
$$
Write locally
$$
g(z)
=(z-a)^m u(z),
$$
$$
h(z)
=(z-a)^n v(z),
$$
with
$$
u(a)\ne0,
\qquad
v(a)\ne0.
$$
Then for
$$
z\ne a,
$$
$$
\frac{h(z)}{g(z)}
=(z-a)^{n-m}
\frac{v(z)}{u(z)}.
$$
Because
$$
n-m>0,
$$
the right-hand side extends holomorphically across $a$ with value $0$.

:::

:::

::: {.pf-step #s1-5}

If $g$ vanishes identically on a nonempty open set, then $f$ vanishes there and is analytic there.


::: pf-proof

If
$$
g=f^2\equiv0
$$
on an open set, then
$$
f\equiv0
$$
there. The zero function is analytic.

:::

:::

::: {.pf-step #s1-6}

The function $f$ is analytic on all of $\DD$.


::: pf-proof

On the open set
$$
U=\{g\ne0\},
$$
step [](#s1-1){.pf-ref} writes
$$
f=h/g,
$$
so $f$ is analytic there.

At each isolated zero of $g$, step [](#s1-4){.pf-ref} gives a holomorphic extension of
$$
h/g
$$
with value $0$. By step [](#s1-2){.pf-ref}, this value equals
$$
f(a).
$$

On any open region where
$$
g\equiv0,
$$
step [](#s1-5){.pf-ref} gives
$$
f\equiv0.
$$
Thus every point of the disk has a neighborhood on which $f$ is analytic.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
