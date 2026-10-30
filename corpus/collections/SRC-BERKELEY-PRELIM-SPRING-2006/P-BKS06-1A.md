---
schema: qual/card@1
id: P-BKS06-1A
kind: problem
title: Basis of the kernel of $2x+3y+5z+7w$ on $\ZZ^4$ and its free quotient
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
---

::: {.problem}
Let $G$ be the subgroup of the free abelian group $\ZZ^{4}$ consisting of all integer vectors $(x, y, z, w)$ such that $2x + 3y + 5z + 7w = 0$.

(a) Determine a linearly independent subset of $G$ which generates $G$ as an abelian group.

(b) Show that $\ZZ^{4}/G$ is a free abelian group and determine its rank.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\varphi:\ZZ^4\to\ZZ$ be $\varphi(x,y,z,w)=2x+3y+5z+7w$. Then $G=\ker\varphi$ and $\varphi$ is onto.

::: pf-proof

$G$ is the kernel by definition. Since $\varphi(-1,1,0,0)=1$, the image contains $1$, so it is $\ZZ$.

:::

:::

::: {.pf-step #s2}

$\ZZ^4/G\cong\ZZ$, a free abelian group of rank $1$.

::: pf-proof

This is the first isomorphism theorem applied to step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Let
$$
U=\begin{pmatrix}
7&9&15&-3\\
0&1&0&0\\
0&0&1&0\\
-2&-3&-5&1
\end{pmatrix}.
$$
Then $\begin{pmatrix}2&3&5&7\end{pmatrix}U=\begin{pmatrix}0&0&0&1\end{pmatrix}$ and $\det U=1$.

::: pf-proof

The four products are $14-14=0$, $18+3-21=0$, $30+5-35=0$ and $-6+7=1$. Expanding the determinant along the second and third rows gives $\det U=\det\begin{pmatrix}7&-3\\-2&1\end{pmatrix}=7-6=1$.

:::

:::

::: {.pf-step #s4}

The first three columns
$$
u_1=(7,0,0,-2),\qquad u_2=(9,1,0,-3),\qquad u_3=(15,0,1,-5)
$$
of $U$ form a linearly independent subset of $G$ that generates $G$.

::: pf-proof

By step [](#s3){.pf-ref}, $\varphi(u_1)=\varphi(u_2)=\varphi(u_3)=0$, so $u_i\in G$. They are linearly independent because $\det U\ne0$. Since $\det U=1$, the matrix $U^{-1}$ has integer entries. Let $v\in G$ and put $(\alpha,\beta,\gamma,\delta)^T=U^{-1}v\in\ZZ^4$. By step [](#s3){.pf-ref},
$$
0=\varphi(v)=\begin{pmatrix}2&3&5&7\end{pmatrix}U\,U^{-1}v=\begin{pmatrix}0&0&0&1\end{pmatrix}U^{-1}v=\delta.
$$
Hence $v=\alpha u_1+\beta u_2+\gamma u_3$ with $\alpha,\beta,\gamma\in\ZZ$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} answers part (a), and step [](#s2){.pf-ref} answers part (b): $\ZZ^4/G$ is free of rank $1$.

:::

:::

:::
