---
schema: qual/card@1
id: P-BERK77S-16
kind: problem
title: Evaluate $\int_0^{2\pi}(a+\cos\theta)^{-1}\,d\theta$ by residues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Substituted z=e^{i theta}, reducing the integral to a unit-circle
    contour integral with poles -a±sqrt(a^2-1). For real a>1 exactly the
    plus-sign pole lies inside, giving 2 pi/sqrt(a^2-1). On the half-plane
    Re(a)>1 both the parameter integral and the compatible square-root
    formula are holomorphic, so the identity theorem extends the formula to
    all nonreal a in that half-plane.
---

::: {.problem}
Use the residue theorem to evaluate
\[
I(a)=\int_0^{2\pi}\frac{d\theta}{a+\cos\theta},
\]
where $a$ is real and $a>1$.

Why is the resulting formula for $I(a)$ also valid for certain nonreal complex values of $a$?
:::

::: {.solution}
<1>1. With the substitution
$$
z=e^{i\theta},
$$
the integral becomes
$$
I(a)
=
\oint_{\abs{z}=1}
\frac{2\,dz}
{i(z^2+2az+1)}.
$$

::: {.proof}
On the unit circle,
$$
\cos\theta
=
\frac12\left(z+\frac1z\right)
$$
and
$$
d\theta=\frac{dz}{iz}.
$$
Therefore
$$
\begin{aligned}
\frac{d\theta}{a+\cos\theta}
&=
\frac{1}{a+\frac12(z+z^{-1})}
\frac{dz}{iz}\\
&=
\frac{2\,dz}{i(z^2+2az+1)}.
\end{aligned}
$$
As $\theta$ runs from $0$ to $2\pi$, $z$ traverses the unit circle once
counterclockwise.
:::

<1>2. For real $a>1$, the two poles of the contour integrand are
$$
z_\pm=-a\pm\sqrt{a^2-1},
$$
and exactly $z_+$ lies inside the unit circle.

::: {.proof}
The poles are the roots of
$$
z^2+2az+1=0,
$$
which are the displayed numbers. Their product is
$$
z_+z_-=1.
$$
Since $a>1$,
$$
z_-=-a-\sqrt{a^2-1}<-1,
$$
so $\abs{z_-}>1$. Hence
$$
\abs{z_+}
=
\frac1{\abs{z_-}}
<
1.
$$
Thus only $z_+$ is enclosed by the unit circle.
:::

<1>3. The residue at the enclosed pole is
$$
\operatorname{Res}_{z=z_+}
\frac{2}{i(z^2+2az+1)}
=
\frac1{i\sqrt{a^2-1}}.
$$

::: {.proof}
Factor
$$
z^2+2az+1=(z-z_+)(z-z_-).
$$
The pole at $z_+$ is simple, so
$$
\begin{aligned}
\operatorname{Res}_{z=z_+}
\frac{2}{i(z-z_+)(z-z_-)}
&=
\frac{2}{i(z_+-z_-)}\\
&=
\frac{2}
{i\left(2\sqrt{a^2-1}\right)}\\
&=
\frac1{i\sqrt{a^2-1}}.
\end{aligned}
$$
:::

<1>4. For real $a>1$,
$$
\boxed{
I(a)=\frac{2\pi}{\sqrt{a^2-1}}.
}
$$

::: {.proof}
By the residue theorem and steps <1>1--<1>3,
$$
\begin{aligned}
I(a)
&=
2\pi i
\operatorname{Res}_{z=z_+}
\frac{2}{i(z^2+2az+1)}\\
&=
2\pi i
\frac1{i\sqrt{a^2-1}}\\
&=
\frac{2\pi}{\sqrt{a^2-1}}.
\end{aligned}
$$
:::

<1>5. The function
$$
a\longmapsto I(a)
=
\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}
$$
is holomorphic on the half-plane
$$
H=\{a\in\CC:\operatorname{Re}a>1\}.
$$

::: {.proof}
Fix a compact set $K\subset H$. There is a $\delta>0$ such that
$$
\operatorname{Re}a\geq1+\delta
$$
for every $a\in K$. Hence for every $\theta$,
$$
\abs{a+\cos\theta}
\geq
\operatorname{Re}(a+\cos\theta)
\geq
\delta.
$$
Thus the integrand and its $a$-derivative
$$
-\frac1{(a+\cos\theta)^2}
$$
are uniformly bounded on $K\times[0,2\pi]$. Differentiation under the
integral sign is therefore valid on $H$, so $I$ is holomorphic there.
:::

<1>6. There is a holomorphic square root
$$
s(a)=\sqrt{a^2-1}
$$
on $H$ which is positive for real $a>1$.

::: {.proof}
For $a\in H$, both $a-1$ and $a+1$ lie in the right half-plane. The
principal square root is holomorphic on the right half-plane and positive
on the positive real axis. Define
$$
s(a)
=
\sqrt{a-1}\,\sqrt{a+1}
$$
using these principal square roots. Then $s$ is holomorphic on $H$,
$$
s(a)^2=a^2-1,
$$
and $s(a)>0$ for real $a>1$.
:::

<1>7. For every complex $a$ with $\operatorname{Re}a>1$,
$$
\boxed{
I(a)=\frac{2\pi}{s(a)}
=
\frac{2\pi}{\sqrt{a^2-1}},
}
$$
where the square root is the branch from step <1>6.

::: {.proof}
By step <1>5, $I(a)$ is holomorphic on the connected domain $H$. By step
<1>6,
$$
\frac{2\pi}{s(a)}
$$
is also holomorphic on $H$. Step <1>4 shows that the two holomorphic
functions agree for every real $a>1$. This set has accumulation points in
$H$, so the identity theorem implies that they agree throughout $H$.
In particular, the formula holds for every nonreal $a$ with
$\operatorname{Re}a>1$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 evaluates the original real integral, and step <1>7 explains the
nonreal complex parameters for which the same formula follows by analytic
continuation.
:::
:::
