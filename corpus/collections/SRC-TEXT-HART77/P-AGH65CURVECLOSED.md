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
A projective variety is complete: the image of a projective variety under a morphism of varieties is closed.
In the language of schemes this is Theorem II.4.9, that a projective morphism of noetherian schemes is proper, together with the closedness of the image of a proper morphism.
The notion of a complete variety is introduced in §II.4 and is quoted here, not derived from Chapter I.
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

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 6.5, PDF p. 8: "we know that $\bar X$ is a curve. If $x\in\bar X-X$ then by 6.8 the map from $X$ to $X$ can be extended to a map from $x\cup X$ to $X$, which is impossible", with the alternative "this problem follows from the fact that the image of any projective variety under a regular map is closed". The first argument does not give the contradiction it claims: the identity of $X$ extends to $\bar X\to\bar X$ carrying $x$ to $x$, and nothing in it forbids that. The alternative is the correct route.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 6.5.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.6.5, PDF p. 54: "note that the image of a projective variety $X$ under a regular embedding $X\hookrightarrow Y$ is closed", which is the assertion of the exercise rather than an argument for it.
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.6.5, PDF p. 25: "embed $X\hookrightarrow Y$ by a regular map; since the image of a projective variety is closed under regular mappings, $X$ is closed in $Y$", the same one-line reduction to closedness of images of projective varieties.
Steps [](#inclusion-is-morphism){.pf-ref} to [](#image-closed){.pf-ref} follow that reduction and state the quoted fact as the completeness of projective varieties, which is where it is proved. Step [](#x-complete){.pf-ref} also withdraws the card's former attribution of completeness to Chapter I, where the notion does not occur. Matches with Cutrone--Marshburn on the reduction.
:::
