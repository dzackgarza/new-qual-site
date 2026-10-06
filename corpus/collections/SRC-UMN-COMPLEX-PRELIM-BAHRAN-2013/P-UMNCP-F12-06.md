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

<1>1. The map
$$
\phi:\mathbb H\longrightarrow\mathbb D
$$
is a biholomorphism satisfying
$$
\phi(i)=0.
$$

::: {.proof}
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
which maps $\mathbb D$ to $\mathbb H$. Finally,
$$
\phi(i)=0.
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
The function
$$
\phi^{-1}
$$
maps $\mathbb D$ holomorphically into the domain of $f$, and
$$
|f|<1
$$
there. Thus $g$ maps $\mathbb D$ into itself. Since
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
\phi(2i)=\frac13.
$$

::: {.proof}
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

<1>5. Every admissible function $f$ satisfies
$$
\boxed{
|f(2i)|
\le
\frac13}.
$$

::: {.proof}
By step <1>2,
$$
f(2i)
=
g(\phi(2i)).
$$
Using steps <1>3--<1>4,
$$
|f(2i)|
\le
|\phi(2i)|
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
By step <1>1, this function maps the upper half-plane into the unit disk and satisfies
$$
f(i)=0.
$$
By step <1>4,
$$
|f(2i)|
=
\frac13.
$$
:::

<1>7. Therefore the largest possible value is
$$
\boxed{\frac13}.
$$

::: {.proof}
Step <1>5 gives the universal upper bound and step <1>6 shows it is sharp.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required extremal value.
:::
:::
