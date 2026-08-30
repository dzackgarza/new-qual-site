---
schema: qual/card@1
id: E-MUN-4-10
kind: exercise
title: Existence and uniqueness of positive square roots
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that every positive number $a$ has exactly one positive square root, as follows:

(a) Show that if $x > 0$ and $0 \leq h < 1$, then

$$
(x + h) ^ {2} \leq x ^ {2} + h (2 x + 1),
$$

$$
(x - h) ^ {2} \geq x ^ {2} - h (2 x).
$$

(b) Let $x > 0$ . Show that if $x^2 < a$, then $(x + h)^2 < a$ for some $h > 0$ ; and if $x^2 > a$, then $(x - h)^2 > a$ for some $h > 0$ .

(c) Given $a > 0$, let $B$ be the set of all real numbers $x$ such that $x^2 < a$ . Show that $B$ is bounded above and contains at least one positive number.
Let $b = \sup B$ ; show that $b^2 = a$ .

(d) Show that if $b$ and $c$ are positive and $b^2 = c^2$, then $b = c$ .
:::

::: {.solution}
<1>1. Part (a): Quadratic inequalities for $x > 0$ and $0 \le h < 1$: <2>1. Expand $(x + h)^2$:
\[
(x + h)^2 = x^2 + 2xh + h^2.
\]
Because $0 \le h < 1$, we have $h^2 \le h$.
Therefore:
\[
(x + h)^2 = x^2 + 2xh + h^2 \le x^2 + 2xh + h = x^2 + h(2x + 1).
\]
Proof: $0 \le h < 1 \implies h^2 \le h$.
<2>2. Expand $(x - h)^2$:
\[
(x - h)^2 = x^2 - 2xh + h^2 \ge x^2 - 2xh = x^2 - h(2x),
\]
since $h^2 \ge 0$.
Proof: square of any real number is non-negative.

<1>2. Part (b): Stepping inequalities: <2>1. Suppose $x^2 < a$.
Then $a - x^2 > 0$.
Choose $h = \min\left( \frac{a - x^2}{2x + 1}, \, \frac{1}{2} \right) > 0$.
Then $0 < h < 1$, so by Part (a):
\[
(x + h)^2 \le x^2 + h(2x + 1) \le x^2 + \left(\frac{a - x^2}{2x + 1}\right)(2x + 1) = x^2 + a - x^2 = a.
\]
Since $h \le \frac{1}{2} < \frac{a - x^2}{2x + 1}$ or $h = \frac{a - x^2}{2x + 1}$, choosing $h' = \frac{h}{2} > 0$ yields $(x + h')^2 < a$.
Proof: Part (a) and choice of $h$.
<2>2. Suppose $x^2 > a$.
Then $x^2 - a > 0$.
Choose $h = \min\left( \frac{x^2 - a}{2x}, \, \frac{x}{2} \right) > 0$.
Then $x - h > 0$, and by Part (a):
\[
(x - h)^2 \ge x^2 - h(2x) \ge x^2 - \left(\frac{x^2 - a}{2x}\right)(2x) = x^2 - (x^2 - a) = a.
\]
Choosing $h' = \frac{h}{2} > 0$ yields $(x - h')^2 > a$.
Proof: Part (a) and choice of $h$.

<1>3. Part (c): Existence of $\sup B$ and proof that $b^2 = a$: <2>1. Let $B = \{x \in \mathbb{R} \mid x^2 < a\}$.
For $x_0 = \min(1, \frac{a}{2}) > 0$, $x_0^2 \le x_0 < a$, so $x_0 \in B$, meaning $B$ contains a positive number and is non-empty.
If $x > 1 + a$, then $x^2 > (1 + a)^2 = 1 + 2a + a^2 > a$, so $x \notin B$.
Thus $1 + a$ is an upper bound for $B$.
By the Least Upper Bound Property of $\mathbb{R}$, $b = \sup B$ exists and $b \ge x_0 > 0$.
Proof: completeness of $\mathbb{R}$.
<2>2. Suppose for contradiction that $b^2 < a$.
By Part (b), there exists $h > 0$ such that $(b + h)^2 < a$.
Then $b + h \in B$, which contradicts that $b$ is an upper bound of $B$ (since $b + h > b$). Proof: definition of upper bound.
<2>3. Suppose for contradiction that $b^2 > a$.
By Part (b), there exists $h \in (0, b)$ such that $(b - h)^2 > a$.
For any $x \in B$, $x^2 < a < (b - h)^2$, which implies $x < b - h$.
Thus $b - h$ is an upper bound of $B$, contradicting that $b = \sup B$ is the least upper bound (since $b - h < b$). Proof: definition of supremum.
<2>4. By trichotomy of real numbers, we must have $b^2 = a$.
Proof: exclusion of $b^2 < a$ and $b^2 > a$.

<1>4. Part (d): Uniqueness of positive square roots: <2>1. Let $b, c > 0$ such that $b^2 = c^2$.
Then $b^2 - c^2 = 0 \implies (b - c)(b + c) = 0$.
Since $b > 0$ and $c > 0$, $b + c > 0$.
Dividing by $b + c$ yields $b - c = 0$, so $b = c$.
Proof: factorization of difference of squares and non-zero sum of positive numbers.

<1>5. Conclusion: Every positive number $a > 0$ has a unique positive square root $b = \sup \{x \in \mathbb{R} \mid x^2 < a\}$.
Q.E.D. Proof: <1>1 through <1>4.
:::
