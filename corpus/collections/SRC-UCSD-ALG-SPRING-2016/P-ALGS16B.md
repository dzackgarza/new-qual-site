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

::: problem
Let $G$ be a (not necessarily finite) group with $|G| > 2$.
Prove that there is an automorphism $\varphi \colon G \to G$ other than the identity map.
:::

::: {.solution}
<1>1. If $G$ is nonabelian, then $G$ has a nontrivial inner automorphism.
::: {.proof}
Choose $g\notin Z(G)$.
Conjugation $c_g(x)=gxg^{-1}$ is an automorphism, and it is not the identity because $g$ is not central.
:::

<1>2. Suppose now that $G$ is abelian.
Then inversion $\iota(x)=x^{-1}$ is an automorphism.
::: {.proof}
Because $G$ is abelian, $\iota(xy)=(xy)^{-1}=x^{-1}y^{-1}=\iota(x)\iota(y)$, and $\iota^2=\operatorname{id}_G$.
:::

<1>3. If some element has order different from $1$ or $2$, then $\iota\neq\operatorname{id}_G$.
::: {.proof}
For such an element $x$, one has $x^{-1}\neq x$, so inversion moves $x$.
:::

<1>4. It remains to consider the case in which every element has order dividing $2$.
Then $G$ is naturally a vector space over $\mathbf F_2$.
::: {.proof}
Use the group law as addition.
Since $x+x=0$ for every $x$, the axioms for an $\mathbf F_2$-vector space hold.
:::

<1>5. Since $|G|>2$, this vector space has dimension at least $2$.
Choose linearly independent vectors $e_1,e_2$ and extend them to a basis.
::: {.proof}
A one-dimensional vector space over $\mathbf F_2$ has exactly two elements.
Any linearly independent set extends to a basis.
:::

<1>6. The linear map that swaps $e_1$ and $e_2$ and fixes every other basis vector is a nonidentity automorphism of $G$.
::: {.proof}
A permutation of a basis extends uniquely to a linear automorphism.
It is not the identity because it sends $e_1$ to $e_2\neq e_1$.
:::

<1>7. Therefore every group $G$ with $|G|>2$ has a nonidentity automorphism.
::: {.proof}
The nonabelian case is Step <1>1; the abelian cases are Steps <1>2--<1>6.
:::
:::
