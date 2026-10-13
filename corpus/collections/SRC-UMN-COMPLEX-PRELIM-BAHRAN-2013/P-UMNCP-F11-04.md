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

<1>1. The map
$$
\phi:\{z:\operatorname{Re}z>0\}\longrightarrow\mathbb D
$$
is a biholomorphism and
$$
\phi(1)=0.
$$

::: {.proof}
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

<1>2. Define
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

::: {.proof}
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

<1>3. Schwarz's lemma gives
$$
|g(w)|\le|w|
$$
for every
$$
w\in\mathbb D.
$$

::: {.proof}
Step <1>2 gives exactly the hypotheses of Schwarz's lemma.
:::

<1>4. One has
$$
\phi(2)=\frac13.
$$

::: {.proof}
Compute
$$
\phi(2)
=
\frac{2-1}{2+1}
=
\frac13.
$$
:::

<1>5. Every admissible function satisfies
$$
\boxed{
|f(2)|
\le
\frac13}.
$$

::: {.proof}
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

<1>6. The bound
$$
\frac13
$$
is attained.

::: {.proof}
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

<1>7. Therefore the largest possible value is
$$
\boxed{\frac13}.
$$

::: {.proof}
Step <1>5 gives the universal upper bound and step <1>6 shows that it is sharp.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required extremal value.
:::
:::
