---
schema: qual/card@1
id: E-AMD-JPKP6MG6
kind: problem
title: Every permutation is a product of disjoint cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the orbit decomposition directly and included the usual uniqueness statement.
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard theorem, no repair needed), and the existing prose solution against a
    fresh re-derivation: the orbit relation is an equivalence relation (k = 0 for
    reflexivity, addition of exponents, sigma^{-k} for symmetry); the least return
    time m exists by pigeonhole on |O|+1 iterates, and by minimality the m listed
    elements are distinct, with the division algorithm giving
    O = {a, ..., sigma^{m-1}(a)}; sigma acts on O as that m-cycle; the cycles have
    disjoint supports, hence commute, and their product agrees with sigma
    pointwise; uniqueness because the support of a nontrivial factor is
    sigma-invariant and transitive, hence a single orbit. All correct; the prose's
    least-return-time existence, the distinctness of the listed elements, and the
    uniqueness argument are now given with their reasons. No source solution is
    retained for this card, so no source comparison was made. What was not
    checked: any printed source.
---

::: {.exercise}
Show that every permutation in $S_n$ is a product of disjoint cycles.
:::

::: {.solution}
Let $\sigma\in S_n$ and let $X=\theset{1,\ldots,n}$; write $\sigma^k$ for the $k$-th iterate of $\sigma$, with $\sigma^0=\mathrm{id}$.

::: pf

::: {.pf-step #orbits}
The relation $a\sim b$ defined by $b=\sigma^k(a)$ for some $k\in\ZZ$ is an equivalence relation on $X$, and its classes — the orbits of $\generators{\sigma}$ — partition $X$.

::: pf-proof
Reflexivity is $k=0$. If $b=\sigma^k(a)$ and $c=\sigma^l(b)$ then $c=\sigma^{k+l}(a)$, so the relation is transitive. If $b=\sigma^k(a)$ then $a=\sigma^{-k}(b)$, because $\sigma$ is a bijection with inverse $\sigma^{-1}$ and $\sigma^{-k}$ denotes the $k$-th iterate of that inverse, so the relation is symmetric. Classes of an equivalence relation partition the set.
:::

:::

::: {.pf-step #order}
Let $O$ be an orbit and $a\in O$. Then $m\coloneqq\min\theset{k>0:\sigma^k(a)=a}$ exists, the elements $a,\sigma(a),\ldots,\sigma^{m-1}(a)$ are distinct, and $O=\theset{a,\sigma(a),\ldots,\sigma^{m-1}(a)}$.

::: pf-proof
The set of positive $k$ with $\sigma^k(a)=a$ is nonempty: the elements $\sigma^0(a),\ldots,\sigma^{\abs{O}}(a)$ all lie in the finite set $O$ of size $\abs{O}$, so two of them coincide, say $\sigma^i(a)=\sigma^j(a)$ with $0\leq i<j\leq\abs{O}$, and applying the bijection $\sigma^{-i}$ gives $\sigma^{j-i}(a)=a$ with $j-i>0$. So the minimum $m$ exists.

If $\sigma^i(a)=\sigma^j(a)$ with $0\leq i<j<m$, then $\sigma^{j-i}(a)=a$ with $0<j-i<m$, contradicting the minimality of $m$; so the $m$ listed elements are distinct. Every element of $O$ has the form $\sigma^k(a)$ for some $k\in\ZZ$; writing $k=qm+r$ with $0\leq r<m$ and using $\sigma^m(a)=a$, we get $\sigma^k(a)=\sigma^r(a)$, so $O$ is exactly the listed set, of size $m$.
:::

:::

::: {.pf-step #cycle}
For an orbit $O$ as above, $\sigma$ maps $\sigma^{j}(a)\mapsto\sigma^{j+1}(a)$ for $0\leq j<m-1$ and $\sigma^{m-1}(a)\mapsto a$, that is, $\sigma$ acts on $O$ as the $m$-cycle $(a\ \sigma(a)\ \cdots\ \sigma^{m-1}(a))$.

::: pf-proof
The first assertion is the definition of the iterates, and the last one uses $\sigma^m(a)=a$; these are exactly the transitions of the cycle that lists $a,\sigma(a),\ldots,\sigma^{m-1}(a)$ in that order, whose entries are distinct by step [](#order){.pf-ref}.
:::

:::

::: {.pf-step #product}
Let $c_O$ be the cycle of step [](#cycle){.pf-ref} on the orbit $O$, regarded as a permutation of $X$ fixing the complement of $O$. Then the $c_O$ are pairwise disjoint, they commute, and $\prod_O c_O=\sigma$.

::: pf-proof
Two distinct orbits are disjoint by step [](#orbits){.pf-ref}, and $c_O$ moves exactly the elements of $O$, so the supports of distinct $c_O$ are disjoint; disjoint cycles commute. For $x\in X$, let $O$ be its orbit; then $c_O(x)=\sigma(x)$ by step [](#cycle){.pf-ref}, and every $c_{O'}$ with $O'\neq O$ fixes $x$ because $x\notin O'$. Hence the product sends $x$ to $\sigma(x)$ for every $x$, so it equals $\sigma$.
:::

:::

::: {.pf-step}
Every $\sigma\in S_n$ is a product of disjoint cycles, and the decomposition is unique up to the order of the factors and the insertion or omission of $1$-cycles.

::: pf-proof
Steps [](#orbits){.pf-ref}, [](#order){.pf-ref}, [](#cycle){.pf-ref} and [](#product){.pf-ref} produce such a product. For uniqueness, let $\sigma=d_1\cdots d_r$ be a product of pairwise disjoint cycles, each of length at least $2$. The support of $d_i$ is invariant under $\sigma$, since $\sigma$ agrees with $d_i$ on it and the other factors fix it, so that support is a union of orbits; and $d_i$ acts transitively on its support, which is therefore a single orbit. A $1$-cycle moves nothing and contributes no support, so the nontrivial factors are in bijection with the nontrivial orbits, and each is the cycle read along its orbit from any starting point; hence the factors are determined up to their order and the $1$-cycles.
:::

:::

:::
:::
