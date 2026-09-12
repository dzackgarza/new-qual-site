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
\[
\boxed{(1),(2),(5),(6),(14),(15).}
\]
That is: connectedness, path connectedness, compactness, limit point compactness, Lindelöfness, and existence of a countable dense subset.

The proofs are direct.

- Continuous images of connected and path connected spaces are connected and path connected.
- Continuous images of compact spaces are compact.
- Continuous images of limit point compact spaces are limit point compact, as proved in §28.
- If \(X\) is Lindelöf and \(f:X\to Y\) is continuous, pull an open cover of \(f(X)\) back to \(X\), take a countable subcover, and push it forward.
- If \(D\subset X\) is countable dense, then \(f(D)\) is countable dense in \(f(X)\).

None of the other eleven properties is preserved by arbitrary continuous maps. Quotient maps already supply failures for Hausdorffness, regularity, normality, countability axioms, and metrizability; local connectedness/local path connectedness and local compactness likewise fail under general quotients. Identity maps from a finer topology to a coarser topology give further elementary counterexamples. Thus no additional item on the list is functorial under arbitrary continuous images.
:::
