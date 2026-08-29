---
schema: qual/card@1
id: P-NHWAK
kind: problem
title: Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Ideals
  - Algebras
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What is the Jacobson radical $J(R)$ of a ring $R$? State its equivalent characterizations.
(2) If $R$ is a finitely generated commutative algebra over a field $k$, what can you say about $J(R)$ (Jacobson rings and Hilbert's Nullstellensatz)?
:::

::: solution
**Goal:** Define the Jacobson radical $J(R)$ and prove that $J(R) = \operatorname{nil}(R) = \sqrt{(0)}$ for finitely generated commutative algebras over a field $k$.

<1>1. Definition and Characterizations of the Jacobson Radical $J(R)$:
    *Proof:*
    <2>1. For a commutative ring $R$ with 1, the **Jacobson radical** $J(R)$ is defined as the intersection of all maximal ideals of $R$:
        $$J(R) = \bigcap_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m}.$$
    <2>2. **Elementwise characterization:** An element $x \in J(R)$ if and only if $1 - r x$ is a unit in $R$ for all $r \in R$.
        *(Proof: If $x \notin \mathfrak{m}$ for some maximal $\mathfrak{m}$, then $(x) + \mathfrak{m} = R$, so $r x + m = 1 \implies 1 - rx = m \in \mathfrak{m}$ is not a unit. Conversely, if $1 - rx$ is not a unit for some $r$, it is contained in a maximal ideal $\mathfrak{m}$; if $x \in \mathfrak{m}$ then $1 = (1-rx) + rx \in \mathfrak{m}$, a contradiction).*
    <2>3. In general, the nilradical $\operatorname{nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$ is contained in $J(R)$, since every maximal ideal is prime.

<1>2. Commutative $k$-algebras of finite type (Jacobson rings):
    *Proof:*
    <2>1. Let $R = k[x_1, \dots, x_n] / I$ be a finitely generated commutative algebra over a field $k$.
    <2>2. **Hilbert's Nullstellensatz (Weak Form):** For the polynomial ring $k[x_1, \dots, x_n]$, every prime ideal is the intersection of the maximal ideals containing it:
        $$\mathfrak{p} = \bigcap_{\substack{\mathfrak{m} \in \operatorname{MaxSpec}(R) \\ \mathfrak{p} \subseteq \mathfrak{m}}} \mathfrak{m}.$$
    <2>3. A ring with this property is called a **Jacobson ring** (or Hilbert ring).
    <2>4. In particular, any quotient of a polynomial ring over a field is a Jacobson ring.

<1>3. Behavior of $J(R)$ for finitely generated $k$-algebras:
    *Proof:*
    <2>1. In any Jacobson ring $R$, the intersection of all maximal ideals is equal to the intersection of all prime ideals:
        $$J(R) = \bigcap_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m} = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p} = \operatorname{nil}(R) = \sqrt{(0)}.$$
    <2>2. Thus, the Jacobson radical of $R$ coincides with the **nilradical** (the ideal of all nilpotent elements in $R$).
    <2>3. Furthermore, if $R$ is **reduced** (has no non-zero nilpotent elements, e.g. the coordinate ring of an algebraic set), then:
        $$J(R) = (0).$$
    <2>4. If $R$ is finite-dimensional as a $k$-vector space (Artinian algebra), then $J(R)$ is a nilpotent ideal, and $R/J(R)$ is a finite direct product of finite field extensions of $k$.

<1>4. Conclusion:
    $J(R) = \bigcap \mathfrak{m} = \{x \mid 1-rx \in R^\times \ \forall r\}$. For a finitely generated $k$-algebra, $R$ is a Jacobson ring, so $J(R) = \operatorname{nil}(R) = \sqrt{(0)}$, which is $(0)$ if $R$ is reduced. Q.E.D.
:::
