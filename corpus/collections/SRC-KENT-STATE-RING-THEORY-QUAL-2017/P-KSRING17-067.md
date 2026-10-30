---
schema: qual/card@1
id: P-KSRING17-067
kind: problem
title: Lifting idempotents modulo a square-zero ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 67 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with $1$ and let $I$ be an ideal of $R$ satisfying $I^{2} = \{0\}$. Show that if $a + I \in R/I$ is an idempotent element of $R/I$, then the coset $a + I$ contains an idempotent element of $R$.
:::

::: {.solution}

Assume
$$
(a+I)^2
=
a+I.
$$

::: pf

::: {.pf-step #s1-1}

The element
$$
\delta
\coloneqq
a^2-a
$$
lies in $I$.


::: pf-proof

The idempotence relation in the quotient gives
$$
a^2+I
=
a+I.
$$
Hence
$$
a^2-a
\in
I.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\delta^2=0.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\delta\in I.
$$
Since
$$
I^2=\{0\},
$$
the product of any two elements of $I$ is zero. In particular,
$$
\delta^2=0.
$$

:::

:::

::: {.pf-step #s1-3}

Define
$$
t
\coloneqq
-(2a-1)\delta.
$$
Then
$$
t\in I.
$$


::: pf-proof

Since
$$
\delta\in I
$$
and $I$ is an ideal,
$$
(2a-1)\delta
\in
I.
$$
Hence also
$$
t\in I.
$$

:::

:::

::: {.pf-step #s1-4}

Set
$$
e
\coloneqq
a+t.
$$
Then
$$
e+I
=
a+I.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
t\in I.
$$
Therefore
$$
e-a=t\in I,
$$
so $e$ and $a$ determine the same coset modulo $I$.

:::

:::

::: {.pf-step #s1-5}

Because
$$
t\in I
$$
and
$$
I^2=0,
$$
one has
$$
t^2=0.
$$


::: pf-proof

This is immediate from the square-zero hypothesis on $I$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
e^2-e
=
\delta+(2a-1)t.
$$


::: pf-proof

Using
$$
e=a+t,
$$
and step [](#s1-5){.pf-ref},
$$
\begin{aligned}
e^2-e
&=
(a+t)^2-(a+t)\\
&=
a^2+2at+t^2-a-t\\
&=
(a^2-a)+(2a-1)t\\
&=
\delta+(2a-1)t.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
(2a-1)^2\delta
=
\delta.
$$


::: pf-proof

Compute
$$
\begin{aligned}
(2a-1)^2
&=
4a^2-4a+1\\
&=
1+4(a^2-a)\\
&=
1+4\delta.
\end{aligned}
$$
Hence
$$
\begin{aligned}
(2a-1)^2\delta
&=
(1+4\delta)\delta\\
&=
\delta+4\delta^2.
\end{aligned}
$$
By step [](#s1-2){.pf-ref},
$$
\delta^2=0,
$$
so
$$
(2a-1)^2\delta
=
\delta.
$$

:::

:::

::: {.pf-step #s1-8}

The element $e$ is idempotent.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
t
=
-(2a-1)\delta.
$$
Substitute this into step [](#s1-6){.pf-ref}:
$$
\begin{aligned}
e^2-e
&=
\delta
-
(2a-1)^2\delta\\
&=
\delta-\delta\\
&=
0,
\end{aligned}
$$
where step [](#s1-7){.pf-ref} is used in the second equality.
Therefore
$$
e^2=e.
$$

:::

:::

::: {.pf-step #s1-9}

Hence the coset
$$
a+I
$$
contains an idempotent element of $R$.


::: pf-proof

Step [](#s1-4){.pf-ref} shows
$$
e+I=a+I,
$$
and step [](#s1-8){.pf-ref} shows that $e$ is idempotent.
Thus
$$
\boxed{
e\in a+I
\text{ and }
e^2=e.
}
$$

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
