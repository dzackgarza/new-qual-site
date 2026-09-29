---
schema: qual/card@1
id: P-BKF00-6
kind: problem
title: The ring $E(U,U)$ of endomorphisms with $F(U)$ finite-dimensional modulo $U$, and its ideals $E(V,U)$ and $E(U,0)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    The finite-dimensional-lift criterion is applied separately to ring
    closure and to both left and right absorption for each proposed ideal.
---

::: {.problem}
Let $V$ be a vector space over a field $K$. For subspaces $U,W\subseteq V$, let $E(U,W)$ be the set of endomorphisms $F$ of $V$ such that the image of $F(U)$ in $V/W$ is finite-dimensional.

Show that $E(U,U)$ is a subring of $\operatorname{End}_K(V)$ and that
\[
E(V,U)
\qquad\text{and}\qquad
E(U,0)
\]
are two-sided ideals in $E(U,U)$.
:::

::: {.solution}

Set $R=E(U,U)$. For endomorphisms $A,B$ of $V$, juxtaposition denotes
composition, so $AB=A\circ B$.

::: pf

::: {.pf-step #finite-dim-lift-criterion}
For subspaces $A,B\subseteq V$ and $T\in\Endo_K(V)$,
$T\in E(A,B)$ if and only if there is a finite-dimensional subspace
$L\subseteq V$ such that
$$
T(A)\subseteq B+L.
$$

::: pf-proof
Let $q_B:V\to V/B$ be the quotient map. If $T\in E(A,B)$, then
$q_B(T(A))$ is finite-dimensional. Choose finitely many vectors
$y_1,\ldots,y_m\in T(A)$ whose cosets span $q_B(T(A))$, and set
$L=\operatorname{span}_K\{y_1,\ldots,y_m\}$. For every $a\in A$ there is
$\ell\in L$ with $q_B(T(a))=q_B(\ell)$, hence $T(a)-\ell\in B$ and
$T(A)\subseteq B+L$.

Conversely, if $T(A)\subseteq B+L$ with $L$ finite-dimensional, then
$q_B(T(A))\subseteq q_B(L)$, and $q_B(L)$ is finite-dimensional. Thus
$T\in E(A,B)$.
:::

:::

::: {.pf-step #R-subring}
$R$ is a subring of $\Endo_K(V)$.

::: pf-proof
The zero endomorphism and the identity lie in $R$, since both send $U$ into
$U$. Let $A,B\in R$. By step [](#finite-dim-lift-criterion){.pf-ref} there are finite-dimensional subspaces
$L_A,L_B\subseteq V$ such that
$$
A(U)\subseteq U+L_A,
\qquad
B(U)\subseteq U+L_B.
$$
Then
$$
(A-B)(U)\subseteq U+(L_A+L_B),
$$
and $L_A+L_B$ is finite-dimensional, so $A-B\in R$ by step [](#finite-dim-lift-criterion){.pf-ref}.
Moreover,
$$
AB(U)
\subseteq A(U+L_B)
\subseteq U+L_A+A(L_B).
$$
The space $L_A+A(L_B)$ is finite-dimensional, so step [](#finite-dim-lift-criterion){.pf-ref} gives
$AB\in R$. Hence $R$ is an additive subgroup closed under multiplication
and containing the identity.
:::

:::

::: {.pf-step #E-V-U-ideal}
$E(V,U)$ is a two-sided ideal of $R$.

::: pf-proof
If $F\in E(V,U)$, then step [](#finite-dim-lift-criterion){.pf-ref} gives a finite-dimensional subspace
$L_F\subseteq V$ such that
$$
F(V)\subseteq U+L_F.
$$
In particular $F(U)\subseteq U+L_F$, so $F\in R$. The zero endomorphism is
in $E(V,U)$, and if $F,G\in E(V,U)$ then, for suitable finite-dimensional
$L_F,L_G$,
$$
(F-G)(V)\subseteq U+(L_F+L_G),
$$
so step [](#finite-dim-lift-criterion){.pf-ref} shows that $F-G\in E(V,U)$. Thus $E(V,U)$ is an additive
subgroup of $R$.

Now let $A\in R$ and $F\in E(V,U)$. Choose finite-dimensional
$L_A,L_F\subseteq V$ with
$$
A(U)\subseteq U+L_A,
\qquad
F(V)\subseteq U+L_F.
$$
Then
$$
AF(V)
\subseteq A(U+L_F)
\subseteq U+L_A+A(L_F),
$$
whose image modulo $U$ is finite-dimensional. Also
$$
FA(V)\subseteq F(V)\subseteq U+L_F.
$$
By step [](#finite-dim-lift-criterion){.pf-ref}, both $AF$ and $FA$ lie in $E(V,U)$. Hence $E(V,U)$ is a
two-sided ideal of $R$.
:::

:::

::: {.pf-step #E-U-0-ideal}
$E(U,0)$ is a two-sided ideal of $R$.

::: pf-proof
An endomorphism $F$ lies in $E(U,0)$ exactly when $F(U)$ is
finite-dimensional. Hence $E(U,0)\subseteq R$, and it is an additive
subgroup because sums and negatives of finite-dimensional images are again
contained in finite-dimensional subspaces.

Let $A\in R$ and $F\in E(U,0)$. By step [](#finite-dim-lift-criterion){.pf-ref}, choose a finite-dimensional
subspace $L_A\subseteq V$ such that $A(U)\subseteq U+L_A$. Since $F(U)$ is
finite-dimensional,
$$
AF(U)=A(F(U))
$$
is finite-dimensional. Also
$$
FA(U)
\subseteq F(U+L_A)
\subseteq F(U)+F(L_A),
$$
and the space on the right is finite-dimensional. Thus both $AF$ and $FA$
belong to $E(U,0)$, proving two-sided absorption.
:::

:::

::: pf-qed
Step [](#R-subring){.pf-ref} proves that $E(U,U)$ is a subring, while steps [](#E-V-U-ideal){.pf-ref} and [](#E-U-0-ideal){.pf-ref}
prove that $E(V,U)$ and $E(U,0)$ are two-sided ideals in it.
:::

:::

:::
