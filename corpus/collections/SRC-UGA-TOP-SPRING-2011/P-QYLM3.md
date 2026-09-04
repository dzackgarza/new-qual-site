---
schema: qual/card@1
id: P-QYLM3
kind: problem
title: Possible homology of $\RP^2$ with a $2$-cell attached
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
Let $X$ be a topological space obtained by attaching a 2-cell to $\RP^2$ via some map $f: S^1 \to \RP^2$ .

What are the possibilities for the homology $H_* (X; Z)$?
:::

::: {.solution}
<1>1. Up to homotopy, there are exactly two possible attaching maps
\[
f:S^1\to\RP^2:
\]
the nullhomotopic map and a map representing the nonzero element of
\[
\pi_1(\RP^2)\cong\ZZ/2\ZZ.
\]
::: {.proof}
The homotopy classes of based loops in $\RP^2$ form $\pi_1(\RP^2)\cong\ZZ/2\ZZ$.
Since the target is path-connected, free homotopy classes of maps $S^1\to\RP^2$ are conjugacy classes in this group.
The group is abelian, so its two elements give exactly two free homotopy classes.

Attaching a cell along homotopic attaching maps produces homotopy-equivalent adjunction spaces.
Therefore the homology of $X$ depends only on which of these two classes contains $f$.
:::

<1>2. Use the standard CW structure on $\RP^2$ with one cell in each dimension $0,1,2$.
Its cellular chain complex is
\[
0\longrightarrow\ZZ
\xrightarrow{\;2\;}\ZZ
\xrightarrow{\;0\;}\ZZ
\longrightarrow0.
\]
::: {.proof}
The $1$-skeleton is $S^1$.
The original $2$-cell of $\RP^2$ is attached by the degree-$2$ map $S^1\to S^1$, so its cellular boundary is multiplication by $2$.
There is one $0$-cell, hence the boundary $C_1\to C_0$ is zero.
:::

<1>3. If $f$ is nullhomotopic, then the cellular chain complex of $X$ in positive degrees is
\[
0\longrightarrow\ZZ^2
\xrightarrow{\;(2\;0)\;}\ZZ
\xrightarrow{\;0\;}\ZZ
\longrightarrow0.
\]
::: {.proof}
By <1>1 we may take the new attaching map to be constant.
Thus the new $2$-cell contributes zero to the cellular boundary, while the original $2$-cell contributes $2$ by <1>2.
With respect to the basis consisting of the original and new $2$-cells,
\[
d_2(u,v)=2u.
\]
:::

<1>4. In the nullhomotopic case,
\[
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ/2\ZZ,&k=1,\\
\ZZ,&k=2,\\
0,&k\ge3.
\end{cases}
\]
::: {.proof}
For the differential in <1>3,
\[
\ker d_2=\{(0,v):v\in\ZZ\}\cong\ZZ,
\]
so $H_2(X;\ZZ)\cong\ZZ$.
Also
\[
H_1(X;\ZZ)
=
\ZZ/\operatorname{im}(d_2)
=
\ZZ/2\ZZ.
\]
The space is connected, so $H_0\cong\ZZ$, and it has no cells above dimension $2$.
Equivalently, in this case $X\simeq\RP^2\vee S^2$.
:::

<1>5. If $f$ represents the nonzero element of $\pi_1(\RP^2)$, then the cellular chain complex of $X$ in positive degrees is
\[
0\longrightarrow\ZZ^2
\xrightarrow{\;(2\;1)\;}\ZZ
\xrightarrow{\;0\;}\ZZ
\longrightarrow0.
\]
::: {.proof}
By cellular approximation, take the nontrivial attaching map to land in the $1$-skeleton $S^1$.
The generator of $\pi_1(S^1)\cong\ZZ$ maps to the nonzero class modulo $2$ in
\[
\pi_1(\RP^2)\cong\ZZ/2\ZZ,
\]
so we may choose the degree-$1$ loop on the $1$-skeleton as a representative.
Hence the new $2$-cell contributes cellular boundary $1$, while the original $2$-cell contributes $2$.
Thus
\[
d_2(u,v)=2u+v.
\]
:::

<1>6. In the nontrivial case,
\[
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2,\\
0,&k\ne0,2.
\end{cases}
\]
::: {.proof}
The map
\[
d_2:\ZZ^2\to\ZZ,
\qquad
(u,v)\longmapsto2u+v
\]
is surjective, so $H_1(X;\ZZ)=0$.
Its kernel is
\[
\{(u,-2u):u\in\ZZ\}\cong\ZZ,
\]
so $H_2(X;\ZZ)\cong\ZZ$.
Again $H_0\cong\ZZ$ and all groups above degree $2$ vanish.
:::

<1>7. These are the only two possibilities for $H_*(X;\ZZ)$.
::: {.proof}
By <1>1 every attaching map belongs to exactly one of the two homotopy classes, and <1>4 and <1>6 compute the homology in those two cases.
:::
:::
