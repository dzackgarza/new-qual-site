---
schema: qual/card@1
id: P-BKF97-9
kind: problem
title: Groups of order $p^2$ are abelian
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the class equation to show the center is nontrivial. If the center
    has order p, the quotient by the center is cyclic of order p, which
    forces the whole group to be abelian.
---

::: {.problem}
Prove that if $p$ is prime, then every group of order $p^2$ is abelian.
:::

::: {.solution}

Let
$$
\abs G=p^2.
$$

::: pf

::: {.pf-step #center-nontrivial}
The center $Z(G)$ is nontrivial.

::: pf-proof
The class equation is
$$
\abs G
=
\abs{Z(G)}
+
\sum_j [G:C_G(x_j)],
$$
where the $x_j$ represent the noncentral conjugacy classes. Each class size
$$
[G:C_G(x_j)]
$$
divides $p^2$. For a noncentral element the class size is greater than $1$,
so it is divisible by $p$. Therefore every summand in the displayed sum is
divisible by $p$.

Since $\abs G=p^2$ is also divisible by $p$, the class equation implies
$$
p\mid\abs{Z(G)}.
$$
In particular, the center has more than one element.
:::

:::

::: {.pf-step #center-order-p-or-p-squared}
One has
$$
\abs{Z(G)}\in\{p,p^2\}.
$$

::: pf-proof
By Lagrange's theorem, the order of $Z(G)$ divides $p^2$. Step [](#center-nontrivial){.pf-ref} shows
it is divisible by $p$, leaving only the two displayed possibilities.
:::

:::

::: {.pf-step #center-full-implies-abelian}
If
$$
\abs{Z(G)}=p^2,
$$
then $G$ is abelian.

::: pf-proof
In this case $Z(G)$ is a subgroup of $G$ having the same finite order as
$G$, so
$$
Z(G)=G.
$$
That equality is exactly the assertion that every pair of elements of $G$
commutes.
:::

:::

::: {.pf-step #quotient-cyclic-order-p}
If
$$
\abs{Z(G)}=p,
$$
then
$$
G/Z(G)
$$
is cyclic.

::: pf-proof
The quotient has order
$$
\frac{p^2}{p}=p.
$$
Every group of prime order is cyclic.
:::

:::

::: {.pf-step #cyclic-quotient-implies-abelian}
If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: pf-proof
Suppose
$$
G/Z(G)=\langle gZ(G)\rangle.
$$
For arbitrary $x,y\in G$, there are integers $r,s$ and central elements
$z_1,z_2\in Z(G)$ such that
$$
x=g^rz_1,
\qquad
y=g^sz_2.
$$
Since $z_1$ and $z_2$ commute with every element,
$$
\begin{aligned}
xy
&=
g^{r+s}z_1z_2\\
&=
g^{s+r}z_2z_1\\
&=
yx.
\end{aligned}
$$
Thus every pair of elements commutes.
:::

:::

::: {.pf-step #G-abelian}
The group $G$ is abelian.

::: pf-proof
By step [](#center-order-p-or-p-squared){.pf-ref}, either $\abs{Z(G)}=p^2$, handled by step [](#center-full-implies-abelian){.pf-ref}, or
$\abs{Z(G)}=p$, in which case steps [](#quotient-cyclic-order-p){.pf-ref} and [](#cyclic-quotient-implies-abelian){.pf-ref} give the conclusion.
:::

:::

::: pf-qed
Step [](#G-abelian){.pf-ref} proves the claim.
:::

:::

:::
