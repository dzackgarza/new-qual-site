---
schema: qual/card@1
id: P-ZJQO4
kind: problem
title: $\Hom(\ZZ_2,-)$ sends the epimorphism $\ZZ\to\ZZ_2$ to the zero map
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Exact Sequences
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section IV.4,
    exercise 3, book page 206, read from the page image: "Let π: Z → Z_2 be the
    canonical epimorphism. The induced map π̄: Hom(Z_2, Z) → Hom(Z_2, Z_2) is the
    zero map. Since Hom(Z_2, Z_2) ≠ 0 (Exercise 1(b)), π̄ is not an epimorphism."
    The card states this, and adds the sentence that Hom(Z_2, -) is therefore not
    right exact, which the printed exercise does not spell out but which is
    exactly its point: applied to 0 → Z → Z → Z_2 → 0 the functor ends in
    Hom(Z_2, Z_2) ≠ 0 reached from Hom(Z_2, Z) = 0, so the sequence is not exact
    at the right. That added sentence is true. The proof was checked: a
    homomorphism out of Z_2 into the torsion-free Z is zero, so the induced map
    has zero domain, and the identity of Z_2 is a nonzero element missed by it.
    Complete; no defect.
---

::: {.problem}
Let $\pi\colon \ZZ \to \ZZ_2$ be the canonical epimorphism.
Show that the induced map $\overline{\pi}: \Hom(\ZZ_2, \ZZ) \to \Hom(\ZZ_2, \ZZ_2)$ is the zero map.
Conclude that $\overline{\pi}$ is not an epimorphism, so the functor $\Hom(\ZZ_2, -)$ is not right exact.
:::

::: {.solution}
The induced map is post-composition, $\overline{\pi}(\varphi) = \pi \circ \varphi$.

::: pf

::: {.pf-step #s1}

$\Hom_\ZZ(\ZZ_2, \ZZ) = 0$.

::: pf-proof

Let $\varphi \in \Hom_\ZZ(\ZZ_2, \ZZ)$. Since $2 \cdot 1 = 0$ in $\ZZ_2$,
$$2 \varphi(1) = \varphi(2 \cdot 1) = \varphi(0) = 0 \quad \text{in } \ZZ.$$
As $\ZZ$ is torsion-free, $\varphi(1) = 0$, and since $1$ generates $\ZZ_2$, $\varphi = 0$.

:::

:::

::: {.pf-step #s2}

$\overline{\pi}$ is the zero map.

::: pf-proof

By step [](#s1){.pf-ref} the domain of $\overline\pi$ is $\{0\}$, and $\overline{\pi}(0) = \pi \circ 0 = 0$.

:::

:::

::: pf-step

$\overline{\pi}$ is not an epimorphism.

::: pf-proof

The identity $\id_{\ZZ_2}$ is a nonzero element of $\Hom_\ZZ(\ZZ_2, \ZZ_2)$, since $\id_{\ZZ_2}(1) = 1 \neq 0$. By step [](#s2){.pf-ref} the image of $\overline{\pi}$ is $\{0\}$, so $\overline\pi$ is not surjective.

:::

:::

:::

:::

::: {.remark}
Thus the functor $\Hom_\ZZ(\ZZ_2,-)$ applied to the short exact sequence $0\to\ZZ\xrightarrow{2}\ZZ\xrightarrow{\pi}\ZZ_2\to0$ gives a sequence that is not exact at $\Hom(\ZZ_2,\ZZ_2)$: the functor $\Hom_\ZZ(M,-)$ is left exact but not right exact in general.
:::
