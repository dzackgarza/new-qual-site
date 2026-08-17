---
schema: qual/card@1
id: P-Q75IH
kind: problem
title: The symmetric derivative of a singular measure vanishes Lebesgue-a.e.
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Prove the following variant of the Lebesgue differentiation theorem: Let $\mu$ be a finite Borel measure on $\mathbb{R}$, singular with respect to Lebesgue measure.
Then for Lebesgue almost every $x\in\mathbb{R}$, $$\lim_{\epsilon\to 0} \frac{\mu([x-\epsilon,x+\epsilon])}{2\epsilon} = 0.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Decompose $\mu$ relative to the measure $\lambda = \mu + m$.
Proof: both $\mu$ and Lebesgue measure $m$ are absolutely continuous with respect to $\lambda$, and $\mu \ll \lambda$ with density $g = d\mu/d\lambda$, $0 \le g \le 1$.
Since $\mu \perp m$, there is a Borel set $A$ with $m(A) = 0$ and $\mu(A^c) = 0$.
Then $g = 0$ $\lambda$-a.e. on $A^c$: indeed $\int_{A^c}g\,d\lambda = \mu(A^c) = 0$.
In particular $g = 0$ at $m$-a.e. point (as $m(A) = 0$ and $m \ll \lambda$). <1>2. Apply the Lebesgue differentiation theorem to $g \in L^1(\lambda)$.
Proof: the classical LDT for locally integrable functions with respect to the finite Borel measure $\lambda$ (Vitali-covering argument with the centered intervals $[x-\epsilon, x+\epsilon]$) gives, for $\lambda$-a.e. $x$, \[\frac{1}{\lambda([x-\epsilon,x+\epsilon])}\int_{[x-\epsilon,x+\epsilon]}g\,d\lambda \longrightarrow g(x) \quad \text{as } \epsilon \to 0.\] <1>3. Convert the average into the symmetric derivative of $\mu$.
Proof: since $\mu(I) = \int_I g\,d\lambda$ and $\lambda(I) = 2\epsilon + \mu(I)$ for $I = [x-\epsilon,x+\epsilon]$, \[\frac{\mu(I)}{2\epsilon} = \frac{\lambda(I)}{2\epsilon}\cdot\frac{\mu(I)}{\lambda(I)} = \left(1 + \frac{\mu(I)}{2\epsilon}\right)\cdot\frac{\int_I g\,d\lambda}{\lambda(I)}.\] Let $a_\epsilon = \int_I g\,d\lambda/\lambda(I) \to g(x)$ along a $\lambda$-a.e. $x$.
Then $\frac{\mu(I)}{2\epsilon}(1 - a_\epsilon) = a_\epsilon$; if $g(x) \ne 1$, dividing gives $\frac{\mu(I)}{2\epsilon} = \frac{a_\epsilon}{1 - a_\epsilon} \to \frac{g(x)}{1-g(x)}$.
<1>4. For $m$-a.e. $x$, $g(x) = 0$, so the limit is $0$.
Proof: by <1>1, $g = 0$ at $m$-a.e. $x$.
For such $x$ the formula of <1>3 yields \[\lim_{\epsilon\to 0}\frac{\mu([x-\epsilon,x+\epsilon])}{2\epsilon} = \frac{0}{1-0} = 0.\] (The excluded set, where $g(x) = 1$, is $\lambda$-null on $A^c$ and sits inside $A$ where it has $m$-measure zero, so it is $m$-negligible.)
<1>5. Q.E.D.
:::
