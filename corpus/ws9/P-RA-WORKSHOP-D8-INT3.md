---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-INT3
kind: problem
title: 'Reduce a Riemann–Stieltjes integral with a C1 integrator to a Riemann integral'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
  - differentiation
relations: []
review: draft
---

:::{.problem title="?"}
(Spring 2017, 7) Prove that if $f\in\mathcal R$ on $[a,b]$ and $\alpha\in C^1[a,b]$, then the Riemann integral
$$
\int_a^b f(x)\alpha'(x)\,dx
$$
exists and
$$
\int_a^b f(x)\,d\alpha(x)=\int_a^b f(x)\alpha'(x)\,dx.
$$
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove $\int_a^b f(x)\,d\alpha(x) = \int_a^b f(x)\alpha'(x)\,dx$ when $f \in \mathcal R[a,b]$ and $\alpha \in C^1[a,b]$.

<1>1. $f\alpha' \in \mathcal R[a,b]$.
    Proof: $f$ is Riemann integrable and $\alpha'$ is continuous (hence Riemann integrable), and the product of two Riemann integrable functions is Riemann integrable.

<1>2. For any partition $a = x_0 < \cdots < x_n = b$, compare the Stieltjes sum with a Riemann sum for $f\alpha'$.
    <2>1. $\sum_i f(t_i)\Delta\alpha_i = \sum_i f(t_i)\alpha'(s_i)\Delta x_i$ for suitable $s_i \in [x_{i-1}, x_i]$ (Mean Value Theorem applied to $\alpha$ on each subinterval, using $\Delta\alpha_i = \alpha(x_i) - \alpha(x_{i-1}) = \alpha'(s_i)\Delta x_i$).
        Proof: MVT for $\alpha \in C^1$ on $[x_{i-1}, x_i]$.
    <2>2. $\left|\sum_i f(t_i)(\alpha'(s_i) - \alpha'(t_i))\Delta x_i\right| \le \|f\|_\infty \cdot \omega_{\alpha'}(\|P\|) \cdot (b-a) \to 0$ as $\|P\| \to 0$.
        Proof: $\alpha'$ is uniformly continuous on $[a,b]$ (continuous on compact), so its modulus of continuity $\omega_{\alpha'}(\delta) \to 0$; and $|s_i - t_i| \le \|P\|$.
    <2>3. Q.E.D.
        Proof: <2>2 shows the Stieltjes sum with tags $t_i$ differs from $\sum f(t_i)\alpha'(t_i)\Delta x_i$ (a Riemann sum for $f\alpha'$ with the same partition and tags) by $\to 0$. Since the latter converges to $\int_a^b f\alpha'$ (Riemann integrability, <1>1), the former converges to the same value.

<1>3. The Stieltjes sums converge to $\int_a^b f(x)\alpha'(x)\,dx$, so $\int_a^b f\,d\alpha = \int_a^b f\alpha'$.
    Proof: <1>2 shows every sequence of Stieltjes sums (with mesh $\to 0$) converges to $\int f\alpha'$; by definition of the Riemann–Stieltjes integral this is $\int f\,d\alpha$.

<1>4. Q.E.D.
    Proof: <1>3 is the claim.

:::
