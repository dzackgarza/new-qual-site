---
schema: qual/card@1
id: P-KSRING17-045
kind: problem
title: Prime ideals in a ring with a nontrivial idempotent contain nontrivial idempotents
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 45 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[NEW] Let R be a commutative ring with identity.
Suppose R contains an idempotent element a other than 0 or 1. Show that every prime ideal in R contains an idempotent element other than 0 or 1. (An element $a \in R$ is idempotent if $a ^ { 2 } = a . )$
:::

::: {.solution}
Let
$$
P
$$
be an arbitrary prime ideal of $R$.

<1>1. Since
$$
a^2=a,
$$
one has
$$
a(1-a)=0.
$$

::: {.proof}
Rearrange the idempotent relation:
$$
a-a^2=0.
$$
Factoring gives
$$
a(1-a)=0.
$$
:::

<1>2. One has
$$
a\in P
\quad\text{or}\quad
1-a\in P.
$$

::: {.proof}
By step <1>1,
$$
a(1-a)=0\in P.
$$
Since $P$ is prime,
$$
a\in P
\quad\text{or}\quad
1-a\in P.
$$
:::

<1>3. The element
$$
1-a
$$
is idempotent.

::: {.proof}
Using
$$
a^2=a,
$$
one computes
$$
\begin{aligned}
(1-a)^2
&=
1-2a+a^2\\
&=
1-2a+a\\
&=
1-a.
\end{aligned}
$$
Thus $1-a$ is idempotent.
:::

<1>4. Both
$$
a
\qquad\text{and}\qquad
1-a
$$
are different from
$$
0
\qquad\text{and}\qquad
1.
$$

::: {.proof}
The hypothesis already gives
$$
a\ne0,
\qquad
a\ne1.
$$
If
$$
1-a=0,
$$
then
$$
a=1,
$$
contradiction.
If
$$
1-a=1,
$$
then
$$
a=0,
$$
contradiction.
Therefore $1-a$ is also nontrivial.
:::

<1>5. Therefore every prime ideal $P$ contains a nontrivial idempotent.

::: {.proof}
By step <1>2, the ideal $P$ contains either $a$ or $1-a$. By steps <1>3--<1>4, whichever element occurs is an idempotent different from both $0$ and $1$.
Thus
$$
\boxed{
\text{every prime ideal of }R\text{ contains a nontrivial idempotent.}
}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
