---
schema: qual/card@1
id: D-HFR32
kind: definition
title: "Homotopy Equivalence"
classification:
  areas:
  - topology
  topics:
  - homotopy
relations: []
review: draft
---

::: {.definition title="Homotopy Equivalence"}
Let $f: X \to Y$ be a continuous map, then $f$ is said to be a *homotopy equivalence* if there exists a continuous map $g: X \to Y$ such that

$f\circ g \homotopic \id_Y$ and $g\circ f \homotopic \id_X$.

Such a map $g$ is called a homotopy inverse of $f$, the pair of maps is a homotopy equivalence.

If such an $f$ exists, we write $X \homotopic Y$ and say $X$ and $Y$ have the same homotopy type, or that they are homotopy equivalent.

> Note that homotopy equivalence is strictly weaker than homeomorphic equivalence, i.e., $X\cong Y$ implies $X \homotopic Y$ but not necessarily the converse.
:::
