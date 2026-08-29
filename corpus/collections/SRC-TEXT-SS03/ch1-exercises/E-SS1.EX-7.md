---
schema: qual/card@1
id: E-SS1.EX-7
kind: exercise
title: "The family of mappings introduced here plays an important role in complex analys"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
7. The family of mappings introduced here plays an important role in complex analysis.
   These mappings, sometimes called Blaschke factors, will reappear in various applications in later chapters.

(a) Let $z , w$ be two complex numbers such that $\overline { { z } } w \ne 1$ . Prove that

$$
\left| \frac {w - z}{1 - \overline {{w}} z} \right| <   1 \quad \text { if } | z | <   1 \text { and } | w | <   1,
$$

and also that

$$
\left| \frac {w - z}{1 - \overline {{w}} z} \right| = 1 \quad \text { if } | z | = 1 \text { or } | w | = 1.
$$

[Hint: Why can one assume that z is real?
It then sufices to prove that

$$
(r - w) (r - \overline {{w}}) \leq (1 - r w) (1 - r \overline {{w}})
$$

with equality for appropriate r and <sub>|</sub>w<sub>|</sub>.]

(b) Prove that for a fixed w in the unit disc D, the mapping

$$
F: z \mapsto \frac {w - z}{1 - \overline {{w}} z}
$$

satisfies the following conditions:

4. Exercises

(i) F maps the unit disc to itself (that is, $F : \mathbb { D } \to \mathbb { D } )$ , and is holomorphic.

(ii) F interchanges 0 and $w ,$ namely $F ( 0 ) = w$ and $F ( w ) = 0$

(iii) $| F ( z ) | = 1 { \mathrm { ~ i f ~ } } | z | = 1 .$

(iv) $F : \mathbb { D }  \mathbb { D }$ is bijective.
[Hint: Calculate $F \circ F . ]$
:::

::: {.solution}
**(a).**

<1>1. We may assume $z = r$ is real (rotate so that $z$ is real, since the expression is invariant under a simultaneous rotation).
Proof: the hint; a rotation $z \mapsto e^{i\theta}z$, $w \mapsto e^{i\theta}w$ preserves the modulus of $\frac{w - z}{1 - \bar w z}$.

<1>2. It suffices to show $(r - w)(r - \bar w) \le (1 - rw)(1 - r\bar w)$ for $|w| < 1$, $0 \le r < 1$.
Proof: squaring both sides of $|w - r| \le |1 - \bar w r|$ (both sides are real and nonnegative).

<1>3. Expanding: $r^2 - r(w + \bar w) + |w|^2 \le 1 - r(w + \bar w) + r^2|w|^2$.
Proof: <1>2, expanding both sides.

<1>4. This is equivalent to $r^2 + |w|^2 \le 1 + r^2|w|^2$, i.e. $(1 - r^2)(1 - |w|^2) \ge 0$.
Proof: <1>3, rearranging.

<1>5. This holds since $r < 1$ and $|w| < 1$.
Proof: <1>4.

<1>6. Hence $\left| \frac{w - z}{1 - \bar w z} \right| < 1$ when $|z| < 1$ and $|w| < 1$.
Proof: <1>2–<1>5.

<1>7. If $|z| = 1$ or $|w| = 1$, then $(1 - r^2)(1 - |w|^2) = 0$, so equality holds: $\left| \frac{w - z}{1 - \bar w z} \right| = 1$.
Proof: <1>4 with $r = 1$ or $|w| = 1$.

**(b).**

<1>1. $F(z) = \frac{w - z}{1 - \bar w z}$ is holomorphic on $\mathbb{D}$ (the denominator is nonzero since $|\bar w z| < 1$ for $|z| < 1$).
Proof: $F$ is a rational function with no pole in $\mathbb{D}$.

<1>2. $F$ maps $\mathbb{D}$ to itself.
Proof: part (a) ($|F(z)| < 1$ for $|z| < 1$).

<1>3. $F(0) = w$ and $F(w) = 0$.
Proof: direct substitution.

<1>4. $|F(z)| = 1$ if $|z| = 1$.
Proof: part (a).

<1>5. $F \circ F = \operatorname{id}$.
Proof: compute $F(F(z)) = \frac{w - \frac{w - z}{1 - \bar w z}}{1 - \bar w \frac{w - z}{1 - \bar w z}} = \frac{w(1 - \bar w z) - (w - z)}{(1 - \bar w z) - \bar w(w - z)} = \frac{z(1 - |w|^2)}{1 - |w|^2} = z$.

<1>6. Hence $F$ is bijective (it is its own inverse).
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>6, <1>7 (a) and <1>2–<1>6 (b).
:::
