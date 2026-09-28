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

<1>1. For each $g\in G$, the map
$$
\lambda_g:G\longrightarrow G,
\qquad
\lambda_g(x)=gx,
$$
is a permutation of the underlying set of $G$.

::: {.proof}
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

<1>2. The assignment
$$
\Lambda:G\longrightarrow\operatorname{Sym}(G),
\qquad
g\longmapsto\lambda_g,
$$
is an injective group homomorphism.

::: {.proof}
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

<1>3. Every group is isomorphic to a group of permutations.

::: {.proof}
By step <1>2, $\Lambda$ identifies $G$ with the subgroup
$$
\Lambda(G)\leq\operatorname{Sym}(G).
$$
This is Cayley's theorem.
:::

<1>4. Now suppose $G$ is finite and set
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

::: {.proof}
The set $Y$ is finite because $G$ is finite. On each copy
$$
G\times\{i\},
$$
the map $\rho_g$ is exactly a copy of the permutation $\lambda_g$ from
step <1>1. Hence it is bijective.

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

<1>5. Every permutation $\rho_g$ from step <1>4 is even.

::: {.proof}
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

<1>6. Every finite group is isomorphic to a group of even permutations of
a finite set.

::: {.proof}
By steps <1>4 and <1>5, the injective homomorphism
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

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves the first assertion, and step <1>6 proves the finite
even-permutation refinement.
:::
:::
