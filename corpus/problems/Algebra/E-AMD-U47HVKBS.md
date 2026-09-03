---
schema: qual/card@1
id: E-AMD-U47HVKBS
kind: problem
title: $I$ is a prime ideal iff $R/I$ is an integral domain
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Integral Domains
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Show that $I \normal R$ is prime iff $R/I$ is an integral domain.
:::

::: {.solution}
<1>1. Definitions:
<2>1. An ideal $I$ of a commutative ring $R$ with identity $1 \neq 0$ is a **prime ideal** if $I \subsetneq R$ (i.e. $1 \notin I$) and for all $a, b \in R$:
\[
ab \in I \implies a \in I \quad \text{or} \quad b \in I.
\]
<2>2. A commutative ring $S$ is an **integral domain** if $1_S \neq 0_S$ and for all $x, y \in S$:
\[
xy = 0_S \implies x = 0_S \quad \text{or} \quad y = 0_S.
\]

<1>2. Direction ($\Rightarrow$): If $I$ is prime, then $R/I$ is an integral domain:
<2>1. Since $I$ is prime, $I \neq R$, which implies $1 \notin I$, and thus $1 + I \neq 0 + I$ in $R/I$ (the identity element is distinct from the zero element).
<2>2. Let $\bar{a} = a + I$ and $\bar{b} = b + I$ in $R/I$ satisfy $\bar{a} \bar{b} = 0_{R/I}$.
By the definition of multiplication in the quotient ring:
\[
ab + I = 0 + I \implies ab \in I.
\]
<2>3. Because $I$ is prime, $ab \in I$ implies $a \in I$ or $b \in I$.
If $a \in I$, then $\bar{a} = a + I = 0 + I = 0_{R/I}$.
If $b \in I$, then $\bar{b} = b + I = 0 + I = 0_{R/I}$.
Therefore $R/I$ has no non-zero zero divisors, so $R/I$ is an integral domain.

<1>3. Direction ($\Leftarrow$): If $R/I$ is an integral domain, then $I$ is prime:
<2>1. Since $R/I$ is an integral domain, $1 + I \neq 0 + I$, so $1 \notin I$, which gives $I \subsetneq R$.
<2>2. Let $a, b \in R$ with $ab \in I$.
In $R/I$, this translates to:
\[
(a + I)(b + I) = ab + I = 0 + I = 0_{R/I}.
\]
<2>3. Because $R/I$ is an integral domain, it has no non-zero zero divisors, so:
\[
a + I = 0_{R/I} \quad \text{or} \quad b + I = 0_{R/I}.
\]
This means $a \in I$ or $b \in I$.
Therefore $I$ is a prime ideal of $R$.

<1>4. Conclusion:
$I$ is a prime ideal if and only if $R/I$ is an integral domain. Q.E.D.
:::
