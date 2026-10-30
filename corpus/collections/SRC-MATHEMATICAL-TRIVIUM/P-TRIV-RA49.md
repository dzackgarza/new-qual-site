---
schema: qual/card@1
id: P-TRIV-RA49
kind: problem
title: Fourier transform of the Yukawa potential $\alpha e^{-\mu r}/r$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 49, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the Fourier image $\tilde { f } ( \vec { k } )$ of the function $f ( \vec { r } ) = \alpha \frac { e ^ { - \mu r } } { r }$ , where $r = \norm{ \vec { r } }$ $\vec { r } \in \RR ^ { 3 }$ , and α and µ are constants.
:::

::: {.remark}
Use the three-dimensional extension of the Fourier convention from Problems
45--48:
$$
\widetilde f(\vec k)
=
\frac1{(2\pi)^3}
\int_{\RR^3}
f(\vec r)e^{-i\vec k\cdot\vec r}
\,d^3r.
$$
For an ordinary absolutely convergent Fourier integral, assume $\mu>0$.
:::

::: {.solution}

Put
$$
k=\norm{\vec k}.
$$

::: pf

::: pf-step

Because $f$ is radial, rotate coordinates so that $\vec k$ points
along the polar axis.


::: pf-proof

The integration measure and the radial function $f(\vec r)$ are rotation
invariant, so an orthogonal change of coordinates does not change the value of
the integral. In the rotated coordinates,
$$
\vec k\cdot\vec r
=
kr\cos\theta.
$$

:::

:::

::: {.pf-step #s1-2}

In spherical coordinates,
$$
\widetilde f(\vec k)
=
\frac{\alpha}{(2\pi)^3}
\int_0^\infty
e^{-\mu r}r
\,dr
\int_0^{2\pi}d\varphi
\int_0^\pi
e^{-ikr\cos\theta}
\sin\theta
\,d\theta.
$$


::: pf-proof

The volume element is
$$
d^3r
=
r^2\sin\theta\,dr\,d\theta\,d\varphi.
$$
Multiplying by
$$
f(r)=\alpha\frac{e^{-\mu r}}r
$$
leaves the radial factor $\alpha e^{-\mu r}r$.

:::

:::

::: {.pf-step #s1-3}

The polar-angle integral is
$$
\int_0^\pi
e^{-ikr\cos\theta}
\sin\theta
\,d\theta
=
\frac{2\sin(kr)}{kr}.
$$


::: pf-proof

Set
$$
u=\cos\theta,
\qquad
du=-\sin\theta\,d\theta.
$$
Then
$$
\begin{aligned}
\int_0^\pi
e^{-ikr\cos\theta}\sin\theta\,d\theta
&=
\int_{-1}^{1}e^{-ikru}\,du\\
&=
\frac{e^{ikr}-e^{-ikr}}{ikr}\\
&=
\frac{2\sin(kr)}{kr}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Therefore, for $k>0$,
$$
\widetilde f(\vec k)
=
\frac{4\pi\alpha}{(2\pi)^3k}
\int_0^\infty
e^{-\mu r}\sin(kr)
\,dr.
$$


::: pf-proof

The $\varphi$-integral gives $2\pi$. Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref};
the factor $r$ cancels with the $r$ in $kr$.

:::

:::

::: {.pf-step #s1-5}

The remaining integral is
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
\frac{\mu+ik}{\mu^2+k^2},
$$
which is valid because $\mu>0$.

:::

:::

::: pf-step

Hence, for $k>0$,
$$
\widetilde f(\vec k)
=
\frac{4\pi\alpha}{(2\pi)^3}
\frac1{\mu^2+k^2}.
$$


::: pf-proof

Substitute step [](#s1-5){.pf-ref} into step [](#s1-4){.pf-ref} and cancel the factor $k$.

:::

:::

::: {.pf-step #s1-7}

Simplifying the normalization gives
$$
\boxed{
\widetilde f(\vec k)
=
\frac{\alpha}
{2\pi^2(\mu^2+k^2)}.
}
$$


::: pf-proof

Since
$$
(2\pi)^3=8\pi^3,
$$
one has
$$
\frac{4\pi}{(2\pi)^3}
=
\frac1{2\pi^2}.
$$

:::

:::

::: {.pf-step #s1-8}

The same formula holds at $k=0$ by continuity.


::: pf-proof

The right-hand side tends to
$$
\frac{\alpha}{2\pi^2\mu^2}
$$
as $k\to0$. Directly at $k=0$,
$$
\widetilde f(0)
=
\frac{4\pi\alpha}{(2\pi)^3}
\int_0^\infty re^{-\mu r}\,dr
=
\frac{4\pi\alpha}{(2\pi)^3\mu^2},
$$
which is the same value.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give the Fourier image for all $\vec k\in\RR^3$.

:::

:::

:::
