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
**(a)** Take $g \in G$.
As $g^N=1$ for some $N$, the min.
poly.
of $\rho(g)$ divides $x^N-1$, which has distinct linear factors.
Hence, $\rho(g)$ is diagonalizable, say to $\operatorname{diag}(c_1,\dots,c_n)$, each $c_i$ a root of unity.
So $\chi(g) = c_1+\cdots+c_n$, and by the triangle inequality $|c_1+\cdots+c_n| \le |c_1|+\cdots+|c_n| = n$, with equality iff $c_1=\cdots=c_n$.

Now $\chi(g)=\chi(1) \iff c_1+\cdots+c_n = n \iff c_1=\cdots=c_n=1 \iff \rho(g)=I \iff g\in\ker\rho$.

**(b)** Note $\alpha,\beta$ are real: by definition of the inner product, $(\chi_2\chi_2^*,\chi_1) = (\chi_2,\chi_2) = 1$.
So $\chi_2\chi_2^* - \chi_1$ is a character of degree 3 with no trivial constituents, so could only be $\chi_4$ or $\chi_5$ (using $\delta\ne1$, else what's $\chi_2\chi_9$?). Also real-valued, so $\alpha,\beta$ are real as values of $\chi_4/\chi_5$.

Dot columns together using this to see: $$0 = C_1\cdot C_2 \Rightarrow \delta^2 = 36 \Rightarrow \delta=6,\ \gamma=0$$ $$0 = C_4\cdot C_7 \Rightarrow 2\gamma = 0$$ $$0 = C_4\cdot C_5 \Rightarrow \alpha+\beta=1$$ $$0 = C_8\cdot C_9 \Rightarrow \alpha\beta=-1$$ so $\alpha,\beta$ are roots of $x^2-x-1$, giving $\alpha,\beta = \dfrac{1\pm\sqrt5}{2}$.

Note now we can also find the conjugacy class sizes.
(See table.)

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

Observe it's a simple group of order 60. So it must be $A_5$.

To justify this: the character table shows $H$ has no nontrivial proper normal subgroup, since a normal subgroup would be a union of conjugacy classes whose size divides $60$ and whose character-theoretic kernel is nontrivial; checking the class sizes $\{1, 1, 20, 12, 12\}$ (after merging under $Z(G)$) shows no such union forms a subgroup. Hence $H$ is simple of order $60$. The only simple group of order $60$ is $A_5$ (a standard classification: a simple group of order $60$ has $n_2 \in \{5, 15\}$ and $n_5 = 6$, forcing it to act faithfully on $5$ Sylow $2$-subgroups or $6$ Sylow $5$-subgroups, embedding it in $S_5$; the only simple subgroup of $S_5$ of order $60$ is $A_5$).
:::
