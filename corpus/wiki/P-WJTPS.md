---
schema: qual/card@1
id: P-WJTPS
kind: problem
title: Green's theorem for $\int_C xe^x\,dx+(ye^y+x^2)\,dy$ over the upper half of
  $(x-1)^2+y^2=1$
classification:
  areas:
  - prelim
  topics:
  - line-integrals
  - green-s-theorem
relations: []
review: draft
solved: false
---

::: problem
2. We first note that we can rewrite the equation of the region to obtain something more familiar: $x^2 + y^2 = 2x \implies (x-1)^2 + y^2 = 1$, which is a translated circle. Integrating over this region will be easy compared to the line integral, so we apply Green's theorem:
$$
\int_C xe^x ~dx + ye^y +x^2 ~dy = \iint_D 2x ~dA.
$$

    We can parameterize this region as 
  $$
  D = \theset{x^2+y^2-2x = 0 \suchthat (x,y) \in \RR^2, y \geq 0} 
  = \theset{(r(1+ \cos\theta), r\sin\theta) \suchthat \theta \in [0, \pi), r\in [0, 1]}.
  $$ 

    Noting that $dA = r~dr~d\theta$, we can then integrate
  $$
  \iint_D 2x ~dA 
  = \int_0^{\pi} \int_0^1 2(r(1 + \cos\theta)) r ~dr ~d\theta \\
  = 2\int_0^{\pi} \int_0^1 r^2(1+\cos \theta) ~dr ~d\theta \\
  = 2\int_0^{\pi} \frac 1 3 r^3(1+\cos \theta) \bigg\rvert_0^1  ~d\theta\\
  = \frac 2 3 \int_0^{\pi} (1+\cos \theta)  ~d\theta\\
  = \frac 2 3 ( \theta + \sin \theta) \bigg\rvert_0^\pi  \\
  = \frac 2 3 [(\pi + 0) - (0 + 0)]
  = \frac 2 3 \pi. \qed 
  $$
:::
