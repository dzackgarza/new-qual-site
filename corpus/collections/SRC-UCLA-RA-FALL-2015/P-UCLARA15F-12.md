---
schema: qual/card@1
id: P-UCLARA15F-12
kind: problem
title: Harmonic function between the tangent circles $|z|=2$ and $|z-1|=1$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 12 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Find a function $u(x,y)$ harmonic in the region between the circles $|z| = 2$ and $|z - 1| = 1$ which equals 1 on the outer circle and 0 on the inner circle (except at the point where the circles are tangent to each other).
:::

::: {.solution}
Let
\[
\Omega
=
\{z:|z|<2,\ |z-1|>1\}
\]
be the region between the two circles, excluding the tangency point \(z=2\).

Consider the Möbius transformation
\[
\boxed{
w=\frac1{z-2}}.
\]

<1>1. The map \(z\mapsto1/(z-2)\) is conformal on \(\Omega\).

::: {.proof}
The only pole is at
\[
z=2,
\]
which lies on the boundary of the region and is excluded from \(\Omega\).
:::

Write
\[
w=\xi+i\eta.
\]

## Image of the outer circle

<1>2. If
\[
|z|=2
\]
and \(z\ne2\), then
\[
z=2+\frac1w.
\]

::: {.proof}
This is the inverse relation to the definition of \(w\).
:::

<1>3. The equation
\[
|z|=2
\]
becomes
\[
\left|
2+\frac1w
\right|
=2.
\]

::: {.proof}
Substitute step <1>2.
:::

<1>4. Multiplying by \(|w|\),
\[
\boxed{
|2w+1|=2|w|}.
\]

::: {.proof}
Since \(w\ne0\),
\[
\left|
2+\frac1w
\right|
=
\frac{|2w+1|}{|w|}.
\]
:::

<1>5. Squaring gives
\[
4|w|^2+4\operatorname{Re}w+1
=
4|w|^2.
\]

::: {.proof}
\[
|2w+1|^2
=
(2w+1)(2\overline w+1)
=
4|w|^2+2w+2\overline w+1.
\]
Since
\[
2w+2\overline w
=
4\operatorname{Re}w,
\]
the formula follows.
:::

<1>6. Hence the outer circle maps to the vertical line
\[
\boxed{
\operatorname{Re}w=-\frac14}.
\]

::: {.proof}
Cancel \(4|w|^2\) from step <1>5:
\[
4\operatorname{Re}w+1=0.
\]
:::

## Image of the inner circle

<1>7. If
\[
|z-1|=1,
\]
then
\[
\left|
1+\frac1w
\right|
=1.
\]

::: {.proof}
Using
\[
z=2+\frac1w,
\]
one has
\[
z-1=1+\frac1w.
\]
:::

<1>8. Multiplying by \(|w|\),
\[
\boxed{
|w+1|=|w|}.
\]

::: {.proof}
\[
\left|
1+\frac1w
\right|
=
\frac{|w+1|}{|w|}.
\]
:::

<1>9. Squaring gives
\[
|w|^2+2\operatorname{Re}w+1
=
|w|^2.
\]

::: {.proof}
\[
|w+1|^2
=
|w|^2+w+\overline w+1
=
|w|^2+2\operatorname{Re}w+1.
\]
:::

<1>10. Hence the inner circle maps to the vertical line
\[
\boxed{
\operatorname{Re}w=-\frac12}.
\]

::: {.proof}
Cancel \(|w|^2\) in step <1>9.
:::

<1>11. The region \(\Omega\) maps to the strip
\[
\boxed{
-\frac12
<
\operatorname{Re}w
<
-\frac14}.
\]

::: {.proof}
It suffices to test one point of \(\Omega\). For example,
\[
z=-1
\]
satisfies
\[
|-1|<2
\]
and
\[
|-2|>1,
\]
so \(z=-1\in\Omega\). Its image is
\[
w=\frac1{-3}=-\frac13,
\]
which lies between \(-1/2\) and \(-1/4\). Since the Möbius map is continuous and conformal, it sends the connected region between the two tangent circles to the connected strip between the two image lines.
:::

## Harmonic function on the strip

<1>12. Define
\[
\boxed{
U(w)=4\operatorname{Re}w+2}.
\]

::: {.proof}
This is an affine function of the real part of \(w\).
:::

<1>13. The function \(U\) is harmonic.

::: {.proof}
If \(w=\xi+i\eta\), then
\[
U(\xi,\eta)=4\xi+2.
\]
Hence
\[
U_{\xi\xi}=0,
\qquad
U_{\eta\eta}=0.
\]
:::

<1>14. On the line
\[
\operatorname{Re}w=-\frac14,
\]
one has
\[
\boxed{U=1}.
\]

::: {.proof}
\[
4\left(-\frac14\right)+2
=
-1+2
=
1.
\]
:::

<1>15. On the line
\[
\operatorname{Re}w=-\frac12,
\]
one has
\[
\boxed{U=0}.
\]

::: {.proof}
\[
4\left(-\frac12\right)+2
=
-2+2
=
0.
\]
:::

Pull this harmonic function back to \(\Omega\).

<1>16. Define
\[
\boxed{
u(z)
=
4\operatorname{Re}
\left(
\frac1{z-2}
\right)
+
2}.
\]

::: {.proof}
This is
\[
u=U\circ w.
\]
:::

<1>17. The function \(u\) is harmonic in \(\Omega\).

::: {.proof}
The function
\[
\frac1{z-2}
\]
is holomorphic on \(\Omega\), so its real part is harmonic. Affine combinations of harmonic functions are harmonic.
:::

<1>18. On the outer circle \(|z|=2\), away from \(z=2\),
\[
\boxed{u=1}.
\]

::: {.proof}
By step <1>6,
\[
\operatorname{Re}\frac1{z-2}
=
-\frac14.
\]
Apply step <1>14.
:::

<1>19. On the inner circle \(|z-1|=1\), away from \(z=2\),
\[
\boxed{u=0}.
\]

::: {.proof}
By step <1>10,
\[
\operatorname{Re}\frac1{z-2}
=
-\frac12.
\]
Apply step <1>15.
:::

<1>20. In Cartesian coordinates,
\[
\boxed{
u(x,y)
=
2+
\frac{
4(x-2)
}{
(x-2)^2+y^2
}}.
\]

::: {.proof}
Since
\[
\frac1{z-2}
=
\frac{x-2-iy}{(x-2)^2+y^2},
\]
its real part is
\[
\frac{x-2}{(x-2)^2+y^2}.
\]
Substitute into step <1>16.
:::

<1>21. Therefore the required harmonic function is
\[
\boxed{
u(x,y)
=
2+
\frac{
4(x-2)
}{
(x-2)^2+y^2
}}.
\]

::: {.proof}
Steps <1>17--<1>20 verify harmonicity and both boundary values.
:::

<1>22. Q.E.D.

::: {.proof}
Step <1>21 is the requested function.
:::
:::
