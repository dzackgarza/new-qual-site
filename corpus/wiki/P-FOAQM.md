---
schema: qual/card@1
id: P-FOAQM
kind: problem
title: "Suppose $f, g: [0, 1] \\to \\RR$ where $f$ is Riemann integrable and for $x, y\\in [0, 1]$, $\\abs{g(x) - g(y)} \\leq \\abs{f(x) - f(y)}$ Prove that\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - riemann-integrability
  - integrals
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Suppose $f, g: [0, 1] \to \RR$ where $f$ is Riemann integrable and for $x, y\in [0, 1]$,
\[
\abs{g(x) - g(y)} \leq \abs{f(x) - f(y)}
.\]

Prove that $g$ is Riemann integrable.
:::


:::{.solution}
Write $U(f), L(f)$ for the upper and lower sums of $f$, so for $\Pi$ the collection of all partitions of $[0, 1]$,
\[
U(f) \da \inf_{P\in \Pi} U(f, P) && U(f, P) \da \sum_{k=1}^n \sup_{x\in I_k}f(x) \cdot \mu(I_k) \\
L(f) \da \sup_{P\in \Pi} L(f, P) && L(f, P) \da \sum_{k=1}^n \inf_{x\in I_k} f(x) \cdot \mu(I_k)
.\]

Note that integrability of $f$ is equivalent to
\[
\forall \eps \exists P \text{ such that }
U(f, P) - L(f, P) < \eps \\
\iff 
\sum_{k=1}^n \qty{ \sup_{x\in I_k} f(x) - \inf_{x\in I_k} f(x)} \mu(I_k) < \eps
.\]


:::



