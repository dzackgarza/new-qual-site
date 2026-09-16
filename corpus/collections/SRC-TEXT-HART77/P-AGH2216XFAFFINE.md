---
schema: qual/card@1
id: P-AGH2216XFAFFINE
kind: problem
title: Sections over the nonvanishing locus of a global function
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Global Sections
  - Localization
relations: []
review: draft
---

::: {.problem}
Let $X$ be a scheme, let $f \in \Gamma(X, \OO_X)$, and define $X_f$ to be the subset of points $x \in X$ such that the stalk $f_x$ of $f$ at $x$ is not contained in the maximal ideal $\mfm_x$ of the local ring $\OO_x$.

a. If $U = \Spec B$ is an open affine subscheme of $X$ and $\bar{f} \in B = \Gamma\qty{U, \ro{\OO_X}{U}}$ is the restriction of $f$, show that $U \intersect X_f = D(\bar{f})$.
Conclude that $X_f$ is an open subset of $X$.

b. Assume that $X$ is quasi-compact.
Let $A = \Gamma(X, \OO_X)$ and let $a \in A$ be an element whose restriction to $X_f$ is $0$.
Show that $f^n a = 0$ for some $n > 0$.
Use an open affine cover of $X$.

c. Now assume that $X$ has a finite cover by open affines $U_i$ such that each intersection $U_i \intersect U_j$ is quasi-compact.
This hypothesis is satisfied, for example, if $\operatorname{sp}(X)$ is noetherian.
Let $b \in \Gamma(X_f, \OO_{X_f})$.
Show that for some $n > 0$ the section $f^n b$ is the restriction of an element of $A$.

d. With the hypothesis of (c), conclude that $\Gamma(X_f, \OO_{X_f}) \cong A_f$.
:::
