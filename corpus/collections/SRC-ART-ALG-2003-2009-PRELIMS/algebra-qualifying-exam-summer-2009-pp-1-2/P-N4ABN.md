---
schema: qual/card@1
id: P-N4ABN
kind: problem
title: If $A$ and $B$ are normal and $G/A$, $G/B$ are abelian then $G/(A \cap B)$
  is abelian
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
If $A$ and $B$ are normal in $G$, and $G/A$ and $G/B$ are abelian, show that $G/(A \cap B)$ is also abelian.
:::

::: {.solution}
**Goal.** If $A, B \normal G$ with $G/A$ and $G/B$ abelian, show $G/(A \cap B)$ is abelian.

<1>1. $G/A$ abelian means $[G, G] \subseteq A$.
::: {.proof}
$G/A$ abelian iff the commutator subgroup $[G,G]$ maps to the identity in $G/A$, i.e. $[G,G] \subseteq A$.
:::

<1>2. Similarly $[G, G] \subseteq B$.
::: {.proof}
same argument for $G/B$.
:::

<1>3. Hence $[G, G] \subseteq A \cap B$.
::: {.proof}
$[G,G]$ is contained in both $A$ and $B$.
:::

<1>4. Therefore $G/(A \cap B)$ is abelian.
::: {.proof}
$G/N$ is abelian iff $[G,G] \subseteq N$; here $N = A \cap B$ contains $[G,G]$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 is the claim.
:::
:::
