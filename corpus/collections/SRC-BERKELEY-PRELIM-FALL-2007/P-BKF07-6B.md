---
schema: qual/card@1
id: P-BKF07-6B
kind: problem
title: Possible rank triples for three matrices summing to zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked necessity of the three rank inequalities and the
    diagonal support construction realizing every admissible triple against
    the vendored solution.
---

::: {.problem}
Given a positive integer \(n\), determine all possible triples
\[
(\operatorname{rank}A,\operatorname{rank}B,\operatorname{rank}C)
\]
as \(A,B,C\) range over real \(n\times n\) matrices satisfying
\[
A+B+C=0.
\]
:::

::: {.solution}
Let
$$
a\coloneqq\operatorname{rank}A,
\qquad
b\coloneqq\operatorname{rank}B,
\qquad
c\coloneqq\operatorname{rank}C.
$$

<1>1. Every realizable triple $(a,b,c)$ satisfies
$$
0\le a,b,c\le n
$$
and
$$
a\le b+c,
\qquad
b\le c+a,
\qquad
c\le a+b.
$$

::: {.proof}
The bounds $0\le a,b,c\le n$ hold for ranks of $n\times n$
matrices. Since $C=-(A+B)$,
$$
\operatorname{im}C
\subseteq
\operatorname{im}A+\operatorname{im}B.
$$
Therefore
$$
c\le a+b.
$$
The other two inequalities follow in the same way from
$A=-(B+C)$ and $B=-(C+A)$.
:::

<1>2. Conversely, let $(a,b,c)\in\{0,\ldots,n\}^3$ satisfy the
three inequalities in step <1>1. After permuting the three matrices if
necessary, assume
$$
c\ge a,
\qquad
c\ge b.
$$

::: {.proof}
The conditions and the equation $A+B+C=0$ are symmetric under
permuting $A,B,C$. Thus one may label a largest member of
$\{a,b,c\}$ by $c$.
:::

<1>3. Define diagonal matrices $A$ and $B$ by
$$
A_{ii}=
\begin{cases}
1,&1\le i\le a,\\
0,&a<i\le n,
\end{cases}
$$
and
$$
B_{ii}=
\begin{cases}
1,&c-b<i\le c,\\
0,&\text{otherwise}.
\end{cases}
$$
Then
$$
\operatorname{rank}A=a,
\qquad
\operatorname{rank}B=b,
\qquad
\operatorname{rank}(A+B)=c.
$$

::: {.proof}
The first two rank equalities are immediate from the numbers of nonzero
diagonal entries. The inequality $c\le a+b$ is equivalent to
$$
c-b\le a.
$$
Hence the support intervals
$$
\{1,\ldots,a\},
\qquad
\{c-b+1,\ldots,c\}
$$
overlap or meet so that their union is exactly
$\{1,\ldots,c\}$. On the overlap the corresponding diagonal entry
of $A+B$ is $2$, which is nonzero over $\RR$; elsewhere in the union
it is $1$. Thus $A+B$ has exactly $c$ nonzero diagonal entries, and
$\operatorname{rank}(A+B)=c$.
:::

<1>4. Setting $C\coloneqq-(A+B)$ realizes the triple $(a,b,c)$.

::: {.proof}
By construction,
$$
A+B+C=0.
$$
Step <1>3 gives
$$
\operatorname{rank}C
=\operatorname{rank}(A+B)
=c,
$$
while the ranks of $A$ and $B$ are $a$ and $b$.
:::

<1>5. The possible rank triples are exactly
$$
\boxed{
\left\{
(a,b,c)\in\{0,\ldots,n\}^3:
a\le b+c,\ b\le c+a,\ c\le a+b
\right\}.
}
$$

::: {.proof}
Step <1>1 gives the necessary conditions, and steps <1>2--<1>4 realize
every triple satisfying them.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested classification.
:::
:::
