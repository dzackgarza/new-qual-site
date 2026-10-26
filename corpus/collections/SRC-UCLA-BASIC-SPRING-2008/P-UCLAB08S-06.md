---
schema: qual/card@1
id: P-UCLAB08S-06
kind: problem
title: A complete countable metric space has an isolated point
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $Y$ be a complete countable metric space.
Prove that there exists $y\in Y$ such that the singleton $\{y\}$ is open.
:::

Assume for contradiction that no singleton in $Y$ is open.

::: pf

::: pf-step

Every singleton
\[
\{y\}\subseteq Y
\]
is closed.


::: pf-proof

Metric spaces are $T_1$.
More directly, if
\[
x\ne y,
\]
then the ball
\[
B\left(x,\frac{d(x,y)}2\right)
\]
contains $x$ but not $y$.
Thus
\[
Y\setminus\{y\}
\]
is open, so
\[
\{y\}
\]
is closed.

:::

:::

::: pf-step

Under the contradiction hypothesis, every singleton
\[
\{y\}
\]
has empty interior.


::: pf-proof

If
\[
\operatorname{int}\{y\}
\ne
\varnothing,
\]
then necessarily
\[
y\in\operatorname{int}\{y\},
\]
so
\[
\{y\}
\]
would itself be open.
This contradicts the standing assumption.

:::

:::

::: pf-step

Under the contradiction hypothesis, every singleton is nowhere dense.


::: pf-proof

By step <1>1, each singleton is closed.
Therefore
\[
\overline{\{y\}}=\{y\}.
\]
By step <1>2, this closure has empty interior.
That is exactly the definition of nowhere dense.

:::

:::

::: pf-step

Since $Y$ is countable, write
\[
Y=\{y_1,y_2,\ldots\}.
\]
Then
\[
Y
=
\bigcup_{n=1}^{\infty}\{y_n\}
\]
is a countable union of nowhere dense subsets of $Y$.


::: pf-proof

Countability gives an enumeration of $Y$.
Step <1>3 shows that each singleton in the union is nowhere dense.

:::

:::

::: pf-step

Step <1>4 contradicts the Baire category theorem.


::: pf-proof

The Baire category theorem states that a nonempty complete metric space cannot be expressed as a countable union of nowhere dense subsets of itself.
The space $Y$ is complete by hypothesis.
Step <1>4 gives exactly such a representation.
Thus the contradiction hypothesis is impossible.

:::

:::

::: pf-step

Therefore there exists
\[
y\in Y
\]
such that
\[
\boxed{\{y\}\text{ is open in }Y}.
\]


::: pf-proof

The negation of the displayed conclusion was the contradiction hypothesis.
Step <1>5 shows that hypothesis is false.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
