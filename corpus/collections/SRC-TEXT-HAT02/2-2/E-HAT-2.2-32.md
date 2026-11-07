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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the cover by the two cones: both are contractible and their intersection deformation
    retracts onto the equatorial copy of $X$, so the connecting homomorphism is an isomorphism in
    every degree.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 32 as printed on p. 158. The cone decomposition and the vanishing of the two cone terms are correct; the sequence is now cited to pp. 149-150, the cover is described (two closed cones meeting along X times an interval) and the n = 0 case is tied to the convention that reduced homology vanishes in negative degrees. What is not covered: no certificate.
---

::: {.problem}
For $SX$ the suspension of $X$, show by a Mayer–Vietoris sequence that there are isomorphisms $\tilde{H}_n(SX) \approx \tilde{H}_{n-1}(X)$ for all $n$.
:::

::: {.solution}
Write the suspension as the union of the upper and lower cones,
$$
SX=C_+X\cup C_-X.
$$
Choose slightly enlarged open cone neighborhoods so that Mayer--Vietoris applies: $SX$ is the union of the interiors of two closed cones on $X$, which meet in a copy of $X$ times an interval and deformation retract onto that copy. Each cone is contractible, while their intersection deformation retracts onto the equatorial copy of $X$.

The reduced Mayer--Vietoris sequence, the reduced form of the sequence in the subsection beginning on p. 149 and set out on p. 150, contains
$$
\widetilde H_n(C_+X)\oplus\widetilde H_n(C_-X)
\longrightarrow
\widetilde H_n(SX)
\xrightarrow{\delta}
\widetilde H_{n-1}(X)
\longrightarrow
\widetilde H_{n-1}(C_+X)\oplus\widetilde H_{n-1}(C_-X).
$$
Both cone terms vanish, in every degree including degree $0$ because a cone is contractible and connected, so the connecting homomorphism is an isomorphism:
$$
\boxed{
\widetilde H_n(SX)\cong\widetilde H_{n-1}(X)}
$$
for every $n$, with $\widetilde H_{-1}=0$ by the convention of p. 149 for the case $n=0$.
:::
