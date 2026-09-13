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
---

::: problem
Let $Y$ be a scheme.
A **geometric vector bundle** of rank $n$ over $Y$ is a scheme $X$ and a morphism $f: X \to Y$, together with an open covering $\ts{U_i}$ of $Y$ and isomorphisms $\psi_i: f\inv(U_i) \to \AA^n_{U_i}$, such that for any $i, j$ and any open affine $V = \Spec A \subseteq U_i \intersect U_j$, the automorphism $\psi = \psi_j \circ \psi_i\inv$ of $\AA^n_V = \Spec A[x_1, \ldots, x_n]$ is given by a *linear* automorphism $\theta$ of $A[x_1, \ldots, x_n]$: that is, $\theta(a) = a$ for $a \in A$, and $\theta(x_i) = \sum_j a_{ij} x_j$ for suitable $a_{ij} \in A$.

An **isomorphism** $g: (X, f, \ts{U_i}, \ts{\psi_i}) \to (X', f', \ts{U'_i}, \ts{\psi'_i})$ of vector bundles of rank $n$ is an isomorphism $g: X \to X'$ of the underlying schemes with $f = f' \circ g$, such that $X, f$ together with the covering of $Y$ by all the $U_i$ and $U'_i$, and the isomorphisms $\psi_i$ and $\psi'_i \circ g$, is also a vector bundle structure on $X$.

a. Let $\mce$ be a locally free sheaf of rank $n$ on a scheme $Y$.
   Let $S(\mce)$ be the symmetric algebra on $\mce$, and let $X = \Spec S(\mce)$ with projection $f: X \to Y$.
   For each open affine $U \subseteq Y$ on which $\ro{\mce}{U}$ is free, choose a basis, and let $\psi: f\inv(U) \to \AA^n_U$ be the resulting isomorphism from identifying $S(\mce(U))$ with $\OO(U)[x_1, \ldots, x_n]$.

   Then $(X, f, \ts{U}, \ts{\psi})$ is a vector bundle of rank $n$ over $Y$ which, up to isomorphism, does not depend on the chosen bases.
   We call it the geometric vector bundle associated to $\mce$ and denote it $\mathbf{V}(\mce)$.

b. For any morphism $f: X \to Y$, a **section** of $f$ over an open set $U \subseteq Y$ is a morphism $s: U \to X$ with $f \circ s = \id_U$.
   Sections restrict and glue, so $U \mapsto \ts{\text{sections of } f \text{ over } U}$ is a sheaf of sets on $Y$, denoted $\mcs(X/Y)$.

   Show that if $f: X \to Y$ is a vector bundle of rank $n$, then $\mcs(X/Y)$ has a natural structure of $\OO_Y\dash$module making it locally free of rank $n$.
   *Hint:* define the module structure locally, assuming $Y = \Spec A$ and $X = \AA^n_Y$; a section $s: Y \to X$ comes from an $A\dash$algebra homomorphism $\theta: A[x_1, \ldots, x_n] \to A$, which determines the $n\dash$tuple $\gens{\theta(x_1), \ldots, \theta(x_n)}$ of elements of $A$.

c. Again let $\mce$ be locally free of rank $n$ on $Y$, let $X = \mathbf{V}(\mce)$, and let $\mcs = \mcs(X/Y)$.
   Show that $\mcs \cong \mce\dual$, as follows.
   Given a section $s \in \Gamma(V, \mce\dual)$ over an open set $V$, think of $s$ as an element of $\Hom(\ro{\mce}{V}, \OO_V)$, so $s$ determines an $\OO_V\dash$algebra homomorphism $S(\ro{\mce}{V}) \to \OO_V$.
   This determines a morphism of spectra $V = \Spec \OO_V \to \Spec S(\ro{\mce}{V}) = f\inv(V)$, which is a section of $X/Y$.
   Show that this construction gives an isomorphism of $\mce\dual$ with $\mcs$.

d. Summing up, show that we have a bijection between isomorphism classes of locally free sheaves of rank $n$ on $Y$ and isomorphism classes of vector bundles of rank $n$ over $Y$.
:::
