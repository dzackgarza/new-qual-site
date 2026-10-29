---
schema: qual/card@1
id: P-UCLAB10F-08
kind: problem
title: Orthogonal complement of an intersection
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Let $W_1,W_2$ be subspaces of a finite-dimensional inner-product space $V$.
Prove that
$$
(W_1\cap W_2)^\perp=W_1^\perp+W_2^\perp.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For any subspaces $U_1,U_2\subseteq V$,
$$
(U_1+U_2)^\perp
=
U_1^\perp\cap U_2^\perp.
$$


::: pf-proof

Let $v\in V$. Then
$$
v\in(U_1+U_2)^\perp
$$
if and only if
$$
\langle v,u_1+u_2\rangle=0
$$
for every $u_1\in U_1$ and $u_2\in U_2$.

Taking $u_2=0$ shows that this implies $v\in U_1^\perp$, and taking $u_1=0$ shows that it implies $v\in U_2^\perp$. Conversely, if $v$ belongs to both orthogonal complements, then
$$
\langle v,u_1+u_2\rangle
=
\langle v,u_1\rangle+\langle v,u_2\rangle
=0.
$$
Thus the two subspaces are equal.

:::

:::

::: {.pf-step #s1-2}

In a finite-dimensional inner-product space,
$$
(U^\perp)^\perp=U
$$
for every subspace $U\subseteq V$.


::: pf-proof

One always has
$$
U\subseteq(U^\perp)^\perp.
$$
Also
$$
\dim U+\dim U^\perp=\dim V,
$$
so
$$
\dim(U^\perp)^\perp
=
\dim V-\dim U^\perp
=
\dim U.
$$
Thus the inclusion is between subspaces of equal dimension and is therefore equality.

:::

:::

::: {.pf-step #s1-3}

Applying step [](#s1-1){.pf-ref} to $W_1^\perp$ and $W_2^\perp$ gives
$$
(W_1^\perp+W_2^\perp)^\perp
=
W_1\cap W_2.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} yields
$$
(W_1^\perp+W_2^\perp)^\perp
=
(W_1^\perp)^\perp
\cap
(W_2^\perp)^\perp.
$$
By step [](#s1-2){.pf-ref},
$$
(W_i^\perp)^\perp=W_i
$$
for $i=1,2$, giving the stated equality.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
(W_1\cap W_2)^\perp
=
W_1^\perp+W_2^\perp
}.
$$


::: pf-proof

Take orthogonal complements of both sides of step [](#s1-3){.pf-ref}. By step [](#s1-2){.pf-ref},
$$
\bigl((W_1^\perp+W_2^\perp)^\perp\bigr)^\perp
=
W_1^\perp+W_2^\perp,
$$
while the orthogonal complement of the right side of step [](#s1-3){.pf-ref} is
$$
(W_1\cap W_2)^\perp.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required identity.

:::

:::

:::
