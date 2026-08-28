---
schema: qual/card@1
id: P-CAFA17D
kind: problem
title: "Schwarz lemma on the upper half-plane: maximum of |f(2i)|"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $\mathfrak{h}^+ = \{z : \operatorname{Im} z > 0\}$ denote the upper-half plane.
Let $\mathcal{F}$ be the family of holomorphic functions $f: \mathfrak{h}^+ \to \mathbb{C}$ such that $f(i) = 0$ and $|f(z)| < 1$ for all $z \in \mathfrak{h}^+$.
Find the maximum value of $|f(2i)|$ for $f \in \mathcal{F}$.
:::

::: {.solution}
**Goal.** Find $\max_{f \in \mathcal F} |f(2i)|$.

<1>1. Conjugate to the unit disk via the Cayley transform $\phi(z) = \frac{z - i}{z + i}$, which maps $\mathfrak h^+$ to $\DD$ and $i \mapsto 0$.
Proof: the Cayley transform maps the upper half-plane to the unit disk, sending $i$ to $0$.

<1>2. $\phi(2i) = \frac{2i - i}{2i + i} = \frac{i}{3i} = \frac13$.
Proof: compute.

<1>3. For $f \in \mathcal F$, define $g = f \circ \phi^{-1}: \DD \to \DD$ with $g(0) = f(i) = 0$.
Proof: $g$ is a holomorphic self-map of the disk with $g(0) = 0$.

<1>4. By the Schwarz lemma, $|g(w)| \le |w|$ for all $w \in \DD$.
Proof: Schwarz lemma applied to $g$.

<1>5. Hence $|f(2i)| = |g(\phi(2i))| = |g(1/3)| \le 1/3$.
Proof: <1>2 and <1>4.

<1>6. The bound is attained by $g(w) = w$ (i.e. $f = \phi$), giving $|f(2i)| = 1/3$.
Proof: $g(w) = w$ satisfies $g(0) = 0$ and $|g(w)| < 1$, and $|g(1/3)| = 1/3$.

<1>7. Q.E.D.
Proof: the maximum value is $1/3$.
:::
