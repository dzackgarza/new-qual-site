---
schema: qual/card@1
id: P-UCLAB05F-10
kind: problem
title: Nilpotency bounds for square and upper triangular matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
(a) For each $n=2,3,4,\ldots$, is there an $n\times n$ matrix $A$ with
$$
A^{n-1}\ne0
\qquad\text{but}\qquad
A^n=0?
$$
Give an example or a proof of nonexistence.

(b) Is there an $n\times n$ upper triangular matrix $A$ with
$$
A^n\ne0
\qquad\text{but}\qquad
A^{n+1}=0?
$$
Give an example or a proof of nonexistence.
:::

::: {.solution}

For $n\ge2$, let $N\in M_n(\RR)$ be the matrix with ones on the superdiagonal and zeros elsewhere:
$$
N=
\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&0&1\\
0&\cdots&\cdots&0&0
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

For the standard basis $e_1,\ldots,e_n$,
$$
Ne_1=0
\qquad\text{and}\qquad
Ne_j=e_{j-1}
$$
for $2\le j\le n$.


::: pf-proof

The $j$th column of $N$ is $e_{j-1}$ for $j\ge2$, while the first column is zero. Since the $j$th column is $Ne_j$, the formulas follow.

:::

:::

::: {.pf-step #s1-2}

One has
$$
N^n=0
\qquad\text{but}\qquad
N^{n-1}\ne0.
$$


::: pf-proof

By repeated application of step [](#s1-1){.pf-ref},
$$
N^ke_j=
\begin{cases}
e_{j-k},&k<j,\\
0,&k\ge j.
\end{cases}
$$
Thus $N^ne_j=0$ for every $j$, so $N^n=0$. On the other hand,
$$
N^{n-1}e_n=e_1\ne0,
$$
so $N^{n-1}\ne0$.

:::

:::

::: {.pf-step #s1-3}

The answer to part (a) is yes for every $n\ge2$.


::: pf-proof

The matrix $N$ from steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} is an explicit example.

:::

:::

::: {.pf-step #s1-4}

Suppose an $n\times n$ matrix $A$ satisfies
$$
A^{n+1}=0
\qquad\text{and}\qquad
A^n\ne0.
$$
Then there is a vector $v$ for which
$$
A^nv\ne0.
$$


::: pf-proof

If $A^nv=0$ for every vector $v$, then $A^n$ would be the zero operator. This contradicts $A^n\ne0$.

:::

:::

::: {.pf-step #s1-5}

Under the assumptions of step [](#s1-4){.pf-ref}, the vectors
$$
v,Av,A^2v,\ldots,A^nv
$$
are linearly independent.


::: pf-proof

Suppose
$$
\sum_{j=0}^n c_jA^jv=0.
$$
If not all coefficients vanish, let $r$ be the smallest index with $c_r\ne0$. Apply $A^{n-r}$ to the relation. The term with index $r$ becomes
$$
c_rA^nv.
$$
Every term with index $j>r$ becomes
$$
c_jA^{n-r+j}v,
$$
whose exponent is at least $n+1$, so it vanishes because $A^{n+1}=0$. Hence
$$
c_rA^nv=0.
$$
By step [](#s1-4){.pf-ref}, $A^nv\ne0$, so $c_r=0$, a contradiction. Therefore all coefficients are zero.

:::

:::

::: {.pf-step #s1-6}

No $n\times n$ matrix can satisfy
$$
A^n\ne0
\qquad\text{and}\qquad
A^{n+1}=0.
$$


::: pf-proof

If such a matrix existed, step [](#s1-5){.pf-ref} would produce $n+1$ linearly independent vectors in the $n$-dimensional space $\RR^n$, which is impossible.

:::

:::

::: {.pf-step #s1-7}

The answer to part (b) is no.


::: pf-proof

Step [](#s1-6){.pf-ref} rules out such a matrix even without the additional hypothesis that it be upper triangular.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} answers part (a), and step [](#s1-7){.pf-ref} answers part (b).

:::

:::

:::
