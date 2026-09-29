---
schema: qual/card@1
id: P-MCG5C
kind: problem
title: Compactness and Euler characteristic of covering spaces, and coverings of even-dimensional
  $\RP^N$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Euler Characteristic
  - Cell Complexes
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $X$ be a CW complex and let $\pi : Y \to X$ be a covering space.

Show that $Y$ is compact iff $X$ is compact and $\pi$ has finite degree.

Assume that $\pi$ has finite degree $d$.
Show show that $\chi (Y ) = d \chi (X)$.

Let $\pi :\RP^N \to X$ be a covering map.
Show that if $N$ is even, $\pi$ is a homeomorphism.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$Y$ is compact iff $X$ is compact and $d<\infty$.

::: pf-proof

covering of compact is compact iff finite sheeted; if $X$ compact and $d<\infty$, $Y$ is finite union of compact lifts.

:::

:::

::: {.pf-step #s2}

If $\deg\pi=d<\infty$ and $X$ is finite CW, $\chi(Y)=d\,\chi(X)$.

::: pf-proof

lift cell structure; $Y$ has $d$ times as many cells in each dimension, so Euler characteristic multiplies by $d$.

:::

:::

::: {.pf-step #s3}

For $\pi:\RP^N\to X$ with $N$ even, $\chi(\RP^N)=1$ (even $N$).

::: pf-proof

$\chi(\RP^{2k})=1$.

:::

:::

::: {.pf-step #s4}

If $d>1$ then $1=\chi(\RP^N)=d\,\chi(X)$ forces $d=1$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} ($d$ divides $1$).

:::

:::

::: {.pf-step #s5}

Hence $\pi$ is a homeomorphism.

::: pf-proof

Step [](#s4){.pf-ref} (degree $1$ covering of nice spaces is homeomorphism).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::
