---
schema: qual/card@1
id: P-BKF00-9
kind: problem
title: Two real-value lines for a nonconstant entire function meet at a rational angle
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Reality on the two normalized lines forces one nonconstant Taylor
    coefficient to make e^{im theta} real, hence the angle is rational in pi.
---

::: {.problem}
Let $f$ be a nonconstant entire function. Suppose $f$ takes real values on two intersecting lines in the complex plane. Prove that the measure of either angle formed by the two lines is a rational multiple of $\pi$.
:::

::: {.solution}

Let $z_0$ be the intersection point of the two lines. Choose $\varphi$ so
that the first line is $z_0+e^{i\varphi}\RR$, and let $\theta$ be an angle
from the first line to the second, so the second line is
$z_0+e^{i(\varphi+\theta)}\RR$ with $0\le\theta\le\pi$. Set
$$
g(z)=f(z_0+e^{i\varphi}z),
$$
so $g$ is a nonconstant entire function real-valued on both $\RR$ and
$e^{i\theta}\RR$.

::: pf

::: {.pf-step #taylor-coeffs-real}
In the Taylor expansion
$$
g(z)=\sum_{m=0}^{\infty}a_mz^m,
$$
every coefficient $a_m$ is real.

::: pf-proof
Since $g(x)\in\RR$ for real $x$, every real derivative of the restriction
$g|_{\RR}$ at $0$ is real. Because $g$ is holomorphic, these derivatives
are the complex derivatives $g^{(m)}(0)$. Hence
$$
a_m=\frac{g^{(m)}(0)}{m!}\in\RR
$$
for every $m\ge0$.
:::

:::

::: {.pf-step #a-m-e-im-theta-real}
For every $m\ge0$, the number $a_me^{im\theta}$ is real.

::: pf-proof
The entire function
$$
h(z)=g(e^{i\theta}z)
=\sum_{m=0}^{\infty}a_me^{im\theta}z^m
$$
is real-valued on $\RR$, because $g$ is real-valued on
$e^{i\theta}\RR$. Applying step [](#taylor-coeffs-real){.pf-ref} to $h$ shows that all of its Taylor
coefficients $a_me^{im\theta}$ are real.
:::

:::

::: {.pf-step #theta-rational-multiple-pi}
The angle $\theta$ is a rational multiple of $\pi$.

::: pf-proof
Since $g$ is nonconstant, there is some $m\ge1$ with $a_m\neq0$. By step
[](#taylor-coeffs-real){.pf-ref}, $a_m$ is a nonzero real number, and by step [](#a-m-e-im-theta-real){.pf-ref},
$a_me^{im\theta}$ is real. Therefore $e^{im\theta}$ is real, so
$$
\sin(m\theta)=0.
$$
Hence $m\theta=k\pi$ for some integer $k$, and therefore
$$
\theta=\frac{k}{m}\pi.
$$
:::

:::

::: {.pf-step #either-angle-rational}
Either angle formed by the two lines is a rational multiple of
$\pi$.

::: pf-proof
One angle has measure $\theta$, which is a rational multiple of $\pi$ by
step [](#theta-rational-multiple-pi){.pf-ref}. The other has measure $\pi-\theta$, which is therefore also a
rational multiple of $\pi$.
:::

:::

::: pf-qed
Step [](#either-angle-rational){.pf-ref} is the required conclusion.
:::

:::

:::
