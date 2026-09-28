---
schema: qual/card@1
id: P-BERK85S-03
kind: problem
title: Algebraic criterion for three complex points to form an equilateral triangle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-corrected
  by: chatgpt
  date: 2026-09-22
  note: >-
    The source omits a distinctness hypothesis. As written,
    a=b=c satisfies the displayed identity but does not give the
    vertices of a nondegenerate triangle. Added the necessary
    distinctness hypothesis.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Translated one vertex to zero, reduced the identity to
    u^2+v^2=uv, and solved the resulting quadratic for v/u. The two
    roots are the rotations through plus or minus pi/3, which are
    exactly the two orientations of an equilateral triangle.
---

::: {.problem}
Show that three distinct complex numbers $a,b,c$ are the vertices of an equilateral triangle if and only if
\[
a^2+b^2+c^2=ab+bc+ca.
\]
:::

::: {.solution}
Set
$$
u=b-a,
\qquad
v=c-a.
$$

<1>1. The identity
$$
a^2+b^2+c^2=ab+bc+ca
$$
is equivalent to
$$
u^2+v^2=uv.
$$

::: {.proof}
Substitute
$$
b=a+u,
\qquad
c=a+v.
$$
Then the left-hand side minus the right-hand side becomes
$$
u^2+v^2-uv.
$$
Thus the two displayed equations are equivalent.
:::

<1>2. If the algebraic identity holds, then
$$
\frac vu
=
e^{i\pi/3}
\qquad\text{or}\qquad
\frac vu
=
e^{-i\pi/3}.
$$

::: {.proof}
Since $a,b,c$ are distinct, in particular
$$
u=b-a\neq0.
$$
Divide the equation from step <1>1 by $u^2$ and put
$$
t=\frac vu.
$$
Then
$$
t^2-t+1=0.
$$
Hence
$$
t
=
\frac{1\pm i\sqrt3}{2}
=
e^{\pm i\pi/3}.
$$
:::

<1>3. If the algebraic identity holds, then $a,b,c$ are the vertices
of an equilateral triangle.

::: {.proof}
By step <1>2,
$$
\abs v=\abs u.
$$
Moreover, for either choice
$$
t=e^{\pm i\pi/3},
$$
one has
$$
\abs{t-1}=1.
$$
Therefore
$$
\abs{v-u}
=
\abs u\abs{t-1}
=
\abs u.
$$
Since
$$
\abs u=\abs{b-a},
\qquad
\abs v=\abs{c-a},
\qquad
\abs{v-u}=\abs{c-b},
$$
all three side lengths are equal.
:::

<1>4. Conversely, if $a,b,c$ are the vertices of an equilateral
triangle, then
$$
\frac vu=e^{i\pi/3}
\qquad\text{or}\qquad
\frac vu=e^{-i\pi/3}.
$$

::: {.proof}
Because the triangle is equilateral,
$$
\abs u=\abs v=\abs{v-u}>0.
$$
Put $t=v/u$. Then
$$
\abs t=1
\qquad\text{and}\qquad
\abs{t-1}=1.
$$
Write $t=e^{i\theta}$. Squaring the second equality gives
$$
1
=
\abs{e^{i\theta}-1}^2
=
2-2\cos\theta,
$$
so
$$
\cos\theta=\frac12.
$$
Thus
$$
t=e^{\pm i\pi/3}.
$$
:::

<1>5. If $a,b,c$ form an equilateral triangle, then
$$
a^2+b^2+c^2=ab+bc+ca.
$$

::: {.proof}
By step <1>4, the number
$$
t=\frac vu
$$
satisfies
$$
t^2-t+1=0.
$$
Multiplying by $u^2$ yields
$$
u^2+v^2=uv.
$$
Step <1>1 converts this back to the required identity.
:::

<1>6. Therefore the identity $a^2+b^2+c^2=ab+bc+ca$ is necessary and
sufficient for three distinct complex numbers to be the vertices of
an equilateral triangle.

::: {.proof}
Step <1>3 proves sufficiency and step <1>5 proves necessity.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the asserted equivalence.
:::
:::
