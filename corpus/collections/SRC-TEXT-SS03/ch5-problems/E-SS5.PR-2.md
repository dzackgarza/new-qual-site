---
schema: qual/card@1
id: E-SS5.PR-2
kind: exercise
title: Infinite Blaschke products from sequences satisfying the Blaschke condition
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
relations: []
review: draft
---

::: exercise
In this problem, we discuss Blaschke products, which are bounded analogues in the disc of the Weierstrass products for entire functions.

1. Show that for $0<|\alpha|<1$ and $|z|\leq r<1$, the inequality

   $$
   \left|\frac{\alpha+|\alpha|z}{(1-\overline{\alpha}z)\alpha}\right|
   \leq \frac{1+r}{1-r}
   $$

   holds.

2. Let $\{\alpha_n\}$ be a sequence in the unit disc such that $\alpha_n\neq 0$ for all $n$ and

   $$
   \sum_{n=1}^{\infty}(1-|\alpha_n|)<\infty.
   $$

   This condition holds when $\{\alpha_n\}$ are the zeros of a bounded holomorphic function on the unit disc, by Problem 1.
   Show that the product

   $$
   f(z)=\prod_{n=1}^{\infty}
   \frac{\alpha_n-z}{1-\overline{\alpha_n}z}
   \frac{|\alpha_n|}{\alpha_n}
   $$

   converges uniformly for $|z|\leq r<1$ and defines a holomorphic function on the unit disc with precisely the zeros $\alpha_n$.
   Show also that $|f(z)|\leq 1$.
:::
