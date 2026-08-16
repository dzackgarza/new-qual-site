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
