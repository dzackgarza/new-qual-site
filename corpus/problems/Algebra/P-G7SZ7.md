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
<1>1. $\Hom_{\ZZ}(\ZZ/2\ZZ,\ZZ)=0$.

::: {.proof}
For $f\colon\ZZ/2\ZZ\to\ZZ$, $2f([1])=f([2])=f([0])=0$, and $\ZZ$ has no nonzero element $y$ with $2y=0$, so $f([1])=0$.
Since $[1]$ generates $\ZZ/2\ZZ$, $f=0$.
:::

<1>2. $\Hom_{\ZZ}(\ZZ/2\ZZ,\ZZ/2\ZZ)\neq0$.

::: {.proof}
It contains $\operatorname{id}_{\ZZ/2\ZZ}$, which sends $[1]$ to $[1]\neq[0]$.
:::

<1>3. $\pi_*$ is not surjective.

::: {.proof}
By step <1>1, the image of $\pi_*$ is $\{0\}$, and by step <1>2 the target is nonzero.
:::

<1>4. Q.E.D.

::: {.proof}
$\pi$ is surjective, but by step <1>3 the induced map $\pi_*$ is not, so $\Hom_{\ZZ}(\ZZ/2\ZZ,-)$ does not preserve the exactness of $\ZZ\xrightarrow{\pi}\ZZ/2\ZZ\to0$.
:::
:::
