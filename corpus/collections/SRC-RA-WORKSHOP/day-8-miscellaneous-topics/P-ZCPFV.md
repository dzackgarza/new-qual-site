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

Since $\alpha$ need not be monotone, the Riemann–Stieltjes integral is the limit of tagged sums $S_\alpha(f;P,\xi)=\sum_i f(\xi_i)(\alpha(x_i)-\alpha(x_{i-1}))$ as the mesh tends to zero.

::: pf

::: {.pf-step #s1}

The product $f\alpha'$ is Riemann integrable on $[a,b]$.

::: pf-proof

The derivative $\alpha'$ is continuous on compact $[a,b]$, hence bounded and Riemann integrable.
Since $f$ is Riemann integrable, the product theorem for Riemann-integrable functions gives $f\alpha'\in\mathcal R[a,b]$.

:::

:::

::: {.pf-step #s2}

For every tagged partition $(P,\xi)$, the difference between its Stieltjes sum and the Riemann sum for $f\alpha'$ with the same tags is bounded by
$$
\abs{S_\alpha(f;P,\xi)-S(f\alpha';P,\xi)}
\le B(b-a)\,\omega_{\alpha'}(\operatorname{mesh}P),
$$
where $B=\sup_{[a,b]}\abs{f}$ and $\omega_{\alpha'}(\delta)=\sup\{\abs{\alpha'(s)-\alpha'(t)}:s,t\in[a,b],\,\abs{s-t}\le\delta\}$.

::: pf-proof

For $P=(a=x_0<\cdots<x_m=b)$, the mean value theorem supplies $\eta_i\in(x_{i-1},x_i)$ with
$$
\alpha(x_i)-\alpha(x_{i-1})=\alpha'(\eta_i)(x_i-x_{i-1}).
$$
The difference between the two sums equals
$$
\sum_{i=1}^m f(\xi_i)(\alpha'(\eta_i)-\alpha'(\xi_i))(x_i-x_{i-1}).
$$
Taking absolute values and using $\abs{\eta_i-\xi_i}\le\operatorname{mesh}P$ yields the claimed bound after summing the subinterval lengths to $b-a$.

:::

:::

::: {.pf-step #s3}

The difference in step [](#s2){.pf-ref} tends uniformly to zero over all tagged partitions as their mesh tends to zero.

::: pf-proof

Uniform continuity of $\alpha'$ on $[a,b]$ gives $\omega_{\alpha'}(\delta)\to0$ as $\delta\downarrow0$.
The bound in step [](#s2){.pf-ref} is independent of the choice of partition tags, so the convergence is uniform.

:::

:::

::: pf-step

The Riemann–Stieltjes integral exists and $\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx$.

::: pf-proof

By step [](#s1){.pf-ref}, the tagged Riemann sums $S(f\alpha';P,\xi)$ converge to $I=\int_a^b f(x)\alpha'(x)\,dx$ as the mesh tends to zero, uniformly over all choices of tags.
Step [](#s2){.pf-ref} and step [](#s3){.pf-ref} show that the corresponding tagged Stieltjes sums converge to the same $I$.
This is the tagged-sum criterion for Riemann–Stieltjes integrability and identifies the integral.

:::

:::

:::

:::
