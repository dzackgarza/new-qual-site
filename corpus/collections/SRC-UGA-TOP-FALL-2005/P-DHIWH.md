---
schema: qual/card@1
id: P-DHIWH
kind: problem
title: The unit interval is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 3 of the official UGA Fall 2005 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the circular nested-compact-interval argument by a proof from the least-upper-bound property of the real numbers.
---

::: {.problem}
Prove that the unit interval $I$ is compact.
Be sure to explicitly state any properties of $\RR$ that you use.
:::

::: {.solution}
<1>1. We use the least-upper-bound property of $\RR$.
::: {.proof}
The required property of the real numbers is:

> Every nonempty subset of $\RR$ that is bounded above has a least upper bound in $\RR$.

We also use the defining property of the usual topology on $\RR$: if $U\subseteq\RR$ is open and $x\in U$, then some $\varepsilon>0$ satisfies $(x-\varepsilon,x+\varepsilon)\subseteq U$.
:::

<1>2. Let $\mathcal U$ be an arbitrary open cover of $[0,1]$, and define
\[
S=\{x\in[0,1]:[0,x]\text{ is covered by finitely many members of }\mathcal U\}.
\]
Then $S$ is nonempty and bounded above.
::: {.proof}
Because $\mathcal U$ covers $[0,1]$, some $U_0\in\mathcal U$ contains $0$.
Hence the one-element family $\{U_0\}$ covers $[0,0]=\{0\}$, so $0\in S$.
Also $S\subseteq[0,1]$, so $1$ is an upper bound for $S$.
:::

<1>3. Let
\[
s=\sup S.
\]
Then $s\in S$.
::: {.proof}
Choose $U\in\mathcal U$ with $s\in U$.
Since $U$ is open in the subspace $[0,1]$, there exists $\varepsilon>0$ such that
\[
(s-\varepsilon,s+\varepsilon)\cap[0,1]\subseteq U.
\]

If $s=0$, then $s\in S$ by <1>2.
Suppose $s>0$.
By the defining property of the supremum, there exists $x\in S$ satisfying
\[
s-\varepsilon<x\le s.
\]
Choose finitely many members of $\mathcal U$ covering $[0,x]$.
Together with $U$, they cover $[0,s]$: points at most $x$ are covered by the finite family, while points of $[x,s]$ lie in $(s-\varepsilon,s+\varepsilon)\cap[0,1]\subseteq U$.
Thus $[0,s]$ has a finite subcover, so $s\in S$.
:::

<1>4. One must have $s=1$.
::: {.proof}
Suppose instead that $s<1$.
Using the same $U$ and $\varepsilon$ from <1>3, choose
\[
y\in(s,\min\{1,s+\varepsilon\}).
\]
Such a $y$ exists because both $1$ and $s+\varepsilon$ are strictly larger than $s$.

By <1>3, finitely many members of $\mathcal U$ cover $[0,s]$.
Adding $U$ gives a finite cover of $[0,y]$, because
\[
[s,y]\subseteq(s-\varepsilon,s+\varepsilon)\cap[0,1]\subseteq U.
\]
Hence $y\in S$, contradicting $y>s=\sup S$.
Therefore $s=1$.
:::

<1>5. The interval $[0,1]$ is compact.
::: {.proof}
By <1>4, $1=s\in S$.
By the definition of $S$, the arbitrary open cover $\mathcal U$ therefore has a finite subcover of $[0,1]$.
This is exactly compactness of the unit interval.
:::
:::
