---
schema: qual/card@1
id: P-V7ULH
kind: problem
title: A power series has an expansion about every point of its disc of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.problem}
Let $f(z) = \sum_{n=0}^\infty a_n z^n$ be a power series centered at the origin with radius of convergence $R > 0$. Prove that $f$ has a power series expansion about any point $z_0$ in its disc of convergence $D_R(0)$.
:::

::: {.solution}
Fix $z_0 \in D_R(0)$ and $r$ with $0 < r < R - \abs{z_0}$. Choose $\rho$ with $\abs{z_0} + r < \rho < R$, and let $\Gamma$ be the circle $\abs{\xi} = \rho$, oriented counterclockwise.

<1>1. The function $f$ is holomorphic on $D_R(0)$, and every $z \in D_r(z_0)$ lies inside $\Gamma$.

::: {.proof}
A power series converges uniformly on compact subsets of its open disc of convergence, and its sum is holomorphic there. For $z \in D_r(z_0)$, the triangle inequality gives $\abs{z} \le \abs{z_0} + \abs{z - z_0} < \abs{z_0} + r < \rho$.
:::

<1>2. For every $z \in D_r(z_0)$,
$$f(z) = \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{\xi - z} \, d\xi.$$

::: {.proof}
By step <1>1, $f$ is holomorphic on $D_R(0)\supset\overline{D}_\rho(0)$ and $z$ lies inside $\Gamma$, so Cauchy's integral formula applies.
:::

<1>3. For every $z \in D_r(z_0)$, the series
$$\frac{f(\xi)}{\xi - z} = \sum_{k=0}^\infty \frac{f(\xi)}{(\xi - z_0)^{k+1}} (z - z_0)^k$$
converges uniformly for $\xi \in \Gamma$.

::: {.proof}
For $\xi\in\Gamma$,
$$\frac{1}{\xi - z} = \frac{1}{\xi - z_0} \cdot \frac{1}{1 - \frac{z - z_0}{\xi - z_0}}
\qquad\text{and}\qquad
\abs{\xi - z_0} \ge \abs{\xi} - \abs{z_0} = \rho - \abs{z_0}.$$
Hence
$$\left| \frac{z - z_0}{\xi - z_0} \right| \le c \coloneqq \frac{r}{\rho - \abs{z_0}} < 1,$$
and the Weierstrass $M$-test with $M_k=c^k$ shows that the geometric series $\sum_k \bigl(\frac{z - z_0}{\xi - z_0}\bigr)^k$ converges uniformly on $\Gamma$. Multiplying by $f(\xi)/(\xi - z_0)$, which is bounded on $\Gamma$, preserves uniform convergence.
:::

<1>4. For every $z \in D_r(z_0)$,
$$f(z) = \sum_{k=0}^\infty b_k (z - z_0)^k,
\qquad
b_k = \frac{1}{2\pi i} \oint_\Gamma \frac{f(\xi)}{(\xi - z_0)^{k+1}} \, d\xi = \frac{f^{(k)}(z_0)}{k!}.$$

::: {.proof}
Substitute step <1>3 into step <1>2 and integrate term by term, which uniform convergence on $\Gamma$ permits. The second formula for $b_k$ is Cauchy's integral formula for derivatives.
:::

<1>5. Q.E.D.

::: {.proof}
The coefficients $b_k = f^{(k)}(z_0)/k!$ do not depend on $r$. Since $r < R - \abs{z_0}$ was arbitrary, step <1>4 gives the expansion $f(z) = \sum_{k} b_k (z - z_0)^k$ on the whole disc $D_{R - \abs{z_0}}(z_0)$.
:::
:::
