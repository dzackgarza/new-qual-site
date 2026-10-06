---
schema: qual/card@1
id: P-PRECALC1-16
kind: problem
title: Derivative of the inverse of $\int_0^x\cos^2(t^2)\,dt$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\begin{array} { r } { f ( x ) = \int _ { 0 } ^ { x } \cos ^ { 2 } ( t ^ { 2 } ) d t } \end{array}$ . Find $( f ^ { - 1 } ) ^ { \prime } ( y )$ for $y = f ( 3 )$
:::

::: {.solution}
Let
\[
f(x)
=
\int_0^x
\cos^2(t^2)\,dt.
\]

<1>1. By the fundamental theorem of calculus,
\[
\boxed{
f'(x)=\cos^2(x^2)}.
\]

::: {.proof}
The integrand is continuous, so differentiation with respect to the upper
limit gives
\[
f'(x)=\cos^2(x^2).
\]
:::

<1>2. The function \(f\) is strictly increasing.

::: {.proof}
The derivative satisfies
\[
f'(x)=\cos^2(x^2)\ge0.
\]
Moreover, on every nondegenerate interval the continuous function
\[
\cos^2(x^2)
\]
is not identically zero, because its zeros are isolated. Thus for \(a<b\),
\[
f(b)-f(a)
=
\int_a^b\cos^2(t^2)\,dt
>
0.
\]
Hence \(f\) is strictly increasing.
:::

<1>3. Therefore \(f\) has an inverse on its image.

::: {.proof}
Every strictly increasing function is injective, so it has a well-defined
inverse from its image back to its domain.
:::

<1>4. For
\[
y=f(3),
\]
one has
\[
\boxed{
f^{-1}(y)=3}.
\]

::: {.proof}
Apply \(f^{-1}\) to
\[
y=f(3).
\]
:::

<1>5. One has
\[
\boxed{
f'(3)=\cos^2(9)}.
\]

::: {.proof}
Substitute \(x=3\) into step <1>1:
\[
x^2=9.
\]
:::

<1>6. The value \(\cos 9\) is nonzero.

::: {.proof}
If \(\cos9=0\), then
\[
9=\frac{\pi}{2}+k\pi
=
\frac{(2k+1)\pi}{2}
\]
for some integer \(k\), which would imply
\[
\pi=\frac{18}{2k+1},
\]
a rational number, contradicting the irrationality of \(\pi\).
:::

<1>7. Hence the inverse-function derivative formula applies:
\[
(f^{-1})'(y)
=
\frac1{f'(f^{-1}(y))}.
\]

::: {.proof}
The denominator is nonzero at the relevant point by steps <1>4--<1>6.
:::

<1>8. Therefore
\[
(f^{-1})'(f(3))
=
\frac1{f'(3)}
=
\frac1{\cos^2(9)}.
\]

::: {.proof}
Use steps <1>4--<1>7.
:::

<1>9. Thus
\[
\boxed{
(f^{-1})'(y)=\sec^2(9)
\qquad\text{for }y=f(3)}.
\]

::: {.proof}
By definition,
\[
\sec^2(9)=\frac1{\cos^2(9)}.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the requested derivative.
:::
:::
