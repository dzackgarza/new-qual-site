---
schema: qual/card@1
id: P-YWQOM
kind: problem
title: Groups of order $pqr$ have a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ have order $pqr$ with primes $p<q<r$. Show that $G$ has a normal Sylow subgroup. In particular, show that $G$ is not simple.
:::

::: {.solution}
Let $n_r$ be the number of Sylow $r$-subgroups. Sylow gives
\[
n_r\mid pq,
\qquad
n_r\equiv1\pmod r.
\]
Since $p,q<r$, if $n_r\ne1$ then necessarily
\[
n_r=pq.
\]
If $n_r=1$, the Sylow $r$-subgroup is normal and we are done.

Assume therefore that $n_r=pq$. Distinct Sylow $r$-subgroups have trivial intersection, so they contribute
\[
pq(r-1)
\]
nonidentity elements. Thus only
\[
pqr-pq(r-1)=pq
\]
elements remain.

Now let $n_q$ be the number of Sylow $q$-subgroups. If $n_q>1$, then
\[
n_q\equiv1\pmod q,
\qquad
n_q\mid pr.
\]
Because $p<q$, this forces
\[
n_q\ge r.
\]
Distinct Sylow $q$-subgroups also intersect trivially, so they would contribute at least
\[
r(q-1)
\]
nonidentity elements among the $pq-1$ nonidentity elements not already lying in Sylow $r$-subgroups. But
\[
r(q-1)>q(q-1)>pq-1
\]
because $r>q>p$. This is impossible.

Hence
\[
n_q=1,
\]
so the Sylow $q$-subgroup is normal.

Thus every group of order $pqr$ has a nontrivial proper normal Sylow subgroup and is therefore not simple.
:::
