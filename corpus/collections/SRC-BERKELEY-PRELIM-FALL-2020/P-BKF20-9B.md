---
schema: qual/card@1
id: P-BKF20-9B
kind: problem
title: Reducibility of $x^4+n$ in $\mathbb Z[x]$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 classification. A linear
    factor gives n equal to minus a fourth power, hence the -m^2 family;
    comparing coefficients in a monic quadratic factorization gives either
    n=-m^2 or n=4m^4.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked normalization to monic factors, the linear-factor case, the full
    coefficient comparison for two quadratic factors, the parity step forcing
    a=2m, and explicit factorizations for both resulting families.
---

::: {.problem}
For which integers $n$ is
\[
x^4+n
\]
reducible in $\mathbb Z[x]$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If
$$
n=-m^2
$$
for some $m\in\ZZ$, then $x^4+n$ is reducible in $\ZZ[x]$.

::: pf-proof

One has
$$
x^4-m^2
=
(x^2-m)(x^2+m).
$$
Both factors have positive degree, so the polynomial is reducible.

:::

:::

::: {.pf-step #s2}

If
$$
n=4m^4
$$
for some $m\in\ZZ$, then $x^4+n$ is reducible in $\ZZ[x]$.

::: pf-proof

Direct multiplication gives
$$
\begin{aligned}
&(x^2+2mx+2m^2)(x^2-2mx+2m^2)\\
&\qquad=
(x^2+2m^2)^2-(2mx)^2\\
&\qquad=
x^4+4m^4.
\end{aligned}
$$
Thus $x^4+n$ factors nontrivially over $\ZZ$.

:::

:::

::: {.pf-step #s3}

Conversely, suppose $x^4+n$ is reducible in $\ZZ[x]$. Its
factors may be chosen monic.

::: pf-proof

The polynomial $x^4+n$ is monic. In any factorization into
positive-degree integer polynomials, the product of the leading
coefficients is $1$. Hence both leading coefficients are units
$\pm1$; changing both signs if necessary gives monic factors.

:::

:::

::: {.pf-step #s4}

If $x^4+n$ has a linear factor, then
$$
n=-m^2
$$
for some $m\in\ZZ$.

::: pf-proof

A monic linear factor has the form $x-r$ with $r\in\ZZ$, so
$$
r^4+n=0.
$$
Thus
$$
n=-r^4=-(r^2)^2.
$$
Taking $m=r^2$ gives the stated form.

:::

:::

::: {.pf-step #s5}

If $x^4+n$ is reducible and has no linear factor, then it factors
as two monic quadratics
$$
x^4+n
=
(x^2+ax+b)(x^2+cx+d)
$$
with $a,b,c,d\in\ZZ$.

::: pf-proof

By step [](#s3){.pf-ref} the factors may be chosen monic. Their positive degrees
sum to $4$. Since there is no factor of degree $1$, the only possible
degree split is $2+2$, giving the displayed form.

:::

:::

::: {.pf-step #s6}

In the factorization of step [](#s5){.pf-ref},
$$
c=-a
$$
and
$$
a(d-b)=0,
\qquad
b+d-a^2=0,
\qquad
bd=n.
$$

::: pf-proof

Expanding after comparing the coefficient of $x^3$ gives
$$
c=-a
$$
and hence
$$
\begin{aligned}
(x^2+ax+b)(x^2-ax+d)
&=
x^4
+
(b+d-a^2)x^2\\
&\qquad
+
a(d-b)x
+
bd.
\end{aligned}
$$
The coefficients of $x^2$ and $x$ in $x^4+n$ are zero, and its
constant term is $n$, yielding the three equations.

:::

:::

::: {.pf-step #s7}

If $a=0$ in step [](#s6){.pf-ref}, then
$$
n=-m^2
$$
for some $m\in\ZZ$.

::: pf-proof

When $a=0$, the equation
$$
b+d-a^2=0
$$
becomes
$$
d=-b.
$$
Therefore
$$
n=bd=-b^2.
$$
Taking $m=b$ gives the required form.

:::

:::

::: {.pf-step #s8}

If $a\ne0$ in step [](#s6){.pf-ref}, then
$$
n=4m^4
$$
for some $m\in\ZZ$.

::: pf-proof

Since
$$
a(d-b)=0
$$
and $a\ne0$, one has
$$
d=b.
$$
Then
$$
b+d-a^2=0
$$
becomes
$$
2b=a^2.
$$
Thus $a^2$ is even, so $a$ is even. Write
$$
a=2m.
$$
Then
$$
b=\frac{a^2}{2}=2m^2,
$$
and hence
$$
n=bd=b^2=4m^4.
$$

:::

:::

::: {.pf-step #s9}

Therefore
$$
\boxed{
x^4+n\text{ is reducible in }\ZZ[x]
\iff
n=-m^2\text{ or }n=4m^4
\text{ for some }m\in\ZZ.
}
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove that every integer in either displayed family
gives a reducible polynomial. Conversely, if the polynomial is
reducible, step [](#s4){.pf-ref} handles the linear-factor case, while steps
[](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} handle the only remaining factorization type.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref} is the complete classification.

:::

:::

:::
