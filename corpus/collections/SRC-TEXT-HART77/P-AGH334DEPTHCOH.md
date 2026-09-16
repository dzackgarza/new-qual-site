---
schema: qual/card@1
id: P-AGH334DEPTHCOH
kind: problem
title: Cohomological interpretation of depth
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Cohomology
  - Depth
  - Regular Sequences
relations: []
review: draft
---

::: {.problem}
If $A$ is a ring, $\mfa$ an ideal, and $M$ an $A$-module, then $\depth_\mfa M$ is the maximum length of an $M$-regular sequence $x_1, \ldots, x_r$, with all $x_i \in \mfa$. This generalizes the notion of depth introduced in (II, §8).

a. Assume that $A$ is noetherian. Show that if $\depth_\mfa M \geq 1$, then $\Gamma_{\mfa}(M)=0$, and the converse is true if $M$ is finitely generated.

Hint: When $M$ is finitely generated, both conditions are equivalent to saying that $\mfa$ is not contained in any associated prime of $M$.

b. Show inductively, for $M$ finitely generated, that for any $n \geq 0$, the following conditions are equivalent:

    (i) $\depth_{\mfa} M \geq n$;

    (ii) $H_\mfa^i(M)=0$ for all $i<n$.
:::
