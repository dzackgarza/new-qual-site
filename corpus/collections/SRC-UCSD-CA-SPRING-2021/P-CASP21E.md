---
schema: qual/card@1
id: P-CASP21E
kind: problem
title: 'No bounded holomorphic function on $\DD$ has zero set $\theset{1-1/n \st n\geq 2}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Products
  - Bounded Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $a_n = 1 - \frac{1}{n}$ for $n \geq 2$.
Show that there are no bounded holomorphic functions $f : \DD \to \CC$ with zeros only at the $a_n$'s.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own use of the Blaschke condition follows, with the divergence of the sum and the exclusion of the zero function as separate steps.

::: pf

::: {.pf-step #blaschke}
A bounded holomorphic $f\not\equiv0$ on $\DD$ has zeros $z_{1},z_{2},\dots$ satisfying $\sum_{n}\big(1-\abs{z_{n}}\big)<\infty$.

::: pf-proof
This is the Blaschke condition: if $f$ is bounded by $M$ and nonzero, its zeros cannot accumulate in $\DD$ and their Blaschke sum converges, which is the first half of the Blaschke factorisation theorem. Applied to $f$ whose zeros include the sequence $a_{n}$, it forces the sum over the $a_{n}$ to converge.
:::

:::

::: {.pf-step #diverges}
$\displaystyle\sum_{n\ge2}\big(1-\abs{a_{n}}\big)=\sum_{n\ge2}\frac1n=\infty$.

::: pf-proof
$a_{n}=1-\frac1n\in[0,1)$, so $\abs{a_{n}}=1-\frac1n$ and $1-\abs{a_{n}}=\frac1n$; the harmonic series diverges.
:::

:::

::: {.pf-step #zero-function}
The zero function does not have zeros "only at the $a_{n}$".

::: pf-proof
The zero set of the function $f\equiv0$ is all of $\DD$, which properly contains $\theset{a_{n}\mid n\ge2}$: for instance $0$ is a zero of $f$ but $0\ne a_{n}$ for every $n\ge2$.
:::

:::

::: {.pf-qed}
A nonzero bounded holomorphic $f$ with zeros at every $a_{n}$ would violate the Blaschke condition by steps [](#blaschke){.pf-ref} and [](#diverges){.pf-ref}, and the zero function is excluded by step [](#zero-function){.pf-ref}. So there is no bounded holomorphic $f:\DD\to\CC$ whose zeros are exactly the $a_{n}$.
:::

:::

:::
