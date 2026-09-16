---
schema: qual/card@1
id: P-HU56P
kind: problem
title: 'Frattini''s argument: $G=KN_G(P)$ for a Sylow $p$-subgroup $P$ of a normal
  subgroup $K$'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2010 Groups 3 on PDF page 13, particularly that P is Sylow in K rather than necessarily in G; corrected the area to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked normality at the conjugated-subgroup step, conjugacy by an element of K, and the order of factors in the resulting decomposition g=kn."
---

::: {.problem}
(Frattini) Let $K$ be a normal subgroup of a finite group $G$, and let $P$ be a Sylow $p$-subgroup of $K$.
Recall $N_G(P)$ denotes the normalizer of $P$ in $G$.
Show that $G = KN_G(P)$.
:::

::: {.solution}
<1>1. For every $g\in G$, there is $k\in K$ with
$gPg^{-1}=kPk^{-1}$.

::: {.proof}
Normality gives $gKg^{-1}=K$. Hence $gPg^{-1}$ is a
subgroup of $K$. Conjugation preserves order, so it has
order $|P|$, the largest power of $p$ dividing $|K|$.
It is therefore a Sylow $p$-subgroup of $K$.
Sylow conjugacy, applied inside the finite group $K$,
gives an element $k\in K$ with the asserted equality
[@DF04]. The conjugating element is in $K$, not merely in $G$.
:::

<1>2. Every $g\in G$ belongs to $KN_G(P)$.

::: {.proof}
Choose $k$ as in step <1>1. Then
$$
(k^{-1}g)P(k^{-1}g)^{-1}
=k^{-1}(gPg^{-1})k=P.
$$
Thus $k^{-1}g\in N_G(P)$ and
$g=k(k^{-1}g)\in KN_G(P)$. This proves
$G\subseteq KN_G(P)$. The reverse inclusion holds
because both factors are subsets of the group $G$ and
their products lie in $G$. Hence $G=KN_G(P)$.
:::
:::
