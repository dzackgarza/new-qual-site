---
schema: qual/card@1
id: P-BKF15-9A
kind: problem
title: Injectivity of $x^3-2x$ on $\mathbb Q$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: equality
    of two values reduces to x^2+xy+y^2=2, and clearing denominators gives
    an infinite-descent contradiction modulo 2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the factorization, the parity argument for the homogeneous
    integer equation, and the minimal-denominator descent.
---

::: {.problem}
Show that $x ^ { 3 } - 2 x$ is an injective function from the rational numbers to the rational numbers.
:::

::: {.solution}
Let
$$
F(x)\coloneqq x^3-2x.
$$

::: pf

::: {.pf-step #s1}

If
$$
F(x)=F(y),
$$
then either $x=y$ or
$$
x^2+xy+y^2=2.
$$

::: pf-proof

One has
$$
\begin{aligned}
0
&=
F(x)-F(y)\\
&=
x^3-y^3-2(x-y)\\
&=
(x-y)(x^2+xy+y^2-2).
\end{aligned}
$$
Thus one of the two factors must vanish.

:::

:::

::: {.pf-step #s2}

The equation
$$
x^2+xy+y^2=2
$$
has no solution $(x,y)\in\QQ^2$.

::: pf-proof

Suppose such a rational solution exists. Choose integers $a,b,c$ with
$c>0$ such that
$$
x=\frac ac,
\qquad
y=\frac bc,
$$
and choose such a representation with $c$ minimal. Clearing
denominators gives
$$
a^2+ab+b^2=2c^2.
$$

Reduce modulo $2$. For residues $a,b\in\FF_2$,
$$
a^2+ab+b^2=0
$$
only when $a=b=0$: the other three pairs give value $1$. Hence $a$
and $b$ are both even.

It follows that the left-hand side is divisible by $4$, so
$$
2c^2
$$
is divisible by $4$. Thus $c^2$ is even and hence $c$ is even.
Therefore $a,b,c$ are all divisible by $2$, and
$$
x=\frac{a/2}{c/2},
\qquad
y=\frac{b/2}{c/2},
$$
contradicting the minimality of the positive denominator $c$.

:::

:::

::: {.pf-step #s3}

If $x,y\in\QQ$ satisfy
$$
F(x)=F(y),
$$
then
$$
x=y.
$$

::: pf-proof

By step [](#s1){.pf-ref}, either $x=y$ or the pair $(x,y)$ solves
$$
x^2+xy+y^2=2.
$$
Step [](#s2){.pf-ref} excludes the second possibility over $\QQ$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{F:\QQ\to\QQ,\qquad F(x)=x^3-2x}
$$
is injective.

::: pf-proof

Step [](#s3){.pf-ref} is exactly the definition of injectivity.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
