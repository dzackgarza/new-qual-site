---
schema: qual/card@1
id: P-WI5OS
kind: problem
title: The center of $S_n$ is trivial for $n\geq 4$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The choice of the three distinct points is justified (n >= 3 leaves a c outside {a,b}), the two evaluations are computed from where tau does and does not move points, and the triviality is concluded for n >= 3 and hence for n >= 4 as the exercise's phrasing asks. No retained solution set covers the problem (the collection's provenance is the problem list); the card says the argument is its own. No statement repair.
---

::: {.problem}
Show that the center of $S_n$ for $n\geq 4$ (and in fact $n \ge 3$) is trivial.
:::

::: {.solution}
The collection's provenance is the problem list alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #setup}
Let $n\ge3$ and $\sigma\in Z(S_n)$ with $\sigma\ne\operatorname{id}$. Then there are distinct $a,b,c\in\{1,\dots,n\}$ with $\sigma(a)=b$.

::: pf-proof
$\sigma\ne\operatorname{id}$ gives $a$ with $\sigma(a)=b\ne a$. Since $n\ge3$ the set $\{1,\dots,n\}\setminus\{a,b\}$ is nonempty, so choose $c$ in it; then $a,b,c$ are pairwise distinct.
:::

:::

::: {.pf-step #commutator}
With $\tau=(bc)$, $\sigma\tau(a)=b$ and $\tau\sigma(a)=c$, so $\sigma\tau\ne\tau\sigma$.

::: pf-proof
$\tau=(bc)$ fixes $a$ because $a\notin\{b,c\}$, so $\sigma\tau(a)=\sigma(a)=b$. On the other hand $\tau\sigma(a)=\tau(b)=c$ because $\tau$ interchanges $b$ and $c$. Since $b\ne c$, the two maps differ at $a$.
:::

:::

::: {.pf-step}
$Z(S_n)=\{\operatorname{id}\}$ for every $n\ge3$, hence in particular for $n\ge4$.

::: pf-proof
If $\sigma\in Z(S_n)$ and $\sigma\ne\operatorname{id}$, step [](#commutator){.pf-ref} exhibits $\tau\in S_n$ with $\sigma\tau\ne\tau\sigma$, contradicting $\sigma\in Z(S_n)$. So the centre is trivial; the case $n\ge4$ is included.
:::

:::

:::
:::
