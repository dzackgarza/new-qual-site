---
schema: qual/card@1
id: E-VFXN4
kind: problem
title: Maps of the projective plane and the torus into the circle
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

(a) Show that every continuous map $f: P^2 \to S^1$ is nulhomotopic.

(b) Find a continuous map of the torus into $S^1$ that is not nulhomotopic.
:::

::: {.solution}
**Goal.** (a) Every map $P^2 \to S^1$ is null-homotopic. (b) Find a non-null-homotopic map $T^2 \to S^1$.

::: pf

::: {.pf-step #s1}

(a) Every map $f: P^2 \to S^1$ is null-homotopic.

::: pf-proof

::: pf-step

$f$ induces $f_*: \pi_1(P^2) = \ZZ/2 \to \pi_1(S^1) = \ZZ$.

::: pf-proof

$\pi_1(P^2) = \ZZ/2$ and $\pi_1(S^1) = \ZZ$.

:::

:::

::: pf-step

$f_* = 0$.

::: pf-proof

the only homomorphism $\ZZ/2 \to \ZZ$ is the zero map (there is no element of order $2$ in $\ZZ$).

:::

:::

::: pf-step

Hence $f$ lifts to the universal cover $\RR \to S^1$.

::: pf-proof

the lifting criterion: $f_*(\pi_1(P^2)) = 0 \subseteq \pi_1(\RR) = 0$, so $f$ lifts to $\tilde f: P^2 \to \RR$.

:::

:::

::: pf-step

$\tilde f$ is null-homotopic (since $\RR$ is contractible).

::: pf-proof

$\RR$ is contractible, so any map into it is null-homotopic.

:::

:::

::: pf-step

Hence $f = p \circ \tilde f$ is null-homotopic.

::: pf-proof

composing a null-homotopy of $\tilde f$ with the covering map $p$ gives a null-homotopy of $f$.

:::

:::

:::

:::

::: {.pf-step #s2}

(b) A non-null-homotopic map $T^2 \to S^1$.

::: pf-proof

::: pf-step

Take the projection $f: T^2 = S^1 \times S^1 \to S^1$ onto the first factor.

::: pf-proof

$f(x, y) = x$.

:::

:::

::: pf-step

$f_*: \pi_1(T^2) = \ZZ \oplus \ZZ \to \pi_1(S^1) = \ZZ$ is the projection onto the first factor.

::: pf-proof

the induced map on $\pi_1$ of a product projection is the projection.

:::

:::

::: pf-step

$f_*$ is nonzero (it is surjective), so $f$ is not null-homotopic.

::: pf-proof

a null-homotopic map induces the zero map on $\pi_1$.

:::

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a); step [](#s2){.pf-ref} gives the example for (b).

:::

:::

:::
