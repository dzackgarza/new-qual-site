---
schema: qual/card@1
id: P-OWBTK
kind: problem
title: "Let $R$ be a ring with the property that for every $a \\in R, a^2 = a$. Prove\u2026"
classification:
  areas:
  - algebra
  topics:
  - rings
  - characteristic
relations: []
review: draft
solved: true
---
Let $R$ be a ring with the property that for every $a \in R, a^2 = a$.

a.
Prove that $R$ has characteristic 2.

b.
Prove that $R$ is commutative.


:::{.strategy}
\envlist

- Just fiddle with direct computations.
- Context hint: that we should be considering things like $x^2$ and $a+b$.

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\[
2a  = (2a)^2 = 4a^2 = 4a \implies 2a = 0
.\]
Note that this implies $x = -x$ for all $x\in R$.
:::

:::{.proof title="of b"}
\[
a+b = (a+b)^2 &= a^2 + ab + ba + b^2 = a + ab + ba + b \\
&\implies ab + ba = 0 \\
&\implies ab = -ba \\
&\implies ab = ba \quad\text{by (a)}
.\]

:::

:::
