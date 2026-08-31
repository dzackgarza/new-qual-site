---
schema: qual/card@1
id: P-AMD-IUGBCO5R
kind: problem
title: The kernel of $A\to A\otimes\QQ$, $a\mapsto a\otimes 1$, is the torsion subgroup
  of $A$
classification:
  areas:
  - topology
  topics:
  - Modules
  - Torsion
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that $\ker A \into A\tensor \QQ$ given by $a \mapsto a\tensor 1$ is the torsion subgroup of $A$.
:::

::: {.solution}
**Goal.** For an abelian group $A$, show the kernel of $A \to A \otimes \QQ$, $a \mapsto a \otimes 1$, is the torsion subgroup $T(A)$.

<1>1. Every torsion element lies in the kernel.
<2>1. If $a \in A$ has $na = 0$ for some $n > 0$, then $a \otimes 1 = 0$ in $A \otimes \QQ$.
::: {.proof}
$a \otimes 1 = a \otimes (n \cdot \frac1n) = (na) \otimes \frac1n = 0 \otimes \frac1n = 0$.
:::
<2>2. Hence $T(A) \subseteq \ker$.
::: {.proof}
<1>1.1 applies to every torsion element.
:::

<1>2. Every element of the kernel is torsion.
<2>1. $A \otimes \QQ \cong S^{-1}A$ where $S = \ZZ \sm \theset{0}$.
::: {.proof}
$\QQ$ is the localization of $\ZZ$ at the nonzero integers, and $A \otimes \QQ \cong A \otimes S^{-1}\ZZ \cong S^{-1}A$.
:::
<2>2. The map $A \to S^{-1}A$, $a \mapsto a/1$, has kernel exactly $T(A)$.
::: {.proof}
$a/1 = 0$ in $S^{-1}A$ iff $sa = 0$ for some $s \in S$, i.e. iff $a$ is torsion.
:::
<2>3. Hence $\ker = T(A)$.
::: {.proof}
combine <1>2.1 and <1>2.2.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2 give both inclusions.
:::
:::
