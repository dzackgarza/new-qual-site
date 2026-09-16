---
schema: qual/card@1
id: P-APAF11C
kind: problem
title: Inductions and Kronecker product of Specht modules of $S_5$, $S_7$, $S_8$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Suppose that $\lambda=(\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_k)$ is a partition of $n$.
Then $A^\lambda$ denotes the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$, and $S_{\lambda_1}\times\cdots\times S_{\lambda_k}$ denotes the Young subgroup of $S_n$ corresponding to $\lambda$.

(a) Find the decomposition of
\[
A^{(2,1^2)}\times A^{(2,2)}\uparrow_{S_4\times S_4}^{S_8}
\]
as a sum of irreducible representations of $S_8$.

(b) Let $T$ denote the trivial representation on the Young subgroup $S_3\times S_2\times S_1$ of $S_7$ and $\mathrm{Alt}$ denote the alternating representation on the Young subgroup $S_3\times S_2\times S_1$ of $S_7$.
Find the decomposition of
\[
T\uparrow_{S_3\times S_2\times S_1}^{S_7}\quad\text{and}\quad\mathrm{Alt}\uparrow_{S_3\times S_2\times S_1}^{S_7}
\]
as a sum of irreducible representations of $S_7$.

(c) Find the decomposition of the Kronecker product $A^{(3,2)}\otimes A^{(3,2)}$ as a sum of irreducible representations of $S_5$.
:::

::: {.remark}
In the source, part (b) is internally inconsistent: the displayed formulas carry superscript $S_6$, while the prose twice describes $S_3\times S_2\times S_1$ as a Young subgroup of $S_7$ and asks for decompositions "of $S_7$". The prose reading is taken here: under the exam's own preamble convention a Young subgroup $S_{\lambda_1}\times\cdots\times S_{\lambda_k}$ sits in $S_n$ for $\lambda$ a partition of $n$, so the subgroup of $S_7$ is the one for the padded partition $(3,2,1,1)$, and the induction target is $S_7$.
:::

::: {.solution}
We use the Frobenius characteristic map. Under this map, induction from a Young subgroup corresponds to multiplication of Schur functions, while tensoring by the sign representation sends $s_\lambda$ to $s_{\lambda'}$.

<1>1. For part (a),
\[
\operatorname{ch}\left(\left(A^{(2,1,1)}\boxtimes A^{(2,2)}\right)\uparrow_{S_4\times S_4}^{S_8}\right)
=s_{(2,1,1)}s_{(2,2)}.
\]
Moreover
\[
s_{(2,2)}=h_2^2-h_3h_1.
\]
::: {.proof}
The first assertion is the induction-product property of the Frobenius characteristic. The second is the Jacobi--Trudi determinant
\[
s_{(2,2)}=
\det\begin{pmatrix}h_2&h_3\\ h_1&h_2\end{pmatrix}
=h_2^2-h_3h_1.
\]
:::

<1>2. Repeated application of the Pieri rule gives
\[
\begin{aligned}
s_{(2,1,1)}h_2^2
={}&s_{(2,2,2,1,1)}+2s_{(3,2,1,1,1)}+2s_{(3,2,2,1)}+2s_{(3,3,1,1)}+s_{(3,3,2)}\\
&+s_{(4,1,1,1,1)}+4s_{(4,2,1,1)}+s_{(4,2,2)}+2s_{(4,3,1)}\\
&+2s_{(5,1,1,1)}+2s_{(5,2,1)}+s_{(6,1,1)},
\end{aligned}
\]
and
\[
\begin{aligned}
s_{(2,1,1)}h_3h_1
={}&s_{(3,2,1,1,1)}+s_{(3,2,2,1)}+s_{(3,3,1,1)}+s_{(4,1,1,1,1)}\\
&+3s_{(4,2,1,1)}+s_{(4,2,2)}+s_{(4,3,1)}\\
&+2s_{(5,1,1,1)}+2s_{(5,2,1)}+s_{(6,1,1)}.
\end{aligned}
\]
::: {.proof}
The Pieri rule says that $s_\lambda h_r$ is the sum of $s_\mu$ over partitions $\mu$ for which $\mu/\lambda$ is a horizontal $r$-strip, each with coefficient $1$.
First,
\[
s_{(2,1,1)}h_2
=s_{(2,2,1,1)}+s_{(3,1,1,1)}+s_{(3,2,1)}+s_{(4,1,1)},
\]
while
\[
s_{(2,1,1)}h_3
=s_{(3,2,1,1)}+s_{(4,1,1,1)}+s_{(4,2,1)}+s_{(5,1,1)}.
\]
Applying Pieri once more, with $h_2$ in the first line and $h_1$ in the second, and collecting equal partitions gives exactly the two displayed expansions.
:::

<1>3. Therefore
\[
\begin{aligned}
\left(A^{(2,1,1)}\boxtimes A^{(2,2)}\right)\uparrow_{S_4\times S_4}^{S_8}
\cong{}&A^{(2,2,2,1,1)}\oplus A^{(3,2,1,1,1)}\oplus A^{(3,2,2,1)}\\
&\oplus A^{(3,3,1,1)}\oplus A^{(3,3,2)}\oplus A^{(4,2,1,1)}\oplus A^{(4,3,1)}.
\end{aligned}
\]
::: {.proof}
Subtract the two expansions in <1>2 according to <1>1. All terms not displayed cancel, and each surviving Schur function has coefficient $1$. The Frobenius characteristic is injective on the complex representation ring of $S_8$, so the Schur expansion gives the stated irreducible decomposition.
:::

For part (b), interpret the source as in the remark: the subgroup is the Young subgroup of type $(3,2,1,1)$ in $S_7$; the extra $S_1$ factor is invisible as an abstract direct factor.

<1>4. The induced trivial representation has Frobenius characteristic
\[
s_{(3)}s_{(2)}s_{(1)}^2.
\]
Repeated Pieri gives
\[
\begin{aligned}
s_{(3)}s_{(2)}s_{(1)}^2
={}&s_{(3,2,1,1)}+s_{(3,2,2)}+2s_{(3,3,1)}+s_{(4,1,1,1)}\\
&+4s_{(4,2,1)}+3s_{(4,3)}+3s_{(5,1,1)}+4s_{(5,2)}+3s_{(6,1)}+s_{(7)}.
\end{aligned}
\]
::: {.proof}
First Pieri gives
\[
s_{(3)}s_{(2)}=s_{(3,2)}+s_{(4,1)}+s_{(5)}.
\]
Multiplying by one copy of $s_{(1)}=h_1$ gives
\[
s_{(3,2,1)}+s_{(3,3)}+s_{(4,1,1)}+2s_{(4,2)}+2s_{(5,1)}+s_{(6)}.
\]
A second multiplication by $h_1$ and another application of Pieri gives the displayed degree-$7$ expansion.
:::

<1>5. Hence
\[
\begin{aligned}
T\uparrow_{S_3\times S_2\times S_1}^{S_7}
\cong{}&A^{(3,2,1,1)}\oplus A^{(3,2,2)}\oplus2A^{(3,3,1)}\oplus A^{(4,1,1,1)}\\
&\oplus4A^{(4,2,1)}\oplus3A^{(4,3)}\oplus3A^{(5,1,1)}\\
&\oplus4A^{(5,2)}\oplus3A^{(6,1)}\oplus A^{(7)}.
\end{aligned}
\]
::: {.proof}
This is the representation decomposition corresponding to the Schur expansion in <1>4.
:::

<1>6. The alternating induction is obtained from <1>5 by conjugating every partition:
\[
\begin{aligned}
\mathrm{Alt}\uparrow_{S_3\times S_2\times S_1}^{S_7}
\cong{}&A^{(1^7)}\oplus3A^{(2,1^5)}\oplus4A^{(2,2,1,1,1)}\oplus3A^{(2,2,2,1)}\\
&\oplus3A^{(3,1,1,1,1)}\oplus4A^{(3,2,1,1)}\oplus2A^{(3,2,2)}\\
&\oplus A^{(3,3,1)}\oplus A^{(4,1,1,1)}\oplus A^{(4,2,1)}.
\end{aligned}
\]
::: {.proof}
Let $H=S_3\times S_2\times S_1\times S_1\le S_7$. The alternating representation in the problem is the restriction of the sign representation $\operatorname{sgn}_{S_7}$ to $H$. For any $H$-module $V$ and $S_7$-module $W$ there is a natural isomorphism
\[
\operatorname{Ind}_H^{S_7}(V\otimes\operatorname{Res}_H W)
\cong
\operatorname{Ind}_H^{S_7}(V)\otimes W.
\]
Taking $V$ trivial and $W=\operatorname{sgn}_{S_7}$ shows that the alternating induction is the sign twist of the trivial induction. Since
\[
A^\lambda\otimes\operatorname{sgn}\cong A^{\lambda'},
\]
conjugating the partitions in <1>5 gives exactly the displayed decomposition.
:::

For part (c), use the conjugacy classes of $S_5$ in the order
\[
(5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5),
\]
whose sizes are
\[
24,30,20,20,15,10,1.
\]

<1>7. The character of $A^{(3,2)}$ on these classes is
\[
\chi^{(3,2)}=(0,-1,1,-1,1,1,5).
\]
Consequently the character of $A^{(3,2)}\otimes A^{(3,2)}$ is
\[
(0,1,1,1,1,1,25).
\]
::: {.proof}
The first row follows from the Murnaghan--Nakayama rule applied to the diagram $(3,2)$; at the identity the value is $5$ by the hook-length formula. Characters multiply pointwise under tensor product, so squaring the seven entries gives the second row.
:::

<1>8. The pointwise square in <1>7 is the sum of the irreducible characters indexed by
\[
(5),\ (4,1),\ (3,2),\ (3,1,1),\ (2,2,1),\ (2,1,1,1),
\]
each with multiplicity $1$, and has zero inner product with the sign character $(1^5)$.
::: {.proof}
On the same ordered conjugacy classes, these six irreducible rows are
\[
\begin{array}{c|rrrrrrr}
(5)&1&1&1&1&1&1&1\\
(4,1)&-1&0&-1&1&0&2&4\\
(3,2)&0&-1&1&-1&1&1&5\\
(3,1,1)&1&0&0&0&-2&0&6\\
(2,2,1)&0&1&-1&-1&1&-1&5\\
(2,1,1,1)&-1&0&1&1&0&-2&4.
\end{array}
\]
These rows are obtained from Murnaghan--Nakayama (with the dimensions at $(1^5)$ given by the hook-length formula). Adding them columnwise gives
\[
(0,1,1,1,1,1,25),
\]
which is exactly the tensor-square character from <1>7. The remaining irreducible character is the sign character. The six displayed rows together with the sign character form all seven irreducible characters of $S_5$; since the tensor-square character already equals the sum of the six displayed rows, uniqueness of irreducible-character expansion gives sign multiplicity $0$.
:::

<1>9. Therefore
\[
\boxed{
A^{(3,2)}\otimes A^{(3,2)}
\cong
A^{(5)}\oplus A^{(4,1)}\oplus A^{(3,2)}\oplus A^{(3,1,1)}\oplus A^{(2,2,1)}\oplus A^{(2,1,1,1)}.}
\]
::: {.proof}
This is precisely the irreducible-character identity proved in <1>8.
:::
:::
