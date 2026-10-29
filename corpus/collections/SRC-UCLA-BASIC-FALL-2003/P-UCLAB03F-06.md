---
schema: qual/card@1
id: P-UCLAB03F-06
kind: problem
title: A local diffeomorphism covering the unit disk from boundary data
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let
\[
U=\{(x,y)\in\RR^2:x^2+y^2<1\}
\]
be the open unit disk and let $\partial U$ denote its boundary.
Suppose $F:\RR^2\to\RR^2$ is continuously differentiable and its Jacobian determinant is everywhere nonzero.
Assume also that

- $F(p)\in U$ for some $p\in U$, and

- $F(q)\notin U\cup\partial U$ for every $q\in\partial U$.

Prove that
\[
U\subseteq F(U).
\]
:::

::: {.solution}

Set
\[
Y=F(U)\cap U.
\]

::: pf

::: {.pf-step #s1-1}

The set $Y$ is nonempty.


::: pf-proof

By hypothesis there is $p\in U$ such that
\[
F(p)\in U.
\]
Since also $F(p)\in F(U)$, one has $F(p)\in Y$.

:::

:::

::: {.pf-step #s1-2}

The set $F(U)$ is open in $\RR^2$.


::: pf-proof

At every $x\in U$, the Jacobian determinant of $F$ is nonzero. Hence the derivative
\[
DF(x):\RR^2\to\RR^2
\]
is invertible. By the inverse function theorem, there is an open neighborhood $N_x\subseteq U$ such that
\[
F(N_x)
\]
is open in $\RR^2$. Therefore
\[
F(U)=\bigcup_{x\in U}F(N_x)
\]
is open.

:::

:::

::: {.pf-step #s1-3}

The set $Y$ is open in the subspace $U$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $F(U)$ is open in $\RR^2$. Hence
\[
Y=F(U)\cap U
\]
is open in the subspace topology on $U$.

:::

:::

::: {.pf-step #s1-4}

The set $Y$ is closed in the subspace $U$.


::: pf-proof

Let $(y_n)$ be a sequence in $Y$ converging to some $y\in U$. For each $n$, choose $x_n\in U$ such that
\[
F(x_n)=y_n.
\]
The closed unit disk
\[
\overline U=\{x\in\RR^2:\|x\|\le1\}
\]
is compact. Hence some subsequence $(x_{n_j})$ converges to a point
\[
x\in\overline U.
\]
Continuity of $F$ gives
\[
F(x)
=
\lim_{j\to\infty}F(x_{n_j})
=
\lim_{j\to\infty}y_{n_j}
=y.
\]
If $x\in\partial U$, then the boundary hypothesis would give
\[
F(x)\notin U\cup\partial U,
\]
contradicting $F(x)=y\in U$. Therefore $x\notin\partial U$. Since $x\in\overline U$, it follows that $x\in U$. Hence
\[
y=F(x)\in F(U),
\]
and therefore $y\in Y$. Thus $Y$ is closed in $U$.

:::

:::

::: {.pf-step #s1-5}

One has
\[
Y=U.
\]


::: pf-proof

The open unit disk $U$ is connected. By steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref}, the subset $Y\subseteq U$ is nonempty and both open and closed in $U$. Connectedness therefore forces
\[
Y=U.
\]

:::

:::

::: {.pf-step #s1-6}

Consequently
\[
\boxed{U\subseteq F(U)}.
\]


::: pf-proof

By definition,
\[
Y=F(U)\cap U.
\]
Step [](#s1-5){.pf-ref} says this intersection equals $U$, which is exactly the stated inclusion.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
