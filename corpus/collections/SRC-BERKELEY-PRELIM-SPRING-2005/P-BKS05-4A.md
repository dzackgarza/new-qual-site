---
schema: qual/card@1
id: P-BKS05-4A
kind: problem
title: Product of commuting diagonalizable real matrices is diagonalizable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained simultaneous-eigenspace argument:
    commutativity makes each A-eigenspace B-invariant; the restriction of
    diagonalizable B is diagonalizable there, yielding a common eigenbasis.
---

::: {.problem}
Suppose A and B are commuting $n \times n$ matrices over R. Suppose A and B are each diagonalizable over R. Show that AB is diagonalizable over R.
:::

::: {.solution}
Regard $A$ and $B$ as endomorphisms of $\RR^n$.

<1>1. Every eigenspace of $A$ is invariant under $B$.

::: {.proof}
Let $V_\lambda$ be the eigenspace of $A$ with eigenvalue $\lambda$.
If $v\in V_\lambda$, then commutativity gives
$$
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv.
$$
Thus $Bv\in V_\lambda$.
:::

<1>2. For every eigenvalue $\lambda$ of $A$, the restriction
$$
B|_{V_\lambda}:V_\lambda\longrightarrow V_\lambda
$$
is diagonalizable over $\RR$.

::: {.proof}
Because $B$ is diagonalizable over $\RR$, its minimal polynomial
$m_B(t)$ is a product of distinct linear factors over $\RR$.
By step <1>1, $V_\lambda$ is $B$-invariant, and therefore the minimal
polynomial of $B|_{V_\lambda}$ divides $m_B(t)$. It is consequently
also a product of distinct linear factors over $\RR$, so the
restriction is diagonalizable.
:::

<1>3. The vector space $\RR^n$ has a basis consisting of simultaneous
eigenvectors of $A$ and $B$.

::: {.proof}
Since $A$ is diagonalizable,
$$
\RR^n=\bigoplus_\lambda V_\lambda,
$$
where the sum runs over the distinct eigenvalues of $A$. By step
<1>2, each $V_\lambda$ has a basis of eigenvectors of the restricted
operator $B|_{V_\lambda}$. Every vector in such a basis is already an
eigenvector of $A$ because it lies in $V_\lambda$. The union of these
bases is therefore a basis of $\RR^n$ consisting of common
eigenvectors.
:::

<1>4. The product $AB$ is diagonalizable over $\RR$.

::: {.proof}
Let $v$ be one of the simultaneous eigenvectors from step <1>3, with
$$
Av=\lambda v,
\qquad
Bv=\mu v.
$$
Then
$$
ABv=A(\mu v)=\lambda\mu v.
$$
Thus the basis from step <1>3 is an eigenbasis for $AB$, proving that
$AB$ is diagonalizable over $\RR$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
