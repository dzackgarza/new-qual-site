---
schema: qual/card@1
id: P-APAS11C
kind: problem
title: Group determinant factorization and the circulant determinant
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the sum of the x_g A(g) reproduces X entry
    by entry, that A(g)A(h) = A(gh) with the unique contributing index g_l = g^-1 g_i, that
    A(g) is the matrix of left multiplication by g in the basis g_1..g_k so that A is the
    left regular representation, and that the determinant formula follows from the
    decomposition of the regular representation with multiplicities equal to the degrees,
    the latter now derived from C[G] isomorphic to the sum of the End(V_nu). For (c): the
    characters of Z_n, all multiplicities one, and the transpose relating the displayed
    circulant (entry x_{j-i}) to X = [x_{i-j}], which the earlier prose identified without
    stating the convention. The argument is the card's own; no retained set is cited.
review: draft
---

::: {.problem}
Let $G=\{g_1,\ldots,g_k\}$ be a finite group.
Introduce variables $x_{g_1},\ldots,x_{g_k}$ and consider the $k\times k$ matrix
$$
X=[x_{g_i g_j^{-1}}].
$$
Let
$$
X=\sum_{i=1}^{k} A(g_i)x_{g_i}
$$
so that we can define a map $g_i\mapsto A(g_i)$.

(a) Show that $A$ is the left regular representation of $G$.

(b) Show that
$$
\det(X)=\prod_{\nu=1}^{h}\det\Biggl(\sum_{g\in G}A^{(\nu)}(g)x_g\Biggr)^{n_\nu}
$$
where $A^{(1)},\ldots,A^{(h)}$ are a complete set of representatives of the irreducible representations of $G$ and $n_\nu=\dim(A^{(\nu)})$ for $\nu=1,\ldots,h$.

(c) Use part (b) to show that
$$
\det\begin{bmatrix}
x_0 & x_1 & x_2 & \cdots & x_{n-1} \\
x_{n-1} & x_0 & x_1 & \cdots & x_{n-2} \\
x_{n-2} & x_{n-1} & x_0 & \cdots & x_{n-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_1 & x_2 & x_3 & \cdots & x_0
\end{bmatrix}
=
\prod_{r=0}^{n-1}\bigl(x_0+\epsilon^r x_1+\epsilon^{2r} x_2+\cdots+\epsilon^{(n-1)r}x_{n-1}\bigr)
$$
where $\epsilon=e^{2\pi i/n}$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. It is the classical group-determinant computation of Frobenius, in the form the exercise sets it. Throughout, $G=\{g_{1},\dots,g_{k}\}$, the variables are $x_{g}$ for $g\in G$, and $\rho$ denotes the left regular representation of $\CC[G]$ on the $k$-dimensional space with basis $g_{1},\dots,g_{k}$.

::: pf

::: {.pf-step #matrix}
Definition: for $g\in G$ let $A(g)$ be the matrix with $A(g)_{ij}=1$ if $g_{i}g_{j}^{-1}=g$ and $0$ otherwise. Then $X=[x_{g_{i}g_{j}^{-1}}]=\sum_{g\in G}x_{g}A(g)$.

::: pf-proof
The $(i,j)$ entry of $\sum_{g}x_{g}A(g)$ is $\sum_{g}x_{g}A(g)_{ij}=x_{g_{i}g_{j}^{-1}}$, since exactly one summand is nonzero, the one indexed by $g=g_{i}g_{j}^{-1}$; and that is the $(i,j)$ entry of $X$ by the definition of $X$ in the statement.
:::

:::

::: {.pf-step #homomorphism}
$A(g)A(h)=A(gh)$ for all $g,h\in G$; hence each $A(g)$ is a permutation matrix and $A$ is the left regular representation.

::: pf-proof
$(A(g)A(h))_{ij}=\sum_{\ell}A(g)_{i\ell}A(h)_{\ell j}$ is the number of indices $\ell$ with $g_{i}g_{\ell}^{-1}=g$ and $g_{\ell}g_{j}^{-1}=h$. The first condition determines $\ell$ uniquely, namely $g_{\ell}=g^{-1}g_{i}$, so the sum is $1$ when that $\ell$ also satisfies the second condition and $0$ otherwise; substituting $g_{\ell}=g^{-1}g_{i}$ into the second gives $g^{-1}g_{i}g_{j}^{-1}=h$, that is $g_{i}g_{j}^{-1}=gh$. Hence $(A(g)A(h))_{ij}=1$ exactly when $g_{i}g_{j}^{-1}=gh$, which is the definition of $A(gh)_{ij}$. So $A$ is a homomorphism into $GL_{k}$. For each $g$ the matrix $A(g)$ has exactly one $1$ in each row and each column: for fixed $i$ the unique $j$ with $g_{i}g_{j}^{-1}=g$ is $g_{j}=g^{-1}g_{i}$, and for fixed $j$ the unique $i$ with $g_{i}g_{j}^{-1}=g$ is $g_{i}=gg_{j}$; so $A(g)$ is a permutation matrix. Finally, left multiplication by $g$ sends the basis vector $g_{j}$ to $gg_{j}$, whose coordinate at $g_{i}$ is $1$ exactly when $g_{i}=gg_{j}$, that is $g_{i}g_{j}^{-1}=g$; so $A(g)$ is the matrix of left multiplication by $g$, that is, $A$ is the left regular representation.
:::

:::

::: {.pf-step #regular}
With $a=\sum_{g}x_{g}g\in\CC[G]$ one has $X=\rho(a)$, and $\rho$ decomposes as $\bigoplus_{\nu=1}^{h}n_{\nu}A^{(\nu)}$ with $n_{\nu}=\dim A^{(\nu)}$.

::: pf-proof
$X=\sum_{g}x_{g}A(g)=\rho\big(\sum_{g}x_{g}g\big)$ by linearity and step [](#homomorphism){.pf-ref}. Over $\CC$, Maschke's theorem makes $\CC[G]$ semisimple, so $\rho$ is a direct sum of irreducibles, and each irreducible $A^{(\nu)}$ occurs with multiplicity equal to its degree $n_{\nu}$: as left $G$-modules $\CC[G]\cong\bigoplus_{\nu}\operatorname{End}(V_{\nu})$, and $\operatorname{End}(V_{\nu})$ is the direct sum of $\dim V_{\nu}=n_{\nu}$ copies of the irreducible $V_{\nu}$.
:::

:::

::: {.pf-step #part-b}
(b) $\displaystyle\det(X)=\prod_{\nu=1}^{h}\det\Big(\sum_{g\in G}A^{(\nu)}(g)x_{g}\Big)^{n_{\nu}}$.

::: pf-proof
By step [](#regular){.pf-ref} there is $P\in GL_{k}(\CC)$ with $PXP^{-1}$ block diagonal, having $n_{\nu}$ diagonal blocks $M_{\nu}=\sum_{g}A^{(\nu)}(g)x_{g}$ for each $\nu$. The determinant of a block diagonal matrix is the product of the determinants of its blocks, and determinant is invariant under conjugation, so
$$
\det(X)=\det(PXP^{-1})=\prod_{\nu=1}^{h}\det(M_{\nu})^{n_{\nu}} .
$$
:::

:::

::: {.pf-step #part-c}
(c) For $G=\ZZ_{n}$ the matrix of the display has determinant $\prod_{r=0}^{n-1}\big(x_{0}+\epsilon^{r}x_{1}+\dots+\epsilon^{(n-1)r}x_{n-1}\big)$, with $\epsilon=e^{2\pi i/n}$.

::: pf-proof
Write $G=\{0,1,\dots,n-1\}$ additively. Its irreducible representations are the characters $A^{(r)}(j)=\epsilon^{rj}$ for $r=0,\dots,n-1$, all one-dimensional, so $n_{r}=1$ for every $r$ and step [](#part-b){.pf-ref} gives
$$
\det(X)=\prod_{r=0}^{n-1}\sum_{j=0}^{n-1}\epsilon^{rj}x_{j},
\qquad X=[x_{i-j}].
$$
The matrix displayed in (c) has $(i,j)$ entry $x_{j-i}$, that is $X^{\mathsf T}$, and $\det(X^{\mathsf T})=\det(X)$; so the displayed determinant equals the same product. Equivalently, the eigenvalues of the displayed circulant are $\sum_{j}\epsilon^{rj}x_{j}$ for $r=0,\dots,n-1$, since the vector $(\epsilon^{rj})_{j}$ is an eigenvector.
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Step [](#homomorphism){.pf-ref} is (a), step [](#part-b){.pf-ref} is (b) and step [](#part-c){.pf-ref} is (c).
:::

:::

:::
:::
