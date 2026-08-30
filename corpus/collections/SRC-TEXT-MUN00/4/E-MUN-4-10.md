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
<1>1. (a) $(x+h)^2=x^2+2xh+h^2\le x^2+h(2x+1)$ for $0\le h<1$, and $(x-h)^2=x^2-2xh+h^2\ge x^2-h(2x)$.
Proof: expand.

<1>2. (b) If $x^2<a$, take $h=\min((a-x^2)/(2x+1),1/2)>0$, then $(x+h)^2<a$ by (a); if $x^2>a$, take $h=(x^2-a)/(2x)>0$, then $(x-h)^2>a$.
Proof: <1>1.

<1>3. (c) $B$ nonempty ($0\in B$) and bounded above by $1+a$, so $b=\sup B$ exists.
Proof: completeness.

<1>4. $b^2=a$: if $b^2<a$ then $(b+h)^2<a$ by (b) contradicting $b$ upper bound; if $b^2>a$ then $(b-h)^2>a$ contradicting $b$ least upper bound.
Proof: <1>2.

<1>5. (d) $b^2=c^2$ with $b,c>0$ implies $b=c$ (if $b\neq c$ assume $b<c$ then $b^2<c^2$).
Proof: monotonicity of squaring for positives.

<1>6. Q.E.D.
Proof: <1>4 and <1>5.
:::
