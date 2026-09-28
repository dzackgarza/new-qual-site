---
schema: qual/card@1
id: P-BERK78S-03
kind: problem
title: Eigenvectors from column sums and positivity of a two-by-two matrix
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Column sums equal to one make the all-ones vector a left eigenvector of
    A with eigenvalue one; hence A-I is singular and has a nonzero right
    kernel. For a positive 2-by-2 matrix, the characteristic discriminant
    (a-d)^2+4bc is positive, and the larger eigenvalue
    (a+d+sqrt(discriminant))/2 is positive.
---

::: {.problem}
Let $A$ be a real $n\times n$ matrix.

1. If the sum of the entries in each column of $A$ is $1$, prove that there is a nonzero column vector $x$ such that $Ax=x$.
2. Suppose $n=2$ and every entry of $A$ is positive. Prove that there are a nonzero column vector $y$ and a number $\lambda>0$ such that $Ay=\lambda y$.
:::

::: {.solution}
<1>1. Under the hypothesis of part (1), if
$$
\mathbf 1
=
\begin{pmatrix}
1\\
\vdots\\
1
\end{pmatrix},
$$
then
$$
A^T\mathbf 1=\mathbf 1.
$$

::: {.proof}
The $j$th entry of $A^T\mathbf 1$ is the sum of the entries in the $j$th
column of $A$. By hypothesis, every such sum is $1$. Hence every entry of
$A^T\mathbf1$ is $1$.
:::

<1>2. The matrix $A-I$ is singular.

::: {.proof}
Step <1>1 gives
$$
(A^T-I)\mathbf1=0.
$$
Since $\mathbf1\neq0$, the matrix $A^T-I$ is singular. Therefore
$$
0
=
\det(A^T-I)
=
\det((A-I)^T)
=
\det(A-I),
$$
so $A-I$ is singular.
:::

<1>3. There is a nonzero column vector $x$ such that
$$
\boxed{
Ax=x.
}
$$

::: {.proof}
By step <1>2, the kernel of $A-I$ is nonzero. Choose
$$
0\neq x\in\ker(A-I).
$$
Then
$$
(A-I)x=0,
$$
which is equivalent to $Ax=x$.
:::

<1>4. For part (2), write
$$
A
=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
$$
with
$$
a,b,c,d>0.
$$
The characteristic polynomial is
$$
p(\lambda)
=
\lambda^2-(a+d)\lambda+(ad-bc).
$$

::: {.proof}
Directly,
$$
\begin{aligned}
\det(\lambda I-A)
&=
(\lambda-a)(\lambda-d)-bc\\
&=
\lambda^2-(a+d)\lambda+(ad-bc).
\end{aligned}
$$
:::

<1>5. The characteristic polynomial has two distinct real roots
$$
\lambda_\pm
=
\frac{
a+d\pm\sqrt{(a-d)^2+4bc}
}{2}.
$$

::: {.proof}
The discriminant of the polynomial in step <1>4 is
$$
\begin{aligned}
(a+d)^2-4(ad-bc)
&=
a^2-2ad+d^2+4bc\\
&=
(a-d)^2+4bc.
\end{aligned}
$$
Since $b,c>0$, this discriminant is strictly positive. The quadratic
formula gives the displayed roots.
:::

<1>6. The larger root
$$
\lambda_+
=
\frac{
a+d+\sqrt{(a-d)^2+4bc}
}{2}
$$
is strictly positive.

::: {.proof}
Both $a+d$ and the square root are positive, so their sum is positive.
:::

<1>7. There is a nonzero column vector $y$ such that
$$
\boxed{
Ay=\lambda_+y
}
$$
with $\lambda_+>0$.

::: {.proof}
Since $\lambda_+$ is a root of the characteristic polynomial,
$$
\det(A-\lambda_+I)=0.
$$
Thus $A-\lambda_+I$ is singular and has a nonzero kernel vector $y$.
For such a vector,
$$
(A-\lambda_+I)y=0,
$$
so $Ay=\lambda_+y$. Positivity of $\lambda_+$ is step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), and step <1>7 proves part (2).
:::
:::
