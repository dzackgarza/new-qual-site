---
schema: qual/card@1
id: P-5CM5W
kind: problem
title: "Prove that if \\( E \\subseteq \\RR^n \\) is a Lebesgue measurable set, then for any \\( h \\in \\RR \\)\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
relations: []
review: draft
---

::: problem
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
> **AI-Generated Solution**

<1>1. For measurable $E$ and $h \in \RR^n$: $E + h$ is measurable and $m(E + h) = m(E)$.
    <2>1. Translation preserves outer measure: $m^*(A + h) = m^*(A)$ for every set $A$.
        Proof: the family of boxes covering $A$ is in bijection (by translation) with the family covering $A + h$, with identical total volumes; taking infima gives equality.
    <2>2. It suffices to prove measurability for Borel sets, then transfer to measurable sets.
        Proof: every Lebesgue measurable $E$ is $E = B \cup N$ with $B$ Borel and $N$ null; then $E + h = (B + h) \cup (N + h)$, where $B + h$ is Borel (translation is a homeomorphism, so it maps open sets to open sets and preserves the Borel $\sigma$-algebra), and $N + h$ is null by <2>1; a Borel set plus a null set is measurable.
    <2>3. $m(E + h) = m(E)$ for measurable $E$.
        Proof: from <2>1, $m^*(E + h) = m^*(E)$; for measurable sets outer measure equals measure.
    <2>4. Q.E.D.
        Proof: <2>2 gives measurability and <2>3 gives the measure identity.

<1>2. For non-negative measurable $f$ and $h \in \RR^n$: $\tau_h f(x) := f(x - h)$ is non-negative measurable and $\int f(x)\,dx = \int f(x - h)\,dx$.
    <2>1. $\tau_h f$ is measurable.
        Proof: $\tau_h f = f \circ T$ where $T(x) = x - h$ is continuous, and the composition of a measurable function with a continuous map (Borel measurable) is measurable.
    <2>2. The claim holds for indicators: $\int \tau_h \chi_E = m(E - h) = m(E)$.
        Proof: $\tau_h\chi_E(x) = \chi_E(x - h) = 1 \iff x \in E + h$, so $\tau_h\chi_E = \chi_{E + h}$, and $m(E + h) = m(E)$ by <1>1.
    <2>3. The claim holds for non-negative simple functions.
        Proof: linearity and <2>2.
    <2>4. The claim holds for all non-negative measurable $f$.
        Proof: choose simple $s_k \nearrow f$; then $\tau_h s_k \nearrow \tau_h f$, and monotone convergence plus <2>3 give $\int \tau_h f = \lim_k \int \tau_h s_k = \lim_k \int s_k = \int f$.
    <2>5. Q.E.D.
        Proof: <2>1 and <2>4.
:::
