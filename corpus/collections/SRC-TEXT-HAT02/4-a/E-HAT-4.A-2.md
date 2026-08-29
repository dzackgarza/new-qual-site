---
schema: qual/card@1
id: E-HAT-4.A-2
kind: exercise
title: "$\\pi_1$-action on $\\langle X, Y \\rangle$ and Eilenberg--MacLane spaces"
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
  date: 2026-08-30
---

Show that under the map $\langle X, Y \rangle \to \operatorname{Hom}(\pi_n(X, x_0), \pi_n(Y, y_0))$, $[f] \mapsto f_*$, the action of $\pi_1(Y, y_0)$ on $\langle X, Y \rangle$ corresponds to composing with the action on $\pi_n(Y, y_0)$, that is, $(\gamma f)_* = \beta_\gamma f_*$.
Deduce a bijection of $[X, K(\pi, 1)]$ with the set of orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.

::: {.solution}
<1>1. The action of $\gamma \in \pi_1(Y, y_0)$ on $[f] \in \langle X, Y \rangle$ is given by $\gamma f$, the map obtained by "dragging" $f$ along $\gamma$.
Proof: definition of the $\pi_1(Y)$-action on homotopy classes.

<1>2. On $\pi_n(Y, y_0)$, the action of $\gamma$ is the automorphism $\beta_\gamma$ (conjugation by $\gamma$).
Proof: the standard $\pi_1$-action on higher homotopy groups.

<1>3. The induced map $(\gamma f)_* : \pi_n(X) \to \pi_n(Y)$ equals $\beta_\gamma \circ f_*$.
Proof: the action of $\gamma$ on the map $f$ corresponds, on the induced homomorphism, to post-composing with the action $\beta_\gamma$ on $\pi_n(Y)$.

<1>4. Hence $(\gamma f)_* = \beta_\gamma f_*$.
Proof: <1>3.

<1>5. For $Y = K(\pi, 1)$, $\langle X, K(\pi,1) \rangle \cong \operatorname{Hom}(\pi_1(X), \pi)$ (since $K(\pi,1)$ is an Eilenberg–MacLane space, maps are classified by $\pi_1$).
Proof: the classification of maps into a $K(\pi,1)$.

<1>6. The $\pi_1(K(\pi,1)) = \pi$-action on $\langle X, K(\pi,1) \rangle$ corresponds, under <1>5, to composition with inner automorphisms of $\pi$.
Proof: <1>4 (the action $\beta_\gamma$ on $\pi_1(K(\pi,1)) = \pi$ is conjugation by $\gamma$, an inner automorphism).

<1>7. Hence $[X, K(\pi,1)]$ (the set of orbits) is in bijection with the orbits of $\operatorname{Hom}(\pi_1(X), \pi)$ under composition with inner automorphisms of $\pi$.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>4 and <1>7.
:::
