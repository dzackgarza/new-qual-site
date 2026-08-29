---
schema: qual/card@1
id: E-P5AAV
kind: exercise
title: The quotient R over Z as a familiar topological group
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

The integers $\mathbb{Z}$ are a normal subgroup of $(\mathbb{R}, +)$.
The quotient $\mathbb{R}/\mathbb{Z}$ is a familiar topological group; what is it?
:::

::: {.solution}
<1>1. Define $\varphi : \mathbb{R} \to S^1$ by $\varphi(t) = e^{2\pi i t}$.
Proof: definition.

<1>2. $\varphi$ is a continuous surjective group homomorphism from $(\mathbb{R}, +)$ to $(S^1, \cdot)$.
Proof: $\varphi(s + t) = e^{2\pi i(s+t)} = e^{2\pi i s} e^{2\pi i t} = \varphi(s)\varphi(t)$, and it is surjective (every point of $S^1$ is $e^{2\pi i t}$ for some $t$).

<1>3. $\ker \varphi = \mathbb{Z}$.
Proof: $e^{2\pi i t} = 1$ iff $t \in \mathbb{Z}$.

<1>4. Hence by the first isomorphism theorem, $\mathbb{R}/\mathbb{Z} \cong S^1$.
Proof: <1>2 and <1>3.

<1>5. This is an isomorphism of topological groups (the quotient topology on $\mathbb{R}/\mathbb{Z}$ agrees with the subspace topology on $S^1$).
Proof: $\varphi$ is a quotient map (it is open and continuous), so the induced bijection $\mathbb{R}/\mathbb{Z} \to S^1$ is a homeomorphism.

<1>6. Q.E.D.
Proof: <1>4 and <1>5.
:::
