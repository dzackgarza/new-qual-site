---
schema: qual/card@1
id: P-FHQAB
kind: problem
title: A holomorphic function on $\DD\setminus\{0\}$ with $|f(z)|\le\log(1/|z|)$ is
  identically zero
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Maximum Modulus Principle
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic on $\DD\smz$ and $\abs{f(z)} \leq \log\qty{1\over \abs{z}}$, then $f\equiv 0$.
:::

::: {.solution}
\envlist

- Claim: $f$ has a removable singularity at $z_0=0$.

- Thus $f$ extends to some holomorphic $F$ defined on $\DD$.

- By continuity, $\abs{F}$ satisfies the same inequality as $f$.

- Now $\lim_{\abs z \to 1}\abs{F(z)}\leq \lim_{\abs z\to 1} \log\qty{1\over \abs{z}} = 0$, so by the MMP on $\DD$, $F\equiv 0$ on $\DD\smz$.
:::
