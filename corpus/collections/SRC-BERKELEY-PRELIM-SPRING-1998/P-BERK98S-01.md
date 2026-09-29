---
schema: qual/card@1
id: P-BERK98S-01
kind: problem
title: $z^4+z^3+1$ has exactly one root in the first quadrant
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
  date: 2026-09-23
---

::: {.problem}
Prove that
\[
z^4+z^3+1
\]
has exactly one root in the quadrant
\[
\{z=x+iy:x>0,\ y>0\}.
\]
:::

::: {.solution}
Put
$$
p(z)\coloneqq z^4+z^3+1.
$$
Let $\Gamma$ be the positively oriented boundary of the right half-disk
$$
D\coloneqq\{z\in\CC:\operatorname{Re}z>0,\ \abs{z}<2\}.
$$
Thus $\Gamma$ consists of the segment from $2i$ to $-2i$ and the semicircle
$2e^{i\theta}$, $-\pi/2\leq\theta\leq\pi/2$.

::: pf

::: {.pf-step #s1}

The polynomial $p$ has no zero on $\Gamma$, and every zero of $p$
with positive real part lies in $D$.

::: pf-proof

If $p(z)=0$ and $\abs{z}\geq2$, then
$$
\abs{z}^4
=\abs{z^3+1}
\leq \abs{z}^3+1.
$$
For $r\geq2$,
$$
r^4-r^3-1
=r^3(r-1)-1
>0,
$$
so this is impossible. Hence every zero of $p$ has modulus less than $2$.

On the imaginary axis,
$$
p(iy)
=y^4+1-iy^3,
$$
whose real part is $y^4+1>0$. Thus $p$ has no zero on the diameter of
$\Gamma$. The preceding modulus estimate excludes zeros on the semicircle.

:::

:::

::: {.pf-step #s2}

Along the diameter of $\Gamma$, the change in a continuous argument
of $p$ is $2\alpha$, where
$$
\alpha\coloneqq\arctan\frac{8}{17}.
$$

::: pf-proof

Parametrize the diameter by $z=iy$ with $y$ decreasing from $2$ to $-2$.
By step [](#s1){.pf-ref},
$$
p(iy)=1+y^4-iy^3
$$
always lies in the open right half-plane, so its principal argument varies
continuously. At the endpoints,
$$
p(2i)=17-8i,
\qquad
p(-2i)=17+8i.
$$
Their arguments are $-\alpha$ and $\alpha$, respectively. Hence the change
is $2\alpha$.

:::

:::

::: {.pf-step #s3}

Along the semicircle of $\Gamma$, the change in a continuous
argument of $p$ is $4\pi-2\alpha$.

::: pf-proof

For $z=2e^{i\theta}$ with $-\pi/2\leq\theta\leq\pi/2$,
$$
p(z)
=16e^{4i\theta}u(\theta),
$$
where
$$
u(\theta)
\coloneqq
1+\frac12e^{-i\theta}+\frac1{16}e^{-4i\theta}.
$$
Since
$$
\abs{u(\theta)-1}
\leq\frac12+\frac1{16}
=\frac9{16}
<1,
$$
the value $u(\theta)$ remains in the open right half-plane. We may therefore
use its principal argument continuously. At the endpoints,
$$
u(-\pi/2)=\frac{17+8i}{16},
\qquad
u(\pi/2)=\frac{17-8i}{16},
$$
so the change in the argument of $u$ is $-2\alpha$.

Meanwhile, as $\theta$ increases from $-\pi/2$ to $\pi/2$, the argument of
$e^{4i\theta}$ increases by $4\pi$. Therefore the total change in the
argument of $p$ along the semicircle is $4\pi-2\alpha$.

:::

:::

::: {.pf-step #s4}

The polynomial $p$ has exactly two zeros in the open right
half-plane, counted with multiplicity.

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, the total change in the argument of $p$ along
$\Gamma$ is
$$
2\alpha+(4\pi-2\alpha)=4\pi.
$$
By step [](#s1){.pf-ref}, $p$ has no zero on $\Gamma$. The argument principle therefore
gives
$$
\frac{4\pi}{2\pi}=2
$$
zeros in $D$, counted with multiplicity. Step [](#s1){.pf-ref} shows that these are
exactly the zeros of $p$ with positive real part.

:::

:::

::: {.pf-step #s5}

The first quadrant contains exactly $\boxed{1}$ zero of $p$.

::: pf-proof

The polynomial $p$ has real coefficients, so its nonreal zeros occur in
complex-conjugate pairs with the same multiplicity. It has no positive real
zero because
$$
p(x)=x^4+x^3+1>0
\qquad(x>0).
$$
Hence the two zeros in the open right half-plane counted in step [](#s4){.pf-ref} form
one conjugate pair: one lies in the first quadrant and the other in the
fourth quadrant. Thus exactly one zero lies in the first quadrant.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
