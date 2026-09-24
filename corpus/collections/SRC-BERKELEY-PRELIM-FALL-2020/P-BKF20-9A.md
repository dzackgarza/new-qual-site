---
schema: qual/card@1
id: P-BKF20-9A
kind: problem
title: A cubic with odd linear and constant coefficients has no rational root
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
    Independently checked the retained Fall 2020 mod-2 argument. Since the
    polynomial is monic, any rational root would be an integer; reduction
    modulo 2 would then give a root of x^3+x+1, which has none in F_2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked integrality of a hypothetical rational root, the reduction using
    oddness of a and b, and evaluation at both elements of F_2.
---

::: {.problem}
If $a,b$ are odd integers, prove that
\[
f(x)=x^3+ax+b
\]
has no rational roots.
:::

::: {.solution}
<1>1. Any rational root of $f$ would in fact be an integer.

::: {.proof}
The polynomial
$$
f(x)=x^3+ax+b
$$
is monic with integer coefficients. By the rational root theorem, a
rational root of a monic integer polynomial must be an integer.
:::

<1>2. Modulo $2$, the polynomial $f$ becomes
$$
\overline f(x)=x^3+x+1
$$
in $\FF_2[x]$.

::: {.proof}
Because $a$ and $b$ are odd,
$$
a\equiv1\pmod2,
\qquad
b\equiv1\pmod2.
$$
Reducing every coefficient of $f$ modulo $2$ therefore gives the
displayed polynomial.
:::

<1>3. The polynomial
$$
x^3+x+1
$$
has no root in $\FF_2$.

::: {.proof}
The field $\FF_2$ has only the elements $0$ and $1$. Direct evaluation
gives
$$
0^3+0+1=1
$$
and
$$
1^3+1+1=1
$$
in $\FF_2$. Hence neither element is a root.
:::

<1>4. The polynomial $f$ has no rational root.

::: {.proof}
Suppose $r\in\QQ$ were a root. By step <1>1, $r\in\ZZ$. Reducing the
identity
$$
f(r)=0
$$
modulo $2$ would make the residue class of $r$ a root of
$\overline f$ in $\FF_2$, contradicting step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
