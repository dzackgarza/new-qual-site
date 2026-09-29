---
schema: qual/card@1
id: P-RI6SK
kind: problem
title: $O_p(G)$ is the maximal normal $p$-subgroup of $G$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: The intended statement agrees with the companion corpus card E-AMD-3MQL7TPB; notation was normalized from O_P to O_p.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let \(O_p(G)\) be the intersection of all Sylow \(p\)-subgroups of the finite group \(G\).
Show that \(O_p(G)\trianglelefteq G\), that \(O_p(G)\) is a \(p\)-group, and that it contains every normal \(p\)-subgroup of \(G\).
:::

::: {.solution}
Let
\[
O_p(G)=\bigcap_{P\in\operatorname{Syl}_p(G)}P.
\]

::: pf

::: {.pf-step #s1}

The subgroup \(O_p(G)\) is normal in \(G\).

::: pf-proof

For every \(g\in G\), conjugation sends Sylow \(p\)-subgroups to Sylow \(p\)-subgroups and therefore permutes the set \(\operatorname{Syl}_p(G)\). Hence
\[
gO_p(G)g^{-1}
=\bigcap_{P\in\operatorname{Syl}_p(G)}gPg^{-1}
=\bigcap_{Q\in\operatorname{Syl}_p(G)}Q
=O_p(G).
\]

:::

:::

::: {.pf-step #s2}

The subgroup \(O_p(G)\) is a \(p\)-group.

::: pf-proof

It is contained in every Sylow \(p\)-subgroup, hence in particular in one \(p\)-group. Every subgroup of a finite \(p\)-group is a \(p\)-group.

:::

:::

::: {.pf-step #s3}

Every normal \(p\)-subgroup \(N\trianglelefteq G\) is contained in every Sylow \(p\)-subgroup of \(G\).

::: pf-proof

Fix \(P\in\operatorname{Syl}_p(G)\). Since \(N\trianglelefteq G\), the product \(NP\) is a subgroup of \(G\). Both \(N\) and \(P\) are \(p\)-groups, so
\[
|NP|=\frac{|N|\,|P|}{|N\cap P|}
\]
is a power of \(p\). Thus \(NP\) is a \(p\)-subgroup containing the Sylow subgroup \(P\). Maximality of \(P\) among \(p\)-subgroups gives \(NP=P\), hence \(N\le P\).

:::

:::

::: pf-step

Therefore \(O_p(G)\) is the unique maximal normal \(p\)-subgroup of \(G\).

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, \(O_p(G)\) itself is a normal \(p\)-subgroup. By step [](#s3){.pf-ref}, every normal \(p\)-subgroup \(N\) satisfies
\[
N\le\bigcap_{P\in\operatorname{Syl}_p(G)}P=O_p(G).
\]
Hence \(O_p(G)\) contains every normal \(p\)-subgroup, which is exactly the asserted maximality and uniqueness.

:::

:::

:::

:::
