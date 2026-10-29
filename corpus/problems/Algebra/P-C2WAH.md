---
schema: qual/card@1
id: P-C2WAH
kind: problem
title: The nilradical is the intersection of the prime ideals
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves R unspecified; the statement declares R a commutative ring.
---

::: {.problem}
Let $R$ be a commutative ring. The nilradical is the intersection of all prime ideals, i.e.
$$
\nilrad{R} = \Intersect_{\mathfrak{p} \in \Spec(R)} \mathfrak{p}
$$
:::

::: {.solution}

::: pf

::: pf-step

$\nilrad{R}\subseteq\mfp$ for every prime ideal $\mfp$.

::: pf-proof

If $x^n=0\in\mfp$, then induction on $n$, using that $\mfp$ is prime, gives $x\in\mfp$.

:::

:::

::: {.pf-step #zorn}

For a non-nilpotent $a\in R$, let $S$ be the set of ideals $I$ with $a^n\notin I$ for all $n\ge1$. Then $S$ has a maximal element $\mfp$.

::: pf-proof

$(0)\in S$ because $a$ is not nilpotent. The union of a chain in $S$ is an ideal containing no power of $a$, so it lies in $S$. Zorn's lemma gives a maximal element.

:::

:::

::: {.pf-step #prime}

The ideal $\mfp$ of step [](#zorn){.pf-ref} is prime.

::: pf-proof

$\mfp\ne R$ because $a\notin\mfp$. Let $a',b'\notin\mfp$. Then $\mfp+(a')$ and $\mfp+(b')$ strictly contain $\mfp$, so they are not in $S$: $a^m\in\mfp+(a')$ and $a^n\in\mfp+(b')$ for some $m,n$. Multiplying, $a^{m+n}\in\mfp+(a'b')$, so $\mfp+(a'b')\notin S$ and hence $\mfp+(a'b')\ne\mfp$, that is, $a'b'\notin\mfp$.

:::

:::

::: pf-step

$\Intersect_{\mfp\in\Spec(R)}\mfp\subseteq\nilrad{R}$.

::: pf-proof

If $a$ is not nilpotent, the prime ideal $\mfp$ of step [](#prime){.pf-ref} lies in $S$, so $a\notin\mfp$ and $a$ is not in the intersection.

:::

:::

:::

:::

::: {.remark}
The prime ideal $\mfp$ constructed in the solution need not be a maximal ideal; it is maximal only among the ideals that avoid all powers of $a$.
:::
