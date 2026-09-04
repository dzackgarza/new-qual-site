---
schema: qual/card@1
id: P-YCZ6A
kind: problem
title: Homology of $S^2\times S^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
Compute the homology groups of $S^2 \times S^2$.
:::

::: {.solution}
<1>1. Give each factor $S^2$ the CW structure with one $0$-cell and one $2$-cell.
Then $S^2\times S^2$ has one $0$-cell, two $2$-cells, and one $4$-cell, and no cells in any other dimension.
::: {.proof}
Write the cells of either copy of $S^2$ as $e^0$ and $e^2$.
The product CW structure has one cell $e^i\times e^j$ of dimension $i+j$ for each pair of cells from the two factors.
Thus its cells are
\[
e^0\times e^0,
\qquad
e^2\times e^0,
\qquad
e^0\times e^2,
\qquad
e^2\times e^2,
\]
of dimensions $0,2,2,4$, respectively.
:::

<1>2. The cellular chain complex of $S^2\times S^2$ is
\[
0\longrightarrow \ZZ
\xrightarrow{0}0
\xrightarrow{0}\ZZ^2
\xrightarrow{0}0
\xrightarrow{0}\ZZ
\longrightarrow0.
\]
::: {.proof}
By <1>1,
\[
C_k(S^2\times S^2;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,4,\\
\ZZ^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
Every cellular differential decreases degree by one.
Since $C_1=C_3=0$, the only differentials leaving nonzero chain groups have zero target, so all cellular differentials vanish.
:::

<1>3. Therefore
\[
H_k(S^2\times S^2;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,4,\\
\ZZ^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Cellular homology is the homology of the complex in <1>2. Because every differential there is zero, each homology group is the corresponding cellular chain group.
:::
:::
