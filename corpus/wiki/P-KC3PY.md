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
---

::: problem
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
> **AI-Generated Solution**

<1>1. (a) $E + h$ is measurable with $m(E + h) = m(E)$.
    <2>1. For open $U$: $U + h$ is open and $m(U + h) = m(U)$.
        Proof: translation is a homeomorphism; Lebesgue measure of an open set is the supremum of measures of contained cubes, and cubes translate with equal measure (the measure of a cube is invariant under translation).
    <2>2. For $G_\delta$ sets and null sets the identity passes; $E$ is measurable iff $E = B \cup N$ with $B$ Borel (or $G_\delta$) and $N$ null; hence $E + h = (B + h) \cup (N + h)$ is measurable with $m(E+h) = m(B+h) + 0 = m(B) = m(E)$.
        Proof: regularity of Lebesgue measure (measurable = Borel + null); translation preserves Borel sets (homeomorphism) and null sets ($m(N+h) = m(N) = 0$ by <2>1 applied to the open covers approximating $N$).
    <2>3. Q.E.D.
        Proof: <2>1, <2>2.

<1>2. (b) $\tau_h f(x) = f(x - h)$ is measurable and $\int f = \int f(x-h)\,dx$.
    <2>1. For $f = \chi_E$: $\tau_h \chi_E = \chi_{E + h}$, measurable with integral $m(E+h) = m(E)$.
        Proof: <1>1.
    <2>2. For simple $f = \sum a_i\chi_{E_i}$: $\tau_h f = \sum a_i\chi_{E_i + h}$, measurable, and $\int \tau_h f = \sum a_i m(E_i + h) = \sum a_i m(E_i) = \int f$.
        Proof: <2>1 and linearity.
    <2>3. For $f \ge 0$ measurable: $\int \tau_h f = \int f$.
        Proof: monotone convergence applied to simple approximations $s_k \uparrow f$ (then $\tau_h s_k \uparrow \tau_h f$), using <2>2.
    <2>4. For signed $f = f^+ - f^-$: $\int \tau_h f = \int \tau_h f^+ - \int \tau_h f^- = \int f^+ - \int f^- = \int f$.
        Proof: <2>3 on each part; $\tau_h f^\pm = (\tau_h f)^\pm$.

<1>3. Q.E.D.
    Proof: <1>1 and <1>2 establish (a) and (b). (In the card, the translation is written $\tau_h d(x) = f(x-h)$ — the standard $\tau_h f$.)
:::
