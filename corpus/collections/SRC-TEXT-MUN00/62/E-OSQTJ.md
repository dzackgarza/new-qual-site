---
schema: qual/card@1
id: E-OSQTJ
kind: problem
title: Compact contractible subsets of the sphere do not separate
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 2, printed p. 384. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The proof is the contrapositive of Lemma 62.2, the
    Borsuk lemma (printed p. 382), which the earlier card cited in paraphrase and without a page; the statement
    of the lemma is now reproduced and applied to the inclusion map, and the identification
    S^2 - {a,b} = R^2 - {0} up to homeomorphism is made explicit. Checked against Lemma 62.1 (printed p. 381)
    and the definition of a nullhomotopic map.
---

::: {.exercise}

Let $A$ be a compact contractible subspace of $S^2$.
Show that $A$ does not separate $S^2$.
:::

::: {.solution}

The Borsuk lemma is Lemma 62.2 (printed p. 382): if $a,b\in S^2$, $A$ is compact, and $f:A\to S^2-\theset{a,b}$ is continuous, injective and nullhomotopic, then $a$ and $b$ lie in the same component of $S^2-f(A)$. We prove the contrapositive for the inclusion.

::: pf

::: pf-step

If $A$ separates $S^2$, there are points $a,b$ in different components of $S^2-A$, and the inclusion $i:A\to S^2-\theset{a,b}$ is nullhomotopic.

::: pf-proof

Choose $a,b$ in two distinct components. Since $a,b\notin A$, the inclusion $i$ has image in $S^2-\theset{a,b}$. Because $A$ is contractible, there is a point $a_0\in A$ and a homotopy $H:A\times I\to A$ from the identity to the constant map at $a_0$; composing with the inclusion of $A$ into $S^2-\theset{a,b}$ gives a homotopy from $i$ to the constant map at $a_0$, so $i$ is nullhomotopic. The map $i$ is injective and its domain is compact.

:::

:::

::: pf-step

Contradiction with Lemma 62.2.

::: pf-proof

Lemma 62.2 applied to $f=i$ gives that $a$ and $b$ lie in the same component of $S^2-i(A)=S^2-A$, contradicting the choice of $a$ and $b$.

:::

:::

::: pf-qed

$S^2-A$ is connected, so a compact contractible subspace of $S^2$ does not separate $S^2$.

:::

:::
:::
