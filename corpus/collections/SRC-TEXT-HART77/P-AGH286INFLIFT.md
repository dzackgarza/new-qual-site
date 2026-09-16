---
schema: qual/card@1
id: P-AGH286INFLIFT
kind: problem
title: The infinitesimal lifting property
classification:
  areas:
  - algebraic-geometry
  topics:
  - Deformation Theory
  - Sheaves of Differentials
  - Derivations
relations: []
review: draft
---

::: {.problem}
The following result is important in studying deformations of nonsingular varieties.
Let $k$ be an algebraically closed field, let $A$ be a finitely generated $k\dash$algebra such that $\Spec A$ is a nonsingular variety over $k$.
Let
\[
0 \to I \to B' \to B \to 0
\]
be an exact sequence, where $B'$ is a $k\dash$algebra and $I$ is an ideal with $I^2 = 0$.
Finally suppose given a $k\dash$algebra homomorphism $f: A \to B$.
Then there exists a $k\dash$algebra homomorphism $g: A \to B'$ lifting $f$, i.e. with $f$ equal to $g$ followed by the surjection $B' \surjects B$.
We call this the **infinitesimal lifting property for $A$**.
Prove it in several steps.

a. First suppose that $g: A \to B'$ is a given homomorphism lifting $f$.
   If $g': A \to B'$ is another such homomorphism, show that $\theta = g - g'$ is a $k\dash$derivation of $A$ into $I$, which we can consider as an element of $\Hom_A(\Omega_{A/k}, I)$.
   Note that since $I^2 = 0$, $I$ has a natural structure of $B\dash$module and hence also of $A\dash$module.
   Conversely, for any $\theta \in \Hom_A(\Omega_{A/k}, I)$, $g' = g + \theta$ is another homomorphism lifting $f$.
   For this step you do not need the hypothesis that $\Spec A$ is nonsingular.

b. Now let $P = k[x_1, \ldots, x_n]$ be a polynomial ring over $k$ of which $A$ is a quotient, and let $J$ be the kernel.
   Show that there does exist a homomorphism $h: P \to B'$ compatible with $f$ and with the surjections $P \surjects A$ and $B' \surjects B$, and show that $h$ induces an $A\dash$linear map $\bar h: J/J^2 \to I$.

c. Now use the hypothesis that $\Spec A$ is nonsingular and (8.17) to obtain an exact sequence
\[
0 \to J/J^2 \to \Omega_{P/k} \tensor A \to \Omega_{A/k} \to 0
.\]
   Show furthermore that applying $\Hom_A(\wait, I)$ gives an exact sequence
\[
0 \to \Hom_A(\Omega_{A/k}, I) \to \Hom_P(\Omega_{P/k}, I) \to \Hom_A(J/J^2, I) \to 0
.\]
   Let $\theta \in \Hom_P(\Omega_{P/k}, I)$ be an element whose image gives $\bar h \in \Hom_A(J/J^2, I)$.
   Consider $\theta$ as a derivation of $P$ into $B'$.
   Then let $h' = h - \theta$, and show that $h'$ is a homomorphism $P \to B'$ with $h'(J) = 0$.
   Thus $h'$ induces the desired homomorphism $g: A \to B'$.
:::
