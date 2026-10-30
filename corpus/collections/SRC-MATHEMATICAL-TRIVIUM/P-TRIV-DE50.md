---
schema: qual/card@1
id: P-TRIV-DE50
kind: problem
title: Radial harmonic functions in $\RR^d$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 50, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider a spherically symmetric potential satisfying the Laplace equation in d dimensions $( d \geq 3 )$ and vanishing at infinity.
Show that this potential can be written as $\textstyle u ( r ) = { \frac { a } { r ^ { b } } }$ , where a is a constant, and find the value of b.
:::

::: {.solution}

Let $u=u(r)$ with $r=\norm{x}$ in $\RR^d$, where $d\geq3$.

::: pf

::: {.pf-step #s1-1}

For $r>0$, the radial Laplacian is
$$
\Delta u=u''(r)+\frac{d-1}{r}u'(r).
$$


::: pf-proof

For a radial function, $\partial_{x_i}u=u'(r)x_i/r$. Differentiating once more and summing over $i=1,\ldots,d$ gives
$$
\sum_i\partial_{x_i}^2u
=u''(r)+\frac{d-1}{r}u'(r).
$$

:::

:::

::: {.pf-step #s1-2}

The harmonicity equation is equivalent to
$$
\frac d{dr}\left(r^{d-1}u'(r)\right)=0.
$$


::: pf-proof

Multiply the equation in step [](#s1-1){.pf-ref} by $r^{d-1}$:
$$
r^{d-1}u''+(d-1)r^{d-2}u'=0.
$$
The left side is the derivative of $r^{d-1}u'$.

:::

:::

::: pf-step

Hence
$$
u(r)=C_0+C_1r^{2-d}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives $r^{d-1}u'=C$, so $u'=Cr^{1-d}$. Since $d\ne2$,
$$
u=C_0+\frac{C}{2-d}r^{2-d}.
$$
Rename the second constant as $C_1$.

:::

:::

::: {.pf-step #s1-4}

Vanishing at infinity forces $C_0=0$, so
$$
\boxed{u(r)=\frac{a}{r^{d-2}}},
\qquad
\boxed{b=d-2}.
$$


::: pf-proof

Because $d\geq3$, $r^{2-d}\to0$ as $r\to\infty$, whereas the constant term tends to $C_0$. Thus $u(r)\to0$ requires $C_0=0$. Writing $C_1=a$ gives the required form and exponent.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives every radial harmonic potential on $r>0$ that vanishes at infinity.

:::

:::

:::
