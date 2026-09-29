---
schema: qual/card@1
id: P-BKS12-4A
kind: problem
title: Eigenvalues of the skew-symmetric tridiagonal matrix with entries $\pm 1$
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
  note: Compared the authored statement with pages 1--2 of the retained Spring 2012 solution PDF and independently reviewed the recurrence-based eigenvalue computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked a diagonal similarity to i times the symmetric path-adjacency matrix and its sine eigenvectors.
---

::: {.problem}
Find the eigenvalues of the $n \times n$ matrix with entries $a _ { i j }$ , where $a _ { i j }$ is 1 if $i = j + 1 , - 1$ if $i = j - 1$ , and 0 otherwise.
:::

::: {.solution}
Let $A$ denote the matrix in the statement, and let $T$ be the real
symmetric tridiagonal matrix with
$$
T_{j,j+1}=T_{j+1,j}=1
$$
and all other entries zero.

::: pf

::: {.pf-step #similarity}
With
$$
D
\coloneqq
\operatorname{diag}
\bigl(
1,-i,(-i)^2,\ldots,(-i)^{n-1}
\bigr),
$$
one has
$$
D^{-1}AD=iT.
$$

::: pf-proof
The only nonzero entries of $A$ are
$$
A_{j,j+1}=-1
$$
and
$$
A_{j+1,j}=1.
$$
Since the $j$th diagonal entry of $D$ is $(-i)^{j-1}$,
$$
(D^{-1}AD)_{j,j+1}
=
(-i)^{-(j-1)}(-1)(-i)^j
=
i,
$$
and
$$
(D^{-1}AD)_{j+1,j}
=
(-i)^{-j}(-i)^{j-1}
=
i.
$$
All other entries remain zero. Thus $D^{-1}AD=iT$.
:::

:::

::: {.pf-step #eigenvector-formula}
For
$$
\theta_k
\coloneqq
\frac{k\pi}{n+1},
\qquad
1\leq k\leq n,
$$
the vector
$$
v^{(k)}
\coloneqq
\bigl(
\sin\theta_k,
\sin(2\theta_k),
\ldots,
\sin(n\theta_k)
\bigr)^T
$$
is a nonzero eigenvector of $T$ with eigenvalue
$$
2\cos\theta_k.
$$

::: pf-proof
Set
$$
v^{(k)}_0=0
\qquad\text{and}\qquad
v^{(k)}_{n+1}=0.
$$
The second equality holds because
$$
\sin((n+1)\theta_k)=\sin(k\pi)=0.
$$
For $1\leq j\leq n$,
$$
\begin{aligned}
(Tv^{(k)})_j
&=
\sin((j-1)\theta_k)
+
\sin((j+1)\theta_k)\\
&=
2\cos\theta_k\sin(j\theta_k)\\
&=
2\cos\theta_k\,v^{(k)}_j.
\end{aligned}
$$
Also
$$
\sin\theta_k\neq0
$$
because $0<\theta_k<\pi$, so $v^{(k)}\neq0$.
:::

:::

::: {.pf-step #eigenvalues-complete}
The numbers
$$
2\cos\theta_k,
\qquad
1\leq k\leq n,
$$
are all the eigenvalues of $T$.

::: pf-proof
The angles
$$
0<\theta_1<\theta_2<\cdots<\theta_n<\pi
$$
are distinct, and cosine is strictly decreasing on $[0,\pi]$. Hence the
$n$ eigenvalues exhibited in step [](#eigenvector-formula){.pf-ref} are distinct. An $n\times n$
matrix has exactly $n$ eigenvalues counted with algebraic multiplicity, so
these exhaust the spectrum.
:::

:::

::: {.pf-step #eigenvalues-of-a}
The eigenvalues of $A$ are
$$
\boxed{
2i\cos\left(\frac{k\pi}{n+1}\right),
\qquad
k=1,\ldots,n
}.
$$

::: pf-proof
By step [](#similarity){.pf-ref}, $A$ is similar to $iT$. Similar matrices have the same
eigenvalues, and multiplying a matrix by $i$ multiplies every eigenvalue by
$i$. Apply step [](#eigenvalues-complete){.pf-ref}.
:::

:::

::: pf-qed
Step [](#eigenvalues-of-a){.pf-ref} gives the complete spectrum.
:::

:::

:::
