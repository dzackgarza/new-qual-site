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
---

::: {.problem}
Prove that TFAE for a Möbius transformation $T$ given by $T(z) = {az + b \over cz + d}$:

a. $T$ maps $\RR\union \theset{\infty}$ to itself.
b. It is possible to choose $a,b,c,d$ to be real numbers.
c. $\bar{T(z)} = T(\bar z)$ for every $z\in \CP^1$.
d. There exist $\alpha\in \RR, \beta \in \CC\setminus \RR$ such that $T(\alpha) = \alpha$ and $T(\bar \beta) = \bar{T(\beta)}$.
:::

::: {.solution}
::: pf

::: {.pf-step #tfae-abc}
(a) $\Leftrightarrow$ (b) $\Leftrightarrow$ (c).

::: pf-proof

::: pf-step
(a) $\Rightarrow$ (b): $T$ maps $\RR \cup \{\infty\}$ to itself, so it sends three real points to three real points; a Möbius map is determined by three values, and a map sending three real points to three real points has real coefficients (up to a common real scalar).

::: pf-proof
the cross-ratio of real points is real.
:::

:::

::: {.pf-step #b-implies-c}
(b) $\Rightarrow$ (c): if $a,b,c,d \in \RR$, then $\overline{T(z)} = \frac{\bar a \bar z + \bar b}{\bar c \bar z + \bar d} = \frac{a\bar z + b}{c\bar z + d} = T(\bar z)$.

::: pf-proof
conjugation commutes with real coefficients.
:::

:::

::: {.pf-step #c-implies-a}
(c) $\Rightarrow$ (a): if $z \in \RR$, then $\bar z = z$, so $\overline{T(z)} = T(\bar z) = T(z)$, hence $T(z) \in \RR$; thus $T$ maps $\RR$ to $\RR$ and $\RR \cup \{\infty\}$ to itself.

::: pf-proof
Step [](#b-implies-c){.pf-ref} applied to real $z$.
:::

:::

:::

:::

::: {.pf-step #d-implies-a}
(d) $\Rightarrow$ (a).

::: pf-proof

::: pf-step
$T$ fixes $\alpha \in \RR$ and satisfies $T(\bar\beta) = \overline{T(\beta)}$ for $\beta \notin \RR$.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #agrees-at-three-points}
The map $z \mapsto \overline{T(\bar z)}$ is a Möbius map agreeing with $T$ at the three distinct points $\alpha, \beta, \bar\beta$.

::: pf-proof
at $\alpha$ (real), $\overline{T(\bar\alpha)} = \overline{T(\alpha)} = \overline{\alpha} = \alpha = T(\alpha)$; at $\beta$, $\overline{T(\bar\beta)} = T(\beta)$ by hypothesis; at $\bar\beta$, $\overline{T(\beta)} = T(\bar\beta)$ by hypothesis.
:::

:::

::: pf-step
Hence $\overline{T(z)} = T(\bar z)$ for all $z$, so $T$ maps $\RR \cup \{\infty\}$ to itself (by step [](#c-implies-a){.pf-ref}).

::: pf-proof
Step [](#agrees-at-three-points){.pf-ref} and step [](#c-implies-a){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #a-not-implies-d}
(a) does NOT imply (d): the statement "TFAE" is false as written.

::: pf-proof

::: {.pf-step #T-satisfies-abc}
$T(z) = -\frac{1}{z}$ has real coefficients, so it satisfies (a), (b), and (c).

::: pf-proof
$a = 0$, $b = -1$, $c = 1$, $d = 0$ are real.
:::

:::

::: {.pf-step #T-no-real-fixed-point}
But $T$ has no real fixed point.

::: pf-proof
$T(z) = z$ means $-\frac{1}{z} = z$, i.e. $z^2 = -1$, so the fixed points are $z = \pm i \notin \RR$.
:::

:::

::: pf-step
Hence (d) fails for $T$, so (a) $\not\Rightarrow$ (d).

::: pf-proof
Steps [](#T-satisfies-abc){.pf-ref} and [](#T-no-real-fixed-point){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Step [](#tfae-abc){.pf-ref} proves (a) $\Leftrightarrow$ (b) $\Leftrightarrow$ (c); step [](#d-implies-a){.pf-ref} proves (d) $\Rightarrow$ (a); step [](#a-not-implies-d){.pf-ref} shows (a) $\not\Rightarrow$ (d), so the four statements are not all equivalent.
:::

:::

:::
