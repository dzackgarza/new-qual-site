---
schema: qual/card@1
id: P-TRIV-RA56
kind: problem
title: $\sum_{n\in\mathbb{Z}}\lvert 2n+1\rvert e^{-a\lvert 2n+1\rvert}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 56, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the series $J ( a ) = \sum _ { n = - \infty } ^ { \infty } | 2 n + 1 | e ^ { - a | 2 n + 1 | }$ for $a > 0$
:::

::: pf

::: pf-step

The absolute values
$$
|2n+1|,
\qquad
n\in\mathbb Z,
$$
run through every positive odd integer exactly twice.


::: pf-proof

For $n=0,1,2,\ldots$, one obtains
$$
1,3,5,\ldots.
$$
For $n=-1,-2,-3,\ldots$, one obtains
$$
|-1|,|-3|,|-5|,\ldots
=
1,3,5,\ldots.
$$

:::

:::

::: pf-step

Therefore
$$
J(a)
=
2
\sum_{m=0}^{\infty}
(2m+1)e^{-a(2m+1)}.
$$


::: pf-proof

Group the equal positive and negative odd contributions from step <1>1.

:::

:::

::: pf-step

Put
$$
q=e^{-2a}.
$$
Then
$$
0<q<1
$$
and
$$
J(a)
=
2e^{-a}
\sum_{m=0}^{\infty}(2m+1)q^m.
$$


::: pf-proof

Factor
$$
e^{-a(2m+1)}
=
e^{-a}(e^{-2a})^m
=
e^{-a}q^m
$$
from step <1>2.

:::

:::

::: pf-step

The geometric-series identities are
$$
\sum_{m=0}^{\infty}q^m
=
\frac1{1-q}
$$
and
$$
\sum_{m=0}^{\infty}m q^m
=
\frac{q}{(1-q)^2}.
$$


::: pf-proof

The first is the geometric series. Differentiate it with respect to $q$ and
multiply by $q$ to obtain the second.

:::

:::

::: pf-step

Hence
$$
\sum_{m=0}^{\infty}(2m+1)q^m
=
\frac{1+q}{(1-q)^2}.
$$


::: pf-proof

By step <1>4,
$$
\begin{aligned}
\sum_{m=0}^{\infty}(2m+1)q^m
&=
2\sum_{m=0}^{\infty}m q^m
+
\sum_{m=0}^{\infty}q^m\\
&=
\frac{2q}{(1-q)^2}
+
\frac1{1-q}\\
&=
\frac{1+q}{(1-q)^2}.
\end{aligned}
$$

:::

:::

::: pf-step

Therefore
$$
J(a)
=
2e^{-a}
\frac{1+e^{-2a}}
{(1-e^{-2a})^2}.
$$


::: pf-proof

Substitute step <1>5 into step <1>3 and restore $q=e^{-2a}$.

:::

:::

::: pf-step

Using
$$
1+e^{-2a}
=
2e^{-a}\cosh a
$$
and
$$
1-e^{-2a}
=
2e^{-a}\sinh a,
$$
one obtains
$$
\boxed{
J(a)
=
\frac{\cosh a}{\sinh^2a}.
}
$$


::: pf-proof

Substitute the two hyperbolic identities into step <1>6. The common factor
$4e^{-2a}$ cancels between numerator and denominator.

:::

:::

::: pf-qed

Step <1>7 is the required closed form.

:::

:::
