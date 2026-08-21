---
schema: qual/card@1
id: PR-2ZW5Z
kind: proposition
title: Properties of the norm
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Number Theory
relations: []
review: draft
---

::: {.proposition title="Properties of the norm"}
Let $K$ be a number field with ring of integers $\OO_K$.
The norm is $N: K \to \QQ$, and it restricts to $N: \OO_K \to \ZZ$.

- $N(ab) = N(a)N(b)$ for $a, b\in K$.

- $a\divides b \in \OO_K \implies N(a)\divides N(b)\in \ZZ$.

- $a\in \OO_K\units \iff N(a) = \pm 1$.

The last two statements are about $\OO_K$, not $K$.
In $K$ every nonzero element is a unit and divides every other, so both would be vacuous there.
:::
