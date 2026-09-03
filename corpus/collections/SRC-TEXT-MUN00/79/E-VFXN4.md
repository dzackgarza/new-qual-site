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

<1>1. (a) Every map $f: P^2 \to S^1$ is null-homotopic.
<2>1. $f$ induces $f_*: \pi_1(P^2) = \ZZ/2 \to \pi_1(S^1) = \ZZ$.
::: {.proof}
$\pi_1(P^2) = \ZZ/2$ and $\pi_1(S^1) = \ZZ$.
:::
<2>2. $f_* = 0$.
::: {.proof}
the only homomorphism $\ZZ/2 \to \ZZ$ is the zero map (there is no element of order $2$ in $\ZZ$).
:::
<2>3. Hence $f$ lifts to the universal cover $\RR \to S^1$.
::: {.proof}
the lifting criterion: $f_*(\pi_1(P^2)) = 0 \subseteq \pi_1(\RR) = 0$, so $f$ lifts to $\tilde f: P^2 \to \RR$.
:::
<2>4. $\tilde f$ is null-homotopic (since $\RR$ is contractible).
::: {.proof}
$\RR$ is contractible, so any map into it is null-homotopic.
:::
<2>5. Hence $f = p \circ \tilde f$ is null-homotopic.
::: {.proof}
composing a null-homotopy of $\tilde f$ with the covering map $p$ gives a null-homotopy of $f$.
:::

<1>2. (b) A non-null-homotopic map $T^2 \to S^1$.
<2>1. Take the projection $f: T^2 = S^1 \times S^1 \to S^1$ onto the first factor.
::: {.proof}
$f(x, y) = x$.
:::
<2>2. $f_*: \pi_1(T^2) = \ZZ \oplus \ZZ \to \pi_1(S^1) = \ZZ$ is the projection onto the first factor.
::: {.proof}
the induced map on $\pi_1$ of a product projection is the projection.
:::
<2>3. $f_*$ is nonzero (it is surjective), so $f$ is not null-homotopic.
::: {.proof}
a null-homotopic map induces the zero map on $\pi_1$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves (a); <1>2 gives the example for (b).
:::
:::
