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

::: {.solution}

Let
$$
\phi(z)
\coloneqq
\frac{z-1}{z+1}.
$$

::: pf

::: {.pf-step #s1-1}

The map
$$
\phi:\{z:\operatorname{Re}z>0\}\longrightarrow\DD
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

::: {.pf-step #s1-2}

Define
$$
g(w)
\coloneqq
f(\phi^{-1}(w)).
$$
Then
$$
g:\DD\to\DD
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

::: {.pf-step #s1-3}

Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\DD.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives exactly the hypotheses of Schwarz's lemma.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

Every admissible function satisfies
$$
\boxed{
|f(2)|
\le
\frac13}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
f(2)
=
g(\phi(2)).
$$
Using steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} gives
$$
|f(2)|
\le
|\phi(2)|
=
\frac13.
$$

:::

:::

::: {.pf-step #s1-6}

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
By step [](#s1-1){.pf-ref}, this function maps the right half-plane into the unit disk and satisfies
$$
f(1)=0.
$$
Step [](#s1-4){.pf-ref} gives
$$
|f(2)|
=
\frac13.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore the largest possible value is
$$
\boxed{\frac13}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives the universal upper bound and step [](#s1-6){.pf-ref} shows that it is sharp.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required extremal value.

:::

:::

:::
