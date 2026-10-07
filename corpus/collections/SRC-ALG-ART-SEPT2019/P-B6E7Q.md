---
schema: qual/card@1
id: P-B6E7Q
kind: problem
title: The character criterion for kernels and a character table of order 120
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Conjugacy
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group.
Adopt the usual notation for the character table of $G$.
In particular, $C_1 = \{1\}, C_2,\dots,C_n$ are the conjugacy classes and $\chi_1 = \mathbf{1}, \chi_2,\dots,\chi_n$ are the irreducible characters.

a. Let $\rho: G \to GL_n(\mathbb{C})$ be a finite-dimensional representation with associated character $\chi$.
Prove that $\ker\rho = \{g \in G \mid \chi(g) = \chi(1)\}$.
b. Use the row and column orthogonality relations to work out the values of $\alpha,\beta,\gamma$ and $\delta$ in the following character table:

|  | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ | $C_6$ | $C_7$ | $C_8$ | $C_9$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\#$ | 1 | 1 | 20 | 30 | 12 | 12 | 20 | 12 | 12 |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $\chi_2$ | 2 | -2 | -1 | $\gamma$ | $-\beta$ | $-\alpha$ | 1 | $\alpha$ | $\beta$ |
| $\chi_3$ | 2 | -2 | -1 | $\gamma$ | $-\alpha$ | $-\beta$ | 1 | $\beta$ | $\alpha$ |
| $\chi_4$ | 3 | 3 | 0 | -1 | $\beta$ | $\alpha$ | 0 | $\alpha$ | $\beta$ |
| $\chi_5$ | 3 | 3 | 0 | -1 | $\alpha$ | $\beta$ | 0 | $\beta$ | $\alpha$ |
| $\chi_6$ | 4 | -4 | 1 | $\gamma$ | -1 | -1 | 1 | 1 | 1 |
| $\chi_7$ | 4 | 4 | 1 | $\gamma$ | -1 | -1 | 1 | -1 | -1 |
| $\chi_8$ | 5 | 5 | -1 | 1 | 0 | 0 | -1 | 0 | 0 |
| $\chi_9$ | $\delta$ | $-\delta$ | 0 | $\gamma$ | 1 | 1 | 0 | -1 | -1 |

c. Let $G$ be a group with the character table computed in (b). Work out the character table of the group $H = G/Z(G)$, explaining your steps.
What group is $H$?
:::

::: {.solution}
<1>1. For any finite-dimensional complex representation $\rho$ with character $\chi$,
$$
\boxed{\ker\rho=\{g\in G:\chi(g)=\chi(1)\}}.
$$
::: {.proof}
Fix $g\in G$. Since $G$ is finite, $g$ has finite order, say $g^N=1$. Hence
$$
\rho(g)^N=I,
$$
so the minimal polynomial of $\rho(g)$ divides $x^N-1$. Over $\CC$, this polynomial has distinct roots, so $\rho(g)$ is diagonalizable with eigenvalues $c_1,\ldots,c_d$, all roots of unity, where $d=\chi(1)$.

Thus
$$
\chi(g)=c_1+\cdots+c_d,
\qquad
|c_i|=1.
$$
If $\chi(g)=d$, then
$$
d=|\chi(g)|\le \sum_i|c_i|=d.
$$
Equality in the triangle inequality forces all $c_i$ to have the same argument; since their sum is the positive real number $d$, all $c_i=1$. Hence $\rho(g)=I$. The converse is immediate.
:::

<1>2. Column orthogonality gives
$$
\boxed{\delta=6,\qquad \gamma=0}.
$$
::: {.proof}
The columns for $C_1$ and $C_2$ are distinct, so column orthogonality gives
$$
0
=1-4-4+9+9-16+16+25-\delta^2
=36-\delta^2.
$$
Since $\delta=\chi_9(1)>0$, one gets $\delta=6$.

Now orthogonality of the columns for $C_1$ and $C_4$ gives
$$
0
=1+2\gamma+2\gamma-3-3+4\gamma+4\gamma+5+6\gamma
=18\gamma,
$$
so $\gamma=0$.
:::

<1>3. The remaining parameters satisfy
$$
\boxed{\alpha+\beta=1,\qquad \alpha\beta=-1}.
$$
::: {.proof}
With $\gamma=0$, orthogonality of the columns for $C_4$ and $C_5$ gives
$$
0=1-\alpha-\beta,
$$
so $\alpha+\beta=1$.

Orthogonality of the columns for $C_8$ and $C_9$ gives
$$
0=4+4\alpha\beta,
$$
so $\alpha\beta=-1$.
:::

<1>4. Therefore
$$
\boxed{\{\alpha,\beta\}
=\left\{\frac{1+\sqrt5}{2},\frac{1-\sqrt5}{2}\right\}}.
$$
::: {.proof}
By step <1>3, $\alpha$ and $\beta$ are the two roots of
$$
t^2-t-1=0.
$$
The table is symmetric under interchanging $\alpha$ and $\beta$, so their individual labels may be swapped without changing the character table.
:::

<1>5. The center is
$$
Z(G)=C_1\union C_2,
\qquad
|Z(G)|=2,
$$
and hence
$$
|H|=|G/Z(G)|=60.
$$
::: {.proof}
An element is central exactly when its conjugacy class has size $1$. The class-size row shows that exactly $C_1$ and $C_2$ are singleton classes. Their union is therefore $Z(G)$.
:::

<1>6. Let $C_2=\{z\}$. The irreducible characters of $H=G/Z(G)$ are precisely
$$
\chi_1,\chi_4,\chi_5,\chi_7,\chi_8.
$$
::: {.proof}
An irreducible representation of $G$ descends to $H$ exactly when $z$ lies in its kernel. By step <1>1, this is equivalent to
$$
\chi(z)=\chi(1).
$$
Comparing the $C_2$ and $C_1$ entries of the table gives exactly the five displayed characters.
:::

<1>7. The conjugacy classes of $H$ have sizes
$$
\boxed{1,20,15,12,12},
$$
with preimages
$$
C_1\union C_2,
\quad
C_3\union C_7,
\quad
C_4,
\quad
C_5\union C_9,
\quad
C_6\union C_8.
$$
::: {.proof}
Multiplication by the central element $z$ permutes the conjugacy classes of $G$, and two elements of $G$ have the same image in $H$ exactly when they differ by multiplication by $z$.

The five characters from step <1>6 are constant on the fibres of $G\to H$. Comparing their columns in the given table pairs
$$
C_1\leftrightarrow C_2,
\qquad
C_3\leftrightarrow C_7,
\qquad
C_5\leftrightarrow C_9,
\qquad
C_6\leftrightarrow C_8,
$$
while $C_4$ is fixed by multiplication by $z$. Dividing each preimage size by $|Z(G)|=2$ gives
$$
1,\quad20,\quad15,\quad12,\quad12.
$$
:::

<1>8. The character table of $H$ is

|  | $D_1$ | $D_2$ | $D_3$ | $D_4$ | $D_5$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $\#$ | 1 | 20 | 15 | 12 | 12 |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 |
| $\chi_4$ | 3 | 0 | -1 | $\beta$ | $\alpha$ |
| $\chi_5$ | 3 | 0 | -1 | $\alpha$ | $\beta$ |
| $\chi_7$ | 4 | 1 | 0 | -1 | -1 |
| $\chi_8$ | 5 | -1 | 1 | 0 | 0 |

where $D_1,\ldots,D_5$ correspond in order to the five preimages in step <1>7.
::: {.proof}
The class sizes are step <1>7. The character values are read from any representative class in each preimage, because the characters in step <1>6 factor through $H$.
:::

<1>9. The group $H$ is simple.
::: {.proof}
By the table in step <1>8, for each nontrivial irreducible character of $H$, the character value equals its degree only on the identity class. By step <1>1, every nontrivial irreducible representation of $H$ is therefore faithful.

Suppose $1\ne N\trianglelefteq H$ were proper. Then the nontrivial finite group $H/N$ has a nontrivial irreducible representation. Inflating it along $H\to H/N$ gives a nontrivial irreducible representation of $H$ whose kernel contains $N$, contradicting faithfulness. Hence $H$ has no nontrivial proper normal subgroup.
:::

<1>10. Therefore
$$
\boxed{H\cong A_5}.
$$
::: {.proof}
By step <1>5, $|H|=60$, and by step <1>9, $H$ is simple. The classification proved in [[P-MMAQ-RQA4XXNOF3]] shows that every simple group of order $60$ is isomorphic to $A_5$.
:::

<1>11. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), step <1>2 through step <1>4 determine the unknown character values in part (b), and step <1>5 through step <1>10 compute the character table and identify the quotient in part (c).
:::
:::
