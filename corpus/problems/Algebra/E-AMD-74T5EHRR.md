---
schema: qual/card@1
id: E-AMD-74T5EHRR
kind: problem
title: The center of $S_n$ is trivial for $n\geq 3$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose proof into numbered steps and re-checked it: the choice of i and j
    from a moved point, the existence of k outside the two-element set using n >= 3, the two
    evaluations, and the conclusion that the transposition witnesses non-centrality. Nothing was
    changed mathematically. Not checked against a printed source: no AmD (algebra qualifying)
    solution set is retained in tmp/sources, and the card records no page; the exercise text is
    the card's own transcription. The argument remains the card's own, as its solution section
    says.
---

::: {.exercise}
Show that $Z(S_n) = 1$ for $n\geq 3$
:::

::: {.solution}

The argument is the card's own: no solution set for this source is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $S_n$ is the symmetric group on $\theset{1,\dots,n}$ with $n\geq3$, $Z(S_n)$ is its centre, and $(j\ k)$ is the transposition exchanging $j$ and $k$.

::: pf

::: {.pf-step #choose}

Let $\sigma\in S_n$ be nonidentity. Then there is $i$ with $\sigma(i)=j\neq i$, and an element $k\notin\theset{i,j}$.

::: pf-proof

A nonidentity permutation moves some point, giving $i$ and $j=\sigma(i)\neq i$; since $n\geq3$ the set $\theset{1,\dots,n}$ has an element other than the two distinct elements $i,j$.

:::

:::

::: {.pf-step #values}

With $\tau=(j\ k)$, $(\sigma\tau)(i)=j$ and $(\tau\sigma)(i)=k$.

::: pf-proof

$\tau$ fixes $i$, so $(\sigma\tau)(i)=\sigma(\tau(i))=\sigma(i)=j$; and $(\tau\sigma)(i)=\tau(j)=k$ by the definition of the transposition.

:::

:::

::: {.pf-step #noncomm}

$\sigma\tau\neq\tau\sigma$.

::: pf-proof

The two permutations take different values at $i$, since $j\neq k$ by the choice of $k$.

:::

:::

::: {.pf-step #done}

$Z(S_n)=\theset{\mathrm{id}}$ for $n\geq3$.

::: pf-proof

A central element commutes with every element, hence with every transposition $(j\ k)$; step [](#noncomm){.pf-ref} shows that no nonidentity $\sigma$ does, so the centre contains only the identity, and the identity is central.

:::

:::

:::

:::
