---
schema: qual/card@1
id: P-JTRQ2
kind: problem
title: Injective module
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is an injective module over a ring $R$?
State Baer's Criterion and the characterization of injective modules over PIDs (divisible modules).
:::

::: solution
**Goal:** Define injective modules, characterize them via exact contravariant Hom functors, state Baer's Criterion, and detail the equivalence with divisible modules over PIDs.

<1>1. Categorical and Lifting Definition:
    *Proof:*
    <2>1. Let $R$ be a ring (with 1). A left $R$-module $Q$ is **injective** if for every injective $R$-module homomorphism $i: A \hookrightarrow B$ and every homomorphism $f: A \to Q$, there exists a homomorphism $g: B \to Q$ extending $f$ (i.e. $g \circ i = f$):
        $$\begin{array}{ccc}
        0 \longrightarrow A & \xrightarrow{i} & B \\
        \phantom{0 \longrightarrow} \Big\downarrow \scriptstyle f & \swarrow \scriptstyle g & \\
        Q & &
        \end{array}$$
    <2>2. **Equivalent Functorial Definition:** $Q$ is injective if and only if the contravariant functor $\operatorname{Hom}_R(-, Q)$ is **exact** (sends short exact sequences to short exact sequences).

<1>2. Baer's Criterion:
    *Proof:*
    <2>1. **Theorem (Baer, 1940):** An $R$-module $Q$ is injective if and only if for every left ideal $I \subseteq R$, any $R$-module homomorphism $f: I \to Q$ can be extended to an $R$-module homomorphism $g: R \to Q$:
        $$\begin{array}{ccc}
        0 \longrightarrow I & \hookrightarrow & R \\
        \phantom{0 \longrightarrow} \Big\downarrow \scriptstyle f & \swarrow \scriptstyle g & \\
        Q & &
        \end{array}$$
    <2>2. *Proof Idea:* Zorn's Lemma applied to the poset of partial extensions of homomorphisms from submodules of $B$ into $Q$.

<1>3. Injective Modules over Principal Ideal Domains (Divisibility):
    *Proof:*
    <2>1. An $R$-module $M$ over an integral domain $R$ is **divisible** if for every $r \in R \setminus \{0\}$ and every $m \in M$, there exists $y \in M$ such that $r y = m$ (i.e. the multiplication map $r \cdot: M \to M$ is surjective).
    <2>2. **Theorem:** Let $R$ be a PID (e.g. $R = \mathbb{Z}$ or $R = k[x]$). An $R$-module $Q$ is injective if and only if $Q$ is **divisible**.
    <2>3. *Proof via Baer's Criterion:*
        - In a PID, every ideal is principal: $I = (r) = Rr$.
        - A homomorphism $f: (r) \to Q$ is completely determined by $f(r) = q \in Q$.
        - An extension $g: R \to Q$ is determined by $g(1) = y \in Q$ such that $r y = g(r) = f(r) = q$.
        - Such an element $y$ exists for all $q \in Q$ and $r \ne 0 \iff Q$ is divisible.

<1>4. Examples:
    *Proof:*
    <2>1. Over $R = \mathbb{Z}$ (Abelian groups), the injective modules are the divisible abelian groups:
        $$\mathbb{Q}, \quad \mathbb{Q}/\mathbb{Z}, \quad \mathbb{Z}(p^\infty) \text{ (Prüfer } p\text{-group)}.$$
    <2>2. The field of fractions $K = \operatorname{Frac}(R)$ of any integral domain is an injective $R$-module.

<1>5. Conclusion:
    An injective module admits lifting of homomorphisms, is characterized by Baer's criterion on ideals $I \subseteq R$, and is equivalent to divisibility over PIDs. Q.E.D.
:::
