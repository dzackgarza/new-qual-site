---
schema: qual/card@1
id: P-J6BNQ
kind: problem
title: Galois groups of the compositum and intersection of two splitting fields over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - subgroups
relations: []
review: draft
solved: true
---
Let $K$ be a Galois extension of $\QQ$ with Galois group $G$, and let $E_1 , E_2$ be intermediate fields of $K$ which are the splitting fields of irreducible $f_i (x) \in \QQ[x]$. 

Let $E = E_1 E_2 \subset K$. 

Let $H_i = \Gal(K/E_i)$ and $H = \Gal(K/E)$.

a.
Show that $H = H_1 \cap H_2$.

b.
Show that $H_1 H_2$ is a subgroup of $G$.

c.
Show that 
$$
\Gal(K/(E_1 \cap E_2 )) = H_1 H_2
.$$

:::{.concept}
\envlist

- The Galois correspondence:
  - $H_1 \intersect H_2 \mapstofrom E_1 E_2$, 
  - $H_1 H_2 \mapstofrom E_1 \intersect E_2$.
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
By the Galois correspondence, it suffices to show that the fixed field of $H_1 \intersect H_2$ is $E_1 E_2$.

Let $\sigma \in H_1 \intersect H_2$; then $\sigma \in \Aut(K)$ fixes both $E_1$ and $E_2$.

> Not sure if this works -- compositum is not literally product..?

Writing $x \in E_1E_2$ as $x=e_1 e_2$, we have 
$$
\sigma(x) = \sigma(e_1 e_2) = \sigma(e_1) \sigma(e_2) = e_1 e_2  =x,
$$

so $\sigma$ fixes $E_1 E_2$.

:::

:::{.proof title="of b"}
That $H_1 H_2 \subseteq G$ is clear, since if $\sigma = \tau_1 \tau_2 \in H_1 H_2$, then each $\tau_i$ is an automorphism of $K$ that fixes $E_i \supseteq \QQ$, so each $\tau_i$ fixes $\QQ$ and thus $\sigma$ fixes $\QQ$.

:::{.claim}
All elements in this subset commute.
:::

:::{.proof title="of claim"}
\envlist

- Let $\sigma = \sigma_1 \sigma_2 \in H_1 H_2$.

- Note that $\sigma_1(e) = e$ for all $e\in E_1$ by definition, since $H_1$ fixes $E_1$, and $\sigma_2(e) \in E_1$ (?).

- Then 
  \[
  \sigma_1(e) = e \quad \forall e \in E_1 \implies \sigma_1(\sigma_2(e)) = \sigma_2(e) 
  \]
  and substituting $e = \sigma_1(e)$ on the RHS yields
  \[
  \sigma_1 \sigma_2(e) = \sigma_2 \sigma_1(e)
  ,\]
  where a similar proof holds for $e\in E_2$ and thus for arbitrary $x\in E_1 E_2$.

:::
 


:::

:::{.proof title="of c"}
By the Galois correspondence, the subgroup $H_1H_2 \leq G$ will correspond to an intermediate field $E$ such that $K/E/\QQ$ and $E$ is the fixed field of $H_1 H_2$.

But if $\sigma \in H_1 H_2$, then $\sigma = \tau_1 \tau_2$ where $\tau_i$ is an automorphism of $K$ that fixes $E_i$, and so 
\[
\sigma(x) = x \iff \tau_1\tau_2(x) = x
&\iff \tau_2(x) = x 
\\
&~\&~ 
\\
\tau_1(x) = x &\iff x \in E_1 \intersect E_2
.\].

:::

:::

