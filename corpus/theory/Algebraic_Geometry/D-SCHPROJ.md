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
Let $S = \bigoplus_{d \geq 0} S_d$ be a graded ring and $S_+ \da \bigoplus_{d \geq 1} S_d$ the \dfn{irrelevant ideal}. Then $\Proj S$ is the set of homogeneous primes $\mfp$ with $\mfp \not\supseteq S_+$, topologised by the closed sets $V(\mfa) = \ts{\mfp \st \mfp \supseteq \mfa}$ for $\mfa$ homogeneous.
Its structure sheaf sends $U$ to the functions $s: U \to \coprod_{\mfp \in U} S_{(\mfp)}$ with $s(\mfp) \in S_{(\mfp)}$ and locally of the form $a/f$ with $a, f$ homogeneous of the *same* degree and $f \notin \mfp$, where $S_{(\mfp)}$ is the degree-zero part of the homogeneous localisation.
:::

::: {.remark}
Every clause answers a question the examiner will ask.

*Homogeneous* primes only, because the closed sets should be cut out by homogeneous equations: a non-homogeneous polynomial does not have a well-defined vanishing locus on lines through the origin.

*Degree zero* fractions only, because a ratio $a/f$ of equal degrees is the thing that is constant on lines, hence an actual function on the projective object.

*Discard $V(S_+)$*, because $S_+$ is the origin of the affine cone, and $\Proj$ is the set of lines through it.
Keeping the irrelevant ideal would add one extra point below everything, which is precisely the point being blown down.
:::
