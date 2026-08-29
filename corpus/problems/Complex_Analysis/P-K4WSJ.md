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

::: problem
Prove that TFAE for a Möbius transformation $T$ given by $T(z) = {az + b \over cz + d}$:

a. $T$ maps $\RR\union \theset{\infty}$ to itself.
b. It is possible to choose $a,b,c,d$ to be real numbers.
c. $\bar{T(z)} = T(\bar z)$ for every $z\in \CP^1$.
d. There exist $\alpha\in \RR, \beta \in \CC\setminus \RR$ such that $T(\alpha) = \alpha$ and $T(\bar \beta) = \bar{T(\beta)}$.
:::

::: {.solution}
<1>1. (a) $\Leftrightarrow$ (b) $\Leftrightarrow$ (c).
<2>1. (a) $\Rightarrow$ (b): $T$ maps $\RR \cup \{\infty\}$ to itself, so it sends three real points to three real points; a Möbius map is determined by three values, and a map sending three real points to three real points has real coefficients (up to a common real scalar).
Proof: the cross-ratio of real points is real.
<2>2. (b) $\Rightarrow$ (c): if $a,b,c,d \in \RR$, then $\overline{T(z)} = \frac{\bar a \bar z + \bar b}{\bar c \bar z + \bar d} = \frac{a\bar z + b}{c\bar z + d} = T(\bar z)$.
Proof: conjugation commutes with real coefficients.
<2>3. (c) $\Rightarrow$ (a): if $z \in \RR$, then $\bar z = z$, so $\overline{T(z)} = T(\bar z) = T(z)$, hence $T(z) \in \RR$; thus $T$ maps $\RR$ to $\RR$ and $\RR \cup \{\infty\}$ to itself.
Proof: <2>2 applied to real $z$.

<1>2. (d) $\Rightarrow$ (a).
<2>1. $T$ fixes $\alpha \in \RR$ and satisfies $T(\bar\beta) = \overline{T(\beta)}$ for $\beta \notin \RR$.
Proof: hypothesis.
<2>2. The map $z \mapsto \overline{T(\bar z)}$ is a Möbius map agreeing with $T$ at the three distinct points $\alpha, \beta, \bar\beta$.
Proof: at $\alpha$ (real), $\overline{T(\bar\alpha)} = \overline{T(\alpha)} = \overline{\alpha} = \alpha = T(\alpha)$; at $\beta$, $\overline{T(\bar\beta)} = T(\beta)$ by hypothesis; at $\bar\beta$, $\overline{T(\beta)} = T(\bar\beta)$ by hypothesis.
<2>3. Hence $\overline{T(z)} = T(\bar z)$ for all $z$, so $T$ maps $\RR \cup \{\infty\}$ to itself (by <1>2.3).
Proof: <2>2 and <1>2.3.

<1>3. (a) does NOT imply (d): the statement "TFAE" is false as written.
<2>1. $T(z) = -\frac{1}{z}$ has real coefficients, so it satisfies (a), (b), and (c).
Proof: $a = 0$, $b = -1$, $c = 1$, $d = 0$ are real.
<2>2. But $T$ has no real fixed point.
Proof: $T(z) = z$ means $-\frac{1}{z} = z$, i.e. $z^2 = -1$, so the fixed points are $z = \pm i \notin \RR$.
<2>3. Hence (d) fails for $T$, so (a) $\not\Rightarrow$ (d).
Proof: <2>1 and <2>2.

<1>4. Q.E.D.
Proof: <1>1 proves (a) $\Leftrightarrow$ (b) $\Leftrightarrow$ (c); <1>2 proves (d) $\Rightarrow$ (a); <1>3 shows (a) $\not\Rightarrow$ (d), so the four statements are not all equivalent.
:::
