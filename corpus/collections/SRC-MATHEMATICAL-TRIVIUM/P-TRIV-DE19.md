---
schema: qual/card@1
id: P-TRIV-DE19
kind: problem
title: Power series solution of $x(2-x)y''+3(1-x)y'-y=0$ about $x=1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the general solution of the equation :

$$
x ( 2 - x ) \frac { d ^ { 2 } y } { d x ^ { 2 } } + 3 ( 1 - x ) \frac { d y } { d x } - y = 0\tag{28}
$$

as a power series about $x = 1$
:::

::: {.solution}

Set $s=x-1$ and write
$$
y(s)=\sum_{n=0}^{\infty}a_ns^n.
$$

::: pf

::: {.pf-step #s1-1}

In the variable $s$, the differential equation is
$$
(1-s^2)y''-3sy'-y=0.
$$


::: pf-proof

Since $x=1+s$, one has
$$
x(2-x)=(1+s)(1-s)=1-s^2,
\qquad
1-x=-s,
$$
and differentiation with respect to $x$ is the same as differentiation with respect to $s$.

:::

:::

::: {.pf-step #s1-2}

The power-series coefficients satisfy
$$
(n+2)(n+1)a_{n+2}-(n+1)^2a_n=0,
$$
or equivalently
$$
a_{n+2}=\frac{n+1}{n+2}a_n
\qquad(n\geq0).
$$


::: pf-proof

From the declared series,
$$
y'=\sum_{n=0}^{\infty}(n+1)a_{n+1}s^n,
\qquad
y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}s^n.
$$
Substitution into step [](#s1-1){.pf-ref} shows that the coefficient of $s^n$ is
$$
(n+2)(n+1)a_{n+2}
-\bigl(n(n-1)+3n+1\bigr)a_n.
$$
The expression in parentheses is $(n+1)^2$, which gives the recurrence.

:::

:::

::: {.pf-step #s1-3}

The even coefficients are
$$
a_{2m}=a_0\prod_{j=1}^{m}\frac{2j-1}{2j}
=a_0\frac{(2m)!}{4^m(m!)^2}
\qquad(m\geq0).
$$


::: pf-proof

Apply the recurrence in step [](#s1-2){.pf-ref} successively with $n=0,2,\ldots,2m-2$. This gives the product. Using
$$
(2m)!!=2^m m!,
\qquad
(2m-1)!!=\frac{(2m)!}{2^m m!}
$$
gives the factorial form.

:::

:::

::: {.pf-step #s1-4}

The odd coefficients are
$$
a_{2m+1}=a_1\prod_{j=1}^{m}\frac{2j}{2j+1}
=a_1\frac{(2m)!!}{(2m+1)!!}
\qquad(m\geq0).
$$


::: pf-proof

Apply the recurrence in step [](#s1-2){.pf-ref} successively with $n=1,3,\ldots,2m-1$.

:::

:::

::: {.pf-step #s1-5}

Hence the general power-series solution about $x=1$ is
$$
\boxed{
y(x)=C_0\sum_{m=0}^{\infty}
\frac{(2m)!}{4^m(m!)^2}(x-1)^{2m}
+C_1\sum_{m=0}^{\infty}
\frac{(2m)!!}{(2m+1)!!}(x-1)^{2m+1}}
$$
for $\abs{x-1}<1$.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} determine all coefficients from the two independent initial coefficients $a_0=C_0$ and $a_1=C_1$. The nearest singular points of the differential equation to the expansion point $x=1$ occur at $x=0$ and $x=2$, both at distance $1$, so these power series converge for $\abs{x-1}<1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the two-parameter general solution as a power series about $x=1$.

:::

:::

:::
