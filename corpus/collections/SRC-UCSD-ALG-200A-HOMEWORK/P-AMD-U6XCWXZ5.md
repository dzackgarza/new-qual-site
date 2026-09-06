---
schema: qual/card@1
id: P-AMD-U6XCWXZ5
kind: problem
title: Groups of order 75
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 5, Exercise 4. Restored
    the source hint to use Aut(C5 x C5), including its order and conjugacy of
    subgroups of order 3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    The Sylow 5-subgroup is unique and has type C25 or C5 x C5. Every group is
    its semidirect product with C3. Since |Aut(C25)|=20, that action is trivial.
    For C5 x C5, Aut is GL(2,5) of order 480, whose order-3 subgroups are Sylow
    3-subgroups and hence conjugate. Thus there is one trivial and one
    nontrivial action in the elementary-abelian case, giving exactly three
    groups in total.
---

::: {.problem}
Classify groups of order
\[
75=3\cdot5^2
\]
up to isomorphism.

Hint: determine the order of
\[
\operatorname{Aut}(C_5\times C_5)
\]
and show that all of its subgroups of order $3$ are conjugate.
:::

::: {.solution}
<1>1. Every group $G$ of order $75$ has a unique Sylow $5$-subgroup $N$.
::: {.proof}
Let $n_5$ be the number of Sylow $5$-subgroups.
Sylow's theorem gives
\[
n_5\equiv1\pmod5
\qquad\text{and}\qquad
n_5\mid3.
\]
Thus $n_5\in\{1,3\}$.
Since $3\not\equiv1\pmod5$,
\[
n_5=1.
\]
Hence
\[
N\normal G,
\qquad
|N|=25.
\]
:::

<1>2. The normal subgroup $N$ is isomorphic to either
\[
C_{25}
\qquad\text{or}\qquad
C_5\times C_5.
\]
::: {.proof}
Every group of order $p^2$ is abelian.
The classification of finite abelian groups therefore gives precisely the two possibilities
\[
C_{25}
\qquad\text{and}\qquad
C_5\times C_5.
\]
:::

<1>3. Every group $G$ of order $75$ has the form
\[
G\cong N\rtimes_\psi C_3
\]
for one of the two groups $N$ in <1>2.
::: {.proof}
Let $P$ be a Sylow $3$-subgroup of $G$.
Then
\[
P\cong C_3,
\qquad
N\cap P=\{1\}.
\]
Since $N\normal G$, the product $NP$ is a subgroup and
\[
|NP|=|N||P|=25\cdot3=75=|G|.
\]
Thus $G=NP$.
Conjugation by $P$ on $N$ gives a homomorphism
\[
\psi:P\longrightarrow\operatorname{Aut}(N),
\]
and the internal semidirect-product theorem yields
\[
G\cong N\rtimes_\psi P
\cong N\rtimes_\psi C_3.
\]
:::

<1>4. If $N\cong C_{25}$, the action of $C_3$ on $N$ is necessarily trivial.
::: {.proof}
A generator of $C_{25}$ may be sent by an automorphism to any of the
\[
\varphi(25)=25-5=20
\]
generators of $C_{25}$.
Hence
\[
|\operatorname{Aut}(C_{25})|=20.
\]
For a homomorphism
\[
\psi:C_3\longrightarrow\operatorname{Aut}(C_{25}),
\]
the image has order dividing both $3$ and $20$.
Therefore
\[
|\operatorname{im}\psi|=1,
\]
so $\psi$ is trivial.
:::

<1>5. The case $N\cong C_{25}$ gives exactly one group,
\[
G_1=C_{25}\times C_3\cong C_{75}.
\]
::: {.proof}
By <1>4 the semidirect product is a direct product.
Since $25$ and $3$ are coprime,
\[
C_{25}\times C_3\cong C_{75}.
\]
:::

Assume from now on that
\[
N\cong C_5\times C_5.
\]
Identify $N$ with the additive group of the two-dimensional vector space
\[
V=\mathbb F_5^2.
\]

<1>6. One has
\[
\operatorname{Aut}(N)\cong\operatorname{GL}_2(\mathbb F_5)
\]
and
\[
|\operatorname{Aut}(N)|=480.
\]
::: {.proof}
An automorphism of the additive group $V$ is exactly an invertible $\mathbb F_5$-linear map, so
\[
\operatorname{Aut}(N)\cong\operatorname{GL}_2(\mathbb F_5).
\]
To choose an invertible $2\times2$ matrix over $\mathbb F_5$, its first column may be any nonzero vector, giving
\[
5^2-1=24
\]
choices.
Its second column may be any vector outside the one-dimensional span of the first column, giving
\[
5^2-5=20
\]
choices.
Thus
\[
|\operatorname{GL}_2(\mathbb F_5)|
=(25-1)(25-5)
=24\cdot20
=480
=2^5\cdot3\cdot5.
\]
:::

<1>7. Every subgroup of order $3$ in $\operatorname{Aut}(N)$ is a Sylow $3$-subgroup, and all such subgroups are conjugate.
::: {.proof}
By <1>6, the highest power of $3$ dividing
\[
|\operatorname{Aut}(N)|=480
\]
is $3$ itself.
Thus every subgroup of order $3$ is a Sylow $3$-subgroup.
Sylow's conjugacy theorem says that all Sylow $3$-subgroups are conjugate.
:::

<1>8. Up to isomorphism, there is exactly one nontrivial action
\[
C_3\longrightarrow\operatorname{Aut}(C_5\times C_5).
\]
::: {.proof}
Any nontrivial homomorphism
\[
\psi:C_3\longrightarrow\operatorname{Aut}(N)
\]
is injective because $C_3$ has prime order.
Hence its image is a subgroup of order $3$.

Let $\psi_1$ and $\psi_2$ be two nontrivial actions.
By <1>7 there exists
\[
\theta\in\operatorname{Aut}(N)
\]
such that conjugation by $\theta$ carries $\operatorname{im}\psi_1$ to $\operatorname{im}\psi_2$.
Exercise 1(a) shows that conjugating an action by $\theta$ does not change the isomorphism type of the semidirect product.
After this conjugation, the two actions have the same image, a cyclic group of order $3$.
The two resulting isomorphisms from $C_3$ onto that image differ by an automorphism of $C_3$.
Exercise 1(b) shows that precomposing by such an automorphism also does not change the semidirect-product isomorphism type.
Therefore all nontrivial actions give one isomorphism class.
:::

<1>9. A representative nontrivial action is given by the matrix
\[
A=
\begin{pmatrix}
0&-1\\
1&-1
\end{pmatrix}
\in\operatorname{GL}_2(\mathbb F_5),
\]
which has order $3$.
::: {.proof}
A direct multiplication gives
\[
A^2=
\begin{pmatrix}
-1&1\\
-1&0
\end{pmatrix}
\]
and
\[
A^3=I.
\]
Since $A\ne I$, its order is exactly $3$.
Thus a generator of $C_3$ may act on $V$ by $A$.
:::

<1>10. The case $N\cong C_5\times C_5$ gives exactly two groups:
\[
G_2=(C_5\times C_5)\times C_3
\]
and the nonabelian semidirect product
\[
G_3=(C_5\times C_5)\rtimes_A C_3.
\]
::: {.proof}
The trivial action gives $G_2$.
By <1>8, every nontrivial action gives the same isomorphism class, and <1>9 supplies the representative $G_3$.
Since $A\ne I$, the $C_3$-factor does not centralize $N$, so $G_3$ is nonabelian.
:::

<1>11. The three groups $G_1,G_2,G_3$ are pairwise nonisomorphic.
::: {.proof}
The group $G_3$ is nonabelian, whereas $G_1$ and $G_2$ are abelian, so
\[
G_3\not\cong G_1,
\qquad
G_3\not\cong G_2.
\]
The Sylow $5$-subgroup of $G_1$ is cyclic:
\[
\operatorname{Syl}_5(G_1)\cong C_{25},
\]
whereas the Sylow $5$-subgroup of $G_2$ is
\[
\operatorname{Syl}_5(G_2)\cong C_5\times C_5.
\]
Thus
\[
G_1\not\cong G_2.
\]
:::

<1>12. The complete classification of groups of order $75$ is
\[
C_{75},
\qquad
C_5\times C_5\times C_3,
\qquad
(C_5\times C_5)\rtimes_A C_3,
\]
with $A$ as in <1>9.
::: {.proof}
By <1>1--<1>3, every group of order $75$ is a semidirect product of a group of order $25$ by $C_3$.
The cyclic order-$25$ case is exhausted by <1>4--<1>5, and the elementary-abelian order-$25$ case is exhausted by <1>6--<1>10. The resulting three groups are pairwise nonisomorphic by <1>11.
:::
:::
