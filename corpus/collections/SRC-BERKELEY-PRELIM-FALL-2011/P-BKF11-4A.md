---
schema: qual/card@1
id: P-BKF11-4A
kind: problem
title: Polynomials representing evaluation at $1$ are orthogonal for the weight $1-x$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the finite-dimensional representation argument, proved that the
    representing polynomial has degree exactly n, and verified the weighted
    orthogonality using degree m+1 for (1-x)S_m.
---

::: {.problem}
Show that for any integer $n\ge0$ there is a unique polynomial $S_n$ of degree $n$ with real coefficients such that
$$
\int_{-1}^1 S_n(x)P(x)\,dx=P(1)
$$
for every polynomial $P$ of degree at most $n$.

Show that
$$
\int_{-1}^1(1-x)S_m(x)S_n(x)\,dx=0
$$
if $m\ne n$.
:::

::: {.solution}
For $n\ge0$, let $V_n\subset\RR[x]$ be the real vector space of
polynomials of degree at most $n$.

::: pf

::: {.pf-step #s1}

The linear map
$$
T_n\colon V_n\longrightarrow V_n^*,
\qquad
T_n(S)(P)=\int_{-1}^1S(x)P(x)\,dx,
$$
is an isomorphism.

::: pf-proof

The map is linear. If $T_n(S)=0$, then taking $P=S$ gives
$$
0=T_n(S)(S)=\int_{-1}^1S(x)^2\,dx.
$$
The integrand is continuous and nonnegative, so it vanishes identically
on $[-1,1]$. Hence $S=0$ as a polynomial, and $T_n$ is injective.

Both $V_n$ and $V_n^*$ have dimension $n+1$. Therefore the injective
linear map $T_n$ is an isomorphism.

:::

:::

::: {.pf-step #s2}

There is a unique $S_n\in V_n$ satisfying
$$
\int_{-1}^1S_n(x)P(x)\,dx=P(1)
\qquad(P\in V_n),
$$
and $S_n$ has degree exactly $n$.

::: pf-proof

Evaluation at $1$ defines a linear functional
$$
E_n\colon V_n\to\RR,
\qquad
E_n(P)=P(1).
$$
By step [](#s1){.pf-ref}, there is a unique $S_n\in V_n$ with
$T_n(S_n)=E_n$, which is exactly the displayed identity.

For $n=0$, taking $P=1$ gives
$$
\int_{-1}^1S_0(x)\,dx=1,
$$
so $S_0$ is a nonzero constant and has degree $0$.

Now let $n\ge1$ and suppose, for contradiction, that
$\deg S_n\le n-1$. Then
$$
P(x)\coloneqq(1-x)S_n(x)
$$
belongs to $V_n$ and satisfies $P(1)=0$. The defining identity for
$S_n$ therefore gives
$$
0
=\int_{-1}^1(1-x)S_n(x)^2\,dx.
$$
The integrand is continuous and nonnegative on $[-1,1]$. Since
$1-x>0$ on $(-1,1)$, the integral can vanish only if $S_n$ vanishes
on $(-1,1)$, hence only if $S_n=0$ as a polynomial. But the defining
identity with $P=1$ gives
$$
\int_{-1}^1S_n(x)\,dx=1,
$$
a contradiction. Thus $\deg S_n=n$.

:::

:::

::: {.pf-step #s3}

If $m<n$, then
$$
\int_{-1}^1(1-x)S_m(x)S_n(x)\,dx=0.
$$

::: pf-proof

Since $\deg S_m=m$ by step [](#s2){.pf-ref}, the polynomial
$$
P(x)\coloneqq(1-x)S_m(x)
$$
has degree at most $m+1\le n$. Hence $P\in V_n$, and $P(1)=0$.
Applying the defining identity for $S_n$ from step [](#s2){.pf-ref} gives
$$
\int_{-1}^1S_n(x)(1-x)S_m(x)\,dx=P(1)=0,
$$
which is the asserted integral.

:::

:::

::: {.pf-step #s4}

For all $m\ne n$,
$$
\boxed{
\int_{-1}^1(1-x)S_m(x)S_n(x)\,dx=0
}.
$$

::: pf-proof

If $m<n$, this is step [](#s3){.pf-ref}. If $n<m$, apply step [](#s3){.pf-ref} with the roles
of $m$ and $n$ interchanged; multiplication is commutative, so the
same integral is obtained.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the required existence, uniqueness, and degree of
$S_n$, and step [](#s4){.pf-ref} proves the required orthogonality.

:::

:::

:::
