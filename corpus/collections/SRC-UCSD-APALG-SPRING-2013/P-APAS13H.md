---
schema: qual/card@1
id: P-APAS13H
kind: problem
title: Induced trivial and alternating characters; Kronecker and outer products of Specht modules
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: problem
Suppose that $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$.
Then $A^\lambda$ denotes the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$, and $S_{\lambda_1}\times\cdots\times S_{\lambda_k}$ denotes the Young subgroup of $S_n$ corresponding to $\lambda$.

(a) Let $T$ denote the trivial representation on the Young subgroup $S_2\times S_3\times S_1$ of $S_6$ and $\mathrm{Alt}$ denote the alternating representation on the Young subgroup $S_2\times S_3\times S_1$ of $S_6$.
Express the characters of
\[
T\uparrow_{S_2\times S_3\times S_1}^{S_6}
\quad\text{and}\quad
\mathrm{Alt}\uparrow_{S_2\times S_3\times S_1}^{S_6}
\]
as a sum of irreducible characters of $S_6$.

(b) Find the decomposition of the Kronecker product $A^{(4,1)}\otimes A^{(2,2,1)}$ as a sum of irreducible representations of $S_5$.

(c) Find the decomposition of $A^{(2,1)}\times A^{(3,1)}\uparrow_{S_3\times S_4}^{S_7}$ as a sum of irreducible representations of $S_7$.
:::

::: solution
Under the Frobenius characteristic map, induction from a Young subgroup corresponds to multiplication of symmetric functions.

For part (a), the trivial character of \(S_r\) has Frobenius image \(h_r=s_{(r)}\). Hence
\[
\operatorname{ch}\left(T\uparrow_{S_2\times S_3\times S_1}^{S_6}\right)
=h_2h_3h_1.
\]
Applying the Pieri rule twice gives
\[
h_2h_3h_1
=s_{(6)}+2s_{(5,1)}+2s_{(4,2)}+s_{(4,1,1)}+s_{(3,3)}+s_{(3,2,1)}.
\]
Therefore
\[
T\uparrow_{S_2\times S_3\times S_1}^{S_6}
\cong
A^{(6)}\oplus2A^{(5,1)}\oplus2A^{(4,2)}\oplus A^{(4,1,1)}
\oplus A^{(3,3)}\oplus A^{(3,2,1)}.
\]

The alternating character of \(S_r\) has Frobenius image \(e_r=s_{(1^r)}\). Thus
\[
\operatorname{ch}\left(\mathrm{Alt}\uparrow_{S_2\times S_3\times S_1}^{S_6}\right)
=e_2e_3e_1.
\]
By the vertical-strip form of the Pieri rule,
\[
e_2e_3e_1
=s_{(1^6)}+2s_{(2,1,1,1,1)}+2s_{(2,2,1,1)}+s_{(2,2,2)}
+s_{(3,1,1,1)}+s_{(3,2,1)}.
\]
Hence
\[
\mathrm{Alt}\uparrow_{S_2\times S_3\times S_1}^{S_6}
\cong
A^{(1^6)}\oplus2A^{(2,1,1,1,1)}\oplus2A^{(2,2,1,1)}
\oplus A^{(2,2,2)}\oplus A^{(3,1,1,1)}\oplus A^{(3,2,1)}.
\]

For part (b), the Kronecker product is computed by pointwise multiplication of characters. Equivalently, in the Schur basis one uses the internal product. The decomposition is
\[
\boxed{
A^{(4,1)}\otimes A^{(2,2,1)}
\cong
A^{(3,2)}\oplus A^{(3,1,1)}\oplus A^{(2,2,1)}\oplus A^{(2,1,1,1)}.}
\]
A check by dimensions gives
\[
\dim A^{(4,1)}\,\dim A^{(2,2,1)}=4\cdot5=20,
\]
while the four dimensions on the right are \(5,6,5,4\), whose sum is \(20\).

For part (c), induction from \(S_3\times S_4\) corresponds to the ordinary product
\[
s_{(2,1)}s_{(3,1)}.
\]
The Littlewood--Richardson rule gives
\[
\begin{aligned}
s_{(2,1)}s_{(3,1)}={}&
 s_{(5,2)}+s_{(5,1,1)}+s_{(4,3)}+2s_{(4,2,1)}+s_{(4,1,1,1)}\\
&+s_{(3,3,1)}+s_{(3,2,2)}+s_{(3,2,1,1)}.
\end{aligned}
\]
Therefore
\[
\boxed{
\begin{aligned}
\left(A^{(2,1)}\times A^{(3,1)}\right)\uparrow_{S_3\times S_4}^{S_7}
\cong{}&A^{(5,2)}\oplus A^{(5,1,1)}\oplus A^{(4,3)}\oplus2A^{(4,2,1)}\\
&\oplus A^{(4,1,1,1)}\oplus A^{(3,3,1)}\oplus A^{(3,2,2)}\oplus A^{(3,2,1,1)}.
\end{aligned}}
\]
:::
