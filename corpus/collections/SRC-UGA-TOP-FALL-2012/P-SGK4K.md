---
schema: qual/card@1
id: P-SGK4K
kind: problem
title: Quotient of $S^2$ by collapsing a letter $A$ to a point
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Homotopy
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Fall 2012 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used the standard capital-A graph as the 1-skeleton of a two-face CW
    decomposition of S^2; collapsing that subcomplex leaves two 2-cells
    attached constantly to one point, hence S^2 wedge S^2.
---

::: {.problem}
Let $A$ denote a subset of points of $S^2$ that looks exactly like the capital letter A. Let $Q$ be the quotient of $S^2$ given by identifying all points of $A$ to a single point.

Show that $Q$ is homeomorphic to a familiar topological space and identify that space.
:::

::: {.solution}
<1>1. Regard the standard capital letter $A$ as a finite graph embedded in $S^2$.
Its complement has exactly two components, and each component is an open $2$-cell.
Thus $S^2$ has a CW decomposition whose $1$-skeleton is $A$ and whose remaining cells are two $2$-cells.
::: {.proof}
The graph $A$ consists of one simple closed cycle—the triangular loop formed by the two sloping sides and the crossbar—together with two pendant edges extending below the crossbar.
The simple closed cycle separates $S^2$ into two disks.
One of these disks is the region inside the triangular loop.
The two pendant edges lie in the other disk and form disjoint embedded slits from its boundary toward interior endpoints; the complement of these standard slits is again an open disk.
Hence the two components of $S^2\setminus A$ are open disks.

Taking the vertices and edges of the graph as the $0$- and $1$-cells and these two complementary disks as the open $2$-cells gives the asserted CW decomposition.
:::

<1>2. After collapsing $A$ to one point, $Q=S^2/A$ has a CW structure with one $0$-cell, no $1$-cells, and two $2$-cells, each attached by the constant map.
::: {.proof}
The subspace $A$ is the $1$-skeleton in <1>1, hence is a subcomplex.
For a CW pair $(X,A)$, the quotient $X/A$ inherits the cells of $X\setminus A$ together with one new $0$-cell representing the collapsed subcomplex.

Here the only cells outside $A$ are the two $2$-cells.
Their attaching maps originally have image in $A$; after $A$ is collapsed, both attaching maps
\[
S^1\longrightarrow A\longrightarrow A/A
\]
are constant.
:::

<1>3. A CW complex with one $0$-cell and two $2$-cells attached constantly is homeomorphic to
\[
\boxed{S^2\vee S^2}.
\]
::: {.proof}
Attaching a $2$-disk to a point by collapsing its entire boundary produces
\[
D^2/\partial D^2\cong S^2.
\]
Doing this for two disks with the same attaching point gives two copies of $S^2$ meeting exactly in that point, which is the wedge $S^2\vee S^2$.
By <1>2 this is precisely the quotient topology on $Q$.
:::
:::
