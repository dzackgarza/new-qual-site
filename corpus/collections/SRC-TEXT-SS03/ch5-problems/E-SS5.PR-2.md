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

::: {.exercise}
In this problem, we discuss Blaschke products, which are bounded analogues in the disc of the Weierstrass products for entire functions.

1. Show that for $0<\abs{\alpha}<1$ and $\abs{z}\leq r<1$, the inequality

   $$
   \abs{\frac{\alpha+\abs{\alpha}z}{(1-\overline{\alpha}z)\alpha}}
   \leq \frac{1+r}{1-r}
   $$

   holds.

2. Let $\{\alpha_n\}$ be a sequence in the unit disc such that $\alpha_n\neq 0$ for all $n$ and

   $$
   \sum_{n=1}^{\infty}(1-\abs{\alpha_n})<\infty.
   $$

   This condition holds when $\{\alpha_n\}$ are the zeros of a bounded holomorphic function on the unit disc, by Problem 1. Show that the product

   $$
   f(z)=\prod_{n=1}^{\infty}
   \frac{\alpha_n-z}{1-\overline{\alpha_n}z}
   \frac{\abs{\alpha_n}}{\alpha_n}
   $$

   converges uniformly for $\abs{z}\leq r<1$ and defines a holomorphic function on the unit disc with precisely the zeros $\alpha_n$.
   Show also that $\abs{f(z)}\leq 1$.
:::

::: {.solution}
For part 1, write $\rho=\abs{\alpha}$. Then
$$
\abs{\frac{\alpha+\rho z}{(1-\overline\alpha z)\alpha}}
\le \frac{\abs{\alpha}+\rho\abs{z}}{\abs{\alpha}(1-\abs{\alpha}\abs{z})}
=\frac{1+\abs{z}}{1-\rho\abs{z}}
\le \frac{1+r}{1-r}
$$
for $\abs{z}\le r<1$.

Now put
$$
b_\alpha(z)=\frac{\alpha-z}{1-\overline\alpha z}\frac{\abs{\alpha}}{\alpha}.
$$
A direct calculation gives
$$
1-b_\alpha(z)
=(1-\abs{\alpha})\frac{\alpha+\abs{\alpha}z}{\alpha(1-\overline\alpha z)}.
$$
Thus, for $\abs{z}\le r<1$,
$$
\abs{1-b_{\alpha_n}(z)}
\le \frac{1+r}{1-r}(1-\abs{\alpha_n}).
\tag{1}
$$
The assumed Blaschke condition makes the right-hand side summable. Hence $\sum_n(1-b_{\alpha_n})$ converges uniformly on every closed disc $\abs{z}\le r<1$. The standard infinite-product criterion therefore implies that
$$
\prod_{n=1}^\infty b_{\alpha_n}(z)
$$
converges uniformly on compact subsets to a holomorphic function $f$, and the limit is nonzero at every point at which none of the factors vanishes. Consequently the zeros of $f$ are precisely the $\alpha_n$, with multiplicity.

For $\abs{z}<1$,
$$
\abs{\frac{\alpha-z}{1-\overline\alpha z}}<1,
$$
because
$$
\abs{1-\overline\alpha z}^2-\abs{\alpha-z}^2
=(1-\abs{\alpha}^2)(1-\abs{z}^2)>0.
$$
Therefore every finite partial product has modulus at most $1$, and passing to the locally uniform limit gives $\abs{f(z)}\le1$ on $\DD$.
:::
