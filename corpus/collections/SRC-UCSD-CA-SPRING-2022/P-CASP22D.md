---
schema: qual/card@1
id: P-CASP22D
kind: problem
title: "Equivalence of two-component complement and rational approximation with prescribed poles"
classification:
  areas:
  - complex-analysis
  topics:
  - Rational Approximation
  - Runge Theorem
  - Simply Connected
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, with Runge's theorem in pole-set form
    stated once as its own step and cited without a theorem number (the numbering differs between
    editions of Rudin and Conway, so only chapter-level attribution is given). Forward direction:
    A = {0, infinity} meets both complementary components. Backward direction: density forces
    {0, infinity} to meet every component, so there are at most two; and the complement cannot be
    connected, since for a region in the plane having a connected complement in the sphere is
    equivalent to being simply connected and G is assumed not simply connected. The step also now
    draws the consequence the prose left implicit: infinity is not in G, because otherwise {0}
    alone would meet the complement and G would be simply connected. Statement unchanged; the card
    says the argument is its own.
---

::: {.problem}
Let $G \subset \CC$ be a region such that $0 \notin G$ and $G$ is not simply connected.
Show that the following are equivalent:

(i) $\CC_\infty \setminus G$ has precisely two components $F_0, F_\infty$ such that $0 \in F_0$, $\infty \in F_\infty$.

(ii) Every $f \in H(G)$ can be approximated in $H(G)$ by rational functions with poles only in $\{0, \infty\}$.
:::

::: {.solution}
Both directions are the pole-set form of Runge's theorem: rational functions with poles confined to a set $A$ are dense in $H(G)$ exactly when $A$ meets every component of $\CC_\infty\setminus G$. In the forward direction $A=\{0,\infty\}$ meets both complementary components; in the backward direction density forces $\{0,\infty\}$ to meet every component, so there are at most two, and not one, since a plane region whose complement in the sphere is connected is simply connected. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #runge}
For a region $G\subseteq\CC_\infty$ and a subset $A\subseteq\CC_\infty\setminus G$, the rational functions with poles in $A$ are dense in $H(G)$ if and only if $A$ meets every connected component of $\CC_\infty\setminus G$.

::: pf-proof
This is Runge's theorem in its pole-set form, as stated for plane regions in the standard texts (Rudin, *Real and Complex Analysis*, the chapter on Runge's theorem; Conway, *Functions of One Complex Variable*, the chapter on Runge theory). It is quoted, not re-proved, and it is the only input to both directions below; no theorem number is cited, since the numbering differs between editions.
:::

:::


::: {.pf-step #forward}
(i) implies (ii).

::: pf-proof
Assume (i): $\CC_\infty\setminus G=F_0\cup F_\infty$ with $0\in F_0$ and $\infty\in F_\infty$ and the two sets the components. Then $A=\{0,\infty\}\subseteq\CC_\infty\setminus G$ meets each component, so by step [](#runge){.pf-ref} the rational functions with poles in $A$ — that is, with poles only at $0$ and $\infty$ — are dense in $H(G)$, which is (ii).
:::

:::


::: {.pf-step #backward-count}
If (ii) holds then $\CC_\infty\setminus G$ has at most two components, and $\infty\notin G$.

::: pf-proof
By step [](#runge){.pf-ref} the density in (ii) says that $\{0,\infty\}$ meets every component of the complement. Each component then contains $0$ or $\infty$, and the two points are distinct and lie in the complement ($0\notin G$ by hypothesis), so there are at most two components. In particular, if $\infty\in G$ then the complement is met by $\{0\}$ alone, so it is connected.
:::

:::


::: {.pf-step #backward-two}
If (ii) holds then $\CC_\infty\setminus G$ has exactly two components, so (i) holds.

::: pf-proof
It has at most two by step [](#backward-count){.pf-ref}. It cannot have exactly one: a region $G\subset\CC$ is simply connected if and only if $\CC_\infty\setminus G$ is connected, and $G$ is assumed not simply connected. So there are exactly two, and by step [](#backward-count){.pf-ref} one contains $0$ and the other $\infty$; call them $F_0$ and $F_\infty$. Since $0\in\CC_\infty\setminus G$ by hypothesis and $\infty\notin G$ as shown, these are the two components with $0\in F_0$ and $\infty\in F_\infty$, which is (i).
:::

:::


::: {.pf-step #conclusion}
Conditions (i) and (ii) are equivalent.

::: pf-proof
Step [](#forward){.pf-ref} gives (i) $\Rightarrow$ (ii) and step [](#backward-two){.pf-ref} gives (ii) $\Rightarrow$ (i), for a region $G$ with $0\notin G$ that is not simply connected — the two hypotheses used.
:::

:::

:::
:::
