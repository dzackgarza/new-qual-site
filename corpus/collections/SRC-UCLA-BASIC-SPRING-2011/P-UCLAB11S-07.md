---
schema: qual/card@1
id: P-UCLAB11S-07
kind: problem
title: Existence of a real root of $x^5-3x+1$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Prove that there exists a real number $x$ such that
$$
x^5-3x+1=0.
$$
:::

::: {.solution}

Define
$$
p(x)=x^5-3x+1.
$$

::: pf

::: {.pf-step #s1-1}

The function $p$ is continuous on $\RR$.


::: pf-proof

The function $p$ is a polynomial, and every polynomial is continuous.

:::

:::

::: {.pf-step #s1-2}

One has
$$
p(0)=1>0.
$$


::: pf-proof

Direct substitution gives
$$
p(0)
=
0^5-3\cdot0+1
=1.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
p(1)=-1<0.
$$


::: pf-proof

Direct substitution gives
$$
p(1)
=
1-3+1
=
-1.
$$

:::

:::

::: {.pf-step #s1-4}

There exists
$$
c\in(0,1)
$$
such that
$$
\boxed{c^5-3c+1=0}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, the continuous function $p$ takes opposite signs at $0$ and $1$.
The intermediate value theorem therefore gives
$$
c\in(0,1)
$$
with
$$
p(c)=0.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required existence statement.

:::

:::

:::
