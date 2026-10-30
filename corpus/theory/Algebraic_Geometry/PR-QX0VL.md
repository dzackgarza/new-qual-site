---
schema: qual/card@1
id: PR-QX0VL
kind: proposition
title: Two morphisms agreeing on a dense open agree
slogan: 'Separatedness closes the agreement locus, and reducedness turns dense agreement into equality of morphisms.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Reduced Schemes
  - Density
relations:
- kind: uses
  target: D-T2J3Q
review: draft
prompts:
- Name a good property of separated morphisms.
- If two morphisms agree on a dense open subset, do they agree?
---

::: {.proposition}
Let $f\colon X\to Y$ be separated, let $Z$ be a reduced $Y$-scheme, and let $g,h\colon Z\to X$ be $Y$-morphisms whose restrictions to a dense open subset $U\subseteq Z$ are equal.
Then $g = h$.
:::

::: {.proof}
The pair $(g,h)$ defines
$$
(g,h)\colon Z\longrightarrow X\times_YX.
$$
Let
$$
E\coloneqq Z\times_{X\times_YX,\,(g,h)}X,
$$
where $X\to X\times_YX$ is the diagonal of $f$. Since $f$ is separated, this diagonal is a closed immersion, so $E\hookrightarrow Z$ is a closed immersion. It is the equalizer of $g$ and $h$.

Because $g\restrict_U=h\restrict_U$, the closed subset $\abs E$ contains the dense open subset $U$. Hence $\abs E=\abs Z$. If $\mathcal I\subseteq\OO_Z$ is the ideal sheaf defining $E$, then $V(\mathcal I)=Z$, so $\sqrt{\mathcal I}$ is the nilradical of $\OO_Z$. Since $Z$ is reduced, $\sqrt{\mathcal I}=0$, and therefore $\mathcal I=0$. Thus $E=Z$, so $g=h$.
:::

::: {.remark}
Reducedness is necessary. Let
$$
Z=\Spec k[x,\varepsilon]/(\varepsilon^2,x\varepsilon).
$$
Its underlying space is that of $\Spec k[x]$, because $(\varepsilon)$ is a nilpotent ideal, so $U=D(x)$ is dense in $Z$.
On $U$ one has $\varepsilon=0$, because $x\varepsilon=0$ and $x$ is inverted. Hence the two morphisms
$$
Z\rightrightarrows\AA^1_k
$$
induced by $t\mapsto0$ and $t\mapsto\varepsilon$ agree on $U$.
They are distinct on $Z$, because the image of $\varepsilon$ in $k[x,\varepsilon]/(\varepsilon^2,x) = k[\varepsilon]/(\varepsilon^2)$ is nonzero.
The target $\AA^1_k$ is affine and therefore separated, so the failure comes from the nonreduced source.
:::
