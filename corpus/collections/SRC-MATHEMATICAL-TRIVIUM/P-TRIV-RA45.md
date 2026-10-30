---
schema: qual/card@1
id: P-TRIV-RA45
kind: problem
title: Fourier transforms of a box function and a one-sided exponential
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 45, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the Fourier image $\tilde{f}(k)$ of the function $f(x)$, if $f(x)$ is given by

(a) $f(x) = \begin{cases} f_0, & \abs{x} \leqslant x_0, \\ 0, & \abs{x} > x_0 \end{cases}$

(b) $f(x) = \begin{cases} e^{-ax}, & x \geqslant 0, \ a > 0, \\ 0, & x < 0 \end{cases}$
:::

::: {.remark}
The source does not restate its Fourier-transform normalization here. The
solution uses
$$
\widetilde f(k)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
f(x)e^{-ikx}
\,dx,
$$
with inverse
$$
f(x)
=
\int_{-\infty}^{\infty}
\widetilde f(k)e^{ikx}
\,dk.
$$
This convention is consistent with the normalization of the adjacent inverse
transform problem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In part (a),
$$
\widetilde f(k)
=
\frac{f_0}{2\pi}
\int_{-x_0}^{x_0}
e^{-ikx}
\,dx.
$$


::: pf-proof

The function equals $f_0$ on $[-x_0,x_0]$ and vanishes elsewhere, so only
that interval contributes to the Fourier integral.

:::

:::

::: {.pf-step #s1-2}

For $k\neq0$,
$$
\int_{-x_0}^{x_0}
e^{-ikx}
\,dx
=
\frac{2\sin(kx_0)}{k}.
$$


::: pf-proof

An antiderivative is
$$
\frac{e^{-ikx}}{-ik}.
$$
Hence
$$
\begin{aligned}
\int_{-x_0}^{x_0}e^{-ikx}\,dx
&=
\frac{e^{-ikx_0}-e^{ikx_0}}{-ik}\\
&=
\frac{-2i\sin(kx_0)}{-ik}\\
&=
\frac{2\sin(kx_0)}k.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\widetilde f(k)
=
\frac{f_0}{\pi}
\frac{\sin(kx_0)}{k}
}
$$
for $k\neq0$.


::: pf-proof

Substitute step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The continuous value at $k=0$ is
$$
\boxed{
\widetilde f(0)
=
\frac{f_0x_0}{\pi}.
}
$$


::: pf-proof

Using
$$
\lim_{k\to0}\frac{\sin(kx_0)}k=x_0,
$$
step [](#s1-3){.pf-ref} extends continuously to the displayed value. Equivalently, set
$k=0$ directly in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Part (a) follows.


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give the complete transform.

:::

:::

::: {.pf-step #s1-6}

In part (b),
$$
\widetilde f(k)
=
\frac1{2\pi}
\int_0^\infty
e^{-(a+ik)x}
\,dx.
$$


::: pf-proof

The function is zero for $x<0$ and equals $e^{-ax}$ for $x\geq0$. Multiplying
by the Fourier kernel gives $e^{-(a+ik)x}$.

:::

:::

::: {.pf-step #s1-7}

Since $a>0$,
$$
\int_0^\infty
e^{-(a+ik)x}
\,dx
=
\frac1{a+ik}.
$$


::: pf-proof

The real part of $a+ik$ is positive, so the exponential decays at infinity.
Thus
$$
\int_0^\infty e^{-(a+ik)x}\,dx
=
\left[
-\frac{e^{-(a+ik)x}}{a+ik}
\right]_0^\infty
=
\frac1{a+ik}.
$$

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
\widetilde f(k)
=
\frac1{2\pi(a+ik)}
=
\frac{a-ik}{2\pi(a^2+k^2)}.
}
$$


::: pf-proof

Substitute step [](#s1-7){.pf-ref} into step [](#s1-6){.pf-ref} and rationalize the denominator.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

This is step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-9){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
