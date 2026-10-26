---
schema: qual/card@1
id: P-KSRING17-086
kind: problem
title: An integral domain algebraic over a subfield is a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 86 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and F a subring of D that is a field.
Show that if each element of D is algebraic over F , then D is a field.
:::

Let
$$
0\ne a\in D.
$$

::: pf

::: pf-step

Since $a$ is algebraic over $F$, there is a nonzero polynomial
$$
f(X)
\in
F[X]
$$
such that
$$
f(a)=0.
$$
Choose such a polynomial of minimal degree.


::: pf-proof

Algebraicity of $a$ over the field $F$ gives at least one nonzero polynomial relation.
The set of degrees of such relations is a nonempty subset of the nonnegative integers, so it has a least element.

:::

:::

::: pf-step

We may assume the chosen polynomial is monic:
$$
f(X)
=
X^n
+
c_{n-1}X^{n-1}
+
\cdots
+
c_1X
+
c_0,
$$
with
$$
c_i\in F.
$$


::: pf-proof

The leading coefficient of the minimal-degree polynomial is a nonzero element of the field $F$, hence a unit.
Multiplying the polynomial by the inverse of its leading coefficient preserves its degree and its set of roots, and makes it monic.

:::

:::

::: pf-step

The constant coefficient
$$
c_0
$$
is nonzero.


::: pf-proof

Suppose
$$
c_0=0.
$$
Then
$$
f(X)
=
X
\left(
X^{n-1}
+
c_{n-1}X^{n-2}
+
\cdots
+
c_1
\right).
$$
Evaluating at $a$ gives
$$
a
\left(
a^{n-1}
+
c_{n-1}a^{n-2}
+
\cdots
+
c_1
\right)
=
0.
$$
Because $D$ is an integral domain and
$$
a\ne0,
$$
the second factor must vanish:
$$
a^{n-1}
+
c_{n-1}a^{n-2}
+
\cdots
+
c_1
=
0.
$$
This is a polynomial relation over $F$ of degree
$$
n-1,
$$
contradicting minimality.
Therefore
$$
c_0\ne0.
$$

:::

:::

::: pf-step

Rearranging
$$
f(a)=0
$$
gives
$$
a
\left(
a^{n-1}
+
c_{n-1}a^{n-2}
+
\cdots
+
c_1
\right)
=
-c_0.
$$


::: pf-proof

Substitute
$$
X=a
$$
in the monic relation from step <1>2 and factor $a$ from all positive-degree terms.

:::

:::

::: pf-step

The element
$$
c_0
$$
is a unit of $D$.


::: pf-proof

By step <1>3,
$$
c_0\ne0.
$$
Since
$$
c_0\in F
$$
and $F$ is a field,
$$
c_0^{-1}\in F.
$$
Because
$$
F\subseteq D,
$$
both
$$
c_0
$$
and
$$
c_0^{-1}
$$
lie in $D$.
Thus $c_0$ is a unit of $D$.

:::

:::

::: pf-step

The element $a$ is a unit of $D$.


::: pf-proof

Multiply the identity in step <1>4 by
$$
-c_0^{-1}.
$$
Then
$$
a
\left[
-c_0^{-1}
\left(
a^{n-1}
+
c_{n-1}a^{n-2}
+
\cdots
+
c_1
\right)
\right]
=
1.
$$
The bracketed element belongs to $D$ because
$$
a\in D
$$
and all
$$
c_i,c_0^{-1}\in F\subseteq D.
$$
Thus $a$ has a multiplicative inverse in $D$.

:::

:::

::: pf-step

Every nonzero element of $D$ is invertible.


::: pf-proof

The nonzero element
$$
a\in D
$$
was arbitrary.
Step <1>6 shows that every such $a$ is a unit.

:::

:::

::: pf-step

Therefore
$$
\boxed{
D\text{ is a field}.
}
$$


::: pf-proof

The ring $D$ is already assumed to be an integral domain, hence a nonzero commutative ring with identity.
Step <1>7 shows that every nonzero element is invertible.
This is exactly the definition of a field.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
