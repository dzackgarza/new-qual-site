---
schema: qual/card@1
id: P-AGH285BLOWUPCANON
kind: problem
title: Picard group and canonical sheaf of a blowing-up
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Picard Groups
  - Canonical Sheaves
relations: []
review: draft
---

::: problem
Let $X$ be a nonsingular variety, let $Y$ be a nonsingular subvariety of codimension $r \geq 2$, let $\pi: \tilde X \to X$ be the blowing-up of $X$ along $Y$, and let $Y' = \pi\inv(Y)$.

a. Show that the maps $\pi^*: \Pic X \to \Pic \tilde X$, and $\ZZ \to \Pic \tilde X$ defined by $n \mapsto$ the class of $nY'$, give rise to an isomorphism $\Pic \tilde X \cong \Pic X \oplus \ZZ$.

b. Show that
\[
\omega_{\tilde X} \cong \pi^* \omega_X \tensor \mcl((r-1) Y')
.\]
   *Hint:* by (a) we can write $\omega_{\tilde X} \cong \pi^* \mcm \tensor \mcl(qY')$ for some invertible sheaf $\mcm$ on $X$ and some integer $q$.
   Restricting to $\tilde X - Y' \cong X - Y$, show that $\mcm \cong \omega_X$.
   To determine $q$, proceed as follows.

    - First show that $\omega_{Y'} \cong \pi^* \omega_X \tensor \OO_{Y'}(-q-1)$.
    - Then take a closed point $y \in Y$ and let $Z$ be the fibre of $Y'$ over $y$.
    - Then show that $\omega_Z \cong \OO_Z(-q-1)$. But $Z \cong \PP^{r-1}$, so $\omega_Z \cong \OO_Z(-r)$, whence $q = r - 1$.
:::
