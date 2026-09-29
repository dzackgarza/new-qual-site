---
schema: qual/card@1
id: P-ZJQO4
kind: problem
title: $\operatorname{Hom}(\ZZ_2,-)$ sends the epimorphism $\ZZ\to\ZZ_2$ to the zero map
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
---

::: {.problem}
Let$\pi: \mathbb{Z} \to \mathbb{Z}_2$ be the canonical epimorphism.
Show that the induced map $\overline{\pi}: \mathrm{Hom}(\mathbb Z_2, \mathbb Z) \to \mathrm{Hom}(\mathbb Z_2, \mathbb Z_2)$ is the zero map.
Conclude that $\overline{\pi}$ is not an epimorphism.
:::

::: {.solution}
The induced map is post-composition, $\overline{\pi}(\varphi) = \pi \circ \varphi$.

::: pf

::: {.pf-step #s1}

$\operatorname{Hom}_\ZZ(\ZZ_2, \ZZ) = 0$.

::: pf-proof

Let $\varphi \in \operatorname{Hom}_\ZZ(\ZZ_2, \ZZ)$. Since $2 \cdot 1 = 0$ in $\ZZ_2$,
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

The identity $\operatorname{id}_{\ZZ_2}$ is a nonzero element of $\operatorname{Hom}_\ZZ(\ZZ_2, \ZZ_2)$, since $\operatorname{id}_{\ZZ_2}(1) = 1 \neq 0$. By step [](#s2){.pf-ref} the image of $\overline{\pi}$ is $\{0\}$, so $\overline\pi$ is not surjective.

:::

:::

:::

:::

::: {.remark}
Thus the functor $\operatorname{Hom}_\ZZ(\ZZ_2,-)$ applied to the short exact sequence $0\to\ZZ\xrightarrow{2}\ZZ\xrightarrow{\pi}\ZZ_2\to0$ gives a sequence that is not exact at $\operatorname{Hom}(\ZZ_2,\ZZ_2)$: the functor $\operatorname{Hom}_\ZZ(M,-)$ is left exact but not right exact in general.
:::
