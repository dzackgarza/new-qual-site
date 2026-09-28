---
schema: qual/card@1
id: P-BKS08-2A
kind: problem
title: Evaluation of $\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx$ by residues
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the upper-half-plane residue computation and the
    semicircle decay estimate for the exponential integrand.
---

::: {.problem}
Evaluate
$$
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx.
$$
:::

::: {.solution}
Let
$$
F(z)\coloneqq\frac{e^{iz}}{1+z^2}.
$$

<1>1. For $R>1$, let $C_R$ be the positively oriented contour formed
by the interval $[-R,R]$ and the upper semicircle
$\Gamma_R=\{Re^{it}:0\le t\le\pi\}$. Then
$$
\int_{C_R}F(z)\,dz=\frac{\pi}{e}.
$$

::: {.proof}
The only pole of $F$ inside $C_R$ is the simple pole at $z=i$, with
residue
$$
\operatorname{Res}_{z=i}F(z)
=\frac{e^{ii}}{2i}
=\frac{e^{-1}}{2i}.
$$
The residue theorem therefore gives
$$
\int_{C_R}F(z)\,dz
=2\pi i\frac{e^{-1}}{2i}
=\frac{\pi}{e}.
$$
:::

<1>2. The integral over the semicircular arc satisfies
$$
\int_{\Gamma_R}F(z)\,dz\longrightarrow0
\qquad(R\to\infty).
$$

::: {.proof}
For $z\in\Gamma_R$ one has
$$
\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1
$$
and
$$
\abs{1+z^2}\ge \abs{z}^2-1=R^2-1.
$$
Since $\Gamma_R$ has length $\pi R$,
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\le
\frac{\pi R}{R^2-1}
\longrightarrow0.
$$
:::

<1>3. One has
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^2}\,dx
=\frac{\pi}{e}.
$$

::: {.proof}
Splitting the contour in step <1>1 gives
$$
\int_{-R}^{R}\frac{e^{ix}}{1+x^2}\,dx
+
\int_{\Gamma_R}F(z)\,dz
=\frac{\pi}{e}.
$$
The real-axis integral converges absolutely because
$\abs{e^{ix}/(1+x^2)}=(1+x^2)^{-1}$. Letting $R\to\infty$ and using
step <1>2 yields the identity.
:::

<1>4. Therefore
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx
=\frac{\pi}{e}.
}
$$

::: {.proof}
Taking real parts in step <1>3 gives the displayed formula. Equivalently,
the imaginary part integrates to zero because
$\sin x/(1+x^2)$ is odd.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested evaluation.
:::
:::
