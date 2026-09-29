---
schema: qual/card@1
id: P-BKF11-6B
kind: problem
title: Groups of exponent $2$ are abelian but groups of exponent $3$ need not be
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the exponent-2 commutativity argument and verified explicitly
    that the upper-unitriangular group over F_3 is nonabelian of exponent 3.
---

::: {.problem}
(a) Show that if every element of a group has order $1$ or $2$, then the group is abelian.

(b) Show that there is a nonabelian group such that every element has order $1$ or $3$.
:::

::: {.solution}
For part (b), let
$$
H\coloneqq
\left\{
\begin{pmatrix}
1&a&c\\
0&1&b\\
0&0&1
\end{pmatrix}
:a,b,c\in\FF_3
\right\}.
$$
This is the group of upper-unitriangular $3\times3$ matrices over
$\FF_3$.

::: pf

::: {.pf-step #s1}

If every element of a group $G$ has order $1$ or $2$, then
$G$ is abelian.

::: pf-proof

For every $x\in G$, one has $x^2=e$, hence $x^{-1}=x$. Therefore,
for arbitrary $a,b\in G$,
$$
ab=(ab)^{-1}=b^{-1}a^{-1}=ba.
$$
Thus every pair of elements commutes.

:::

:::

::: pf-step

The set $H$ is a group under matrix multiplication.

::: pf-proof

Write
$$
M(a,b,c)\coloneqq
\begin{pmatrix}
1&a&c\\
0&1&b\\
0&0&1
\end{pmatrix}.
$$
Direct multiplication gives
$$
M(a,b,c)M(a',b',c')
=M(a+a',b+b',c+c'+ab').
$$
Thus $H$ is closed under multiplication and contains
$M(0,0,0)=I$. Moreover,
$$
M(a,b,c)^{-1}=M(-a,-b,ab-c),
$$
as the multiplication formula verifies. Hence every element has its
inverse in $H$.

:::

:::

::: {.pf-step #s3}

The group $H$ is nonabelian.

::: pf-proof

Consider
$$
X=
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
Y=
\begin{pmatrix}
1&0&0\\
0&1&1\\
0&0&1
\end{pmatrix}.
$$
Then
$$
XY=
\begin{pmatrix}
1&1&1\\
0&1&1\\
0&0&1
\end{pmatrix},
\qquad
YX=
\begin{pmatrix}
1&1&0\\
0&1&1\\
0&0&1
\end{pmatrix}.
$$
Hence $XY\ne YX$.

:::

:::

::: {.pf-step #s4}

Every element of $H$ has order $1$ or $3$.

::: pf-proof

Every $A\in H$ has the form
$$
A=I+N
$$
with $N$ strictly upper triangular. For a $3\times3$ strictly upper
triangular matrix,
$$
N^3=0.
$$
Since the ground field has characteristic $3$,
$$
A^3=(I+N)^3
=I+3N+3N^2+N^3
=I.
$$
Thus the order of every $A\in H$ divides $3$. The identity has order
$1$, and every nonidentity element therefore has order $3$.

:::

:::

::: {.pf-step #s5}

Consequently,
$$
\boxed{H\text{ is nonabelian and every element of }H
\text{ has order }1\text{ or }3}.
$$

::: pf-proof

Step [](#s3){.pf-ref} proves that $H$ is nonabelian, and step [](#s4){.pf-ref} gives the
required orders.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s5){.pf-ref} supplies the example required
for part (b).

:::

:::

:::
