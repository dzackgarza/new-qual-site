---
schema: qual/card@1
id: PR-2ZW5Z
kind: proposition
title: Multiplicativity of the norm $N_{K/\QQ}$ and units of $\OO_K$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Number Theory
relations: []
review: draft
---

::: {.proposition}
Let $K$ be a number field with ring of integers $\OO_K$.
For $a \in K$, let $N(a) \coloneqq \det(m_a)$, where $m_a\colon K \to K$ is the $\QQ$-linear map $x \mapsto ax$; this defines the norm $N = N_{K/\QQ}\colon K \to \QQ$.

- For all $a, b \in K$, $N(ab) = N(a)N(b)$.

- $N(\OO_K) \subseteq \ZZ$.

- For $a, b \in \OO_K$, if $a$ [[D-AVBIP|divides]] $b$ in $\OO_K$, then $N(a) \divides N(b)$ in $\ZZ$.

- For $a \in \OO_K$, $a$ is a [[D-QQIQZ|unit]] of $\OO_K$ if and only if $N(a) = \pm 1$.
:::
