---
schema: qual/card@1
id: P-G7SZ7
kind: problem
title: $\Hom_{\ZZ}(\ZZ/2\ZZ,-)$ is not right exact
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
Let $\pi: \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ be the canonical quotient homomorphism of $\mathbb{Z}$-modules.
Show that the induced homomorphism on Hom groups:
\[
\pi_*: \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, \mathbb{Z}) \to \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, \mathbb{Z}/2\mathbb{Z}), \quad f \mapsto \pi \circ f
\]
is not surjective, and conclude that the functor $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}/2\mathbb{Z}, -)$ is not right exact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\Hom_{\ZZ}(\ZZ/2\ZZ,\ZZ)=0$.

::: pf-proof

For $f\colon\ZZ/2\ZZ\to\ZZ$, $2f([1])=f([2])=f([0])=0$, and $\ZZ$ has no nonzero element $y$ with $2y=0$, so $f([1])=0$.
Since $[1]$ generates $\ZZ/2\ZZ$, $f=0$.

:::

:::

::: {.pf-step #s2}

$\Hom_{\ZZ}(\ZZ/2\ZZ,\ZZ/2\ZZ)\neq0$.

::: pf-proof

It contains $\operatorname{id}_{\ZZ/2\ZZ}$, which sends $[1]$ to $[1]\neq[0]$.

:::

:::

::: {.pf-step #s3}

$\pi_*$ is not surjective.

::: pf-proof

By step [](#s1){.pf-ref}, the image of $\pi_*$ is $\{0\}$, and by step [](#s2){.pf-ref} the target is nonzero.

:::

:::

::: pf-qed

$\pi$ is surjective, but by step [](#s3){.pf-ref} the induced map $\pi_*$ is not, so $\Hom_{\ZZ}(\ZZ/2\ZZ,-)$ does not preserve the exactness of $\ZZ\xrightarrow{\pi}\ZZ/2\ZZ\to0$.

:::

:::

:::
