---
schema: qual/card@1
id: P-ZFCV4
kind: problem
title: Galois-group conditions implied by irreducibility of a polynomial, and by a
  root in the base field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Group Actions
  - Irreducibility Criteria
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Tell me a condition on the Galois group which is implied by irreducibility of the polynomial.
What happens when the polynomial has a root in the base field?
:::

::: solution
**Theorem.**  
Let $f\in F[x]$ be irreducible of degree $n\ge1$ and let $L$ be its splitting field.
Then $G=\mathrm{Gal}(L/F)$ acts transitively on the $n$ roots of $f$.
If $f$ has a root in $F$, then $n=1$, so $L=F$ and $G$ is trivial.

1. Let $\alpha,\beta$ be roots of $f$ in $L$.
   Each generates an $F$-embedding $F(\alpha)\hookrightarrow L$ with $\alpha\mapsto\beta$.
2. Because $L/F$ is normal, any such embedding extends to an $F$-automorphism $\sigma\in G$.
3. Then $\sigma(\alpha)=\beta$, so every root is in the $G$-orbit of every other root.
   Hence the action is transitive.

4. If $f$ has a root $\alpha\in F$, then $x-\alpha$ divides $f$ in $F[x]$.
   Irreducibility forces $f(x)=x-\alpha$ (degree $1$).
5. For degree $1$ there is no nontrivial splitting field extension, so $L=F$ and $G=\{1\}$.
:::
