---
schema: qual/card@1
id: E-HAT-4.3-10
kind: problem
title: "Action of $\\pi_1(E)$ on $\\pi_n(F)$ for fibrations"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Given a fibration $F \to E \to B$, use the homotopy lifting property to define an action of $\pi_1(E)$ on $\pi_n(F)$, a homomorphism $\pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$, such that the composition $\pi_1(F) \to \pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$ is the usual action of $\pi_1(F)$ on $\pi_n(F)$.
Deduce that if $\pi_1(E) = 0$, then the action of $\pi_1(F)$ on $\pi_n(F)$ is trivial.
:::

::: {.solution}
Fix a basepoint \(e_0\in F=p^{-1}(b_0)\). Let
\[
[\beta]\in\pi_1(E,e_0),
\qquad
[\alpha]\in\pi_n(F,e_0).
\]
Use the relative homotopy lifting property for the cofibration
\[
S^n\times\{0\}\cup\{*\}\times I
\subset S^n\times I.
\]
On this subspace define a map to \(E\) by \(\alpha\) on \(S^n\times\{0\}\) and by \(\beta\) on \(\{*\}\times I\). Its projection extends over \(S^n\times I\) by
\[
(x,t)\longmapsto p\beta(t).
\]
Lift this homotopy relative to the displayed subspace. At \(t=1\) the resulting map
\[
\alpha_1:S^n\to E
\]
lands in \(F\), since \(p\beta(1)=b_0\), and is based because the basepoint track is \(\beta\). Define
\[
[\beta]\cdot[\alpha]=[\alpha_1]\in\pi_n(F,e_0).
\]

Homotopies of \(\alpha\) or \(\beta\) give homotopies of \(\alpha_1\), so this is well-defined. Concatenating loops concatenates the transport homotopies, hence
\[
(\beta\gamma)\cdot\alpha
=\beta\cdot(\gamma\cdot\alpha),
\]
and reversing \(\beta\) gives the inverse automorphism. Thus
\[
\pi_1(E,e_0)\to\operatorname{Aut}(\pi_n(F,e_0))
\]
is a homomorphism.

If \(\beta\) is a loop in \(F\), its projection is constant, and the construction is exactly the usual basepoint-change action of \(\pi_1(F)\) on \(\pi_n(F)\). Therefore the composite
\[
\pi_1(F)\to\pi_1(E)\to\operatorname{Aut}(\pi_n(F))
\]
is the usual action. In particular, if \(\pi_1(E)=0\), this action is trivial.
:::
