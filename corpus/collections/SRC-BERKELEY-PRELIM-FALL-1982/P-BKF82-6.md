---
schema: qual/card@1
id: P-BKF82-6
kind: problem
title: Eigenvalues of a polynomial in an operator
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
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved both directions of polynomial spectral mapping, using an eigenvector forward and factorization of f(z)-mu plus invertibility of products backward."
---

::: {.problem}
Let $T$ be a linear operator on a finite-dimensional complex vector space and $f$ a complex polynomial. If $\lambda$ is an eigenvalue of $T$, show that $f(\lambda)$ is an eigenvalue of $f(T)$. Is every eigenvalue of $f(T)$ obtained this way?
:::

::: {.solution}
Yes. The eigenvalues of $f(T)$ are exactly the numbers $f(\lambda)$ with
$\lambda$ an eigenvalue of $T$.

<1>1. An eigenvalue of $T$ produces an eigenvalue of $f(T)$.
::: {.proof}
Let $v\ne0$ satisfy
$$
Tv=\lambda v.
$$
If
$$
f(z)=\sum_{k=0}^d a_kz^k,
$$
then $T^kv=\lambda^kv$ for every $k$, and hence
$$
f(T)v
=\sum_{k=0}^d a_kT^kv
=\sum_{k=0}^d a_k\lambda^kv
=f(\lambda)v.
$$
Thus $f(\lambda)$ is an eigenvalue of $f(T)$.
:::

<1>2. Every eigenvalue of $f(T)$ arises in this way when $f$ is nonconstant.
::: {.proof}
Let $\mu$ be an eigenvalue of $f(T)$. Then
$$
f(T)-\mu I
$$
is not invertible. Since the scalar field is $\mathbb C$, factor
$$
f(z)-\mu=c\prod_{j=1}^r(z-\lambda_j)
$$
with $c\ne0$. Substituting $T$ gives
$$
f(T)-\mu I
=c\prod_{j=1}^r(T-\lambda_jI).
$$
If every $T-\lambda_jI$ were invertible, their product would be invertible,
contrary to the choice of $\mu$. Hence some $T-\lambda_jI$ is not invertible,
so $\lambda_j$ is an eigenvalue of $T$. By construction
$$
f(\lambda_j)=\mu.
$$
:::

<1>3. The constant-polynomial case gives the same conclusion.
::: {.proof}
If $f\equiv c$, then $f(T)=cI$, whose only eigenvalue is $c$. On a nonzero
finite-dimensional complex vector space, $T$ has an eigenvalue $\lambda$, and
$f(\lambda)=c$. Thus again every eigenvalue of $f(T)$ is obtained from an
eigenvalue of $T$.

Therefore
$$
\boxed{\sigma(f(T))=f(\sigma(T)).}
$$
:::
:::
