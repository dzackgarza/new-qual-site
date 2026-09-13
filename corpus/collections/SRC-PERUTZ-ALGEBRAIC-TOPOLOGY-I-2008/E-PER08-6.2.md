---
schema: qual/card@1
id: E-PER08-6.2
kind: problem
title: Perutz Algebraic Topology I Exercise 6.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Make the topology on ˜X more precise, then prove the proposition.
:::

::: {.solution}
Fix $x_0\in X$.
Let $\widetilde X$ be the set of endpoint-preserving homotopy classes $[\gamma]$ of paths beginning at $x_0$, and let $p([\gamma])=\gamma(1)$.

<1>1. Define the topology.
::: {.proof}
For $[\gamma]\in\widetilde X$ and a path-connected open neighbourhood $U$ of $\gamma(1)$ for which $\pi_1(U)\to\pi_1(X)$ is trivial, set
\[
B([\gamma],U)=\{[\gamma*\eta]:\eta:[0,1]\to U,\ \eta(0)=\gamma(1)\}.
\]
These sets form a basis.
Indeed $[\gamma]\in B([\gamma],U)$, and if $[\alpha]$ lies in the intersection of two basic sets, local path connectedness gives a smaller path-connected open $W$ around $p([\alpha])$ contained in the two corresponding base opens; then $B([\alpha],W)$ lies in the intersection.
The triviality of the relevant $\pi_1$ images guarantees that the description is independent of the chosen paths inside $U$.
:::

<1>2. $p$ is a covering map.
::: {.proof}
For a basic neighbourhood $B([\gamma],U)$, the restriction
\[
p:B([\gamma],U)\to U
\]
is bijective.
Surjectivity follows from path connectedness of $U$.
If $[\gamma*\eta_1]$ and $[\gamma*\eta_2]$ have the same endpoint, then $\eta_1*\eta_2^{-1}$ is a loop in $U$ and is null-homotopic in $X$, so the two path classes coincide.
The definition of the basis makes this bijection a homeomorphism.
For fixed $U$, the sets $B([\gamma],U)$ over the various points of $p^{-1}(U)$ are disjoint and cover $p^{-1}(U)$, so $U$ is evenly covered.
:::

<1>3. $\widetilde X$ is simply connected.
::: {.proof}
A path in $\widetilde X$ beginning at the class of the constant path is precisely the lift, under $p$, of its projection to $X$.
If a loop $\widetilde\alpha$ at the basepoint projects to $\alpha$, then the endpoint of the canonical lift of $\alpha$ is $[\alpha]$.
Since the lift is closed, $[\alpha]$ is the constant-path class; hence $\alpha$ is null-homotopic in $X$.
Lift a null-homotopy of $\alpha$ to $\widetilde X$; uniqueness of homotopy lifting contracts $\widetilde\alpha$.
Therefore $\pi_1(\widetilde X)=0$.
:::
:::
