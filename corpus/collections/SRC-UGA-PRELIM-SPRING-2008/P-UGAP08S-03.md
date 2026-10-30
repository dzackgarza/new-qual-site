---
schema: qual/card@1
id: P-UGAP08S-03
kind: problem
title: State both parts of the Fundamental Theorem of Calculus
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
State both parts of the Fundamental Theorem of Calculus and outline a proof of one of them.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Fundamental Theorem of Calculus, Part I.**

Let
$$
f:[a,b]\to\RR
$$
be continuous, and define
$$
F(x)
\coloneqq
\int_a^x f(t)\,dt.
$$
Then $F$ is differentiable on
$$
(a,b)
$$
and
$$
\boxed{
F'(x)=f(x).
}
$$


::: pf-proof

This is the first standard form of the theorem.
The proof is given in steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-2}

**Fundamental Theorem of Calculus, Part II.**

Let
$$
f:[a,b]\to\RR
$$
be continuous, and let
$$
G:[a,b]\to\RR
$$
be any differentiable function satisfying
$$
G'(x)=f(x)
$$
for
$$
a<x<b.
$$
Then
$$
\boxed{
\int_a^b f(x)\,dx
=
G(b)-G(a).
}
$$


::: pf-proof

Equivalently, definite integration computes the net change of any
antiderivative.

:::

:::

::: {.pf-step #s1-3}

To prove Part I, fix
$$
x\in(a,b)
$$
and let $h$ be small enough that
$$
x+h\in[a,b].
$$
Then
$$
\frac{F(x+h)-F(x)}{h}
=
\frac1h
\int_x^{x+h}f(t)\,dt.
$$


::: pf-proof

By additivity of the integral,
$$
F(x+h)-F(x)
=
\int_a^{x+h}f
-
\int_a^x f
=
\int_x^{x+h}f.
$$
Divide by $h$.

:::

:::

::: {.pf-step #s1-4}

Subtracting $f(x)$ gives
$$
\frac{F(x+h)-F(x)}{h}
-
f(x)
=
\frac1h
\int_x^{x+h}
\bigl(f(t)-f(x)\bigr)
\,dt.
$$


::: pf-proof

Since
$$
f(x)
=
\frac1h
\int_x^{x+h}f(x)\,dt,
$$
subtract the two averages.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\abs{
\frac{F(x+h)-F(x)}{h}
-
f(x)
}
\le
\sup_{t\text{ between }x\text{ and }x+h}
\abs{f(t)-f(x)}.
$$


::: pf-proof

Using step [](#s1-4){.pf-ref},
$$
\begin{aligned}
\abs{
\frac1h
\int_x^{x+h}
\bigl(f(t)-f(x)\bigr)
\,dt
}
&\le
\frac1{\abs{h}}
\int_{\min(x,x+h)}^{\max(x,x+h)}
\abs{f(t)-f(x)}
\,dt\\
&\le
\sup_{t\text{ between }x\text{ and }x+h}
\abs{f(t)-f(x)}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

Letting
$$
h\to0,
$$
the right-hand side tends to $0$, so
$$
F'(x)=f(x).
$$


::: pf-proof

Continuity of $f$ at $x$ implies
$$
\abs{f(t)-f(x)}
\to
0
$$
uniformly for $t$ confined to a sufficiently small interval around $x$.
Thus the supremum in step [](#s1-5){.pf-ref} tends to $0$ as $h\to0$.
Hence
$$
\lim_{h\to0}
\frac{F(x+h)-F(x)}{h}
=
f(x).
$$

:::

:::

::: pf-step

Part II follows immediately from Part I.


::: pf-proof

Define
$$
F(x)
=
\int_a^x f(t)\,dt.
$$
By Part I,
$$
F'=f.
$$
If $G'=f$ as well, then
$$
(G-F)'=0.
$$
By the Mean Value Theorem,
$$
G-F
$$
is constant.
Since
$$
F(a)=0,
$$
one has
$$
G(x)-F(x)=G(a).
$$
At
$$
x=b,
$$
$$
G(b)-\int_a^b f
=
G(a),
$$
so
$$
\int_a^b f
=
G(b)-G(a).
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} state both parts, and steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} prove Part I.

:::

:::

:::
