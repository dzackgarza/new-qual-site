---
schema: qual/card@1
id: P-ALGCOMP03-02
kind: problem
title: Sylow subgroups in orders 21, 39, and 56
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified all Sylow-number congruence/divisibility cases and the counting contradiction for a hypothetical simple group of order 56.
---

::: {.problem}
(a) List the Sylow subgroups of non-abelian groups of orders $21$ and $39$.

(b) Prove that there is no simple group of order $56$.
:::


::: {.solution}
<1>1. Determine the Sylow subgroups for the nonabelian groups of orders \(21\) and \(39\).
::: {.proof}
First let \(|G|=21=3\cdot7\). If \(n_7\) is the number of Sylow \(7\)-subgroups, Sylow's theorems give
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid3.
\]
Hence
\[
n_7=1.
\]
Thus the Sylow \(7\)-subgroup is unique and normal.

For the Sylow \(3\)-subgroups,
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid7,
\]
so
\[
n_3\in\{1,7\}.
\]
If \(n_3=1\), then both Sylow subgroups are normal. Their intersection is trivial, and since their orders are coprime they commute elementwise; hence \(G\cong C_7\times C_3\cong C_{21}\), which is abelian. Therefore a nonabelian group of order \(21\) must have
\[
\boxed{n_3=7,\qquad n_7=1}.
\]
Every Sylow \(3\)-subgroup is cyclic of order \(3\), and the unique Sylow \(7\)-subgroup is cyclic of order \(7\).

Now let \(|G|=39=3\cdot13\). Sylow's theorems give
\[
n_{13}\equiv1\pmod{13},
\qquad
n_{13}\mid3,
\]
so
\[
n_{13}=1.
\]
Also
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid13,
\]
so
\[
n_3\in\{1,13\}.
\]
As above, \(n_3=1\) would make both Sylow subgroups normal and force \(G\cong C_{13}\times C_3\), hence \(G\) abelian. Therefore a nonabelian group of order \(39\) has
\[
\boxed{n_3=13,\qquad n_{13}=1}.
\]
:::

<1>2. No group of order \(56\) is simple.
::: {.proof}
Let \(|G|=56=2^3\cdot7\). Suppose for contradiction that \(G\) is simple.

The number \(n_7\) of Sylow \(7\)-subgroups satisfies
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid8.
\]
Thus
\[
n_7\in\{1,8\}.
\]
Simplicity excludes \(n_7=1\), so \(n_7=8\).

Distinct subgroups of order \(7\) intersect only in the identity. Hence the union of all eight Sylow \(7\)-subgroups contains
\[
1+8(7-1)=49
\]
elements. Therefore exactly
\[
56-49=7
\]
elements of \(G\) lie outside this union.

Let \(P\) be any Sylow \(2\)-subgroup. Then \(|P|=8\), and every nonidentity element of \(P\) has order a power of \(2\); in particular, no such element lies in a subgroup of order \(7\). Thus the seven nonidentity elements of \(P\) must be precisely the seven elements outside the union of the Sylow \(7\)-subgroups.

Consequently every Sylow \(2\)-subgroup has the same underlying set
\[
\{1\}\cup\bigl(G\setminus\textstyle\bigcup_{Q\in\operatorname{Syl}_7(G)}Q\bigr).
\]
Hence the Sylow \(2\)-subgroup is unique. A unique Sylow subgroup is normal, contradicting simplicity.

Therefore
\[
\boxed{\text{there is no simple group of order }56}.
\]
:::
:::
