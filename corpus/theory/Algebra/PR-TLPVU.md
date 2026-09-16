---
schema: qual/card@1
id: PR-TLPVU
kind: proposition
title: Converting between elementary divisors and invariant factors
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.proposition}
Let $G$ be a finite abelian group with $G\cong\bigoplus_{i=1}^s \ZZ/m_i\ZZ$ for integers $m_i\geq 2$, not necessarily distinct.

(a) The elementary divisors of $G$ are the prime powers $p^e$, $e\geq1$, occurring in the factorizations $m_i=\prod_p p^{e_{p,i}}$, listed with multiplicity over all $i$; that is, $G\cong\bigoplus_{i}\bigoplus_{p} \ZZ/p^{e_{p,i}}\ZZ$.

(b) For each prime $p$, list the exponents of the $p$-power elementary divisors in decreasing order, $e_{p,1}\geq e_{p,2}\geq\cdots$, padding with zeros.
Put $d_j\coloneqq\prod_p p^{e_{p,j}}$ and let $t$ be the largest $j$ with $d_j\neq 1$.
Then $d_t\divides d_{t-1}\divides\cdots\divides d_1$ and
$$
G\cong \ZZ/d_t\ZZ\oplus\cdots\oplus\ZZ/d_1\ZZ
$$
is the invariant factor decomposition of $G$.
:::

::: {.proof}
By the Chinese remainder theorem, $\ZZ/m\ZZ\cong\bigoplus_p\ZZ/p^{e_p}\ZZ$ for $m=\prod_p p^{e_p}$, which gives (a).
For (b), the same theorem gives $\ZZ/d_j\ZZ\cong\bigoplus_p\ZZ/p^{e_{p,j}}\ZZ$, so $\bigoplus_j\ZZ/d_j\ZZ$ has the same elementary divisors as $G$ and is isomorphic to $G$.
Since $e_{p,j+1}\leq e_{p,j}$ for every $p$, $d_{j+1}\divides d_j$.
:::

::: {.example}
Let $G=\ZZ/12\ZZ\oplus\ZZ/18\ZZ\oplus\ZZ/5\ZZ$.
Since $12=2^2\cdot3$ and $18=2\cdot3^2$, the elementary divisors are $2^2, 2, 3^2, 3, 5$.
The largest power of each prime gives $d_1=2^2\cdot3^2\cdot5=180$, and the remaining powers give $d_2=2\cdot3=6$.
Hence $G\cong\ZZ/6\ZZ\oplus\ZZ/180\ZZ$, with $6\divides180$.
:::
