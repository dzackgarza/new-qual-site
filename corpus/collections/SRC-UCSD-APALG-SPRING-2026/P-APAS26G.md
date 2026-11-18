---
schema: qual/card@1
id: P-APAS26G
kind: problem
title: Eigenvalues and eigenspaces of the $3$-cube adjacency operator
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the chi_J are the characters of (Z/2)^3
    and are orthonormal after normalisation (the sum over S of chi_J chi_K vanishing for J
    different K by the half-splitting argument, and being 8 for J = K), the action of the
    adjacency operator A f (x) = sum_i f(x + e_i) and the eigenvalue 3 - 2|J| on each
    character, the multiplicities binomial(3,k), and that the normalised characters with |J|
    = k form an orthonormal basis of each eigenspace because their number equals the
    multiplicity. The argument is the card's own; no retained set is cited. No repair needed
    to the answers.
---

::: {.problem}
Let $G = (S, T)$ be the graph whose vertex set $S$ consists of all bitstrings of length $3$, with $\{s_1, s_2\} \in T$ an edge if and only if $s_1$ and $s_2$ differ by a single bit.
Let $A \in \operatorname{End}\mathcal{F}(S)$ be the adjacency operator of $G$.
Find the eigenvalues of $A$, and give an orthonormal basis for each eigenspace.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $S=(\ZZ/2\ZZ)^{3}$ and $\mathcal{F}(S)$ for the complex-valued functions on $S$, with the inner product $\langle f,g\rangle=2^{-3}\sum_{x\in S}\overline{f(x)}g(x)$.

::: pf

::: {.pf-step #basis}
The functions $\chi_{J}(x)=(-1)^{\sum_{j\in J}x_{j}}$, for $J\subseteq\{1,2,3\}$, are the characters of the group $(\ZZ/2)^{3}$; the $2^{-3/2}\chi_{J}$ form an orthonormal basis of $\mathcal{F}(S)$, eight functions in all.

::: pf-proof
Each $\chi_{J}$ is a homomorphism $(\ZZ/2)^{3}\to\{\pm1\}\subset\CC^{\times}$, since $x\mapsto(-1)^{x_{j}}$ is and a product of homomorphisms is one. For $J\ne K$ choose $j$ in the symmetric difference; then $\chi_{J}\chi_{K}=\chi_{J\triangle K}$ takes the value $-1$ on the vectors with $x_{j}=1$, which are exactly half of the $8$ elements, so $\sum_{x}\chi_{J}(x)\chi_{K}(x)=0$; and for $J=K$ the product is $\chi_{\varnothing}\equiv1$ and the sum is $8$. Hence $\langle\chi_{J},\chi_{K}\rangle=2^{-3}\cdot8=1$ if $J=K$ and $0$ otherwise, and the eight orthonormal vectors form a basis of the $8$-dimensional space.
:::

:::

::: {.pf-step #operator}
$Af(x)=\sum_{i=1}^{3}f(x+e_{i})$ for the standard basis vectors $e_{i}$ of $(\ZZ/2)^{3}$, and $A\chi_{J}=(3-2\abs{J})\chi_{J}$.

::: pf-proof
The neighbours of $x$ in the cube are exactly $x+e_{1}$, $x+e_{2}$, $x+e_{3}$, since adding $e_{i}$ flips the $i$-th bit and two vertices are joined exactly when they differ in one bit. And
$$
\chi_{J}(x+e_{i})=(-1)^{\sum_{j\in J}\big(x_{j}+\delta_{ij}\big)}=(-1)^{\mathbf{1}_{i\in J}}\chi_{J}(x),
$$
so summing over $i$ multiplies $\chi_{J}(x)$ by $\sum_{i=1}^{3}(-1)^{\mathbf{1}_{i\in J}}=\abs{J}^{c}-\abs{J}=3-2\abs{J}$, the three indices splitting into those in $J$ and those not.
:::

:::

::: {.pf-step #eigenvalues}
The eigenvalues of $A$ are $3,1,-1,-3$ with multiplicities $1,3,3,1$.

::: pf-proof
By step [](#operator){.pf-ref} each of the eight basis vectors $2^{-3/2}\chi_{J}$ is an eigenvector with eigenvalue $3-2\abs{J}$, and by step [](#basis){.pf-ref} they form a basis, so $A$ is diagonalizable with exactly these eigenvalues. The value $3-2\abs{J}$ depends only on $\abs{J}$, and the number of subsets of size $k$ is $\binom{3}{k}$, giving multiplicities $1,3,3,1$ for $k=0,1,2,3$, that is for the eigenvalues $3,1,-1,-3$.
:::

:::

::: {.pf-step #eigenspaces}
An orthonormal basis of the eigenspace for $3-2k$ is $\{2^{-3/2}\chi_{J}:\abs{J}=k\}$, namely
$$
E_{3}=\langle 2^{-3/2}\chi_{\varnothing}\rangle,\quad
E_{1}=\langle 2^{-3/2}\chi_{\{1\}},2^{-3/2}\chi_{\{2\}},2^{-3/2}\chi_{\{3\}}\rangle,
$$
$$
E_{-1}=\langle 2^{-3/2}\chi_{\{1,2\}},2^{-3/2}\chi_{\{1,3\}},2^{-3/2}\chi_{\{2,3\}}\rangle,\quad
E_{-3}=\langle 2^{-3/2}\chi_{\{1,2,3\}}\rangle .
$$

::: pf-proof
Each $2^{-3/2}\chi_{J}$ is an eigenvector for $3-2\abs{J}$ by step [](#operator){.pf-ref}, the set of them with a fixed $\abs{J}=k$ is orthonormal by step [](#basis){.pf-ref}, and its size $\binom{3}{k}$ equals the multiplicity of that eigenvalue by step [](#eigenvalues){.pf-ref}; so the set is an orthonormal basis of the eigenspace.
:::

:::

::: {.pf-step}
The eigenvalues and an orthonormal basis of each eigenspace are as displayed.

::: pf-proof
Steps [](#eigenvalues){.pf-ref} and [](#eigenspaces){.pf-ref} give the eigenvalues with their multiplicities and the orthonormal bases.
:::

:::

:::
:::
