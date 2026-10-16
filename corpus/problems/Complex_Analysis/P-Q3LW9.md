---
schema: qual/card@1
id: P-Q3LW9
kind: problem
title: Polynomials cannot approximate $\bar z$ uniformly on $\partial\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomials
  - Power Series
relations: []
review: draft
---

::: {.problem}
Prove or disprove: there is a sequence of analytic polynomials $p_n$ such
that $p_n(z)\to\bar z$ uniformly for $z\in\partial\DD$.
:::

::: {.solution}
Such a sequence does not exist. On $|z|=1$, $\bar z=1/z$. If $p_n\to\bar z$ uniformly there,
then
\[
zp_n(z)\to1
\]
uniformly on $|z|=1$. By the maximum modulus principle applied to
$zp_n(z)-1$, the convergence would be uniform on the whole closed disk. But
at $z=0$ every term equals $-1$, a contradiction.
:::