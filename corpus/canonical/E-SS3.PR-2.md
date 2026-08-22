---
schema: qual/card@1
id: E-SS3.PR-2
kind: exercise
title: "Let u be a harmonic function in the unit disc that is continuous on its closure"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: exercise
2. Let u be a harmonic function in the unit disc that is continuous on its closure. Deduce Poisson’s integral formula

$$

u (z _ {0}) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \frac {1 - | z _ {0} | ^ {2}}{| e ^ {i \theta} - z _ {0} | ^ {2}} u (e ^ {i \theta}) d \theta \quad \mathrm{for} | z _ {0} | <   1

$$

from the special case $z _ { 0 } = 0$ (the mean value theorem). Show that if $z _ { 0 } = r e ^ { i \varphi }$ ， then

$$

\frac {1 - | z _ {0} | ^ {2}}{| e ^ {i \theta} - z _ {0} | ^ {2}} = \frac {1 - r ^ {2}}{1 - 2 r \cos (\theta - \varphi) + r ^ {2}} = P _ {r} (\theta - \varphi),

$$

and we recover the expression for the Poisson kernel derived in the exercises of the previous chapter.

[Hint: Set $u _ { 0 } ( z ) = u ( T ( z ) )$ where

$$

T (z) = \frac {z _ {0} - z}{1 - \overline {{z _ {0}}} z}.

$$

Prove that $u _ { 0 }$ is harmonic. Then apply the mean value theorem to $u _ { 0 }$ , and make a change of variables in the integral.]
:::
