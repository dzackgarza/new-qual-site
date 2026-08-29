---
schema: qual/card@1
id: P-CASP11B
kind: problem
title: "Completeness of analytic functions with the sup norm on the boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a bounded region and $$\mathcal{F} = \{f \in C(\overline{G}, \mathbb{C}) : f \text{ is analytic in } G\},$$ and put $\|f\| = \sup_{z \in \partial G} |f(z)|$.
Show that $\mathcal{F}$ is a complete metric space with $d(f, g) = \|f - g\|$.
:::

::: {.solution}
<1>1. $\|\cdot\|$ is a norm on $\mathcal F$.
<2>1. $\|f\| \ge 0$ and $\|f\| = 0$ iff $f = 0$.
Proof: if $\|f\| = 0$, then $f = 0$ on $\partial G$; by the maximum modulus principle, $f = 0$ on all of $\overline G$.
<2>2. $\|cf\| = |c|\|f\|$ and $\|f + g\| \le \|f\| + \|g\|$.
Proof: the sup norm satisfies these.

<1>2. Let $\{f_n\}$ be a Cauchy sequence in $\mathcal F$.
Proof: take an arbitrary Cauchy sequence.

<1>3. $\{f_n\}$ converges uniformly on $\partial G$ to a continuous function $f_0$ on $\partial G$.
Proof: $\partial G$ is compact, and a Cauchy sequence in the sup norm converges uniformly.

<1>4. $f_0$ extends to a function $f \in \mathcal F$ (continuous on $\overline G$, analytic in $G$).
<2>1. $f_0$ is the boundary value of a function analytic in $G$.
Proof: the $f_n$ are analytic in $G$ and converge uniformly on $\partial G$; by the maximum modulus principle, they converge uniformly on all of $\overline G$, and the uniform limit of analytic functions is analytic in $G$.
<2>2. Hence $f \in \mathcal F$.
Proof: <2>1.

<1>5. $\|f_n - f\| \to 0$.
Proof: uniform convergence on $\overline G$ (hence on $\partial G$).

<1>6. Hence every Cauchy sequence converges, so $\mathcal F$ is complete.
Proof: <1>2–<1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
