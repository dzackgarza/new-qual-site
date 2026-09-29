---
schema: qual/card@1
id: P-AGH65CURVECLOSED
kind: problem
title: A nonsingular projective curve is closed in any ambient variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Curves
  - Projective Varieties
  - Zariski Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.5 and the Chapter I completeness/properness context in the Hartshorne source. The proof uses only that a projective curve is complete and that the image of a complete variety under a morphism to a variety is closed.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a nonsingular projective curve.
Suppose that $X$ is a locally closed subvariety of a variety $Y$.
Show that $X$ is in fact a closed subset of $Y$.
:::

::: {.solution}
::: pf

::: {.pf-step #inclusion-is-morphism}
The locally closed inclusion of $X$ in $Y$ is a morphism of varieties.

::: pf-proof
By hypothesis there is an open subset $U\subseteq Y$ such that $X$ is closed in $U$.
The inclusion $X\hookrightarrow U$ is a closed immersion of varieties and the inclusion $U\hookrightarrow Y$ is an open immersion.
Their composite
$$
i:X\longrightarrow Y
$$
is therefore a morphism whose image is the given subset $X\subseteq Y$.
:::

:::

::: {.pf-step #x-complete}
The variety $X$ is complete.

::: pf-proof
The curve $X$ is projective over $k$ by hypothesis.
Projective varieties are complete, so $X$ is complete in the sense of Chapter I.
:::

:::

::: {.pf-step #image-closed}
The image $i(X)$ is closed in $Y$.

::: pf-proof
A defining property of a complete variety is that its image under every morphism to a variety is closed.
Apply this to the morphism $i:X\to Y$ from step [](#inclusion-is-morphism){.pf-ref}.
Since $X$ is complete by step [](#x-complete){.pf-ref}, the subset
$$
i(X)=X
$$
is closed in $Y$.
:::

:::

::: pf-qed
Step [](#image-closed){.pf-ref} is exactly the required conclusion.
:::

:::
:::
