---
schema: qual/card@1
id: E-WX8FM
kind: problem
title: Homeomorphisms extend to one-point compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 5, printed p. 186; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.5, PDF p. 22. Extending f by sending the point
    at infinity to the point at infinity gives a bijection which is open, the image of the
    complement of a compact set being the complement of a compact set, and symmetrically.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

If $f: X_1 \to X_2$ is a homeomorphism of locally compact Hausdorff spaces, show $f$ extends to a homeomorphism of their one-point compactifications.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.5, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the extension map and the openness argument are theirs, split below into the two cases.

Let $X_{1}^{+}=X_{1}\cup\theset{\infty_{1}}$ and $X_{2}^{+}=X_{2}\cup\theset{\infty_{2}}$ be the one-point compactifications of the locally compact Hausdorff spaces $X_{1}$, $X_{2}$, and let $f:X_{1}\to X_{2}$ be a homeomorphism.

::: pf

::: {.pf-step #facts}
$X_{i}^{+}$ is compact and Hausdorff and contains $X_{i}$ as an open subspace, and a subset of $X_{i}^{+}$ that is closed in $X_{i}^{+}$ and misses $\infty_{i}$ is compact as a subset of $X_{i}$.

::: pf-proof
The first two assertions are Theorem 29.1. If $C\subseteq X_{i}^{+}$ is closed in $X_{i}^{+}$ and $\infty_{i}\notin C$, then $C\subseteq X_{i}$ and $C$ is a closed subspace of the compact space $X_{i}^{+}$, hence compact (Theorem 26.2); its topology as a subspace of $X_{i}$ is the same, so it is compact as a subset of $X_{i}$.
:::

:::

::: {.pf-step #bijection}
$g:X_{1}^{+}\to X_{2}^{+}$ with $g\restriction_{X_{1}}=f$ and $g(\infty_{1})=\infty_{2}$ is a well defined bijection.

::: pf-proof
$X_{1}^{+}$ is the disjoint union of $X_{1}$ and $\{\infty_{1}\}$, so the two clauses define a map; it is injective because $f$ is injective and $\infty_{2}\notin X_{2}=f(X_{1})$, and surjective because $f$ is surjective onto $X_{2}$ and $\infty_{2}=g(\infty_{1})$.
:::

:::

::: {.pf-step #open-outside}
If $U$ is open in $X_{1}^{+}$ and $\infty_{1}\notin U$, then $g(U)$ is open in $X_{2}^{+}$.

::: pf-proof
Then $U\subseteq X_{1}$, and $U$ is open in the subspace $X_{1}$; $f(U)$ is open in $X_{2}$ because $f$ is a homeomorphism, and $X_{2}$ is open in $X_{2}^{+}$ by step [](#facts){.pf-ref}, so $g(U)=f(U)$ is open in $X_{2}^{+}$.
:::

:::

::: {.pf-step #open-inside}
If $U$ is open in $X_{1}^{+}$ and $\infty_{1}\in U$, then $g(U)$ is open in $X_{2}^{+}$.

::: pf-proof
Put $C=X_{1}^{+}\setminus U$, which is closed in $X_{1}^{+}$ and misses $\infty_{1}$, hence compact as a subset of $X_{1}$ by step [](#facts){.pf-ref}. Then $f(C)$ is compact, being a continuous image of a compact set (Theorem 26.5), hence closed in the Hausdorff space $X_{2}^{+}$ (Theorem 26.3). Since $g$ is a bijection with $g(\infty_{1})=\infty_{2}\notin f(C)$, one has $g(U)=X_{2}^{+}\setminus g(C)=X_{2}^{+}\setminus f(C)$, which is open.
:::

:::

::: {.pf-qed}
$g$ is a bijection by step [](#bijection){.pf-ref} and carries open sets to open sets by steps [](#open-outside){.pf-ref} and [](#open-inside){.pf-ref}, so $g$ is a homeomorphism; it extends $f$ by construction.
:::

:::

:::
