---
schema: qual/card@1
id: P-KPSXT
kind: problem
title: An example of a flat module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(a) What is the definition of a **flat module** over a ring $R$?

(b) Give standard examples of flat modules, including an example of a flat module that is not projective/free, and an example of a non-flat module.
:::

::: {.solution}

::: pf

::: pf-step
(a) A right $R$-module $M$ is flat if the functor $-\otimes_R M$ from left $R$-modules to abelian groups is exact.

::: pf-proof
Since tensor product is right exact, this is equivalent to $-\otimes_R M$ preserving injections, and to $\Tor_1^R(N,M)=0$ for every left $R$-module $N$.
:::

:::

::: pf-step
(b) Free and projective modules are flat; $\QQ$ is a flat $\ZZ$-module that is not projective; $\ZZ/n\ZZ$ with $n\ge2$ is a $\ZZ$-module that is not flat.

::: pf-proof

::: pf-step
Every projective module, in particular every free module, is flat.

::: pf-proof
Tensor product commutes with direct sums, so a free module is flat, and a direct summand of a flat module is flat. A projective module is a direct summand of a free module.
:::

:::

::: pf-step
$\QQ$ is a flat $\ZZ$-module that is not projective.

::: pf-proof
$\QQ$ is the localization of $\ZZ$ at $\ZZ\setminus\{0\}$, and localizations are flat. If $\QQ$ were a direct summand of a free abelian group, some coordinate projection would restrict to a nonzero homomorphism $\QQ\to\ZZ$; but $\Hom_{\ZZ}(\QQ,\ZZ)=0$, since the image of a divisible group is divisible and $\ZZ$ has no nonzero divisible subgroup.
:::

:::

::: pf-step
$\ZZ/n\ZZ$ is not flat for $n\ge2$.

::: pf-proof
Tensoring the injection $\ZZ\xrightarrow{\times n}\ZZ$ with $\ZZ/n\ZZ$ gives the zero map $\ZZ/n\ZZ\xrightarrow{0}\ZZ/n\ZZ$, which is not injective.
:::

:::

:::

:::

:::

:::
