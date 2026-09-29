---
schema: qual/card@1
id: P-BKF78-3
kind: problem
title: Local fourth roots of matrices near the identity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For the polynomial map Phi(X)=X^4 on M_n(R), one has
    D Phi_I(H)=4H. This derivative is an isomorphism of the n^2-dimensional
    real vector space, so the inverse function theorem makes Phi a
    diffeomorphism between neighborhoods V and U of I.
---

::: {.problem}
Let $M_{n\times n}$ be the vector space of real $n\times n$ matrices.
Prove that there are neighborhoods $U$ and $V$ of the identity matrix in $M_{n\times n}$ such that for every $A\in U$, there is a unique $X\in V$ satisfying
\[
X^4=A.
\]
:::

::: {.solution}
Identify $M_{n\times n}$ with the real vector space $\RR^{n^2}$,
and define
$$
\Phi:M_{n\times n}\to M_{n\times n},
\qquad
\Phi(X)=X^4.
$$

::: pf

::: {.pf-step #phi-smooth}
The map $\Phi$ is continuously differentiable and satisfies
$$
\Phi(I)=I.
$$

::: pf-proof
Each entry of $X^4$ is a polynomial in the entries of $X$, so
$\Phi$ is a polynomial map and hence is continuously differentiable.
The identity $\Phi(I)=I$ is immediate.
:::

:::

::: {.pf-step #d-phi-formula}
The derivative of $\Phi$ at $I$ is
$$
D\Phi_I(H)=4H.
$$

::: pf-proof
For a matrix $H$ and a real scalar $t$,
$$
\Phi(I+tH)
=(I+tH)^4
=
I+4tH+O(t^2)
$$
as $t\to0$. Hence
$$
\frac{\Phi(I+tH)-\Phi(I)}{t}
\longrightarrow
4H,
$$
which gives the displayed derivative.
:::

:::

::: {.pf-step #d-phi-invertible}
The linear map
$$
D\Phi_I:M_{n\times n}\to M_{n\times n}
$$
is invertible.

::: pf-proof
By step [](#d-phi-formula){.pf-ref}, this map is multiplication by the nonzero scalar $4$.
Its inverse is multiplication by $1/4$.
:::

:::

::: {.pf-step #phi-bijection}
There are neighborhoods $V$ and $U$ of $I$ such that
$$
\Phi|_V:V\longrightarrow U
$$
is a bijection.

::: pf-proof
Steps [](#phi-smooth){.pf-ref} and [](#d-phi-invertible){.pf-ref} verify the hypotheses of the inverse function
theorem at $I$. Therefore there are neighborhoods $V$ of $I$ and
$U$ of $\Phi(I)=I$ such that $\Phi|_V$ is a diffeomorphism from
$V$ onto $U$, in particular a bijection.
:::

:::

::: {.pf-step #existence-uniqueness}
For every $A\in U$, there is a unique $X\in V$ satisfying
$$
\boxed{X^4=A}.
$$

::: pf-proof
By step [](#phi-bijection){.pf-ref}, every $A\in U$ has a unique preimage
$X\in V$ under $\Phi$. By definition of $\Phi$, the equation
$\Phi(X)=A$ is exactly $X^4=A$.
:::

:::

::: pf-qed
Steps [](#phi-bijection){.pf-ref} and [](#existence-uniqueness){.pf-ref} give the required neighborhoods and the stated
existence and uniqueness.
:::

:::
:::
