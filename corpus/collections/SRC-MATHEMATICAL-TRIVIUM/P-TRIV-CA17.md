---
schema: qual/card@1
id: P-TRIV-CA17
kind: problem
title: $\int_{-\infty}^\infty \frac{x^2}{x^4-2x^2\cos 2\theta+1}\,dx$ by residues
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 17, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
For real $\theta$ with $\sin\theta\ne0$, compute $\int _ { - \infty } ^ { \infty } \frac { x ^ { 2 } } { x ^ { 4 } - 2 x ^ { 2 } \cos 2 \theta + 1 } \mathrm { d } x ;$
:::

::: {.remark}
The source gives no range for $\theta$. For real $\theta$ the denominator is
$(x^2-1)^2+4x^2\sin^2\theta$, so when $\sin\theta=0$ the integrand has a
nonintegrable singularity at $x=\pm1$. The solution below treats every real
$\theta$ for which the ordinary improper integral is finite.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integral depends on $\theta$ only through
$$
\abs{\sin\theta}.
$$


::: pf-proof

The denominator contains $\theta$ only through
$$
\cos2\theta
=
1-2\sin^2\theta.
$$
Thus replacing $\theta$ by any angle with the same value of
$\abs{\sin\theta}$ leaves the integrand unchanged.

:::

:::

::: {.pf-step #s1-2}

It suffices to compute the integral for
$$
0<\theta<\pi.
$$


::: pf-proof

If $\sin\theta\ne0$, choose $\vartheta\in(0,\pi)$ with
$$
\sin\vartheta=\abs{\sin\theta}.
$$
By step [](#s1-1){.pf-ref} the two integrands coincide. After computing the formula in this
range, replace $\sin\vartheta$ by $\abs{\sin\theta}$.

:::

:::

::: {.pf-step #s1-3}

For $0<\theta<\pi$,
$$
z^4-2z^2\cos2\theta+1
=
(z^2-e^{2i\theta})(z^2-e^{-2i\theta}).
$$


::: pf-proof

Multiplying gives
$$
z^4
-
(e^{2i\theta}+e^{-2i\theta})z^2
+
1.
$$
Euler's formula gives
$$
e^{2i\theta}+e^{-2i\theta}
=
2\cos2\theta.
$$

:::

:::

::: {.pf-step #s1-4}

Suppose
$$
0<\theta<\pi
\qquad\text{and}\qquad
\theta\ne\frac\pi2.
$$
Then the poles in the upper half-plane are
$$
z_1=e^{i\theta}
\qquad\text{and}\qquad
z_2=-e^{-i\theta},
$$
and both are simple.


::: pf-proof

By step [](#s1-3){.pf-ref} the four poles are
$$
\pm e^{i\theta},
\qquad
\pm e^{-i\theta}.
$$
For $0<\theta<\pi$, the roots $e^{i\theta}$ and
$-e^{-i\theta}=e^{i(\pi-\theta)}$ lie in the upper half-plane. The other
two lie in the lower half-plane. The two upper poles coincide only when
$\theta=\pi/2$, which is excluded here.

:::

:::

::: {.pf-step #s1-5}

For
$$
F(z)
=
\frac{z^2}{z^4-2z^2\cos2\theta+1},
$$
the two upper-half-plane residues from step [](#s1-4){.pf-ref} are
$$
\operatorname{Res}_{z=e^{i\theta}}F
=
\frac{e^{i\theta}}{4i\sin2\theta}
$$
and
$$
\operatorname{Res}_{z=-e^{-i\theta}}F
=
\frac{e^{-i\theta}}{4i\sin2\theta}.
$$


::: pf-proof

Let
$$
P(z)=z^4-2z^2\cos2\theta+1.
$$
Then
$$
P'(z)
=
4z(z^2-\cos2\theta).
$$
At $z=e^{i\theta}$,
$$
z^2-\cos2\theta
=
e^{2i\theta}-\cos2\theta
=
i\sin2\theta,
$$
so
$$
\operatorname{Res}_{z=e^{i\theta}}F
=
\frac{e^{2i\theta}}
{4e^{i\theta}i\sin2\theta}
=
\frac{e^{i\theta}}{4i\sin2\theta}.
$$

At $z=-e^{-i\theta}$,
$$
z^2-\cos2\theta
=
-i\sin2\theta,
$$
and direct substitution gives the second displayed residue.

:::

:::

::: {.pf-step #s1-6}

The sum of the two residues in step [](#s1-5){.pf-ref} is
$$
\frac1{4i\sin\theta}.
$$


::: pf-proof

Their sum is
$$
\frac{e^{i\theta}+e^{-i\theta}}
{4i\sin2\theta}
=
\frac{2\cos\theta}
{8i\sin\theta\cos\theta}
=
\frac1{4i\sin\theta}.
$$
The cancellation is valid because $\theta\ne\pi/2$.

:::

:::

::: {.pf-step #s1-7}

If
$$
0<\theta<\pi,
\qquad
\theta\ne\frac\pi2,
$$
then
$$
\int_{-\infty}^{\infty}
\frac{x^2}
{x^4-2x^2\cos2\theta+1}\,dx
=
\frac{\pi}{2\sin\theta}.
$$


::: pf-proof

Close the real segment by an upper semicircle. On $\abs{z}=R>1$,
$$
\abs{z^2-e^{2i\theta}}
\geq
R^2-1
$$
and
$$
\abs{z^2-e^{-2i\theta}}
\geq
R^2-1.
$$
Thus
$$
\abs{F(z)}
\leq
\frac{R^2}{(R^2-1)^2}.
$$
The upper arc has length $\pi R$, so its integral tends to zero.

By the residue theorem and step [](#s1-6){.pf-ref},
$$
\int_{-\infty}^{\infty}F(x)\,dx
=
2\pi i
\frac1{4i\sin\theta}
=
\frac{\pi}{2\sin\theta}.
$$

:::

:::

::: {.pf-step #s1-8}

If
$$
\theta=\frac\pi2,
$$
then
$$
\int_{-\infty}^{\infty}
\frac{x^2}{(x^2+1)^2}\,dx
=
\frac\pi2.
$$


::: pf-proof

For $\theta=\pi/2$,
$$
x^4-2x^2\cos\pi+1
=
(x^2+1)^2.
$$
Close in the upper half-plane. The only enclosed pole is the double pole
$z=i$. Its residue is
$$
\operatorname{Res}_{z=i}
\frac{z^2}{(z^2+1)^2}
=
\evaluated{
\frac{d}{dz}
\frac{z^2}{(z+i)^2}
}_{z=i}
=
-\frac{i}{4}.
$$
The arc integral again tends to zero because the integrand is
$O(\abs{z}^{-2})$. Hence
$$
\int_{-\infty}^{\infty}
\frac{x^2}{(x^2+1)^2}\,dx
=
2\pi i
\left(-\frac{i}{4}\right)
=
\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-9}

For every
$$
0<\theta<\pi,
$$
one has
$$
\int_{-\infty}^{\infty}
\frac{x^2}
{x^4-2x^2\cos2\theta+1}\,dx
=
\frac{\pi}{2\sin\theta}.
$$


::: pf-proof

Step [](#s1-7){.pf-ref} proves the formula away from $\theta=\pi/2$, and step [](#s1-8){.pf-ref} gives
the same value at $\theta=\pi/2$ because $\sin(\pi/2)=1$.

:::

:::

::: {.pf-step #s1-10}

Therefore, for every real $\theta$ with $\sin\theta\ne0$,
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{x^2}
{x^4-2x^2\cos2\theta+1}\,dx
=
\frac{\pi}{2\abs{\sin\theta}}.
}
$$


::: pf-proof

Reduce to an angle in $(0,\pi)$ using step [](#s1-2){.pf-ref}, apply step [](#s1-9){.pf-ref}, and replace
$\sin\vartheta$ by $\abs{\sin\theta}$.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the maximal real-parameter form of the requested integral.

:::

:::

:::
