---
schema: qual/card@1
id: P-OX7OF
kind: problem
title: Induced maps on $\pi_1(S^1)$ of $z\mapsto z^n$, antipodal, and $\sin$ maps
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source text in the problem block was a worked answer (opening 'Here we go:') rather than the question; the statement now poses the three computations that answer treats, and the answer's content is carried by the solution."
---

::: {.problem}
Regard $S^1$ as the unit circle in $\CC$, and identify $\pi_1(S^1)$ with $\ZZ$ at every base point.
Compute the homomorphism $f_*\colon \ZZ \to \ZZ$ induced on fundamental groups by each of the following maps $f\colon S^1 \to S^1$.

(a) $f(z) = z^n$, for a fixed integer $n$.

(b) The antipodal map $f(z) = -z$.

(c) $f(e^{it}) = e^{2\pi i \sin t}$.
:::

::: {.solution}
Let $\alpha(t) = e^{2\pi i t}$ for $t \in [0,1]$; its class $[\alpha]$ generates $\pi_1(S^1, 1) \cong \ZZ$, and a loop in $S^1$ represents the integer equal to its winding number.

::: pf

::: pf-step
(a) $f_*(a) = \boxed{na}$.

::: pf-proof
The loop $f \circ \alpha$ is $t \mapsto (e^{2\pi i t})^n = e^{2\pi i n t}$, whose winding number is $n$.
So $f_*$ sends the generator $1$ to $n$, and hence $a$ to $na$.
:::

:::

::: pf-step
(b) $f_*(a) = \boxed{a}$.

::: pf-proof
The maps $h_s(z) = e^{i(1-s)\pi} z$ for $s \in [0,1]$ form a homotopy from $f = h_0$ to $\id = h_1$.
Homotopic maps of $S^1$ have loops $f \circ \alpha$ and $\alpha$ with the same winding number, since the winding number of a loop is invariant under free homotopy of loops.
So $f \circ \alpha$ has winding number $1$, and $f_*$ is the identity of $\ZZ$.
:::

:::

::: pf-step
(c) $f_*(a) = \boxed{0}$ for all $a$.

::: pf-proof
Parametrize the generator as $t \mapsto e^{it}$ for $t \in [0, 2\pi]$.
Then $f \circ \alpha$ is $t \mapsto e^{2\pi i \sin t}$, which has the continuous argument $\theta(t) = 2\pi \sin t$.
Its winding number is $(\theta(2\pi) - \theta(0))/2\pi = \sin 2\pi - \sin 0 = 0$.
On the four quarter-intervals of $[0, 2\pi]$ the argument changes by $+2\pi, -2\pi, -2\pi, +2\pi$, which sum to $0$.
So $f \circ \alpha$ is null-homotopic and $f_*$ is the zero homomorphism.
:::

:::

:::

:::
