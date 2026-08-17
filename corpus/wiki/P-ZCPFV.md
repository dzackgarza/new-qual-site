---
schema: qual/card@1
id: P-ZCPFV
kind: problem
title: $\int_a^b f\,d\alpha=\int_a^b f\alpha'\,dx$ when $f$ is Riemann integrable and $\alpha\in C^1[a,b]$
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Prove that if $f \in \mathcal{R}$ on $[a,b]$ and $\alpha \in C^1[a,b]$, then the Riemann integral $\int_a^b f(x)\alpha'(x)dx$ exists and $$\int_a^b f(x) d\alpha(x)= \int_a^b f(x)\alpha'(x)dx.$$
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $\alpha'$ is continuous, hence uniformly continuous and bounded on $[a,b]$; $\alpha$ is of bounded variation.
Proof: $\alpha \in C^1[a,b]$, so $\alpha'$ is continuous on the compact set $[a,b]$, hence uniformly continuous and bounded.
By the mean value theorem, for any partition the total variation of $\alpha$ is at most $\norm{\alpha'}_\infty (b-a) < \infty$.
<1>2. $f\alpha'$ is Riemann integrable on $[a,b]$.
Proof: $f$ is Riemann integrable, hence bounded and continuous a.e.; $\alpha'$ is continuous, hence Riemann integrable.
The product of two Riemann integrable functions is Riemann integrable, so $f\alpha' \in \mathcal{R}[a,b]$.
<1>3. Compare Riemann--Stieltjes sums to Riemann sums for $f\alpha'$.
Proof: let $P = \{a = x_0 < \cdots < x_n = b\}$ be a partition and pick tags $\xi_k \in [x_{k-1}, x_k]$.
By the mean value theorem applied to $\alpha$, there are $\eta_k \in [x_{k-1}, x_k]$ with $\alpha(x_k) - \alpha(x_{k-1}) = \alpha'(\eta_k)(x_k - x_{k-1})$.
Hence the Stieltjes sum is \[ S_P = \sum_k f(\xi_k)\big(\alpha(x_k) - \alpha(x_{k-1})\big) = \sum_k f(\xi_k)\alpha'(\eta_k)(x_k - x_{k-1}), \] which is a Riemann sum for $f\alpha'$ with tags $(\xi_k, \eta_k)$ in each subinterval.
<1>4. Such sums converge to $\int_a^b f\alpha'$.
Proof: since $f$ is bounded ($|f| \le B$) and $\alpha'$ is uniformly continuous, the difference between the sums in <1>3 and the ordinary Riemann sums $\sum_k f(\xi_k)\alpha'(\xi_k)(x_k-x_{k-1})$ tends to $0$ as the mesh goes to $0$: \[ \Big|\sum_k f(\xi_k)\big(\alpha'(\eta_k) - \alpha'(\xi_k)\big)\Delta x_k\Big| \le B \sum_k |\alpha'(\eta_k)-\alpha'(\xi_k)|\Delta x_k \le B\,(b-a)\,\omega_\alpha'(\text{mesh}) \to 0. \] Both sums converge to $\int_a^b f(x)\alpha'(x)\,dx$ (<1>2), so the Stieltjes sums converge to the same value.
<1>5. Conclude.
Proof: the Riemann--Stieltjes integral $\int_a^b f\,d\alpha$ exists (as $f$ is Riemann integrable and $\alpha$ is of bounded variation, <1>1) and equals the limit of the Stieltjes sums, which by <1>4 is $\int_a^b f(x)\alpha'(x)\,dx$.
<1>6. Q.E.D.
:::
