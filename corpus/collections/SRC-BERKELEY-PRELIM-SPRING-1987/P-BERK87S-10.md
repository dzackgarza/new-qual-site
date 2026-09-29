---
schema: qual/card@1
id: P-BERK87S-10
kind: problem
title: Embedding of a finite group of order $n$ in the real orthogonal group $O(n)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the left regular action of the group on itself. In the basis indexed
    by group elements, each left translation is a permutation matrix, hence
    orthogonal; evaluating at the identity proves faithfulness.
---

::: {.problem}
Prove that every finite group of order $n$ is isomorphic to a subgroup of
\[
O(n),
\]
the group of real $n\times n$ orthogonal matrices.
:::

::: {.solution}
Let
$$
G=\{g_1,\ldots,g_n\}
$$
be a finite group of order $n$, and let $V$ be the real vector space with
basis
$$
\{e_g:g\in G\}.
$$

::: pf

::: {.pf-step #rho-defined}
For each $a\in G$, define a linear map
$$
\rho(a):V\to V
$$
by
$$
\rho(a)e_g=e_{ag}
$$
for every $g\in G$.

::: pf-proof
Left multiplication
$$
g\longmapsto ag
$$
is a permutation of the set $G$. Hence the displayed prescription sends
the basis of $V$ to a basis and therefore extends uniquely to a linear
automorphism of $V$.
:::

:::

::: {.pf-step #rho-is-homomorphism}
The assignment
$$
\rho:G\to GL(V),
\qquad
a\longmapsto\rho(a),
$$
is a group homomorphism.

::: pf-proof
For $a,b,g\in G$,
$$
\rho(a)\rho(b)e_g
=
\rho(a)e_{bg}
=
e_{abg}
=
\rho(ab)e_g.
$$
Thus
$$
\rho(a)\rho(b)=\rho(ab)
$$
because the two maps agree on a basis.
:::

:::

::: {.pf-step #rho-is-orthogonal}
Each $\rho(a)$ is orthogonal with respect to the inner product for
which the basis $(e_g)_{g\in G}$ is orthonormal.

::: pf-proof
By step [](#rho-defined){.pf-ref}, $\rho(a)$ permutes the orthonormal basis vectors. Hence for
all $g,h\in G$,
$$
\inner{\rho(a)e_g}{\rho(a)e_h}
=
\inner{e_{ag}}{e_{ah}}
=
\delta_{ag,ah}
=
\delta_{g,h}.
$$
By bilinearity, $\rho(a)$ preserves the inner product on all of $V$.
Therefore, after identifying $V$ with $\RR^n$ by this orthonormal basis,
its matrix lies in $O(n)$.
:::

:::

::: {.pf-step #rho-injective}
The homomorphism $\rho$ is injective.

::: pf-proof
Let $e\in G$ denote the identity. If
$$
\rho(a)=\rho(b),
$$
then evaluating both maps on $e_e$ gives
$$
e_a
=
\rho(a)e_e
=
\rho(b)e_e
=
e_b.
$$
Distinct group elements label distinct basis vectors, so $a=b$.
:::

:::

::: {.pf-step #embedding-boxed}
Therefore
$$
\boxed{G\cong\rho(G)\leq O(n)}.
$$

::: pf-proof
Steps [](#rho-is-homomorphism){.pf-ref} and [](#rho-injective){.pf-ref} show that $\rho$ is an injective group
homomorphism, while step [](#rho-is-orthogonal){.pf-ref} shows that every matrix in its image is
orthogonal.
:::

:::

::: pf-qed
Step [](#embedding-boxed){.pf-ref} gives the required isomorphic embedding into $O(n)$.
:::

:::
:::
