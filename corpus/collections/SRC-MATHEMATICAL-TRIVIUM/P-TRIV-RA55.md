---
schema: qual/card@1
id: P-TRIV-RA55
kind: problem
title: Closed form and small-$a$ expansion of $\sum_n ne^{-an}$
classification:
  areas: [real-analysis]
  topics:
  - Series
  - Asymptotic Expansions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 55, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the function $J(a) = \sum_{n=0}^{\infty} ne^{-an}$ defined for positive $a$.

(a) Write an explicit expression for $J(a)$.

(b) Expand $J(a)$ around the point $a = 0$ up to $O(a^0)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Put
$$
q=e^{-a}.
$$
Then
$$
0<q<1
$$
because $a>0$.


::: pf-proof

The exponential of a negative number lies strictly between $0$ and $1$.

:::

:::

::: pf-step

The geometric series gives
$$
\sum_{n=0}^{\infty}q^n
=
\frac1{1-q}.
$$


::: pf-proof

This is the standard geometric-series formula for $\abs{q}<1$.

:::

:::

::: {.pf-step #s1-3}

Differentiating with respect to $q$ gives
$$
\sum_{n=1}^{\infty}nq^{n-1}
=
\frac1{(1-q)^2}.
$$


::: pf-proof

The geometric series converges uniformly on every closed disk $\abs{q}\leq r<1$, so termwise differentiation is valid there.

:::

:::

::: {.pf-step #s1-4}

Multiplying by $q$ gives
$$
\sum_{n=0}^{\infty}nq^n
=
\frac{q}{(1-q)^2}.
$$


::: pf-proof

The $n=0$ term is zero, so multiplying step [](#s1-3){.pf-ref} by $q$ gives the stated series.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
J(a)
=
\frac{e^{-a}}{(1-e^{-a})^2}.
}
$$


::: pf-proof

Substitute $q=e^{-a}$ from step [](#s1-1){.pf-ref} into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Equivalently,
$$
\boxed{
J(a)
=
\frac1{4\sinh^2(a/2)}.
}
$$


::: pf-proof

Since
$$
1-e^{-a}
=
e^{-a/2}
\left(e^{a/2}-e^{-a/2}\right)
=
2e^{-a/2}\sinh(a/2),
$$
one has
$$
(1-e^{-a})^2
=
4e^{-a}\sinh^2(a/2).
$$
Substitute this into step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give two explicit equivalent formulas.

:::

:::

::: {.pf-step #s1-8}

As $a\to0$,
$$
\sinh\frac a2
=
\frac a2
+
\frac{a^3}{48}
+
O(a^5).
$$


::: pf-proof

Use the Taylor series
$$
\sinh z
=
z+\frac{z^3}{3!}+O(z^5)
$$
with $z=a/2$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
4\sinh^2\frac a2
=
a^2
+
\frac{a^4}{12}
+
O(a^6).
$$


::: pf-proof

Square the expansion from step [](#s1-8){.pf-ref}:
$$
\left(
\frac a2+\frac{a^3}{48}+O(a^5)
\right)^2
=
\frac{a^2}{4}
+
\frac{a^4}{48}
+
O(a^6).
$$
Multiply by $4$.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
J(a)
=
\frac1{a^2}
\frac1{1+a^2/12+O(a^4)}.
$$


::: pf-proof

Factor $a^2$ from the denominator in step [](#s1-9){.pf-ref} and use step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Using
$$
\frac1{1+u}
=
1-u+O(u^2),
$$
one obtains
$$
\boxed{
J(a)
=
\frac1{a^2}
-
\frac1{12}
+
O(a^2).
}
$$


::: pf-proof

In step [](#s1-10){.pf-ref}, take
$$
u=\frac{a^2}{12}+O(a^4).
$$
Then
$$
\frac1{1+u}
=
1-\frac{a^2}{12}+O(a^4).
$$
Multiplying by $a^{-2}$ gives the result.

:::

:::

::: {.pf-step #s1-12}

Part (b) follows.


::: pf-proof

Step [](#s1-11){.pf-ref} includes every term through order $a^0$.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-12){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
