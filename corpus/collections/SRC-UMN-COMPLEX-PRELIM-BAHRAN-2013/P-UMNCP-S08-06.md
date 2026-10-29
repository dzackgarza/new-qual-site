---
schema: qual/card@1
id: P-UMNCP-S08-06
kind: problem
title: Conformally map a quarter-disk to the first quadrant
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
  note: Checked against Spring 2008, 6 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Find an explicit conformal equivalence from
$$
R_1=\{z\in\CC:\operatorname{Re}z>0,\ \operatorname{Im}z>0,\ |z|<1\}
$$
to
$$
R_2=\{z\in\CC:\operatorname{Re}z>0,\ \operatorname{Im}z>0\}.
$$
:::

::: {.solution}

Define
$$
\boxed{
F(z)
=
\frac{1+z^2}{1-z^2}}.
$$

::: pf

::: {.pf-step #s1-1}

The map
$$
S(z)=z^2
$$
is a biholomorphism from $R_1$ onto the upper half-disk
$$
D_+
\coloneqq
\{w\in\CC:|w|<1,\ \operatorname{Im}w>0\}.
$$


::: pf-proof

If
$$
z=re^{i\theta}
$$
with
$$
0<r<1,
\qquad
0<\theta<\frac\pi2,
$$
then
$$
z^2=r^2e^{2i\theta},
$$
so
$$
|z^2|<1
$$
and
$$
0<\arg(z^2)<\pi.
$$
Thus $S(R_1)\subseteq D_+$.

Conversely, if
$$
w=\rho e^{i\varphi}\in D_+,
$$
then
$$
0<\rho<1,
\qquad
0<\varphi<\pi.
$$
The unique square root
$$
z=\sqrt\rho,e^{i\varphi/2}
$$
lies in $R_1$ and satisfies $z^2=w$. Hence $S$ is bijective.

Finally,
$$
S'(z)=2z\ne0
$$
on $R_1$, so $S$ is conformal.

:::

:::

::: {.pf-step #s1-2}

The Möbius map
$$
T(w)
=
\frac{1+w}{1-w}
$$
maps $D_+$ into $R_2$.


::: pf-proof

Let
$$
w=u+iv\in D_+.
$$
Then
$$
|w|<1
$$
and
$$
v>0.
$$
Multiplying numerator and denominator by
$$
1-\overline w
$$
gives
$$
T(w)
=
\frac{(1+w)(1-\overline w)}
{|1-w|^2}.
$$
Its real part is
$$
\operatorname{Re}T(w)
=
\frac{1-|w|^2}
{|1-w|^2}
>0,
$$
and its imaginary part is
$$
\operatorname{Im}T(w)
=
\frac{2\operatorname{Im}w}
{|1-w|^2}
>0.
$$
Thus
$$
T(w)\in R_2.
$$

:::

:::

::: {.pf-step #s1-3}

The map $T:D_+\to R_2$ is bijective.


::: pf-proof

The inverse Möbius transformation is
$$
T^{-1}(\zeta)
=
\frac{\zeta-1}{\zeta+1}.
$$
Let
$$
\zeta=x+iy\in R_2,
$$
so $x>0$ and $y>0$. Set
$$
w=T^{-1}(\zeta).
$$
Then
$$
|w|^2
=
\frac{|\zeta-1|^2}
{|\zeta+1|^2}.
$$
Because
$$
|\zeta+1|^2-|\zeta-1|^2
=
4x
>0,
$$
one has
$$
|w|<1.
$$
Also
$$
\operatorname{Im}w
=
\frac{2y}
{|\zeta+1|^2}
>0.
$$
Hence
$$
w\in D_+.
$$
Therefore $T$ is onto $R_2$, and injectivity follows from the fact that it is a Möbius transformation.

:::

:::

::: {.pf-step #s1-4}

The composition
$$
F=T\circ S
$$
is a conformal equivalence
$$
R_1\xrightarrow{\sim}R_2.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
S:R_1\to D_+
$$
is a biholomorphism. By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
T:D_+\to R_2
$$
is a biholomorphism. Their composition is therefore a biholomorphism, and
$$
(T\circ S)(z)
=
\frac{1+z^2}{1-z^2}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested explicit conformal equivalence.

:::

:::

:::
