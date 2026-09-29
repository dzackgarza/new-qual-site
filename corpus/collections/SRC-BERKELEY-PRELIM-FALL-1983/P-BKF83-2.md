---
schema: qual/card@1
id: P-BKF83-2
kind: problem
title: No surjective ring homomorphism $M_{n+1}(F)\to M_n(F)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Matrix rings over a field are simple, so any surjective homomorphism
    M_{n+1}(F)->M_n(F) would be injective. The n+1 diagonal matrix units
    would then give n+1 nonzero pairwise orthogonal idempotents in M_n(F).
    Their images in F^n form a direct sum of n+1 nonzero subspaces,
    impossible in dimension n.
---

::: {.problem}
Let $F$ be a field and $n\ge1$. Does there exist a surjective ring homomorphism
\[
M_{n+1}(F)\longrightarrow M_n(F)?
\]
Give a proof of your answer.
:::

::: {.solution}
For matrix units, write $E_{ij}$ for the matrix having a single $1$
in position $(i,j)$ and zeros elsewhere.

::: pf

::: {.pf-step #s1}

For every $m\ge1$, the ring $M_m(F)$ is simple.

::: pf-proof

Let $I$ be a nonzero two-sided ideal of $M_m(F)$. Choose a nonzero
matrix $A=(a_{ij})\in I$, and choose indices $i,j$ with
$a_{ij}\neq0$.

For arbitrary $r,s$,
$$
E_{ri}AE_{js}=a_{ij}E_{rs}\in I.
$$
Since $a_{ij}$ is invertible in the field $F$, multiplying by the
scalar matrix $a_{ij}^{-1}I_m$ shows that
$$
E_{rs}\in I.
$$
Thus every matrix unit lies in $I$, and therefore $I=M_m(F)$.

:::

:::

::: {.pf-step #s2}

If a surjective ring homomorphism
$$
\varphi:M_{n+1}(F)\longrightarrow M_n(F)
$$
existed, then $\varphi$ would be injective.

::: pf-proof

The kernel of $\varphi$ is a two-sided ideal of $M_{n+1}(F)$.
Because the target ring is nonzero and $\varphi$ is surjective,
$\ker\varphi$ is a proper ideal. By step [](#s1){.pf-ref}, the only proper
ideal is $0$. Hence $\ker\varphi=0$.

:::

:::

::: {.pf-step #s3}

Under the assumption of step [](#s2){.pf-ref}, the matrices
$$
P_i=\varphi(E_{ii}),
\qquad
1\le i\le n+1,
$$
are nonzero pairwise orthogonal idempotents in $M_n(F)$.

::: pf-proof

Since
$$
E_{ii}^2=E_{ii},
$$
each $P_i$ is idempotent. Step [](#s2){.pf-ref} shows that $\varphi$ is
injective, so $P_i\neq0$. For $i\neq j$,
$$
E_{ii}E_{jj}=0=E_{jj}E_{ii},
$$
and therefore
$$
P_iP_j=0=P_jP_i.
$$

:::

:::

::: {.pf-step #s4}

The vector space $F^n$ cannot admit $n+1$ nonzero pairwise
orthogonal idempotent endomorphisms.

::: pf-proof

Suppose $P_1,\ldots,P_{n+1}$ were such idempotents. Each
$\operatorname{im}P_i$ is nonzero because $P_i\neq0$.

These images form a direct sum. Indeed, if
$$
v_1+\cdots+v_{n+1}=0,
\qquad
v_i\in\operatorname{im}P_i,
$$
then applying $P_j$ gives
$$
v_j=0,
$$
because $P_jv_j=v_j$ and $P_jv_i=0$ for $i\neq j$.

Hence
$$
\operatorname{im}P_1
\oplus\cdots\oplus
\operatorname{im}P_{n+1}
$$
is a direct sum of $n+1$ nonzero subspaces of the $n$-dimensional
space $F^n$, which is impossible.

:::

:::

::: {.pf-step #s5}

Therefore the answer is
$$
\boxed{\text{No}.}
$$

::: pf-proof

If a surjective ring homomorphism existed, step [](#s3){.pf-ref} would produce
the idempotents forbidden by step [](#s4){.pf-ref}. Thus no such homomorphism
exists.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the required answer and proof.

:::

:::

:::
