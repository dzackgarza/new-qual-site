---
schema: qual/card@1
id: P-BKS21-7B
kind: problem
title: Eigenvalues of a skew tridiagonal matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Find the eigenvalues of the $n\times n$ matrix $(a_{ij})$ with
$$
a_{ij}=\begin{cases}
1,&i=j+1,\\
-1,&i=j-1,\\
0,&\text{otherwise}.
\end{cases}
$$
:::

::: {.solution}

Let $A=(a_{ij})$, and let $T$ be the real symmetric tridiagonal matrix with $1$ on both the superdiagonal and subdiagonal and $0$ elsewhere.

::: pf

::: {.pf-step #s1-1}

The matrix $A$ is similar over $\CC$ to $iT$.


::: pf-proof

Set
$$
D\coloneqq
\operatorname{diag}\bigl(1,-i,(-i)^2,\ldots,(-i)^{n-1}\bigr).
$$
Then $D$ is invertible. For $1\leq j<n$,
$$
(D^{-1}AD)_{j,j+1}
=
(-i)^{-(j-1)}(-1)(-i)^j
=i,
$$
and
$$
(D^{-1}AD)_{j+1,j}
=
(-i)^{-j}(1)(-i)^{j-1}
=i.
$$
All other entries remain $0$. Hence
$$
D^{-1}AD=iT.
$$

:::

:::

::: {.pf-step #s1-2}

For each $m=1,\ldots,n$, set
$$
\theta_m\coloneqq\frac{m\pi}{n+1}
$$
and define $v^{(m)}\in\RR^n$ by
$$
v^{(m)}_j\coloneqq\sin(j\theta_m),
\qquad
1\leq j\leq n.
$$
Then
$$
Tv^{(m)}
=
2\cos(\theta_m)\,v^{(m)}.
$$


::: pf-proof

Extend the notation by
$$
v^{(m)}_0=0,
\qquad
v^{(m)}_{n+1}
=
\sin((n+1)\theta_m)
=
\sin(m\pi)
=0.
$$
For $1\leq j\leq n$,
$$
(Tv^{(m)})_j
=
v^{(m)}_{j-1}+v^{(m)}_{j+1}.
$$
Using
$$
\sin((j-1)\theta)+\sin((j+1)\theta)
=
2\cos\theta\,\sin(j\theta),
$$
one gets
$$
(Tv^{(m)})_j
=
2\cos(\theta_m)v^{(m)}_j.
$$
The vector $v^{(m)}$ is nonzero because its first coordinate is $\sin\theta_m\neq0$.

:::

:::

::: {.pf-step #s1-3}

The $n$ numbers
$$
2\cos\frac{m\pi}{n+1},
\qquad
m=1,\ldots,n,
$$
are all the eigenvalues of $T$.


::: pf-proof

Step [](#s1-2){.pf-ref} gives all of them as eigenvalues. The angles
$$
\frac{\pi}{n+1},
\frac{2\pi}{n+1},
\ldots,
\frac{n\pi}{n+1}
$$
are distinct and lie in $(0,\pi)$, where $\cos$ is strictly decreasing. Hence the displayed eigenvalues are distinct. An $n\times n$ matrix has at most $n$ distinct eigenvalues, so these are all of them.

:::

:::

::: {.pf-step #s1-4}

The eigenvalues of $A$ are
$$
\boxed{
\lambda_m
=
2i\cos\frac{m\pi}{n+1},
\qquad
m=1,\ldots,n
}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $A$ and $iT$ are similar and therefore have the same eigenvalues. Multiplying a matrix by $i$ multiplies each eigenvalue by $i$. Apply step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the complete list of eigenvalues.

:::

:::

:::
