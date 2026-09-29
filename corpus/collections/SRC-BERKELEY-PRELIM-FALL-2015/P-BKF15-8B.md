---
schema: qual/card@1
id: P-BKF15-8B
kind: problem
title: Matrix rings over a field are simple
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: from any
    nonzero matrix in a two-sided ideal, multiplication on the left and
    right produces matrix units and hence the whole matrix ring.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the matrix-unit multiplication formula, scalar rescaling over
    the field, and spanning of the full matrix ring by the E_ij.
---

::: {.problem}
If $A$ is the ring of $n\times n$ matrices with entries in a field $K$, show that the only two-sided ideals of $A$ are $A$ itself and $0$.
:::

::: {.solution}
Let
$$
A=M_n(K),
$$
and let $I$ be a nonzero two-sided ideal of $A$. For
$1\le i,j\le n$, let $E_{ij}$ denote the standard matrix unit.

::: pf

::: pf-step

There is a matrix
$$
M=(m_{ab})\in I
$$
with at least one entry
$$
m_{ab}\ne0.
$$

::: pf-proof

Since $I\ne0$, choose a nonzero matrix $M\in I$. A matrix is zero
exactly when all of its entries are zero, so some entry $m_{ab}$ is
nonzero.

:::

:::

::: {.pf-step #s2}

For every $1\le i,j\le n$,
$$
E_{ia}ME_{bj}
=
m_{ab}E_{ij}.
$$

::: pf-proof

Left multiplication by $E_{ia}$ keeps only row $a$ of $M$ and moves it
to row $i$. Right multiplication by $E_{bj}$ then keeps only column
$b$ of that result and moves it to column $j$. The only remaining
entry is therefore the $(i,j)$ entry, equal to $m_{ab}$.

Equivalently, using the matrix-unit identity
$$
E_{pq}E_{rs}
=
\delta_{qr}E_{ps},
$$
write
$$
M=\sum_{p,q}m_{pq}E_{pq}.
$$
Then
$$
\begin{aligned}
E_{ia}ME_{bj}
&=
\sum_{p,q}m_{pq}E_{ia}E_{pq}E_{bj}\\
&=
m_{ab}E_{ij}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

Every matrix unit $E_{ij}$ belongs to $I$.

::: pf-proof

Since $I$ is a two-sided ideal and $M\in I$, step [](#s2){.pf-ref} gives
$$
m_{ab}E_{ij}\in I
$$
for every $i,j$. The scalar $m_{ab}$ is nonzero and hence invertible
in the field $K$. Multiplying by the scalar matrix
$$
m_{ab}^{-1}I_n\in A
$$
therefore gives
$$
E_{ij}\in I.
$$

:::

:::

::: {.pf-step #s4}

One has
$$
I=A.
$$

::: pf-proof

Every matrix $X=(x_{ij})\in A$ has the expansion
$$
X=\sum_{i,j}x_{ij}E_{ij}.
$$
By step [](#s3){.pf-ref} every $E_{ij}$ belongs to $I$, and an ideal is closed
under multiplication by scalar matrices and under addition. Hence
every $X\in A$ lies in $I$.

:::

:::

::: {.pf-step #s5}

Consequently the only two-sided ideals of $A$ are
$$
\boxed{0\ \text{and}\ A}.
$$

::: pf-proof

The zero ideal is a two-sided ideal. Step [](#s4){.pf-ref} shows that every
nonzero two-sided ideal equals $A$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required classification.

:::

:::

:::
