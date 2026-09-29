---
schema: qual/card@1
id: P-APAS24I
kind: problem
title: Finite-dimensionality of $\mathbb{C}[x,y]/I$ for a one-point variety
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $I\subseteq\mathbb{C}[x,y]$ be an ideal such that $\mathrm{V}(I)=\{(1,3)\}$.
Prove that $\mathbb{C}[x,y]/I$ is a finite-dimensional vector space.
Is this true if $\mathbb{C}[x,y]$ is replaced by $\mathbb{R}[x,y]$?
:::

::: {.solution}
**Goal.** For $I \subseteq \CC[x,y]$ with $V(I) = \theset{(1,3)}$, show $\CC[x,y]/I$ is finite-dimensional, and decide the $\RR[x,y]$ analogue.

::: pf

::: pf-step

$V(I) = \theset{(1,3)}$ means the radical $\sqrt I$ is the maximal ideal $\mathfrak m = (x-1, y-3)$.

::: pf-proof

by the Nullstellensatz, $V(I) = V(\sqrt I)$, and the only maximal ideal vanishing at $(1,3)$ is $(x-1, y-3)$; so $\sqrt I = (x-1, y-3)$.

:::

:::

::: pf-step

Some power of $\mathfrak m$ lies in $I$.

::: pf-proof

since $\sqrt I = \mathfrak m$ and $\mathfrak m$ is finitely generated, there is $N$ with $\mathfrak m^N \subseteq I$ (the radical of a finitely generated ideal is nilpotent mod $I$).

:::

:::

::: pf-step

$\CC[x,y]/\mathfrak m^N$ is finite-dimensional.

::: pf-proof

$\mathfrak m^N$ contains all monomials $(x-1)^a (y-3)^b$ with $a + b \ge N$, so the quotient is spanned by the finitely many monomials with $a + b < N$.

:::

:::

::: {.pf-step #s4}

$\CC[x,y]/I$ is finite-dimensional.

::: pf-proof

$I \supseteq \mathfrak m^N$ gives a surjection $\CC[x,y]/\mathfrak m^N \surjects \CC[x,y]/I$, and a quotient of a finite-dimensional space is finite-dimensional.

:::

:::

::: {.pf-step #s5}

The $\RR[x,y]$ analogue fails.

::: pf-proof

::: pf-step

Over $\RR$, $V(I) = \theset{(1,3)}$ does not force $\sqrt I = (x-1, y-3)$.

::: pf-proof

the real Nullstellensatz only gives $\sqrt I = I(V(I))$, the ideal of all polynomials vanishing at $(1,3)$; but over $\RR$ this ideal is still $(x-1, y-3)$ — however, the failure is different: consider $I = ((x-1)^2 + (y-3)^2)$.

:::

:::

::: pf-step

For $I = ((x-1)^2 + (y-3)^2)$, one has $V(I) = \theset{(1,3)}$ but $\RR[x,y]/I$ is infinite-dimensional.

::: pf-proof

$(x-1)^2 + (y-3)^2$ is irreducible over $\RR$ (a sum of squares with no real zero except the point), so $I$ is prime and $\RR[x,y]/I$ is an integral domain of Krull dimension $1$, hence infinite-dimensional as an $\RR$-vector space.

:::

:::

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} answers the first question; step [](#s5){.pf-ref} answers the second (false over $\RR$).

:::

:::

:::
