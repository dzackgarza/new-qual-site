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
\[
x^5-3x+1=0.
\]
:::

::: {.solution}
Define
\[
p(x)=x^5-3x+1.
\]

<1>1. The function $p$ is continuous on $\mathbb R$.

::: {.proof}
The function $p$ is a polynomial, and every polynomial is continuous.
:::

<1>2. One has
\[
p(0)=1>0.
\]

::: {.proof}
Direct substitution gives
\[
p(0)
=
0^5-3\cdot0+1
=1.
\]
:::

<1>3. One has
\[
p(1)=-1<0.
\]

::: {.proof}
Direct substitution gives
\[
p(1)
=
1-3+1
=
-1.
\]
:::

<1>4. There exists
\[
c\in(0,1)
\]
such that
\[
\boxed{c^5-3c+1=0}.
\]

::: {.proof}
By steps <1>1--<1>3, the continuous function $p$ takes opposite signs at $0$ and $1$.
The intermediate value theorem therefore gives
\[
c\in(0,1)
\]
with
\[
p(c)=0.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required existence statement.
:::
:::
