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
Find a function f (x) such that its Fourier image ${ \tilde { f } } ( p ) = c f ( p )$ , where c is a constant.
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

<1>1. Define
$$
I(p)
=
\int_{-\infty}^{\infty}
e^{-x^2/2}e^{-ipx}
\,dx.
$$

::: {.proof}
This is the unnormalized Fourier integral of the chosen Gaussian.
:::

<1>2. Differentiating under the integral sign gives
$$
I'(p)
=
-i
\int_{-\infty}^{\infty}
x e^{-x^2/2}e^{-ipx}
\,dx.
$$

::: {.proof}
The derivative of $e^{-ipx}$ with respect to $p$ is $-ix e^{-ipx}$. The
integrand is dominated by $|x|e^{-x^2/2}$, which is integrable, so dominated
convergence justifies differentiation under the integral sign.
:::

<1>3. Since
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
-ip,I(p).
$$

::: {.proof}
Write
$$
\begin{aligned}
\int x e^{-x^2/2}e^{-ipx}\,dx
&=
-\int
\frac{d}{dx}left(e^{-x^2/2}\right)e^{-ipx}\,dx\\
&=
-\left[e^{-x^2/2}e^{-ipx}\right]_{-\infty}^{\infty}
+
\int e^{-x^2/2}(-ip)e^{-ipx}\,dx.
\end{aligned}
$$
The boundary term vanishes because of Gaussian decay, leaving $-ipI(p)$.
:::

<1>4. Therefore
$$
I'(p)=-pI(p).
$$

::: {.proof}
Substitute step <1>3 into step <1>2:
$$
I'(p)
=
-i(-ip)I(p)
=
-pI(p).
$$
:::

<1>5. The initial value is
$$
I(0)=\sqrt{2\pi}.
$$

::: {.proof}
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

<1>6. Solving the differential equation from step <1>4 gives
$$
I(p)
=
\sqrt{2\pi}
e^{-p^2/2}.
$$

::: {.proof}
The equation
$$
I'=-pI
$$
has solution
$$
I(p)=Ce^{-p^2/2}.
$$
Step <1>5 gives $C=\sqrt{2\pi}$.
:::

<1>7. Hence
$$
\widetilde f(p)
=
\frac1{2\pi}I(p)
=
\frac1{\sqrt{2\pi}}
e^{-p^2/2}.
$$

::: {.proof}
Apply the Fourier normalization from the remark to the value in step <1>6.
:::

<1>8. Therefore
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

::: {.proof}
Since
$$
f(p)=e^{-p^2/2},
$$
step <1>7 is exactly the required eigenfunction relation.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 supplies the requested function and constant.
:::
:::
