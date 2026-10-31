---
schema: qual/card@1
id: P-UCTOP290-S4-2
kind: problem
title: Cyclic covers of closed orientable surfaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 2 against the checked-in extraction and PDF page image.
---

::: {.problem}
Construct a five-sheeted covering
$$
\Sigma_{11}\longrightarrow\Sigma_3
$$
and a three-sheeted covering
$$
\Sigma_4\longrightarrow\Sigma_2,
$$
where $\Sigma_g$ is the closed orientable surface of genus $g$.
Find the deck transformation group of each covering.
:::

::: {.solution}

For each $g\ge1$ and $n\ge2$, the surface group
$\pi_1(\Sigma_g)$ has generators
$a_1,b_1,\ldots,a_g,b_g$ and one relation
$\prod_{j=1}^g[a_j,b_j]=1$.
Define a surjection $\phi:\pi_1(\Sigma_g)\to\ZZ/n$ by sending $a_1$
to $1$ and every other generator to $0$. The surface relation maps
to $0$, so this is well defined. Its kernel is normal and has index
$n$. The corresponding connected cover is therefore regular with
deck group
$$
\pi_1(\Sigma_g)/\ker\phi\cong\ZZ/n.
$$

The covering surface is closed and orientable. Its Euler
characteristic is $n(2-2g)$, so its genus is
$$
1+n(g-1).
$$
For $(g,n)=(3,5)$ this is $11$, and for $(g,n)=(2,3)$ it is $4$.
The classification of closed orientable surfaces identifies the
covering surfaces with $\Sigma_{11}$ and $\Sigma_4$, respectively.
Their deck groups are $\ZZ/5$ and $\ZZ/3$.

:::
