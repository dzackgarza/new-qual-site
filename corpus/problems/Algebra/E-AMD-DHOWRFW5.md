---
schema: qual/card@1
id: E-AMD-DHOWRFW5
kind: problem
title: $A_n$ is the unique proper nontrivial normal subgroup of $S_n$ for $n\geq 5$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
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
Show that $S_n$ for $n \ge 5$ has exactly one non-trivial proper normal subgroup: $A_n$.
:::

::: solution
Use the standard theorem that \(A_n\) is simple for \(n\ge5\).

Let \(N\trianglelefteq S_n\) be nontrivial. Then
\[
N\cap A_n\trianglelefteq A_n.
\]
By simplicity of \(A_n\), either
\[
N\cap A_n=A_n
\qquad\text{or}\qquad
N\cap A_n=1.
\]

<1>1. If \(N\cap A_n=A_n\), then \(N=A_n\) or \(N=S_n\).
::: proof
In this case \(A_n\le N\le S_n\). Since \([S_n:A_n]=2\), there is no intermediate subgroup strictly between them.
:::

<1>2. The case \(N\cap A_n=1\) is impossible.
::: proof
The quotient map \(S_n\to S_n/A_n\cong C_2\) restricts injectively to \(N\), because its kernel on \(N\) is \(N\cap A_n=1\). Since \(N\ne1\), it follows that \(|N|=2\).

Write \(N=\{1,\sigma\}\). Normality implies
\[
g\sigma g^{-1}\in N\setminus\{1\}=\{\sigma\}
\]
for every \(g\in S_n\). Hence \(\sigma\in Z(S_n)\). But \(Z(S_n)=1\) for \(n\ge3\), contradiction.
:::

Thus every nontrivial proper normal subgroup of \(S_n\) equals \(A_n\). Therefore
\[
\boxed{A_n\text{ is the unique nontrivial proper normal subgroup of }S_n\quad(n\ge5).}
\]
:::
