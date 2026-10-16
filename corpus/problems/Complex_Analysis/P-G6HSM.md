---
schema: qual/card@1
id: P-G6HSM
kind: problem
title: $|1-\bar z_1z_2|^2-|z_1-z_2|^2=(1-|z_1|^2)(1-|z_2|^2)$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
For $z_1,z_2\in\CC$:
(a) prove
\[
|1-\bar z_1z_2|^2-|z_1-z_2|^2
=(1-|z_1|^2)(1-|z_2|^2);
\]
(b) deduce that if $|z_1|,|z_2|<1$, then
\[
\left|\frac{z_1-z_2}{1-\bar z_1z_2}\right|<1;
\]
(c) if $z_1\ne z_2$, prove that the last modulus equals $1$ if and only
if $|z_1|=1$ or $|z_2|=1$.
:::

::: {.solution}
Direct expansion gives
\[
|1-\bar z_1z_2|^2-|z_1-z_2|^2
=1-|z_1|^2-|z_2|^2+|z_1|^2|z_2|^2
=(1-|z_1|^2)(1-|z_2|^2).
\]
If $|z_1|,|z_2|<1$, the right side is positive, proving (b). If
$z_1\ne z_2$, then whenever the quotient is defined its modulus equals $1$
exactly when the right side is zero, i.e. exactly when $|z_1|=1$ or
$|z_2|=1$. Under either of those alternatives the denominator cannot vanish
unless $z_1=z_2$, which is excluded, so this also proves the converse in (c).
:::