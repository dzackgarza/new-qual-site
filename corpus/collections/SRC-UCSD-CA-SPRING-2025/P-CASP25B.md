---
schema: qual/card@1
id: P-CASP25B
kind: problem
title: "Mobius and conformal maps from a sector to the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
  - Conformal Maps
  - Sectors
relations: []
review: draft
---

::: {.problem}
Let $\alpha \in (0, 1]$ and $\Omega_\alpha \subset \mathbb{C}$ denote the open region
$$
\Omega_\alpha := \left\{z = re^{i\theta} : \theta \in \left(-\frac{\alpha\pi}{2}, \frac{\alpha\pi}{2}\right), r > 0\right\}.
$$

(i) Determine for which $\alpha$ there is a Möbius transformation $S$ from $\Omega_\alpha$ onto $\mathbb{D}$.
Prove nonexistence or give an explicit example if such exists.

(ii) Determine for which $\alpha$ there is a conformal map $f$ from $\Omega_\alpha$ onto $\mathbb{D}$.
Prove nonexistence or give an explicit example if such exists.
:::

::: {.solution}
(i) A Möbius transformation exists exactly when $\alpha=1$. In that case
$\Omega_1$ is the right half-plane, and for example
\[
S(z)=\frac{z-1}{z+1}
\]
maps it biholomorphically onto $\mathbb D$.

Now suppose $0<\alpha<1$. The boundary of $\Omega_\alpha$ consists of two
distinct rays lying on two distinct lines through the origin. Möbius
transformations take generalized circles to generalized circles and preserve
incidence. If such a transformation sent $\Omega_\alpha$ onto the disk, both
boundary rays would have to map into the single generalized circle
$\partial\mathbb D$. Their two supporting lines would therefore both have to
map to that same generalized circle, impossible because a Möbius
transformation is injective on generalized circles. Hence no Möbius map exists
for $\alpha<1$.

(ii) A conformal map exists for every $0<\alpha\le1$. On the sector choose the
single-valued branch
\[
w=z^{1/\alpha}.
\]
It maps $\Omega_\alpha$ biholomorphically onto the right half-plane. Composing
with the Cayley map gives
\[
\boxed{
f(z)=\frac{z^{1/\alpha}-1}{z^{1/\alpha}+1},
}
\]
which maps $\Omega_\alpha$ conformally onto $\mathbb D$.
:::
