---
schema: qual/card@1
id: P-AGH2518VECBUN
kind: problem
title: Vector bundles and locally free sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Vector Bundles
  - Locally Free Sheaves
  - Symmetric Algebras
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read the vector-bundle definition and all four parts of Hartshorne Exercise II.5.18. Kept the source convention V(E)=Spec Sym(E), so its section sheaf is E dual. The reconstruction uses the dual of the section sheaf and is checked on linear coordinate changes, not only on local isomorphism types.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $Y$ be a scheme and let $n\ge0$ be an integer.
A \dfn{geometric vector bundle} of rank $n$ over $Y$ is a scheme $X$ and a morphism $f:X\to Y$, together with an open covering $\ts{U_i}$ of $Y$ and isomorphisms $\psi_i:f^{-1}(U_i)\to\AA^n_{U_i}$, such that for any $i,j$ and any open affine $V=\Spec A\subseteq U_i\cap U_j$, the automorphism $\psi_j\circ\psi_i^{-1}$ of $\AA^n_V=\Spec A[x_1,\ldots,x_n]$ is given by a linear $A$-algebra automorphism $\theta$ with $\theta(x_a)=\sum_b c_{ab}x_b$ for an invertible matrix $(c_{ab})$ over $A$.

An \dfn{isomorphism} $g:(X,f,\ts{U_i},\ts{\psi_i})\to(X',f',\ts{U'_i},\ts{\psi'_i})$ of vector bundles of rank $n$ is a scheme isomorphism $g:X\to X'$ with $f=f'\circ g$, such that the combined trivializations $\psi_i$ and $\psi'_i\circ g$ define a vector bundle structure on $X$.

(a) Let $\mce$ be a locally free sheaf of rank $n$ on $Y$.
    Let $S(\mce)$ be its symmetric algebra and let $X=\Spec_Y S(\mce)$ with projection $f:X\to Y$.
    For each open affine $U\subseteq Y$ on which $\mce|_U$ is free, choose a basis and use $S(\mce(U))\cong\OO_Y(U)[x_1,\ldots,x_n]$ to define $\psi:f^{-1}(U)\to\AA^n_U$.

Show that these trivializations define a vector bundle of rank $n$ whose isomorphism class does not depend on the bases.
Denote it by $\mathbf V(\mce)$.

(b) For a morphism $f:X\to Y$, a \dfn{section} over an open set $U\subseteq Y$ is a morphism $s:U\to f^{-1}(U)$ with $(f|_{f^{-1}(U)})\circ s=\id_U$.
    Sections restrict and glue to form a sheaf of sets $\mcs(X/Y)$ on $Y$.
    Show that for a rank-$n$ vector bundle this sheaf has a natural $\OO_Y$-module structure making it locally free of rank $n$.

(c) Let $\mce$ be locally free of rank $n$, put $X=\mathbf V(\mce)$, and let $\mcs=\mcs(X/Y)$.
For an open set $V\subseteq Y$, send a section $s\in\Gamma(V,\dualof{\mce})=\Hom_{\OO_V}(\mce|_V,\OO_V)$ to its induced $\OO_V$-algebra homomorphism $S(\mce|_V)\to\OO_V$, and then to the resulting section
$$
V=\Spec_V\OO_V\longrightarrow\Spec_V S(\mce|_V)=f^{-1}(V).
$$
Show that this construction gives an isomorphism $\dualof{\mce}\cong\mcs$.

(d) Prove the resulting bijection between isomorphism classes of locally free sheaves of rank $n$ on $Y$ and isomorphism classes of vector bundles of rank $n$ over $Y$.
:::

::: {.hint}
For part (b), work locally with $Y=\Spec A$ and $X=\AA_Y^n$.
A section is an $A$-algebra map $A[x_1,\ldots,x_n]\to A$, determined by the tuple of images of $x_1,\ldots,x_n$.
:::

::: {.solution}
Write $\mathcal S_X=\mcs(X/Y)$ for the sheaf of sections of a bundle $f:X\to Y$.
All duals and symmetric algebras in this solution are over $\OO_Y$, and all spectra of sheaves of algebras are relative spectra.

<1>1. The construction $\mathbf V(\mce)=\Spec_Y S(\mce)$ gives the bundle in part (a), independently of the chosen frames.

::: {.proof}
A locally free sheaf is [[D-QNTZY|quasi-coherent]], and its [[D-DEFTALG|symmetric algebra]] is quasi-coherent because locally it is a polynomial algebra with its underlying direct-sum module.
Thus [[P-AGH2517AFFMOR]] constructs its relative spectrum.
On an affine open $U=\Spec A$ with frame $e_1,\ldots,e_n$ of $\mce$, the map
$$
A[x_1,\ldots,x_n]\longrightarrow S_A(\mce(U)),\qquad x_a\longmapsto e_a
$$
is an algebra isomorphism.
It gives the required trivialization of $f^{-1}(U)$.

On an affine open in the overlap of two framed opens, write the second frame as $e'_a=\sum_b c_{ab}e_b$, with $(c_{ab})$ invertible.
The corresponding map between polynomial coordinate rings sends $x'_a$ to $\sum_b c_{ab}x_b$ and is linear.
These are precisely the transition maps required in the statement.
The same calculation applies to any replacement frames, so the union of the original and replacement trivializations remains a vector bundle structure.
The identity on $\Spec_Y S(\mce)$ is then an isomorphism of the resulting bundles.
:::

<1>2. The sheaf $\mathcal S_X$ has the natural locally free module structure asserted in part (b).

::: {.proof}
Over a trivializing affine open $U=\Spec A$, sections of $\AA_U^n\to U$ correspond to $A$-algebra maps $A[x_1,\ldots,x_n]\to A$.
Sending a map to the tuple of coordinate images identifies this set with $A^n$.
On smaller affine opens the correspondence commutes with restriction, so it identifies the section sheaf on $U$ with $\OO_U^n$.

Use coordinatewise addition and multiplication by sections of $\OO_U$ to define its module operations.
On an overlap, a linear coordinate change with matrix $C=(c_{ab})$ sends a section tuple $v$ to $Cv$.
This is an invertible linear map and preserves those operations, so the local operations agree and glue on $Y$.
The module axioms hold locally, hence globally.
Each trivialization identifies the resulting module sheaf with $\OO_U^n$, proving local freeness of rank $n$.
A compatible change of bundle trivializations preserves these operations by the same calculation.
:::

<1>3. For $X=\mathbf V(\mce)$, the isomorphism in part (c) is
$$
\boxed{\dualof{\mce}\xrightarrow{\cong}\mathcal S_X}.
$$

::: {.proof}
For an open set $U\subseteq Y$, a section of $\dualof{\mce}$ is an $\OO_U$-linear sheaf morphism $\lambda:\mce|_U\to\OO_U$.
By the symmetric-algebra universal property, it extends uniquely to an $\OO_U$-algebra morphism
$$
S(\mce|_U)\longrightarrow\OO_U.
$$
Taking spectra on affine opens of $U$ and gluing gives a section $s_\lambda:U\to X$ over $Y$, by the relative-spectrum construction of [[P-AGH2517AFFMOR]]. Conversely, a section of $X$ over $U$ induces this algebra homomorphism on each affine open of $U$.
Its restriction to degree one gives $\lambda$.
The two constructions are inverse on affine opens and commute with restriction, so they are inverse for every $U$ and define an isomorphism of sheaves of sets.

In a frame $e_1,\ldots,e_n$, the tuple representing $s_\lambda$ is $(\lambda(e_1),\ldots,\lambda(e_n))$.
This identifies addition and scalar multiplication of functionals with the operations of step <1>2. Thus the isomorphism is $\OO_Y$-linear.
The construction is independent of frames since it uses the specified algebra homomorphism, and it is natural in $\mce$.
:::

<1>4. Every rank-$n$ bundle $f:X\to Y$ is canonically isomorphic, as a bundle, to $\mathbf V(\dualof{\mathcal S_X})$.

::: {.proof}
The morphism $f$ is affine: refine the trivializing cover by affine opens, whose inverse images are affine $n$-spaces.
Put $\mathcal B=f_*\OO_X$.
On a trivializing affine open $U$, the algebra $\mathcal B|_U$ is $\OO_U[x_1,\ldots,x_n]$.
Its degree-one summand consists of the linear forms in the coordinates.
The transition maps are linear and preserve this summand, so these summands glue to a locally free subsheaf $\mathcal E\subseteq\mathcal B$ of rank $n$.

Evaluation of a linear form on a section gives a pairing
$$
\mathcal E\otimes\mathcal S_X\longrightarrow\OO_Y.
$$
On a trivializing open set, its coordinate expression sends $\bigl(\sum_a b_ax_a,v\bigr)$ to $\sum_a b_av_a$.
It is the perfect pairing between coordinate linear forms and tuples, and identifies $\mathcal E\cong\dualof{\mathcal S_X}$.
It is invariant under the linear transition maps because the value of a function pulled back by a section does not depend on coordinates.

The inclusion $\mathcal E\to\mathcal B$ extends to an algebra homomorphism $S(\mathcal E)\to\mathcal B$.
On each framed open set it is the polynomial algebra isomorphism sending the degree-one generators to the coordinate functions.
Hence it is an isomorphism globally.
Part (d) of [[P-AGH2517AFFMOR]] now gives
$$
X\cong\Spec_Y\mathcal B\cong\Spec_Y S(\mathcal E)\cong\mathbf V(\dualof{\mathcal S_X}).
$$
On every trivializing open this map identifies the same linear coordinate functions, so it is an isomorphism of vector bundles, not only of schemes over $Y$.
:::

<1>5. The inverse bijections in part (d) are
$$
\boxed{[\mce]\longmapsto[\mathbf V(\mce)],\qquad
[X\to Y]\longmapsto[\dualof{\mathcal S_X}]}.
$$

::: {.proof}
A sheaf isomorphism induces an isomorphism of symmetric algebras and therefore a bundle isomorphism after taking relative spectra.
A bundle isomorphism carries sections to sections; step <1>2 makes the resulting map linear, so it induces an isomorphism of their dual section sheaves.
Thus both maps are defined on the indicated isomorphism classes.
For a locally free $\mce$, step <1>3 and the canonical bidual isomorphism from [[P-AGH251DUALSHEAF]] give
$$
\dualof{\mathcal S_{\mathbf V(\mce)}}\dualof{\cong(\dualof{\mce})}\cong\mce.
$$
For a vector bundle, step <1>4 gives the inverse reconstruction.
Consequently the two maps are mutually inverse.
When $n=0$, the same constructions give the zero sheaf and the bundle $Y\xrightarrow{\id_Y}Y$, so this case is included.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, <1>3, and <1>5 prove parts (a), (b), (c), and (d), respectively.
:::
:::
