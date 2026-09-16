---
schema: qual/card@1
id: E-HAT-2.2-19
kind: problem
title: $H_i(\mathbb{RP}^n/\mathbb{RP}^m)$ by cellular homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
  - Cellular Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 19; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
---

::: {.problem}
Compute $H_i(\mathbb{RP}^n/\mathbb{RP}^m)$ for $m < n$ by cellular homology, using the standard CW structure on $\mathbb{RP}^n$ with $\mathbb{RP}^m$ as its $m$ skeleton.
:::

::: {.solution}
Let
\[
Y=\mathbb{RP}^n/\mathbb{RP}^m,
\qquad m<n.
\]
The quotient CW structure has one $0$-cell and one cell in each dimension
\[
m+1,m+2,\dots,n.
\]
Thus its reduced cellular chain groups are
\[
\widetilde C_i(Y)\cong
\begin{cases}
\mathbb Z,&m<i\le n,\\
0,&\text{otherwise}.
\end{cases}
\]
For $i>m+1$, the cellular boundary is the usual projective-space boundary
\[
d_i=
\begin{cases}
2,&i\text{ even},\\
0,&i\text{ odd},
\end{cases}
\]
while $d_{m+1}=0$ because its target chain group has been collapsed away.

<1>1. If $n=m+1$, then
\[
\widetilde H_n(Y)\cong\mathbb Z
\]
and all other reduced homology groups vanish.
::: {.proof}
There is a single nonzero reduced cellular chain group, in degree $n$, and both adjacent boundary maps are zero.
:::

Assume henceforth that $n\ge m+2$.

<1>2. In the bottom degree $m+1$,
\[
\widetilde H_{m+1}(Y)\cong
\begin{cases}
\mathbb Z,&m+1\text{ even},\\
\mathbb Z_2,&m+1\text{ odd}.
\end{cases}
\]
::: {.proof}
The outgoing differential is zero. The incoming differential is $d_{m+2}$, which is zero when $m+2$ is odd and multiplication by $2$ when $m+2$ is even. These are exactly the two displayed cases.
:::

<1>3. For $m+1<i<n$,
\[
\widetilde H_i(Y)\cong
\begin{cases}
\mathbb Z_2,&i\text{ odd},\\
0,&i\text{ even}.
\end{cases}
\]
::: {.proof}
If $i$ is even, $d_i=2$ is injective, so there are no cycles. If $i$ is odd, $d_i=0$ and $d_{i+1}=2$, giving
\[
H_i\cong\mathbb Z/2\mathbb Z.
\]
:::

<1>4. In the top degree $n$,
\[
\widetilde H_n(Y)\cong
\begin{cases}
\mathbb Z,&n\text{ odd},\\
0,&n\text{ even},
\end{cases}
\qquad(n>m+1).
\]
::: {.proof}
There is no incoming boundary from degree $n+1$. Thus top homology is $\ker d_n$, which is $\mathbb Z$ for odd $n$ and $0$ for even $n$.
:::

Finally $Y$ is connected, so
\[
H_0(Y)\cong\mathbb Z.
\]
Together <1>1--<1>4 give all homology groups of $\mathbb{RP}^n/\mathbb{RP}^m$.
:::
