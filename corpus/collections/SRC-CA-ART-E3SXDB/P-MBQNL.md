---
schema: qual/card@1
id: P-MBQNL
kind: problem
title: $\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that

\[
\int_{0}^{\infty} \frac{\sin x}{x} d x=\frac{\pi}{2}
.\]

> Hint: use the fact that this integral equals $\frac{1}{2 i} \int_{-\infty}^{\infty} \frac{e^{i x}-1}{x} d x$, and integrate around an indented semicircle.
:::

::: {.solution}
Let $f(z) \coloneqq e^{iz}/z$. For $0<\varepsilon<R$, let $\gamma_\varepsilon$ be the upper semicircle $z=\varepsilon e^{it}$ traversed from $-\varepsilon$ to $\varepsilon$ ($t$ from $\pi$ to $0$), and let $\Gamma_R$ be the upper semicircle $z=Re^{it}$, $t\in[0,\pi]$, traversed counterclockwise.
The closed contour $C_{\varepsilon,R}$ consists of $[-R,-\varepsilon]$, $\gamma_\varepsilon$, $[\varepsilon,R]$, and $\Gamma_R$.

<1>1. $\displaystyle\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{1}{2}\, \Im\left(\operatorname{PV}\!\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx\right)$, where
$$\operatorname{PV}\!\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx \coloneqq \lim_{\varepsilon\to0,\,R\to\infty}\left(\int_{-R}^{-\varepsilon}+\int_{\varepsilon}^{R}\right)\frac{e^{ix}}{x}\,dx.$$

<2>1. $\dfrac{e^{ix}}{x} = \dfrac{\cos x}{x} + i\,\dfrac{\sin x}{x}$ for real $x\neq0$.

::: {.proof}
This is Euler's formula $e^{ix} = \cos x + i \sin x$.
:::

<2>2. $\displaystyle\left(\int_{-R}^{-\varepsilon}+\int_{\varepsilon}^{R}\right)\frac{\cos x}{x}\,dx = 0$.

::: {.proof}
The function $\cos x/x$ is odd and the domain of integration is symmetric about $0$.
:::

<2>3. $\displaystyle\left(\int_{-R}^{-\varepsilon}+\int_{\varepsilon}^{R}\right)\frac{\sin x}{x}\,dx = 2\int_\varepsilon^{R} \frac{\sin x}{x}\, dx$.

::: {.proof}
The function $\sin x / x$ is even.
:::

<2>4. Q.E.D.

::: {.proof}
By steps <2>1--<2>3, the imaginary part of the truncated integral of $e^{ix}/x$ is $2\int_\varepsilon^R \frac{\sin x}{x}\,dx$; let $\varepsilon\to0$ and $R\to\infty$.
:::

<1>2. $\displaystyle\int_{C_{\varepsilon,R}} f(z)\,dz = 0$.

::: {.proof}
The only singularity of $f$ is the simple pole at $z=0$, which the indentation $\gamma_\varepsilon$ excludes. Hence $f$ is holomorphic on a neighborhood of the closed region bounded by $C_{\varepsilon,R}$, and Cauchy's theorem applies.
:::

<1>3. $\displaystyle\int_{\gamma_\varepsilon} f(z)\,dz \to -i\pi$ as $\varepsilon \to 0$.

::: {.proof}
With $z = \varepsilon e^{it}$, $dz/z = i\,dt$, so
$$\int_{\gamma_\varepsilon} f\, dz = i\int_\pi^0 e^{i\varepsilon e^{it}}\, dt.$$
The integrand converges uniformly to $1$ as $\varepsilon\to0$, so the integral tends to $i\int_\pi^0 dt=-i\pi$.
:::

<1>4. $\displaystyle\int_{\Gamma_R} f(z)\,dz \to 0$ as $R \to \infty$.

::: {.proof}
With $z = Re^{it}$, $dz/z = i\,dt$, so
$$\int_{\Gamma_R} f\, dz = i\int_0^\pi e^{iRe^{it}}\, dt,
\qquad
\abs{e^{iRe^{it}}} = e^{-R\sin t} \le 1.$$
For each $t\in(0,\pi)$, $e^{-R\sin t}\to0$ as $R\to\infty$. Dominated convergence, with dominating function $1$ on $[0,\pi]$, gives $\int_0^\pi e^{-R\sin t}\,dt\to0$, hence the claim.
:::

<1>5. $\displaystyle\operatorname{PV}\!\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx = i\pi$.

::: {.proof}
By step <1>2,
$$0 = \int_{-R}^{-\varepsilon} f + \int_{\gamma_\varepsilon} f + \int_{\varepsilon}^{R} f + \int_{\Gamma_R} f.$$
Let $\varepsilon \to 0$ and $R \to \infty$. Steps <1>3 and <1>4 give $\operatorname{PV}\!\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx - i\pi = 0$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1 and <1>5 give $\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{1}{2} \Im(i\pi) = \boxed{\frac{\pi}{2}}$.
:::
:::
