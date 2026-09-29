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

::: pf

::: {.pf-step #identity-equivalent-form}
The identity
$$
a^2+b^2+c^2=ab+bc+ca
$$
is equivalent to
$$
u^2+v^2=uv.
$$

::: pf-proof
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

:::

::: {.pf-step #ratio-values}
If the algebraic identity holds, then
$$
\frac vu
=
e^{i\pi/3}
\qquad\text{or}\qquad
\frac vu
=
e^{-i\pi/3}.
$$

::: pf-proof
Since $a,b,c$ are distinct, in particular
$$
u=b-a\neq0.
$$
Divide the equation from step [](#identity-equivalent-form){.pf-ref} by $u^2$ and put
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

:::

::: {.pf-step #identity-implies-equilateral}
If the algebraic identity holds, then $a,b,c$ are the vertices
of an equilateral triangle.

::: pf-proof
By step [](#ratio-values){.pf-ref},
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

:::

::: {.pf-step #equilateral-implies-ratio}
Conversely, if $a,b,c$ are the vertices of an equilateral
triangle, then
$$
\frac vu=e^{i\pi/3}
\qquad\text{or}\qquad
\frac vu=e^{-i\pi/3}.
$$

::: pf-proof
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

:::

::: {.pf-step #equilateral-implies-identity}
If $a,b,c$ form an equilateral triangle, then
$$
a^2+b^2+c^2=ab+bc+ca.
$$

::: pf-proof
By step [](#equilateral-implies-ratio){.pf-ref}, the number
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
Step [](#identity-equivalent-form){.pf-ref} converts this back to the required identity.
:::

:::

::: {.pf-step #equivalence-conclusion}
Therefore the identity $a^2+b^2+c^2=ab+bc+ca$ is necessary and
sufficient for three distinct complex numbers to be the vertices of
an equilateral triangle.

::: pf-proof
Step [](#identity-implies-equilateral){.pf-ref} proves sufficiency and step [](#equilateral-implies-identity){.pf-ref} proves necessity.
:::

:::

::: pf-qed
Step [](#equivalence-conclusion){.pf-ref} is the asserted equivalence.
:::

:::
:::
