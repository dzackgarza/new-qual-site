---
schema: qual/card@1
id: P-2TASE
kind: problem
title: Classification of abelian groups of a given composite order
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Classification
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
- **Important**: Pick your favorite composite number $m = \prod p_i^{e_i}$ and classify all abelian groups of that order.

  - Write their invariant factor decompositions *and* their elementary divisor decompositions.
    Come up with an algorithm for converting back and forth between these.
:::


::: {.solution}
Take
\[
m=72=2^3\cdot3^2.
\]
By the classification theorem for finite abelian groups, the $2$-primary part is determined by a partition of $3$, and the $3$-primary part by a partition of $2$.

<1>1. The possible primary components are
\[
\begin{aligned}
G_{(2)}&\cong C_8,\quad C_4\oplus C_2,\quad C_2\oplus C_2\oplus C_2,\\
G_{(3)}&\cong C_9,\quad C_3\oplus C_3.
\end{aligned}
\]
::: {.proof}
The partitions of $3$ are
\[
3,\qquad2+1,\qquad1+1+1,
\]
which give the three $2$-primary groups. The partitions of $2$ are
\[
2,\qquad1+1,
\]
which give the two $3$-primary groups.
:::

<1>2. Hence there are exactly six abelian groups of order $72$.
::: {.proof}
The primary decomposition is unique, so each choice of a $2$-primary type and a $3$-primary type gives one isomorphism class, and every class occurs this way. Thus there are
\[
3\cdot2=6
\]
classes.
:::

<1>3. Their elementary-divisor and invariant-factor forms are as follows:
\[
\begin{array}{c|c}
\text{elementary divisors}&\text{invariant factors}\\ \hline
C_8\oplus C_9&C_{72}\\
C_8\oplus C_3\oplus C_3&C_3\oplus C_{24}\\
C_4\oplus C_2\oplus C_9&C_2\oplus C_{36}\\
C_4\oplus C_2\oplus C_3\oplus C_3&C_6\oplus C_{12}\\
C_2\oplus C_2\oplus C_2\oplus C_9&C_2\oplus C_2\oplus C_{18}\\
C_2\oplus C_2\oplus C_2\oplus C_3\oplus C_3&C_2\oplus C_6\oplus C_6
\end{array}
\]
::: {.proof}
For relatively prime integers $a,b$, one has
\[
C_a\oplus C_b\cong C_{ab}.
\]
To obtain invariant factors, align the prime-power cyclic factors in nondecreasing order, pad the shorter lists on the left by $1$'s, and multiply columnwise. For example,
\[
(C_4,C_2)=(C_2,C_4),
\qquad
(C_9)=(C_1,C_9),
\]
so
\[
(C_2\oplus C_4)\oplus C_9
\cong C_{2\cdot1}\oplus C_{4\cdot9}
=C_2\oplus C_{36}.
\]
The other rows follow identically. In every invariant-factor row, each factor divides the next.
:::

<1>4. The conversion algorithm from elementary divisors to invariant factors is columnwise multiplication of aligned prime powers.
::: {.proof}
For each prime $p$, write the $p$-primary cyclic factors as
\[
p^{a_{p,1}}\mid p^{a_{p,2}}\mid\cdots\mid p^{a_{p,r_p}}.
\]
Let $r=\max_p r_p$ and pad each list on the left by exponent $0$. For each column $j$, define
\[
d_j=\prod_p p^{a_{p,j}}.
\]
Then
\[
d_1\mid d_2\mid\cdots\mid d_r,
\]
and the direct sum of the $C_{d_j}$ is the invariant-factor decomposition.
:::

<1>5. The reverse algorithm factors each invariant factor into its prime-power parts.
::: {.proof}
Given
\[
C_{d_1}\oplus\cdots\oplus C_{d_r},
\qquad d_1\mid\cdots\mid d_r,
\]
factor each
\[
d_j=\prod_p p^{v_p(d_j)}.
\]
Using the Chinese remainder theorem,
\[
C_{d_j}\cong\bigoplus_{p\mid d_j}C_{p^{v_p(d_j)}}.
\]
Collecting these prime-power cyclic summands gives the elementary-divisor decomposition. The two algorithms are inverse because they merely regroup the same primary cyclic factors.
:::
:::
