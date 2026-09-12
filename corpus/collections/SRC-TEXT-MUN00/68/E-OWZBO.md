---
schema: qual/card@1
id: E-OWZBO
kind: problem
title: Uniqueness of free products
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
---

::: {.exercise}

Prove Theorem 68.4 (uniqueness of free products): let$\ts{G_\alpha}_{\alpha \in J}$be a family of groups.
Suppose$G$and$G'$are groups and$i_\alpha: G_\alpha \to G$and$i_\alpha': G_\alpha \to G'$are families of monomorphisms such that the families$\ts{i_\alpha(G_\alpha)}$and$\ts{i_\alpha'(G_\alpha)}$are free products with the extension property.
Then there is a unique isomorphism$\phi: G \to G'$such that$\phi \circ i_\alpha = i_\alpha'$for each$\alpha$.
:::

::: {.solution}
By the extension property for the free product family \(\{i_\alpha(G_\alpha)\}\subset G\), applied to the homomorphisms
\[
i'_\alpha:G_\alpha\to G',
\]
there is a unique homomorphism
\[
\phi:G\to G'
\]
such that \(\phi\circ i_\alpha=i'_\alpha\) for every \(\alpha\).

Likewise, the extension property for \(G'\) gives a unique homomorphism
\[
\psi:G'\to G
\]
such that \(\psi\circ i'_\alpha=i_\alpha\) for every \(\alpha\).

For each \(\alpha\),
\[
(\psi\phi)\circ i_\alpha=\psi\circ i'_\alpha=i_\alpha.
\]
The identity map \(1_G\) has the same property. By uniqueness in the extension property for \(G\),
\[
\psi\phi=1_G.
\]
Similarly,
\[
\phi\psi=1_{G'}.
\]
Hence \(\phi\) is an isomorphism with inverse \(\psi\).

If \(\phi':G\to G'\) is another isomorphism satisfying \(\phi' i_\alpha=i'_\alpha\) for every \(\alpha\), then the uniqueness clause in the extension property for \(G\) gives \(\phi'=\phi\). Thus the required isomorphism is unique.
:::
