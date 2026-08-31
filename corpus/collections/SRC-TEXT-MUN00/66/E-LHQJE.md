---
schema: qual/card@1
id: E-LHQJE
kind: exercise
title: The winding number as a degree
classification:
  areas:
  - topology
  topics:
  - Winding Number
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $f$ be a loop in $\mathbb{R}^2 - a$; let $g(s) = [f(s) - a]/\norm{f(s) - a}$.
The map $g$ induces, via the standard quotient map $p: I \to S^1$, a continuous map $h: S^1 \to S^1$.
Show that $n(f, a)$ equals the degree of $h$, as defined in [[E-UU8CC]].
:::

::: {.solution}
<1>1. Lifting and definition of the winding number:
<2>1. Consider the standard universal covering map $e: \mathbb{R} \to S^1$ given by $e(t) = (\cos 2\pi t, \sin 2\pi t) = e^{2\pi i t}$.
The normalized loop $g: [0, 1] \to S^1$ is defined by:
\[
g(s) = \frac{f(s) - a}{\|f(s) - a\|}.
\]
::: {.proof}
definition of radial projection onto $S^1$.
:::
<2>2. By the Path Lifting Property for covering spaces, given any choice of $\tilde{g}(0) = t_0 \in e^{-1}(g(0))$, there exists a unique continuous lift $\tilde{g}: [0, 1] \to \mathbb{R}$ such that $e \circ \tilde{g} = g$.
::: {.proof}
Path Lifting Theorem for covering spaces.
:::
<2>3. By definition, the winding number of the loop $f$ around $a$ is the integer change:
\[
n(f, a) = \tilde{g}(1) - \tilde{g}(0).
\]
::: {.proof}
standard definition of winding number via angular lifting.
:::

<1>2. Lifting and definition of the degree of $h: S^1 \to S^1$:
<2>1. The quotient map $p: [0, 1] \to S^1$ is $p(s) = e(s)$.
The continuous map $h: S^1 \to S^1$ satisfies $h(p(s)) = g(s)$ for all $s \in [0, 1]$.
::: {.proof}
definition of the induced map $h$.
:::
<2>2. The standard generator of $\pi_1(S^1, 1)$ is the path homotopy class of $\gamma(s) = e(s)$.
The induced homomorphism $h_*: \pi_1(S^1, 1) \to \pi_1(S^1, h(1))$ maps $[\gamma]$ to $[h \circ \gamma] = [g]$.
::: {.proof}
functoriality of the fundamental group.
:::
<2>3. Under the canonical isomorphism $\pi_1(S^1) \cong \mathbb{Z}$ that identifies a loop's homotopy class with the difference of the endpoints of its lift in $\mathbb{R}$:
The loop $g = h \circ \gamma$ lifts to $\tilde{g}$, so the degree of $h$ is:
\[
\deg(h) = \tilde{g}(1) - \tilde{g}(0).
\]
::: {.proof}
definition of the degree of a self-map of $S^1$ via lifting.
:::

<1>3. Conclusion:
Both definitions coincide with $\tilde{g}(1) - \tilde{g}(0)$, so $n(f, a) = \deg(h)$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
