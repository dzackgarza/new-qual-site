---
schema: qual/card@1
id: P-TRIV-DE10
kind: problem
title: Separable rate equation $C'=\alpha(a-C)(b-C)$ with $C(0)=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $C(t)$ when
$$
C'(t) = \alpha(a - C(t))(b - C(t))
$$
if

(a) $a \neq b$

(b) $a = b$

and with $C(0) = 0$.
:::

::: {.solution}

::: pf

::: pf-step

First suppose
$$
a\neq b.
$$
Then the equation is separable:
$$
\frac{dC}{(a-C)(b-C)}
=
\alpha\,dt.
$$


::: pf-proof

Rearrange
$$
C'=alpha(a-C)(b-C).
$$

:::

:::

::: pf-step

The partial-fraction decomposition is
$$
\frac1{(a-C)(b-C)}
=
\frac1{b-a}
\left(
\frac1{a-C}
-
\frac1{b-C}
\right).
$$


::: pf-proof

Combine the right-hand side over the common denominator:
$$
\frac{(b-C)-(a-C)}{(b-a)(a-C)(b-C)}
=
\frac1{(a-C)(b-C)}.
$$

:::

:::

::: {.pf-step #s1-3}

Integration gives
$$
\frac1{b-a}
\log\abs{
\frac{b-C}{a-C}
}
=
\alpha t
+
K.
$$


::: pf-proof

Use
$$
\int\frac{dC}{a-C}
=
-\log\abs{a-C}
$$
and the analogous formula with $b$.

:::

:::

::: pf-step

The initial condition $C(0)=0$ gives
$$
K
=
\frac1{b-a}
\log\abs{\frac ba}
$$
when $ab\neq0$.


::: pf-proof

Set $t=0$ and $C=0$ in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\frac{b-C}{a-C}
=
\frac ba
e^{\alpha(b-a)t}.
$$


::: pf-proof

Subtract the constant from step [](#s1-3){.pf-ref} and exponentiate. On the interval containing the initial point, the sign of the ratio is fixed, so the absolute values may be removed consistently.

:::

:::

::: {.pf-step #s1-6}

Solving for $C$ gives
$$
\boxed{
C(t)
=
\frac{
ab\left(e^{\alpha(b-a)t}-1\right)
}{
b e^{\alpha(b-a)t}-a
}.
}
$$


::: pf-proof

Let
$$
q=e^{\alpha(b-a)t}.
$$
Then step [](#s1-5){.pf-ref} is
$$
a(b-C)=bq(a-C).
$$
Expanding and collecting the terms containing $C$ gives
$$
C(bq-a)=ab(q-1).
$$

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Step [](#s1-6){.pf-ref} gives the solution for $a\neq b$. If $a=0$ or $b=0$, the initial condition $C(0)=0$ gives the equilibrium solution $C\equiv0$, which is also the continuous limiting case of the formula whenever defined.

:::

:::

::: pf-step

Now suppose
$$
a=b.
$$
Then
$$
C'
=
\alpha(a-C)^2.
$$


::: pf-proof

Substitute $b=a$ into the original differential equation.

:::

:::

::: {.pf-step #s1-9}

If $a\neq0$, separation gives
$$
\frac1{a-C}
=
\alpha t
+
\frac1a.
$$


::: pf-proof

Since
$$
\frac d{dC}\frac1{a-C}
=
\frac1{(a-C)^2},
$$
integrating
$$
\frac{dC}{(a-C)^2}
=
\alpha,dt
$$
gives
$$
\frac1{a-C}
=
\alpha t+K.
$$
The initial condition $C(0)=0$ gives $K=1/a$.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
C(t)
=
\frac{\alpha a^2t}{1+\alpha at}.
}
$$


::: pf-proof

Invert step [](#s1-9){.pf-ref}:
$$
a-C
=
\frac{a}{1+\alpha at}.
$$
Subtract from $a$.

:::

:::

::: {.pf-step #s1-11}

If $a=b=0$, then
$$
\boxed{C(t)\equiv0}.
$$


::: pf-proof

The equation becomes
$$
C'=\alpha C^2,
$$
and the initial value $C(0)=0$ yields the equilibrium solution. Uniqueness for this smooth right-hand side forces it to be the only solution through $0$.

:::

:::

::: {.pf-step #s1-12}

Part (b) follows.


::: pf-proof

Steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref} cover the cases $a=b\neq0$ and $a=b=0$.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-12){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
