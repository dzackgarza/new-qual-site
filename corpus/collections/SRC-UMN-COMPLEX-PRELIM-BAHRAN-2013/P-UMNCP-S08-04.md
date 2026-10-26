---
schema: qual/card@1
id: P-UMNCP-S08-04
kind: problem
title: A transcendental equation has one root in the right half-plane
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
  note: Checked against Spring 2008, 4 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(\lambda>1\). Show that
\[
z+e^{-z}=\lambda
\]
has exactly one solution with positive real part.
:::

Set
$$
f(z)
\coloneqq
z+e^{-z}-\lambda
$$
and, for
$$
R>\lambda+1,
$$
let
$$
D_R
\coloneqq
\{z\in\CC:\operatorname{Re}z>0,\ |z|<R\}.
$$

::: pf

::: pf-step

On the semicircular part of
$$
\partial D_R,
$$
one has
$$
|e^{-z}|<|z-\lambda|.
$$


::: pf-proof

If
$$
|z|=R
$$
and
$$
\operatorname{Re}z\ge0,
$$
then
$$
|e^{-z}|
=
e^{-\operatorname{Re}z}
\le
1.
$$
Also, by the reverse triangle inequality,
$$
|z-\lambda|
\ge
R-\lambda
>
1.
$$
Thus
$$
|e^{-z}|<|z-\lambda|.
$$

:::

:::

::: pf-step

On the imaginary-axis part of
$$
\partial D_R,
$$
one also has
$$
|e^{-z}|<|z-\lambda|.
$$


::: pf-proof

Write
$$
z=iy
$$
with
$$
|y|\le R.
$$
Then
$$
|e^{-z}|
=
|e^{-iy}|
=1.
$$
On the other hand,
$$
|iy-\lambda|
=
\sqrt{y^2+\lambda^2}
\ge
\lambda
>
1.
$$
Hence the same strict inequality holds.

:::

:::

::: pf-step

The functions
$$
f(z)
=(z-\lambda)+e^{-z}
$$
and
$$
z-\lambda
$$
have the same number of zeros in $D_R$, counted with multiplicity.


::: pf-proof

Steps <1>1--<1>2 give
$$
|e^{-z}|<|z-\lambda|
$$
on every point of the positively oriented boundary
$$
\partial D_R.
$$
Both functions are entire. Rouché's theorem therefore applies.

:::

:::

::: pf-step

The function $f$ has exactly one zero in $D_R$.


::: pf-proof

The comparison function
$$
z-\lambda
$$
has exactly one zero, namely
$$
z=\lambda.
$$
Since
$$
\lambda>0
$$
and
$$
R>\lambda+1,
$$
this zero lies in $D_R$. Step <1>3 therefore gives exactly one zero of $f$ in $D_R$.

:::

:::

::: pf-step

The equation
$$
z+e^{-z}=\lambda
$$
has exactly one solution with positive real part.


::: pf-proof

The right half-plane is the union of the nested domains
$$
D_R
$$
as
$$
R\to\infty.
$$
By step <1>4, every
$$
R>\lambda+1
$$
contains exactly one zero of $f$.

Choose one such $R_0$ and let
$$
z_0
$$
be the unique zero in $D_{R_0}$. For every
$$
R>R_0,
$$
the same point $z_0$ lies in $D_R$, and step <1>4 says $D_R$ contains no other zero. Since every point of the open right half-plane lies in some sufficiently large $D_R$, there is no second zero with positive real part.

:::

:::

::: pf-qed

Step <1>5 is the required existence-and-uniqueness statement.

:::

:::
