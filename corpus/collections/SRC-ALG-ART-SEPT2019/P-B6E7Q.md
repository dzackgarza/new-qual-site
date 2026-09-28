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
**(a)** Let $g \in G$.
As $g^N=1$ for some $N$, the minimal polynomial of $\rho(g)$ divides $x^N-1$, which has distinct linear factors over $\CC$.
Hence, $\rho(g)$ is diagonalizable, say to $\operatorname{diag}(c_1,\dots,c_n)$, each $c_i$ a root of unity.
So $\chi(g) = c_1+\cdots+c_n$, and by the triangle inequality $|c_1+\cdots+c_n| \le |c_1|+\cdots+|c_n| = n$, with equality iff $c_1=\cdots=c_n$.

Now $\chi(g)=\chi(1) \iff c_1+\cdots+c_n = n \iff c_1=\cdots=c_n=1 \iff \rho(g)=I \iff g\in\ker\rho$.

**(b)** Column orthogonality of $C_1$ and $C_2$ gives
$$1-4-4+9+9-16+16+25-\delta^2=0,$$
so $\delta^2=36$ and $\delta=6$.

The character $\psi=\chi_2\overline{\chi_2}-\chi_1$ is real-valued, has degree $3$, and satisfies $(\psi,\chi_1)=(\chi_2,\chi_2)-1=0$. With $\delta=6$, the only irreducible characters of degree at most $3$ other than $\chi_1$ are $\chi_2,\chi_3$ (degree $2$) and $\chi_4,\chi_5$ (degree $3$), and $\chi_1$ is the only one of degree $1$. Hence $\psi\in\{\chi_4,\chi_5\}$. Each of $\chi_4,\chi_5$ takes both values $\alpha$ and $\beta$, so $\alpha,\beta\in\RR$.

Column orthogonality now gives
$$0 = C_4\cdot C_7 = 4\gamma,\qquad 0 = C_4\cdot C_5 = 1-(\alpha+\beta),\qquad 0 = C_8\cdot C_9 = 4+4\alpha\beta,$$
where the first uses nothing about $\alpha,\beta$ and the last two use $\gamma=0$. So $\gamma=0$, and $\alpha,\beta$ are the roots of $x^2-x-1$, giving $\alpha,\beta = \dfrac{1\pm\sqrt5}{2}$.

**(c)** $Z(G) =$ union of classes of size $1$.
So $Z(G) = C_1 \cup C_2$, size $2$, while $|G|=120$.
So $|G/Z(G)| = 60$.

If $C_2=\{z\}$, $z^2=1$, so it's either $+1$ or $-1$ on each irrep.
The irreps of $G/Z(G)$ are the same as ones of $G$ on which $z$ is $+1$.
Classes in $G/Z(G)$ are either images of $1$ or $2$ classes in $G$:

|  | $C_1\cup C_2$ | $C_3\cup C_7$ | $C_4$ | $C_5\cup C_9$ | $C_6\cup C_8$ |
| --- | --- | --- | --- | --- | --- |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 |
| $\chi_4$ | 3 | 0 | -1 | $\beta$ | $\alpha$ |
| $\chi_5$ | 3 | 0 | -1 | $\alpha$ | $\beta$ |
| $\chi_7$ | 4 | 1 | 0 | -1 | -1 |
| $\chi_8$ | 5 | -1 | 1 | 0 | 0 |

The group $H$ is simple of order $60$, hence $H\cong A_5$.

The conjugacy classes of $H$ have sizes $1, 20, 15, 12, 12$ (each merged pair, and $C_4$, has half the total size in $G$). A normal subgroup of $H$ is a union of conjugacy classes containing the identity class, and its order divides $60$. No sum of $1$ with a nonempty proper subcollection of $\{20,15,12,12\}$ divides $60$, so $H$ has no nontrivial proper normal subgroup.
Hence $H$ is simple of order $60$, and every simple group of order $60$ is isomorphic to $A_5$.
:::
