---
schema: qual/card@1
id: E-AMD-KRMOU3CI
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
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
Show that every group of order $pqr$ with $p<q<r$ primes contains a normal Sylow subgroup, and hence is never simple.
:::

::: solution
Let $n_r$ be the number of Sylow $r$-subgroups. By Sylow,
\[
n_r\equiv1\pmod r,
\qquad
n_r\mid pq.
\]
Since $p,q<r$, if $n_r\ne1$ then necessarily
\[
n_r=pq.
\]
Distinct Sylow $r$-subgroups intersect trivially, so they contribute
\[
pq(r-1)
\]
nonidentity elements.

Now let $n_q$ be the number of Sylow $q$-subgroups. Again,
\[
n_q\equiv1\pmod q,
\qquad
n_q\mid pr.
\]
If $n_q\ne1$, then $n_q\ge q+1$. Since the divisors of $pr$ are $1,p,r,pr$ and $p<q$, this forces
\[
n_q\in\{r,pr\},
\]
so in particular $n_q\ge r$. Distinct Sylow $q$-subgroups also intersect trivially, hence they contribute at least
\[
r(q-1)
\]
nonidentity elements.

If both $n_r>1$ and $n_q>1$, the sets of nonidentity elements counted above are disjoint, because an element cannot simultaneously have order $r$ and order $q$. Thus $G$ would contain at least
\[
pq(r-1)+r(q-1)+1
\]
elements. But
\[
pq(r-1)+r(q-1)+1-pqr
=r(q-1)-pq+1>0,
\]
because $q-1\ge p$ and $r>q$. This is impossible.

Therefore either $n_r=1$ or $n_q=1$. Hence $G$ has a normal Sylow subgroup and is not simple.
:::
