---
schema: qual/card@1
id: P-TRIV-RA47
kind: problem
title: Eigenfunctions of the Fourier transform
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 47, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find a function $f(x)$ such that its Fourier image $\tilde{f}(p) = cf(p)$, where $c$ is a constant.
:::

::: {.remark}
Use the Fourier convention from Problems 45--46:
$$
\widetilde f(p)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
f(x)e^{-ipx}
\,dx.
$$
:::

::: {.solution}

Choose
$$
f(x)=e^{-x^2/2}.
$$

::: pf

::: pf-step

Define
$$
I(p)
=
\int_{-\infty}^{\infty}
e^{-x^2/2}e^{-ipx}
\,dx.
$$


::: pf-proof

This is the unnormalized Fourier integral of the chosen Gaussian.

:::

:::

::: {.pf-step #s1-2}

Differentiating under the integral sign gives
$$
I'(p)
=
-i
\int_{-\infty}^{\infty}
x e^{-x^2/2}e^{-ipx}
\,dx.
$$


::: pf-proof

The derivative of $e^{-ipx}$ with respect to $p$ is $-ix e^{-ipx}$. The
integrand is dominated by $\abs{x}e^{-x^2/2}$, which is integrable, so dominated
convergence justifies differentiation under the integral sign.

:::

:::

::: {.pf-step #s1-3}

Since
$$
x e^{-x^2/2}
=
-\frac{d}{dx}e^{-x^2/2},
$$
integration by parts gives
$$
\int_{-\infty}^{\infty}
x e^{-x^2/2}e^{-ipx}
\,dx
=
-ip\,I(p).
$$


::: pf-proof

Write
$$
\begin{aligned}
\int x e^{-x^2/2}e^{-ipx}\,dx
&=
-\int
\frac{d}{dx}\left(e^{-x^2/2}\right)e^{-ipx}\,dx\\
&=
-\left[e^{-x^2/2}e^{-ipx}\right]_{-\infty}^{\infty}
+
\int e^{-x^2/2}(-ip)e^{-ipx}\,dx.
\end{aligned}
$$
The boundary term vanishes because of Gaussian decay, leaving $-ipI(p)$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
I'(p)=-pI(p).
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}:
$$
I'(p)
=
-i(-ip)I(p)
=
-pI(p).
$$

:::

:::

::: {.pf-step #s1-5}

The initial value is
$$
I(0)=\sqrt{2\pi}.
$$


::: pf-proof

At $p=0$,
$$
I(0)
=
\int_{-\infty}^{\infty}e^{-x^2/2}\,dx.
$$
With $u=x/\sqrt2$,
$$
I(0)
=
\sqrt2
\int_{-\infty}^{\infty}e^{-u^2}\,du
=
\sqrt{2\pi}.
$$

:::

:::

::: {.pf-step #s1-6}

Solving the differential equation from step [](#s1-4){.pf-ref} gives
$$
I(p)
=
\sqrt{2\pi}
e^{-p^2/2}.
$$


::: pf-proof

The equation
$$
I'=-pI
$$
has solution
$$
I(p)=Ce^{-p^2/2}.
$$
Step [](#s1-5){.pf-ref} gives $C=\sqrt{2\pi}$.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\widetilde f(p)
=
\frac1{2\pi}I(p)
=
\frac1{\sqrt{2\pi}}
e^{-p^2/2}.
$$


::: pf-proof

Apply the Fourier normalization from the remark to the value in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\widetilde f(p)
=
c f(p),
\qquad
c=\frac1{\sqrt{2\pi}},
}
$$
for
$$
\boxed{f(x)=e^{-x^2/2}}.
$$


::: pf-proof

Since
$$
f(p)=e^{-p^2/2},
$$
step [](#s1-7){.pf-ref} is exactly the required eigenfunction relation.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} supplies the requested function and constant.

:::

:::

:::
