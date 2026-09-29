---
schema: qual/card@1
id: P-AGH367AFFINEEXT
kind: problem
title: Ext on an affine scheme computes module Ext
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Groups
  - Ext Sheaves
  - Affine Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both global and sheaf Ext comparisons with the retained Hartshorne III.6.7 transcription. Checked the first-quadrant double-complex comparison in Stacks Project section 12.25. The proof computes global Ext in Mod(X) using an injective resolution and affine acyclicity, while finite-free sheafification computes sheaf Ext.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X=\Spec A$ be an affine noetherian scheme.
Let $M, N$ be $A$-modules, with $M$ finitely generated.
Then, for every $i\ge0$,
$$
\Ext_X^i(\tilde{M}, \tilde{N}) \cong \Ext_A^i(M, N)
$$
and
$$
\mathcal{E}xt_X^i(\tilde{M}, \tilde{N}) \cong \Ext_A^i(M, N)^{\sim}.
$$
:::

::: {.solution}
Take a finite-free $A$-module resolution $P_\bullet\to M$ and an injective resolution $\widetilde N\to I^\bullet$ in $\Mod(X)$.
The first resolution exists because $M$ is finite and $A$ is noetherian, as in [[P-AGH363EXTCOHERENT]], step 1.
The second exists by [@Har10a, Proposition III.2.2].
Write $L_p=\widetilde P_p$ and $b_p=\operatorname{rank}_A P_p$.

::: pf

::: {.pf-step #s1}
The sheaf-Ext comparison in the statement holds.

::: pf-proof
The sheafified resolution $L_\bullet\to\widetilde M$ is exact and has finite-rank free terms.
It computes sheaf Ext by [@Har10a, Proposition III.6.5].
The natural identifications
$$
\sheafhom_X(L_p,\widetilde N)
\cong\widetilde{\Hom_A(P_p,N)}
$$
commute with the differentials.
Since the associated-sheaf functor is exact, taking cohomology gives
$$
\mathcal{E}xt_X^i(\widetilde M,\widetilde N)
\cong\widetilde{H^i(\Hom_A(P_\bullet,N))}
=\widetilde{\Ext_A^i(M,N)},
$$
as proved in [[P-AGH363EXTCOHERENT]], step 2.
This applies to arbitrary $N$.
:::

:::

::: {.pf-step #s2}
The first-quadrant double complex
$$
C^{p,q}=\Hom_X(L_p,I^q),\qquad p,q\ge0,
$$
has total cohomology $\Ext_X^i(\widetilde M,\widetilde N)$.

::: pf-proof
Its horizontal differential is precomposition with the differential of $L_\bullet$, and its vertical differential is postcomposition with that of $I^\bullet$.
Use total differential $d_h+(-1)^p d_v$ on $C^{p,q}$.
The two component operations commute, so this total differential squares to zero.

For every $q$, injectivity of $I^q$ makes the augmented row
$$
0\to\Hom_X(\widetilde M,I^q)\to\Hom_X(L_0,I^q)
\to\Hom_X(L_1,I^q)\to\cdots
$$
exact.
Thus horizontal cohomology is concentrated in column zero, where it is $\Hom_X(\widetilde M,I^q)$.
The [first-quadrant double-complex comparison](https://stacks.math.columbia.edu/tag/012X) identifies
$$
H^i(\operatorname{Tot}C)\cong H^i(\Hom_X(\widetilde M,I^\bullet))
=\Ext_X^i(\widetilde M,\widetilde N).
$$
The comparison is induced by the augmentation $L_\bullet\to\widetilde M$.
Each total degree involves finitely many terms, so the first-quadrant comparison has no convergence or infinite-product qualification.
:::

:::

::: {.pf-step #s3}
The same total complex has cohomology $\Ext_A^i(M,N)$.

::: pf-proof
For a fixed $p$, the vertical column is
$$
\Hom_X(L_p,I^\bullet)=\Gamma(X,I^\bullet)^{\oplus b_p}.
$$
Injective module sheaves are flasque, hence acyclic for global sections [@Har10a, Lemma III.2.4 and Proposition III.2.5].
Its degree-$q$ cohomology is therefore $H^q(X,\widetilde N)^{\oplus b_p}$.
By [[T-COHAFF|affine vanishing]] [@Har10a, Theorem III.3.5], this is zero for $q>0$.
In degree zero it is
$$
\Hom_X(L_p,\widetilde N)\cong\Hom_A(P_p,N).
$$
These identifications respect the horizontal differential by naturality of sheafification and the affine module correspondence.
The vertical-first double-complex comparison consequently gives
$$
H^i(\operatorname{Tot}C)
\cong H^i(\Hom_A(P_\bullet,N))=\Ext_A^i(M,N).
$$
This comparison is induced by $\widetilde N\to I^\bullet$.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves the sheaf formula, and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} identify global sheaf Ext with module Ext.
All comparison maps arise from the augmentations and the natural Hom identifications.
Maps of modules lift to comparison maps of their resolutions, uniquely up to chain homotopy [@Har10a, Chapter III, §1].
Those comparison maps commute with these constructions, and homotopic choices induce the same maps on cohomology.
Thus the isomorphisms are natural in $M$ and $N$ and independent of the chosen resolutions.
:::

:::
:::
