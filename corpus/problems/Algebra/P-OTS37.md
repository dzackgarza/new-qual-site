---
schema: qual/card@1
id: P-OTS37
kind: problem
title: Left, right, and two-sided ideals in $M_n(K)$, and simple one-sided ideals in $\Endo_K(V)$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Semisimplicity
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $V$ be an $n$-dimensional vector space over a field $K$, and identify $M_n(K)$ with $\Endo_K(V)$.
Describe the left, right, and two-sided ideals of $M_n(K)$, and identify the simple left and right ideals geometrically.
:::

::: {.solution}
Fix a basis of $V\cong K^n$, write elements of $V$ as columns, and write multiplication in $\Endo_K(V)$ as composition. Let $E_{k\ell}$ be the matrix units. For a subspace $U\le V$ and a subspace $W\le V$ put
$$
L_U\coloneqq\{f\in\Endo_K(V):U\subseteq\ker f\},\qquad R_W\coloneqq\{f\in\Endo_K(V):\im f\subseteq W\}.
$$

::: pf

::: {.pf-step #left}

The left ideals of $M_n(K)$ are exactly the $L_U$ for subspaces $U\le V$.

::: pf-proof

$L_U$ is a left ideal: it is a subspace, and if $f$ vanishes on $U$, then so does $g\circ f$ for every $g$.

Conversely, let $L$ be a left ideal, and let $R\le K^n$ be the span of all rows of all elements of $L$. For $f\in L$ the product $E_{ki}f$ has row $k$ equal to row $i$ of $f$ and all other rows $0$, so sums $\sum_j c_jE_{ki_j}f_j$ show that $L$ contains every matrix whose only nonzero row is row $k$ and lies in $R$. Adding such matrices, $L$ is the set of all matrices whose rows lie in $R$. A matrix has all rows in $R$ exactly when it vanishes on $U\coloneqq\{v\in K^n:rv=0\text{ for all }r\in R\}$, so $L=L_U$.

:::

:::

::: {.pf-step #right}

The right ideals of $M_n(K)$ are exactly the $R_W$ for subspaces $W\le V$.

::: pf-proof

$R_W$ is a right ideal, because $\im(f\circ g)\subseteq\im f\subseteq W$.

Conversely, let $R$ be a right ideal and $W$ the span of all columns of all elements of $R$. For $f\in R$, the product $fE_{ik}$ has column $k$ equal to column $i$ of $f$ and all other columns $0$; as in step [](#left){.pf-ref}, $R$ is the set of all matrices whose columns lie in $W$, that is, $R=R_W$.

:::

:::

::: pf-step

The only two-sided ideals are $0$ and $M_n(K)$.

::: pf-proof

Let $I\ne0$ be a two-sided ideal and choose $0\ne A=(a_{ij})\in I$ with $a_{ij}\ne0$. Then
$$
E_{ki}AE_{j\ell}=a_{ij}E_{k\ell}\in I.
$$
Since $a_{ij}$ is invertible in $K$, every matrix unit $E_{k\ell}$ belongs to $I$. Hence $I=M_n(K)$.

:::

:::

::: pf-step

A simple left ideal is $L_U$ for a hyperplane $U$: the maps that factor through the one-dimensional quotient $V/U$. A simple right ideal is $R_W$ for a line $W$: the maps with image in $W$.

::: pf-proof

By step [](#left){.pf-ref}, $U\mapsto L_U$ is an inclusion-reversing bijection from subspaces of $V$ to left ideals, with $L_V=0$. So the minimal nonzero left ideals are the $L_U$ with $U$ maximal among proper subspaces, that is, $U$ a hyperplane. By step [](#right){.pf-ref}, $W\mapsto R_W$ is an inclusion-preserving bijection with $R_0=0$, so the minimal nonzero right ideals are the $R_W$ with $\dim W=1$.

:::

:::

:::

:::
