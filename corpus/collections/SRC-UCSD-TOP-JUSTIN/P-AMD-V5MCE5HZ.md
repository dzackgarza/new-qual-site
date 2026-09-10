---
schema: qual/card@1
id: P-AMD-V5MCE5HZ
kind: problem
title: A map $S^m\to S^n$ homeomorphic onto an open set is a surjection of $S^n$
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
---

::: {.problem}
Show that if $f: S^m \into S^n$ and $\exists U \subset S^m$ such that $\restrictionof{f}{U} \cong f(U)$, then $m=n$ and $f$ is surjective.
:::

::: {.solution}
<1>1. The statement on the retained source sheet is false as written.
::: {.proof}
Take the standard equatorial embedding $f:S^1\hookrightarrow S^2$. For every nonempty open arc $U\subset S^1$, the restriction $f|_U$ is a homeomorphism onto its image, but $m=1\ne2=n$ and $f$ is not surjective.
:::

<1>2. Even requiring $f(U)$ to be open in $S^n$ would not by itself imply surjectivity unless a global injectivity/local-homeomorphism hypothesis is added.
::: {.proof}
A map $S^1\to S^1$ can map one open arc homeomorphically onto an open arc while collapsing or folding the rest of the circle into that same proper arc. Thus a local condition at one open set cannot force global surjectivity.
:::

<1>3. A standard valid correction is: if $f:S^m\to S^n$ is continuous and injective, then $m=n$ implies $f$ is surjective; moreover an injective map between spheres can exist only when $m\le n$, while a homeomorphism from a nonempty open subset of $S^m$ onto an open subset of $S^n$ forces $m=n$ by invariance of dimension.
::: {.proof}
The dimension assertion is invariance of dimension. If $m=n$ and $f$ is injective, invariance of domain makes $f(S^n)$ open in $S^n$; compactness of the domain and Hausdorffness of the target make the image closed. Since $S^n$ is connected and the image is nonempty, it is all of $S^n$.
:::
:::
