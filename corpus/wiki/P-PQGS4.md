---
schema: qual/card@1
id: P-PQGS4
kind: problem
title: "Let $F_1, F_2$ be free, so they have bases $\\mathcal B_1 = \\theset{\\vector b_{1, k}}, \\mathcal B_2 = \\theset{\\vector b_{2, k}}$."
classification:
  areas:
  - algebra
  topics:
  - free-modules
  - bases
  - direct-products
relations: []
review: draft
---

::: problem
Let $F_1, F_2$ be free, so they have bases $\mathcal B_1 = \theset{\vector b_{1, k}}, \mathcal B_2 = \theset{\vector b_{2, k}}$.
Supposing that they have the invariant dimension property, we can assume that $\size\mathcal B_1 \definedas \rank F_1$ and similarly $\size\mathcal B_2 \definedas \rank F_2$.

The claim is that the set $$\mathcal B = \theset{(v, 0) \mid v\in \mathcal{B}_1 } \union \theset{(0, w) \mid w \in \mathcal{B}_2}$$ is a basis for $F_1 \oplus F_2$, where $\size \mathcal B = \size \mathcal B_1 + \size \mathcal B_2 = \rank F_1 + \rank F_2$.

So see that $\mathcal B$ spans $F_1 \oplus F_2$, let $x\in F_1 \oplus F_2 = (f_1, f_2)$ be arbitrary.
Since $f_1 \in F_1$, we have $f_1 = \sum_i r_i \vector b_{1, i}$, and similarly $f_2 = \sum_j s_j \vector b_{2, j}$.

We can then write
$$
x = (f_1, f_2) = (f_1, 0) + (0, f_2) = (\sum_i r_i \vector b_{1, i}, 0) + (0, \sum_j s_j \vector b_{2, j}),
$$

which exhibits $x$ as a linear combination of elements in $\mathcal B$.

To see linear independence, we just note that
\[
\begin{align*}
x &= (0, 0) \\
&= \sum_i r_i (v_i, 0) + \sum_j s_j (0, w_j) \\&
= \sum_i (r_i v_i, 0) + \sum_j (0, s_j w_j) \\
&= (\sum_i r_i v_i, \sum_j s_j w_j)  \\
& \implies \sum_i r_i v_i = 0 \quad \& \quad \sum_j s_j w_j = 0
,\end{align*}
\]

but since the $v_i$ were a basis of $F_1$ and the $w_j$ a basis of $F_2$, this forces $r_i = 0, w_j = 0$ for all $i, j$.
:::
