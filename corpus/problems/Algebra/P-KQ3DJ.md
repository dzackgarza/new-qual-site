---
schema: qual/card@1
id: P-KQ3DJ
kind: problem
title: Projective module
classification:
  areas:
  - algebra
  topics:
  - Projective Modules
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
What is a projective module? Give standard equivalent characterizations.
:::

::: {.solution}

::: pf

::: pf-step
An $R$-module $P$ is projective if for every surjective $R$-linear map $\pi:M\twoheadrightarrow N$ and every $R$-linear map $f:P\to N$ there is an $R$-linear map $\widetilde f:P\to M$ with $\pi\circ\widetilde f=f$.

:::

::: pf-step
The following are equivalent: (i) $P$ is projective; (ii) every short exact sequence $0\to A\to B\to P\to0$ splits; (iii) $P$ is a direct summand of a free module, that is, $P\oplus Q\cong F$ for some module $Q$ and free module $F$; (iv) the functor $\Hom_R(P,-)$ is exact.

::: pf-proof
(i)$\Rightarrow$(ii): lift $\id_P$ along $B\to P$ to obtain a section. (ii)$\Rightarrow$(iii): apply (ii) to a surjection $F\twoheadrightarrow P$ from a free module. (iii)$\Rightarrow$(i): a free module has the lifting property, by choosing preimages of the images of a basis, and a direct summand inherits it by composing with the inclusion and the projection. (i)$\Leftrightarrow$(iv): $\Hom_R(P,-)$ is always left exact, and right exactness says that $\Hom_R(P,M)\to\Hom_R(P,N)$ is surjective for every surjection $M\to N$, which is the lifting property.
:::

:::

::: pf-step
Every free module is projective; over a PID every projective module is free; over a general ring a projective module need not be free.

::: pf-proof
The first claim is (iii). Over a PID every submodule of a free module is free, and a projective module is a submodule of a free module by (iii). Over $R=\ZZ/6\ZZ\cong\ZZ/2\ZZ\times\ZZ/3\ZZ$, the summand $\ZZ/2\ZZ$ is projective but not free, since a nonzero free $R$-module has at least $6$ elements.
:::

:::

:::

:::
