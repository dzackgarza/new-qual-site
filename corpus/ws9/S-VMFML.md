---
schema: qual/card@1
id: S-VMFML
kind: solution
title: Solution to P-YQDFJ
classification:
  areas:
  - real-analysis
  topics:
  - Variation
  - Continuity
relations:
- kind: solves
  target: P-YQDFJ
review: draft
---

:::{.solution}
Define $r(t)=(f(t),g(t))$. Then since on $\mathbb{R}^2$, $l_1^2$ norm is equivalent to $l_2^2$ norm, $r$ is a $\mathbb{R}^2$-valued function of BV, say whenever $0=x_0<x_1<\dots<x_n=b$, $\sum_{i=1}^n\|r(x_i)-r(x_{i-1})\|_2<\infty$. Suppose $[0,1]\times[0,1]$ can be covered. Divide $[0,1]\times[0,1]$ into $n^2-1$ small squares, with center $z_j$, in which the length of each edge is $1/n$. Then, we can choose $t_j$ such that $r(t_j)=z_j$ and reorder $t_j$ in increasing order i.e. $s_1<s_2<\dots<s_{n^2}$. Then, $\sum_{j=1}^{n^2-1}\|r(s_j)-r(s_{j+1})\|_2\ge\sum_{j=1}^{n^2-1}1/n=(n^2-1)/n=n-1/n\to\infty$. A contradiction.
:::
