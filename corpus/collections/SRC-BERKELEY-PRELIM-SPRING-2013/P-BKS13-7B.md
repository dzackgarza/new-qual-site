---
schema: qual/card@1
id: P-BKS13-7B
kind: problem
title: Cayley transform between orthogonal and skew-symmetric matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared all three parts with page 5 of the retained Spring 2013 solution PDF and independently reviewed the Cayley-transform identities.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked invertibility of I+A and I+S, skew-symmetry and orthogonality, exclusion of eigenvalue -1, and mutual inverseness of the transforms.
---

::: {.problem}
Prove the following three statements about real $n\times n$ matrices.

1. If $A$ is an orthogonal matrix whose eigenvalues are all different from $-1$, then $I+A$ is nonsingular and
$$
S=(I-A)(I+A)^{-1}
$$
is skew-symmetric.
2. If $S$ is a skew-symmetric matrix, then
$$
A=(I-S)(I+S)^{-1}
$$
is an orthogonal matrix with no eigenvalue equal to $-1$.
3. The correspondence (called the Cayley transform) $A\leftrightarrow S$ from Parts 1 and 2 is one-to-one.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Under the hypotheses of part 1, the matrix $I+A$ is nonsingular.

::: pf-proof

If $I+A$ were singular, there would be a nonzero vector $v$ with
$$
(I+A)v=0.
$$
Then
$$
Av=-v,
$$
so $-1$ would be an eigenvalue of $A$, contrary to the hypothesis.

:::

:::

::: {.pf-step #s2}

For
$$
S=(I-A)(I+A)^{-1},
$$
one has
$$
S^T=-S.
$$

::: pf-proof

Since $A$ is orthogonal,
$$
A^T=A^{-1}.
$$
Therefore
$$
\begin{aligned}
S^T
&=
(I+A^T)^{-1}(I-A^T)\\
&=
(I+A^{-1})^{-1}(I-A^{-1}).
\end{aligned}
$$
Now
$$
I+A^{-1}
=
A^{-1}(A+I),
$$
so
$$
(I+A^{-1})^{-1}
=
(A+I)^{-1}A.
$$
Also
$$
I-A^{-1}
=
A^{-1}(A-I).
$$
Hence
$$
\begin{aligned}
S^T
&=
(A+I)^{-1}(A-I)\\
&=
-(I+A)^{-1}(I-A).
\end{aligned}
$$
The matrices $I+A$ and $I-A$ commute because both are polynomials in
$A$. Thus
$$
S^T
=
-(I-A)(I+A)^{-1}
=
-S.
$$
This proves part 1.

:::

:::

::: {.pf-step #s3}

If $S$ is skew-symmetric, then $I+S$ is nonsingular.

::: pf-proof

Suppose
$$
(I+S)v=0.
$$
Then
$$
Sv=-v.
$$
Because $S^T=-S$,
$$
v^TSv
=
(v^TSv)^T
=
v^TS^Tv
=
-v^TSv,
$$
so
$$
v^TSv=0.
$$
But $Sv=-v$ also gives
$$
v^TSv=-v^Tv.
$$
Hence
$$
v^Tv=0,
$$
which over $\RR$ implies $v=0$. Therefore the kernel of $I+S$ is
trivial.

:::

:::

::: {.pf-step #s4}

For
$$
A=(I-S)(I+S)^{-1},
$$
one has
$$
A^TA=I.
$$

::: pf-proof

Using $S^T=-S$,
$$
\begin{aligned}
A^T
&=
(I+S^T)^{-1}(I-S^T)\\
&=
(I-S)^{-1}(I+S).
\end{aligned}
$$
Therefore
$$
\begin{aligned}
A^TA
&=
(I-S)^{-1}(I+S)(I-S)(I+S)^{-1}\\
&=
I,
\end{aligned}
$$
because $I+S$ and $I-S$ commute. Thus $A$ is orthogonal.

:::

:::

::: {.pf-step #s5}

The matrix $A$ from step [](#s4){.pf-ref} has no eigenvalue equal to $-1$.

::: pf-proof

Compute
$$
\begin{aligned}
I+A
&=
I+(I-S)(I+S)^{-1}\\
&=
\bigl((I+S)+(I-S)\bigr)(I+S)^{-1}\\
&=
2(I+S)^{-1}.
\end{aligned}
$$
Step [](#s3){.pf-ref} shows that $I+S$ is invertible, so $I+A$ is invertible.
Therefore $-1$ is not an eigenvalue of $A$. This completes part 2.

:::

:::

::: {.pf-step #s6}

Starting from an orthogonal $A$ as in part 1, applying the second
formula to its Cayley transform recovers $A$.

::: pf-proof

Let
$$
S=(I-A)(I+A)^{-1}.
$$
Then
$$
\begin{aligned}
I-S
&=
\bigl((I+A)-(I-A)\bigr)(I+A)^{-1}\\
&=
2A(I+A)^{-1},
\end{aligned}
$$
while
$$
\begin{aligned}
I+S
&=
\bigl((I+A)+(I-A)\bigr)(I+A)^{-1}\\
&=
2(I+A)^{-1}.
\end{aligned}
$$
Consequently
$$
(I-S)(I+S)^{-1}
=
A.
$$

:::

:::

::: {.pf-step #s7}

Starting from a skew-symmetric $S$, applying the first formula to
the matrix $A$ from part 2 recovers $S$.

::: pf-proof

Let
$$
A=(I-S)(I+S)^{-1}.
$$
Then
$$
I-A
=
2S(I+S)^{-1}
$$
and
$$
I+A
=
2(I+S)^{-1}.
$$
Therefore
$$
(I-A)(I+A)^{-1}
=
S.
$$

:::

:::

::: {.pf-step #s8}

The two Cayley-transform formulas define inverse bijections between
the matrices in parts 1 and 2.

::: pf-proof

Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} show that each transformation undoes the other.
Hence the correspondence is one-to-one, and indeed bijective between the
two stated classes of matrices.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part 1, steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part 2, and step
[](#s8){.pf-ref} proves part 3.

:::

:::

:::
