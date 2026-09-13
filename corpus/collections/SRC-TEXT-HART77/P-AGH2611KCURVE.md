---
schema: qual/card@1
id: P-AGH2611KCURVE
kind: problem
title: The Grothendieck group of a nonsingular curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Grothendieck Groups
  - Picard Groups
  - Determinant of a Sheaf
relations: []
review: draft
---

::: problem
Let $X$ be a nonsingular curve over an algebraically closed field $k$.
We show that $K(X) \cong \Pic X \oplus \ZZ$ in several steps.

a. For any divisor $D = \sum n_i P_i$ on $X$, let $\psi(D) = \sum n_i \gamma(k(P_i)) \in K(X)$, where $k(P_i)$ is the skyscraper sheaf $k$ at $P_i$ and $0$ elsewhere.
   If $D$ is an effective divisor, let $\OO_D$ be the structure sheaf of the associated subscheme of codimension $1$, and show that $\psi(D) = \gamma(\OO_D)$.
   Then show that for any $D$, $\psi(D)$ depends only on the linear equivalence class of $D$, so $\psi$ defines a homomorphism $\psi: \Cl X \to K(X)$.

b. For any coherent sheaf $\mcf$ on $X$, show that there exist locally free sheaves $\mce_0$ and $\mce_1$ and an exact sequence $0 \to \mce_1 \to \mce_0 \to \mcf \to 0$.
   Let $r_0 = \rank \mce_0$, $r_1 = \rank \mce_1$, and define
\[
\det \mcf = \left(\bigwedge\nolimits^{r_0} \mce_0\right) \tensor \left(\bigwedge\nolimits^{r_1} \mce_1\right)\inv \in \Pic X
.\]
   Show that $\det \mcf$ is independent of the resolution chosen, and that it gives a homomorphism $\det: K(X) \to \Pic X$.
   Finally show that if $D$ is a divisor then $\det(\psi(D)) = \mcl(D)$.

c. If $\mcf$ is any coherent sheaf of rank $r$, show that there is a divisor $D$ on $X$ and an exact sequence
\[
0 \to \mcl(D)^{\oplus r} \to \mcf \to \mct \to 0,
\]
   where $\mct$ is a torsion sheaf.
   Conclude that if $\mcf$ has rank $r$ then $\gamma(\mcf) - r\gamma(\OO_X) \in \im \psi$.

d. Using the maps $\psi$, $\det$, $\rank$, and $1 \mapsto \gamma(\OO_X)$ from $\ZZ \to K(X)$, show that $K(X) \cong \Pic X \oplus \ZZ$.
:::
