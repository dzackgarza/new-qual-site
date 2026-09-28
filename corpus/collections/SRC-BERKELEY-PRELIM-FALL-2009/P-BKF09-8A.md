---
schema: qual/card@1
id: P-BKF09-8A
kind: problem
title: Number of fifth powers in $\mathbb Z/6464\mathbb Z$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the number of elements $a$ in the ring $R=\ZZ/6464\ZZ$ such that $a=x^5$ for some $x\in R$.
:::

::: {.solution}
By the Chinese Remainder Theorem, $R\cong(\ZZ/64\ZZ)\times(\ZZ/101\ZZ)$.
Since $101$ is prime, the multiplicative group $(\ZZ/101\ZZ)^\times$ is cyclic of order $100$. Its subgroup of fifth powers has order $20$. Including $0$, this gives $21$ fifth powers in $\ZZ/101\ZZ$.
The multiplicative group $(\ZZ/64\ZZ)^\times$ has order $32$. Since $32$ is coprime to $5$, every element of $(\ZZ/64\ZZ)^\times$ is a fifth power.
The non-invertible elements of $\ZZ/64\ZZ$ belong to the ideal $(2)$, hence their fifth powers belong to $(2^5)$.
This shows that the only non-invertible fifth powers in $\ZZ/64\ZZ$ are $\{0,32\}$, giving a total of $34$ fifth powers in $\ZZ/64\ZZ$.
Hence there are $21\times34=714$ fifth powers in $R$.
:::
