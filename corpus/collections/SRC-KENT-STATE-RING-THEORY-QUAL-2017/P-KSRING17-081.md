---
schema: qual/card@1
id: P-KSRING17-081
kind: problem
title: $\mathbb Z[\sqrt p]$ is not a UFD when $p\equiv 1 \pmod 4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 81 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if p is a prime such that $p \equiv 1 ( { \bmod { 4 } } )$ , then $\mathbb { Z } [ { \sqrt { p } } ]$ is not a unique factorization domain.
:::

Set
$$
R
\coloneqq
\ZZ[\sqrt p].
$$

::: pf

::: pf-step

Every unique factorization domain is integrally closed in its fraction field.


::: pf-proof

Let
$$
A
$$
be a UFD and let
$$
K=\operatorname{Frac}(A).
$$
Suppose
$$
x\in K
$$
is integral over $A$.
Write
$$
x=\frac ab
$$
with
$$
a,b\in A,
\qquad
b\ne0,
$$
and choose the fraction in lowest terms, meaning that $a$ and $b$ have no common irreducible factor.

Since $x$ is integral, there exist
$$
n\ge1
$$
and
$$
c_0,\ldots,c_{n-1}\in A
$$
such that
$$
x^n
+
c_{n-1}x^{n-1}
+
\cdots
+
c_1x
+
c_0
=
0.
$$
Multiplying by
$$
b^n
$$
gives
$$
a^n
+
c_{n-1}a^{n-1}b
+
\cdots
+
c_1ab^{n-1}
+
c_0b^n
=
0.
$$
Hence
$$
a^n
=
-b
\left(
c_{n-1}a^{n-1}
+
c_{n-2}a^{n-2}b
+
\cdots
+
c_0b^{n-1}
\right).
$$
Thus
$$
b\mid a^n.
$$

If $b$ were not a unit, some irreducible element
$$
\pi
$$
would divide $b$.
Then
$$
\pi\mid a^n.
$$
In a UFD every irreducible is prime, so
$$
\pi\mid a.
$$
This contradicts the choice of $a$ and $b$ with no common irreducible factor.

Therefore
$$
b
$$
is a unit, and hence
$$
x=\frac ab\in A.
$$
Thus every element of the fraction field integral over $A$ already lies in $A$, so $A$ is integrally closed.

:::

:::

::: pf-step

Since
$$
p\equiv1\pmod4,
$$
the integer
$$
\frac{1-p}{4}
$$
lies in $\ZZ$.


::: pf-proof

The congruence
$$
p\equiv1\pmod4
$$
means
$$
4\mid p-1.
$$
Hence
$$
\frac{1-p}{4}
\in
\ZZ.
$$

:::

:::

::: pf-step

Define
$$
\alpha
\coloneqq
\frac{1+\sqrt p}{2}
\in
\operatorname{Frac}(R).
$$
Then $\alpha$ is integral over $R$.


::: pf-proof

Compute
$$
\begin{aligned}
\alpha^2-\alpha
&=
\left(
\frac{1+\sqrt p}{2}
\right)^2
-
\frac{1+\sqrt p}{2}\\
&=
\frac{1+2\sqrt p+p-2-2\sqrt p}{4}\\
&=
\frac{p-1}{4}.
\end{aligned}
$$
Therefore
$$
\alpha^2
-
\alpha
+
\frac{1-p}{4}
=
0.
$$
By step <1>2, the constant coefficient lies in
$$
\ZZ\subseteq R.
$$
Thus $\alpha$ satisfies the monic polynomial
$$
X^2-X+\frac{1-p}{4}
\in
R[X].
$$
Hence $\alpha$ is integral over $R$.

:::

:::

::: pf-step

The element
$$
\alpha
=
\frac{1+\sqrt p}{2}
$$
does not lie in
$$
R=\ZZ[\sqrt p].
$$


::: pf-proof

Suppose, for contradiction, that
$$
\alpha
=
a+b\sqrt p
$$
for integers
$$
a,b.
$$
Then
$$
\frac12
+
\frac12\sqrt p
=
a+b\sqrt p.
$$
Since $p$ is prime, $\sqrt p$ is irrational, so
$$
1
\qquad\text{and}\qquad
\sqrt p
$$
are linearly independent over $\QQ$.
Therefore equality of the two expressions forces
$$
a=\frac12,
\qquad
b=\frac12,
$$
contradicting
$$
a,b\in\ZZ.
$$
Thus
$$
\alpha\notin R.
$$

:::

:::

::: pf-step

The ring $R$ is not integrally closed.


::: pf-proof

Step <1>3 gives an element
$$
\alpha
\in
\operatorname{Frac}(R)
$$
that is integral over $R$, while step <1>4 shows
$$
\alpha\notin R.
$$
This is exactly failure of integral closure.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\ZZ[\sqrt p]
\text{ is not a unique factorization domain}.
}
$$


::: pf-proof

If
$$
R=\ZZ[\sqrt p]
$$
were a UFD, step <1>1 would imply that $R$ is integrally closed.
Step <1>5 shows that it is not.
Therefore $R$ cannot be a UFD.

:::

:::

::: pf-qed

Step <1>6 is the required conclusion.

:::

:::
