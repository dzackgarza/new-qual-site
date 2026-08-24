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
---

:::{.problem title="?"}
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

:::{.solution}
**Part 1**:
By Holder with $p=q=2$ on $L_1[a, b]$,
\[
(b-a)^2 = \norm{\id}_1^2 = \norm{f^{1\over 2}f^{- {1\over 2} } }_1^2 \leq \norm{f^{1\over 2}}_2^2 \cdot \norm{f^{-{1\over 2}}}_2^2 = \int_a^b f(x)\dx \cdot \int_a^b {1\over f(x)}\dx
.\]

**Part 2**:
It suffices to show 
\[
\int_{2^k}^{2^{k+1}}{1\over f} > c_k \text{ where } \sum_{k\geq 0} c_k = \infty
.\]
Manipulate the given inequality a bit:
\[
\int_a^b f \leq \int_1^b f \leq b^2 \log(b) \implies 
\qty{\int_a^b f}\inv \geq {1\over b^2\log(b)}\\
\implies 
.\]
Rewrite the bound in part 1:
\[
\int_a^b {1\over f} \geq \qty{\int_a^b f}\inv (b-a)^2 \geq {(b-a)^2 \over b^2 \log(b) }
.\]
Now set $a=2^k, b=2^{k+1}$:
\[
\int_{2^k}^{2^{k+1}} {1\over f(x)} \dx
\geq
{(2^{k+1} - 2^k )^2 \over 2^{2(k+1)} (k+1)\log(2) }
= {2^{2k} \over 2^{2k} \cdot 4(k+1)\log(2)}
= \bigo(1/k)
,\]
and $\sum 1/k = \infty$.
:::

