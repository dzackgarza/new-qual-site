---
schema: qual/card@1
id: E-HAT-4.1-3
kind: problem
title: "H-space multiplication gives group structure on $\\pi_n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

For an H-space $(X, x_0)$ with multiplication $\mu: X \times X \to X$, show that the group operation in $\pi_n(X, x_0)$ can also be defined by the rule $(f + g)(x) = \mu\bigl(f(x), g(x)\bigr)$.

::: {.solution}
Write the usual group operation on \(\pi_n(X,x_0)\) additively. Since
\[
\pi_n(X\times X,(x_0,x_0))\cong \pi_n(X,x_0)\times\pi_n(X,x_0),
\]
the multiplication \(\mu:X\times X\to X\) induces a homomorphism
\[
\mu_*:\pi_n(X)\times\pi_n(X)\longrightarrow\pi_n(X).
\]
Because \(x\mapsto\mu(x,x_0)\) and \(x\mapsto\mu(x_0,x)\) are homotopic to the identity,
\[
\mu_*(a,0)=a,
\qquad
\mu_*(0,b)=b.
\]
Hence, using that \(\mu_*\) is a homomorphism,
\[
\mu_*(a,b)
=\mu_*((a,0)+(0,b))
=\mu_*(a,0)+\mu_*(0,b)
=a+b.
\]
If \(a=[f]\) and \(b=[g]\), the class \(\mu_*(a,b)\) is represented by
\[
x\longmapsto\mu(f(x),g(x)).
\]
Therefore this pointwise H-space multiplication gives exactly the usual operation on \(\pi_n(X,x_0)\).
:::
