---
schema: qual/card@1
id: P-4Y4QT
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^3}\,dx=\frac{\pi}{3}\csc\frac{\pi a}{3}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Let $0<a<4$ and evaluate
\[
\int_0^\infty \frac{x^{\alpha-1}}{1+x^3} ~dx
\]
:::

::: {.solution}
Read the exponent as $\alpha=a$.

<1>1. The integral $\int_0^\infty x^{a-1}/(1+x^3)\,dx$ converges if and only if $0<a<3$.

::: {.proof}
Near $0$ the integrand is asymptotic to $x^{a-1}$, which is integrable on $(0,1)$ if and only if $a>0$. Near $\infty$ it is asymptotic to $x^{a-4}$, which is integrable on $(1,\infty)$ if and only if $a<3$.
:::

<1>2. For $0<a<3$,
$$\int_0^\infty {x^{a-1}\over1+x^3}\,dx = \boxed{{\pi\over3}\csc{\pi a\over3}}.$$

::: {.proof}
With $t=x^3$,
$$\int_0^\infty {x^{a-1}\over1+x^3}\,dx
={1\over3}\int_0^\infty {t^{a/3-1}\over1+t}\,dt
={1\over3}B\!\left(\frac a3,1-\frac a3\right)
={1\over3}\Gamma\!\left(\frac a3\right)\Gamma\!\left(1-\frac a3\right),$$
and Euler's reflection formula $\Gamma(s)\Gamma(1-s)=\pi/\sin(\pi s)$ gives the value.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 evaluates the integral on its range of convergence from step <1>1; for $3\le a<4$ it diverges.
:::
:::

::: {.remark}
The hypothesis names $a$ while the integrand has exponent $\alpha-1$. With $\alpha=a$, the integral converges only for $0<a<3$. The stated range $0<a<4$ is the range of convergence of $\int_0^\infty x^{a-1}/(1+x^4)\,dx$, and the substitution $t=x^4$ gives
$$\int_0^\infty\frac{x^{a-1}}{1+x^4}\,dx=\frac{\pi}{4}\csc\frac{\pi a}{4}\qquad(0<a<4).$$
:::
