---
schema: qual/card@1
id: P-URPZ4
kind: problem
title: The number of solutions of $6z^3+1=-e^z$ in $|z|<1$
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Find the number of solutions to the following equation on $\abs{z} < 1$:
\[
6z^3 + 1 = -e^z
.\]
:::

:::{.solution}
Write $f(z) \da 6z^3 + 1 + e^z$.

- Small: $m(z) = e^z + 1$
- Large: $M(z) = 6z^3$
- The estimate:
\[
\abs{m(z)} = \abs{e^z + 1} \leq e^{\Re(z)} + 1 \leq e^{\abs{z}} + 1 = e+1 < 6 = \abs{6z^3}
,\]
so $3 = Z_M = Z_f$.
:::

