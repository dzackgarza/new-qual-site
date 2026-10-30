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

(a) Let $\rho: G \to GL_n(\CC)$ be a finite-dimensional representation with associated character $\chi$.
Prove that $\ker\rho = \{g \in G \mid \chi(g) = \chi(1)\}$.

(b) Use the row and column orthogonality relations to work out the values of $\alpha,\beta,\gamma$ and $\delta$ in the following character table:

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

(c) Let $G$ be a group with the character table computed in (b). Work out the character table of the group $H = G/Z(G)$, explaining your steps.
What group is $H$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) $\ker\rho = \{g \in G \mid \chi(g) = \chi(1)\}$.

::: pf-proof
Let $g \in G$. As $g^N=1$ for some $N$, the minimal polynomial of $\rho(g)$ divides $x^N-1$, which has distinct roots over $\CC$. Hence $\rho(g)$ is diagonalizable, say to $\operatorname{diag}(c_1,\dots,c_n)$ with each $c_i$ a root of unity. So $\chi(g) = c_1+\cdots+c_n$, and $\abs{c_1+\cdots+c_n} \le n$, with equality if and only if $c_1=\cdots=c_n$. Therefore
$$
\chi(g)=\chi(1) \iff c_1=\cdots=c_n=1 \iff \rho(g)=I \iff g\in\ker\rho.
$$
:::

:::

::: {.pf-step #s2}
(b) $\delta=6$.

::: pf-proof
Column orthogonality of $C_1$ and $C_2$ gives
$$
1-4-4+9+9-16+16+25-\delta^2=0,
$$
so $\delta^2=36$, and $\delta=6$ because $\delta=\chi_9(1)>0$.
:::

:::

::: {.pf-step #s3}
(b) $\alpha$ and $\beta$ are real.

::: pf-proof
The character $\psi=\chi_2\overline{\chi_2}-\chi_1$ is real-valued, has degree $3$, and satisfies $(\psi,\chi_1)=(\chi_2,\chi_2)-1=0$. By step [](#s2){.pf-ref}, the irreducible characters of degree at most $3$ are $\chi_1$, $\chi_2,\chi_3$ (degree $2$) and $\chi_4,\chi_5$ (degree $3$), and only $\chi_1$ has degree $1$. Hence $\psi\in\{\chi_4,\chi_5\}$. Each of $\chi_4,\chi_5$ takes both values $\alpha$ and $\beta$, so $\alpha,\beta\in\RR$.
:::

:::

::: {.pf-step #s4}
(b) $\gamma=0$ and $\{\alpha,\beta\}=\left\{\dfrac{1+\sqrt5}{2},\dfrac{1-\sqrt5}{2}\right\}$.

::: pf-proof
Column orthogonality gives
$$
0 = C_4\cdot C_7 = 4\gamma,\qquad 0 = C_4\cdot C_5 = 1-(\alpha+\beta),\qquad 0 = C_8\cdot C_9 = 4+4\alpha\beta,
$$
where the last two use $\gamma=0$ and step [](#s3){.pf-ref}. So $\alpha,\beta$ are the roots of $x^2-x-1$.
:::

:::

::: {.pf-step #s5}
(c) $Z(G)=C_1\cup C_2$ and the character table of $H=G/Z(G)$ is

| | $C_1\cup C_2$ | $C_3\cup C_7$ | $C_4$ | $C_5\cup C_9$ | $C_6\cup C_8$ |
| --- | --- | --- | --- | --- | --- |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 |
| $\chi_4$ | 3 | 0 | -1 | $\beta$ | $\alpha$ |
| $\chi_5$ | 3 | 0 | -1 | $\alpha$ | $\beta$ |
| $\chi_7$ | 4 | 1 | 0 | -1 | -1 |
| $\chi_8$ | 5 | -1 | 1 | 0 | 0 |

::: pf-proof
$Z(G)$ is the union of the classes of size $1$, so $Z(G) = C_1 \cup C_2$ has order $2$ and $\cardinality{H} = 60$. If $C_2=\{z\}$, then $z^2=1$, so $z$ acts as $+1$ or $-1$ on each irreducible representation. The irreducible characters of $H$ are the irreducible characters of $G$ with $\chi(z)=\chi(1)$, which are $\chi_1,\chi_4,\chi_5,\chi_7,\chi_8$. Multiplication by $z$ permutes the classes of $G$, and a class of $H$ is the image of one class or of a pair of classes exchanged by $z$; comparing the values of $\chi_2$, which changes sign under $z$, shows that the pairs are $C_3,C_7$, $C_5,C_9$ and $C_6,C_8$.
:::

:::

::: {.pf-step #s6}
(c) $H\cong A_5$.

::: pf-proof
By step [](#s5){.pf-ref}, the conjugacy classes of $H$ have sizes $1, 20, 15, 12, 12$. A normal subgroup of $H$ is a union of conjugacy classes containing the identity class, and its order divides $60$. No sum of $1$ with a nonempty proper subcollection of $\{20,15,12,12\}$ divides $60$, so $H$ is simple of order $60$. Every simple group of order $60$ is isomorphic to $A_5$.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves (a), steps [](#s2){.pf-ref} and [](#s4){.pf-ref} answer (b), and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} answer (c).
:::

:::

:::
