---
schema: qual/card@1
id: P-UMNCP-F12-06
kind: problem
title: Sharp Schwarz bound in the upper half-plane
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
  note: Checked against Fall 2012, 6 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be analytic on the upper half-plane \(\{z:\operatorname{Im}z>0\}\). Suppose \(|f(z)|<1\) throughout the domain and \(f(i)=0\). Find the largest possible value of \(|f(2i)|\).
:::

::: {.solution}

Let
$$
\phi(z)
\coloneqq
\frac{z-i}{z+i}.
$$

::: pf

::: {.pf-step #s1-1}

The map
$$
\phi:\mathbb H\longrightarrow\DD
$$
is a biholomorphism satisfying
$$
\phi(i)=0.
$$


::: pf-proof

The Möbius transformation
$$
\phi(z)=\frac{z-i}{z+i}
$$
is the standard Cayley map from the upper half-plane
$$
\mathbb H
=
\{z:\operatorname{Im}z>0\}
$$
onto the unit disk.

Indeed, for
$$
z=x+iy,
\qquad
y>0,
$$
one has
$$
|z+i|^2-|z-i|^2
=
4y
>0,
$$
so
$$
|\phi(z)|<1.
$$
Its inverse is
$$
\phi^{-1}(w)
=
i\frac{1+w}{1-w},
$$
which maps $\DD$ to $\mathbb H$. Finally,
$$
\phi(i)=0.
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

The function
$$
\phi^{-1}
$$
maps $\DD$ holomorphically into the domain of $f$, and
$$
|f|<1
$$
there. Thus $g$ maps $\DD$ into itself. Since
$$
\phi^{-1}(0)=i
$$
and
$$
f(i)=0,
$$
we have
$$
g(0)=0.
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
\phi(2i)=\frac13.
$$


::: pf-proof

Compute
$$
\phi(2i)
=
\frac{2i-i}{2i+i}
=
\frac{i}{3i}
=
\frac13.
$$

:::

:::

::: {.pf-step #s1-5}

Every admissible function $f$ satisfies
$$
\boxed{
|f(2i)|
\le
\frac13}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
f(2i)
=
g(\phi(2i)).
$$
Using steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
|f(2i)|
\le
|\phi(2i)|
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
By step [](#s1-1){.pf-ref}, this function maps the upper half-plane into the unit disk and satisfies
$$
f(i)=0.
$$
By step [](#s1-4){.pf-ref},
$$
|f(2i)|
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

Step [](#s1-5){.pf-ref} gives the universal upper bound and step [](#s1-6){.pf-ref} shows it is sharp.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required extremal value.

:::

:::

:::
