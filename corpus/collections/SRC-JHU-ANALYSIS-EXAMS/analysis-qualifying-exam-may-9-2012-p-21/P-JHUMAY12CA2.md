---
schema: qual/card@1
id: P-JHUMAY12CA2
kind: problem
title: Fixed point of holomorphic function on unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Suppose $f$ is holomorphic on the open unit disc $D(0,1)$ and continuous on $\overline{D(0,1)}$.
Assume $|f(\xi)| < 1$ for $\xi \in \partial D(0,1)$.
Show that there exists a unique point $a \in D(0,1)$ such that $f(a) = a$.

::: {.solution}
<1>1. Define $g(z) = f(z) - z$.
Proof: definition.

<1>2. On $\partial D(0,1)$, $|f(\xi)| < 1 = |\xi|$.
Proof: hypothesis, and $|\xi| = 1$ on the boundary.

<1>3. Apply Rouché's theorem to $g(z) = f(z) - z$ and $h(z) = -z$ on $D(0,1)$: on $\partial D(0,1)$, $|g(z) - h(z)| = |f(z)| < 1 = |z| = |h(z)|$.
Proof: $g - h = f$, and $|f(z)| < |h(z)| = |z| = 1$ on the boundary.

<1>4. Hence $g$ and $h$ have the same number of zeros in $D(0,1)$.
Proof: Rouché's theorem.

<1>5. $h(z) = -z$ has exactly one zero in $D(0,1)$ (at $z = 0$).
Proof: obvious.

<1>6. Hence $g(z) = f(z) - z$ has exactly one zero in $D(0,1)$, i.e. there is a unique $a \in D(0,1)$ with $f(a) = a$.
Proof: <1>4 and <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
