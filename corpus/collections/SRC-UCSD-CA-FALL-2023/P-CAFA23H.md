---
schema: qual/card@1
id: P-CAFA23H
kind: problem
title: "Nowhere-zero entire function with integrable log-modulus is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be a nowhere zero analytic function on the entire complex plane $\CC$ and write $u(z) = \log|f(z)|$.
Assume $|u|$ is Lebesgue integrable: $\int_{\CC} |u(z)|\,dx\,dy < +\infty$, where $z = x + iy$.
Prove $f$ is constant.
What is the value of $f$?
:::

::: {.solution}
Because $f$ is entire and nowhere zero and $\CC$ is simply connected,
$f$ has an entire logarithm. In particular
$$
u(z)=\log|f(z)|
$$
is harmonic on all of $\CC$.

Let
$$
L=\int_{\CC}|u(z)|\,dA(z)<\infty.
$$
For any $a\in\CC$ and $R>0$, the mean-value property gives
$$
|u(a)|
\le \frac1{\pi R^2}
\int_{D(a,R)}|u(z)|\,dA(z)
\le \frac{L}{\pi R^2}.
$$
Letting $R\to\infty$ yields $u(a)=0$. Thus
$$
|f(z)|=1
\qquad(z\in\CC).
$$
Liouville's theorem, or the open mapping theorem, now shows that $f$ is
constant. Its value can be any constant of modulus one:
$$
\boxed{f(z)\equiv c,\qquad |c|=1.}
$$
:::
