---
schema: qual/card@1
id: P-OSUVG
kind: problem
title: A function in $L^2([0,1])$ orthogonal to every polynomial vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Let $f\in L^2([0, 1])$ and suppose
$$
\int_{[0,1]} f(x) x^{n} d x=0 \text { for all integers } n \geq 0.
$$
Show that $f = 0$ almost everywhere.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

1. By linearity of the integral, the assumption implies that for any polynomial $P(x) \in \RR[x]$:
$$
\int_0^1 f(x) P(x) \, dx = 0.
$$

2. By the **Stone-Weierstrass theorem**, the algebra of polynomials is uniformly dense in $C([0, 1])$.
   Thus, for any continuous function $g \in C([0, 1])$, there exists a sequence of polynomials $P_k \to g$ uniformly on $[0, 1]$.
   Since $f \in L^2([0, 1]) \subset L^1([0, 1])$, by the bounded convergence theorem (or Cauchy-Schwarz inequality):
$$
\left| \int_0^1 f(x) g(x) \, dx - \int_0^1 f(x) P_k(x) \, dx \right| \leq \|f\|_{L^1} \|g - P_k\|_\infty \to 0,
$$
which implies:
$$
\int_0^1 f(x) g(x) \, dx = 0 \quad \text{for all } g \in C([0, 1]).
$$

3. Since $C([0, 1])$ is dense in $L^2([0, 1])$ under the $L^2$-norm, there exists a sequence $g_k \in C([0, 1])$ such that $g_k \to f$ in $L^2([0, 1])$.
   Using the continuity of the $L^2$ inner product:
$$
\|f\|_{L^2}^2 = \langle f, f \rangle = \lim_{k \to \infty} \langle f, g_k \rangle = \lim_{k \to \infty} \int_0^1 f(x) g_k(x) \, dx = 0.
$$

4. Since $\|f\|_{L^2} = 0$, it follows that $f(x) = 0$ almost everywhere on $[0, 1]$.
:::
