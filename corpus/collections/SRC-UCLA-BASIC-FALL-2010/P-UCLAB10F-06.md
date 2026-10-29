---
schema: qual/card@1
id: P-UCLAB10F-06
kind: problem
title: The inverse of an invertible operator is a polynomial in the operator
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Let $T$ be an invertible linear operator on a finite-dimensional vector space $V$ over a field $F$.
Prove that there exists a polynomial $f\in F[t]$ such that
$$
T^{-1}=f(T).
$$
:::

::: {.solution}

Let
$$
\chi_T(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_1t+c_0
$$
be the characteristic polynomial of $T$, where $n=\dim V$.

::: pf

::: {.pf-step #s1-1}

The constant coefficient $c_0$ is nonzero.


::: pf-proof

Up to the sign convention for the characteristic polynomial,
$$
c_0=(-1)^n\det T.
$$
Since $T$ is invertible,
$$
\det T\ne0.
$$
Hence $c_0\ne0$.

:::

:::

::: {.pf-step #s1-2}

By the Cayley--Hamilton theorem,
$$
T^n+c_{n-1}T^{n-1}+\cdots+c_1T+c_0I=0.
$$


::: pf-proof

The Cayley--Hamilton theorem states that every endomorphism of a finite-dimensional vector space satisfies its characteristic polynomial.

:::

:::

::: {.pf-step #s1-3}

Multiplying the identity in step [](#s1-2){.pf-ref} by $T^{-1}$ gives
$$
T^{n-1}+c_{n-1}T^{n-2}+\cdots+c_2T+c_1I+c_0T^{-1}=0.
$$


::: pf-proof

Since $T$ is invertible, compose every term in step [](#s1-2){.pf-ref} with $T^{-1}$. Powers of the same operator commute, so
$$
T^jT^{-1}=T^{j-1}
$$
for $j\ge1$, while
$$
IT^{-1}=T^{-1}.
$$

:::

:::

::: {.pf-step #s1-4}

Define
$$
f(t)
=
-\frac1{c_0}
\left(
t^{n-1}
+c_{n-1}t^{n-2}
+\cdots
+c_2t
+c_1
\right).
$$
Then
$$
\boxed{T^{-1}=f(T)}.
$$


::: pf-proof

Solve the identity in step [](#s1-3){.pf-ref} for $T^{-1}$:
$$
T^{-1}
=
-\frac1{c_0}
\left(
T^{n-1}
+c_{n-1}T^{n-2}
+\cdots
+c_2T
+c_1I
\right).
$$
This is exactly $f(T)$ for the polynomial defined above. Since $c_0\ne0$ by step [](#s1-1){.pf-ref}, all coefficients lie in the field $F$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required polynomial expression for the inverse.

:::

:::

:::
