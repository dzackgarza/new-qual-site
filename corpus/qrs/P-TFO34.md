---
schema: qual/card@1
id: P-TFO34
kind: problem
title: $z\mapsto\overline{f(\bar z)}$ is analytic if $f$ is
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-reflection
  - cauchy-riemann
  - holomorphic-functions
relations: []
review: draft
solved: true
---

::: problem
Prove that if $z\mapsto f(z)$ is analytic, then $z \mapsto \bar{f(\bar z)}$ is analytic.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $z \mapsto f(z)$ is analytic on a domain $\Omega$, then $z \mapsto \overline{f(\bar z)}$ is analytic on $\overline{\Omega} \definedas \theset{\bar z \suchthat z \in \Omega}$.

<1>1. Fix $z_0 \in \Omega$; near $z_0$, $f$ has a convergent power series $f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$.
Proof: Analytic functions are locally representable by power series (Taylor expansion).

<1>2. Compute $\overline{f(\bar z)}$ for $z$ near $\bar z_0$.
<2>1. $\overline{f(\bar z)} = \sum_{n=0}^{\infty} \bar a_n (z - \bar z_0)^n$.
Proof: Substitute $\bar z$ for $z$ in <1>1 and conjugate termwise: $\overline{a_n(\bar z - z_0)^n} = \bar a_n \overline{(\bar z - z_0)}^n = \bar a_n (z - \bar z_0)^n$.
<2>2. The series $\sum \bar a_n (z - \bar z_0)^n$ converges for $\abs{z - \bar z_0} < r$, where $r$ is the radius of convergence of <1>1. Proof: $\abs{z - \bar z_0} = \abs{\bar z - z_0}$, so the set of convergence is the mirror image of that of <1>1.

<1>3. $g(z) := \overline{f(\bar z)}$ is analytic at $\bar z_0$.
Proof: <1>2.1 gives a power series representation of $g$ centered at $\bar z_0$ with positive radius of convergence, which characterizes analyticity.

<1>4. Q.E.D. Proof: $\bar z_0$ was an arbitrary point of $\overline{\Omega}$, so $g$ is analytic throughout $\overline{\Omega}$.
:::
