---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-09
kind: problem
title: Connectedness of the real line
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 9 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Assumed a separation U union V, chose u in U below v in V, and took the
    supremum of U intersect [u,v]. Openness shows the supremum can lie in
    neither U nor V, contradicting that they cover R.
---

::: {.problem}
Prove that $\mathbb R$ with the usual topology is connected.
:::

::: {.solution}

::: pf

::: pf-step
Suppose, for contradiction, that
\[
\mathbb R=U\cup V
\]
is a separation, with $U$ and $V$ disjoint nonempty open subsets of $\mathbb R$.
Choose
\[
u\in U,
\qquad
v\in V.
\]
After interchanging $u$ and $v$ and simultaneously interchanging $U$ and $V$ if necessary, assume
\[
u<v.
\]

::: pf-proof
If $u>v$, rename the point in $V$ as the left endpoint and the point in $U$ as the right endpoint, and interchange the names of the two sets.
The hypotheses of a separation are symmetric in $U$ and $V$.
:::

:::

::: pf-step
The set
\[
S=U\cap[u,v]
\]
is nonempty and bounded above, so it has a supremum
\[
c=\sup S
\]
with
\[
u\le c\le v.
\]

::: pf-proof
Since $u\in U\cap[u,v]$, the set $S$ is nonempty.
Every element of $S$ lies in $[u,v]$, so $v$ is an upper bound.
The least-upper-bound property of $\mathbb R$ therefore gives $c=\sup S$.
Since $u\in S$, we have $u\le c$, and since $v$ is an upper bound, $c\le v$.
:::

:::

::: {.pf-step #c-not-in-u}
The point $c$ cannot lie in $U$.

::: pf-proof
Suppose $c\in U$.
Because $v\in V$ and $U\cap V=\varnothing$, we have $c\ne v$, so
\[
c<v.
\]
Since $U$ is open, choose $\varepsilon>0$ such that
\[
(c-\varepsilon,c+\varepsilon)\subseteq U.
\]
Choose
\[
t\in\left(c,\min\{c+\varepsilon,v\}\right).
\]
Then
\[
t\in U\cap[u,v]=S
\]
and $t>c$, contradicting that $c$ is an upper bound of $S$.
Hence $c\notin U$.
:::

:::

::: {.pf-step #c-not-in-v}
The point $c$ cannot lie in $V$.

::: pf-proof
Suppose $c\in V$.
Because $u\in U$ and $U\cap V=\varnothing$, we have $c\ne u$, so
\[
u<c.
\]
Since $V$ is open, choose $\varepsilon>0$ such that
\[
(c-\varepsilon,c+\varepsilon)\subseteq V.
\]
Set
\[
\delta=\min\left\{\frac\varepsilon2,\frac{c-u}{2}\right\}>0.
\]
By the defining property of the supremum, $c-\delta$ is not an upper bound for $S$.
Hence there exists $s\in S$ with
\[
c-\delta<s\le c.
\]
By step [](#c-not-in-u){.pf-ref}, $c\notin U$.
Since $s\in S\subseteq U$, we have $s\ne c$, and therefore $s<c$.
Also
\[
s>c-\delta\ge c-\frac\varepsilon2>c-\varepsilon,
\]
so $s\in(c-\varepsilon,c+\varepsilon)\subseteq V$.
Thus $s\in U\cap V$, contradicting disjointness.
Therefore $c\notin V$.
:::

:::

::: pf-step
Therefore $\mathbb R$ is connected.

::: pf-proof
By steps [](#c-not-in-u){.pf-ref} and [](#c-not-in-v){.pf-ref},
\[
c\notin U\cup V,
\]
contradicting the assumed equality
\[
\mathbb R=U\cup V.
\]
Thus no separation of $\mathbb R$ exists, so $\mathbb R$ is connected.
:::

:::

:::

:::
