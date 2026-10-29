---
schema: qual/card@1
id: P-UCLAB11F-11
kind: problem
title: Rank-nullity and a quotient-dimension identity
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 11. (a) State and prove the rank-nullity theorem.

(b) Suppose $V,W,U$ are finite-dimensional real vector spaces and $T:V\to W$, $S:W\to U$ are linear maps.
Suppose further that $T$ is one-to-one, $S$ is onto, and $S\circ T=0$.
Prove that
$$
\ker S\supseteq \operatorname{image}T
$$
and that
$$
-\dim V+\dim W-\dim U
=
\dim\bigl(\ker S/\operatorname{image}T\bigr).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The rank-nullity theorem states that for a linear map
$$
L:E\to F
$$
between finite-dimensional vector spaces,
$$
\boxed{\dim E=\dim\ker L+\dim\operatorname{image}L}.
$$


::: pf-proof

Let
$$
e_1,\ldots,e_k
$$
be a basis of $\ker L$, and extend it to a basis
$$
e_1,\ldots,e_k,e_{k+1},\ldots,e_n
$$
of $E$.

The vectors
$$
Le_{k+1},\ldots,Le_n
$$
span $\operatorname{image}L$: if
$$
v=\sum_{i=1}^n a_ie_i,
$$
then
$$
Lv=\sum_{i=k+1}^n a_iLe_i
$$
because $Le_i=0$ for $i\le k$.

They are also linearly independent. If
$$
\sum_{i=k+1}^n a_iLe_i=0,
$$
then
$$
L\left(\sum_{i=k+1}^n a_ie_i\right)=0,
$$
so the vector in parentheses belongs to $\ker L=\operatorname{span}\{e_1,\ldots,e_k\}$. It also belongs to $\operatorname{span}\{e_{k+1},\ldots,e_n\}$. Since the full list is a basis, these two spans intersect only in $0$, so all $a_i=0$.

Thus
$$
\dim\operatorname{image}L=n-k,
$$
while
$$
\dim\ker L=k.
$$
Adding gives
$$
\dim E=n=\dim\ker L+\dim\operatorname{image}L.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\operatorname{image}T\subseteq\ker S.
$$


::: pf-proof

Let $w\in\operatorname{image}T$. Then
$$
w=T(v)
$$
for some $v\in V$. Since
$$
S\circ T=0,
$$
one has
$$
S(w)=S(T(v))=0.
$$
Hence $w\in\ker S$.

:::

:::

::: {.pf-step #s1-3}

Since $T$ is one-to-one,
$$
\dim\operatorname{image}T=\dim V.
$$


::: pf-proof

Injectivity gives
$$
\ker T=\{0\}.
$$
Applying rank-nullity from step [](#s1-1){.pf-ref} to
$$
T:V\to W
$$
gives
$$
\dim V
=
0+\dim\operatorname{image}T.
$$

:::

:::

::: {.pf-step #s1-4}

Since $S$ is onto,
$$
\dim\ker S=\dim W-\dim U.
$$


::: pf-proof

Surjectivity gives
$$
\operatorname{image}S=U.
$$
Applying rank-nullity from step [](#s1-1){.pf-ref} to
$$
S:W\to U
$$
gives
$$
\dim W
=
\dim\ker S+\dim U.
$$
Rearranging yields the claim.

:::

:::

::: {.pf-step #s1-5}

For finite-dimensional spaces with
$$
\operatorname{image}T\subseteq\ker S,
$$
one has
$$
\dim\bigl(\ker S/\operatorname{image}T\bigr)
=
\dim\ker S-\dim\operatorname{image}T.
$$


::: pf-proof

For any finite-dimensional vector space $E$ and subspace $F\subseteq E$,
$$
\dim(E/F)=\dim E-\dim F.
$$
Apply this with
$$
E=\ker S,
\qquad
F=\operatorname{image}T,
$$
using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\dim\bigl(\ker S/\operatorname{image}T\bigr)
=
-\dim V+\dim W-\dim U
}.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref},
$$
\begin{aligned}
\dim\bigl(\ker S/\operatorname{image}T\bigr)
&=
\dim\ker S-\dim\operatorname{image}T\\
&=
(\dim W-\dim U)-\dim V\\
&=
-\dim V+\dim W-\dim U.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states and proves rank-nullity, step [](#s1-2){.pf-ref} proves the inclusion in part (b), and step [](#s1-6){.pf-ref} proves the quotient-dimension identity.

:::

:::

:::
