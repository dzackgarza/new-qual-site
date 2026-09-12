---
schema: qual/card@1
id: P-RAF10C
kind: problem
title: "Semifinite measures approximate by finite-measure subsets"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2010 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that a measure $\mu$ is semifinite if for all $E \in \mathcal{M}$ with $\mu(E) > 0$ there exists $A \in \mathcal{M}$, $A \subset E$ such that $0 < \mu(A) < \infty$.
If $\mu$ is semifinite, prove that for all $E \in \mathcal{M}$,
$$
\mu(E) = \sup\{\mu(A) : A \in \mathcal{M},\; A \subseteq E,\; \mu(A) < \infty\}.
$$
:::

::: solution
<1>1. The case $\mu(E)<\infty$ is immediate.
::: proof
Let
\[
S:=\sup\{\mu(A):A\subseteq E,\ A\in\mathcal M,\ \mu(A)<\infty\}.
\]
Every admissible $A$ satisfies $\mu(A)\le\mu(E)$, so $S\le\mu(E)$. If $\mu(E)<\infty$, then $A=E$ is admissible and hence $S\ge\mu(E)$. Therefore
\[
S=\mu(E).
\]
:::

<1>2. The case $\mu(E)=\infty$.
::: proof
Suppose for contradiction that $S<\infty$. Choose measurable $A_n\subseteq E$ with
\[
\mu(A_n)<\infty,
\qquad
\mu(A_n)>S-\frac1n.
\]
Set
\[
B_n:=\bigcup_{k=1}^nA_k.
\]
Then $B_n\subseteq E$, $\mu(B_n)<\infty$, and
\[
S-\frac1n<\mu(B_n)\le S.
\]
Hence $\mu(B_n)\to S$. Let
\[
B:=\bigcup_{n=1}^\infty B_n.
\]
By continuity from below,
\[
\mu(B)=S<\infty.
\]
Since $\mu(E)=\infty$, we must have
\[
\mu(E\setminus B)=\infty.
\]
In particular this set has positive measure. By semifiniteness, there exists measurable
\[
C\subset E\setminus B
\]
with
\[
0<\mu(C)<\infty.
\]
Then $B\cup C\subset E$ has finite measure and
\[
\mu(B\cup C)=S+\mu(C)>S,
\]
contradicting the definition of $S$.

Therefore $S=\infty=\mu(E)$. Combining the two cases proves
\[
\boxed{
\mu(E)=\sup\{\mu(A):A\subseteq E,\ A\in\mathcal M,\ \mu(A)<\infty\}.}
\]
:::
:::
