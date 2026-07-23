---
schema: qual/card@1
id: P-4IKVH
kind: problem
title: "Let $G$ be a group of order $p^2q$ for $p, q$ prime. Show that $G$ has\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $G$ be a group of order $p^2q$ for $p, q$ prime. Show that $G$ has a nontrivial normal subgroup.

:::{.solution}
\envlist

- Write $\size G = p^2 q$
- Cases: first assume $p>q$, then do $q<p$.
- In any case, we have
\[
n_p \divides q &\implies n_p \in \ts{ 1,q } \\ \\
n_q \divides p^2 &\implies n_q \in \ts{ 1, p, p^2} 
.\]

- If $n_p=1$ or $n_q=1$, we're done, so suppose otherwise.

- **Case 1:** $:p>q$.
  - Using that $[n_p]_p \equiv 1$, consider reducing elements in $\ts{1, q} \mod p$.
  - Since $q<p$, we just have $q\mod p = q$, and as long as $q\neq 1$ we have $q\not\equiv 1\mod p$.
    But since $n_p\neq 1$ and $n_p\neq q$, this is a contradiction. $\contradiction$

- **Case 2:** $p< q$:
  - Using that $[n_q]_q \equiv 1$, consider reducing $\ts{1, p, p^2}\mod q$.
  - Since now $p<q$, we have $p\mod q = p$ itself, so $p\mod q \neq 1$ and we can rule it out.
  - The remaining possibility is $n_q = p^2$.
  - Supposing that $n_p \neq 1$, we have $n_p=q$, so we can count 
  \[
  \text{Elements from Sylow } q: n_q( \size S_q - 1) &= p^2(q-1) + 1
  ,\]
  where we've used that distinct Sylow $q$s can only intersect at the identity, and although Sylow $p$s *can* intersect trivially, they can also intersect in a subgroup of size $p$.
  - Suppose all Sylow $p$s intersect trivially, we get at least
  \[
  \text{Elements from Sylow } p: n_p( \size S_p - 1) &= q(p^2-1) 
  .\]
  Then we get a count of how many elements the Sylow $p$s and $q$s contribute:
  \[
  q(p^2-1) + p^2(q-1) + 1
  = p^2q - q + p^2q - p^2 + 1 
  = p^2q + (p^2-1)(q-1)
  > p^2q = \size G
  ,\]
  provided $(p^2-1)(q-1) \neq 0$, which is fine for $p\geq 2$ since this is at least $(2^2-1)(3-2) = 3$ (since $p<q$ and $q=3$ is the next smallest prime). $\contradiction$

  - Otherwise, we get two Sylow $p$s intersecting nontrivially, which must be in a subgroup of order at least $p$ since the intersection is a subgroup of both.
  In this case, just considering these two subgroups, we get
  \[
  \text{Elements from Sylow } p: n_p( \size S_p - 1) &> p^2 + p^2 - p = 2p^2-p -1
  .\]
  Then a count:
  \[
  p^2(q-1) + (2p^2-p - 1) + 1
  &= p^2 q- p^2 + 2p^2 -p \\
  &= p^2 q + p^2 -p \\
  &= p^2q + p(p-1) \\
  &> p^2q = \size G
  ,\]
  a contradiction since this inequality is strict provided $p\geq 2$. $\contradiction$

:::

