---
schema: qual/card@1
id: PR-TNVSI
kind: proposition
title: Irreducible decomposition in a Noetherian space
slogan: 'Noetherian closed sets split into finitely many maximal irreducible pieces, uniquely; algebraically these are the minimal primes.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Noetherian Spaces
  - Varieties
relations:
- kind: uses
  target: D-9DIKB
review: draft
prompts:
- Decompose a closed algebraic set into irreducibles.
- In what sense is the decomposition into irreducible components unique?
---

::: {.proposition}
Every closed subset $X$ of a Noetherian space is a finite union
$$
X = X_1 \union \cdots \union X_r
$$
of irreducible closed subsets.
If no $X_i$ contains another, then the $X_i$ are exactly the [[D-9DIKB|irreducible components]] of $X$ and are uniquely determined up to permutation.
:::

::: {.proof}
Existence follows by Noetherian induction on closed subsets. If a nonempty closed subset $Z$ is irreducible, it is already a finite union of irreducible closed subsets. Otherwise write
$$
Z=Z_1\cup Z_2
$$
with $Z_1,Z_2\subsetneq Z$ closed. By induction each $Z_i$ is a finite union of irreducible closed subsets, hence so is $Z$. Removing any member contained in another produces a decomposition with no inclusions among the remaining terms.

For uniqueness, suppose
$$
X=X_1\cup\cdots\cup X_r=Y_1\cup\cdots\cup Y_s
$$
are two finite irreducible decompositions with no containment among distinct members of either family. Since $X_i$ is irreducible and is contained in the finite union $\bigcup_jY_j$, one has $X_i\subseteq Y_j$ for some $j$. Likewise $Y_j\subseteq X_k$ for some $k$. Hence
$$
X_i\subseteq Y_j\subseteq X_k,
$$
so the no-containment condition forces $X_i=X_k=Y_j$. Thus every $X_i$ occurs among the $Y_j$, and conversely.
:::

::: {.remark}
If $R$ is Noetherian and $J\subseteq R$, then the irreducible components of $V(J)\subseteq\Spec R$ are
$$
V(\mfp_1),\ldots,V(\mfp_r),
$$
where the $\mfp_i$ are the minimal prime ideals over $J$.

For a polynomial ring over a field, if
$$
f=u\prod_{i=1}^r f_i^{e_i}
$$
with the $f_i$ pairwise nonassociate irreducible polynomials, then the irreducible components of $V(f)$ are the $V(f_i)$. The exponents $e_i$ do not affect the underlying topological space but are retained by the nonreduced scheme $\Spec k[x_1,\ldots,x_n]/(f)$.
:::
