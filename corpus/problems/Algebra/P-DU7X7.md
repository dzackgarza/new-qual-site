---
schema: qual/card@1
id: P-DU7X7
kind: problem
title: Hilbert's theorem 90
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
What's Hilbert's theorem 90?
:::

::: {.solution}
<1>1. Let $L/K$ be a finite Galois extension with Galois group $G = \operatorname{Gal}(L/K)$.
Proof: setup.

<1>2. **Hilbert's Theorem 90 (multiplicative form).** If $L/K$ is cyclic with generator $\sigma$, then every element $a \in L$ with norm $N_{L/K}(a) = 1$ is of the form $a = b/\sigma(b)$ for some $b \in L^\times$.
Proof: statement of the theorem.

<1>3. Equivalently, the first Galois cohomology group $H^1(G, L^\times)$ is trivial.
Proof: the theorem asserts that the kernel of the norm map equals the image of $1 - \sigma$, which is exactly $H^1(G, L^\times) = 0$.

<1>4. **Additive form.** $H^1(G, L) = 0$, i.e. if $\operatorname{tr}_{L/K}(a) = 0$ then $a = b - \sigma(b)$ for some $b \in L$.
Proof: the additive analogue (also called Hilbert 90).

<1>5. Q.E.D.
Proof: <1>2 and <1>4.
:::
