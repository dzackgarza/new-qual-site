---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W2
kind: problem
title: Absolute-value Stieltjes integrability without function integrability
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Counterexamples
relations: []
review: draft
---

::: {.problem title="?"}
([Apo74, 7.12] c.f. [Rud76, p. 138 #3]) Give an example of a bounded function $f$ and an increasing function $\alpha$ defined on $[a,b]$ such that $|f|\in\mathcal R(\alpha)$ but $f\notin\mathcal R(\alpha)$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. The example.
Proof: take $[a,b] = [0,1]$, $\alpha(x) = x$ (increasing), and $f(x) = 1$ if $x$ is rational, $f(x) = -1$ if $x$ is irrational.
<1>2. $|f| \in \mathcal{R}(\alpha)$.
Proof: $|f| \equiv 1$ on $[0,1]$, a constant, hence Riemann integrable with $\int_0^1 |f|\,dx = 1$.
<1>3. $f \notin \mathcal{R}(\alpha)$.
Proof: on any subinterval $[x_{i-1}, x_i]$, the interval contains both rationals and irrationals (density of both in $\mathbb{R}$), so $\inf f = -1$ and $\sup f = 1$ on every subinterval.
Hence for every partition $P$, $L(f, P) = -1$ and $U(f, P) = 1$, so $U(f,P) - L(f,P) = 2$ never goes to $0$; the Riemann criterion fails and $f \notin \mathcal{R}$.
<1>4. Q.E.D.
:::
