---
schema: qual/card@1
id: E-HAT-4.1-18
kind: problem
title: "Asymmetric weak homotopy equivalence"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Give an example of a weak homotopy equivalence $X \to Y$ for which there does not exist a weak homotopy equivalence $Y \to X$.

::: {.solution}
**Goal.** Exhibit a weak homotopy equivalence $X \to Y$ with no weak homotopy equivalence $Y \to X$.

<1>1. The example is the pseudocircle: $X = S^1$ and $Y = P$, the pseudocircle (Hatcher, Proposition 4.21).
<2>1. The pseudocircle $P$ is a finite topological space (four points) weakly homotopy equivalent to $S^1$.
::: {.proof}
Hatcher Prop. 4.21 (McCord's construction) gives a finite space $P$ with $\pi_1(P) \cong \ZZ$ and $\pi_n(P) = 0$ for $n \ge 2$, matching $S^1$.
:::
<2>2. There is a weak homotopy equivalence $f: S^1 \to P$.
::: {.proof}
McCord's theorem produces a natural weak equivalence from the geometric realization $|K| \simeq S^1$ to the finite space $P$.
:::

<1>2. There is no weak homotopy equivalence $P \to S^1$.
<2>1. Every continuous map $g: P \to S^1$ is null-homotopic.
::: {.proof}
$P$ is a finite space, and every map from a finite topological space to a CW complex is null-homotopic (the image of a finite space in a CW complex is contained in a finite subcomplex, and a finite space admits no essential maps into a CW complex of positive dimension).
:::
<2>2. Hence $g$ cannot induce an isomorphism on $\pi_1$.
::: {.proof}
$g_*: \pi_1(P) \cong \ZZ \to \pi_1(S^1) \cong \ZZ$ is the zero map (a null-homotopic map induces the trivial map on homotopy groups), not an isomorphism.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 gives a weak equivalence $S^1 \to P$; <1>2 shows no weak equivalence $P \to S^1$ exists.
:::
:::
