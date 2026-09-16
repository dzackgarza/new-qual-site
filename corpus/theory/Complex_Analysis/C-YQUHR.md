---
schema: qual/card@1
id: C-YQUHR
kind: corollary
title: Minimum modulus principle
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: {.corollary}
Let $\Omega\subseteq\CC$ be a bounded connected open set, and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, continuous on $\overline\Omega$, and nowhere zero on $\Omega$.
Then
$$
\min_{z\in\overline\Omega}\abs{f(z)}=\min_{z\in\bd\Omega}\abs{f(z)}.
$$
:::

::: {.proof}
If $f$ vanishes at a point of $\bd\Omega$, both minima are $0$.
Otherwise $f$ is nowhere zero on $\overline\Omega$, and the function $1/f$ is holomorphic on $\Omega$ and continuous on $\overline\Omega$, so by the [[C-GM57K|maximum modulus principle]], $\max_{\overline\Omega}\abs{1/f}=\max_{\bd\Omega}\abs{1/f}$.
:::

::: {.example}
The hypothesis that $f$ has no zeros is needed: $f(z)=z$ on $\DD$ has $\min_{\overline\DD}\abs{f}=0$, attained only at the interior point $0$, while $\abs{f}=1$ on $\bd\DD$.
:::

::: {.remark}
Stein--Shakarchi, *Complex Analysis*, Chapter 3, Theorem 4.5 and Corollary 4.6.
:::
