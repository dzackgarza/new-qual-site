---
schema: qual/card@1
id: E-UWGCC
kind: problem
title: The fundamental group of the torus via the circle covering
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Generalize the proof of Theorem 54.5 to show that the fundamental group of the torus is isomorphic to the group $\mathbb{Z} \times \mathbb{Z}$.
:::

::: {.solution}
Write the torus as
\[
T=S^1\times S^1.
\]
Consider the covering map
\[
p:\mathbb R^2\longrightarrow T,
\qquad
p(s,t)=\bigl(e^{2\pi i s},e^{2\pi i t}\bigr).
\]
It is the product of the standard coverings \(\mathbb R\to S^1\), hence is a covering map. The total space \(\mathbb R^2\) is simply connected.

Fix the basepoint \((1,1)\in T\) and its lift \((0,0)\). For a loop \(f\) in \(T\) based at \((1,1)\), let \(\widetilde f\) be its unique lift beginning at \((0,0)\). Its endpoint lies in
\[
p^{-1}(1,1)=\mathbb Z^2.
\]
Define
\[
\Phi:\pi_1(T,(1,1))\to\mathbb Z^2,
\qquad
\Phi([f])=\widetilde f(1).
\]
Exactly as in the proof for \(S^1\), the homotopy-lifting theorem shows that \(\Phi\) is well defined, and lifting concatenations shows
\[
\Phi([f]*[g])=\Phi([f])+\Phi([g]).
\]
It is surjective: for \((m,n)\in\mathbb Z^2\), the path
\[
\widetilde f(t)=(mt,nt)
\]
projects to a loop whose image under \(\Phi\) is \((m,n)\).

It is injective: if \(\Phi([f])=(0,0)\), then \(\widetilde f\) is a loop in the simply connected space \(\mathbb R^2\), so it is nullhomotopic there. Projecting the nullhomotopy by \(p\) shows that \(f\) is nullhomotopic in \(T\).

Therefore
\[
\boxed{\pi_1(S^1\times S^1,(1,1))\cong\mathbb Z\times\mathbb Z}.
\]
:::
