---
schema: qual/card@1
id: PR-2MTPE
kind: proposition
title: Summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
relations: []
review: draft
---

::: {.proposition}
Let $(a_k)_{k\ge1}$ and $(b_k)_{k\ge1}$ be sequences of complex numbers, and put $A_n \coloneqq \sum_{k=1}^n a_k$ and $B_n\coloneqq\sum_{k=1}^n b_k$ for $n\ge1$, with $A_0 \coloneqq 0$ and $B_0\coloneqq0$.

(a) For all integers $1\le m\le n$,
$$
\sum_{k=m}^n a_k b_k = A_nb_n - A_{m-1} b_m - \sum_{k=m}^{n-1} A_k(b_{k+1} - b_{k}).
$$

(b) For all sequences $(f_k)$ and $(g_k)$ of complex numbers and all integers $m\le n$, writing $\Delta g_k \coloneqq g_{k+1} - g_k$ and $\Delta f_k\coloneqq f_{k+1}-f_k$,
$$
\sum_{k=m}^n f_k \, \Delta g_k = f_{n+1} g_{n+1} - f_m g_m - \sum_{k=m}^n g_{k+1} \, \Delta f_k.
$$

(c) For every $n\ge1$,
$$
A_{n} B_{n}=\sum_{k=1}^{n} A_{k} b_{k}+\sum_{k=1}^{n} a_{k} B_{k-1}.
$$
:::

::: {.proof}
For (b), $f_{k+1}g_{k+1}-f_kg_k=f_k\,\Delta g_k+g_{k+1}\,\Delta f_k$ for every $k$; summing over $m\le k\le n$ telescopes the left side to $f_{n+1}g_{n+1}-f_mg_m$.

For (a), substitute $a_k=A_k-A_{k-1}$:
$$
\sum_{k=m}^n a_kb_k=\sum_{k=m}^nA_kb_k-\sum_{k=m-1}^{n-1}A_kb_{k+1}=A_nb_n-A_{m-1}b_m-\sum_{k=m}^{n-1}A_k(b_{k+1}-b_k).
$$

For (c), $A_kB_k-A_{k-1}B_{k-1}=A_k(B_{k-1}+b_k)-(A_k-a_k)B_{k-1}=A_kb_k+a_kB_{k-1}$ for every $k\ge1$; summing over $1\le k\le n$ and using $A_0B_0=0$ gives the identity.
:::

::: {.remark}
Identity (a) is the discrete analogue of integration by parts: for $F$ an antiderivative of $f$ on $[a,b]$ and $g$ continuously differentiable,
$$
\int_a^b f g = F(b)g(b) - F(a)g(a) - \int_a^b Fg'.
$$
The partial sums $A_k$ play the role of $F$, and the differences $b_{k+1}-b_k$ the role of $g'$.
:::
