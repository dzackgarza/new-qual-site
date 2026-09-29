---
schema: qual/card@1
id: P-AZOFF-C03
kind: problem
title: Möbius map of the upper half-plane onto the disk and the image of a quadrant
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used T(z)=(z-i)/(z+i). The standard modulus calculation gives a
    biholomorphism from the upper half-plane to the disk. For the open
    first-quadrant sector of the disk, explicit formulas for Re T and Im T
    show that its image is exactly the open third-quadrant sector of the disk;
    the inverse formulas prove the reverse inclusion. The source compilation
    contains no worked solution.
---

::: {.problem}
Find a linear fractional transformation $T$ which maps the open upper half plane onto the open unit disk.
Then explicitly describe the image of the first quadrant of the unit disk under $T$.
:::

::: {.solution}
Let
$$
\mathcal H=\{z\in\CC:\operatorname{Im}z>0\},
\qquad
\DD=\{w\in\CC:\abs w<1\},
$$
and define
$$
T(z)=\frac{z-i}{z+i}.
$$

::: pf

::: {.pf-step #s1}

The map
$$
T:\mathcal H\longrightarrow\DD
$$
is a conformal bijection, with inverse
$$
T^{-1}(w)=i\frac{1+w}{1-w}.
$$

::: pf-proof

Write
$$
z=x+iy,
\qquad
y>0.
$$
Then
$$
\abs{z+i}^2-\abs{z-i}^2
=
\bigl(x^2+(y+1)^2\bigr)
-
\bigl(x^2+(y-1)^2\bigr)
=
4y
>
0.
$$
Hence
$$
\abs{T(z)}<1.
$$

Solving
$$
w=\frac{z-i}{z+i}
$$
for $z$ gives the displayed inverse. The same calculation in reverse shows
that this inverse maps $\DD$ into $\mathcal H$, so $T$ is bijective. Finally,
$$
T'(z)=\frac{2i}{(z+i)^2}\neq0
$$
on $\mathcal H$. Thus $T$ is conformal.

:::

:::

::: {.pf-step #s2}

Let
$$
Q=\{z\in\CC:\abs z<1,\ \operatorname{Re}z>0,\ \operatorname{Im}z>0\},
$$
the open first-quadrant sector of the unit disk. Then
$$
T(Q)\subseteq
\{w\in\CC:\abs w<1,\ \operatorname{Re}w<0,\ \operatorname{Im}w<0\}.
$$

::: pf-proof

For
$$
z=x+iy\in Q,
$$
put
$$
\Delta=x^2+(y+1)^2>0.
$$
Multiplying numerator and denominator of $T(z)$ by
$$
x-i(y+1)
$$
gives
$$
\operatorname{Re}T(z)
=
\frac{x^2+y^2-1}{\Delta}
<
0
$$
because $\abs z<1$, and
$$
\operatorname{Im}T(z)
=
\frac{-2x}{\Delta}
<
0
$$
because $x>0$. Since $y>0$, step [](#s1){.pf-ref} also gives $\abs{T(z)}<1$.

:::

:::

::: {.pf-step #s3}

Conversely, if
$$
w\in\DD,
\qquad
\operatorname{Re}w<0,
\qquad
\operatorname{Im}w<0,
$$
then
$$
T^{-1}(w)\in Q.
$$

::: pf-proof

Write
$$
w=u+iv
$$
and set
$$
z=T^{-1}(w)=i\frac{1+w}{1-w}.
$$
Put
$$
\Gamma=(1-u)^2+v^2>0.
$$
Direct calculation gives
$$
\operatorname{Re}z
=
\frac{-2v}{\Gamma}
>
0
$$
because $v<0$, and
$$
\operatorname{Im}z
=
\frac{1-\abs w^2}{\Gamma}
>
0
$$
because $\abs w<1$.

Moreover,
$$
\abs z^2
=
\frac{\abs{1+w}^2}{\abs{1-w}^2}.
$$
Since
$$
\abs{1-w}^2-\abs{1+w}^2=-4u>0,
$$
we have $\abs z<1$. Hence $z\in Q$.

:::

:::

::: {.pf-step #s4}

Therefore the image of the open first-quadrant sector of the unit disk
is
$$
\boxed{
T(Q)
=
\{w\in\CC:\abs w<1,\ \operatorname{Re}w<0,\ \operatorname{Im}w<0\},
}
$$
the open third-quadrant sector of the unit disk.

::: pf-proof

Step [](#s2){.pf-ref} gives one inclusion, and step [](#s3){.pf-ref} gives the reverse inclusion.

:::

:::

::: {.pf-step #s5}

The three boundary pieces are sent as follows:
$$
\begin{aligned}
[0,1]&\longmapsto
\text{the unit-circle arc from }-1\text{ to }-i,\\
[0,i]&\longmapsto[-1,0],\\
\{z:\abs z=1,\ \operatorname{Re}z,\operatorname{Im}z\geq0\}
&\longmapsto[-i,0].
\end{aligned}
$$

::: pf-proof

The endpoint values are
$$
T(0)=-1,
\qquad
T(1)=-i,
\qquad
T(i)=0.
$$
The real axis maps to the unit circle because it is the boundary of
$\mathcal H$; for $z=iy$ with $0\leq y\leq1$,
$$
T(iy)=\frac{y-1}{y+1}\in[-1,0];
$$
and the circle $\abs z=1$, which passes through the pole $-i$, maps under a
Möbius transformation to a line. Since the relevant arc has endpoint images
$-i$ and $0$, it maps to the segment $[-i,0]$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} supplies the required linear fractional transformation, and step
[](#s4){.pf-ref} explicitly describes the requested image; step [](#s5){.pf-ref} records its boundary
correspondence.

:::

:::

:::
