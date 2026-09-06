---
schema: qual/card@1
id: P-AMD-5H2CPVWT
kind: problem
title: Normal subgroups with trivial intersection commute elementwise
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Commutators
  - Direct Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against the source-audited UCSD Math 200A Homework 1 occurrence and independently against standard group-theory statements of the trivial-intersection commutator lemma.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For h in H and k in K, showed hkh^{-1}k^{-1} lies in K by normality of K and in H by normality of H; trivial intersection forces the commutator to be the identity.
---

::: {.problem}
Given: $H \normal G, K \normal G,H \intersect K = e$

Show: $\forall h\in H, \forall k\in K, hk = kh$
:::

::: {.solution}
Let $h\in H$ and $k\in K$ be arbitrary, and set
\[
c=hkh^{-1}k^{-1}.
\]

<1>1. The element $c$ belongs to $K$.
::: {.proof}
Since $K\trianglelefteq G$ and $k\in K$,
\[
hkh^{-1}\in K.
\]
Also $k^{-1}\in K$ because $K$ is a subgroup.
Therefore
\[
c=(hkh^{-1})k^{-1}\in K.
\]
:::

<1>2. The element $c$ belongs to $H$.
::: {.proof}
Since $H\trianglelefteq G$ and $h^{-1}\in H$,
\[
kh^{-1}k^{-1}\in H.
\]
Also $h\in H$.
Therefore
\[
c=h(kh^{-1}k^{-1})\in H.
\]
:::

<1>3. One has $c=e$.
::: {.proof}
By <1>1 and <1>2,
\[
c\in H\cap K.
\]
The hypothesis says
\[
H\cap K=\{e\}.
\]
Hence
\[
c=e.
\]
:::

<1>4. The elements $h$ and $k$ commute.
::: {.proof}
From <1>3,
\[
hkh^{-1}k^{-1}=e.
\]
Multiplying on the right by $k$ and then by $h$ gives
\[
hk=kh.
\]
Since $h\in H$ and $k\in K$ were arbitrary, the two normal subgroups commute elementwise.
:::
:::
