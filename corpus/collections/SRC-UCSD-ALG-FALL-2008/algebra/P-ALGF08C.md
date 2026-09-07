---
schema: qual/card@1
id: P-ALGF08C
kind: problem
title: "A group of order p^2 q has a normal Sylow subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow-number argument and treated the sole residual numerical case p=2, q=3 by counting the elements in the four Sylow 3-subgroups.
---

::: {.problem}
Show that if $G$ is a group of order $p^2 q$, where $p$ and $q$ are distinct primes, then $G$ has either a normal $p$-Sylow subgroup or a normal $q$-Sylow subgroup.
:::

::: {.solution}
Let
\[
|G|=p^2q,
\]
where \(p\neq q\) are primes.
Write \(n_p\) and \(n_q\) for the numbers of Sylow \(p\)- and \(q\)-subgroups, respectively.

<1>1. If neither Sylow subgroup is normal, then \(q>p\), \(n_p=q\), and \(n_q=p^2\).
::: {.proof}
Sylow's theorem gives
\[
n_p\mid q,
\qquad
n_p\equiv1\pmod p.
\]
Since \(q\) is prime, \(n_p\in\{1,q\}\).
If the Sylow \(p\)-subgroup is not normal, then
\[
n_p=q.
\]
The congruence \(q\equiv1\pmod p\) then implies
\[
q>p.
\]

Similarly,
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q,
\]
so
\[
n_q\in\{1,p,p^2\}.
\]
If the Sylow \(q\)-subgroup is not normal, then \(n_q\neq1\).
Because \(q>p\), one cannot have
\[
p\equiv1\pmod q.
\]
Thus \(n_q\neq p\), and hence
\[
n_q=p^2.
\]
:::

<1>2. Under the assumptions of <1>1, necessarily
\[
(p,q)=(2,3).
\]
::: {.proof}
From
\[
n_q=p^2\equiv1\pmod q
\]
we obtain
\[
q\mid p^2-1=(p-1)(p+1).
\]
Since \(q>p\), the prime \(q\) cannot divide \(p-1\).
Therefore
\[
q\mid p+1.
\]
But \(q>p\), so \(0<p+1\le q\), and hence
\[
q=p+1.
\]
If \(p\) were odd, then \(q=p+1\) would be an even integer greater than \(2\), hence not prime.
Therefore
\[
p=2,
\qquad
q=3.
\]
:::

<1>3. In a group of order \(12\), four Sylow \(3\)-subgroups force the Sylow \(2\)-subgroup to be unique.
::: {.proof}
Assume
\[
|G|=12
\]
and
\[
n_3=4.
\]
Distinct subgroups of order \(3\) intersect only in the identity.
Thus the four Sylow \(3\)-subgroups contain
\[
4(3-1)=8
\]
distinct nonidentity elements.
Together with the identity, these account for \(9\) elements of \(G\), leaving exactly \(3\) other elements.

Let \(P\) be any Sylow \(2\)-subgroup.
Then
\[
|P|=4.
\]
Since \(P\) has order a power of \(2\), it meets every subgroup of order \(3\) only in the identity.
Therefore the three nonidentity elements of \(P\) must be precisely the three elements not lying in the Sylow \(3\)-subgroups.
This description is independent of the choice of \(P\).
Hence every Sylow \(2\)-subgroup is the same subgroup, so
\[
n_2=1.
\]
:::

<1>4. Therefore \(G\) has a normal Sylow subgroup.
::: {.proof}
Suppose for contradiction that neither a Sylow \(p\)-subgroup nor a Sylow \(q\)-subgroup were normal.
By <1>1 and <1>2, one would have
\[
p=2,
\qquad
q=3,
\qquad
n_3=4.
\]
But <1>3 then gives
\[
n_2=1,
\]
so the Sylow \(2\)-subgroup is normal, a contradiction.
Therefore at least one of the Sylow \(p\)- or Sylow \(q\)-subgroups is normal.
:::
:::
