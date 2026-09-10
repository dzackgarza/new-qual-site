---
schema: qual/card@1
id: E-L4UAO
kind: problem
title: Separation properties project from products to factors
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Show that if $\prod X_\alpha$ is Hausdorff, or regular, or normal, then so is $X_\alpha$.
(Assume that each $X_\alpha$ is nonempty.)
:::

::: {.solution}
Fix an index \(\alpha\), and choose basepoints \(a_\beta\in X_\beta\) for every \(eta\ne\alpha\). The map
\[
i:X_\alpha\to\prod_\beta X_\beta,
\qquad
 i(x)_\alpha=x,\quad i(x)_\beta=a_\beta\ (\beta\ne\alpha)
\]
is a homeomorphism from \(X_\alpha\) onto the corresponding slice \(S\).

Hausdorffness and regularity are hereditary to subspaces, so if the product is Hausdorff or regular, then \(S\), hence \(X_\alpha\), has the same property.

If the product is normal, then it is \(T_1\), so every singleton \(\{a_\beta\}\) is closed. Hence
\[
S=\bigcap_{\beta\ne\alpha}\pi_\beta^{-1}(\{a_\beta\})
\]
is closed in the product. Closed subspaces of normal spaces are normal. Therefore \(X_\alpha\) is normal as well.
:::
