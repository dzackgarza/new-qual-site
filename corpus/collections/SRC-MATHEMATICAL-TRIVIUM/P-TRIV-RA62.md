---
schema: qual/card@1
id: P-TRIV-RA62
kind: problem
title: Borwein integrals
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 62, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the integral

$$
I _ { n } = \int _ { - \infty } ^ { \infty } { \frac { d x } { x } } \sin ( x ) \prod _ { k = 1 } ^ { n } \cos \left( { \frac { x } { 2 k + 1 } } \right) .
$$

Show that $I _ { n } = \pi$ for n = 1, 2, 3, 4, 5, 6. Compute $I _ { 7 }$
:::

For
$$
a_k=\frac1{2k+1},
$$
write
$$
S_n=\sum_{k=1}^{n}a_k.
$$

::: pf

::: pf-step

For every real $x$,
$$
\prod_{k=1}^{n}\cos(a_kx)
=
2^{-n}
\sum_{\varepsilon_1,\ldots,\varepsilon_n\in\{\pm1\}}
e^{ix\sum_{k=1}^{n}\varepsilon_k a_k}.
$$


::: pf-proof

Use
$$
\cos(a_kx)
=
\frac12
\left(
e^{ia_kx}+e^{-ia_kx}
\right)
$$
for each factor and expand the product.

:::

:::

::: pf-step

Pairing conjugate terms in step <1>1 gives
$$
\sin x
\prod_{k=1}^{n}\cos(a_kx)
=
2^{-n}
\sum_{\varepsilon\in\{\pm1\}^n}
\sin\left(
\left[
1+\sum_{k=1}^{n}\varepsilon_k a_k
\right]x
\right).
$$


::: pf-proof

Multiply step <1>1 by
$$
\sin x
=
\frac{e^{ix}-e^{-ix}}{2i}.
$$
Equivalently, apply repeatedly the identity
$$
\sin u\cos v
=
\frac12
\bigl(
\sin(u+v)+\sin(u-v)
\bigr).
$$
After $n$ applications, every sign choice
$$
\varepsilon_k=\pm1
$$
appears exactly once.

:::

:::

::: pf-step

For every nonzero real number $b$,
$$
\operatorname{PV}
\int_{-\infty}^{\infty}
\frac{\sin(bx)}x
\,dx
=
\pi\operatorname{sgn}(b).
$$


::: pf-proof

For $b>0$, substitute $u=bx$ to reduce to the Dirichlet integral
$$
\int_{-\infty}^{\infty}
\frac{\sin u}{u}
\,du
=
\pi.
$$
For $b<0$, the substitution changes the sign.

:::

:::

::: pf-step

Hence, provided none of the frequencies
$$
b_\varepsilon
=
1+\sum_{k=1}^{n}\varepsilon_k a_k
$$
vanishes,
$$
I_n
=
\frac{\pi}{2^n}
\sum_{\varepsilon\in\{\pm1\}^n}
\operatorname{sgn}(b_\varepsilon).
$$


::: pf-proof

Substitute step <1>2 into the defining integral and apply step <1>3 to each
finite summand.

:::

:::

::: pf-step

For $n\leq6$,
$$
S_n<1.
$$


::: pf-proof

Since $S_n$ increases with $n$, it suffices to check $n=6$:
$$
S_6
=
\frac13+\frac15+\frac17+\frac19+\frac1{11}+\frac1{13}
=
\frac{43024}{45045}
<1.
$$

:::

:::

::: pf-step

Therefore, for every sign choice and every $n\leq6$,
$$
b_\varepsilon>0.
$$


::: pf-proof

The smallest possible frequency occurs when every sign is $-1$:
$$
b_\varepsilon
\geq
1-S_n.
$$
By step <1>5, this lower bound is positive.

:::

:::

::: pf-step

Consequently,
$$
\boxed{I_n=\pi}
$$
for
$$
n=1,2,3,4,5,6.
$$


::: pf-proof

By step <1>6, every one of the $2^n$ signs in step <1>4 equals $+1$. Thus
$$
I_n
=
\frac\pi{2^n}\cdot2^n
=
\pi.
$$

:::

:::

::: pf-step

For $n=7$,
$$
S_7
=
\frac13+\frac15+\frac17+\frac19+\frac1{11}+\frac1{13}+\frac1{15}
=
\frac{46027}{45045}
>1.
$$


::: pf-proof

Add $1/15$ to the exact value of $S_6$ from step <1>5.

:::

:::

::: pf-step

The all-minus sign choice gives a negative frequency:
$$
b_{(-,ldots,-)}
=
1-S_7
<0.
$$


::: pf-proof

This is immediate from step <1>8.

:::

:::

::: pf-step

Every other sign choice gives a positive frequency.


::: pf-proof

Starting from the all-minus choice, changing any one sign from $-1$ to $+1$
increases the frequency by
$$
2a_k
=
\frac{2}{2k+1}.
$$
The smallest possible increase occurs at $k=7$ and equals
$$
\frac2{15}.
$$
Now
$$
S_7-1
=
\frac{982}{45045}
<
\frac2{15},
$$
so even the smallest one-sign change makes
$$
1-S_7+\frac2{15}>0.
$$
Any additional sign changes only increase the frequency further.

:::

:::

::: pf-step

Thus among the $2^7=128$ sign choices, exactly one contributes $-1$
and the other $127$ contribute $+1$.


::: pf-proof

Step <1>9 gives the unique negative choice, and step <1>10 proves every other
choice is positive.

:::

:::

::: pf-step

Therefore
$$
I_7
=
\frac\pi{128}
\bigl(127-1\bigr)
=
\boxed{\frac{63\pi}{64}}.
$$


::: pf-proof

Apply the sign formula from step <1>4 and use the count from step <1>11.

:::

:::

::: pf-qed

Step <1>7 proves $I_n=\pi$ for $1\leq n\leq6$, and step <1>12 computes
$I_7$.

:::

:::
