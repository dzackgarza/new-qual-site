---
schema: qual/card@1
id: P-CHAVAN-CA-3-3
kind: problem
title: An analytic square root without an analytic logarithm
classification: {areas: [complex-analysis], topics: [Branches of the Logarithm]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
---

::: {.problem}
Let
$$
\Omega=\CC\setminus[-1,1],
\qquad
f(z)=z^2-1,
$$
and define
$$
g(z)=\abs{f(z)}^{1/2}
\exp\!\left(\frac{i}{2}\bigl(\arg(z-1)+\arg(z+1)\bigr)\right),
$$
where $\arg$ is the principal argument.

(a) Show that $g$ is well-defined and continuous on $\Omega$ and satisfies $g^2=f$.

(b) Show that $g$ is analytic on $\Omega$.

(c) Show that $f$ has no analytic logarithm on $\Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $g$ is well-defined on $\Omega$ and satisfies
$$
g(z)^2=f(z)
$$
for every $z\in\Omega$.


::: pf-proof

For $z\in\Omega$, neither $z-1$ nor $z+1$ is zero, so both principal
arguments in the definition of $g$ are defined. Moreover,
$$
z-1=\abs{z-1}e^{i\arg(z-1)},
\qquad
z+1=\abs{z+1}e^{i\arg(z+1)}.
$$
Therefore
$$
\begin{aligned}
g(z)^2
&=\abs{f(z)}
e^{i(\arg(z-1)+\arg(z+1))}\\
&=\abs{z-1}\abs{z+1}
e^{i\arg(z-1)}e^{i\arg(z+1)}\\
&=(z-1)(z+1)\\
&=f(z).
\end{aligned}
$$
Thus the displayed formula defines a single value $g(z)$ and its
square is $f(z)$.

:::

:::

::: {.pf-step #s1-2}

The function $g$ is continuous on
$$
\Omega\setminus(1,\infty).
$$


::: pf-proof

By Problem 3.1, the principal argument is continuous away from the
positive real axis. Hence $z\mapsto\arg(z-1)$ can be discontinuous
only when $z\in(1,\infty)$, while
$z\mapsto\arg(z+1)$ can be discontinuous only when
$z\in(-1,\infty)$. Intersecting with
$\Omega=\CC\setminus[-1,1]$, both possible discontinuity sets
reduce to $(1,\infty)$. Thus away from that ray both argument terms
are continuous. Since $f$ is continuous and nonzero on $\Omega$, so
is $\abs{f}^{1/2}$, and the defining product for $g$ is continuous there.

:::

:::

::: {.pf-step #s1-3}

The function $g$ is continuous at every $x\in(1,\infty)$.


::: pf-proof

Fix $x>1$ and choose a disk about $x$ small enough that its real points
all lie in $(1,\infty)$. As $z\to x$ through the upper half-plane,
both $z-1$ and $z+1$ approach positive real numbers from above, so
$$
\arg(z-1)\to0,
\qquad
\arg(z+1)\to0.
$$
As $z\to x$ through the lower half-plane, both approach the positive
real axis from below, so
$$
\arg(z-1)\to2\pi,
\qquad
\arg(z+1)\to2\pi.
$$
Consequently the exponential factor in $g$ tends respectively to
$$
e^{i(0+0)/2}=1
\qquad\text{or}\qquad
e^{i(2\pi+2\pi)/2}=e^{2\pi i}=1.
$$
Along the positive real axis itself the two arguments are both $0$.
Thus for every approach to $x$ the exponential factor tends to $1$.
Also $\abs{f(z)}^{1/2}\to\abs{f(x)}^{1/2}$, and the defining formula gives
$g(x)=\abs{f(x)}^{1/2}$. Hence $g(z)\to g(x)$.

:::

:::

::: {.pf-step #s1-4}

The function $g$ is continuous on all of $\Omega$.


::: pf-proof

Step [](#s1-2){.pf-ref} gives continuity away from $(1,\infty)$, and step [](#s1-3){.pf-ref} gives
continuity at every point of that remaining ray.

:::

:::

::: {.pf-step #s1-5}

The function $g$ is analytic on $\Omega$.


::: pf-proof

Fix $z_0\in\Omega$. By step [](#s1-1){.pf-ref},
$$
g(z_0)^2=f(z_0)\ne0,
$$
so $g(z_0)\ne0$. For $z\ne z_0$, the identity $g^2=f$ gives
$$
\frac{g(z)-g(z_0)}{z-z_0}
=
\frac{f(z)-f(z_0)}{z-z_0}
\frac1{g(z)+g(z_0)}.
$$
By step [](#s1-4){.pf-ref}, $g(z)\to g(z_0)$ as $z\to z_0$, and the denominator on
the right tends to $2g(z_0)\ne0$. Since $f$ is analytic,
$$
\lim_{z\to z_0}\frac{g(z)-g(z_0)}{z-z_0}
=\frac{f'(z_0)}{2g(z_0)}.
$$
Thus $g$ is complex differentiable at every point of $\Omega$, hence
analytic there.

:::

:::

::: {.pf-step #s1-6}

If an analytic function $L$ on $\Omega$ satisfied
$$
e^{L(z)}=f(z),
$$
then
$$
L'(z)=\frac{f'(z)}{f(z)}
=\frac1{z-1}+\frac1{z+1}.
$$


::: pf-proof

Differentiating $e^L=f$ gives
$$
L'(z)e^{L(z)}=f'(z).
$$
Since $e^{L(z)}=f(z)\ne0$ on $\Omega$,
$$
L'(z)=\frac{f'(z)}{f(z)}
=\frac{2z}{z^2-1}
=\frac1{z-1}+\frac1{z+1}.
$$

:::

:::

::: {.pf-step #s1-7}

The function $f$ has no analytic logarithm on $\Omega$.


::: pf-proof

Suppose such an $L$ existed. Choose $R>1$ and let
$$
\gamma(t)=Re^{it},
\qquad
0\le t\le2\pi.
$$
The circle $\gamma$ lies in $\Omega$. Since $L'$ has the primitive
$L$ on $\Omega$,
$$
\int_\gamma L'(z)\,dz=0.
$$
On the other hand, step [](#s1-6){.pf-ref} and the Cauchy integral formula give
$$
\begin{aligned}
\int_\gamma L'(z)\,dz
&=\int_\gamma\frac{dz}{z-1}
 +\int_\gamma\frac{dz}{z+1}\\
&=2\pi i+2\pi i\\
&=4\pi i,
\end{aligned}
$$
because both $1$ and $-1$ lie inside the circle. This contradiction
shows that no analytic logarithm of $f$ exists on $\Omega$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove part (a), step [](#s1-5){.pf-ref} proves part (b), and step [](#s1-7){.pf-ref}
proves part (c).

:::

:::

:::
