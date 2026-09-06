---
schema: qual/card@1
id: P-AMD-BWEE5VHM
kind: problem
title: A group of squarefree order $pqr$ has a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 5. The source
    assumes p<q<r are distinct primes and asks for at least one normal Sylow
    subgroup.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    If the Sylow r-subgroup is not normal, Sylow congruence forces n_r=pq,
    accounting for pq(r-1) nonidentity elements. Only pq elements remain. If
    the Sylow q-subgroup were also nonnormal, then n_q>=r and its Sylow
    subgroups would contribute at least r(q-1)>=q^2-1>pq distinct nonidentity
    elements, a contradiction.
---

::: {.problem}
Let $G$ be a finite group with
\[
|G|=pqr,
\]
where $p<q<r$ are distinct primes.
Prove that $G$ has at least one normal Sylow subgroup.
:::

::: {.solution}
For a prime $\ell\mid |G|$, write $n_\ell$ for the number of Sylow $\ell$-subgroups of $G$.

<1>1. Either $n_r=1$ or $n_r=pq$.
::: {.proof}
Sylow's theorem gives
\[
n_r\equiv 1\pmod r
\qquad\text{and}\qquad
n_r\mid pq.
\]
Thus
\[
n_r\in\{1,p,q,pq\}.
\]
Because
\[
1<p<r
\qquad\text{and}\qquad
1<q<r,
\]
neither $p$ nor $q$ is congruent to $1$ modulo $r$.
Hence
\[
n_r\in\{1,pq\}.
\]
:::

<1>2. If $n_r=1$, then $G$ has a normal Sylow subgroup.
::: {.proof}
A Sylow subgroup is normal if and only if it is the unique Sylow subgroup for that prime.
Thus $n_r=1$ makes the Sylow $r$-subgroup normal.
:::

Assume from now on that
\[
n_r=pq.
\]

<1>3. Exactly $pq(r-1)$ elements of $G$ are nonidentity elements of Sylow $r$-subgroups.
::: {.proof}
Since $r$ occurs to the first power in $|G|=pqr$, every Sylow $r$-subgroup has order $r$.
Two distinct subgroups of order $r$ intersect trivially: their intersection has order dividing the prime $r$, and a nontrivial intersection would force the two subgroups to be equal.
Therefore the $pq$ Sylow $r$-subgroups have pairwise disjoint sets of nonidentity elements.
Each contributes $r-1$ such elements, giving
\[
pq(r-1)
\]
in total.
:::

<1>4. There are exactly $pq$ elements of $G$ outside those nonidentity Sylow $r$-elements.
::: {.proof}
By <1>3, their number is
\[
|G|-pq(r-1)
=pqr-pq(r-1)
=pq.
\]
:::

<1>5. If $n_q\ne 1$, then $n_q\ge r$.
::: {.proof}
Sylow's theorem gives
\[
n_q\equiv 1\pmod q
\qquad\text{and}\qquad
n_q\mid pr.
\]
Hence
\[
n_q\in\{1,p,r,pr\}.
\]
Since $1<p<q$, the value $p$ is not congruent to $1$ modulo $q$.
Therefore
\[
n_q\in\{1,r,pr\}.
\]
If $n_q\ne1$, this implies
\[
n_q\ge r.
\]
:::

<1>6. If $n_q\ne1$, then $G$ has more than $pq$ elements of order $q$.
::: {.proof}
Every Sylow $q$-subgroup has order $q$, and two distinct subgroups of order $q$ intersect trivially.
Thus the number of elements of order $q$ is
\[
n_q(q-1).
\]
By <1>5,
\[
n_q(q-1)\ge r(q-1).
\]
Since $r>q$,
\[
r(q-1)\ge(q+1)(q-1)=q^2-1.
\]
Moreover,
\[
q^2-1-pq=q(q-p)-1\ge q-1>0,
\]
because $p<q$ and $q\ge3$.
Hence
\[
n_q(q-1)>pq.
\]
:::

<1>7. Under the assumption $n_r=pq$, one must have $n_q=1$.
::: {.proof}
Every element of order $q$ lies outside the nonidentity elements of the Sylow $r$-subgroups.
By <1>4 there are only $pq$ elements outside those Sylow $r$-elements.
But if $n_q\ne1$, <1>6 produces more than $pq$ elements of order $q$, a contradiction.
Therefore
\[
n_q=1.
\]
:::

<1>8. The group $G$ has a normal Sylow subgroup.
::: {.proof}
If $n_r=1$, the Sylow $r$-subgroup is normal by <1>2. If $n_r\ne1$, then <1>1 gives $n_r=pq$, and <1>7 gives $n_q=1$, so the Sylow $q$-subgroup is normal.
Thus in every case $G$ has at least one normal Sylow subgroup.
:::
:::
