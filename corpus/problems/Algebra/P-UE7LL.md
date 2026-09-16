---
schema: qual/card@1
id: P-UE7LL
kind: problem
title: Groups of order $p^2 q$ have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $p,q$ be primes and let $|G|=p^2q$. Show that $G$ has a nontrivial proper normal subgroup.
:::

::: {.solution}
If $p=q$, then $G$ is a finite $p$-group. Its center is nontrivial, so $G$ has a nontrivial normal subgroup. Thus assume $p\ne q$.

If $p>q$, Sylow's theorem gives
\[
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
\]
Since $q<p$, the only possibility is
\[
n_p=1.
\]
Hence the Sylow $p$-subgroup is normal.

Now suppose $p<q$. Sylow gives
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
Thus $n_q\in\{1,p,p^2\}$. The value $p$ is impossible because $p<q$. If $n_q=p^2$, then
\[
q\mid p^2-1=(p-1)(p+1).
\]
Since $q>p$, this forces $q\mid p+1$, hence
\[
q=p+1.
\]
The only consecutive primes are then
\[
p=2,\qquad q=3.
\]
So except for groups of order $12$, one has $n_q=1$ and hence a normal Sylow $q$-subgroup.

It remains to treat $|G|=12$. If $n_3=1$, the Sylow $3$-subgroup is normal. Otherwise $n_3=4$, and the four Sylow $3$-subgroups contain
\[
4(3-1)=8
\]
distinct nonidentity elements. Hence exactly four elements remain, including the identity. Any Sylow $2$-subgroup has order $4$ and cannot contain an element of order $3$, so it must consist exactly of these four remaining elements. Thus the Sylow $2$-subgroup is unique and normal.

Therefore every group of order $p^2q$ has a nontrivial proper normal subgroup.
:::
