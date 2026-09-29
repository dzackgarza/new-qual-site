---
schema: qual/card@1
id: P-AGH2517AFFMOR
kind: problem
title: Affine morphisms and the relative spectrum
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Morphisms
  - Relative Spectrum
  - Quasi-coherent Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all five parts and the hints with the original Hartshorne Exercise II.5.17. Restored the explicit O_Y-quasi-coherence convention in (e). The proof checks the affine-cover criterion, glues relative spectra through actual localization maps, and constructs the inverse equivalence on modules and morphisms over arbitrary schemes.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
A morphism $f:X\to Y$ of schemes is \dfn{affine} if there is an open affine cover $\ts{V_i}$ of $Y$ such that $f^{-1}(V_i)$ is affine for each $i$.

(a) Show that $f:X\to Y$ is affine if and only if, for every open affine $V\subseteq Y$, $f^{-1}(V)$ is affine.

(b) An affine morphism is quasi-compact and separated.
Any finite morphism is affine.

(c) Let $Y$ be a scheme, and let $\mca$ be a quasi-coherent sheaf of $\OO_Y$-algebras, whose underlying $\OO_Y$-module is quasi-coherent.
Show that there is a scheme $X$ and a morphism $f:X\to Y$ such that, for every open affine $V\subseteq Y$, $f^{-1}(V)\cong\Spec\mca(V)$, and, for every inclusion $U\hookrightarrow V$ of open affines of $Y$, the morphism $f^{-1}(U)\hookrightarrow f^{-1}(V)$ corresponds to restriction $\mca(V)\to\mca(U)$.
The scheme and morphism are unique up to unique isomorphism compatible with these affine identifications.
The scheme $X$ is called $\Spec \mca$.

(d) If $\mca$ is a quasi-coherent $\OO_Y$-algebra, then $f:X=\Spec\mca\to Y$ is affine and $\mca\cong f_*\OO_X$.
Conversely, if $f:X\to Y$ is affine, then $\mca=f_*\OO_X$ is a quasi-coherent sheaf of $\OO_Y$-algebras and $X\cong\Spec\mca$.

(e) Let $f:X\to Y$ be affine and let $\mca=f_*\OO_X$.
Show that $f_*$ induces an equivalence from quasi-coherent $\OO_X$-modules to quasi-coherent $\mca$-modules, meaning quasi-coherent $\OO_Y$-modules with a compatible $\mca$-module structure.
:::

::: {.hint}
For part (a), reduce to $Y$ affine and use (Ex. 2.17).
For part (c), glue the schemes $\Spec\mca(V)$.
For part (e), construct a quasi-coherent $\OO_X$-module $\widetilde{\mcm}$ from a quasi-coherent $\mca$-module $\mcm$, and show that this construction and $f_*$ are inverse functors.
:::

::: {.solution}
For an affine open $V=\Spec A$, write $D_V(a)$ for the distinguished open defined by $a\in A$.
For a global function $b$ on a scheme $Z$, let $Z_b$ be its nonvanishing locus.

::: pf

::: {.pf-step #s1}

The affine-cover condition implies the condition on every affine open, proving part (a).

::: pf-proof

Choose a witnessing affine cover $Y=\bigcup_iV_i$ with every $f^{-1}(V_i)$ affine, and fix an affine open $V=\Spec A\subseteq Y$.
For each $y\in V\cap V_i$, there is a neighborhood $W$ of $y$ distinguished in both $V$ and $V_i$.
To construct it, choose $y\in D_V(a)\subseteq V\cap V_i$, then choose $y\in D_{V_i}(c)\subseteq D_V(a)$.
The restriction of $c$ to $D_V(a)$ is $b/a^n$ for some $b\in A$.
Consequently
$$
D_{V_i}(c)=D_V(a)\cap D_V(b)=D_V(ab).
$$
The inverse image of $W$ is distinguished in the affine scheme $f^{-1}(V_i)$, hence affine.

Quasi-compactness of $V$ gives finitely many such neighborhoods $W_j=D_V(a_j)$ covering $V$.
The elements $a_j$ generate the unit ideal in $A$.
Put $Z=f^{-1}(V)$ and let $b_j\in\Gamma(Z,\OO_Z)$ be their pullbacks.
They still generate the unit ideal, and $Z_{b_j}=f^{-1}(W_j)$ is affine.
The [[P-AGH2217AFFINECRIT|global-function affineness criterion]] makes $Z$ affine.
Conversely, the condition on every affine open holds in particular on an affine cover, giving the defining condition.

:::

:::

::: {.pf-step #s2}

Part (b) holds.

::: pf-proof

By step [](#s1){.pf-ref}, the inverse image of every affine open in $Y$ is affine and therefore quasi-compact, so $f$ is quasi-compact.
On $V=\Spec A\subseteq Y$, write $f^{-1}(V)=\Spec B$.
The restriction of the diagonal of $f$ over this open is induced by the surjection
$$
B\otimes_A B\longrightarrow B,\qquad b\otimes b'\longmapsto bb'.
$$
Hence it is a closed immersion.
These opens cover the target $X\times_YX$ of the diagonal, so the diagonal is a closed immersion and $f$ is separated.
Finally, the defining affine cover for a [[D-MORFIN|finite morphism]] already has affine inverse images, so every finite morphism is affine.

:::

:::

::: {.pf-step #s3}

A quasi-coherent algebra $\mca$ gives compatible affine schemes $X_V=\Spec\mca(V)$ on the affine opens of $Y$.

::: pf-proof

For $V=\Spec A$, put $B=\mca(V)$ and let $h_V:\Spec B\to V$ be induced by its $A$-algebra structure.
Quasi-coherence gives canonical algebra isomorphisms
$$
\mca(D_V(a))\cong B_a\qquad(a\in A),
$$
compatible with restriction [@Har10a, Proposition II.5.4].
Thus $X_{D_V(a)}=\Spec B_a$ identifies with $h_V^{-1}(D_V(a))$ as an open subscheme of $X_V$.

On this distinguished-open basis, the sections of $(h_V)_*\OO_{X_V}$ are $B_a$, with the same restrictions as $\mca|_V$.
Therefore $(h_V)_*\OO_{X_V}\cong\mca|_V$ as sheaves of algebras.
The morphism $h_V$ is affine by the one-member affine cover of $V$.
For any affine open $U\subseteq V$, step [](#s1){.pf-ref} makes $h_V^{-1}(U)$ affine, and its coordinate ring is
$$
\Gamma(h_V^{-1}(U),\OO_{X_V})\cong\mca(U).
$$
This gives an open immersion $X_U\hookrightarrow X_V$ induced by the restriction map $\mca(V)\to\mca(U)$.
For nested affine opens these maps compose as their restriction homomorphisms do.

:::

:::

::: {.pf-step #s4}

These affine schemes glue uniquely to the relative spectrum in part (c).

::: pf-proof

Choose an affine open cover $(V_i)$ of $Y$.
For two members, cover $V_i\cap V_j$ by affine opens $U$.
The schemes $X_U$ in step [](#s3){.pf-ref} form an open cover of both $h_{V_i}^{-1}(V_i\cap V_j)$ and $h_{V_j}^{-1}(V_i\cap V_j)$ and identify them canonically.
For two such opens $U,U'$, refine $U\cap U'$ by affine opens again.
The identifications agree there because they are induced by the same restriction homomorphisms from $\mca$.
This proves consistency of the overlap maps; on triple intersections the same argument proves the cocycle identity.

Gluing schemes along these open identifications gives a scheme $X$ and a morphism $f:X\to Y$ whose pieces are the $h_{V_i}$ [@Har10a, Exercise II.2.12].
For any affine open $V\subseteq Y$, covering $V\cap V_i$ by affine opens and using step [](#s3){.pf-ref} identifies $f^{-1}(V)$ with $X_V$.
The restriction maps for all affine inclusions are exactly those stipulated in part (c).
Any other scheme with these compatible identifications has the same local isomorphisms to $X_V$.
They agree on overlaps and glue to a unique $Y$-isomorphism preserving those identifications.
This proves the required uniqueness and defines $\Spec_Y\mca$.

:::

:::

::: {.pf-step #s5}

The two constructions in part (d) recover each other.

::: pf-proof

For the relative spectrum just constructed, each $f^{-1}(V)=\Spec\mca(V)$ is affine, so $f$ is affine.
On every affine open $V$,
$$
(f_*\OO_X)(V)=\Gamma(\Spec\mca(V),\OO_X)\cong\mca(V).
$$
The identifications respect restriction and algebra multiplication, giving $f_*\OO_X\cong\mca$.

Conversely, let $f$ be affine and put $\mca=f_*\OO_X$.
For an affine open $V=\Spec A$, write $f^{-1}(V)=\Spec B$.
On $D_V(a)$ its direct image has sections $B_a$, so $\mca|_V$ is the quasi-coherent algebra associated to the $A$-algebra $B$.
This holds on an affine cover, proving quasi-coherence on $Y$.
The relative spectrum of $\mca$ is glued from the affine schemes $\Spec B$ and the restriction maps already present in $X$.
The uniqueness in step [](#s4){.pf-ref} gives $X\cong\Spec_Y\mca$ over $Y$.

:::

:::

::: {.pf-step #s6}

Direct image gives a functor to the module category specified in part (e).

::: pf-proof

Let $\mathcal N$ be a quasi-coherent $\OO_X$-module.
For $V=\Spec A\subseteq Y$ with $f^{-1}(V)=\Spec B$, put $N=\Gamma(f^{-1}(V),\mathcal N)$.
Its $B$-module structure makes the direct image a module over $\mca$.
For $a\in A$, the associated-sheaf description of $\mathcal N$ gives
$$
(f_*\mathcal N)(D_V(a))=N_a.
$$
Thus $(f_*\mathcal N)|_V$ is the sheaf associated to $N$ viewed as an $A$-module, and is quasi-coherent over $\OO_V$.
Morphisms of $\OO_X$-modules induce $B$-linear maps on these section modules and hence $\mca$-linear sheaf morphisms after direct image.

:::

:::

::: {.pf-step #s7}

A quasi-coherent $\mca$-module $\mcm$ determines a quasi-coherent $\OO_X$-module $\widetilde{\mcm}$, and this construction is inverse to direct image.

::: pf-proof

On $V=\Spec A\subseteq Y$, put $B=\mca(V)$ and $M_V=\mcm(V)$, a $B$-module.
On $f^{-1}(V)=\Spec B$, take the associated sheaf $\widetilde{M_V}$.
For a distinguished open $D_V(a)$, quasi-coherence over $\OO_Y$ gives $\mcm(D_V(a))\cong(M_V)_a$.
The associated sheaf of this localized module is exactly the restriction of $\widetilde{M_V}$ to $\Spec B_a$.
These identifications commute with further localization.

Equivalently, the direct image of $\widetilde{M_V}$ to $V$ is canonically $\mcm|_V$, by the distinguished-open calculation.
For any smaller affine open $U\subseteq V$, its restriction to the affine scheme $f^{-1}(U)$ therefore has global module $\mcm(U)$.
The affine sheaf-module equivalence identifies it with $\widetilde{M_U}$.
Using common affine refinements as in step [](#s4){.pf-ref}, these identifications glue the local sheaves to $\widetilde{\mcm}$ on $X$.

An $\mca$-linear map $\mcm\to\mcm'$ gives $B$-linear maps $M_V\to M'_V$ and thus sheaf morphisms on $f^{-1}(V)$.
They commute with the gluing identifications, defining this construction on morphisms and preserving composition and identities.

The same calculations give a natural isomorphism $f_*\widetilde{\mcm}\cong\mcm$ on every affine open of $Y$, hence on $Y$.
For a quasi-coherent $\mathcal N$ on $X$, the isomorphism $\widetilde{f_*\mathcal N}\cong\mathcal N$ on $f^{-1}(V)$ is the canonical affine identification
$$
\widetilde{\Gamma(f^{-1}(V),\mathcal N)}\cong\mathcal N|_{f^{-1}(V)}.
$$
It is natural and compatible with restrictions, so it glues on $X$.
These two natural isomorphisms prove the equivalence of categories, including its morphisms.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), step [](#s2){.pf-ref} proves part (b), steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (c), step [](#s5){.pf-ref} proves part (d), and steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (e).

:::

:::

:::
