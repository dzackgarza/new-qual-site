---
schema: qual/card@1
id: P-AGH272LINPROJ
kind: problem
title: Morphisms from the same linear system differ by a linear projection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Invertible Sheaves
  - Linear Projection
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement with the retained Hartshorne II.7.2 transcription. The proof keeps both possibly dependent generating lists, constructs a full-row-rank coefficient matrix, and checks equality on affine coordinate ratios rather than only on points.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a scheme over a field $k$.
Let $\mcl$ be an invertible sheaf on $X$, and let $\ts{s_0, \ldots, s_n}$ and $\ts{t_0, \ldots, t_m}$ be two sets of sections of $\mcl$ which generate the same subspace $V \subseteq \Gamma(X, \mcl)$, and which generate the sheaf $\mcl$ at every point.
Suppose $n \leq m$.

Show that the corresponding morphisms $\varphi: X \to \PP^n_k$ and $\psi: X \to \PP^m_k$ differ by a suitable linear projection $\PP^m - L \to \PP^n$ and an automorphism of $\PP^n$, where $L$ is a linear subspace of $\PP^m$ of dimension $m - n - 1$.
:::

::: {.solution}
Let $E=k^{n+1}$ and $F=k^{m+1}$, with standard bases $e_i$ and $f_j$.
The two lists give surjective linear maps
$$
S:E\longrightarrow V,\quad e_i\longmapsto s_i,
\qquad
T:F\longrightarrow V,\quad f_j\longmapsto t_j.
$$
Write $r=\dim_kV$.

::: pf

::: {.pf-step #s1}

There is an injective linear map $J:E\to F$ with $T\circ J=S$.

::: pf-proof

Choose complements $E=E_0\oplus\ker S$ and $F=F_0\oplus\ker T$.
The restrictions $S|_{E_0}$ and $T|_{F_0}$ are isomorphisms onto $V$.
Since
$$
\dim\ker S=n+1-r\le m+1-r=\dim\ker T,
$$
choose an injection $J_1:\ker S\to\ker T$.
Define $J$ on $E_0$ to be $(T|_{F_0})^{-1}\circ S|_{E_0}$, and on $\ker S$ to be $J_1$.
The images of these two summands lie in the complementary subspaces $F_0$ and $\ker T$, and both restrictions are injective.
Thus $J$ is injective, and its construction gives $T\circ J=S$.

:::

:::

::: {.pf-step #s2}

There is a matrix $A=(a_{ij})$ of row rank $n+1$ such that $s_i=\sum_{j=0}^m a_{ij}t_j$.
Its linear forms define a projection $p_A:\PP^m\setminus L\to\PP^n$, with $\dim L=m-n-1$ when $m>n$.

::: pf-proof

Write $J(e_i)=\sum_j a_{ij}f_j$.
The identity in step [](#s1){.pf-ref} gives the required section identities, and injectivity of $J$ makes the rows of $A$ linearly independent.
For homogeneous coordinates $z_0,\ldots,z_m$, put
$$
\ell_i(z)=\sum_j a_{ij}z_j,\qquad
L=V_+(\ell_0,\ldots,\ell_n),\qquad
p_A([z])=[\ell_0(z):\cdots:\ell_n(z)].
$$
The kernel of the surjection $A:k^{m+1}\to k^{n+1}$ has dimension $m-n$, so its projectivization is the stated center.
Choose a vector-space complement $W$ to this kernel.
Projection along the kernel maps $\PP^m\setminus L$ to the linear $n$-plane of lines in $W$, and $A|_W$ identifies that plane with $\PP^n$.
Thus $p_A$ is a linear projection followed by a projective linear isomorphism of its target.
Under any fixed linear identification of that target with $\PP^n$, the latter is an automorphism of $\PP^n$.
When $m=n$, $A$ is invertible, the center is empty, and $p_A$ itself is a projective linear automorphism; the dimension $-1$ convention refers to this empty center.

:::

:::

::: {.pf-step #s3}

The image of $\psi$ avoids $L$, and $\varphi=p_A\circ\psi$ as morphisms of schemes.

::: pf-proof

Under the isomorphism $\psi^*\OO_{\PP^m}(1)\cong\mcl$, the pullback of $\ell_i$ is $\sum_j a_{ij}t_j=s_i$ [@Har10a, Theorem II.7.1].
The sections $s_i$ [[D-MODGG|generate]] $\mcl$ at every point, so their common zero subscheme is empty.
Consequently $\psi^{-1}(L)=\varnothing$, and the composite is defined on all of $X$.

Let $X_{s_i}$ be the open subset where $s_i$ generates $\mcl$.
On this open set, the coordinate ratio $w_h/w_i$ on the $i$th affine chart of $\PP^n$ pulls back along the composite to
$$
\frac{\sum_j a_{hj}t_j}{\sum_j a_{ij}t_j}=\frac{s_h}{s_i}.
$$
These are exactly the coordinate-ring maps defining $\varphi$ on $X_{s_i}$.
The opens $X_{s_i}$ cover $X$, so the morphisms agree, including when $X$ is nonreduced.
For $X=\varnothing$ the same equality is the uniqueness of its morphism to the target.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} construct a projection with the required center without assuming either generating list is a basis.
Step [](#s3){.pf-ref} proves the required factorization, and the target identification in step [](#s2){.pf-ref} gives its stated automorphism.

:::

:::

:::
