---
schema: qual/card@1
id: P-TRIV-CA08
kind: problem
title: Laurent series of $1/((z+1)(z+2))$ on its annuli of convergence
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
OFind the Laurent series of $\begin{array} { r } { f ( z ) = \frac { 1 } { ( z + 1 ) ( z + 2 ) } } \end{array}$ such that it converges in the regions (a) $| z | < 1 ;$

(b) $1 < | z | < 2 ;$

(c) $| z | > 2 ;$

(d) $0 < | z + 1 | < 1 .$
:::

::: pf

::: pf-step

The partial-fraction decomposition is
$$
f(z)
=
\frac1{z+1}
-
\frac1{z+2}.
$$


::: pf-proof

One has
$$
\frac1{z+1}
-
\frac1{z+2}
=
\frac{(z+2)-(z+1)}{(z+1)(z+2)}
=
\frac1{(z+1)(z+2)}.
$$

:::

:::

::: pf-step

For $|z|<1$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}(-1)^n z^n
$$
and
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
$$


::: pf-proof

Use
$$
\frac1{1+z}
=
\sum_{n=0}^{\infty}(-z)^n,
$$
valid for $|z|<1$, and
$$
\frac1{z+2}
=
\frac12\frac1{1+z/2}
=
\frac12
\sum_{n=0}^{\infty}
\left(-\frac z2\right)^n,
$$
valid for $|z|<2$.

:::

:::

::: pf-step

Therefore, for $|z|<1$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n
\left(
1-\frac1{2^{n+1}}
\right)z^n.
}
$$


::: pf-proof

Subtract the two series in step <1>2 using step <1>1.

:::

:::

::: pf-step

For $1<|z|<2$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1},
$$
while
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
$$


::: pf-proof

For the first term,
$$
\frac1{z+1}
=
\frac1z\frac1{1+1/z}
=
\frac1z
\sum_{n=0}^{\infty}
\left(-\frac1z\right)^n,
$$
which converges when $|z|>1$.

The second expansion is the one from step <1>2 and converges when $|z|<2$.
Thus both are valid simultaneously on $1<|z|<2$.

:::

:::

::: pf-step

Hence, for $1<|z|<2$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1}
-
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
}
$$


::: pf-proof

Substitute step <1>4 into the partial fractions from step <1>1.

:::

:::

::: pf-step

For $|z|>2$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1},
$$
and
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
(-2)^n z^{-n-1}.
$$


::: pf-proof

The first series is from step <1>4. For the second,
$$
\frac1{z+2}
=
\frac1z\frac1{1+2/z}
=
\frac1z
\sum_{n=0}^{\infty}
\left(-\frac2z\right)^n,
$$
which converges for $|z|>2$.

:::

:::

::: pf-step

Therefore, for $|z|>2$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
\bigl((-1)^n-(-2)^n\bigr)
z^{-n-1}.
}
$$


::: pf-proof

Subtract the two negative-power series in step <1>6.

:::

:::

::: pf-step

For part (d), set
$$
w=z+1.
$$
Then
$$
f(z)
=
\frac1{w(w+1)}.
$$


::: pf-proof

Since
$$
z+1=w
\qquad\text{and}\qquad
z+2=w+1,
$$
the displayed identity follows.

:::

:::

::: pf-step

For $0<|z+1|<1$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n(z+1)^{n-1}.
}
$$


::: pf-proof

By step <1>8,
$$
f(z)
=
\frac1w\frac1{1+w}.
$$
For $|w|<1$,
$$
\frac1{1+w}
=
\sum_{n=0}^{\infty}(-1)^n w^n.
$$
Multiplying by $w^{-1}$ gives the stated Laurent series. The point $w=0$
must be excluded because it is a pole.

:::

:::

::: pf-qed

Steps <1>3, <1>5, <1>7, and <1>9 give the requested Laurent series on all
four regions.

:::

:::
