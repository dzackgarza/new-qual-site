---
schema: qual/card@1
id: P-BKF06-2B
kind: problem
title: Linear independence of the monomials in $C^0[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained polynomial-root argument.
---

::: {.problem}
Let $C^0[0,1]$ be the real vector space of continuous functions $[0,1]\to\mathbb R$.
Show that the functions
\[
1,x,x^2,\ldots
\]
are linearly independent in $C^0[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #relation-form}
Suppose a finite linear combination of the displayed functions
vanishes:
$$
c_0+c_1x+\cdots+c_nx^n=0
$$
as an element of $C^0[0,1]$.

::: pf-proof
This is the general form of a finite linear relation among
$1,x,x^2,\ldots$. Equality to the zero function means that the
polynomial
$$
p(t)=c_0+c_1t+\cdots+c_nt^n
$$
satisfies $p(t)=0$ for every $t\in[0,1]$.
:::

:::

::: {.pf-step #p-is-zero-polynomial}
The polynomial $p$ from step [](#relation-form){.pf-ref} is the zero polynomial.

::: pf-proof
If $p$ were nonzero and had degree at most $n$, it could have at most
$n$ distinct real roots. Step [](#relation-form){.pf-ref} gives infinitely many roots,
namely every point of $[0,1]$. Hence $p$ must be the zero polynomial.
:::

:::

::: {.pf-step #coefficients-vanish}
All coefficients in the relation vanish:
$$
c_0=c_1=\cdots=c_n=0.
$$

::: pf-proof
By step [](#p-is-zero-polynomial){.pf-ref}, $p$ is the zero polynomial. A polynomial is zero exactly
when all of its coefficients are zero.
:::

:::

::: {.pf-step #linear-independence}
Therefore
$$
\boxed{1,x,x^2,\ldots\text{ are linearly independent in }C^0[0,1]}.
$$

::: pf-proof
Steps [](#relation-form){.pf-ref}, [](#p-is-zero-polynomial){.pf-ref} and [](#coefficients-vanish){.pf-ref} show that every finite linear relation is trivial,
which is the definition of linear independence.
:::

:::

::: pf-qed
Step [](#linear-independence){.pf-ref} is the required conclusion.
:::

:::

:::
