---
schema: qual/card@1
id: D-KRKV7
kind: definition
title: Quaternion group $Q_8$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
relations: []
review: draft
---

::: {.definition}
The \dfn{quaternion group} is the group of order $8$
$$
\begin{aligned}
Q_8 &= \gens{-1, i, j, k \suchthat (-1)^2 = 1,\ i^2 = j^2 = k^2 = ijk = -1} \\
  &\cong \gens{x, y \suchthat  x^4 = y^4,\ x^2 = y^2,\ yxy^{-1} = x^{-1}},
\end{aligned}
$$
where the isomorphism sends $x\mapsto i$ and $y\mapsto j$.
Its elements are $\pm1,\pm i,\pm j,\pm k$.
:::

::: {.remark}
Every element of $\theset{i,j,k}$ squares to $-1$, and $ijk=-1$.
Products of two distinct elements of $\theset{i,j,k}$ taken along the cycle $i\to j\to k\to i$ are positive, $ij=k$, $jk=i$, $ki=j$, and products taken against the cycle are negative, $ji=-k$, $kj=-i$, $ik=-j$:

\begin{tikzcd}
	&& {-1} \\
	\\
	&& i \\
	\\
	\\
	k &&& {} & j
	\arrow["{ki=j}"', from=3-3, to=6-5]
	\arrow["{ij=k}"', from=6-5, to=6-1]
	\arrow["{jk=i}"', from=6-1, to=3-3]
	\arrow["{ik=-j}"', curve={height=30pt}, dashed, from=6-1, to=6-5]
	\arrow["{kj=-i}"', curve={height=30pt}, dashed, from=6-5, to=3-3]
	\arrow["{ji=-k}"', curve={height=30pt}, dashed, from=3-3, to=6-1]
	\arrow["{ijk=-1}"', from=3-3, to=1-3]
\end{tikzcd}
:::
