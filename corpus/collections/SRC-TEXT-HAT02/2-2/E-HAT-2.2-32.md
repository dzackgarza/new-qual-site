---
schema: qual/card@1
id: E-HAT-2.2-32
kind: problem
title: Mayer–Vietoris gives suspension isomorphism $\tilde{H}_n(SX) \approx \tilde{H}_{n-1}(X)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 32; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

For $SX$ the suspension of $X$, show by a Mayer–Vietoris sequence that there are isomorphisms $\tilde{H}_n(SX) \approx \tilde{H}_{n-1}(X)$ for all $n$.

::: {.solution}
Write the suspension as the union of the upper and lower cones,
\[
SX=C_+X\cup C_-X.
\]
Choose slightly enlarged open cone neighborhoods so that Mayer--Vietoris applies. Each cone is contractible, while their intersection deformation retracts onto the equatorial copy of $X$.

The reduced Mayer--Vietoris sequence contains
\[
\widetilde H_n(C_+X)\oplus\widetilde H_n(C_-X)
\longrightarrow
\widetilde H_n(SX)
\xrightarrow{\delta}
\widetilde H_{n-1}(X)
\longrightarrow
\widetilde H_{n-1}(C_+X)\oplus\widetilde H_{n-1}(C_-X).
\]
Both cone terms vanish, so the connecting homomorphism is an isomorphism:
\[
\boxed{
\widetilde H_n(SX)\cong\widetilde H_{n-1}(X)}
\]
for every $n$.
:::
