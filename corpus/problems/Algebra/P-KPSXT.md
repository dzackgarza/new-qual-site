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

::: problem
(1) What is the definition of a **flat module** over a ring $R$?
(2) Give standard examples of flat modules, including an example of a flat module that is not projective/free, and an example of a non-flat module.
:::

::: solution
A right $R$-module $M$ is **flat** if the functor
\[
-\otimes_R M
\]
from left $R$-modules to abelian groups is exact. Since tensor product is always right-exact, this is equivalent to requiring that tensoring with $M$ preserve injections. Equivalently,
\[
\operatorname{Tor}_1^R(N,M)=0
\]
for every left $R$-module $N$.

Every free module is flat, and every projective module is flat because a projective module is a direct summand of a free module.

A standard flat nonprojective example is $\mathbb Q$ as a $\mathbb Z$-module. It is a localization of $\mathbb Z$, hence flat. It is not projective: if it were a direct summand of a free abelian group, some coordinate projection would give a nonzero homomorphism $\mathbb Q\to\mathbb Z$, but
\[
\operatorname{Hom}_{\mathbb Z}(\mathbb Q,\mathbb Z)=0.
\]

A standard non-flat example is $\mathbb Z/n\mathbb Z$ for $n\ge2$. Tensoring the injection
\[
\mathbb Z\xrightarrow{\times n}\mathbb Z
\]
with $\mathbb Z/n\mathbb Z$ gives the zero map
\[
\mathbb Z/n\mathbb Z\xrightarrow{0}\mathbb Z/n\mathbb Z,
\]
which is not injective. Thus $\mathbb Z/n\mathbb Z$ is not flat.
:::
