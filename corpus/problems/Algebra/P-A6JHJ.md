---
schema: qual/card@1
id: P-A6JHJ
kind: problem
title: Whether $A_4$ is simple, and conjugacy in $S_4$ and $A_4$
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Conjugacy
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Is \(A_4\) a simple group?
What are the conjugacy classes in $S_4$?
What about in \(A_4\)?
:::


::: {.solution}
<1>1. The group $A_4$ is not simple.
::: {.proof}
The subset
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
is a subgroup of $A_4$. Conjugation preserves cycle type, so conjugating any nonidentity element of $V_4$ by an element of $A_4$ again gives a double transposition. Hence $V_4\trianglelefteq A_4$. Since
\[
1<|V_4|=4<12=|A_4|,
\]
this is a proper nontrivial normal subgroup, so $A_4$ is not simple.
:::

<1>2. The conjugacy classes in $S_4$ are determined by cycle type.
::: {.proof}
Two permutations in a symmetric group are conjugate exactly when they have the same cycle type. Thus the classes in $S_4$ are:
\[
\begin{array}{c|c}
\text{cycle type} & \text{class size}\\ \hline
1^4 & 1\\
2\,1^2 & 6\\
2^2 & 3\\
3\,1 & 8\\
4 & 6
\end{array}
\]
The sizes sum to $1+6+3+8+6=24$.
:::

<1>3. The conjugacy classes in $A_4$ are
\[
\{e\},
\qquad
\{(12)(34),(13)(24),(14)(23)\},
\]
and two classes of four $3$-cycles each.
::: {.proof}
Only the even cycle types from <1>2 occur in $A_4$: the identity, the three double transpositions, and the eight $3$-cycles.

The three double transpositions form one conjugacy class in $A_4$: for example conjugation by $3$-cycles permutes them transitively.

Now let $\sigma=(123)$. Its centralizer in $A_4$ is
\[
C_{A_4}(\sigma)=\langle\sigma\rangle,
\]
which has order $3$. Hence its $A_4$-conjugacy class has size
\[
[A_4:C_{A_4}(\sigma)]=12/3=4.
\]
There are eight $3$-cycles total, so they split into exactly two conjugacy classes of size $4$. Equivalently, a $3$-cycle and its inverse lie in the two different $A_4$-classes.
:::

<1>4. These classes also exhibit the normal subgroup $V_4$.
::: {.proof}
A normal subgroup is a union of conjugacy classes containing the identity. The union of the identity class with the double-transposition class is exactly $V_4$, recovering the normal subgroup from <1>1.
:::
:::
