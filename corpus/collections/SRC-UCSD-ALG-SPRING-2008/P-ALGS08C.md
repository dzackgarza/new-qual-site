---
schema: qual/card@1
id: P-ALGS08C
kind: problem
title: "A normal subgroup of a p-group intersects the center nontrivially"
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
  note: Compared the statement with Problem 3 on page 2 of the official Spring 2008 algebra exam and with the UCSD group-theory review sheet. Both omit the necessary assumption that N is nontrivial; the zero subgroup is an immediate counterexample.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked the conjugation-action class equation and the divisibility argument for the fixed-point subgroup N cap Z(G).
---

::: problem
Show that if $G$ is a group of order $p^n$, where $p$ is a prime, and $N$ is a nontrivial normal subgroup, then $N$ intersects the center of $G$ nontrivially.
:::

::: remark
The hypothesis that $N$ is nontrivial is necessary.
For $N=\{1\}$, one has $N\cap Z(G)=\{1\}$, so the conclusion in the unqualified source statement fails.
:::

::: {.solution}
<1>1. Conjugation by $G$ defines an action on $N$, whose fixed points are exactly $N\cap Z(G)$.
::: {.proof}
Normality of $N$ ensures that
\[
gng^{-1}\in N
\qquad(g\in G,\ n\in N),
\]
so conjugation restricts to an action of $G$ on $N$.
An element $n\in N$ is fixed by every $g\in G$ precisely when
\[
gng^{-1}=n
\qquad\text{for all }g\in G,
\]
which is equivalent to $n\in Z(G)$.
Thus the fixed-point set is $N\cap Z(G)$.
:::

<1>2. Every nontrivial orbit in this action has cardinality divisible by $p$.
::: {.proof}
For $n\in N$, orbit-stabilizer gives
\[
|G\cdot n|=[G:C_G(n)].
\]
Since $|G|=p^n$, every subgroup index in $G$ is a power of $p$.
If the orbit is not a singleton, its size is therefore a positive power of $p$, hence is divisible by $p$.
:::

<1>3. The fixed-point set contains a nonidentity element.
::: {.proof}
Partition $N$ into conjugation orbits.
Using <1>1 and <1>2 gives a class equation of the form
\[
|N|=|N\cap Z(G)|+\sum_i p^{a_i},
\qquad a_i\ge1,
\]
where the sum runs over the nontrivial orbits.
Therefore
\[
|N|\equiv |N\cap Z(G)|\pmod p.
\]

Because $N$ is a nontrivial subgroup of the finite $p$-group $G$, its order is a positive power of $p$ and hence is divisible by $p$.
It follows that $p$ divides $|N\cap Z(G)|$.
The latter subgroup contains the identity, so its order is positive; divisibility by $p$ forces
\[
|N\cap Z(G)|\ge p>1.
\]
Thus $N\cap Z(G)$ is nontrivial.
:::
:::
