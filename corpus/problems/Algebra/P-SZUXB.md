---
schema: qual/card@1
id: P-SZUXB
kind: problem
title: Groups of order $p^2q^2$ with $q\nmid(p^2-1)$ and $p\nmid(q^2-1)$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.problem}
Let $p\ne q$ be primes. Show that a group $G$ of order $p^2q^2$ is abelian if
\[
q\nmid(p^2-1)\qquad\text{and}\qquad p\nmid(q^2-1).
\]
:::

::: {.solution}
Let $n_p$ be the number of Sylow $p$-subgroups. Sylow's theorem gives
\[
n_p\mid q^2,
\qquad
n_p\equiv1\pmod p.
\]
Thus $n_p\in\{1,q,q^2\}$. If $n_p=q$, then $p\mid(q-1)$, hence $p\mid(q^2-1)$, contrary to hypothesis. If $n_p=q^2$, then again $p\mid(q^2-1)$, contradiction. Therefore
\[
n_p=1.
\]
So the Sylow $p$-subgroup $P$ is normal.

Similarly,
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
The possibilities $n_q=p$ and $n_q=p^2$ would imply respectively $q\mid(p-1)$ or $q\mid(p^2-1)$, both impossible under the stated hypothesis. Hence
\[
n_q=1,
\]
so the Sylow $q$-subgroup $Q$ is normal.

Since $P,Q\normal G$ and $|P|,|Q|$ are coprime,
\[
[P,Q]\le P\cap Q=1.
\]
Hence $P$ and $Q$ commute elementwise. Also $|PQ|=|P||Q|=|G|$, so
\[
G=P\times Q.
\]
Every group of order $p^2$ or $q^2$ is abelian, so both $P$ and $Q$ are abelian. Therefore $G$ is abelian.
:::
