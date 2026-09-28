---
schema: qual/card@1
id: P-5CM5W
kind: problem
title: Translation invariance of Lebesgue measure and of the integral
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove that if \( E \subseteq \RR^n \) is a Lebesgue measurable set, then for any \( h \in \RR \) the set
\[
E+h \da \ts{x + h \st x\in E }
\]
is also Lebesgue measurable and satisfies \( m(E + h) = m(E) \).

Prove that if $f$ is a non-negative measurable function on $\RR^n$ and $h\in \RR^n$ then the function
\[
\tau_h d(x) \da f(x-h)
\]
is a non-negative measurable function and
\[
\int f(x) \dx = \int f(x-h) \dx
.\]
:::

::: {.solution}
Take $h \in \RR^n$, and write $\tau_h f(x) \coloneqq f(x-h)$.

<1>1. For measurable $E$, $E + h$ is measurable and $m(E + h) = m(E)$.

<2>1. $m^*(A + h) = m^*(A)$ for every $A \subseteq \RR^n$.

::: {.proof}
Translation by $h$ is a bijection between countable covers of $A$ by closed boxes and countable covers of $A + h$ by closed boxes, and it preserves the volume of each box. Taking infima gives equality.
:::

<2>2. $E + h$ is measurable.

::: {.proof}
Write $E = G \setminus Z$ with $G$ a $G_\delta$ set and $Z$ null. Translation is a homeomorphism of $\RR^n$, so $G + h$ is a $G_\delta$ set, and $m^*(Z + h) = 0$ by step <2>1. So $E + h = (G + h) \setminus (Z + h)$ is measurable.
:::

<2>3. Q.E.D.

::: {.proof}
Step <2>2 gives measurability, and on measurable sets $m = m^*$, so step <2>1 gives $m(E + h) = m(E)$.
:::

<1>2. For measurable $f \geq 0$, $\tau_h f$ is measurable and $\int \tau_h f = \int f$.

<2>1. $\tau_h f$ is measurable.

::: {.proof}
For every $a \in \RR$, $\theset{\tau_h f > a} = \theset{f > a} + h$, which is measurable by step <1>1.
:::

<2>2. For measurable $E$, $\int \tau_h \chi_E = m(E)$.

::: {.proof}
$\tau_h\chi_E(x) = \chi_E(x - h) = \chi_{E + h}(x)$, and $m(E + h) = m(E)$ by step <1>1.
:::

<2>3. Q.E.D.

::: {.proof}
By linearity, step <2>2 gives $\int \tau_h s = \int s$ for nonnegative simple $s$. Choose simple $0 \leq s_k \nearrow f$. Then $\tau_h s_k \nearrow \tau_h f$, and the monotone convergence theorem gives $\int \tau_h f = \lim_k \int \tau_h s_k = \lim_k \int s_k = \int f$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 are the two parts.
:::
:::
