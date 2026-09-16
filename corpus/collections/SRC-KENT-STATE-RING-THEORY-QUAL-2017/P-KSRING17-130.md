---
schema: qual/card@1
id: P-KSRING17-130
kind: problem
title: Maximal and minimal elements in sets of prime ideals
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 130 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked problem 130 on Ring_Theory_Qual_Problems.pdf PDF page 16 and added an erratum because the statement is false for arbitrary sets of prime ideals.
---

::: {.problem}
Let $R$ be a commutative ring with identity.
Prove that any non-empty set of prime ideals of $R$ contains maximal *and* minimal elements.
:::

::: {.remark}
Erratum: the statement is false as written in the source.
Let $k$ be a field, $R = k[x_1, x_2, x_3, \ldots]$, and $P_n = (x_1, \ldots, x_n)$.
Each $P_n$ is prime, since $R/P_n \cong k[x_{n+1}, x_{n+2}, \ldots]$ is a domain, and $P_1 \subsetneq P_2 \subsetneq \cdots$.
The non-empty set $\{P_n : n \geq 1\}$ has no maximal element.
Likewise the prime ideals $Q_n = (x_n, x_{n+1}, \ldots)$, with $R/Q_n \cong k[x_1, \ldots, x_{n-1}]$, satisfy $Q_1 \supsetneq Q_2 \supsetneq \cdots$, so the non-empty set $\{Q_n : n \geq 1\}$ has no minimal element.
The statement becomes true, by Zorn's lemma, for a non-empty set of prime ideals that contains the union and the intersection of each of its non-empty chains (the union and the intersection of a chain of prime ideals are prime); for example, the set of all prime ideals of a nonzero ring, or the set of all prime ideals containing a given proper ideal.
:::
