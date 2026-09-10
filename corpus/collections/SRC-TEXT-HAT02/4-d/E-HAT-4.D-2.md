---
schema: qual/card@1
id: E-HAT-4.D-2
kind: problem
title: "Cohomology of $K(\\mathbb{Z}_p, 1)$ via Leray--Hirsch"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Apply the Leray–Hirsch theorem to the bundle $S^1 \to S^\infty/\mathbb{Z}_p \to \mathbb{CP}^\infty$ to compute $H^*(K(\mathbb{Z}_p, 1); \mathbb{Z}_p)$ from $H^*(\mathbb{CP}^\infty; \mathbb{Z}_p)$.

::: {.solution}
Consider
\[
S^1\longrightarrow S^\infty/\mathbb Z_p\xrightarrow{q}\mathbb{CP}^\infty.
\]
The inclusion of a fiber induces on fundamental groups the reduction map
\[
\mathbb Z=\pi_1(S^1)\longrightarrow\pi_1(S^\infty/\mathbb Z_p)=\mathbb Z_p.
\]
Therefore the generator
\[
a\in H^1(S^\infty/\mathbb Z_p;\mathbb Z_p)
\]
restricts to the generator of \(H^1(S^1;\mathbb Z_p)\). Leray--Hirsch gives
\[
H^*(K(\mathbb Z_p,1);\mathbb Z_p)
\cong H^*(\mathbb{CP}^\infty;\mathbb Z_p)\{1,a\}
\]
as a module. If \(b=q^*c\), where \(c\) generates \(H^2(\mathbb{CP}^\infty;\mathbb Z_p)\), then
\[
H^*(K(\mathbb Z_p,1);\mathbb Z_p)
\cong \mathbb Z_p[b]\{1,a\},
\qquad |a|=1,\ |b|=2.
\]
For odd \(p\), graded commutativity gives \(a^2=-a^2\), hence \(a^2=0\), so
\[
\boxed{H^*(K(\mathbb Z_p,1);\mathbb Z_p)
\cong \Lambda(a)\otimes\mathbb Z_p[b]\qquad(p\text{ odd}).}
\]
The Bockstein associated to \(0\to\mathbb Z_p\to\mathbb Z_{p^2}\to\mathbb Z_p\to0\) satisfies \(\beta(a)=b\). For \(p=2\), this Bockstein is \(Sq^1\) on degree-one classes, so \(b=a^2\). Hence
\[
\boxed{H^*(K(\mathbb Z_2,1);\mathbb Z_2)\cong\mathbb Z_2[a],\quad |a|=1.}
\]
:::
