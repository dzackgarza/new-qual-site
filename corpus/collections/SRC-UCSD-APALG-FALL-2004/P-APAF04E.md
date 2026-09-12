---
schema: qual/card@1
id: P-APAF04E
kind: problem
title: Group determinant via the regular representation and a circulant evaluation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
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

::: problem
Let $G=\{g_1,\ldots,g_k\}$ be a finite group.
Introduce variables $x_{g_1},\ldots,x_{g_k}$ and consider the $k\times k$ matrix
\[
X=\bigl[x_{g_i g_j^{-1}}\bigr].
\]
Let $X=\sum_{i=1}^k A(g_i)x_{g_i}$ so that we can define a map $g_i\mapsto A(g_i)$.

(a) Show that $A$ is the left regular representation of $G$.

(b) Show that
\[
\det(X)=\prod_{\nu=1}^{h}\det\Biggl(\sum_{g\in G}A^{(\nu)}(g)x_g\Biggr)^{n_\nu}
\]
where $A^{(1)},\ldots,A^{(h)}$ are a complete set of representatives of the irreducible representations of $G$ and $n_\nu=\dim(A^{(\nu)})$ for $\nu=1,\ldots,h$.

(c) Use part (b) to show that
\[
\det\begin{bmatrix}
x_0 & x_1 & x_2 & \cdots & x_{n-1}\\
x_{n-1} & x_0 & x_1 & \cdots & x_{n-2}\\
x_{n-2} & x_{n-1} & x_0 & \cdots & x_{n-3}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
x_1 & x_2 & x_3 & \cdots & x_0
\end{bmatrix}
=\prod_{r=0}^{n-1}\bigl(x_0+\epsilon^r x_1+\epsilon^{2r}x_2+\cdots+\epsilon^{(n-1)r}x_{n-1}\bigr)
\]
where $\epsilon=e^{2\pi i/n}$.
:::

::: {.solution}
For each $g\in G$, let $A(g)$ denote the coefficient of $x_g$ in
\[
X=[x_{g_i g_j^{-1}}].
\]
Thus
\[
A(g)_{ij}=
\begin{cases}
1,&g_i g_j^{-1}=g,\\
0,&\text{otherwise}.
\end{cases}
\]

<1>1. The map $g\mapsto A(g)$ is the left regular representation of $G$ on the vector space with basis $e_{g_1},\ldots,e_{g_k}$.
::: {.proof}
For a fixed column $j$, there is a unique index $i$ such that
\[
g_i=gg_j.
\]
By the definition above, this is exactly the unique row for which $A(g)_{ij}=1$. Hence
\[
A(g)e_{g_j}=e_{gg_j}.
\]
This is left multiplication by $g$ on the basis indexed by $G$. Therefore
\[
A(g)A(h)e_{g_j}=A(g)e_{hg_j}=e_{ghg_j}=A(gh)e_{g_j}
\]
for every basis vector, so $A(g)A(h)=A(gh)$ and $A(e)=I$. Thus $A$ is precisely the left regular representation. This proves part (a).
:::

<1>2. Over $\mathbb C$, the regular representation decomposes as
\[
\mathbb C[G]\cong\bigoplus_{\nu=1}^h n_\nu V_\nu,
\qquad n_\nu=\dim V_\nu,
\]
where $V_1,\ldots,V_h$ are representatives of the irreducible $G$-modules.
::: {.proof}
Maschke's theorem makes the regular representation completely reducible. Let $\chi_{\mathrm{reg}}$ be its character. Then
\[
\chi_{\mathrm{reg}}(e)=|G|,
\qquad
\chi_{\mathrm{reg}}(g)=0\quad(g\ne e),
\]
because left multiplication by $g\ne e$ permutes the basis $\{e_h:h\in G\}$ without fixed points.

If $\chi_\nu$ is the irreducible character of $V_\nu$, its multiplicity in the regular representation is
\[
\langle\chi_{\mathrm{reg}},\chi_\nu\rangle
=\frac1{|G|}\sum_{g\in G}\chi_{\mathrm{reg}}(g)\overline{\chi_\nu(g)}
=\overline{\chi_\nu(e)}
=\dim V_\nu=n_\nu.
\]
This gives the asserted decomposition.
:::

<1>3. There is an invertible matrix $P$ such that, for every $g\in G$,
\[
P^{-1}A(g)P
=
\bigoplus_{\nu=1}^h
\underbrace{A^{(\nu)}(g)\oplus\cdots\oplus A^{(\nu)}(g)}_{n_\nu\text{ copies}}.
\]
::: {.proof}
Choose a basis adapted to the direct-sum decomposition in <1>2. In that basis, the regular representation acts on each of the $n_\nu$ copies of $V_\nu$ by the irreducible representation $A^{(\nu)}$. The change-of-basis matrix from the original regular basis to this adapted basis is the required $P$.
:::

<1>4. Therefore
\[
\det(X)
=
\prod_{\nu=1}^h
\det\Bigl(\sum_{g\in G}A^{(\nu)}(g)x_g\Bigr)^{n_\nu}.
\]
::: {.proof}
Since
\[
X=\sum_{g\in G}A(g)x_g,
\]
<1>3 gives
\[
P^{-1}XP
=
\bigoplus_{\nu=1}^h
\underbrace{
\Bigl(\sum_{g\in G}A^{(\nu)}(g)x_g\Bigr)
\oplus\cdots\oplus
\Bigl(\sum_{g\in G}A^{(\nu)}(g)x_g\Bigr)
}_{n_\nu\text{ copies}}.
\]
Determinant is invariant under similarity and multiplicative on block-diagonal matrices, so taking determinants gives exactly the displayed formula. This proves part (b).
:::

<1>5. Let $G=C_n=\langle a\rangle$ and put
\[
x_j=x_{a^j}\qquad(0\le j<n).
\]
The irreducible complex representations of $C_n$ are the one-dimensional characters
\[
\chi_r(a^j)=\epsilon^{rj},
\qquad
0\le r<n,
\]
where $\epsilon=e^{2\pi i/n}$.
::: {.proof}
Since $C_n$ is finite abelian, every irreducible complex representation is one-dimensional. A character is determined by the image of $a$, which must be an $n$th root of unity. The $n$ choices are $\epsilon^r$, giving exactly the characters displayed above.
:::

<1>6. If the regular basis is ordered by
\[
1,a^{-1},a^{-2},\ldots,a^{-(n-1)},
\]
then the group-determinant matrix $[x_{g_i g_j^{-1}}]$ is exactly
\[
\begin{bmatrix}
x_0 & x_1 & x_2 & \cdots & x_{n-1}\\
x_{n-1} & x_0 & x_1 & \cdots & x_{n-2}\\
x_{n-2} & x_{n-1} & x_0 & \cdots & x_{n-3}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
x_1 & x_2 & x_3 & \cdots & x_0
\end{bmatrix}.
\]
::: {.proof}
With indices $i,j\in\{0,\ldots,n-1\}$ and $g_i=a^{-i}$,
\[
g_i g_j^{-1}=a^{-i}a^j=a^{j-i}.
\]
Thus the $(i,j)$-entry is $x_{j-i\bmod n}$, which is exactly the displayed circulant matrix.
:::

<1>7. Its determinant is
\[
\prod_{r=0}^{n-1}
\bigl(x_0+\epsilon^r x_1+\epsilon^{2r}x_2+\cdots+\epsilon^{(n-1)r}x_{n-1}\bigr).
\]
::: {.proof}
For $C_n$, every irreducible representation has dimension $1$, so <1>4 becomes
\[
\det(X)
=\prod_{r=0}^{n-1}\left(\sum_{j=0}^{n-1}\chi_r(a^j)x_j\right).
\]
Using <1>5,
\[
\sum_{j=0}^{n-1}\chi_r(a^j)x_j
=\sum_{j=0}^{n-1}\epsilon^{rj}x_j
=x_0+\epsilon^r x_1+\cdots+\epsilon^{(n-1)r}x_{n-1}.
\]
Substitution yields the required formula, proving part (c).
:::
:::
