---
schema: qual/card@1
id: P-APAF22A
kind: problem
title: Jordan form of a $10\times 10$ map with a partial upper-triangular matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
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
A linear map $\phi \colon \mathbb{C}^{10} \to \mathbb{C}^{10}$ is given in the standard basis $e_1, \ldots, e_{10}$ by the matrix
\[
\begin{pmatrix}
0 & 0 & * & * & * & * & * & * & * & * \\
0 & 0 & 1 & * & * & * & * & * & * & * \\
0 & 0 & 0 & 2 & * & * & * & * & * & * \\
0 & 0 & 0 & 0 & 3 & * & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & 4 & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 5 & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 8 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix},
\]
where $*$ denotes an unknown value.

(a) Prove that $\dim \ker \phi = 2$ and that $\phi^8(e_{10}) \neq 0$.

(b) Hence, or otherwise, determine (with proof) the Jordan Normal Form of $\phi$.
:::

::: {.solution}
Let
\[
F_j=\operatorname{span}\{e_1,\ldots,e_j\}
\qquad(0\le j\le10).
\]
Because the matrix is upper triangular, $\phi(F_j)\subseteq F_{j-1}$ for every $j$.

<1>1. The rank of $\phi$ is $8$, hence
\[
\dim\ker\phi=2.
\]
::: {.proof}
The first two columns of the displayed matrix are zero, so
\[
\operatorname{rank}\phi\le8.
\]
Consider columns $3,4,\ldots,10$ and restrict to rows $2,3,\ldots,9$. The resulting $8\times8$ matrix is upper triangular with diagonal entries
\[
1,2,3,4,5,6,7,8,
\]
all nonzero. Hence these eight columns are linearly independent. Therefore
\[
\operatorname{rank}\phi=8.
\]
Rank-nullity gives
\[
\dim\ker\phi=10-8=2.
\]
:::

<1>2. For $1\le k\le8$,
\[
\phi^k(e_{10})
=8\cdot7\cdots(9-k)e_{10-k}+v_k
\]
for some
\[
v_k\in F_{9-k}.
\]
::: {.proof}
We argue by induction on $k$. For $k=1$, the tenth column of the matrix gives
\[
\phi(e_{10})=8e_9+v_1,
\qquad v_1\in F_8,
\]
which is the required formula.

Assume the formula holds for some $k<8$. The visible superdiagonal entry in column $10-k$ is $8-k$, so
\[
\phi(e_{10-k})=(8-k)e_{9-k}+w_k,
\qquad w_k\in F_{8-k}.
\]
Also $\phi(v_k)\in F_{8-k}$ because $v_k\in F_{9-k}$ and $\phi(F_{9-k})\subseteq F_{8-k}$. Therefore
\[
\begin{aligned}
\phi^{k+1}(e_{10})
&=8\cdot7\cdots(9-k)\phi(e_{10-k})+\phi(v_k)\\
&=8\cdot7\cdots(8-k)e_{9-k}+v_{k+1}
\end{aligned}
\]
with $v_{k+1}\in F_{8-k}$. This is the claimed formula for $k+1$.
:::

<1>3. In particular,
\[
\phi^8(e_{10})\ne0.
\]
::: {.proof}
Taking $k=8$ in <1>2 gives
\[
\phi^8(e_{10})=8!\,e_2+v_8,
\qquad v_8\in F_1=\mathbb Ce_1.
\]
Since $8!\ne0$ in $\mathbb C$, the coefficient of $e_2$ is nonzero. Hence the vector cannot vanish.
:::

<1>4. The map $\phi$ is nilpotent, and the number of Jordan blocks in its Jordan form is $2$.
::: {.proof}
The displayed matrix is strictly upper triangular, so $\phi^{10}=0$; hence $\phi$ is nilpotent.
For a nilpotent Jordan block $J_m(0)$, the kernel is one-dimensional. Therefore, for a direct sum of nilpotent Jordan blocks, the dimension of the kernel equals the number of blocks. By <1>1,
\[
\dim\ker\phi=2,
\]
so the Jordan form has exactly two blocks.
:::

<1>5. One Jordan block has size at least $9$.
::: {.proof}
For a nilpotent operator, the nilpotency index equals the size of its largest Jordan block. By <1>3,
\[
\phi^8\ne0,
\]
so the nilpotency index is at least $9$. Hence the largest Jordan block has size at least $9$.
:::

<1>6. Therefore the Jordan normal form is
\[
\boxed{J_9(0)\oplus J_1(0)}.
\]
::: {.proof}
By <1>4 there are exactly two Jordan blocks, and their sizes are positive integers summing to $10$. By <1>5 the larger block has size at least $9$. The only possible pair is therefore
\[
9+1=10.
\]
Thus the Jordan normal form is $J_9(0)\oplus J_1(0)$.
:::
:::
