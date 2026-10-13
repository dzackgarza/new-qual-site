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
Let $A\in M_n(\mathbb C)$.
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

<1>1. Define the real-valued continuous function
\[
h(x)=e^x-1-x-x^2.
\]

::: {.proof}
The exponential function and polynomials are continuous, so their difference is continuous.
:::

<1>2. One has
\[
h(1)=e-3<0.
\]

::: {.proof}
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

<1>3. One has
\[
h(2)=e^2-7>0.
\]

::: {.proof}
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

<1>4. There exists
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

::: {.proof}
By steps <1>1--<1>3, the continuous function $h$ changes sign between $1$ and $2$.
The intermediate value theorem therefore gives
\[
\lambda\in(1,2)
\]
with
\[
h(\lambda)=0.
\]
:::

<1>5. Let
\[
\boxed{A=\lambda I_n}.
\]
Then
\[
A\ne0.
\]

::: {.proof}
Step <1>4 gives
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

<1>6. For this matrix,
\[
e^A=e^\lambda I_n.
\]

::: {.proof}
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

<1>7. One also has
\[
I_n+A+A^2
=
(1+\lambda+\lambda^2)I_n.
\]

::: {.proof}
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

<1>8. Therefore the nonzero matrix $A$ satisfies
\[
\boxed{
e^A=I_n+A+A^2.
}
\]

::: {.proof}
By step <1>4,
\[
e^\lambda
=
1+\lambda+\lambda^2.
\]
Combine steps <1>6--<1>7.
:::

<1>9. Hence the assertion that $A$ must be zero is false.

::: {.proof}
Step <1>5 gives
\[
A\ne0,
\]
while step <1>8 shows that $A$ satisfies the required matrix equation.
Thus $A$ is a counterexample.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 disproves the claim.
:::
:::
