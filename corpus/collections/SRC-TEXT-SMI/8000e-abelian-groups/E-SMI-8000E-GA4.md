---
schema: qual/card@1
id: E-SMI-8000E-GA4
kind: problem
title: Hom from a free abelian group into Q is a rational vector space of the same rank
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Hom and Duality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Prove that $\Hom(\ZZ^s, \QQ)$ is isomorphic as a $\QQ$-vector space to $\QQ^s$, by sending the map $f: \ZZ^s \to \QQ$ to the vector $(f(e_1), \ldots, f(e_s))$ — where we multiply maps by rational numbers by multiplying their values, to make $\Hom(\ZZ^s, \QQ)$ into a $\QQ$-vector space.
[Hint: one proof would be to find a $\QQ$-basis for $\Hom(\ZZ^s, \QQ)$ consisting of exactly $s$ elements.]
:::

::: {.solution}
<1>1. Define $\Phi: \Hom(\ZZ^s, \QQ) \to \QQ^s$ by $\Phi(f) = (f(e_1), \ldots, f(e_s))$.
::: {.proof}
definition.
:::

<1>2. $\Phi$ is $\QQ$-linear.
::: {.proof}
$\Phi(f + g) = ((f+g)(e_1), \ldots) = (f(e_1) + g(e_1), \ldots) = \Phi(f) + \Phi(g)$, and $\Phi(qf) = (qf(e_1), \ldots) = q\Phi(f)$ for $q \in \QQ$.
:::

<1>3. $\Phi$ is injective.
::: {.proof}
if $\Phi(f) = 0$, then $f(e_i) = 0$ for all $i$; since $\{e_1, \ldots, e_s\}$ generates $\ZZ^s$, $f = 0$.
:::

<1>4. $\Phi$ is surjective.
::: {.proof}
given $(q_1, \ldots, q_s) \in \QQ^s$, define $f: \ZZ^s \to \QQ$ by $f(\sum_i n_i e_i) = \sum_i n_i q_i$; this is a well-defined homomorphism with $\Phi(f) = (q_1, \ldots, q_s)$.
:::

<1>5. Hence $\Phi$ is a $\QQ$-linear isomorphism $\Hom(\ZZ^s, \QQ) \cong \QQ^s$.
::: {.proof}
<1>2–<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
