---
schema: qual/card@1
id: PR-OODAV
kind: proposition
title: "Equivalent conditions for splitting SESs"
classification:
  areas:
  - algebra
  topics:
  - exact-sequences
  - projective-modules
  - homological-algebra
relations: []
review: draft
---

::: {.proposition title="Equivalent conditions for splitting SESs"}
Let $\xi: 0 \to A \mapsvia{d_1} B \mapsvia{d_2}  C \to 0$ be a SES, then TFAE

- $\xi$ admits a right-splitting $s: C\to B$.

- $\xi$ admits a left-splitting $t: B\to A$.

- $\xi$ is isomorphic to a SES of the form $0\to A \to A \oplus C \to C \to 0$.

Projectivity and injectivity are **not** on this list: they are conditions on a module, not on one sequence, and they are sufficient rather than equivalent.
What is true is the quantified version:

- $C$ is projective $\iff$ *every* SES ending in $C$ splits.

- $A$ is injective $\iff$ *every* SES beginning at $A$ splits.

A single $\xi$ can split with $C$ not projective: $0\to \ZZ/2\ZZ \to \ZZ/2\ZZ \oplus \ZZ/2\ZZ \to \ZZ/2\ZZ\to 0$ splits over $\ZZ$, and $\ZZ/2\ZZ$ is not a projective $\ZZ\dash$module.
:::
