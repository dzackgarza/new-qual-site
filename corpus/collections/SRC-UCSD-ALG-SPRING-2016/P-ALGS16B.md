---
schema: qual/card@1
id: P-ALGS16B
kind: problem
title: Groups of order greater than $2$ have a nontrivial automorphism
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Let $G$ be a (not necessarily finite) group with $|G| > 2$.
Prove that there is an automorphism $\varphi \colon G \to G$ other than the identity map.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $G$ is nonabelian, then $G$ has a nontrivial inner automorphism.

::: pf-proof

Choose $g\notin Z(G)$.
Conjugation $c_g(x)=gxg^{-1}$ is an automorphism, and it is not the identity because $g$ is not central.

:::

:::

::: {.pf-step #s2}

Suppose now that $G$ is abelian.
Then inversion $\iota(x)=x^{-1}$ is an automorphism.

::: pf-proof

Because $G$ is abelian, $\iota(xy)=(xy)^{-1}=x^{-1}y^{-1}=\iota(x)\iota(y)$, and $\iota^2=\operatorname{id}_G$.

:::

:::

::: {.pf-step #s3}

If some element has order different from $1$ or $2$, then $\iota\neq\operatorname{id}_G$.

::: pf-proof

For such an element $x$, one has $x^{-1}\neq x$, so inversion moves $x$.

:::

:::

::: {.pf-step #s4}

It remains to consider the case in which every element has order dividing $2$.
Then $G$ is naturally a vector space over $\mathbf F_2$.

::: pf-proof

Use the group law as addition.
Since $x+x=0$ for every $x$, the axioms for an $\mathbf F_2$-vector space hold.

:::

:::

::: {.pf-step #s5}

Since $|G|>2$, this vector space has dimension at least $2$.
Choose linearly independent vectors $e_1,e_2$ and extend them to a basis.

::: pf-proof

A one-dimensional vector space over $\mathbf F_2$ has exactly two elements.
Any linearly independent set extends to a basis.

:::

:::

::: {.pf-step #s6}

The linear map that swaps $e_1$ and $e_2$ and fixes every other basis vector is a nonidentity automorphism of $G$.

::: pf-proof

A permutation of a basis extends uniquely to a linear automorphism.
It is not the identity because it sends $e_1$ to $e_2\neq e_1$.

:::

:::

::: pf-step

Therefore every group $G$ with $|G|>2$ has a nonidentity automorphism.

::: pf-proof

The nonabelian case is Step [](#s1){.pf-ref}; the abelian cases are Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

:::

:::
