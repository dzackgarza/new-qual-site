---
schema: qual/card@1
id: P-KSRING17-107
kind: problem
title: 'UFDs are integrally closed: rational roots of monic polynomials'
classification:
  areas: [algebra]
  topics:
  - Unique Factorization Domains
  - Integrally Closed Domains
  - Rational Root Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 107 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a unique factorization domain and F its field of fractions.
Prove that if $f ( x )$ is a monic polynomial in $D [ x ]$ and $\alpha \in F$ is a root of $f ,$ then $\alpha \in D$ .
:::

::: {.solution}

Let
$$
f(x)
=
x^n
+
c_{n-1}x^{n-1}
+
\cdots
+
c_1x
+
c_0
\in
D[x]
$$
be monic, and suppose
$$
f(\alpha)=0
$$
for
$$
\alpha\in F.
$$

::: pf

::: {.pf-step #s1-1}

Write
$$
\alpha=\frac ab
$$
with
$$
a,b\in D,
\qquad
b\ne0,
$$
such that $a$ and $b$ have no common irreducible factor.


::: pf-proof

Every element of the fraction field has a representation
$$
a/b.
$$
Because $D$ is a UFD, common irreducible factors of numerator and denominator can be cancelled.
Thus one may choose a lowest-terms representation.

:::

:::

::: {.pf-step #s1-2}

Substituting
$$
\alpha=a/b
$$
into
$$
f(\alpha)=0
$$
and multiplying by
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


::: pf-proof

This is obtained by clearing denominators in the monic polynomial relation.

:::

:::

::: {.pf-step #s1-3}

The relation in step [](#s1-2){.pf-ref} implies
$$
b\mid a^n.
$$


::: pf-proof

Rearrange:
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
The right-hand side is divisible by $b$.
Hence
$$
b\mid a^n.
$$

:::

:::

::: {.pf-step #s1-4}

Suppose $b$ is not a unit.
Then some irreducible element
$$
\pi
$$
divides $b$.


::: pf-proof

In a UFD, every nonzero nonunit factors into irreducibles.
Thus a nonunit denominator has at least one irreducible divisor.

:::

:::

::: {.pf-step #s1-5}

The irreducible element $\pi$ from step [](#s1-4){.pf-ref} is prime.


::: pf-proof

In a UFD, every irreducible element is prime.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\pi\mid a.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\pi\mid b.
$$
By step [](#s1-3){.pf-ref},
$$
b\mid a^n.
$$
Hence
$$
\pi\mid a^n.
$$
Since $\pi$ is prime by step [](#s1-5){.pf-ref}, repeated application of the prime-divisibility property to
$$
a^n=a\cdots a
$$
gives
$$
\pi\mid a.
$$

:::

:::

::: pf-step

The assumption that $b$ is a nonunit contradicts the lowest-terms choice of $a/b$.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref} show that the irreducible element $\pi$ divides both
$$
a
\qquad\text{and}\qquad
b.
$$
This contradicts step [](#s1-1){.pf-ref}.
Therefore
$$
b
$$
must be a unit.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\alpha\in D.
$$


::: pf-proof

Since
$$
b\in D^\times,
$$
one has
$$
b^{-1}\in D.
$$
Therefore
$$
\alpha
=
ab^{-1}
\in
D.
$$
Thus
$$
\boxed{\alpha\in D.}
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
