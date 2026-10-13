---
schema: qual/card@1
id: P-UCLAB12W-09
kind: problem
title: Matrix recurrence and exponential growth rate
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let
\[
a_1=1,\qquad a_2=4,\qquad a_{n+2}=4a_{n+1}-3a_n\quad(n\ge1).
\]
Find a $2\times2$ matrix $A$ such that
\[
A^n\binom10=\binom{a_{n+1}}{a_n}
\]
for all $n\ge1$.
Compute the eigenvalues of $A$ and use them to determine
\[
\lim_{n\to\infty}a_n^{1/n}.
\]
:::

::: {.solution}
<1>1. Define
$$
A=
\begin{pmatrix}
4&-3\\
1&0
\end{pmatrix}.
$$
Then for every $n\ge1$,
$$
A\binom{a_{n+1}}{a_n}
=
\binom{a_{n+2}}{a_{n+1}}.
$$

::: {.proof}
By the recurrence,
$$
4a_{n+1}-3a_n=a_{n+2}.
$$
Therefore
$$
A\binom{a_{n+1}}{a_n}
=
\binom{4a_{n+1}-3a_n}{a_{n+1}}
=
\binom{a_{n+2}}{a_{n+1}}.
$$
:::

<1>2. For every $n\ge1$,
$$
A^n\binom10
=
\binom{a_{n+1}}{a_n}.
$$

::: {.proof}
For $n=1$,
$$
A\binom10
=
\binom41
=
\binom{a_2}{a_1}.
$$
If the identity holds for some $n$, then step <1>1 gives
$$
A^{n+1}\binom10
=A\binom{a_{n+1}}{a_n}
=
\binom{a_{n+2}}{a_{n+1}}.
$$
Thus the claim follows by induction.
:::

<1>3. The eigenvalues of $A$ are
$$
\boxed{1\text{ and }3}.
$$

::: {.proof}
The characteristic polynomial is
$$
\det(\lambda I-A)
=
\det
\begin{pmatrix}
\lambda-4&3\\
-1&\lambda
\end{pmatrix}
=
\lambda^2-4\lambda+3
=(\lambda-1)(\lambda-3).
$$
:::

<1>4. The recurrence has the closed form
$$
\boxed{a_n=\frac{3^n-1}{2}}.
$$

::: {.proof}
Because the characteristic roots of the recurrence are the distinct numbers $1$ and $3$ from step <1>3, every sequence satisfying the recurrence has the form
$$
a_n=c_1+c_2 3^n.
$$
Using $a_1=1$ and $a_2=4$ gives
$$
c_1+3c_2=1,
\qquad
c_1+9c_2=4.
$$
Subtracting yields $6c_2=3$, so $c_2=1/2$ and then $c_1=-1/2$.
:::

<1>5. One has
$$
\boxed{\lim_{n\to\infty}a_n^{1/n}=3}.
$$

::: {.proof}
By step <1>4,
$$
a_n
=
\frac{3^n-1}{2}
=
3^n\frac{1-3^{-n}}2.
$$
Hence
$$
a_n^{1/n}
=3\left(\frac{1-3^{-n}}2\right)^{1/n}.
$$
The factor in parentheses tends to $1/2>0$, so its $n$-th root tends to $1$. Therefore the limit is $3$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 gives the required matrix identity, step <1>3 computes the eigenvalues, and step <1>5 gives the requested limit.
:::
:::
