---
schema: qual/card@1
id: E-SMI-8000E-N1
kind: problem
title: Every UFD is integrally closed
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Commutative Algebra
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the UFD-normality statement and rational-root hint with the local 8000e PDF and extraction, normality exercise 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Reduced an integral fraction a/b to coprime terms, cleared a monic integral equation, and used unique factorization to force b to be a unit."
---

::: {.exercise}
Any UFD is normal (integrally closed).

[Hint: look at the proof of the rational root theorem from precalculus.]
:::


::: solution
Let $R$ be a UFD with fraction field $K$, and let
$$
x\in K
$$
be integral over $R$. We show $x\in R$.

<1>1. Write $x$ in lowest terms.
::: proof
Because $R$ is a UFD, write
$$
x=\frac ab
$$
with $a,b\in R$, $b\ne0$, and with $a$ and $b$ having no common irreducible
factor. Equivalently, every common divisor of $a$ and $b$ is a unit.
:::

<1>2. Clear denominators in a monic integral equation.
::: proof
Since $x$ is integral, there are
$$
r_0,\ldots,r_{n-1}\in R
$$
such that
$$
x^n+r_{n-1}x^{n-1}+\cdots+r_1x+r_0=0.
$$
Substitute $x=a/b$ and multiply by $b^n$:
$$
a^n+r_{n-1}a^{n-1}b+\cdots+r_1ab^{n-1}+r_0b^n=0.
$$
Rearranging gives
$$
a^n
=-b\bigl(r_{n-1}a^{n-1}+\cdots+r_1ab^{n-2}+r_0b^{n-1}\bigr).
$$
Thus
$$
b\mid a^n.
$$
:::

<1>3. The denominator $b$ is a unit.
::: proof
If $b$ were a nonunit, it would have an irreducible factor $p$. In a UFD,
every irreducible is prime. Since
$$
p\mid b\mid a^n,
$$
primality gives
$$
p\mid a.
$$
Then $p$ would be a common irreducible factor of $a$ and $b$, contradicting
step <1>1. Therefore $b$ is a unit.
:::

<1>4. Conclude normality.
::: proof
Since $b$ is a unit,
$$
x=a/b\in R.
$$
Thus every element of the fraction field integral over $R$ already belongs to
$R$. Hence
$$
\boxed{R\text{ is integrally closed}.}
$$
:::
:::
