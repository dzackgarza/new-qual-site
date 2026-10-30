---
schema: qual/card@1
id: P-CAFA16H
kind: problem
title: 'An $L^2$ harmonic function on $\CC$ is zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $u: \CC \to \RR$ be a harmonic function such that $\iint \abs{u(x+iy)}^2 \, dx\,dy < \infty$.

(a) Prove that $u(a) = \frac{1}{\pi r^2} \iint_{B_r(a)} u(x+iy)\,dx\,dy$ for every $a \in \CC$ and $r > 0$.
Here $B_r(a) = \{z \in \CC : \abs{z - a} < r\}$.

(b) Prove that $u(z) = 0$ for every $z \in \CC$.
:::

::: {.solution}
For (a), the circle mean-value property gives, for every $0<s<r$,
$$
u(a)=\frac1{2\pi}\int_0^{2\pi}u(a+se^{i\theta})\,d\theta.
$$
Multiply by $2s$ and integrate from $s=0$ to $s=r$:
$$
r^2u(a)
=\frac1\pi\int_0^r\int_0^{2\pi}u(a+se^{i\theta})\,s\,d\theta\,ds.
$$
The double integral is the integral over $B_r(a)$, so
$$
u(a)=\frac1{\pi r^2}\iint_{B_r(a)}u(x+iy)\,dx\,dy.
$$

For (b), Cauchy--Schwarz gives
$$
\abs{u(a)}
\le \frac1{\pi r^2}
\left(\pi r^2\right)^{1/2}
\left(\iint_{B_r(a)}\abs{u}^2\right)^{1/2}
\le \frac{\norm{u}_{L^2(\CC)}}{\sqrt\pi\,r}.
$$
Letting $r\to\infty$ yields $u(a)=0$. Since $a$ was arbitrary, $u\equiv0$.
:::
