---
schema: qual/card@1
id: P-UMNCP-F11-04
kind: problem
title: Sharp Schwarz bound in the right half-plane
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
  note: Checked against Fall 2011, 4 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be holomorphic on the right half-plane \(\{z:\operatorname{Re}z>0\}\). Suppose \(|f(z)|<1\) throughout the domain and \(f(1)=0\). Find the largest possible value of \(|f(2)|\).
:::

Let
$$
\phi(z)
\coloneqq
\frac{z-1}{z+1}.
$$

::: pf

::: pf-step

The map
$$
\phi:\{z:\operatorname{Re}z>0\}\longrightarrow\mathbb D
$$
is a biholomorphism and
$$
\phi(1)=0.
$$


::: pf-proof

If
$$
z=x+iy
$$
with
$$
x>0,
$$
then
$$
|z+1|^2-|z-1|^2
=
4x
>0.
$$
Thus
$$
|z-1|<|z+1|,
$$
so
$$
|\phi(z)|<1.
$$

The inverse Möbius transformation is
$$
\phi^{-1}(w)
=
\frac{1+w}{1-w},
$$
and for
$$
|w|<1
$$
one has
$$
\operatorname{Re}\phi^{-1}(w)
=
\frac{1-|w|^2}{|1-w|^2}
>0.
$$
Hence
$$
\phi
$$
is a biholomorphism onto the disk. Finally,
$$
\phi(1)=0.
$$

:::

:::

::: pf-step

Define
$$
g(w)
\coloneqq
f(\phi^{-1}(w)).
$$
Then
$$
g:\mathbb D\to\mathbb D
$$
is holomorphic and
$$
g(0)=0.
$$


::: pf-proof

The inverse map
$$
\phi^{-1}
$$
sends the disk holomorphically into the right half-plane. Since
$$
|f|<1,
$$
the composition maps the disk into itself. Also
$$
\phi^{-1}(0)=1,
$$
so
$$
g(0)
=
f(1)
=0.
$$

:::

:::

::: pf-step

Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\mathbb D.
$$


::: pf-proof

Step <1>2 gives exactly the hypotheses of Schwarz's lemma.

:::

:::

::: pf-step

One has
$$
\phi(2)=\frac13.
$$


::: pf-proof

Compute
$$
\phi(2)
=
\frac{2-1}{2+1}
=
\frac13.
$$

:::

:::

::: pf-step

Every admissible function satisfies
$$
\boxed{
|f(2)|
\le
\frac13}.
$$


::: pf-proof

By step <1>2,
$$
f(2)
=
g(\phi(2)).
$$
Using steps <1>3--<1>4 gives
$$
|f(2)|
\le
|\phi(2)|
=
\frac13.
$$

:::

:::

::: pf-step

The bound
$$
\frac13
$$
is attained.


::: pf-proof

Take
$$
f=\phi.
$$
By step <1>1, this function maps the right half-plane into the unit disk and satisfies
$$
f(1)=0.
$$
Step <1>4 gives
$$
|f(2)|
=
\frac13.
$$

:::

:::

::: pf-step

Therefore the largest possible value is
$$
\boxed{\frac13}.
$$


::: pf-proof

Step <1>5 gives the universal upper bound and step <1>6 shows that it is sharp.

:::

:::

::: pf-qed

Step <1>7 is the required extremal value.

:::

:::
