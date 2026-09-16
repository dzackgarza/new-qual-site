---
schema: qual/card@1
id: FF-VOO4Q
kind: fact
title: Residue at a pole of order $n$
prompts:
- State the residue formula at a pole of order $n$.
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.fact}
Let $n\ge1$, and let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc about $z_0$ with a [[D-AUD6K|pole]] of order at most $n$ at $z_0$.
Then the [[D-C3JIU|residue]] of $f$ at $z_0$ is
$$
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \frac{d^{n-1}}{dz^{n-1}}\qty{(z-z_0)^n f(z)}.
$$
:::
