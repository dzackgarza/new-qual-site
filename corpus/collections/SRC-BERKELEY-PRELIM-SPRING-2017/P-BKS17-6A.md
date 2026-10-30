---
schema: qual/card@1
id: P-BKS17-6A
kind: problem
title: $\det e^A=e^{\operatorname{tr}A}$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored inline-math spacing and wrote det and Tr as operators against Sp17_Exam_0.pdf page 7 problem 6A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 triangularization proof.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified absolute convergence in a submultiplicative matrix norm, compatibility of the exponential with similarity, and the triangular determinant calculation.
---

::: {.problem}
Let $A$ be an $n \times n$ matrix over the complex numbers. Let $e^A = 1 + A + A^2/2 + \cdots + A^m/m! + \cdots$. Show this series converges and $\det(e^A) = e^{\operatorname{Tr}(A)}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The series
$$
\sum_{m=0}^{\infty}\frac{A^m}{m!}
$$
converges absolutely in any submultiplicative matrix norm.


::: pf-proof

Let $\norm{\cdot}$ be such a norm. Then
$$
\norm{\frac{A^m}{m!}}
\leq
\frac{\norm{ A}^m}{m!}.
$$
The scalar series
$$
\sum_{m=0}^{\infty}\frac{\norm{ A}^m}{m!}
=
e^{\norm{ A}}
$$
converges, so comparison proves absolute convergence of the matrix series.

:::

:::

::: {.pf-step #s1-2}

If $S$ is invertible, then
$$
e^{S^{-1}AS}=S^{-1}e^AS.
$$


::: pf-proof

For every $m\geq0$,
$$
(S^{-1}AS)^m=S^{-1}A^mS.
$$
By step [](#s1-1){.pf-ref} the exponential series converges absolutely, so termwise conjugation is valid:
$$
\begin{aligned}
e^{S^{-1}AS}
&=\sum_{m=0}^{\infty}\frac{(S^{-1}AS)^m}{m!}\\
&=S^{-1}\left(\sum_{m=0}^{\infty}\frac{A^m}{m!}\right)S\\
&=S^{-1}e^AS.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

There is an invertible matrix $S$ such that
$$
T\coloneqq S^{-1}AS
$$
is upper triangular.


::: pf-proof

Over $\CC$, every matrix is triangularizable; for example, this is Schur's triangularization theorem.

:::

:::

::: {.pf-step #s1-4}

If the diagonal entries of $T$ are $\lambda_1,\ldots,\lambda_n$, then $e^T$ is upper triangular with diagonal entries
$$
e^{\lambda_1},\ldots,e^{\lambda_n}.
$$


::: pf-proof

Every power $T^m$ is upper triangular, and its $i$-th diagonal entry is $\lambda_i^m$. Therefore the $i$-th diagonal entry of
$$
e^T=\sum_{m=0}^{\infty}\frac{T^m}{m!}
$$
is
$$
\sum_{m=0}^{\infty}\frac{\lambda_i^m}{m!}=e^{\lambda_i}.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{\det(e^A)=e^{\operatorname{Tr}(A)}}.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
e^T=S^{-1}e^AS,
$$
so $e^T$ and $e^A$ have the same determinant. By step [](#s1-4){.pf-ref},
$$
\det(e^A)
=
\det(e^T)
=
\prod_{i=1}^n e^{\lambda_i}
=
e^{\sum_i\lambda_i}.
$$
Since trace is invariant under similarity and the trace of an upper triangular matrix is the sum of its diagonal entries,
$$
\sum_i\lambda_i=\operatorname{Tr}(T)=\operatorname{Tr}(A).
$$
Substitution gives the claimed identity.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves convergence, and step [](#s1-5){.pf-ref} proves the determinant formula.

:::

:::

:::
