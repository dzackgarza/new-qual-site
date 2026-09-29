---
schema: qual/card@1
id: P-BERK85S-05
kind: problem
title: Factorization of $x^4+x^3+x+3$ over $\mathbb F_5$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Checked all five possible roots and then eliminated the only remaining
    reducible degree pattern, a product of two monic quadratics, by comparing
    their constant terms and coefficients over F_5.
---

::: {.problem}
Factor
\[
x^4+x^3+x+3
\]
completely in $\mathbb F_5[x]$.
:::

::: {.solution}
Let
$$
f(x)\coloneqq x^4+x^3+x+3\in\FF_5[x].
$$

::: pf

::: {.pf-step #no-linear-root}
The polynomial $f$ has no root in $\FF_5$.

::: pf-proof
Direct evaluation gives
$$
\begin{aligned}
f(0)&=3, &
f(1)&=1, &
f(2)&=4, &
f(3)&=4, &
f(4)&=2
\end{aligned}
$$
in $\FF_5$. Hence $f$ has no linear factor.
:::

:::

::: {.pf-step #quadratic-factorization-form}
If $f$ were reducible, it would factor as
$$
f(x)=(x^2+ax+b)(x^2+cx+d)
$$
with $a,b,c,d\in\FF_5$.

::: pf-proof
Since $f$ has degree four and has no linear factor by step [](#no-linear-root){.pf-ref}, every
nontrivial factorization has factor degrees $2$ and $2$. Because $f$ is
monic, multiplying the two factors by inverse nonzero constants makes both
quadratic factors monic without changing their product.
:::

:::

::: {.pf-step #no-such-factorization}
No factorization from step [](#quadratic-factorization-form){.pf-ref} exists.

::: pf-proof
Comparing coefficients gives
$$
a+c=1,
\qquad
ac+b+d=0,
\qquad
ad+bc=1,
\qquad
bd=3.
$$
The last equation leaves, up to order, only
$$
\{b,d\}=\{1,3\}
\qquad\text{or}\qquad
\{b,d\}=\{2,4\}.
$$

If $\{b,d\}=\{1,3\}$, then $b+d=4$, so
$$
a+c=1,
\qquad
ac=1.
$$
Thus $a$ and $c$ would be roots of
$$
t^2-t+1.
$$
Its discriminant is
$$
1-4=2,
$$
but the squares in $\FF_5$ are $0$, $1$, and $4$. Hence this case is
impossible.

If $\{b,d\}=\{2,4\}$, then $b+d=1$, so
$$
a+c=1,
\qquad
ac=4.
$$
Thus $a$ and $c$ are roots of $t^2-t+4$, whose discriminant is
$$
1-16=0
$$
in $\FF_5$. Therefore $a=c=3$. But then
$$
ad+bc=3(b+d)=3,
$$
contradicting the required coefficient $ad+bc=1$.
:::

:::

::: {.pf-step #irreducible-boxed}
Therefore
$$
\boxed{f\text{ is irreducible over }\FF_5}.
$$

::: pf-proof
Step [](#no-linear-root){.pf-ref} excludes a linear factor, and step [](#no-such-factorization){.pf-ref} excludes a factorization
into two quadratics. These are all nontrivial degree patterns for a quartic
over a field. Hence $f$ is irreducible, so its complete factorization in
$\FF_5[x]$ is the polynomial itself.
:::

:::

::: pf-qed
Step [](#irreducible-boxed){.pf-ref} gives the complete factorization.
:::

:::
:::
