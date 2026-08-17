---
schema: qual/card@1
id: P-FFLLF
kind: problem
title: "Let $f: [0, 1]\\to \\RR$ be continuous, and prove the Weierstrass approx\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - stone-weierstrass
  - density
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: problem
> Note: (a) is a repeat.

Let $f: [0, 1]\to \RR$ be continuous, and prove the Weierstrass approximation theorem: for any $\eps> 0$ there exists a polynomial $P$ such that $\norm{f - P}_{\infty} < \eps$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Bernstein polynomial proof: for $f \in C([0,1])$ define $B_n(x) = \sum_{k=0}^n f(k/n)\binom{n}{k}x^k(1-x)^{n-k}$.
Proof: $B_n$ is a polynomial of degree $\le n$.

<1>2. $B_n(x) = \sum_{k=0}^n \left(f(k/n) - f(x)\right)\binom{n}{k}x^k(1-x)^{n-k} + f(x)$.
Proof: the binomial theorem gives $\sum_{k=0}^n \binom{n}{k}x^k(1-x)^{n-k} = 1$, so the $f(x)$ term factors out.

<1>3. For $x \in [0,1]$: $|B_n(x) - f(x)| \le \sum_{k=0}^n \left|f(k/n) - f(x)\right|\binom{n}{k}x^k(1-x)^{n-k}$.
Proof: triangle inequality in <1>2.

<1>4. Given $\eps > 0$, by uniform continuity of $f$ (Heine–Cantor) choose $\delta > 0$ with $|u - v| < \delta \Rightarrow |f(u) - f(v)| < \eps/2$.
Proof: $f$ is continuous on the compact interval $[0,1]$, hence uniformly continuous.

<1>5. Split the sum at $|k/n - x| < \delta$: <2>1. Terms with $|k/n - x| < \delta$ contribute $< \eps/2 \cdot \sum \binom{n}{k}x^k(1-x)^{n-k} = \eps/2$.
Proof: <1>4 and the binomial identity.
<2>2. Terms with $|k/n - x| \ge \delta$: their total probability weight is small, since $\sum_{|k/n - x| \ge \delta} \binom{n}{k}x^k(1-x)^{n-k} \le \frac{1}{n\delta^2}\sum_{k} (k-nx)^2\binom{n}{k}x^k(1-x)^{n-k} = \frac{x(1-x)}{n\delta^2} \le \frac{1}{4n\delta^2}$.
Proof: Chebyshev's inequality for the binomial distribution, whose variance is $nx(1-x) \le n/4$: $\sum_k (k-nx)^2\binom{n}{k}x^k(1-x)^{n-k} = nx(1-x)$.
<2>3. Those terms contribute $\le 2\|f\|_\infty \cdot \frac{1}{4n\delta^2} < \eps/2$ for $n > \frac{\|f\|_\infty}{\eps\delta^2}$.
Proof: $|f(k/n) - f(x)| \le 2\|f\|_\infty$ and <2>2.

<1>6. Q.E.D.: $|B_n(x) - f(x)| < \eps$ for all $x \in [0,1]$ and all large $n$.
Proof: <1>5<2>1 and <1>5<2>3 give $|B_n - f|_\infty < \eps$; $\eps$ was arbitrary, so polynomials are dense in $C([0,1])$ under $\|\cdot\|_\infty$.
:::
