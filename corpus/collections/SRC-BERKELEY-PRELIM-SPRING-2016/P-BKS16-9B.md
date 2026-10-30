---
schema: qual/card@1
id: P-BKS16-9B
kind: problem
title: Groups of order $p^2$ are abelian
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the exponent in p^2 against Sp16_Exam.pdf page 20 problem 9B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2016 conjugation-action solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the class-equation center bound and the lemma that a cyclic quotient by the center forces the group to be abelian.
---

::: {.problem}
Let $p$ be a prime number. Prove that every group $G$ of order $p^2$ is commutative.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The center $Z(G)$ has order divisible by $p$, and therefore
$$
\cardinality{Z(G)}\in\{p,p^2\}.
$$


::: pf-proof

Let $G$ act on itself by conjugation. The class equation is
$$
\cardinality{G}
=
\cardinality{Z(G)}
+
\sum_i [G:C_G(x_i)],
$$
where the $x_i$ represent the noncentral conjugacy classes. For each noncentral $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup of the group of order $p^2$. Since it contains the identity and $x_i$, its order is $p$, so
$$
[G:C_G(x_i)]=p.
$$
Thus every term in the sum is divisible by $p$. Since $\cardinality{G}=p^2$, the class equation gives
$$
\cardinality{Z(G)}\equiv0\pmod p.
$$
The center contains the identity, so it is nonempty; its order divides $p^2$. Hence its order is $p$ or $p^2$.

:::

:::

::: {.pf-step #s1-2}

If $\cardinality{Z(G)}=p^2$, then $G$ is abelian. If $\cardinality{Z(G)}=p$, then $G/Z(G)$ is cyclic.


::: pf-proof

If $\cardinality{Z(G)}=p^2=\cardinality{G}$, then $Z(G)=G$, which is precisely the assertion that $G$ is abelian.

If $\cardinality{Z(G)}=p$, then
$$
\cardinality{G/Z(G)}=p.
$$
Every group of prime order is cyclic, so $G/Z(G)$ is cyclic.

:::

:::

::: {.pf-step #s1-3}

If $G/Z(G)$ is cyclic, then $G$ is abelian.


::: pf-proof

Suppose
$$
G/Z(G)=\langle gZ(G)\rangle.
$$
For arbitrary $x,y\in G$, there exist integers $a,b$ and elements $z_1,z_2\in Z(G)$ such that
$$
x=g^az_1,
\qquad
y=g^bz_2.
$$
Since $z_1$ and $z_2$ are central,
$$
xy=g^{a+b}z_1z_2=g^{a+b}z_2z_1=yx.
$$
Thus every pair of elements commutes.

:::

:::

::: {.pf-step #s1-4}

The group $G$ is abelian.


::: pf-proof

By step [](#s1-1){.pf-ref}, the center has order $p$ or $p^2$. The case $p^2$ is abelian by step [](#s1-2){.pf-ref}. In the case $p$, step [](#s1-2){.pf-ref} gives that $G/Z(G)$ is cyclic, and step [](#s1-3){.pf-ref} then gives that $G$ is abelian.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the assertion.

:::

:::

:::
