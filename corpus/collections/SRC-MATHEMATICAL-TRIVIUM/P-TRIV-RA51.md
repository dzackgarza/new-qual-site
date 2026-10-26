---
schema: qual/card@1
id: P-TRIV-RA51
kind: problem
title: Fourier transform of $f_0(\frac1r+\frac1a)e^{-2r/a}$ in $\mathbb{R}^3$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 51, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the Fourier image $\tilde { f } ( \vec { k } )$ of the function $f ( \vec { r } ) = f _ { 0 } \left( \frac { 1 } { r } + \frac { 1 } { a } \right) e ^ { - \frac { 2 r } { a } }$ in $\mathbb { R } ^ { 3 }$
:::

::: {.remark}
Use the three-dimensional Fourier convention from Problems 49--50:
$$
\widetilde f(\vec k)
=
\frac1{(2\pi)^3}
\int_{\mathbb R^3}
f(\vec r)e^{-i\vec k\cdot\vec r}
\,d^3r.
$$
For ordinary convergence, assume $a>0$.
:::

Put
$$
k=|\vec k|
$$
and
$$
\mu=\frac2a.
$$

::: pf

::: pf-step

For any radial function $F(r)$,
$$
\frac1{(2\pi)^3}
\int_{\mathbb R^3}
F(r)e^{-i\vec k\cdot\vec r}
\,d^3r
=
\frac1{2\pi^2k}
\int_0^\infty
rF(r)\sin(kr)
\,dr
$$
for $k>0$.


::: pf-proof

Choose spherical coordinates with polar axis parallel to $\vec k$. Then
$$
\vec k\cdot\vec r=kr\cos\theta.
$$
The angular integral is
$$
\int_0^{2\pi}d\varphi
\int_0^\pi
e^{-ikr\cos\theta}\sin\theta\,d\theta
=
4\pi\frac{\sin(kr)}{kr}.
$$
Multiplying by the spherical volume factor $r^2dr$ and by $(2\pi)^{-3}$
gives the stated radial formula.

:::

:::

::: pf-step

For the present function,
$$
r f(r)
=
f_0
\left(
1+\frac r a
\right)e^{-\mu r}.
$$


::: pf-proof

Multiply
$$
f(r)
=
f_0
\left(
\frac1r+\frac1a
\right)e^{-2r/a}
$$
by $r$ and use $\mu=2/a$.

:::

:::

::: pf-step

Therefore
$$
\widetilde f(\vec k)
=
\frac{f_0}{2\pi^2k}
\left[
\int_0^\infty e^{-\mu r}\sin(kr)\,dr
+
\frac1a
\int_0^\infty r e^{-\mu r}\sin(kr)\,dr
\right].
$$


::: pf-proof

Substitute step <1>2 into the radial transform formula of step <1>1 and split
the integral linearly.

:::

:::

::: pf-step

The first integral equals
$$
\int_0^\infty
e^{-\mu r}\sin(kr)
\,dr
=
\frac{k}{\mu^2+k^2}.
$$


::: pf-proof

Take the imaginary part of
$$
\int_0^\infty
e^{-(\mu-ik)r}
\,dr
=
\frac1{\mu-ik}
=
\frac{\mu+ik}{\mu^2+k^2}.
$$
The integral converges because $\mu>0$.

:::

:::

::: pf-step

The second integral equals
$$
\int_0^\infty
r e^{-\mu r}\sin(kr)
\,dr
=
\frac{2\mu k}{(\mu^2+k^2)^2}.
$$


::: pf-proof

Differentiate the identity in step <1>4 with respect to $\mu$:
$$
\frac{\partial}{\partial\mu}
\int_0^\infty
e^{-\mu r}\sin(kr)
\,dr
=
-\int_0^\infty
r e^{-\mu r}\sin(kr)
\,dr.
$$
On the right-hand side of step <1>4,
$$
\frac{\partial}{\partial\mu}
\frac{k}{\mu^2+k^2}
=
-\frac{2\mu k}{(\mu^2+k^2)^2}.
$$
Negating gives the result.

:::

:::

::: pf-step

Substituting steps <1>4--<1>5 into step <1>3 gives
$$
\widetilde f(\vec k)
=
\frac{f_0}{2\pi^2}
\left[
\frac1{\mu^2+k^2}
+
\frac{2\mu/a}{(\mu^2+k^2)^2}
\right].
$$


::: pf-proof

Both integrals contain a factor $k$, which cancels the $1/k$ in step <1>3.

:::

:::

::: pf-step

Since
$$
\mu=\frac2a,
$$
one has
$$
\frac{2\mu}{a}
=
\frac4{a^2}
$$
and
$$
\mu^2
=
\frac4{a^2}.
$$


::: pf-proof

Substitute $\mu=2/a$ directly.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\widetilde f(\vec k)
=
\frac{f_0}{2\pi^2}
\frac{k^2+8/a^2}
{(k^2+4/a^2)^2}.
}
$$


::: pf-proof

Use step <1>7 in step <1>6 and combine the two fractions:
$$
\frac1D+\frac{4/a^2}{D^2}
=
\frac{D+4/a^2}{D^2},
\qquad
D=k^2+4/a^2.
$$
Thus the numerator becomes $k^2+8/a^2$.

:::

:::

::: pf-step

The same formula holds at $k=0$ by continuity.


::: pf-proof

The right-hand side of step <1>8 is continuous at $k=0$. Direct substitution
there gives
$$
\widetilde f(0)
=
\frac{f_0a^2}{4\pi^2},
$$
which also equals the normalized spatial integral of $f$.

:::

:::

::: pf-qed

Steps <1>8--<1>9 give the Fourier image for every $\vec k$.

:::

:::
