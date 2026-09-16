---
schema: qual/card@1
id: P-NORI-GT-5-05
kind: problem
title: Degree of $F(a^{1/p^n})$ over a field with $p^n$-th roots of unity
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.5 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the degree formulas, moved the source hint to a hint block, and removed the following section note, against Problem 5.5 on pp. 4-5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $p$ be a prime, let $n$ be a natural number, and let $F$ be a field that contains a primitive $p^n$-th root of unity.
Let $a \in F$.
Show that if $\deg(F(a^{1/p})/F) > 1$, then $\deg(F(a^{1/p^n})/F) = p^n$.
:::

::: {.hint}
Let $E = F(b)$ where $b^{p^n} = a$.
Is $E$ a Galois extension of $F$?

Let $u = p^{n-1}$ and let $c = b^u$.
Does a $F$-automorphism $\sigma$ of $F(c)$ extend to an $F$-automorphism of $F(b)$?
:::
