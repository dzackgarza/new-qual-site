---
schema: qual/card@1
id: P-BKF00-8
kind: problem
title: A Singer cycle in $GL_n(\mathbb F_p)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Multiplication by a generator of the finite-field multiplicative group
    has one orbit on all nonzero vectors after choosing a vector-space basis.
---

::: {.problem}
Let $p$ be prime and $n$ a positive integer. Prove that there exists
\[
A\in GL_n(\mathbb F_p)
\]
which, as a permutation of the nonzero vectors of $\mathbb F_p^n$, is a single cycle of length
\[
p^n-1.
\]
:::

::: {.solution}
Let $L=\FF_{p^n}$, regarded as an $n$-dimensional vector space over
$\FF_p$.

<1>1. There is an element $\alpha\in L^\times$ of multiplicative order
$p^n-1$.

::: {.proof}
The multiplicative group of a finite field is cyclic. Since
$\abs{L^\times}=p^n-1$, a generator $\alpha$ has the stated order.
:::

<1>2. Multiplication by $\alpha$ defines an invertible $\FF_p$-linear map
$$
m_\alpha:L\longrightarrow L,
\qquad
x\longmapsto\alpha x.
$$

::: {.proof}
Multiplication in $L$ is $\FF_p$-bilinear, so $m_\alpha$ is
$\FF_p$-linear. Since $\alpha\neq0$, multiplication by $\alpha^{-1}$ is
its inverse.
:::

<1>3. Fix an $\FF_p$-linear isomorphism
$\phi:\FF_p^n\to L$ and set
$$
A=\phi^{-1}m_\alpha\phi.
$$
Then $A\in GL_n(\FF_p)$.

::: {.proof}
By step <1>2, $m_\alpha$ is an invertible $\FF_p$-linear map. Conjugating
it by the vector-space isomorphism $\phi$ gives an invertible
$\FF_p$-linear endomorphism of $\FF_p^n$.
:::

<1>4. Every nonzero vector of $\FF_p^n$ has orbit of length $p^n-1$
under $A$.

::: {.proof}
Let $v\in\FF_p^n$ be nonzero. For every integer $k\ge0$,
$$
\phi(A^k v)=\alpha^k\phi(v).
$$
Since $\phi(v)\neq0$, the equality $A^k v=v$ is equivalent to
$\alpha^k=1$. By step <1>1, the least positive such $k$ is $p^n-1$.
Thus the orbit of $v$ has length $p^n-1$.
:::

<1>5. As a permutation of $\FF_p^n\setminus\{0\}$, $A$ is a single cycle
of length $\boxed{p^n-1}$.

::: {.proof}
There are exactly $p^n-1$ nonzero vectors in $\FF_p^n$. By step <1>4,
the orbit of any one of them already has that cardinality, so it is the
entire set of nonzero vectors.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3 and <1>5 give the required element of $GL_n(\FF_p)$ and its
cycle structure.
:::
:::
