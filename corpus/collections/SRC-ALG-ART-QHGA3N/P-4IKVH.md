---
schema: qual/card@1
id: P-4IKVH
kind: problem
title: Groups of order $p^2q$ have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
audit:
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

Let $G$ be a group of order $p^2q$ for $p, q$ prime. Show that $G$ has a nontrivial normal subgroup.

::: {.solution}
<1>1. Let \(n_p\) and \(n_q\) denote the numbers of Sylow \(p\)- and Sylow \(q\)-subgroups of \(G\). Then
\[
n_p\mid q,\qquad n_p\equiv1\pmod p,
\]
and
\[
n_q\mid p^2,\qquad n_q\equiv1\pmod q.
\]
::: {.proof}
These are exactly the Sylow congruence and divisibility conditions for a group of order \(p^2q\).
:::

<1>2. If \(p>q\), then the Sylow \(p\)-subgroup is unique and hence normal.
::: {.proof}
Since \(n_p\mid q\), one has \(n_p\in\{1,q\}\). But \(q<p\), so \(q\not\equiv1\pmod p\). Thus the Sylow congruence \(n_p\equiv1\pmod p\) forces \(n_p=1\).
:::

<1>3. Suppose \(p<q\). If \(n_q=1\), then the Sylow \(q\)-subgroup is normal, so assume \(n_q>1\). Then \(n_q=p^2\).
::: {.proof}
Because \(n_q\mid p^2\), the possibilities are \(1,p,p^2\). Since \(p<q\), the value \(p\) is not congruent to \(1\pmod q\). Hence if \(n_q\neq1\), the only remaining possibility is \(n_q=p^2\).
:::

<1>4. In the case \(n_q=p^2\), the union of all Sylow \(q\)-subgroups contains exactly
\[
1+p^2(q-1)
\]
elements.
::: {.proof}
Two distinct subgroups of order \(q\) intersect only in the identity, because their intersection has order dividing the prime \(q\). Each Sylow \(q\)-subgroup therefore contributes \(q-1\) new nonidentity elements, and there are \(p^2\) such subgroups.
:::

<1>5. The Sylow \(p\)-subgroup is then unique and hence normal.
::: {.proof}
By <1>4, the number of elements of \(G\) lying outside the union of the Sylow \(q\)-subgroups is
\[
p^2q-\bigl(1+p^2(q-1)\bigr)=p^2-1.
\]
Let \(P\) be any Sylow \(p\)-subgroup. Every nonidentity element of \(P\) lies outside every Sylow \(q\)-subgroup, since its order is divisible by \(p\), not \(q\). Thus the \(p^2-1\) nonidentity elements of \(P\) exhaust the entire complement of the Sylow-\(q\) union. Hence every Sylow \(p\)-subgroup has exactly the same nonidentity elements, so there is only one Sylow \(p\)-subgroup. Therefore \(P\trianglelefteq G\).
:::

<1>6. In all cases, \(G\) has a nontrivial normal subgroup.
::: {.proof}
If \(p>q\), use <1>2. If \(p<q\), either \(n_q=1\) or <1>5 applies. Since \(p\) and \(q\) are prime, these Sylow subgroups are nontrivial.
:::
:::
