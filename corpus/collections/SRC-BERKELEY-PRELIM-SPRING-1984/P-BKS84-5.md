---
schema: qual/card@1
id: P-BKS84-5
kind: problem
title: A spectral relation $AB=BA^2$ forces a common eigenvector away from the unit circle
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the induced map from the $A$-eigenspace for $\lambda$ to that for $\lambda^2$, with extremal-modulus choices and the zero-eigenspace case.
---

::: {.problem}
Let $A,B$ be complex $n\times n$ matrices satisfying
\[
AB=BA^2,
\]
and suppose $A$ has no eigenvalue of absolute value $1$. Prove that $A$ and $B$ have a common nonzero eigenvector.
:::

::: {.solution}
::: pf

::: {.pf-step #b-maps-eigenspace}
For every eigenvalue $\lambda$ of $A$,
$$
B\bigl(E_\lambda(A)\bigr)
\subseteq
E_{\lambda^2}(A),
$$
where $E_\mu(A)=\ker(A-\mu I)$ and $E_\mu(A)=\{0\}$ when $\mu$ is
not an eigenvalue.

::: pf-proof
If $v\in E_\lambda(A)$, then
$$
\begin{aligned}
A(Bv)
&=
BA^2v\\
&=
B(\lambda^2v)\\
&=
\lambda^2Bv.
\end{aligned}
$$
Thus $Bv\in\ker(A-\lambda^2I)=E_{\lambda^2}(A)$.
:::

:::

::: {.pf-step #modulus-greater-than-one-case}
If $A$ has an eigenvalue of modulus greater than $1$, then $A$ and
$B$ have a common nonzero eigenvector.

::: pf-proof
Choose an eigenvalue $\lambda$ of $A$ having maximal absolute value.
Under the present hypothesis, choose it with $\abs{\lambda}>1$. Then
$$
\abs{\lambda^2}
=
\abs{\lambda}^2
>
\abs{\lambda},
$$
so $\lambda^2$ is not an eigenvalue of $A$ by maximality. Step [](#b-maps-eigenspace){.pf-ref}
therefore gives
$$
B(E_\lambda(A))=\{0\}.
$$
Any nonzero $v\in E_\lambda(A)$ then satisfies
$$
Av=\lambda v,
\qquad
Bv=0,
$$
so $v$ is a common eigenvector.
:::

:::

::: {.pf-step #modulus-less-nonzero-case}
Suppose every eigenvalue of $A$ has modulus less than $1$ and
$0$ is not an eigenvalue. Then $A$ and $B$ have a common nonzero
eigenvector.

::: pf-proof
Choose an eigenvalue $\lambda$ of $A$ having minimal absolute value.
Since $0<\abs{\lambda}<1$,
$$
0
<
\abs{\lambda^2}
<
\abs{\lambda}.
$$
Thus $\lambda^2$ is not an eigenvalue of $A$ by minimality. As in step
[](#modulus-greater-than-one-case){.pf-ref}, step [](#b-maps-eigenspace){.pf-ref} gives $B(E_\lambda(A))=\{0\}$, and any nonzero
$v\in E_\lambda(A)$ is a common eigenvector of $A$ and $B$.
:::

:::

::: {.pf-step #zero-eigenvalue-case}
Suppose every eigenvalue of $A$ has modulus less than $1$ and
$0$ is an eigenvalue. Then $A$ and $B$ have a common nonzero eigenvector.

::: pf-proof
Step [](#b-maps-eigenspace){.pf-ref} with $\lambda=0$ gives
$$
B(E_0(A))\subseteq E_0(A).
$$
The space $E_0(A)$ is nonzero. Since it is a finite-dimensional complex
vector space, the restriction
$$
B|_{E_0(A)}
$$
has an eigenvector $v\neq0$. For some $\mu\in\CC$,
$$
Av=0,
\qquad
Bv=\mu v.
$$
Hence $v$ is a common eigenvector.
:::

:::

::: {.pf-step #common-eigenvector-exists}
$A$ and $B$ have a common nonzero eigenvector.

::: pf-proof
Because $A$ is a complex matrix, it has an eigenvalue. By hypothesis no
eigenvalue has modulus $1$. If some eigenvalue has modulus greater than
$1$, step [](#modulus-greater-than-one-case){.pf-ref} applies. Otherwise all eigenvalues have modulus less than
$1$, and either step [](#modulus-less-nonzero-case){.pf-ref} or step [](#zero-eigenvalue-case){.pf-ref} applies according as $0$ is or is
not an eigenvalue.
:::

:::

::: pf-qed
Step [](#common-eigenvector-exists){.pf-ref} is the required conclusion.
:::

:::
:::
