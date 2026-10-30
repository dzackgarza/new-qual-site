---
schema: qual/card@1
id: P-BKS88-8
kind: problem
title: Integrals of $\cos n\theta/(a-\cos\theta)$ and $\sin n\theta/(a-\cos\theta)$
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
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
For $a > 1$ and $n = 0, 1, 2, \ldots$, evaluate the integrals
$$
C_{n}(a) = \int_{-\pi}^{\pi} \frac{\cos n\theta}{a - \cos\theta}\, d\theta, \qquad S_{n}(a) = \int_{-\pi}^{\pi} \frac{\sin n\theta}{a - \cos\theta}\, d\theta.
$$
:::

::: {.solution}
Let
$$
s:=\sqrt{a^2-1}
\qquad\text{and}\qquad
\rho:=a-s.
$$

::: pf

::: {.pf-step #poisson-expansion}
One has $0<\rho<1$ and
$$
\frac{1}{a-\cos\theta}
=\frac1s\left(1+2\sum_{k=1}^{\infty}\rho^k\cos k\theta\right),
$$
with uniform convergence in $\theta$.

::: pf-proof
Since $(a-s)(a+s)=1$, one has $\rho^{-1}=a+s$, and therefore
$$
\rho+\rho^{-1}=2a,
\qquad
\rho^{-1}-\rho=2s.
$$
As $a>1$, this gives $0<\rho<1$. Hence
$$
a-\cos\theta
=\frac{1-2\rho\cos\theta+\rho^2}{2\rho}
$$
and
$$
\frac{2\rho}{1-\rho^2}=\frac1s.
$$
For $\abs{\rho}<1$, the geometric series for $(1-\rho e^{i\theta})^{-1}$ and $(1-\rho e^{-i\theta})^{-1}$ converge uniformly in $\theta$. Adding them gives the Poisson-kernel identity
$$
\frac{1-\rho^2}{1-2\rho\cos\theta+\rho^2}
=1+2\sum_{k=1}^{\infty}\rho^k\cos k\theta.
$$
Combining these identities proves the displayed expansion and its uniform convergence.
:::

:::

::: pf-step
For every $n\geq 0$,
$$
C_n(a)=\boxed{\frac{2\pi}{\sqrt{a^2-1}}
\left(a-\sqrt{a^2-1}\right)^n}.
$$

::: pf-proof
By [](#poisson-expansion){.pf-ref}, termwise integration against $\cos n\theta$ is valid. If $n=0$, orthogonality gives
$$
C_0(a)=\frac1s\int_{-\pi}^{\pi}1\,d\theta=\frac{2\pi}{s}.
$$
If $n\geq 1$, then
$$
\int_{-\pi}^{\pi}\cos n\theta\cos k\theta\,d\theta
=\begin{cases}
\pi,&k=n,\\
0,&k\neq n,
\end{cases}
$$
and the constant term is orthogonal to $\cos n\theta$. Thus
$$
C_n(a)=\frac{2\rho^n}{s}\pi=\frac{2\pi\rho^n}{s}.
$$
Substituting $s=\sqrt{a^2-1}$ and $\rho=a-s$ gives the claimed formula, which also agrees with the $n=0$ case.
:::

:::

::: pf-step
For every $n\geq 0$,
$$
S_n(a)=\boxed{0}.
$$

::: pf-proof
The function $\theta\mapsto a-\cos\theta$ is even, while $\theta\mapsto\sin n\theta$ is odd. Hence the integrand defining $S_n(a)$ is odd on $[-\pi,\pi]$, so its integral is $0$.
:::

:::

:::

:::
