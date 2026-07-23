---
schema: qual/card@1
id: P-WB2SR
kind: problem
title: "Supposing that $\\dim V = n$, let $\\mathcal B \\definedas \\theset{\\vecto\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Supposing that $\dim V = n$, let $\mathcal B \definedas \theset{\vector b_k \mid 1 \leq k \leq n}$ be a basis for $V$, and define
$$
\vector e_i \definedas [0, 0, \cdots, 1, \cdots, 0] \in V^{\oplus m}
$$

where the $1$ occurs in the $i$th position. The claim is that $\mathcal{B}^{m} \definedas \theset{\vector e_i \vector b_k \mid 1 \leq i \leq n,~~1\leq k \leq m}$ forms a basis for $V^{\oplus m}$.

Elements in $\mathcal{B}^{m}$ are of the form
\[
\begin{align*}
[\vector b_1, 0, 0, \cdots, 0]\\
[\vector b_2, 0, 0, \cdots, 0]\\
\cdots \\
[0, \vector b_1, 0, \cdots, 0]\\
[0, \vector b_2, 0, \cdots, 0]\\
\cdots
,\end{align*}
\]

and by construction, $\abs{\mathcal B} = mn = m\dim V$.

To see that this is a spanning set, let $\vector x \in V^{\oplus m}$, so $\vector x = [\vector v_1, \vector v_2, \cdots, \vector v_m]$ where each $\vector v_i \in V$.

Then each $\vector v_i \in \mathcal B$, so $\vector v_i = \sum_{k=1}^n \alpha_{k, i} \vector b_k$. But then
$$
\vector x = [\sum_{k=1}^n \alpha_{k, 1} \vector b_k, \sum_{k=1}^n \alpha_{k, 2} \vector b_k, \cdots, \sum_{k=1}^n \alpha_{k, m} \vector b_k] \definedas \sum_{i=1}^m \sum_{k=1}^n \alpha_{k, i} \vector b_k \vector e_i,
$$

which exhibits $\vector x \in \mathcal{B}^m$.

To see that it is linearly independent, supposing that $\vector x = \sum_i \sum_k \alpha_{k, i} \vector b_k \vector e_i = 0$, this says that $\vector x = [0, 0, \cdots, 0]$, which forces $\sum_k \alpha_{k, i} \vector b_k$ to be zero for each $i$.

But for a fixed $i$, since $\theset{\vector b_k}$ was a basis for $V$, this means that $\alpha_{k, i} = 0$ for all $k$. But then $\alpha_{k, i} = 0$ for all pairs $i, k$.

