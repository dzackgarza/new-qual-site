---
schema: qual/card@1
id: E-HAT-3.3-33
kind: exercise
title: "Boundary of contractible manifold is a homology sphere"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show that if $M$ is a compact contractible $n$-manifold then $\partial M$ is a homology $(n-1)$-sphere, that is, $H_i(\partial M; \mathbb{Z}) \approx H_i(S^{n-1}; \mathbb{Z})$ for all $i$.

::: {.solution}
<1>1. $M$ contractible implies $H_i(M)=0$ for $i>0$, $H_0=\Z$.
Proof: contractible.

<1>2. Lefschetz duality: $H_i(M,\partial M)\cong H^{n-i}(M)=0$ for $i<n$.
Proof: duality for compact $n$-manifold.

<1>3. Long exact sequence of pair $(M,\partial M)$: $\cdots\to H_i(\partial M)\to H_i(M)\to H_i(M,\partial M)\to\cdots$.
Proof: LES.

<1>4. For $i<n-1$, $H_i(M,\partial M)=0$ and $H_i(M)=0$, so $H_i(\partial M)=0$.
Proof: <1>2 and <1>3.

<1>5. For $i=n-1$, $0\to H_{n-1}(\partial M)\to0\to\Z\to H_{n-2}(\partial M)\to0$ gives $H_{n-1}(\partial M)\cong\Z$.
Proof: <1>3 with $H_n(M,\partial M)\cong\Z$, $H_n(M)=0$.

<1>6. Hence $H_i(\partial M)\cong H_i(S^{n-1})$.
Proof: <1>4 and <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
