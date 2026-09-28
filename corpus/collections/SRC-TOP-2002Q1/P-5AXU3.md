---
schema: qual/card@1
id: P-5AXU3
kind: problem
title: Maps $X\to S^1$ are nullhomotopic when $\pi_1(X)$ is finite
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section B, problem B1 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Repaired the covering-space basepoint: choose t0 in R above f(x0), rather
    than using 0 unless f(x0)=1. The finite image of f_* in pi_1(S^1) = Z is
    trivial, so the lifting criterion gives a lift to R, which contracts by a
    straight-line homotopy.
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.problem}
Show that if $X$ is a path-connected, locally path-connected topological space with finite fundamental group $\pi_1(X, x_0)$, then every continuous map $f : X \to S^1$ is **homotopic to a constant map** (nullhomotopic).
:::

::: {.solution}
Let $p\colon\RR\to S^1$, $p(t)=e^{2\pi it}$, be the universal covering map, and choose $t_0\in\RR$ with $p(t_0)=f(x_0)$.

<1>1. The induced homomorphism $f_*\colon\pi_1(X,x_0)\to\pi_1(S^1,f(x_0))\cong\ZZ$ is trivial.

::: {.proof}
The group $\pi_1(X,x_0)$ is finite by hypothesis, so its homomorphic image $f_*(\pi_1(X,x_0))$ is a finite subgroup of $\ZZ$.
Every nontrivial subgroup of $\ZZ$ is infinite, so $f_*(\pi_1(X,x_0))=\{0\}$.
:::

<1>2. The map $f$ lifts to a continuous map $\widetilde f\colon X\to\RR$ with $\widetilde f(x_0)=t_0$ and $p\circ\widetilde f=f$.

::: {.proof}
Because $\RR$ is simply connected, $p_*(\pi_1(\RR,t_0))$ is the trivial subgroup of $\pi_1(S^1,f(x_0))$.
By step <1>1, $f_*(\pi_1(X,x_0))\subseteq p_*(\pi_1(\RR,t_0))$.
Since $X$ is path-connected and locally path-connected, the lifting criterion for covering spaces, applied with the point $t_0\in p^{-1}(f(x_0))$, gives the lift.
:::

<1>3. The lift $\widetilde f$ is homotopic to the constant map with value $t_0$.

::: {.proof}
Define $H\colon X\times[0,1]\to\RR$ by $H(x,s)=(1-s)\widetilde f(x)+s t_0$.
This map is continuous, $H(x,0)=\widetilde f(x)$, and $H(x,1)=t_0$.
:::

<1>4. Q.E.D.

::: {.proof}
Let $F=p\circ H\colon X\times[0,1]\to S^1$, with $H$ from step <1>3.
By step <1>2, $F(x,0)=p(\widetilde f(x))=f(x)$, and $F(x,1)=p(t_0)=f(x_0)$ for every $x\in X$.
Hence $F$ is a homotopy from $f$ to the constant map with value $f(x_0)$, and $f$ is nullhomotopic.
:::
:::
