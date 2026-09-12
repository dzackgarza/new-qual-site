---
schema: qual/card@1
id: P-AMD-QVJXODCH
kind: problem
title: Topological degree of $p(z)=\frac{\prod_i^n(z-a_i)}{\prod_j^m(z-b_j)}$
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
---

::: {.problem}
Let $p(z) = \frac{\prod_i^n z-a_i}{\prod_j^m z-b_j}$ with all $a_i, b_j$ distinct.
What is its topological degree?
:::

::: {.solution}
<1>1. Interpreting $p$ as a rational map of the Riemann sphere,
$$
p:\mathbb{CP}^1\longrightarrow\mathbb{CP}^1,
$$
its topological degree is
$$
\boxed{\max\{n,m\}}.
$$
::: {.proof}
Write $P(z)=\prod_{i=1}^n(z-a_i)$ and $Q(z)=\prod_{j=1}^m(z-b_j)$. Since all $a_i,b_j$ are distinct, $P$ and $Q$ have no common factor. The rational map is represented in homogeneous coordinates by two homogeneous polynomials of the common degree $d=\max(n,m)$:
$$
[Z:W]\longmapsto
\begin{cases}
[W^{d-n}P_h(Z,W):W^{d-m}Q_h(Z,W)]
\end{cases}
$$
after placing the necessary power of $W$ in the lower-degree component. These homogeneous forms have no common zero on $\mathbb{CP}^1$. A generic value therefore has exactly $d$ preimages counted with multiplicity. Holomorphic maps preserve orientation at regular points, so the topological degree equals this algebraic count, namely $d$.
:::

<1>2. In particular, if the intended map is instead the restriction of $p$ to a large circle with values in $\mathbb C^*$, its winding number is $n-m$.
::: {.proof}
On a sufficiently large circle enclosing every zero and pole, the argument principle gives winding number equal to the number of zeros minus the number of poles, namely $n-m$. This is a different notion from the degree of the rational self-map of $S^2$ in <1>1.
:::
:::
