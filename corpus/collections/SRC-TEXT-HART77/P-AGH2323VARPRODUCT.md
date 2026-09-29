---
schema: qual/card@1
id: P-AGH2323VARPRODUCT
kind: problem
title: The product of two varieties agrees with the fibre product of the associated schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Fibre Products
  - Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.23 statement and the affine fibre-product formula from II.3.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
If $V, W$ are two varieties over an algebraically closed field $k$, if $V \times W$ is their product as defined in Hartshorne I, Ex.
3.15 and 3.16, and if $t$ is the functor of II.2.6, then
\[
t(V \times W) = \fiberprod{t(V)}{\Spec k}{t(W)}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #affine-coordinate-ring-tensor}
Suppose first that $V$ and $W$ are affine varieties,
\[
V=\operatorname{Spec}_{\mathrm{var}}A,
\qquad
W=\operatorname{Spec}_{\mathrm{var}}B,
\]
where $A$ and $B$ are finitely generated reduced $k$-algebras which are domains.
Then the classical product variety $V\times W$ is affine with coordinate ring
\[
\boxed{A(V\times W)\cong A\otimes_kB.}
\]

::: pf-proof
This is the affine product construction from Hartshorne I, Exercises 3.15--3.16: embed $V\subseteq\mathbb A^m$ and $W\subseteq\mathbb A^n$.  Then
\[
V\times W\subseteq\mathbb A^{m+n}
\]
is cut out by the equations defining $V$ in the first set of variables and those defining $W$ in the second set.  Thus if
\[
A=k[x_1,\ldots,x_m]/I,
\qquad
B=k[y_1,\ldots,y_n]/J,
\]
then
\[
A(V\times W)
\cong
k[x_1,\ldots,x_m,y_1,\ldots,y_n]/(I,J)
\cong
A\otimes_kB.
\]
:::

:::

::: {.pf-step #affine-case-fibre-product}
In the affine case,
\[
\boxed{
t(V\times W)
\cong
t(V)\times_{\Spec k}t(W).}
\]

::: pf-proof
By the construction of the scheme associated to an affine variety,
\[
t(V)=\Spec A,
\qquad
t(W)=\Spec B.
\]
By step [](#affine-coordinate-ring-tensor){.pf-ref},
\[
t(V\times W)=\Spec(A\otimes_kB).
\]
Hartshorne II.3.9 gives the affine fibre-product formula
\[
\Spec A\times_{\Spec k}\Spec B
\cong
\Spec(A\otimes_kB).
\]
These are the same affine scheme.
:::

:::

::: {.pf-step #affine-cover-of-product}
Let
\[
V=\bigcup_iU_i,
\qquad
W=\bigcup_jT_j
\]
be affine open covers.  Then the subsets
\[
U_i\times T_j
\]
form an affine open cover of the classical product variety $V\times W$.

::: pf-proof
The classical product projections
\[
V\times W\to V,
\qquad
V\times W\to W
\]
are continuous.  Hence
\[
U_i\times T_j
\]
is open in $V\times W$, and these subsets cover the product.

Hartshorne I, Exercises 3.15--3.16 identify the product of two affine open subvarieties with the affine variety having coordinate ring
\[
A(U_i)\otimes_kA(T_j).
\]
Thus every $U_i\times T_j$ is affine.
:::

:::

::: {.pf-step #affine-cover-of-fibre-product}
The inverse images of
\[
t(U_i)\subseteq t(V),
\qquad
t(T_j)\subseteq t(W)
\]
give an affine open cover of the scheme fibre product
\[
P:=t(V)\times_{\Spec k}t(W),
\]
and each member is
\[
t(U_i)\times_{\Spec k}t(T_j)
\cong
t(U_i\times T_j).
\]

::: pf-proof
The schemes $t(U_i)$ and $t(T_j)$ are open subschemes of $t(V)$ and $t(W)$.  Their fibre products are therefore open subschemes of $P$, and they cover $P$ because the two families cover the factors.

The final isomorphism is the affine case step [](#affine-case-fibre-product){.pf-ref}.
:::

:::

::: {.pf-step #overlaps-agree}
On overlaps, the affine identifications in step [](#affine-cover-of-fibre-product){.pf-ref} agree with the restriction maps used to glue $t(V\times W)$.

::: pf-proof
Suppose
\[
U_{ii'}=U_i\cap U_{i'},
\qquad
T_{jj'}=T_j\cap T_{j'}.
\]
Then
\[
(U_i\times T_j)\cap(U_{i'}\times T_{j'})
=
U_{ii'}\times T_{jj'}.
\]

All maps in the affine identifications are induced functorially by restriction homomorphisms on coordinate rings and by the universal tensor-product map.  Thus restricting the isomorphism on $U_i\times T_j$ to the overlap gives exactly the affine isomorphism constructed from $U_{ii'}$ and $T_{jj'}$.  Hence the local identifications satisfy the cocycle compatibility required for gluing.
:::

:::

::: {.pf-step #global-isomorphism}
The local isomorphisms glue to a global isomorphism
\[
\boxed{
t(V\times W)
\xrightarrow{\sim}
t(V)\times_{\Spec k}t(W).}
\]

::: pf-proof
By step [](#affine-cover-of-product){.pf-ref}, the schemes $t(U_i\times T_j)$ cover $t(V\times W)$.  By step [](#affine-cover-of-fibre-product){.pf-ref}, the corresponding affine schemes cover the fibre product $P$.  Step [](#overlaps-agree){.pf-ref} shows that the affine isomorphisms agree on all overlaps.  The gluing theorem therefore gives a global isomorphism.
:::

:::

::: {.pf-step #compatible-with-projections}
This isomorphism is compatible with both projections, so it identifies the classical product with the categorical fibre product after applying $t$.

::: pf-proof
On every affine product chart, the two projections are induced by the canonical ring maps
\[
A(U_i)\longrightarrow A(U_i)\otimes_kA(T_j),
\qquad
A(T_j)\longrightarrow A(U_i)\otimes_kA(T_j).
\]
These are precisely the projections of the affine scheme fibre product.  Compatibility is local, so it holds globally.
:::

:::

::: pf-qed
Step [](#global-isomorphism){.pf-ref} proves the stated equality up to the canonical isomorphism intended by the notation, and step [](#compatible-with-projections){.pf-ref} verifies compatibility with the product structure.
:::

:::

:::
