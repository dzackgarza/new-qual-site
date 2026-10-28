---
schema: qual/card@1
id: P-KSRING17-078
kind: problem
title: Ideals with principal product in a domain are finitely generated
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 78 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Suppose R is a domain and I and J are ideals of R such that IJ is principal.
Show that I (and by symmetry J) is finitely generated.

[Hint: If $I J = ( a )$ , then $a = \sum _ { i = 1 } ^ { n } x _ { i } y _ { i }$ for some $x _ { i } \in I$ and $y _ { i } \in J$ . Show the $x _ { i }$ generate I.]
:::

::: {.remark}
Erratum: the statement needs the principal product to be nonzero.
If $J=(0)$, then $IJ=(0)$ is principal while $I$ may be a non-finitely-generated ideal of a non-Noetherian domain.
The intended hypothesis is
$$
IJ=(a)
\qquad\text{with}\qquad
a\ne0.
$$
:::

::: {.solution}

Assume
$$
IJ=(a)
$$
with
$$
a\ne0.
$$

::: pf

::: {.pf-step #s1-1}

There exist finitely many elements
$$
x_1,\ldots,x_n\in I
$$
and
$$
y_1,\ldots,y_n\in J
$$
such that
$$
a
=
\sum_{i=1}^{n}x_i y_i.
$$


::: pf-proof

By definition, the product ideal
$$
IJ
$$
consists of finite sums of products
$$
xy
$$
with
$$
x\in I,
\qquad
y\in J.
$$
Since
$$
a\in(a)=IJ,
$$
such a finite representation exists.

:::

:::

::: {.pf-step #s1-2}

Let
$$
x\in I.
$$
For each
$$
i=1,\ldots,n,
$$
there exists
$$
r_i\in R
$$
such that
$$
xy_i
=
ar_i.
$$


::: pf-proof

Because
$$
x\in I
$$
and
$$
y_i\in J,
$$
their product
$$
xy_i
$$
lies in
$$
IJ=(a).
$$
Hence
$$
xy_i
=
ar_i
$$
for some
$$
r_i\in R.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
ax
=
a
\sum_{i=1}^{n}x_i r_i.
$$


::: pf-proof

Multiply the identity from step [](#s1-1){.pf-ref} by $x$:
$$
\begin{aligned}
ax
&=
x
\sum_{i=1}^{n}x_i y_i\\
&=
\sum_{i=1}^{n}x_i(xy_i).
\end{aligned}
$$
By step [](#s1-2){.pf-ref},
$$
xy_i
=
ar_i.
$$
Therefore
$$
\begin{aligned}
ax
&=
\sum_{i=1}^{n}x_i(ar_i)\\
&=
a
\sum_{i=1}^{n}x_i r_i,
\end{aligned}
$$
using commutativity of $R$.

:::

:::

::: {.pf-step #s1-4}

Since $R$ is a domain and
$$
a\ne0,
$$
one may cancel $a$ in step [](#s1-3){.pf-ref}, obtaining
$$
x
=
\sum_{i=1}^{n}x_i r_i.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
a
\left(
x-\sum_{i=1}^{n}x_i r_i
\right)
=
0.
$$
Because $R$ is an integral domain and
$$
a\ne0,
$$
the second factor must vanish.
Hence
$$
x
=
\sum_{i=1}^{n}x_i r_i.
$$

:::

:::

::: {.pf-step #s1-5}

The elements
$$
x_1,\ldots,x_n
$$
generate $I$.


::: pf-proof

Each
$$
x_i
$$
lies in $I$, so
$$
(x_1,\ldots,x_n)
\subseteq
I.
$$
Conversely, let
$$
x\in I.
$$
Step [](#s1-4){.pf-ref} expresses $x$ as an $R$-linear combination of the $x_i$.
Thus
$$
x\in(x_1,\ldots,x_n).
$$
Hence
$$
I
=
(x_1,\ldots,x_n).
$$
Therefore $I$ is finitely generated.

:::

:::

::: {.pf-step #s1-6}

By symmetry, $J$ is finitely generated.


::: pf-proof

Interchange the roles of
$$
I
$$
and
$$
J.
$$
The same representation from step [](#s1-1){.pf-ref} and the same cancellation argument show that the finitely many elements
$$
y_1,\ldots,y_n
$$
generate $J$.

:::

:::

::: {.pf-step #s1-7}

Therefore, under the corrected nonzero-product hypothesis,
$$
\boxed{
I\text{ and }J\text{ are finitely generated}.
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} proves the assertion for $I$, and step [](#s1-6){.pf-ref} proves it for $J$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the intended conclusion.

:::

:::

:::
