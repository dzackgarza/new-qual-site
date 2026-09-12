---
schema: qual/card@1
id: E-HAT-1.B-2
kind: problem
title: "Maps to $K(G,1)$ from spaces with trivial $\\pi_1$-to-$G$ homomorphisms"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Lifted an arbitrary map to the contractible universal cover of K(G,1) using the trivial induced fundamental-group homomorphism.
---

Let $X$ be a connected CW complex and $G$ a group such that every homomorphism $\pi_1(X) \to G$ is trivial.
Show that every map $X \to K(G,1)$ is nullhomotopic.


::: {.solution}
Let
\[
f:X\to K(G,1)
\]
be any map and choose basepoints.

<1>1. The induced homomorphism
\[
f_*:\pi_1(X)\to\pi_1(K(G,1))\cong G
\]
is trivial.
::: {.proof}
This is exactly the hypothesis that every homomorphism from $\pi_1(X)$ to $G$ is trivial.
:::

<1>2. The map $f$ lifts to the universal covering space
\[
p:\widetilde K\to K(G,1).
\]
::: {.proof}
Since $X$ is a connected CW complex, it is path connected and locally path connected.
The lifting criterion for the universal cover says that a based map lifts precisely when
\[
f_*\pi_1(X)\subseteq p_*\pi_1(\widetilde K).
\]
The right-hand subgroup is trivial because $\widetilde K$ is simply connected, and the left-hand subgroup is trivial by <1>1.
Hence there is a lift
\[
\widetilde f:X\to\widetilde K
\]
with $p\widetilde f=f$.
:::

<1>3. The universal cover $\widetilde K$ is contractible.
::: {.proof}
Because $K(G,1)$ is aspherical,
\[
\pi_n(K(G,1))=0
\qquad(n\ge2).
\]
A covering induces isomorphisms on all homotopy groups in degrees $n\ge2$, while
\[
\pi_1(\widetilde K)=0.
\]
Thus all homotopy groups of the CW complex $\widetilde K$ vanish.
By Whitehead's theorem, the map $\widetilde K\to *$ is a homotopy equivalence, so $\widetilde K$ is contractible.
:::

<1>4. The map $f$ is nullhomotopic.
::: {.proof}
Since $\widetilde K$ is contractible, the lift $\widetilde f$ is homotopic to a constant map.
Composing this homotopy with $p$ gives a homotopy from
\[
f=p\widetilde f
\]
to a constant map in $K(G,1)$.
:::

<1>5. Hence every map
\[
\boxed{X\to K(G,1)}
\]
is nullhomotopic.
::: {.proof}
The map $f$ was arbitrary.
:::
:::
