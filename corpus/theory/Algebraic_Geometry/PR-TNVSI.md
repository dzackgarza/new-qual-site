---
schema: qual/card@1
id: PR-TNVSI
kind: proposition
title: Irreducible decomposition in a Noetherian space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Noetherian Spaces
  - Varieties
relations:
- kind: uses
  target: D-9DIKB
review: draft
prompts:
- Decompose a closed algebraic set into irreducibles.
- In what sense is the decomposition into irreducible components unique?
---

::: {.proposition}
Every closed subset $X$ of a Noetherian space is a finite union
\[
X = X_1 \union \cdots \union X_r
\]
of irreducible closed subsets.
If no $X_i$ contains another, the $X_i$ are unique, and are the **irreducible components** of $X$.
:::

::: {.remark}
Under the correspondence the components of $V(J)$ are $V(\mfp_i)$ for the minimal primes $\mfp_i$ over $J$, so decomposing a variety is finding minimal primes.
The worked case to have ready is a reducible hypersurface: $V(f)$ for $f = \prod f_i^{e_i}$ with the $f_i$ irreducible has components $V(f_i)$, and the multiplicities $e_i$ are invisible to the topology.
That invisibility is exactly what the scheme structure later restores.
:::
