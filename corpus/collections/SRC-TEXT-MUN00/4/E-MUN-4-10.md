---
schema: qual/card@1
id: E-MUN-4-10
kind: problem
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

::: pf

::: {.pf-step #s1}

For $x > 0$ and $0 \le h < 1$, $(x + h)^2 \le x^2 + h(2x + 1)$ and $(x - h)^2 \ge x^2 - h(2x)$.

::: pf-proof

Since $0 \le h < 1$, $h^2 \le h$, so
$$(x + h)^2 = x^2 + 2xh + h^2 \le x^2 + 2xh + h = x^2 + h(2x + 1).$$
Since $h^2 \ge 0$,
$$(x - h)^2 = x^2 - 2xh + h^2 \ge x^2 - h(2x).$$

:::

:::

::: {.pf-step #s2}

Let $x > 0$. If $x^2 < a$, then $(x + h)^2 < a$ for some $h > 0$; if $x^2 > a$, then $(x - h)^2 > a$ for some $h$ with $0 < h < x$.

::: pf-proof

Suppose $x^2 < a$. Put $h = \min\left(\frac{a - x^2}{2x + 1}, \frac12\right) > 0$ and $h' = h/2$. Then $0 < h' < h < 1$, and step [](#s1){.pf-ref} gives
$$(x + h')^2 \le x^2 + h'(2x + 1) < x^2 + h(2x + 1) \le x^2 + (a - x^2) = a.$$

Suppose $x^2 > a$. Put $h = \min\left(\frac{x^2 - a}{2x}, \frac{x}{2}, \frac12\right) > 0$ and $h' = h/2$. Then $0 < h' < x$ and $h' < 1$, and step [](#s1){.pf-ref} gives
$$(x - h')^2 \ge x^2 - h'(2x) > x^2 - h(2x) \ge x^2 - (x^2 - a) = a.$$

:::

:::

::: {.pf-step #s3}

The set $B = \{x \in \RR \mid x^2 < a\}$ contains a positive number and is bounded above by $1 + a$.

::: pf-proof

Put $x_0 = \min(1, a/2) > 0$. Then $x_0^2 \le x_0 < a$, so $x_0 \in B$. If $x > 1 + a$, then $x^2 > (1 + a)^2 = 1 + 2a + a^2 > a$, so $x \notin B$.

:::

:::

::: {.pf-step #s4}

$b = \sup B$ exists, $b > 0$, and $b^2 = a$.

::: pf-proof

By step [](#s3){.pf-ref} and the least upper bound property of $\RR$, $b = \sup B$ exists and $b \ge x_0 > 0$.

If $b^2 < a$, step [](#s2){.pf-ref} gives $h > 0$ with $(b + h)^2 < a$. Then $b + h \in B$ and $b + h > b$, which contradicts that $b$ is an upper bound of $B$.

If $b^2 > a$, step [](#s2){.pf-ref} gives $h$ with $0 < h < b$ and $(b - h)^2 > a$. Let $x \in B$. If $x \le 0$, then $x < b - h$. If $x > 0$, then $x^2 < a < (b - h)^2$ with $x, b - h > 0$, so $x < b - h$. Hence $b - h$ is an upper bound of $B$ smaller than $b$, which contradicts that $b$ is the least upper bound.

By trichotomy, $b^2 = a$.

:::

:::

::: {.pf-step #s5}

If $b, c > 0$ and $b^2 = c^2$, then $b = c$.

::: pf-proof

$(b - c)(b + c) = b^2 - c^2 = 0$ and $b + c > 0$, so $b - c = 0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} with steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove parts (a), (b), (c), and (d). By step [](#s4){.pf-ref}, $\sup\{x \in \RR \mid x^2 < a\}$ is a positive square root of $a$, and by step [](#s5){.pf-ref} it is the only one.

:::

:::

:::
