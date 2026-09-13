---
schema: qual/card@1
id: PR-VARHT
kind: proposition
title: Krull's principal ideal theorem, and codimension one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Krull Dimension
  - Hypersurfaces
relations:
- kind: uses
  target: D-5LJUX
review: draft
prompts:
- State Krull's Hauptidealsatz.
- Which subvarieties of $\AA^n$ have codimension one?
- How do height and dimension of a quotient add up?
---

::: {.theorem title="Hauptidealsatz"}
Let $A$ be Noetherian and $f \in A$ neither a unit nor a zero divisor.
Every minimal prime over $(f)$ has height one.
:::

::: {.proposition title="Consequences used on varieties"}
For $B$ a finitely generated domain over a field and $\mfp \in \Spec B$,
\[
\height \mfp + \krulldim (B/\mfp) = \krulldim B .
\]
Hence a closed irreducible $Y \subseteq \AA^n$ has $\codim Y = 1$ exactly when $Y = V(f)$ for a single irreducible nonconstant $f$, and $B$ Noetherian normal is a UFD exactly when every height-one prime is principal.
:::

::: {.remark}
The Hauptidealsatz is the statement that one equation cuts exactly one dimension, and the codimension-one corollary is the geometric form an examiner will ask for: divisors are hypersurfaces because height-one primes are principal in $k[x_1,\ldots,x_n]$, which is a UFD.

The additivity formula fails without finite generation over a field, and the failure of "height two implies two generators" is the standard warning: the twisted cubic in $\AA^3$ has codimension two and its ideal needs three generators, so codimension does not bound the number of equations.
:::
