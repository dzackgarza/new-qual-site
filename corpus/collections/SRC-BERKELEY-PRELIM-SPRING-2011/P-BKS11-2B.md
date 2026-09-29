---
schema: qual/card@1
id: P-BKS11-2B
kind: problem
title: Cayley's theorem with even permutations
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2011 solution PDF and independently reviewed the regular-action and doubled-action embeddings.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked bijectivity and faithfulness of the left regular action for arbitrary groups and evenness of the duplicated action for finite groups.
---

::: {.problem}
Prove that every group is isomorphic to a group of permutations.
Prove that every finite group is isomorphic to a group of even permutations of a finite set.
:::

::: {.solution}
Let $G$ be a group.

::: pf

::: {.pf-step #lambda-bijective}
For each $g\in G$, the map
$$
\lambda_g:G\longrightarrow G,
\qquad
\lambda_g(x)=gx,
$$
is a permutation of the underlying set of $G$.

::: pf-proof
The inverse of $\lambda_g$ is
$$
\lambda_{g^{-1}},
$$
because
$$
\lambda_{g^{-1}}(\lambda_g(x))
=
g^{-1}gx
=
x
$$
and similarly
$$
\lambda_g(\lambda_{g^{-1}}(x))=x.
$$
Thus $\lambda_g$ is bijective.
:::

:::

::: {.pf-step #lambda-injective-hom}
The assignment
$$
\Lambda:G\longrightarrow\operatorname{Sym}(G),
\qquad
g\longmapsto\lambda_g,
$$
is an injective group homomorphism.

::: pf-proof
For $g,h,x\in G$,
$$
\lambda_g(\lambda_h(x))
=
g(hx)
=
(gh)x
=
\lambda_{gh}(x).
$$
Hence
$$
\lambda_g\circ\lambda_h=\lambda_{gh},
$$
so $\Lambda$ is a homomorphism.

If
$$
\lambda_g=\operatorname{id}_G,
$$
then evaluating at the identity element $e\in G$ gives
$$
g
=
ge
=
\lambda_g(e)
=
e.
$$
Thus the kernel is trivial.
:::

:::

::: {.pf-step #cayley-theorem}
Every group is isomorphic to a group of permutations.

::: pf-proof
By step [](#lambda-injective-hom){.pf-ref}, $\Lambda$ identifies $G$ with the subgroup
$$
\Lambda(G)\leq\operatorname{Sym}(G).
$$
This is Cayley's theorem.
:::

:::

::: {.pf-step #rho-injective-hom}
Now suppose $G$ is finite and set
$$
Y\coloneqq G\times\{0,1\}.
$$
For $g\in G$, define
$$
\rho_g:Y\longrightarrow Y,
\qquad
\rho_g(x,i)=(gx,i).
$$
Then
$$
g\longmapsto\rho_g
$$
is an injective homomorphism
$$
G\longrightarrow\operatorname{Sym}(Y).
$$

::: pf-proof
The set $Y$ is finite because $G$ is finite. On each copy
$$
G\times\{i\},
$$
the map $\rho_g$ is exactly a copy of the permutation $\lambda_g$ from
step [](#lambda-bijective){.pf-ref}. Hence it is bijective.

The same multiplication calculation as in step <1>2 gives
$$
\rho_g\rho_h=\rho_{gh},
$$
so the assignment is a homomorphism. If $\rho_g$ is the identity on $Y$,
then
$$
(g,0)
=
\rho_g(e,0)
=
(e,0),
$$
so $g=e$. Thus the homomorphism is injective.
:::

:::

::: {.pf-step #rho-even}
Every permutation $\rho_g$ from step [](#rho-injective-hom){.pf-ref} is even.

::: pf-proof
The permutation $\rho_g$ preserves the two disjoint subsets
$$
G\times\{0\}
\qquad\text{and}\qquad
G\times\{1\},
$$
and its restriction to each is a copy of the same permutation
$\lambda_g$ of $G$. Therefore
$$
\operatorname{sgn}(\rho_g)
=
\operatorname{sgn}(\lambda_g)
\operatorname{sgn}(\lambda_g)
=
\operatorname{sgn}(\lambda_g)^2
=
1.
$$
Hence $\rho_g$ is even.
:::

:::

::: {.pf-step #even-permutation-embedding}
Every finite group is isomorphic to a group of even permutations of
a finite set.

::: pf-proof
By steps [](#rho-injective-hom){.pf-ref} and [](#rho-even){.pf-ref}, the injective homomorphism
$$
G\longrightarrow\operatorname{Sym}(Y)
$$
has image contained in the alternating group
$$
\operatorname{Alt}(Y).
$$
Thus $G$ is isomorphic to the subgroup
$$
\{\rho_g:g\in G\}
\leq
\operatorname{Alt}(Y).
$$
:::

:::

::: pf-qed
Step [](#cayley-theorem){.pf-ref} proves the first assertion, and step [](#even-permutation-embedding){.pf-ref} proves the finite
even-permutation refinement.
:::

:::

:::
