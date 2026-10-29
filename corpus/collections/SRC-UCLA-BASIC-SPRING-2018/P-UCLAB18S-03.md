---
schema: qual/card@1
id: P-UCLAB18S-03
kind: problem
title: Complex matrices with $e^A=I+A+A^2$
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $A\in M_n(\CC)$.
Recall that
\[
e^A=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots.
\]
Suppose
\[
e^A=I+A+A^2.
\]
Prove or disprove that $A$ must be the zero matrix.
:::

::: {.solution}

The claim is false.

::: pf

::: {.pf-step #s1-1}

Define the real-valued continuous function
\[
h(x)=e^x-1-x-x^2.
\]


::: pf-proof

The exponential function and polynomials are continuous, so their difference is continuous.

:::

:::

::: {.pf-step #s1-2}

One has
\[
h(1)=e-3<0.
\]


::: pf-proof

The standard estimate
\[
e<3
\]
gives
\[
e-3<0.
\]
For example,
\[
e
=
\sum_{k=0}^{\infty}\frac1{k!}
<
1+1+\sum_{k=2}^{\infty}\frac1{2^{k-1}}
=
3.
\]

:::

:::

::: {.pf-step #s1-3}

One has
\[
h(2)=e^2-7>0.
\]


::: pf-proof

Using the exponential series,
\[
e
>
1+1+\frac12+\frac16
=
\frac83.
\]
Hence
\[
e^2
>
\frac{64}{9}
>
7,
\]
so
\[
e^2-7>0.
\]

:::

:::

::: {.pf-step #s1-4}

There exists
\[
\lambda\in(1,2)
\]
such that
\[
\boxed{
e^\lambda
=
1+\lambda+\lambda^2.
}
\]


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, the continuous function $h$ changes sign between $1$ and $2$.
The intermediate value theorem therefore gives
\[
\lambda\in(1,2)
\]
with
\[
h(\lambda)=0.
\]

:::

:::

::: {.pf-step #s1-5}

Let
\[
\boxed{A=\lambda I_n}.
\]
Then
\[
A\ne0.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} gives
\[
\lambda>1,
\]
so $\lambda$ is nonzero.
Thus the scalar matrix
\[
\lambda I_n
\]
is nonzero.

:::

:::

::: {.pf-step #s1-6}

For this matrix,
\[
e^A=e^\lambda I_n.
\]


::: pf-proof

Using the matrix exponential series,
\[
\begin{aligned}
e^{\lambda I_n}
&=
\sum_{k=0}^{\infty}
\frac{(\lambda I_n)^k}{k!}\\
&=
\left(
\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}
\right)I_n\\
&=
e^\lambda I_n.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-7}

One also has
\[
I_n+A+A^2
=
(1+\lambda+\lambda^2)I_n.
\]


::: pf-proof

Since
\[
A=\lambda I_n,
\]
one has
\[
A^2=\lambda^2I_n.
\]
Add the three scalar multiples of $I_n$.

:::

:::

::: {.pf-step #s1-8}

Therefore the nonzero matrix $A$ satisfies
\[
\boxed{
e^A=I_n+A+A^2.
}
\]


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
e^\lambda
=
1+\lambda+\lambda^2.
\]
Combine steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Hence the assertion that $A$ must be zero is false.


::: pf-proof

Step [](#s1-5){.pf-ref} gives
\[
A\ne0,
\]
while step [](#s1-8){.pf-ref} shows that $A$ satisfies the required matrix equation.
Thus $A$ is a counterexample.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} disproves the claim.

:::

:::

:::
