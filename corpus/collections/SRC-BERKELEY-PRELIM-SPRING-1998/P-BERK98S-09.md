---
schema: qual/card@1
id: P-BERK98S-09
kind: problem
title: Growth and decay of powers of three real $2\times2$ matrices
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
  note: The retained PDF page was inspected directly; M_3 has upper-right entry 6.9, and the source wording asks whether the power sequences are bounded away from infinity and from zero.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
\[
M_1=\begin{pmatrix}3&2\\1&4\end{pmatrix},\qquad
M_2=\begin{pmatrix}5&7\\-3&-4\end{pmatrix},\qquad
M_3=\begin{pmatrix}5&6.9\\-3&-4\end{pmatrix}.
\]
For which, if any, $i\in\{1,2,3\}$ is the sequence $(M_i^n)$ bounded away from $\infty$? For which $i$ is the sequence bounded away from $0$?
:::

::: {.solution}
Fix any matrix norm. We prove that
$$
\norm{M_1^n}\longrightarrow\infty,
\qquad
(M_2^n)\text{ is periodic and never zero},
\qquad
M_3^n\longrightarrow0.
$$

<1>1. The eigenvalues of $M_1$ are $5$ and $2$.

::: {.proof}
Its characteristic polynomial is
$$
\det(\lambda I-M_1)
=
\lambda^2-7\lambda+10
=(\lambda-5)(\lambda-2).
$$
:::

<1>2. The sequence $(M_1^n)$ tends to infinity in norm and is uniformly
bounded away from zero.

::: {.proof}
Let $v$ be a unit eigenvector for the eigenvalue $5$. For the operator norm,
$$
\norm{M_1^n}
\geq
\norm{M_1^n v}
=5^n.
$$
Thus $\norm{M_1^n}\to\infty$. Since all norms on the finite-dimensional
space $M_2(\RR)$ are equivalent, the same conclusion holds for any fixed
matrix norm. Moreover, $\det M_1=10\neq0$, so every $M_1^n$ is nonzero.
The norms are therefore at least $1$ for all sufficiently large $n$, and
the finitely many remaining positive norms have a positive minimum. Hence
$(M_1^n)$ is uniformly bounded away from zero.
:::

<1>3. The powers of $M_2$ satisfy
$$
M_2^3=-I,
\qquad
M_2^6=I.
$$

::: {.proof}
The characteristic polynomial of $M_2$ is
$$
\lambda^2-\lambda+1.
$$
By the Cayley--Hamilton theorem,
$$
M_2^2-M_2+I=0.
$$
Therefore
$$
M_2^3
=M_2(M_2-I)
=M_2^2-M_2
=-I,
$$
and squaring gives $M_2^6=I$.
:::

<1>4. The sequence $(M_2^n)$ is bounded and uniformly bounded away from
zero.

::: {.proof}
By step <1>3, the sequence is periodic with period dividing $6$. Hence its
values belong to the finite set
$$
\{I,M_2,M_2^2,-I,-M_2,-M_2^2\}.
$$
Every matrix in this set is invertible, hence nonzero. The norms of this
finite set therefore have a finite maximum and a positive minimum.
:::

<1>5. Both eigenvalues of $M_3$ have modulus
$$
\sqrt{\frac7{10}}<1.
$$

::: {.proof}
Since $6.9=69/10$,
$$
\det M_3
=5(-4)-\frac{69}{10}(-3)
=\frac7{10},
$$
while $\operatorname{tr}M_3=1$. Thus the characteristic polynomial is
$$
\lambda^2-\lambda+\frac7{10}.
$$
Its roots are
$$
\lambda_\pm
=
\frac{1\pm i\sqrt{9/5}}2,
$$
and
$$
\abs{\lambda_\pm}^2
=\frac{1+9/5}{4}
=\frac7{10}.
$$
:::

<1>6. The sequence $(M_3^n)$ converges to zero.

::: {.proof}
The two eigenvalues in step <1>5 are distinct, so $M_3$ is diagonalizable
over $\CC$. Thus
$$
M_3
=
P
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}
P^{-1}
$$
for some invertible complex matrix $P$, and hence
$$
M_3^n
=
P
\begin{pmatrix}
\lambda_+^n&0\\
0&\lambda_-^n
\end{pmatrix}
P^{-1}
\longrightarrow0
$$
because $\abs{\lambda_\pm}<1$. Therefore $(M_3^n)$ is bounded, but it is
not bounded away from zero.
:::

<1>7. The requested classifications are
$$
\boxed{
\begin{aligned}
\text{bounded away from }\infty &: i=2,3,\\
\text{bounded away from }0 &: i=1,2.
\end{aligned}
}
$$

::: {.proof}
Step <1>2 excludes $i=1$ from the first class and includes it in the second.
Step <1>4 includes $i=2$ in both classes. Step <1>6 includes $i=3$ in the
first class and excludes it from the second.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives both requested answers.
:::
:::
