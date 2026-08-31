---
schema: qual/card@1
id: P-ZJQO4
kind: problem
title: Hungerford 4.4.3
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
<1>1. Compute $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z})$:
<2>1. Let $\varphi \in \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z})$.
::: {.proof}
setup.
:::
<2>2. Since $2 \cdot 1 = 0$ in $\mathbb{Z}_2$, linearity implies:
\[
2 \varphi(1) = \varphi(2 \cdot 1) = \varphi(0) = 0 \quad \text{in } \mathbb{Z}.
\]
::: {.proof}
group homomorphism property.
:::
<2>3. In the ring of integers $\mathbb{Z}$, $2k = 0 \implies k = 0$. Thus $\varphi(1) = 0$.
::: {.proof}
$\mathbb{Z}$ has no non-zero torsion.
:::
<2>4. Since $\mathbb{Z}_2 = \langle 1 \rangle$, $\varphi(x) = 0$ for all $x \in \mathbb{Z}_2$, so $\varphi = 0$.
::: {.proof}
homomorphisms out of cyclic groups are determined by the generator.
:::
<2>5. Therefore $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}) = \{0\}$ is the trivial zero group.
::: {.proof}
<2>1 through <2>4.
:::

<1>2. Show that $\overline{\pi} = \pi_*$ is the zero map:
<2>1. The induced map $\overline{\pi}: \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}) \to \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}_2)$ is defined by post-composition: $\overline{\pi}(\varphi) = \pi \circ \varphi$.
::: {.proof}
definition of the covariant functor $\operatorname{Hom}(M, -)$.
:::
<2>2. Since the domain $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}) = \{0\}$ contains only the zero map, $\overline{\pi}(0) = \pi \circ 0 = 0$.
::: {.proof}
composition with zero homomorphism.
:::
<2>3. Thus the image of $\overline{\pi}$ is the single element $\{0\}$, so $\overline{\pi}$ is the zero map.
::: {.proof}
<2>2.
:::

<1>3. Show that $\overline{\pi}$ is not an epimorphism:
<2>1. The identity homomorphism $\operatorname{id}_{\mathbb{Z}_2}: \mathbb{Z}_2 \to \mathbb{Z}_2$ is a non-zero element of $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}_2) \cong \mathbb{Z}_2$.
::: {.proof}
$\operatorname{id}_{\mathbb{Z}_2}(1) = 1 \neq 0$.
:::
<2>2. Since $\operatorname{im}(\overline{\pi}) = \{0\}$ and $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, \mathbb{Z}_2)$ has $2$ elements, $\operatorname{id}_{\mathbb{Z}_2} \notin \operatorname{im}(\overline{\pi})$.
::: {.proof}
<1>2 and <2>1.
:::
<2>3. Therefore $\overline{\pi}$ is not surjective (not an epimorphism).
::: {.proof}
<2>2.
:::

<1>4. Conclusion:
$\overline{\pi}$ is the zero map and fails to be an epimorphism, demonstrating that $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_2, -)$ is not right exact. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
