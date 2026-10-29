---
schema: qual/card@1
id: PR-HFYSO
kind: proposition
title: A nonnegative function has integral zero if and only if it vanishes almost everywhere
slogan: 'A nonnegative function integrates to zero exactly when it vanishes almost everywhere.'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and $f\in$ [[D-BF5L2|$L^+$]].
Then
$$
\int_X f\dmu = 0 \quad\iff\quad f = 0 \ \mu\text{-almost everywhere}.
$$
:::

::: {.proof}
If $f=0$ almost everywhere, every simple function $0\le s\le f$ vanishes almost everywhere and has integral $0$.
Conversely, suppose $\int_X f\dmu=0$ and put $E_n \coloneqq \theset{x\in X \suchthat f(x) \geq \frac1n}\in\mcm$ for $n\geq1$.
Then $0 = \int_X f\dmu \geq \int_{E_n} f\dmu \geq \frac1n \mu(E_n)$, so $\mu(E_n) = 0$ for every $n$, and $\theset{f\neq0} = \bigcup_{n \geq 1} E_n$ is null.
:::

::: {.remark title="Variations"}
For a [[D-DHFN4|measurable]] $f\colon X\to\CC$, applying the proposition to $\abs{f}$ shows that $\int_X\abs{f}\dmu=0$ if and only if $f=0$ almost everywhere.
:::
