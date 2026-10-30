---
schema: qual/card@1
id: P-UMNCP-S11-08B
kind: problem
title: Fundamental theorem of algebra from Rouche theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2011, 8b as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Use Rouché's theorem to prove the fundamental theorem of algebra.
:::

::: {.solution}

Let
$$
p(z)
=
a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0
$$
be a nonconstant complex polynomial, so
$$
n\ge1,
\qquad
a_n\ne0.
$$

::: pf

::: {.pf-step #s1-1}

There exists $R>0$ such that on the circle
$$
\abs{z}=R
$$
one has
$$
\abs{
a_{n-1}z^{n-1}+\cdots+a_0
}
<
\abs{a_nz^n}.
$$


::: pf-proof

For
$$
\abs{z}=R,
$$
the triangle inequality gives
$$
\abs{
a_{n-1}z^{n-1}+\cdots+a_0
}
\le
\sum_{k=0}^{n-1}\abs{a_k}R^k.
$$
Dividing by
$$
\abs{a_n}R^n
$$
gives
$$
\frac{
\sum_{k=0}^{n-1}\abs{a_k}R^k
}{
\abs{a_n}R^n
}
=
\sum_{k=0}^{n-1}
\frac{\abs{a_k}}{\abs{a_n}}
R^{k-n}.
$$
Every exponent
$$
k-n
$$
is negative, so this sum tends to $0$ as $R\to\infty$. Hence for sufficiently large $R$ it is strictly less than $1$, which gives the required inequality.

:::

:::

::: {.pf-step #s1-2}

For such an $R$, the polynomial $p$ and the monomial
$$
a_nz^n
$$
have the same number of zeros in
$$
\abs{z}<R,
$$
counted with multiplicity.


::: pf-proof

Write
$$
p(z)
=
a_nz^n
+
\left(
a_{n-1}z^{n-1}+\cdots+a_0
\right).
$$
The strict inequality from step [](#s1-1){.pf-ref} holds on the boundary circle. Rouché's theorem therefore applies and gives the same zero count inside the circle.

:::

:::

::: {.pf-step #s1-3}

The polynomial $p$ has exactly $n$ zeros in
$$
\abs{z}<R,
$$
counted with multiplicity.


::: pf-proof

The monomial
$$
a_nz^n
$$
has a zero of multiplicity $n$ at
$$
z=0
$$
and no other zeros. By step [](#s1-2){.pf-ref}, $p$ has the same total number of zeros inside the disk.

:::

:::

::: {.pf-step #s1-4}

In particular, every nonconstant complex polynomial has at least one complex zero.


::: pf-proof

Since
$$
n\ge1,
$$
step [](#s1-3){.pf-ref} gives at least one zero of $p$ in
$$
\abs{z}<R.
$$

:::

:::

::: {.pf-step #s1-5}

Repeated factorization gives the full fundamental theorem of algebra:
$$
\boxed{
p(z)
=
a_n
\prod_{j=1}^n
(z-r_j)}
$$
for some
$$
r_1,\ldots,r_n\in\CC,
$$
counted with multiplicity.


::: pf-proof

Step [](#s1-4){.pf-ref} gives one zero
$$
r_1.
$$
Polynomial division then yields
$$
p(z)
=(z-r_1)q_1(z),
$$
where
$$
q_1
$$
has degree
$$
n-1.
$$
If
$$
n-1>0,
$$
apply step [](#s1-4){.pf-ref} to
$$
q_1
$$
and continue. Induction on the degree gives the displayed factorization into $n$ linear factors.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} prove the fundamental theorem of algebra using Rouché's theorem.

:::

:::

:::
