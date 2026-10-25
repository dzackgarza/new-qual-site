---
schema: qual/card@1
id: P-AGH345PICH1
kind: problem
title: The Picard group as first cohomology of the sheaf of units
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Picard Group
  - Invertible Sheaves
relations: []
review: draft
---
::: {.problem}
For any ringed space $(X, \mco_X)$, let $\Pic X$ be the group of isomorphism classes of invertible sheaves (II, §6). Show that $\Pic X \cong H^1(X, \mco_X^*)$, where $\mco_X^*$ denotes the sheaf whose sections over an open set $U$ are the units in the ring $\Gamma(U, \mco_X)$, with multiplication as the group operation.

Hint: For any invertible sheaf $\mcl$ on $X$, cover $X$ by open sets $U_i$ on which $\mcl$ is free, and fix isomorphisms $\varphi_i: \mco_{U_i} \iso \restrictionof{\mcl}{U_i}$.
Then on $U_i \intersect U_j$, we get an isomorphism $\inverseof{\varphi_i} \circ \varphi_j$ of $\mco_{U_i \intersect U_j}$ with itself.
These isomorphisms give an element of $\check{H}^1(\mathfrak{U}, \mco_X^*)$.
Now use (Ex.
4.4).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\mathfrak U=\{U_i\}_{i\in I}$ be an open cover on which an
invertible sheaf $\mcl$ is free, and choose trivializations
$$
\varphi_i:\mco_{U_i}\xrightarrow{\sim}\restrictionof{\mcl}{U_i}.
$$
Then there are unique units
$$
g_{ij}\in\Gamma(U_i\cap U_j,\mco_X^*)
$$
such that $\varphi_i^{-1}\varphi_j$ is multiplication by $g_{ij}$.

::: pf-proof

An $\mco_{U_i\cap U_j}$-module endomorphism of the free rank-one module
$\mco_{U_i\cap U_j}$ is determined by the image of $1$, and it is an
automorphism exactly when that image is a unit.  Thus the transition
automorphism $\varphi_i^{-1}\varphi_j$ is multiplication by a unique section
$g_{ij}$ of $\mco_X^*$ on $U_i\cap U_j$.

:::

:::

::: {.pf-step #s2}

The family $(g_{ij})$ is a Čech $1$-cocycle.

::: pf-proof

On every triple intersection,
$$
(\varphi_i^{-1}\varphi_j)
(\varphi_j^{-1}\varphi_k)
=
\varphi_i^{-1}\varphi_k.
$$
Since composition of multiplication maps multiplies the corresponding units,
this identity is
$$
g_{ij}g_{jk}=g_{ik}.
$$
This is precisely the multiplicative Čech $1$-cocycle condition.

:::

:::

::: {.pf-step #s3}

Changing the chosen trivializations changes $(g_{ij})$ by a Čech
coboundary.

::: pf-proof

Replace $\varphi_i$ by
$$
\varphi_i' = \varphi_i\circ m_{h_i},
\qquad
h_i\in\Gamma(U_i,\mco_X^*),
$$
where $m_{h_i}$ denotes multiplication by $h_i$.  Then
$$
(\varphi_i')^{-1}\varphi_j'
=
m_{h_i^{-1}}\,
(\varphi_i^{-1}\varphi_j)\,
m_{h_j},
$$
so
$$
g_{ij}'=h_i^{-1}g_{ij}h_j.
$$
Thus $(g_{ij}')$ differs from $(g_{ij})$ by the coboundary of the Čech
$0$-cochain $(h_i)$.

:::

:::

::: {.pf-step #s4}

Isomorphic invertible sheaves determine the same class in
$\check H^1(\mathfrak U,\mco_X^*)$ after passing to a common trivializing
refinement.

::: pf-proof

Let $\alpha:\mcl\xrightarrow{\sim}\mcl'$ be an isomorphism.  If
$\varphi_i$ trivializes $\mcl$, then $\alpha\varphi_i$ trivializes $\mcl'$
and has exactly the same transition maps.  For arbitrary chosen
trivializations of $\mcl'$, step [](#s3){.pf-ref} shows that the resulting cocycle differs
only by a coboundary.

:::

:::

::: {.pf-step #s5}

Conversely, every Čech $1$-cocycle
$(g_{ij})$ in $\mco_X^*$ determines an invertible sheaf on $X$ trivialized by
$\mathfrak U$.

::: pf-proof

Take the free rank-one sheaf $\mco_{U_i}$ on each $U_i$.  On
$U_i\cap U_j$, identify $\mco_{U_j}$ with $\mco_{U_i}$ by multiplication by
$g_{ij}$.  The cocycle identity from step [](#s2){.pf-ref} is exactly the compatibility
condition required on triple intersections.  The sheaf gluing theorem therefore
produces an $\mco_X$-module $\mcl_g$ whose restriction to every $U_i$ is free
of rank one.  Hence $\mcl_g$ is invertible.

:::

:::

::: {.pf-step #s6}

Cohomologous cocycles give isomorphic invertible sheaves, and the
constructions in steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} are inverse.

::: pf-proof

If
$$
g_{ij}'=h_i^{-1}g_{ij}h_j,
$$
multiplication by $h_i$ on $\mco_{U_i}$ intertwines the gluing maps defined by
$g_{ij}$ and $g_{ij}'$, so these local maps glue to an isomorphism
$\mcl_g\cong\mcl_{g'}$.

Starting with an invertible sheaf, gluing copies of $\mco_{U_i}$ by its
transition functions reconstructs the original sheaf because the chosen
$\varphi_i$ identify the two gluing data.  Starting with a cocycle, the
tautological trivializations of the glued sheaf recover that same cocycle.
Thus the two constructions are inverse on isomorphism and cohomology classes.

:::

:::

::: {.pf-step #s7}

For every cover $\mathfrak U$, there is a bijection
$$
\left\{
\begin{array}{c}
\text{invertible sheaves on $X$}\
\text{trivialized by $\mathfrak U$}
\end{array}
\right\}/\cong
\;\xrightarrow{\sim}\;
\check H^1(\mathfrak U,\mco_X^*).
$$

::: pf-proof

This is exactly the mutually inverse correspondence proved in steps
[](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: {.pf-step #s8}

The bijection in step [](#s7){.pf-ref} is compatible with the group laws.

::: pf-proof

If $\mcl$ and $\mcl'$ have transition functions $g_{ij}$ and $g_{ij}'$, then
the tensor-product trivializations identify the transition function of
$\mcl\otimes\mcl'$ with multiplication by
$$
g_{ij}g_{ij}'.
$$
Thus tensor product in $\Pic X$ corresponds to multiplication of Čech
$1$-cocycles, which is the group law in
$\check H^1(\mathfrak U,\mco_X^*)$.

:::

:::

::: {.pf-step #s9}

Passing to refinements gives a natural group isomorphism
$$
\Pic X
\xrightarrow{\sim}
\check H^1(X,\mco_X^*)
\coloneqq
\varinjlim_{\mathfrak U}
\check H^1(\mathfrak U,\mco_X^*).
$$

::: pf-proof

Every invertible sheaf is locally free of rank one, so it is trivial on some
open cover.  The transition cocycle of a sheaf restricts to the transition
cocycle on every refinement, and the gluing construction is likewise
compatible with refinement.  Hence the coverwise isomorphisms of steps
[](#s7){.pf-ref} and [](#s8){.pf-ref} pass to the direct limit over open covers.

:::

:::

::: {.pf-step #s10}

There is a natural isomorphism
$$
\check H^1(X,\mco_X^*)
\xrightarrow{\sim}
H^1(X,\mco_X^*).
$$

::: pf-proof

Exercise III.4.4 identifies degree-one Čech cohomology, after taking the direct
limit over open covers, with derived-functor sheaf cohomology for every sheaf
of abelian groups.  Apply that result to the abelian sheaf
$\mco_X^*$.

:::

:::

::: {.pf-step #s11}

Therefore
$$
\boxed{\Pic X\cong H^1(X,\mco_X^*)}.
$$

::: pf-proof

Compose the natural group isomorphisms in steps [](#s9){.pf-ref} and [](#s10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s11){.pf-ref} is the required identification, and step [](#s8){.pf-ref} verifies that it
respects the Picard-group operation.

:::

:::

:::
