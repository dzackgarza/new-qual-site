---
schema: qual/card@1
id: E-SS5.PR-4
kind: exercise
title: Growth order of an entire function from its Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
---

::: exercise
Let

$$
F(z)=\sum_{n=0}^{\infty}a_nz^n
$$

be an entire function of finite order.
The growth order of $F$ is linked with the growth of the coefficients $a_n$ as $n\to\infty$.

1. Suppose that

   $$
   |F(z)|\leq Ae^{a|z|^\rho}.
   $$

   Show that

   $$
   \limsup_{n\to\infty}|a_n|^{1/n}n^{1/\rho}<\infty.
   \tag{8}
   $$

2. Conversely, if (8) holds, show that

   $$
   |F(z)|\leq A_\varepsilon e^{a_\varepsilon|z|^{\rho+\varepsilon}}
   $$

   for every $\varepsilon>0$.

*Hint.* For part 1, use Cauchy's inequality

$$
|a_n|\leq \frac{A}{r^n}e^{ar^\rho}
$$

and the fact that $u^{-n}e^{u^\rho}$, for $u>0$, has minimum

$$
e^{n/\rho}\left(\frac{\rho}{n}\right)^{n/\rho}
$$

at $u=n^{1/\rho}/\rho^{1/\rho}$.
Choose $r$ in terms of $n$ to attain this minimum.

For part 2, note that for $|z|=r$,

$$
|F(z)|
\leq \sum_n\frac{c^nr^n}{n^{n/\rho}}
\leq \sum_n\frac{c^nr^n}{(n!)^{1/\rho}}
$$

for some constant $c$, since $n^n\geq n!$.
This reduces the problem to Problem 3.
:::
