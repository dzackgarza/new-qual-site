---
schema: qual/card@1
id: P-5CDU3
kind: problem
title: For a nondegenerate skew-symmetric form, $\dim U+\dim U^\perp=\dim V$, and a subspace $W$ with $W^\perp=W$ exists
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Bilinear Forms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2013`; it is the standard symplectic
    linear algebra statement and no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) $U^\perp$ is the kernel of $V\to U^*$, $v\mapsto B(\cdot,v)$, which is surjective because
    $V\to V^*$ is an isomorphism and every functional on $U$ extends to $V$; rank--nullity gives the
    dimension formula. (b) induction on $\dim V$: a nondegenerate subspace $P$ splits off as
    $V=P\oplus P^\perp$, and with $P=\langle v,w\rangle$ symplectic and $W'$ Lagrangian in $P^\perp$,
    the subspace $\langle v\rangle\oplus W'$ is Lagrangian. Nothing is left in outline.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$ of characteristic $0$.
Let $B:V\times V\to F$ be a non-degenerate, skew-symmetric bilinear form.
(In particular, we have $B(x,y)=-B(y,x)$ for all $x,y\in V$.)
If $U$ is a subset of $V$, let
$$
U^\perp=\{v\in V\mid B(u,v)=0 \text{ for all } u\in U\}.
$$

(a) Let $U$ be a subspace of $V$.
Prove that $U^\perp$ is a subspace of $V$ and that
$$
\dim_F(U)+\dim_F(U^\perp)=\dim_F(V).
$$

(b) Prove that there exists a subspace $W$ of $V$ such that $W^\perp=W$.
:::

::: {.solution}

Let $V$ be finite dimensional over a field $F$ of characteristic $0$ and $B$ a nondegenerate skew-symmetric bilinear form; for a subset $U\subseteq V$ put $U^\perp=\{v\in V: B(u,v)=0\ \forall u\in U\}$.

::: pf

::: {.pf-step #s1}

$U^\perp$ is a subspace, and $\dim U+\dim U^\perp=\dim V$ for every subspace $U$.

::: pf-proof

For fixed $u\in U$ the map $v\mapsto B(u,v)$ is linear, so $U^\perp$ is the intersection of the kernels of the linear functionals $B(u,\cdot)$, $u\in U$; hence it is a subspace.

Consider the linear map $\Phi:V\to U^*$, $\Phi(v)=B(\cdot,v)|_U$, whose kernel is exactly $U^\perp$. It is surjective: the map $V\to V^*$, $v\mapsto B(\cdot,v)$, is an isomorphism because $B$ is nondegenerate, and every functional on $U$ extends to a functional on $V$, since $U$ has a complement $U'$ with $V=U\oplus U'$ and one may set it equal to $0$ on $U'$. So $\Phi$ is surjective, $\operatorname{im}\Phi=U^*$, and rank–nullity gives
$$
\dim V=\dim\ker\Phi+\dim\operatorname{im}\Phi=\dim U^\perp+\dim U .
$$

:::

:::

::: {.pf-step #s2}

If $P\subseteq V$ is a subspace on which $B$ restricts to a nondegenerate form, then $V=P\oplus P^\perp$.

::: pf-proof

For $v\in V$ the functional $B(\cdot,v)|_P$ lies in $P^*$, so by nondegeneracy of $B|_P$ there is a unique $p\in P$ with $B(\cdot,p)|_P=B(\cdot,v)|_P$; then $v-p\in P^\perp$. Hence $V=P+P^\perp$. If $x\in P\cap P^\perp$ then $B(x,y)=0$ for all $y\in P$, so $x=0$ by nondegeneracy on $P$. Thus the sum is direct.

:::

:::

::: {.pf-step #s3}

There is a subspace $W$ with $W=W^\perp$.

::: pf-proof

Induct on $n=\dim V$. For $n=0$ take $W=0$, since $0^\perp=V=0$.

Let $n\ge2$. Since $B$ is skew-symmetric, $B(v,v)=0$ for every $v$; if $V\ne0$ then by nondegeneracy there are $v,w$ with $B(v,w)\ne0$. Replacing $w$ by $w/B(v,w)$ we may assume $B(v,w)=1$. The plane $P=\langle v,w\rangle$ carries the nondegenerate form with matrix $\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, so by step [](#s2){.pf-ref} $V=P\oplus P^\perp$, and $P^\perp$ carries a nondegenerate skew-symmetric form (if $z\in P^\perp$ satisfies $B(z,P^\perp)=0$ then $B(z,V)=B(z,P)+B(z,P^\perp)=0$, so $z=0$).

By induction applied to the smaller space $P^\perp$ there is $W'\subseteq P^\perp$ with $W'^{\perp_{P^\perp}}=W'$, where $\perp_{P^\perp}$ denotes the orthogonal complement inside $P^\perp$. Put $W=\langle v\rangle\oplus W'$.

For $x=p+q$ with $p\in P$, $q\in P^\perp$, one has $B(x,W)=0$ if and only if both $B(p,v)=0$ (the terms $B(q,W')$ and $B(p,W')$ vanish since $W'\subseteq P^\perp$ and $P\perp P^\perp$) and $B(q,W')=0$, that is $q\in W'$. Within $P=\langle v,w\rangle$, $B(p,v)=0$ means $p\in\langle v\rangle$, because $B(v,v)=0$ and $B(w,v)=-B(v,w)=-1\ne0$. Hence
$$
W^\perp=\langle v\rangle\oplus W'=W .
$$

:::

:::

:::

:::
