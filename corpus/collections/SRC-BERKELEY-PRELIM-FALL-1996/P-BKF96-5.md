---
schema: qual/card@1
id: P-BKF96-5
kind: problem
title: Every real endomorphism of $\mathbb R^3$ has invariant lines and planes
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the real root of the cubic characteristic polynomial for an
    invariant line, then an eigenvector of the transpose; its orthogonal
    complement is an invariant plane.
---

::: {.problem}
Prove that every linear transformation
\[
T:\mathbb R^3\to\mathbb R^3
\]
has

1. a one-dimensional invariant subspace;
2. a two-dimensional invariant subspace.
:::

::: {.solution}
<1>1. The characteristic polynomial of $T$ has a real root.

::: {.proof}
After choosing a basis, the characteristic polynomial is a real polynomial
of degree $3$. Every real polynomial of odd degree has at least one real
root.
:::

<1>2. The transformation $T$ has a one-dimensional invariant subspace.

::: {.proof}
Let $\lambda\in\RR$ be a root from step <1>1. Then
$$
\det(T-\lambda I)=0,
$$
so there is a nonzero vector $u$ with
$$
Tu=\lambda u.
$$
Therefore the line
$$
\operatorname{span}\{u\}
$$
is $T$-invariant.
:::

<1>3. The transpose $T^t$ has a nonzero real eigenvector.

::: {.proof}
The characteristic polynomials of $T$ and $T^t$ are equal because
$$
\det(tI-T^t)
=
\det\bigl((tI-T)^t\bigr)
=
\det(tI-T).
$$
Hence step <1>1 also supplies a real eigenvalue $\mu$ of $T^t$, with a
nonzero vector $v$ satisfying
$$
T^tv=\mu v.
$$
:::

<1>4. The plane
$$
P\coloneqq v^\perp
$$
is $T$-invariant.

::: {.proof}
Since $v\neq0$ in $\RR^3$, its orthogonal complement has dimension $2$.
If $x\in P$, then
$$
\langle x,v\rangle=0.
$$
Using step <1>3,
$$
\begin{aligned}
\langle Tx,v\rangle
&=
\langle x,T^tv\rangle\\
&=
\langle x,\mu v\rangle\\
&=
\mu\langle x,v\rangle\\
&=0.
\end{aligned}
$$
Thus $Tx\in v^\perp=P$, proving invariance.
:::

<1>5. The transformation $T$ has both a one-dimensional and a
two-dimensional invariant subspace.

::: {.proof}
Step <1>2 supplies the invariant line, and step <1>4 supplies the invariant
plane.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves both requested assertions.
:::
:::
