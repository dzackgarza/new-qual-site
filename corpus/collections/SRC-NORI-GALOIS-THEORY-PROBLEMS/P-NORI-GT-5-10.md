---
schema: qual/card@1
id: P-NORI-GT-5-10
kind: problem
title: Abelian normal closure of $K(a^{1/p})$ is a Kummer extension by an element of $F$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.10 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup of Problems 5.8 and 5.9, on which this problem depends, from p. 5 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $K/F$ be a finite Galois extension with Galois group $G$.
Assume that $K$ contains a primitive $p$-th root of unity.
Let $a \in K^\times$, and let $L$ be the field obtained from $K$ by adjoining $p$-th roots of $\sigma(a)$ for all $\sigma \in G$.
Assume that (i) $\operatorname{Gal}(L/F)$ is Abelian, and (ii) $F$ contains a primitive $p$-th root of unity.

Assume furthermore that $p$ does not divide the order of $\operatorname{Gal}(K/F)$.
Show hat there is some $b \in F$ such that $L = K(b^{1/p})$.
:::
