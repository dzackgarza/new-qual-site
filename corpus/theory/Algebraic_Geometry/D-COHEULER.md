---
schema: qual/card@1
id: D-COHEULER
kind: definition
title: The Euler characteristic and the Hilbert polynomial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Euler Characteristic
  - Hilbert Polynomial
  - Cohomology
relations:
- kind: uses
  target: T-COHFIN
- kind: uses
  target: T-COHSVAN
review: draft
prompts:
- Define the Euler characteristic of a coherent sheaf.
- Why is the Euler characteristic additive?
- How is the Hilbert polynomial defined cohomologically?
---

::: {.definition}
For $X$ projective over a field and $\mcf \in \Coh(X)$,
\[
\chi(\mcf) \da \sum_{i \geq 0} (-1)^i h^i(X, \mcf) ,
\]
a finite sum.
The Hilbert polynomial of $\mcf$ is the unique $P \in \QQ[z]$ with $P(n) = \chi(\mcf(n))$ for all $n$.
:::

::: {.proposition}
$\chi$ is additive: $\chi(\mcf) = \chi(\mcf') + \chi(\mcf'')$ for every short exact sequence $0 \to \mcf' \to \mcf \to \mcf'' \to 0$.
:::

::: {.remark}
Additivity is the alternating sum of the long exact sequence, and it is the whole reason $\chi$ is a better invariant than any single $h^i$: the individual dimensions are not additive, and they jump.
$\chi$ is therefore the object every theorem is stated about — Riemann--Roch, the Hilbert polynomial, arithmetic genus $p_a = (-1)^{\dim X}(\chi(\OO_X) - 1)$ — while duality is what turns $\chi$ back into individual $h^i$.

That $\chi(\mcf(n))$ is a *polynomial* in $n$ is the cohomological form of the statement that the Hilbert function of a graded module is eventually polynomial; for $n \gg 0$ Serre vanishing collapses the sum to $h^0(\mcf(n))$, which is that Hilbert function.
:::
