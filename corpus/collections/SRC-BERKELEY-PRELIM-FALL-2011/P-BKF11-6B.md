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

<1>1. If every element of a group $G$ has order $1$ or $2$, then
$G$ is abelian.

::: {.proof}
For every $x\in G$, one has $x^2=e$, hence $x^{-1}=x$. Therefore,
for arbitrary $a,b\in G$,
$$
ab=(ab)^{-1}=b^{-1}a^{-1}=ba.
$$
Thus every pair of elements commutes.
:::

<1>2. The set $H$ is a group under matrix multiplication.

::: {.proof}
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

<1>3. The group $H$ is nonabelian.

::: {.proof}
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

<1>4. Every element of $H$ has order $1$ or $3$.

::: {.proof}
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

<1>5. Consequently,
$$
\boxed{H\text{ is nonabelian and every element of }H
\text{ has order }1\text{ or }3}.
$$

::: {.proof}
Step <1>3 proves that $H$ is nonabelian, and step <1>4 gives the
required orders.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>5 supplies the example required
for part (b).
:::
:::
