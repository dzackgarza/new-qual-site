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

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $T$ has a real root.

::: pf-proof

After choosing a basis, the characteristic polynomial is a real polynomial
of degree $3$. Every real polynomial of odd degree has at least one real
root.

:::

:::

::: {.pf-step #s2}

The transformation $T$ has a one-dimensional invariant subspace.

::: pf-proof

Let $\lambda\in\RR$ be a root from step [](#s1){.pf-ref}. Then
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

:::

::: {.pf-step #s3}

The transpose $T^t$ has a nonzero real eigenvector.

::: pf-proof

The characteristic polynomials of $T$ and $T^t$ are equal because
$$
\det(tI-T^t)
=
\det\bigl((tI-T)^t\bigr)
=
\det(tI-T).
$$
Hence step [](#s1){.pf-ref} also supplies a real eigenvalue $\mu$ of $T^t$, with a
nonzero vector $v$ satisfying
$$
T^tv=\mu v.
$$

:::

:::

::: {.pf-step #s4}

The plane
$$
P\coloneqq v^\perp
$$
is $T$-invariant.

::: pf-proof

Since $v\neq0$ in $\RR^3$, its orthogonal complement has dimension $2$.
If $x\in P$, then
$$
\langle x,v\rangle=0.
$$
Using step [](#s3){.pf-ref},
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

:::

::: {.pf-step #s5}

The transformation $T$ has both a one-dimensional and a
two-dimensional invariant subspace.

::: pf-proof

Step [](#s2){.pf-ref} supplies the invariant line, and step [](#s4){.pf-ref} supplies the invariant
plane.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves both requested assertions.

:::

:::

:::
