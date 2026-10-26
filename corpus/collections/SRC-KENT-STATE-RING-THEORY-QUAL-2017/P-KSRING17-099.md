---
schema: qual/card@1
id: P-KSRING17-099
kind: problem
title: $\mathbb Z[\sqrt{-2}]$ is a Euclidean domain
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 99 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Prove that $\mathbb { Z } [ \sqrt { - 2 } ] = \{ a + b \sqrt { - 2 } \ | \ a , b \in \mathbb { Z } \}$ is a Euclidean domain.
:::

Set
$$
D
\coloneqq
\ZZ[\sqrt{-2}],
$$
and define
$$
N:D\to\ZZ_{\ge0}
$$
by
$$
N(a+b\sqrt{-2})
\coloneqq
a^2+2b^2.
$$

::: pf

::: pf-step

For
$$
\alpha=a+b\sqrt{-2},
$$
one has
$$
N(\alpha)
=
\alpha\overline\alpha,
$$
where
$$
\overline\alpha
\coloneqq
a-b\sqrt{-2}.
$$


::: pf-proof

Direct multiplication gives
$$
\begin{aligned}
\alpha\overline\alpha
&=
(a+b\sqrt{-2})(a-b\sqrt{-2})\\
&=
a^2-b^2(-2)\\
&=
a^2+2b^2\\
&=
N(\alpha).
\end{aligned}
$$

:::

:::

::: pf-step

The norm is multiplicative:
$$
N(\alpha\beta)
=
N(\alpha)N(\beta).
$$


::: pf-proof

Conjugation is multiplicative:
$$
\overline{\alpha\beta}
=
\overline\alpha\,\overline\beta.
$$
Hence, using step <1>1,
$$
\begin{aligned}
N(\alpha\beta)
&=
\alpha\beta\,
\overline{\alpha\beta}\\
&=
\alpha\beta\,
\overline\alpha\,\overline\beta\\
&=
(\alpha\overline\alpha)
(\beta\overline\beta)\\
&=
N(\alpha)N(\beta).
\end{aligned}
$$

:::

:::

::: pf-step

If
$$
\alpha\ne0,
$$
then
$$
N(\alpha)>0.
$$


::: pf-proof

Write
$$
\alpha=a+b\sqrt{-2}.
$$
If
$$
N(\alpha)
=
a^2+2b^2
=
0,
$$
then both nonnegative terms must vanish, so
$$
a=b=0.
$$
Thus
$$
\alpha=0.
$$
Taking the contrapositive proves the claim.

:::

:::

::: pf-step

Let
$$
\alpha,\beta\in D,
\qquad
\beta\ne0.
$$
In the fraction field
$$
\QQ(\sqrt{-2}),
$$
write
$$
\frac{\alpha}{\beta}
=
x+y\sqrt{-2}
$$
with
$$
x,y\in\QQ.
$$


::: pf-proof

The field of fractions of
$$
\ZZ[\sqrt{-2}]
$$
is
$$
\QQ(\sqrt{-2}),
$$
whose elements have exactly this form.

:::

:::

::: pf-step

Choose integers
$$
m,n\in\ZZ
$$
such that
$$
\abs{x-m}\le\frac12,
\qquad
\abs{y-n}\le\frac12.
$$


::: pf-proof

Every real number has an integer within distance at most
$$
\frac12.
$$
Apply this separately to
$$
x
$$
and
$$
y.
$$

:::

:::

::: pf-step

Set
$$
q
\coloneqq
m+n\sqrt{-2}
\in
D.
$$
Then
$$
N\left(
\frac{\alpha}{\beta}-q
\right)
\le
\frac34.
$$


::: pf-proof

One has
$$
\frac{\alpha}{\beta}-q
=
(x-m)+(y-n)\sqrt{-2}.
$$
Therefore
$$
\begin{aligned}
N\left(
\frac{\alpha}{\beta}-q
\right)
&=
(x-m)^2
+
2(y-n)^2\\
&\le
\frac14
+
2\cdot\frac14\\
&=
\frac34.
\end{aligned}
$$

:::

:::

::: pf-step

Define
$$
r
\coloneqq
\alpha-q\beta.
$$
Then
$$
\alpha=q\beta+r
$$
with
$$
r\in D.
$$


::: pf-proof

Because
$$
\alpha,\beta,q\in D
$$
and $D$ is a ring,
$$
r
=
\alpha-q\beta
\in
D.
$$
The displayed division identity is the definition of $r$.

:::

:::

::: pf-step

One has
$$
N(r)
=
N(\beta)
N\left(
\frac{\alpha}{\beta}-q
\right).
$$


::: pf-proof

From step <1>7,
$$
\begin{aligned}
r
&=
\alpha-q\beta\\
&=
\beta
\left(
\frac{\alpha}{\beta}-q
\right).
\end{aligned}
$$
Apply multiplicativity of the norm from step <1>2.

:::

:::

::: pf-step

If
$$
r\ne0,
$$
then
$$
N(r)<N(\beta).
$$


::: pf-proof

By steps <1>6 and <1>8,
$$
N(r)
\le
\frac34
N(\beta).
$$
Because
$$
\beta\ne0,
$$
step <1>3 gives
$$
N(\beta)>0.
$$
Therefore
$$
\frac34N(\beta)
<
N(\beta),
$$
so
$$
N(r)<N(\beta).
$$

:::

:::

::: pf-step

The function
$$
N:D\setminus\{0\}\to\ZZ_{>0}
$$
is a Euclidean function.


::: pf-proof

Given
$$
\alpha,\beta\in D,
\qquad
\beta\ne0,
$$
steps <1>4--<1>7 construct
$$
q,r\in D
$$
such that
$$
\alpha=q\beta+r.
$$
If
$$
r=0,
$$
the Euclidean condition holds.
If
$$
r\ne0,
$$
step <1>9 gives
$$
N(r)<N(\beta).
$$
Thus the division-with-remainder axiom is satisfied.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\ZZ[\sqrt{-2}]
\text{ is a Euclidean domain}.
}
$$


::: pf-proof

The ring
$$
\ZZ[\sqrt{-2}]
$$
is a subring of the field
$$
\QQ(\sqrt{-2}),
$$
so it is an integral domain.
Step <1>10 supplies a Euclidean function.
Hence it is a Euclidean domain.

:::

:::

::: pf-qed

Step <1>11 is the required conclusion.

:::

:::
