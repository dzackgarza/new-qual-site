---
schema: qual/card@1
id: P-KC3PY
kind: problem
title: Translation invariance of Lebesgue measure and integrals
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
a.
Prove that if \( E \subseteq \RR^n \) is a Lebesgue measurable set, then for any \( h \in \RR \) the set
\[
E+h \da \ts{x + h \st x\in E }
\]
is also Lebesgue measurable and satisfies \( m(E + h) = m(E) \).

b.
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
Take $h \in \RR^n$ and write $\tau_h f(x) \coloneqq f(x-h)$.

::: pf

::: {.pf-step #s1}

For measurable $E$, $E + h$ is measurable and $m(E + h) = m(E)$.

::: pf-proof

Translation by $h$ is a bijection between countable covers of a set $A$ by closed boxes and countable covers of $A + h$, preserving each volume, so $m^*(A + h) = m^*(A)$ for every $A$. Write $E = G \setminus Z$ with $G$ a $G_\delta$ set and $Z$ null. Translation is a homeomorphism, so $G + h$ is $G_\delta$, and $m^*(Z + h) = 0$. So $E + h = (G + h) \setminus (Z + h)$ is measurable, and $m(E + h) = m^*(E + h) = m^*(E) = m(E)$.

:::

:::

::: pf-step

For measurable $f \ge 0$, $\tau_h f$ is measurable and $\int \tau_h f = \int f$.

::: pf-proof

For $a \in \RR$, $\theset{\tau_h f > a} = \theset{f > a} + h$, which is measurable by step [](#s1){.pf-ref}. For $f = \chi_E$, $\tau_h\chi_E = \chi_{E+h}$ has integral $m(E + h) = m(E)$ by step [](#s1){.pf-ref}, and linearity extends this to nonnegative simple functions. For general $f$, choose simple $0 \le s_k \uparrow f$; then $\tau_h s_k \uparrow \tau_h f$, and the monotone convergence theorem gives $\int \tau_h f = \lim_k \int s_k = \int f$. See [[P-5CM5W]].

:::

:::

:::

:::
