---
schema: qual/card@1
id: D-FRVBV
kind: definition
title: Mobius transformation
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

:::{.definition title="Mobius transformation"}
A map of the following form is a **linear fractional transformation** ( or a **Mobius transformation**):
\[  
T(z) = {az + b \over cz + d}
,\]
where the denominator is assumed to not be a multiple of the numerator.
These have inverses given by
\[  
T^{-1}(w) = {dw-b \over -cw + a}
\]
and derivatives given by
\[
T'(z) = {ad-bc \over (cz+d)^2}
,\]
so this is always a conformal map when $ad-bc\neq 0$.
:::
