---
schema: qual/card@1
id: P-K4EJA
kind: problem
title: "Let $f$ be a non-negative Lebesgue measurable function on $[1, \\infty)$.\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $f$ be a non-negative Lebesgue measurable function on $[1, \infty)$.

a.
Prove that
\[  
1 \leq \qty{
{1 \over b-a} \int_a^b f(x) \,dx
}\qty{
{1\over b-a} \int_a^b {1 \over f(x)}\, dx
}
\]
for any $1\leq a < b <\infty$.

b.
Prove that if $f$ satisfies
\[  
\int_1^t f(x) \, dx \leq t^2 \log(t)
\]
for all $t\in [1, \infty)$, then
\[  
\int_1^\infty {1\over f(x) \,dx} = \infty
.\]

> Hint: write
\[  
\int_1^\infty {1\over f(x) \, dx} = \sum_{k=0}^\infty \int_{2^k}^{2^{k+1}} {1 \over f(x)}\,dx
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Setup:** the expression $1/f$ presumes $f > 0$ a.e. on the intervals considered; where $f = 0$ on a set of positive measure the right-hand factor is $+\infty$ and the inequalities hold in the extended sense. Assume $f > 0$ a.e. for the proofs.

<1>1. For $1 \le a < b < \infty$: $\left(\frac{1}{b-a}\int_a^b f\right)\left(\frac{1}{b-a}\int_a^b \frac{1}{f}\right) \ge 1$.
    <2>1. By Cauchy–Schwarz, $\left(\int_a^b \sqrt{f}\cdot\frac{1}{\sqrt{f}}\right)^2 \le \left(\int_a^b f\right)\left(\int_a^b \frac{1}{f}\right)$.
        Proof: Cauchy–Schwarz applied to $g = \sqrt f$ and $h = 1/\sqrt f$, which are in $L^2([a,b])$ (locally, $f$ and $1/f$ are integrable on the bounded interval $[a,b]$).
    <2>2. The left side equals $(b-a)^2$.
        Proof: $\sqrt f \cdot 1/\sqrt f = 1$, so the integral is $b - a$.
    <2>3. Q.E.D.
        Proof: divide <2>2's identity into <2>1 and divide by $(b-a)^2$.

<1>2. If $\int_1^t f \le t^2 \log t$ for all $t \ge 1$, then $\int_1^\infty \frac{dx}{f(x)} = \infty$.
    <2>1. Write $\int_1^\infty \frac{dx}{f(x)} = \sum_{k=0}^\infty \int_{2^k}^{2^{k+1}}\frac{dx}{f(x)}$.
        Proof: the intervals $[2^k, 2^{k+1}]$ partition $[1, \infty)$.
    <2>2. For each $k$: $\int_{2^k}^{2^{k+1}}\frac{dx}{f(x)} \ge \frac{2^{2k}}{\int_{2^k}^{2^{k+1}} f(x)\,dx}$.
        Proof: <1>1 with $a = 2^k$, $b = 2^{k+1}$, so $b - a = 2^k$: $\left(\frac{1}{2^k}\int_{2^k}^{2^{k+1}}f\right)\left(\frac{1}{2^k}\int_{2^k}^{2^{k+1}}\frac{1}{f}\right) \ge 1$.
    <2>3. $\int_{2^k}^{2^{k+1}} f(x)\,dx \le \int_1^{2^{k+1}} f(x)\,dx \le (2^{k+1})^2\log(2^{k+1}) = 4\cdot 2^{2k}(k+1)\log 2$.
        Proof: the hypothesis with $t = 2^{k+1}$.
    <2>4. $\int_{2^k}^{2^{k+1}}\frac{dx}{f(x)} \ge \frac{2^{2k}}{4\cdot 2^{2k}(k+1)\log 2} = \frac{1}{4(k+1)\log 2}$.
        Proof: <2>2 and <2>3.
    <2>5. $\int_1^\infty \frac{dx}{f(x)} \ge \sum_{k=0}^\infty \frac{1}{4(k+1)\log 2} = \infty$.
        Proof: <2>1, <2>4, and divergence of the harmonic series.
    <2>6. Q.E.D.
        Proof: <2>5.
:::
