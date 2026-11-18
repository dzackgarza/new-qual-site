---
schema: qual/card@1
id: P-BKS04-4A
kind: problem
title: Every real invertible $2\times2$ matrix is an $n$-th power exactly when $n$ is odd
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the even obstruction by the determinant, then the three
    cases of odd $n$ (distinct real eigenvalues, equal real eigenvalues, non-real eigenvalues). The argument
    is the retained packet's (problem 4A of `assets/attachments/s04solution.pdf`), read again for this pass
    and unchanged.
---

::: {.problem}
For which positive integers $n$ is it true that every invertible $2\times2$ matrix $A$ with real entries can be expressed as the $n$-th power of another $2\times2$ matrix with real entries?
:::

::: {.solution}
The retained solution set is the **Berkeley Spring 2004 preliminary solution packet** (`assets/attachments/s04solution.pdf`, extracted text at `assets/attachments/s04solution_extracted.md`), problem 4A; the argument below is its, split into steps. The answer is: exactly the odd positive integers $n$.

::: pf

::: {.pf-step #even}
If $n$ is even, $A=\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ is not an $n$-th power.

::: pf-proof
For any real matrix $B$, $\det(B^{n})=\det(B)^{n}$; for even $n$ the right side is $\det(B)^{n}\ge0$, since an even power of a real number is nonnegative. But $\det A=-1<0$, so $A$ cannot be $B^{n}$ for any real $2\times2$ matrix $B$.
:::

:::

::: {.pf-step #distinct}
If $n$ is odd and $A$ has distinct real eigenvalues, then $A=B^{n}$ for some real $B$.

::: pf-proof
Conjugation does not affect the question: if $A=PCP^{-1}$ and $C=D^{n}$ then $A=(PDP^{-1})^{n}$. A real matrix with distinct real eigenvalues is diagonalizable over $\RR$, so take $A$ diagonal, say $A=\operatorname{diag}(\lambda_{1},\lambda_{2})$ with $\lambda_{i}\ne0$ because $A$ is invertible. Since $n$ is odd, every real number has a real $n$-th root, so $B=\operatorname{diag}(\mu_{1},\mu_{2})$ with $\mu_{i}^{n}=\lambda_{i}$ satisfies $B^{n}=A$.
:::

:::

::: {.pf-step #equal}
If $n$ is odd and $A$ has a single real eigenvalue $\lambda$, then $A=B^{n}$ for some real $B$.

::: pf-proof
Up to conjugation $A$ is $\lambda\begin{bmatrix}1&c\\0&1\end{bmatrix}$ with $\lambda\in\RR^{\times}$ and $c\in\RR$: the Jordan form of a matrix whose sole eigenvalue is $\lambda$ is either $\lambda I$ (then take $B=\lambda^{1/n}I$) or a single Jordan block, which is conjugate to that displayed matrix. Then
$$
B=\lambda^{1/n}\begin{bmatrix}1&c/n\\0&1\end{bmatrix},\qquad B^{n}=\lambda\begin{bmatrix}1&n\cdot(c/n)\\0&1\end{bmatrix}=A,
$$
because $\begin{bmatrix}1&x\\0&1\end{bmatrix}^{n}=\begin{bmatrix}1&nx\\0&1\end{bmatrix}$, as induction on $n$ shows.
:::

:::

::: {.pf-step}
If $n$ is odd and the eigenvalues of $A$ are not real, then $A=B^{n}$ for some real $B$.

::: pf-proof
The minimal polynomial of $A$ is then a quadratic $f\in\RR[x]$ with no real root, so $f$ is irreducible over $\RR$ and the subalgebra $\RR[A]\subseteq M_{2}(\RR)$ is isomorphic to $\RR[x]/(f)\cong\CC$: it is a two-dimensional real algebra with no zero divisors, and the two-dimensional field extension of $\RR$ is $\CC$. Under this isomorphism $A$ corresponds to some element of $\CC$; every nonzero complex number has an $n$-th root, so $A$ has an $n$-th root inside $\RR[A]$, that is a real $2\times2$ matrix $B$ with $B^{n}=A$. With steps [](#distinct){.pf-ref} and [](#equal){.pf-ref} this covers every invertible real $A$ when $n$ is odd, and step [](#even){.pf-ref} rules out even $n$; hence the answer is the odd positive integers.
:::

:::

:::
:::
