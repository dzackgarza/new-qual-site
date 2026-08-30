---
schema: qual/card@1
id: P-TOPF24H
kind: problem
title: Compute $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8)$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Compute $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8)$.
:::

::: solution
**Goal:** Compute the torsion product using bilinearity and the cyclic formula.

<1> Expand by direct-sum functoriality:
    $$
    \operatorname{Tor}\!\left(\mathbb Z\oplus\mathbb Z_4,\ \mathbb Z_6\oplus\mathbb Z_8\right)
    \cong \operatorname{Tor}(\mathbb Z,\mathbb Z_6)\oplus \operatorname{Tor}(\mathbb Z,\mathbb Z_8)\oplus \operatorname{Tor}(\mathbb Z_4,\mathbb Z_6)\oplus \operatorname{Tor}(\mathbb Z_4,\mathbb Z_8).
    $$

<1> Use $\operatorname{Tor}(\mathbb Z,A)=0$ for every abelian $A$, and
    $\operatorname{Tor}(\mathbb Z_m,\mathbb Z_n)\cong \mathbb Z_{\gcd(m,n)}$.
    Then
    $$
    \operatorname{Tor}(\mathbb Z,\mathbb Z_6)=0,\qquad
    \operatorname{Tor}(\mathbb Z,\mathbb Z_8)=0,
    $$
    $$
    \operatorname{Tor}(\mathbb Z_4,\mathbb Z_6)\cong\mathbb Z_2,\qquad
    \operatorname{Tor}(\mathbb Z_4,\mathbb Z_8)\cong\mathbb Z_4.
    $$

<1> So
    $$
    \operatorname{Tor}(\mathbb Z\oplus\mathbb Z_4,\mathbb Z_6\oplus\mathbb Z_8)\cong \mathbb Z_2\oplus\mathbb Z_4.
    $$

Authored by **Codex 5.3 Spark Extra High**.
:::
