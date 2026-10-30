---
schema: qual/card@1
id: P-UCLAB16S-11
kind: problem
title: Determinants of a skew-tridiagonal Toeplitz family
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $M_n$ be the tridiagonal $n\times n$ matrix, with $a,b>0$,
$$
M_n=
\begin{pmatrix}
a&b&0&\cdots&0\\
-b&a&b&\ddots&\vdots\\
0&-b&a&\ddots&0\\
\vdots&\ddots&\ddots&\ddots&b\\
0&\cdots&0&-b&a
\end{pmatrix}.
$$
Prove that $\det M_n>0$ for all $n$.
Prove that the limit
$$
\lim_{n\to\infty}\log\det M_n
$$
exists and compute its value.
:::

::: {.solution}

Let
$$
D_n=\det M_n,
\qquad
D_0=1.
$$

::: pf

::: {.pf-step #s1-1}

The determinants satisfy
$$
\boxed{
D_n=aD_{n-1}+b^2D_{n-2}
}
$$
for
$$
n\ge2,
$$
with
$$
D_0=1,
\qquad
D_1=a.
$$


::: pf-proof

Expand $\det M_n$ along the first row.
The contribution from the entry $a$ is
$$
aD_{n-1}.
$$
The contribution from the entry $b$ in position $(1,2)$ is
$$
-b
$$
times the determinant of the corresponding minor.
Expanding that minor along its first column contributes the factor
$$
-b
$$
and leaves $M_{n-2}$.
Thus the second contribution is
$$
(-b)(-b)D_{n-2}
=
b^2D_{n-2}.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{D_n>0}
$$
for every
$$
n\ge0.
$$


::: pf-proof

The initial values satisfy
$$
D_0=1>0,
\qquad
D_1=a>0.
$$
If
$$
D_{n-1}>0
\quad\text{and}\quad
D_{n-2}>0,
$$
then step [](#s1-1){.pf-ref} gives
$$
D_n
=
aD_{n-1}+b^2D_{n-2}
>
0
$$
because
$$
a,b>0.
$$
The claim follows by induction.

:::

:::

::: {.pf-step #s1-3}

Let
$$
r_\pm
=
\frac{
a\pm\sqrt{a^2+4b^2}
}{2}.
$$
Then
$$
r_+>0,
\qquad
r_-<0,
\qquad
\abs{r_-}<r_+.
$$


::: pf-proof

These are the two roots of
$$
r^2-ar-b^2=0.
$$
Since
$$
\sqrt{a^2+4b^2}>a>0,
$$
the numerator defining $r_-$ is negative, so
$$
r_-<0.
$$
Also
$$
r_+
=
\frac{a+\sqrt{a^2+4b^2}}2
>
\frac{\sqrt{a^2+4b^2}-a}{2}
=
\abs{r_-}.
$$

:::

:::

::: {.pf-step #s1-4}

For every
$$
n\ge0,
$$
one has
$$
\boxed{
D_n
=
\frac{
r_+^{n+1}-r_-^{n+1}
}{
r_+-r_-
}.
}
$$


::: pf-proof

The sequence on the right satisfies the recurrence in step [](#s1-1){.pf-ref} because each $r_\pm$ satisfies
$$
r_\pm^2
=
ar_\pm+b^2.
$$
For
$$
n=0,
$$
the formula gives
$$
\frac{r_+-r_-}{r_+-r_-}
=1
=D_0.
$$
For
$$
n=1,
$$
it gives
$$
\frac{r_+^2-r_-^2}{r_+-r_-}
=
r_++r_-
=
a
=
D_1.
$$
The recurrence with two initial values determines the sequence uniquely.

:::

:::

::: {.pf-step #s1-5}

Writing
$$
q=\frac{r_-}{r_+},
$$
one has
$$
\abs{q}<1
$$
and
$$
\boxed{
D_n
=
\frac{
r_+^{n+1}
}{
r_+-r_-
}
\left(
1-q^{n+1}
\right).
}
$$


::: pf-proof

The inequality
$$
\abs{q}<1
$$
is step [](#s1-3){.pf-ref}.
Factor
$$
r_+^{n+1}
$$
from the numerator in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Consequently,
$$
\log D_n
=
(n+1)\log r_+
-
\log(r_+-r_-)
+
\log(1-q^{n+1}).
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
D_n>0,
$$
so its logarithm is defined.
In step [](#s1-5){.pf-ref}, one has
$$
r_+-r_->0
$$
and
$$
1-q^{n+1}>0
$$
because
$$
\abs{q}<1.
$$
Taking logarithms gives the identity.

:::

:::

::: {.pf-step #s1-7}

If
$$
r_+>1,
$$
then
$$
\log D_n\to+\infty.
$$


::: pf-proof

In step [](#s1-6){.pf-ref},
$$
(n+1)\log r_+\to+\infty.
$$
The term
$$
-\log(r_+-r_-)
$$
is constant, while
$$
\log(1-q^{n+1})\to0
$$
because
$$
q^{n+1}\to0.
$$

:::

:::

::: {.pf-step #s1-8}

If
$$
0<r_+<1,
$$
then
$$
\log D_n\to-\infty.
$$


::: pf-proof

Now
$$
\log r_+<0,
$$
so the linear term
$$
(n+1)\log r_+
$$
tends to $-\infty$.
The remaining terms in step [](#s1-6){.pf-ref} stay bounded.

:::

:::

::: {.pf-step #s1-9}

If
$$
r_+=1,
$$
then
$$
\boxed{
\log D_n
\longrightarrow
-
\log(1+b^2).
}
$$


::: pf-proof

Since
$$
r_+r_-=-b^2,
$$
the condition
$$
r_+=1
$$
gives
$$
r_-=-b^2.
$$
Then step [](#s1-4){.pf-ref} gives
$$
D_n
=
\frac{
1-(-b^2)^{n+1}
}{
1+b^2
}.
$$
Because step [](#s1-3){.pf-ref} gives
$$
\abs{r_-}=b^2<1,
$$
the numerator tends to $1$.
Thus
$$
D_n\to\frac1{1+b^2},
$$
and taking logarithms gives the displayed limit.

:::

:::

::: {.pf-step #s1-10}

The condition
$$
r_+=1
$$
is equivalent to
$$
\boxed{a+b^2=1}.
$$


::: pf-proof

The number $r_+=1$ is a root of the characteristic equation
$$
r^2-ar-b^2=0
$$
exactly when
$$
1-a-b^2=0.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore the literal source claim of a finite real limit is false in general.


::: pf-proof

For example, if
$$
a=b=1,
$$
then
$$
r_+
=
\frac{1+\sqrt5}{2}
>
1.
$$
By step [](#s1-7){.pf-ref},
$$
\log\det M_n\to+\infty.
$$
Thus the unnormalized logarithm does not always converge to a finite real number.
The complete extended-real behavior is:
$$
\boxed{
\log\det M_n\to
\begin{cases}
+\infty,&r_+>1,\\
-\log(1+b^2),&r_+=1,\\
-\infty,&0<r_+<1.
\end{cases}
}
$$

:::

:::

::: {.pf-step #s1-12}

The natural normalized statement is
$$
\boxed{
\lim_{n\to\infty}
\frac1n\log\det M_n
=
\log
\left(
\frac{
a+\sqrt{a^2+4b^2}
}{2}
\right).
}
$$


::: pf-proof

Divide the identity in step [](#s1-6){.pf-ref} by $n$.
Then
$$
\frac{n+1}{n}\log r_+
\to
\log r_+,
$$
while the constant term divided by $n$ tends to $0$, and
$$
\frac1n\log(1-q^{n+1})\to0.
$$
Substitute the definition of $r_+$ from step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves positivity of every determinant.
Steps [](#s1-7){.pf-ref} through [](#s1-11){.pf-ref} give the correct disposition of the literal logarithmic limit, and step [](#s1-12){.pf-ref} records the finite normalized limit naturally associated to the problem.

:::

:::

:::
