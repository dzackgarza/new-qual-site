---
schema: qual/card@1
id: P-BKF05-6B
kind: problem
title: Unique nearest points in closed convex subsets of Euclidean space
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained compactness argument for existence and
    replaced the geometric uniqueness sentence by the Euclidean midpoint
    identity, which gives a strict decrease whenever two minimizers are
    distinct.
---

::: {.problem}
Let \(K\subseteq\mathbb R^n\) be nonempty, closed, and convex.
Show that for every \(x\in\mathbb R^n\) there exists a unique \(y\in K\) minimizing the Euclidean distance to \(x\); equivalently,
\[
\|x-y\|<\|x-z\|
\]
for every \(z\in K\setminus\{y\}\).
:::

::: {.solution}

Fix $x\in\RR^n$.

::: pf

::: {.pf-step #minimizer-exists}
The distance from $x$ to $K$ is attained at some point $y\in K$.

::: pf-proof
Choose $y_0\in K$, which is possible because $K$ is nonempty, and set
$$
R=\norm{x-y_0}.
$$
Let
$$
B=\{u\in\RR^n:\norm{x-u}\le R\}.
$$
Then $y_0\in K\cap B$, so $K\cap B$ is nonempty. Since $K$ and $B$
are closed and $B$ is bounded, $K\cap B$ is compact. Hence the
continuous function
$$
u\longmapsto\norm{x-u}
$$
attains a minimum on $K\cap B$ at some $y\in K\cap B$. Write
$$
d=\norm{x-y}.
$$
Since $y_0\in K\cap B$, one has $d\le R$. If $z\in K\cap B$, then
$d\le\norm{x-z}$ by the choice of $y$. If $z\in K\setminus B$, then
$$
\norm{x-z}>R\ge d.
$$
Thus $d\le\norm{x-z}$ for every $z\in K$, so $y$ is a global
distance minimizer.
:::

:::

::: {.pf-step #minimizer-unique}
The minimizer from step [](#minimizer-exists){.pf-ref} is unique.

::: pf-proof
Suppose that $y,z\in K$ are distinct minimizers, and let
$$
d=\norm{x-y}=\norm{x-z}.
$$
By convexity,
$$
w=\frac{y+z}{2}\in K.
$$
The Euclidean inner-product identity gives
$$
\begin{aligned}
\norm{x-w}^2
&=
\frac12\norm{x-y}^2
+\frac12\norm{x-z}^2
-\frac14\norm{y-z}^2
\\
&=
d^2-\frac14\norm{y-z}^2
<
d^2,
\end{aligned}
$$
because $y\ne z$. Hence
$$
\norm{x-w}<d,
$$
contradicting the minimality of $y$ and $z$. Therefore there is only
one minimizer.
:::

:::

::: {.pf-step #strict-inequality}
For the unique minimizer $y$, every $z\in K\setminus\{y\}$
satisfies
$$
\norm{x-y}<\norm{x-z}.
$$

::: pf-proof
Step [](#minimizer-exists){.pf-ref} gives
$$
\norm{x-y}\le\norm{x-z}
$$
for every $z\in K$. Equality for some $z\ne y$ would make $z$ a
second minimizer, contradicting step [](#minimizer-unique){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#minimizer-exists){.pf-ref}, [](#minimizer-unique){.pf-ref} and [](#strict-inequality){.pf-ref} prove existence, uniqueness, and the required strict
inequality.
:::

:::

:::
