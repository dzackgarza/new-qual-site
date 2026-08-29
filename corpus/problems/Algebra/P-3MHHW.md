---
schema: qual/card@1
id: P-3MHHW
kind: problem
title: Local rings via localization and units; primes are primary and irreducible
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Localization
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
- Show that localizing a ring at a prime ideal produces a local ring.

- Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.

- Show that if $R$ is a local ring then $R\setminus R^\times$ is a proper ideal that is contained in the Jacobson radical $J(R)$ (and equals it).

- Show that if $R\neq 0$ is a ring in which every non-unit is nilpotent then $R$ is local.

- Show that every prime ideal is primary.

- Show that every prime ideal is irreducible.
:::

::: solution
**Goal:** Prove six foundational properties of local rings, localization, prime ideals, and primary ideals in commutative algebra.

<1>1. Part 1: Localization at a prime ideal is a local ring:
    *Proof:*
    <2>1. Let $R$ be a commutative ring and $\mathfrak{p} \subset R$ a prime ideal.
    <2>2. The localization $R_\mathfrak{p} = S^{-1}R$ where $S = R \setminus \mathfrak{p}$ is a multiplicatively closed set.
    <2>3. The ideal $\mathfrak{m} = \mathfrak{p} R_\mathfrak{p} = \{a/s \mid a \in \mathfrak{p}, s \in S\}$ is a proper ideal (since $1/1 \notin \mathfrak{m}$).
    <2>4. If $x/s \in R_\mathfrak{p} \setminus \mathfrak{m}$, then $x \notin \mathfrak{p}$, so $x \in S$.
    <2>5. Thus $x/s$ has an inverse $s/x \in R_\mathfrak{p}$, so every element not in $\mathfrak{m}$ is a unit in $R_\mathfrak{p}$.
    <2>6. Every proper ideal consists entirely of non-units, hence is contained in $\mathfrak{m}$. Thus $\mathfrak{m}$ is the unique maximal ideal, so $R_\mathfrak{p}$ is local.

<1>2. Part 2: $R$ is local $\iff$ $\forall x \in R$, $x$ or $1-x$ is a unit:
    *Proof:*
    <2>1. **($\implies$):** Let $(R, \mathfrak{m})$ be local. If neither $x$ nor $1-x$ were units, then $x \in \mathfrak{m}$ and $1-x \in \mathfrak{m}$. Since $\mathfrak{m}$ is an ideal, $1 = x + (1-x) \in \mathfrak{m}$, contradicting that $\mathfrak{m}$ is proper. Thus at least one must be a unit.
    <2>2. **($\impliedby$):** Suppose the condition holds. Let $\mathfrak{m} = R \setminus R^\times$ be the set of non-units. We show $\mathfrak{m}$ is an ideal.
        - If $x \in \mathfrak{m}$ and $r \in R$, $rx \in \mathfrak{m}$ (otherwise $rx \in R^\times \implies x \in R^\times$).
        - If $x, y \in \mathfrak{m}$, suppose $x + y \notin \mathfrak{m}$, so $u = x + y \in R^\times$.
        - Then $u^{-1}x + u^{-1}y = 1$, so $u^{-1}y = 1 - u^{-1}x$.
        - Since $x \in \mathfrak{m}$, $u^{-1}x \in \mathfrak{m}$ is a non-unit.
        - By the given condition, $1 - u^{-1}x = u^{-1}y$ must be a unit, so $y = u(u^{-1}y)$ is a unit, contradicting $y \in \mathfrak{m}$.
        - Thus $x + y \in \mathfrak{m}$, so $\mathfrak{m}$ is an ideal. Since every non-unit lies in $\mathfrak{m}$, $\mathfrak{m}$ is the unique maximal ideal, so $R$ is local.

<1>3. Part 3: In a local ring, $R \setminus R^\times = \mathfrak{m} = J(R)$:
    *Proof:*
    <2>1. By definition, the Jacobson radical $J(R)$ is the intersection of all maximal ideals of $R$.
    <2>2. If $R$ is local with unique maximal ideal $\mathfrak{m}$, then $J(R) = \mathfrak{m}$.
    <2>3. Since every proper ideal is contained in $\mathfrak{m}$, the non-units are precisely the elements of $\mathfrak{m}$: $R \setminus R^\times = \mathfrak{m} = J(R)$.

<1>4. Part 4: If every non-unit is nilpotent in $R \ne 0$, then $R$ is local:
    *Proof:*
    <2>1. Let $\mathfrak{n} = R \setminus R^\times = \operatorname{nil}(R)$ be the set of all nilpotent elements.
    <2>2. In any commutative ring, the nilradical $\operatorname{nil}(R)$ is an ideal (the intersection of all prime ideals).
    <2>3. Since $R \setminus R^\times = \operatorname{nil}(R)$ is an ideal, every non-unit belongs to this unique maximal ideal $\mathfrak{n}$.
    <2>4. Thus $R$ is a local ring (with maximal ideal $\mathfrak{m} = \operatorname{nil}(R)$).

<1>5. Part 5: Every prime ideal is primary:
    *Proof:*
    <2>1. Let $\mathfrak{p} \subset R$ be a prime ideal.
    <2>2. Suppose $xy \in \mathfrak{p}$ and $x \notin \mathfrak{p}$.
    <2>3. Since $\mathfrak{p}$ is prime, $xy \in \mathfrak{p}$ and $x \notin \mathfrak{p}$ implies $y \in \mathfrak{p}$.
    <2>4. Since $y = y^1 \in \mathfrak{p}$, $y^n \in \mathfrak{p}$ holds for $n = 1$.
    <2>5. Thus $\mathfrak{p}$ satisfies the definition of a primary ideal ($\sqrt{\mathfrak{p}} = \mathfrak{p}$).

<1>6. Part 6: Every prime ideal is irreducible:
    *Proof:*
    <2>1. An ideal $I$ is *irreducible* if $I = J \cap K$ implies $I = J$ or $I = K$.
    <2>2. Let $\mathfrak{p}$ be a prime ideal and suppose $\mathfrak{p} = I \cap J$ for ideals $I, J$.
    <2>3. Then $I J \subseteq I \cap J = \mathfrak{p}$.
    <2>4. Because $\mathfrak{p}$ is prime, $IJ \subseteq \mathfrak{p}$ implies $I \subseteq \mathfrak{p}$ or $J \subseteq \mathfrak{p}$.
    <2>5. But $\mathfrak{p} = I \cap J \subseteq I$ and $\mathfrak{p} = I \cap J \subseteq J$.
    <2>6. Thus $I \subseteq \mathfrak{p} \implies I = \mathfrak{p}$, and $J \subseteq \mathfrak{p} \implies J = \mathfrak{p}$.
    <2>7. Therefore $\mathfrak{p}$ is irreducible.

<1>7. Conclusion:
    All six statements have been rigorously proven. Q.E.D.
:::
