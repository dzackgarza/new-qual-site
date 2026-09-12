---
schema: qual/card@1
id: P-APAF22E
kind: problem
title: Schur product $s_{2,1,1} s_{2,2,1}$ as a linear combination of Schur functions
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
---

::: problem
Let $s$ denote the Schur function.
Express the product
\[
s_{2,1,1}\, s_{2,2,1}
\]
as a linear combination of Schur functions.
:::

::: {.solution}
We use the Pieri rules.

<1>1. One has
\[
s_{(2,1,1)}=e_3h_1-e_4.
\]
::: {.proof}
Since $e_3=s_{(1,1,1)}$, the ordinary Pieri rule for multiplication by $h_1=s_{(1)}$ gives
\[
e_3h_1=s_{(2,1,1)}+s_{(1,1,1,1)}=s_{(2,1,1)}+e_4.
\]
Rearrange.
:::

<1>2. Vertical Pieri gives
\[
\begin{aligned}
s_{(2,2,1)}e_3={}&s_{(2,2,1,1,1,1)}+s_{(2,2,2,1,1)}+s_{(3,2,1,1,1)}\\
&+s_{(3,2,2,1)}+s_{(3,3,1,1)}+s_{(3,3,2)}.
\end{aligned}
\]
::: {.proof}
Multiplication by $e_3=s_{(1,1,1)}$ adds a vertical $3$-strip. The displayed six partitions are exactly the partitions obtained from $(2,2,1)$ by adding three boxes with no two in the same row.
:::

<1>3. Multiplying the expression in <1>2 by $h_1$ and applying Pieri once more gives
\[
\begin{aligned}
s_{(2,2,1)}e_3h_1={}&s_{(2,2,1,1,1,1,1)}+2s_{(2,2,2,1,1,1)}+s_{(2,2,2,2,1)}\\
&+2s_{(3,2,1,1,1,1)}+3s_{(3,2,2,1,1)}+s_{(3,2,2,2)}\\
&+2s_{(3,3,1,1,1)}+3s_{(3,3,2,1)}+s_{(3,3,3)}\\
&+s_{(4,2,1,1,1)}+s_{(4,2,2,1)}+s_{(4,3,1,1)}+s_{(4,3,2)}.
\end{aligned}
\]
::: {.proof}
Multiplication by $h_1$ adds one box. For each partition in <1>2, add one box in every possible row (or as a new row) and collect equal resulting partitions. The multiplicities count the number of such one-box additions producing the same partition.
:::

<1>4. Vertical Pieri also gives
\[
\begin{aligned}
s_{(2,2,1)}e_4={}&s_{(2,2,1,1,1,1,1)}+s_{(2,2,2,1,1,1)}+s_{(3,2,1,1,1,1)}\\
&+s_{(3,2,2,1,1)}+s_{(3,3,1,1,1)}+s_{(3,3,2,1)}.
\end{aligned}
\]
::: {.proof}
Multiplication by $e_4$ adds a vertical $4$-strip to $(2,2,1)$. The displayed six partitions are exactly the possibilities.
:::

<1>5. Therefore
\[
\boxed{\begin{aligned}
s_{(2,1,1)}s_{(2,2,1)}={}&s_{(2,2,2,1,1,1)}+s_{(2,2,2,2,1)}+s_{(3,2,1,1,1,1)}\\
&+2s_{(3,2,2,1,1)}+s_{(3,2,2,2)}+s_{(3,3,1,1,1)}\\
&+2s_{(3,3,2,1)}+s_{(3,3,3)}+s_{(4,2,1,1,1)}\\
&+s_{(4,2,2,1)}+s_{(4,3,1,1)}+s_{(4,3,2)}.
\end{aligned}}
\]
::: {.proof}
By <1>1,
\[
s_{(2,1,1)}s_{(2,2,1)}
=s_{(2,2,1)}e_3h_1-s_{(2,2,1)}e_4.
\]
Subtract the expansion in <1>4 from that in <1>3 and collect coefficients.
:::
:::
