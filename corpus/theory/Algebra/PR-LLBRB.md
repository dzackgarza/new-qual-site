---
schema: qual/card@1
id: PR-LLBRB
kind: proposition
title: Inclusions among fields, Euclidean domains, PIDs, UFDs, and integral domains
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Integral Domains
  - Factorization
relations: []
review: draft
---

::: {.proposition}
Every [[D-UI6CU|field]] is a [[D-NKRGN|Euclidean domain]], every Euclidean domain is a [[D-HTIL5|principal ideal domain]], every principal ideal domain is a [[D-INULL|unique factorization domain]], every unique factorization domain is an [[D-QJ3QL|integral domain]], and every integral domain is a commutative [[D-GURUB|ring]]:
$$
\text{Fields} \subset \text{Euclidean domains} \subset \text{PIDs} \subset \text{UFDs} \subset \text{Integral domains} \subset \text{Commutative rings}.
$$
:::

::: {.example}
Each inclusion is proper: $\ZZ$ is a Euclidean domain that is not a field; $\ZZ\big[\tfrac{1+\sqrt{-19}}{2}\big]$ is a PID that is not Euclidean; $\ZZ[x]$ is a UFD that is not a PID; $\ZZ[\sqrt{-5}]$ is an integral domain that is not a UFD; and $\ZZ/4\ZZ$ is a commutative ring that is not an integral domain.
:::
