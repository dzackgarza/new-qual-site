---
schema: qual/card@1
id: D-SCHPROJ
kind: definition
title: $\Proj$ of a graded ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proj
  - Graded Rings
  - Projective Space
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What is $\Proj$ of a graded ring?
- Why are the primes containing the irrelevant ideal thrown away?
---

::: {.definition title="The homogeneous spectrum"}
Let $S = \bigoplus_{d \geq 0} S_d$ be a nonnegatively graded commutative ring and
$$
S_+\coloneqq\bigoplus_{d\geq1}S_d
$$
its \dfn{irrelevant ideal}. The \dfn{homogeneous spectrum} $\Proj S$ is the set of homogeneous primes $\mfp$ with $\mfp \not\supseteq S_+$, topologised by the closed sets
$$
V(\mfa)=\theset{\mfp\in\Proj S\st\mfp\supseteq\mfa}
$$
for homogeneous ideals $\mfa\subseteq S$.
Its structure sheaf sends $U$ to the functions $s: U \to \coprod_{\mfp \in U} S_{(\mfp)}$ with $s(\mfp) \in S_{(\mfp)}$ and locally of the form $a/f$ with $a, f$ homogeneous of the *same* degree and $f \notin \mfp$, where $S_{(\mfp)}$ is the degree-zero part of the homogeneous localisation.
:::

::: {.remark}
Each clause removes an affine-cone artifact from the projective construction.

*Homogeneous* primes only, because the closed sets should be cut out by homogeneous equations: a non-homogeneous polynomial does not have a well-defined vanishing locus on lines through the origin.

*Degree zero* fractions only, because a ratio $a/f$ of equal degrees is the thing that is constant on lines, hence an actual function on the projective object.

*Discard $V(S_+)$*, because the primes containing all positive-degree elements belong to the affine-cone locus that projectivization removes.
Since $S/S_+\cong S_0$, this closed subset of $\Spec S$ is canonically $\Spec S_0$.
For $S=k[x_0,\ldots,x_n]$ it is the single affine origin, but over a general base it is an entire copy of the base rather than one extra point.
:::
