---
schema: qual/card@1
id: P-ZCPFV
kind: problem
title: $\int_a^b f\,d\alpha=\int_a^b f\alpha'\,dx$ when $f$ is Riemann integrable
  and $\alpha\in C^1[a,b]$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that if $f \in \mathcal{R}$ on $[a,b]$ and $\alpha \in C^1[a,b]$, then the Riemann integral $\int_a^b f(x)\alpha'(x)dx$ exists and $$\int_a^b f(x) d\alpha(x)= \int_a^b f(x)\alpha'(x)dx.$$
:::
::: {.solution}
<1>1. The product $f\alpha'$ is Riemann integrable on $[a,b]$.

::: {.proof}
The derivative $\alpha'$ is continuous on compact $[a,b]$, hence bounded and Riemann integrable. Since $f$ is Riemann integrable, the product theorem for Riemann-integrable functions gives $f\alpha'\in\mathcal R[a,b]$.
:::

<1>2. For every tagged partition $(P,\xi)$, the difference between its Stieltjes sum and the Riemann sum for $f\alpha'$ with the same tags is bounded by
\[
\left|S_\alpha(f;P,\xi)-S(f\alpha';P,\xi)\right|
\le B(b-a)\,\omega_{\alpha'}(\operatorname{mesh}P),
\]
where $B=\sup_{[a,b]}|f|$ and $\omega_{\alpha'}(\delta)=\sup\{|\alpha'(s)-\alpha'(t)|:s,t\in[a,b],\,|s-t|\le\delta\}$.

::: {.proof}
For $P=(a=x_0<\cdots<x_m=b)$, the mean value theorem supplies $\eta_i\in(x_{i-1},x_i)$ with
\[
\alpha(x_i)-\alpha(x_{i-1})=\alpha'(\eta_i)(x_i-x_{i-1}).
\]
The difference between the two sums equals
\[
\sum_{i=1}^m f(\xi_i)(\alpha'(\eta_i)-\alpha'(\xi_i))(x_i-x_{i-1}).
\]
Taking absolute values and using $|\eta_i-\xi_i|\le\operatorname{mesh}P$ yields the claimed bound after summing the subinterval lengths to $b-a$.
:::

<1>3. The difference in step <1>2 tends uniformly to zero over all tagged partitions as their mesh tends to zero.

::: {.proof}
Uniform continuity of $\alpha'$ on $[a,b]$ gives $\omega_{\alpha'}(\delta)\to0$ as $\delta\downarrow0$. The bound in step <1>2 is independent of the choice of partition tags, so the convergence is uniform.
:::

<1>4. The Riemann–Stieltjes integral exists and satisfies
\[
\boxed{\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx}.
\]

::: {.proof}
By step <1>1, the tagged Riemann sums $S(f\alpha';P,\xi)$ converge to $I=\int_a^b f(x)\alpha'(x)\,dx$ as the mesh tends to zero, uniformly over all choices of tags. Steps <1>2–<1>3 show that the corresponding tagged Stieltjes sums converge to the same $I$. This is the tagged-sum criterion for Riemann–Stieltjes integrability and identifies the integral.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>4 establish both requested assertions.
:::
