---
schema: qual/card@1
id: P-AGH333LOCALCOH
kind: problem
title: Local cohomology modules of an ideal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Cohomology
  - Derived Functors
  - Commutative Algebra
relations: []
review: draft
---

::: {.problem}
Let $A$ be a noetherian ring, and let $\mfa$ be an ideal of $A$.

a. Show that $\Gamma_{\mfa}(\wait)$ (II, Ex.
5.6) is a left-exact functor from the category of $A$-modules to itself.
We denote its right derived functors, calculated in $\Mod(A)$, by $H_{\mfa}^i(\wait)$.

b. Now let $X=\Spec A$, $Y=V(\mfa)$.
Show that for any $A$-module $M$,
\[
H_{\mfa}^i(M)=H_Y^i(X, \tilde{M}),
\]
where $H_Y^i(X, \wait)$ denotes cohomology with supports in $Y$ (Ex.
2.3).

c. For any $i$, show that $\Gamma_{\mfa}(H_{\mfa}^i(M))=H_{\mfa}^i(M)$.
:::
