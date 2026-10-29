---
schema: qual/card@1
id: P-K4WSJ
kind: problem
title: Characterizations of Möbius transformations preserving $\RR\cup\{\infty\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Schwarz Reflection
  - Biholomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked to prove (a)-(d) equivalent, which is false since T(z) = -1/z satisfies (a)-(c) and has no real fixed point; the statement now asks to prove (a)-(c) equivalent, (d) implies them, and the converse need not hold.'
---

::: {.problem}
Consider the following conditions on a Möbius transformation $T$ given by $T(z) = {az + b \over cz + d}$:

(a) $T$ maps $\RR\union \theset{\infty}$ to itself.

(b) It is possible to choose $a,b,c,d$ to be real numbers.

(c) $\bar{T(z)} = T(\bar z)$ for every $z\in \CP^1$.

(d) There exist $\alpha\in \RR, \beta \in \CC\setminus \RR$ such that $T(\alpha) = \alpha$ and $T(\bar \beta) = \bar{T(\beta)}$.

Prove that (a), (b), and (c) are equivalent. Prove that (d) implies these conditions, and show that the converse need not hold.
:::

::: {.solution}
::: pf

::: pf-step
(a) $\Rightarrow$ (b).

::: pf-proof
Choose distinct $x_1, x_2, x_3 \in \RR \cup \theset{\infty}$ and put $y_i = T(x_i)$, which lie in $\RR \cup \theset{\infty}$ by (a).
The Möbius maps $S$ and $S'$ sending $x_1, x_2, x_3$, respectively $y_1, y_2, y_3$, to $0, 1, \infty$ are cross-ratio maps with real coefficients.
Since a Möbius map is determined by three values, $T = (S')^{-1} \circ S$, a composition of maps with real coefficients.
:::

:::

::: pf-step
(b) $\Rightarrow$ (c).

::: pf-proof
If $a,b,c,d \in \RR$, then $\overline{T(z)} = \frac{\bar a \bar z + \bar b}{\bar c \bar z + \bar d} = \frac{a\bar z + b}{c\bar z + d} = T(\bar z)$.
:::

:::

::: {.pf-step #c-implies-a}
(c) $\Rightarrow$ (a).

::: pf-proof
If $z \in \RR \cup \theset{\infty}$, then $\bar z = z$, so (c) gives $\overline{T(z)} = T(z)$, that is, $T(z) \in \RR \cup \theset{\infty}$.
:::

:::

::: pf-step
(d) $\Rightarrow$ (c), and hence (a) and (b).

::: pf-proof
The map $S(z) = \overline{T(\bar z)}$ is a Möbius map.
It agrees with $T$ at the three distinct points $\alpha, \beta, \bar\beta$: $S(\alpha) = \overline{T(\alpha)} = \alpha = T(\alpha)$, $S(\beta) = \overline{T(\bar\beta)} = T(\beta)$, and $S(\bar\beta) = \overline{T(\beta)} = T(\bar\beta)$ by (d).
So $S = T$, which is (c).
:::

:::

::: pf-step
(a), (b) and (c) do not imply (d).

::: pf-proof
$T(z) = -\frac{1}{z}$ has real coefficients, so it satisfies (b), and hence (a) and (c).
Its fixed points satisfy $z^2 = -1$, so $T$ has no real fixed point and (d) fails.
:::

:::

:::
:::
