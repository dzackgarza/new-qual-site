---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-SEQ4
kind: problem
title: 'Uniform convergence and differentiability of a logarithmic-type series'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-functions
  - uniform-convergence
  - differentiation
relations: []
review: draft
---

:::{.problem title="?"}
Let $f_n:[0,1)\to\mathbb R$ be the function defined by
$$
f_n(x):=\sum_{k=1}^{n}\frac{x^k}{1+x^k}.
$$

(a) Prove that $f_n$ converges to a function $f:[0,1)\to\mathbb R$.

(b) Prove that for every $0<a<1$ the convergence is uniform on $[0,a]$.

(c) Prove that $f$ is differentiable on $(0,1)$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** For $f_n(x) = \sum_{k=1}^{n}\frac{x^k}{1+x^k}$ on $[0,1)$: (a) show $f_n$ converges to some $f$; (b) uniform convergence on $[0,a]$ for $0 < a < 1$; (c) $f$ differentiable on $(0,1)$.

<1>1. (a) $f_n \to f$ pointwise on $[0,1)$.
    Proof: for $0 \le x < 1$, $\frac{x^k}{1+x^k} \le x^k$ and $\sum_k x^k$ converges (geometric, ratio $x < 1$); by comparison $\sum_k \frac{x^k}{1+x^k}$ converges for each $x$, so $f_n(x) \to f(x) := \sum_{k=1}^\infty \frac{x^k}{1+x^k}$.

<1>2. (b) Uniform convergence on $[0,a]$, $0 < a < 1$.
    Proof: for $x \in [0,a]$, $\frac{x^k}{1+x^k} \le x^k \le a^k$ and $\sum a^k < \infty$ since $a < 1$; the Weierstrass M-test with $M_k = a^k$ gives uniform convergence on $[0,a]$.

<1>3. (c) $f$ is differentiable on $(0,1)$.
    <2>1. Each term $g_k(x) = \frac{x^k}{1+x^k}$ is differentiable on $(0,1)$ with $g_k'(x) = \frac{kx^{k-1}}{(1+x^k)^2}$.
        Proof: quotient rule.
    <2>2. $\sum_k g_k'$ converges uniformly on every compact $[\delta, a] \subset (0,1)$.
        Proof: for $x \in [\delta, a]$, $|g_k'(x)| = \frac{kx^{k-1}}{(1+x^k)^2} \le kx^{k-1} \le k a^{k-1}$; and $\sum_{k\ge 1} k a^{k-1} = \frac{1}{(1-a)^2} < \infty$ (derivative of the geometric series, valid for $a < 1$). The M-test applies with $M_k = ka^{k-1}$.
    <2>3. $f$ is differentiable on each $[\delta, a]$ with $f' = \sum_k g_k'$.
        Proof: standard theorem for series of functions: if $\sum g_k$ converges pointwise and $\sum g_k'$ converges uniformly on an interval, then the sum is differentiable and its derivative is $\sum g_k'$.
    <2>4. $f$ is differentiable on all of $(0,1)$.
        Proof: every $x_0 \in (0,1)$ lies in some compact subinterval $[\delta, a] \subset (0,1)$, where <2>3 applies.
    <2>5. Q.E.D.
        Proof: <2>1–<2>4 prove (c).

:::
