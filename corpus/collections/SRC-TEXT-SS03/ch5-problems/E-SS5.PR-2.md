---
schema: qual/card@1
id: E-SS5.PR-2
kind: problem
title: Infinite Blaschke products from sequences satisfying the Blaschke condition
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
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

   This condition holds when $\{\alpha_n\}$ are the zeros of a bounded holomorphic function on the unit disc, by Problem 1. Show that the product

   $$
   f(z)=\prod_{n=1}^{\infty}
   \frac{\alpha_n-z}{1-\overline{\alpha_n}z}
   \frac{|\alpha_n|}{\alpha_n}
   $$

   converges uniformly for $|z|\leq r<1$ and defines a holomorphic function on the unit disc with precisely the zeros $\alpha_n$.
   Show also that $|f(z)|\leq 1$.
:::

::: solution
For part 1, write $\rho=|\alpha|$. Then
\[
\left|\frac{\alpha+\rho z}{(1-\overline\alpha z)\alpha}\right|
\le \frac{|\alpha|+\rho|z|}{|\alpha|(1-|\alpha||z|)}
=\frac{1+|z|}{1-\rho|z|}
\le \frac{1+r}{1-r}
\]
for $|z|\le r<1$.

Now put
\[
b_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}\frac{|\alpha|}{\alpha}.
\]
A direct calculation gives
\[
1-b_\alpha(z)
=(1-|\alpha|)\frac{\alpha+|\alpha|z}{\alpha(1-\overline\alpha z)}.
\]
Thus, for $|z|\le r<1$,
\[
|1-b_{\alpha_n}(z)|
\le \frac{1+r}{1-r}(1-|\alpha_n|).
\tag{1}
\]
The assumed Blaschke condition makes the right-hand side summable. Hence $\sum_n(1-b_{\alpha_n})$ converges uniformly on every closed disc $|z|\le r<1$. The standard infinite-product criterion therefore implies that
\[
\prod_{n=1}^\infty b_{\alpha_n}(z)
\]
converges uniformly on compact subsets to a holomorphic function $f$, and the limit is nonzero at every point at which none of the factors vanishes. Consequently the zeros of $f$ are precisely the $\alpha_n$, with multiplicity.

For $|z|<1$,
\[
\left|\frac{\alpha-z}{1-\overline\alpha z}\right|<1,
\]
because
\[
|1-\overline\alpha z|^2-|\alpha-z|^2
=(1-|\alpha|^2)(1-|z|^2)>0.
\]
Therefore every finite partial product has modulus at most $1$, and passing to the locally uniform limit gives $|f(z)|\le1$ on $\mathbb D$.
:::
