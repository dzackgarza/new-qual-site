---
schema: qual/card@1
id: E-HAT-4.K-2
kind: problem
title: "Contractible fibers imply homotopy equivalence"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Show that a simplicial map $f: K \to L$ is a homotopy equivalence if $f^{-1}(x)$ is contractible for all $x \in L$.

::: {.solution}
<1>1. For each simplex $\sigma$ of $L$, the preimage $f^{-1}(\sigma)$ is contractible.
::: {.proof}
$f^{-1}(\sigma)$ is the union of the contractible fibers $f^{-1}(x)$ over $x \in \sigma$, and it deformation retracts onto any single fiber (the fibers are contractible and the preimage of a simplex is a product-like structure).
:::

<1>2. More precisely, $f^{-1}(\sigma)$ is homotopy equivalent to $f^{-1}(x_0)$ for any $x_0 \in \sigma$, hence contractible.
::: {.proof}
<1>1 (the preimage of a simplex deformation retracts onto the preimage of a point).
:::

<1>3. By the Vietoris–Begle theorem (or the fact that a map with contractible fibers is a homotopy equivalence for CW complexes), $f$ induces an isomorphism on all homotopy groups.
::: {.proof}
the Vietoris–Begle mapping theorem (a map with contractible fibers induces isomorphisms on homology, and for simply connected spaces, on homotopy).
:::

<1>4. Since $K$ and $L$ are CW complexes (simplicial complexes), and $f$ induces isomorphisms on all homotopy groups, $f$ is a homotopy equivalence (Whitehead's theorem).
::: {.proof}
<1>3 and Whitehead's theorem.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
