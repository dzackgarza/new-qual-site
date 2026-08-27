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
Let $\Omega$ be a region with compact closure, $f$ holomorphic on $\Omega$ and continuous on $\cl\Omega$, and suppose $f$ is nowhere zero on $\Omega$.
Then $\abs f$ attains its minimum over $\cl\Omega$ on the boundary $\del\Omega$:
\[
\inf_{z\in\Omega}\abs{f(z)} \geq \inf_{z\in \del\Omega}\abs{f(z)}
.\]
Apply the maximum modulus principle to $1/f$, which is holomorphic exactly because $f$ does not vanish.
That hypothesis cannot be dropped: $f(z) = z$ on $\DD$ attains its minimum modulus at the interior point $0$.
:::

::: {.remark}
Stein and Shakarchi, *Complex Analysis*, Ch. 3 Theorem 4.5 and Corollary 4.6.
:::
