---
schema: qual/card@1
id: P-BKF14-7A
kind: problem
title: Basis for the intersection of two parametrized subspaces of $\mathbb R^4$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: the first
    subspace is the hyperplane a-b+c-d=0 and the intersection condition is
    (1+t)(x-y)=0.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked linear independence of the first three generators and both cases
    t=-1 and t different from -1.
---

::: {.problem}
Find a basis of the intersection of the subspace of $\RR^4$ spanned by $(1,1,0,0)$, $(0,1,1,0)$, $(0,0,1,1)$ and the subspace spanned by $(1,0,t,0)$, $(0,1,0,t)$, where $t$ is given.
:::

::: {.solution}
Let
$$
U\coloneqq
\operatorname{span}\{(1,1,0,0),(0,1,1,0),(0,0,1,1)\}
$$
and
$$
V_t\coloneqq
\operatorname{span}\{(1,0,t,0),(0,1,0,t)\}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
U=\{(a,b,c,d)\in\RR^4:a-b+c-d=0\}.
$$

::: pf-proof

Each of the three displayed generators of $U$ satisfies
$a-b+c-d=0$. They are linearly independent: if
$$
\lambda(1,1,0,0)
+\mu(0,1,1,0)
+\nu(0,0,1,1)=0,
$$
then the first coordinate gives $\lambda=0$, the fourth gives
$\nu=0$, and then the second gives $\mu=0$. Thus $U$ has dimension
$3$. The kernel of the nonzero functional
$$
(a,b,c,d)\longmapsto a-b+c-d
$$
also has dimension $3$, so the inclusion already established is an
equality.

:::

:::

::: pf-step

One has
$$
V_t=\{(x,y,tx,ty):x,y\in\RR\}.
$$

::: pf-proof

Indeed,
$$
x(1,0,t,0)+y(0,1,0,t)=(x,y,tx,ty).
$$
Conversely every linear combination of the two generators has this
form.

:::

:::

::: {.pf-step #s3}

A vector $(x,y,tx,ty)\in V_t$ belongs to $U$ if and only if
$$
(1+t)(x-y)=0.
$$

::: pf-proof

Substituting $(a,b,c,d)=(x,y,tx,ty)$ into the equation from step [](#s1){.pf-ref}
gives
$$
x-y+tx-ty=(1+t)(x-y).
$$

:::

:::

::: {.pf-step #s4}

If $t\ne-1$, then
$$
U\cap V_t
=
\operatorname{span}\{(1,1,t,t)\}.
$$

::: pf-proof

When $t\ne-1$, step [](#s3){.pf-ref} forces $x=y$. Hence every vector in the
intersection has the form
$$
(x,x,tx,tx)=x(1,1,t,t).
$$
The displayed vector is nonzero, so it is a basis of the
one-dimensional intersection.

:::

:::

::: {.pf-step #s5}

If $t=-1$, then
$$
U\cap V_{-1}=V_{-1},
$$
and a basis is
$$
\boxed{\{(1,0,-1,0),(0,1,0,-1)\}}.
$$

::: pf-proof

For $t=-1$, the condition in step [](#s3){.pf-ref} is automatic, so every vector of
$V_{-1}$ lies in $U$. The two displayed generators of $V_{-1}$ are
linearly independent because their first two coordinates are the
standard basis of $\RR^2$.

:::

:::

::: {.pf-step #s6}

Thus a basis of the intersection is
$$
\boxed{
\begin{cases}
\{(1,1,t,t)\},&t\ne-1,\\
\{(1,0,-1,0),(0,1,0,-1)\},&t=-1.
\end{cases}
}
$$

::: pf-proof

This combines steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives the requested basis for every value of $t$.

:::

:::

:::
