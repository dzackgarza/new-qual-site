---
schema: qual/card@1
id: P-I3DSE
kind: problem
title: Product of averages of $f$ and $1/f$ is at least $1$, and $\int_1^\infty 1/f=\infty$
  given $\int_1^t f\le t^2\log t$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 3 of the official UGA Fall 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reviewed and normalized the Cauchy--Schwarz/dyadic proof, replacing the legacy big-O notation by the required explicit harmonic lower bound.
---

::: {.problem}
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
\int_1^\infty {1\over f(x)}\dx = \infty
.\]

> Hint: write
\[  
\int_1^\infty {1\over f(x) }\dx = \sum_{k=0}^\infty \int_{2^k}^{2^{k+1}} {1 \over f(x)}\dx
.\]


:::

::: {.solution}

<1>1. Prove the product-of-averages inequality.
::: {.proof}
If either $\int_a^b f=\infty$ or $\int_a^b 1/f=\infty$, the asserted inequality is automatic in the extended sense. Otherwise $f>0$ almost everywhere on $[a,b]$. By Cauchy--Schwarz,
\[
(b-a)^2
=\left(\int_a^b f^{1/2}f^{-1/2}\,dx\right)^2
\le \left(\int_a^b f\,dx\right)
   \left(\int_a^b\frac{dx}{f(x)}\right).
\]
Dividing by $(b-a)^2$ gives
\[
1\le
\left(\frac1{b-a}\int_a^b f\right)
\left(\frac1{b-a}\int_a^b\frac1f\right).
\]
:::

<1>2. Apply the inequality on dyadic intervals.
::: {.proof}
Take
\[
a=2^k,\qquad b=2^{k+1},\qquad k\ge0.
\]
The hypothesis gives
\[
\int_{2^k}^{2^{k+1}}f(x)\,dx
\le \int_1^{2^{k+1}}f(x)\,dx
\le 2^{2(k+1)}(k+1)\log2.
\]
By Step 1,
\[
\int_{2^k}^{2^{k+1}}\frac{dx}{f(x)}
\ge
\frac{(2^{k+1}-2^k)^2}{\int_{2^k}^{2^{k+1}}f}
\ge \frac{1}{4(k+1)\log2}.
\]
Therefore
\[
\int_1^\infty\frac{dx}{f(x)}
=\sum_{k=0}^\infty
\int_{2^k}^{2^{k+1}}\frac{dx}{f(x)}
\ge \frac1{4\log2}\sum_{k=0}^\infty\frac1{k+1}
=\infty.
\]
:::
:::
