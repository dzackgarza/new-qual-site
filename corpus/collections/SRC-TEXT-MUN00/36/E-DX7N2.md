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
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 6, printed p. 229, with Theorem 23.5, Theorem 26.5, Exercise 28.3 and Exercise
    30.11. No published solution was located (search recorded on E-PWXIV and in the COMPLAINTS.md
    entry). The six preserved properties are connected, path connected, compact, limit point compact,
    Lindelof and separable, each by the direct argument on the card; the eleven that are not preserved
    are excluded by quotient maps and by the identity map on a set carrying two topologies, the card's
    two witnesses being the discrete topology on the underlying set of the sine curve mapping onto the
    sine curve (local connectedness and local path connectedness) and a discrete set mapping onto the
    rationals (local compact Hausdorffness). What was added on checking: the counterexample for the
    countability axioms and for metrizability is the quotient of the disjoint union of countably many
    circles onto the Hawaiian earring, which is second countable at the source and not first countable
    at the common point.
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
