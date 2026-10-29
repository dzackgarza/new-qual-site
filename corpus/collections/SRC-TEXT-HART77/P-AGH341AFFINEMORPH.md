---
schema: qual/card@1
id: P-AGH341AFFINEMORPH
kind: problem
title: Cohomology is preserved by pushforward along an affine morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Affine Morphisms
  - Quasicoherent Sheaves
relations: []
review: draft
---
::: {.problem}
Let $f: X \to Y$ be an affine morphism of noetherian separated schemes (II, Ex.
5.17). Show that for any quasi-coherent sheaf $\mcf$ on $X$, there are natural isomorphisms for all $i \geq 0$,
$$
H^i(X, \mcf) \cong H^i(Y, f_* \mcf).
$$

Hint: Use (II, 5.8).
:::

::: {.solution}
Let $\mathfrak V=\{V_a\}_{a\in A}$ be a finite affine open cover of $Y$.

::: pf

::: {.pf-step #s1}

Every finite intersection
$$
V_{a_0\ldots a_p}
\coloneqq
V_{a_0}\cap\cdots\cap V_{a_p}
$$
is affine.

::: pf-proof

The scheme $Y$ is separated. Hence the intersection of two affine open subsets
of $Y$ is affine, and induction gives the same conclusion for every finite
intersection of members of $\mathfrak V$.

:::

:::

::: {.pf-step #s2}

The inverse-image cover
$$
f^{-1}\mathfrak V
=\{f^{-1}(V_a)\}_{a\in A}
$$
is a finite affine open cover of $X$.

::: pf-proof

The sets $f^{-1}(V_a)$ cover $X$ because the $V_a$ cover $Y$. Since $f$ is
affine, the inverse image of every affine open subset of $Y$ is affine.
Finiteness is inherited from $\mathfrak V$.

:::

:::

::: {.pf-step #s3}

For every ordered tuple $(a_0,\ldots,a_p)$,
$$
\Gamma(V_{a_0\ldots a_p},f_*\mcf)
=
\Gamma(f^{-1}(V_{a_0\ldots a_p}),\mcf).
$$

::: pf-proof

This is the definition of direct image:
$$
(f_*\mcf)(W)=\mcf(f^{-1}(W))
$$
for every open $W\subseteq Y$. Taking $W=V_{a_0\ldots a_p}$ gives the
asserted equality.

:::

:::

::: {.pf-step #s4}

Under the identifications of step [](#s3){.pf-ref}, the Čech complexes are canonically
isomorphic:
$$
\check C^\bullet(\mathfrak V,f_*\mcf)
\cong
\check C^\bullet(f^{-1}\mathfrak V,\mcf).
$$

::: pf-proof

In degree $p$, the two complexes are products of the groups in step [](#s3){.pf-ref}.
Their differentials are alternating sums of restriction maps. Since the
identifications in step [](#s3){.pf-ref} come from the definition of $f_*$, they commute
with restrictions and therefore intertwine the Čech differentials.

:::

:::

::: {.pf-step #s5}

The sheaf $f_*\mcf$ is quasi-coherent on $Y$.

::: pf-proof

This is Hartshorne II.5.8: direct image along an affine morphism preserves
quasi-coherence.

:::

:::

::: {.pf-step #s6}

For every $i\geq0$,
$$
H^i(Y,f_*\mcf)
\cong
\check H^i(\mathfrak V,f_*\mcf)
$$
and
$$
H^i(X,\mcf)
\cong
\check H^i(f^{-1}\mathfrak V,\mcf).
$$

::: pf-proof

Both $X$ and $Y$ are noetherian and separated, and the covers in question are
finite affine open covers by steps [](#s1){.pf-ref} and [](#s2){.pf-ref}. By step [](#s5){.pf-ref}, $f_*\mcf$ is
quasi-coherent, while $\mcf$ is quasi-coherent by hypothesis. The Čech
cohomology theorem for quasi-coherent sheaves on noetherian separated schemes
therefore identifies the displayed Čech groups with sheaf cohomology.

:::

:::

::: {.pf-step #s7}

For every $i\geq0$,
$$
\boxed{H^i(X,\mcf)\cong H^i(Y,f_*\mcf)}.
$$

::: pf-proof

Combining steps [](#s4){.pf-ref} and [](#s6){.pf-ref} gives
$$
\begin{aligned}
H^i(Y,f_*\mcf)
&\cong \check H^i(\mathfrak V,f_*\mcf)\\
&\cong \check H^i(f^{-1}\mathfrak V,\mcf)\\
&\cong H^i(X,\mcf).
\end{aligned}
$$
Taking the inverse of this canonical isomorphism gives the displayed
orientation.

:::

:::

::: {.pf-step #s8}

The isomorphisms in step [](#s7){.pf-ref} are natural in $\mcf$.

::: pf-proof

A morphism $\mcf\to\mathcal G$ of quasi-coherent sheaves induces compatible
maps on every section group occurring in the two Čech complexes of step [](#s4){.pf-ref}.
Hence it induces a morphism of those complexes. The identifications in steps
[](#s4){.pf-ref} and [](#s6){.pf-ref} are canonical, so the resulting cohomology isomorphisms commute
with morphisms of quasi-coherent sheaves.

:::

:::

::: pf-qed

Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} establish the required natural isomorphisms in every degree.

:::

:::

:::
