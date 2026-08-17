---
schema: qual/card@1
id: P-RA19J4
kind: problem
title: 'UGA analysis qualifying exam, January 2019, problem 4'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - mean-value-theorem
relations: []
review: draft
---

:::{.problem title="?"}
Suppose that $f:[0,1]\to\mathbb R$ is differentiable and $f(0)=0$. Assume that there is a $k>0$ such that
$$|f'(x)|\le k|f(x)|$$
for all $x\in[0,1]$. Prove that $f(x)=0$ for all $x\in[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove $f \equiv 0$ on $[0,1]$, given $f$ differentiable with $f(0) = 0$ and $|f'(x)| \le k|f(x)|$ for $k > 0$.

<1>1. $|f(x)| \le k\int_0^x |f(t)|\,dt$ for every $x \in [0,1]$.
    <2>1. For a partition $0 = t_0 < \cdots < t_m = x$: $f(x) - f(0) = \sum_i [f(t_i) - f(t_{i-1})] = \sum_i f'(\xi_i)(t_i - t_{i-1})$ for suitable $\xi_i \in (t_{i-1}, t_i)$.
        Proof: the Mean Value Theorem on each subinterval.
    <2>2. $|f(x)| = |f(x) - f(0)| \le \sum_i |f'(\xi_i)|(t_i - t_{i-1}) \le k \sum_i |f(\xi_i)|(t_i - t_{i-1})$.
        Proof: <2>1, the triangle inequality, and the hypothesis $|f'| \le k|f|$.
    <2>3. As the partition is refined, $\sum_i |f(\xi_i)|(t_i - t_{i-1}) \to \int_0^x |f(t)|\,dt$.
        Proof: $|f|$ is continuous (since $f$ is differentiable, hence continuous), so its Riemann sums converge to its integral.
    <2>4. Q.E.D.
        Proof: <2>2–<2>3 give $|f(x)| \le k\int_0^x |f|$ (no integrability assumption on $f'$ needed).

<1>2. Iterate the bound: $|f(x)| \le M\frac{(kx)^n}{n!}$ for all $n$, where $M := \max_{[0,1]}|f|$.
    <2>1. Base case $n = 0$: $|f(x)| \le M$ trivially.
    <2>2. Induction step: if $|f(t)| \le M\frac{(kt)^{n-1}}{(n-1)!}$ for all $t \le x$, then $|f(x)| \le k\int_0^x M\frac{(kt)^{n-1}}{(n-1)!}\,dt = M\frac{(kx)^n}{n!}$.
        Proof: <1>1 then the induction hypothesis.
    <2>3. Q.E.D.
        Proof: <2>1–<2>2 by induction on $n$.

<1>3. $f \equiv 0$ on $[0,1]$.
    Proof: for fixed $x$, $\frac{(kx)^n}{n!} \to 0$ as $n \to \infty$ (factorial growth beats exponential), so <1>2 gives $|f(x)| \le M \cdot 0 = 0$; hence $f(x) = 0$ for all $x$.

<1>4. Q.E.D.
    Proof: <1>3 is the claim (the standard Grönwall bootstrap).

:::
