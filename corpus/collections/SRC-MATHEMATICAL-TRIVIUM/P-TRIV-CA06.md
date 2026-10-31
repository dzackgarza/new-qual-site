---
schema: qual/card@1
id: P-TRIV-CA06
kind: problem
title: Laurent series of $z/((z+1)(z-1))$ about $z=1$
classification:
  areas: [complex-analysis]
  topics:
  - Laurent Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the Laurent series of $f(z) = \frac{z}{(z + 1)(z - 1)}$ around $z_0 = 1$; give the region of convergence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function has the partial-fraction decomposition
$$
\frac{z}{(z+1)(z-1)}
=
\frac12\frac1{z-1}
+
\frac12\frac1{z+1}.
$$


::: pf-proof

Write
$$
\frac{z}{(z+1)(z-1)}
=
\frac{A}{z-1}+\frac{B}{z+1}.
$$
Then
$$
z=A(z+1)+B(z-1).
$$
Setting $z=1$ gives $A=1/2$, and setting $z=-1$ gives $B=1/2$.

:::

:::

::: {.pf-step #s1-2}

For
$$
\abs{z-1}<2,
$$
one has
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}(z-1)^n.
$$


::: pf-proof

Since
$$
z+1
=
2+(z-1)
=
2\left(1+\frac{z-1}{2}\right),
$$
one has
$$
\frac1{z+1}
=
\frac12
\frac1{1+(z-1)/2}.
$$
The geometric series
$$
\frac1{1+w}
=
\sum_{n=0}^{\infty}(-1)^n w^n
$$
converges for $\abs{w}<1$. Take $w=(z-1)/2$.

:::

:::

::: {.pf-step #s1-3}

Therefore the Laurent series of $f$ about $z=1$ is
$$
\boxed{
\frac{z}{(z+1)(z-1)}
=
\frac1{2(z-1)}
+
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+2}}(z-1)^n.
}
$$


::: pf-proof

Substitute the expansion from step [](#s1-2){.pf-ref} into the decomposition from
step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The region of convergence is
$$
\boxed{
0<\abs{z-1}<2.
}
$$


::: pf-proof

The center $z=1$ is a simple pole, so it must be excluded. The geometric
series from step [](#s1-2){.pf-ref} converges exactly for $\abs{z-1}<2$. The boundary point
$z=-1$ is a singularity of the original function and lies at distance $2$
from the center, so the outer radius cannot be enlarged.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give the Laurent series and its exact annulus of
convergence.

:::

:::

:::
