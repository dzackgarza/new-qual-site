---
schema: qual/card@1
id: P-AGH256SUPPORT
kind: problem
title: Support of a module and sections with support in a closed set
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Support
  - Local Cohomology
relations: []
review: draft
---

::: problem
Recall the notions of support of a section of a sheaf, support of a sheaf, and subsheaf with supports.

a. Let $A$ be a ring, let $M$ be an $A\dash$module, let $X = \Spec A$, and let $\mcf = \tilde M$.
   For any $m \in M = \Gamma(X, \mcf)$, show that $\supp m = V(\Ann m)$, where $\Ann m = \ts{a \in A \st am = 0}$.

b. Now suppose that $A$ is noetherian and $M$ finitely generated.
   Show that $\supp \mcf = V(\Ann M)$.

c. The support of a coherent sheaf on a noetherian scheme is closed.

d. For any ideal $\mfa \subseteq A$, define a submodule $\Gamma_\mfa(M)$ of $M$ by
\[
\Gamma_\mfa(M) = \ts{m \in M \st \mfa^n m = 0 \text{ for some } n > 0}
.\]
   Assume that $A$ is noetherian, and $M$ any $A\dash$module.
   Show that $\Gamma_\mfa(M)^\sim \cong \mch^0_Z(\mcf)$, where $Z = V(\mfa)$ and $\mcf = \tilde M$.

   *Hint:* show a priori that $\mch^0_Z(\mcf)$ is quasi-coherent, then show that $\Gamma_\mfa(M) \cong \Gamma_Z(\mcf)$.

e. Let $X$ be a noetherian scheme, and let $Z$ be a closed subset.
   If $\mcf$ is a quasi-coherent, respectively coherent, $\OO_X\dash$module, then $\mch^0_Z(\mcf)$ is also quasi-coherent, respectively coherent.
:::
