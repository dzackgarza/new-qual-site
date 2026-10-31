---
schema: qual/card@1
id: E-DX7N2
kind: problem
title: The seventeen basic properties under continuous maps
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved by continuous maps?
:::

::: {.solution}
For continuous images, exactly the following six properties from the list are preserved in general:
$$
\boxed{(1),(2),(5),(6),(14),(15).}
$$
That is: connectedness, path connectedness, compactness, limit point compactness, Lindelöfness, and existence of a countable dense subset.

The proofs are direct.

- Continuous images of connected and path connected spaces are connected and path connected.
- Continuous images of compact spaces are compact.
- Continuous images of limit point compact spaces are limit point compact, as proved in §28.
- If $X$ is Lindelöf and $f:X\to Y$ is continuous, pull an open cover of $f(X)$ back to $X$, take a countable subcover, and push it forward.
- If $D\subset X$ is countable dense, then $f(D)$ is countable dense in $f(X)$.

None of the other properties is preserved by arbitrary continuous maps. For example, put the discrete topology on the underlying set of the topologist's sine curve and map it by the identity to the usual sine-curve space. The source is locally connected and locally path connected, while the image is neither. Likewise, a discrete set maps continuously by the identity onto $\QQ$ with its usual topology; the source is locally compact Hausdorff, while $\QQ$ is not locally compact. Quotient maps give failures of Hausdorffness, regularity, normality, the countability axioms, and metrizability.
:::
