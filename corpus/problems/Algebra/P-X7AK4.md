---
schema: qual/card@1
id: P-X7AK4
kind: problem
title: A finite separable splitting field $L/K$ has $[L:K]=\cardinality{\gal(L/K)}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Separability
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Both directions of the embedding-to-root bijection are now given (including the construction of the embedding from a root through K[x]/(m_alpha)), the count of distinct roots is derived from separability of the minimal polynomial, and the normality step is justified rather than asserted: a K-embedding permutes the roots of a defining polynomial, so the image is a splitting field of that polynomial inside the fixed algebraic closure, hence equal to L. No retained solution set covers the problem (the collection's provenance is the problem list); the card says the argument is its own. No statement repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repair of a review finding on this card. The step identifying the K-embeddings of L into an algebraic closure with Gal(L/K) compared sigma(L) with L inside K-bar without having arranged L subset K-bar, so that comparison was not justified. The card now chooses K-bar to be an algebraic closure of K containing L (an algebraic closure of L is algebraic over K because L/K is finite, so it is one, and it contains L), and the step no longer compares two splitting fields inside K-bar: it shows sigma carries the roots of P in L to roots of P in K-bar, hence sigma(L) subset K(roots of P in K-bar) = L, and concludes sigma(L) = L from injectivity and equality of the finite degrees over K. Nothing else on the card changed.
---

::: {.problem}
Let $L/K$ be a finite separable extension which is the splitting field of a polynomial in $K[x]$. Prove
$$
[L:K]=\cardinality{\Gal(L/K)}.
$$
:::

::: {.solution}
The collection's provenance is the problem list alone, so no retained solution set covers this exercise; the argument is the card's own.

Choose an algebraic closure $\overline K$ of $K$ that contains $L$: an algebraic closure of $L$ is algebraic over $K$, because $L/K$ is algebraic (it is finite), and so it is also an algebraic closure of $K$, and it contains $L$. This choice is what lets the images of $K$-embeddings be compared with $L$ itself. Let $\operatorname{Emb}_K(L,\overline K)$ be the set of injective $K$-homomorphisms $L\to\overline K$.

::: pf

::: {.pf-step #primitive}
$L=K(\alpha)$ for some $\alpha\in L$, and $\deg m_\alpha=[L:K]$, where $m_\alpha$ is the minimal polynomial of $\alpha$ over $K$.

::: pf-proof
$L/K$ is finite and separable, so the primitive element theorem applies. For a primitive element, $[K(\alpha):K]=\deg m_\alpha$ because $1,\alpha,\dots,\alpha^{d-1}$ with $d=\deg m_\alpha$ is a $K$-basis of $K(\alpha)$.
:::

:::

::: {.pf-step #embeddings}
The map $\sigma\mapsto\sigma(\alpha)$ is a bijection from $\operatorname{Emb}_K(L,\overline K)$ onto the set of roots of $m_\alpha$ in $\overline K$.

::: pf-proof
If $\sigma$ is a $K$-homomorphism then $m_\alpha(\sigma(\alpha))=\sigma(m_\alpha(\alpha))=0$, so $\sigma(\alpha)$ is a root; and $\sigma$ is determined by $\sigma(\alpha)$ because $L=K(\alpha)$. Conversely, for a root $\beta$ of $m_\alpha$ the substitution $K[x]\to\overline K$, $x\mapsto\beta$, kills $(m_\alpha)$ and so induces a $K$-homomorphism $K[x]/(m_\alpha)\to\overline K$, which transported along $K[x]/(m_\alpha)\cong L$ (sending $x$ to $\alpha$) is an element of $\operatorname{Emb}_K(L,\overline K)$ with $\alpha\mapsto\beta$.
:::

:::

::: {.pf-step #count}
$m_\alpha$ has exactly $[L:K]$ distinct roots in $\overline K$.

::: pf-proof
$m_\alpha$ is irreducible over $K$ of degree $[L:K]$ by step [](#primitive){.pf-ref}; it is separable because $L/K$ is separable, and a separable irreducible polynomial has no repeated roots in $\overline K$. So it has $\deg m_\alpha=[L:K]$ distinct roots there.
:::

:::

::: {.pf-step #automorphisms}
Every element of $\operatorname{Emb}_K(L,\overline K)$ has image $L$; that is, $\operatorname{Emb}_K(L,\overline K)=\Gal(L/K)$.

::: pf-proof
$L$ is the splitting field over $K$ of some $P\in K[x]$, and $L\subseteq\overline K$ by the choice made at the start, so the roots of $P$ that lie in $L$ are all the roots of $P$ in $\overline K$, and $L=K\bigl(\text{those roots}\bigr)$. Let $\sigma:L\to\overline K$ be a $K$-homomorphism. For a root $\beta\in L$ of $P$ one has $P\bigl(\sigma(\beta)\bigr)=\sigma\bigl(P(\beta)\bigr)=0$ because $\sigma$ fixes $K$ and is a ring homomorphism, so $\sigma$ carries the roots of $P$ in $L$ into the roots of $P$ in $\overline K$; since $\sigma$ fixes $K$,
$$
\sigma(L)=K\bigl(\sigma(\text{roots of }P\text{ in }L)\bigr)\subseteq K\bigl(\text{roots of }P\text{ in }\overline K\bigr)=L .
$$
As $\sigma$ is injective, $[\sigma(L):K]=[L:K]$, so the inclusion of finite extensions forces $\sigma(L)=L$. Thus $\sigma$ is a $K$-automorphism of $L$, and $\operatorname{Emb}_K(L,\overline K)\subseteq\Gal(L/K)$; the reverse inclusion is immediate.
:::

:::

::: {.pf-step}
$[L:K]=\cardinality{\Gal(L/K)}$.

::: pf-proof
$\cardinality{\Gal(L/K)}=\cardinality{\operatorname{Emb}_K(L,\overline K)}$ by step [](#automorphisms){.pf-ref}, and that set is in bijection with the $[L:K]$ roots of $m_\alpha$ by steps [](#embeddings){.pf-ref} and [](#count){.pf-ref}.
:::

:::

:::
:::
