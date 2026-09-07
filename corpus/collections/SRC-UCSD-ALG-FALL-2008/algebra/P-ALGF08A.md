---
schema: qual/card@1
id: P-ALGF08A
kind: problem
title: "A finite group of prime-power order is nilpotent"
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
  note: Checked against Question 1 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the induction on the group order using the nontrivial center of every nontrivial finite p-group and lifting a central series from G/Z(G).
---

::: {.problem}
Let $G$ be a finite group of order a prime power.
Show that $G$ is nilpotent.
:::

::: {.solution}
We use the criterion that a group is nilpotent if it admits a finite central series
\[
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_c=G
\]
such that
\[
G_{i+1}/G_i\subseteq Z(G/G_i)
\]
for every $i$.

<1>1. Every nontrivial finite $p$-group has nontrivial center.
::: {.proof}
Let $|G|=p^n$ with $n\ge1$, and let $G$ act on itself by conjugation.
The class equation is
\[
|G|=|Z(G)|+\sum_j [G:C_G(x_j)],
\]
where the $x_j$ represent the noncentral conjugacy classes.
For noncentral $x_j$, the centralizer $C_G(x_j)$ is a proper subgroup of the $p$-group $G$, so
\[
[G:C_G(x_j)]
\]
is a positive power of $p$ and hence is divisible by $p$.
Since $|G|$ is divisible by $p$, the class equation implies
\[
p\mid |Z(G)|.
\]
Thus
\[
|Z(G)|\ge p>1.
\]
:::

<1>2. Every finite $p$-group is nilpotent.
::: {.proof}
We argue by induction on $|G|$.
The trivial group is nilpotent.
Suppose now that $G$ is nontrivial and that every smaller finite $p$-group is nilpotent.
Set
\[
Z:=Z(G).
\]
By <1>1, $Z\neq1$, so
\[
|G/Z|<|G|.
\]
The quotient $G/Z$ is again a finite $p$-group, hence is nilpotent by induction.
Therefore it has a central series
\[
1=\overline G_0\triangleleft\overline G_1\triangleleft\cdots\triangleleft\overline G_c=G/Z
\]
with
\[
\overline G_{i+1}/\overline G_i
\subseteq
Z\bigl((G/Z)/\overline G_i\bigr).
\]

Let $\pi:G\to G/Z$ be the quotient map and define
\[
G_0:=1,
\qquad
G_1:=Z,
\qquad
G_{i+1}:=\pi^{-1}(\overline G_i)
\quad(1\le i\le c).
\]
Then
\[
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_{c+1}=G.
\]
The first factor is central because
\[
G_1/G_0=Z(G).
\]
For $i\ge1$, the natural identification
\[
G/G_i\cong (G/Z)/\overline G_{i-1}
\]
identifies
\[
G_{i+1}/G_i
\]
with
\[
\overline G_i/\overline G_{i-1},
\]
which is central in the corresponding quotient by the central-series property above.
Thus the lifted chain is a central series for $G$.
Hence $G$ is nilpotent.
:::
:::
