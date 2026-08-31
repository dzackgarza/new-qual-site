---
schema: qual/card@1
id: P-J5GIE
kind: problem
title: Definitions of free and torsion-free modules; splitting of $0\to N\to M\to
  F\to 0$ when $F$ is free; finitely generated modules over a PID as torsion plus
  free
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Exact Sequences
relations: []
review: draft
---

::: problem
Let $R$ be a ring with identity $1 \ne 0$.

(a) Give a definition for a free $R$-module.

(b) Define what it means for an $R$-module to be torsion-free.

(c) Prove that if $F$ is a free $R$-module, then any short exact sequence of $R$-modules of the form
$$
0 \to N \xrightarrow{\iota} M \xrightarrow{\pi} F \to 0
$$
splits.

(d) Let $R$ be a principal ideal domain (PID). Show that any finitely generated $R$-module $M$ can be expressed as a direct sum of a torsion module and a free module. (You may assume that every finitely generated torsion-free module over a PID is free.)
:::

::: solution
**Goal:** Define free and torsion-free modules, prove that free modules are projective (surjective maps split), and deduce the direct sum decomposition $M \cong \operatorname{tor}(M) \oplus F$ for finitely generated modules over PIDs.

<1>1. Part (a): Definition of a free $R$-module.
    *Proof:*
    An $R$-module $F$ is called **free** if it satisfies any of the following equivalent conditions:
    1. $F$ possesses an $R$-basis: a subset $B \subseteq F$ such that every element $m \in F$ can be expressed uniquely as a finite $R$-linear combination $m = \sum_{b \in B} r_b b$ with coefficients $r_b \in R$.
    2. $F$ is isomorphic to a direct sum of copies of the regular module $R$: $F \cong \bigoplus_{b \in B} R$.
    3. Universal property of free modules: There exists a subset $B \subseteq F$ such that for every $R$-module $Y$ and every set map $f: B \to Y$, there exists a unique $R$-module homomorphism $\tilde{f}: F \to Y$ such that $\tilde{f}|_B = f$.

<1>2. Part (b): Definition of a torsion-free $R$-module.
    *Proof:*
    Let $R$ be an integral domain (or a commutative ring).
    1. An element $m \in M$ is called a **torsion element** if there exists a non-zero element $r \in R \setminus \{0\}$ such that $r m = 0$.
    2. The **torsion submodule** is $\operatorname{tor}(M) = \{m \in M \mid \exists r \in R \setminus \{0\}, \, r m = 0\}$.
    3. An $R$-module $M$ is called **torsion-free** if $\operatorname{tor}(M) = \{0\}$; that is, for all $r \in R$ and $m \in M$, $r m = 0$ implies $r = 0$ or $m = 0$.

<1>3. Part (c): Splitting of $0 \to N \xrightarrow{\iota} M \xrightarrow{\pi} F \to 0$ when $F$ is free.
    *Proof:*
    <2>1. Let $B \subseteq F$ be an $R$-basis of the free module $F$.
    <2>2. Construct a set map on the basis: Since $\pi: M \to F$ is surjective, for each basis element $b \in B$, the fiber $\pi^{-1}(\{b\})$ is non-empty. Choose an element $y_b \in M$ such that $\pi(y_b) = b$.
    <2>3. Extend to a module homomorphism: By the universal property of the free module $F$ (Part (a)), there exists a unique $R$-module homomorphism $\sigma: F \to M$ such that $\sigma(b) = y_b$ for all $b \in B$.
    <2>4. Verify the section condition $\pi \circ \sigma = \operatorname{id}_F$:
        - For any element $x \in F$, write $x = \sum_{b \in B} r_b b$ as a finite linear combination.
        - Applying $\pi \circ \sigma$:
        $$(\pi \circ \sigma)(x) = \pi\left( \sigma\left( \sum_{b \in B} r_b b \right) \right) = \pi\left( \sum_{b \in B} r_b y_b \right) = \sum_{b \in B} r_b \pi(y_b) = \sum_{b \in B} r_b b = x.$$
        - Thus $\pi \circ \sigma = \operatorname{id}_F$.
    <2>5. By the Splitting Lemma, the exact sequence splits, and $M \cong \iota(N) \oplus \sigma(F) \cong N \oplus F$.

<1>4. Part (d): Decomposition $M \cong \operatorname{tor}(M) \oplus F$ for finitely generated modules over a PID.
    *Proof:*
    <2>1. Define $T = \operatorname{tor}(M)$. Since $R$ is a PID (hence an integral domain), $T$ is an $R$-submodule of $M$.
    <2>2. Consider the canonical short exact sequence:
    $$0 \to T \xrightarrow{\iota} M \xrightarrow{q} M/T \to 0,$$
    where $q(m) = m + T$.
    <2>3. $M/T$ is finitely generated: If $\{x_1, \dots, x_k\}$ generates $M$, then $\{q(x_1), \dots, q(x_k)\}$ generates $M/T$.
    <2>4. $M/T$ is torsion-free:
        - Let $\bar{m} = m + T \in M/T$ and suppose $r \bar{m} = \bar{0}$ in $M/T$ for some $r \in R \setminus \{0\}$.
        - Then $r m \in T = \operatorname{tor}(M)$.
        - By definition of $\operatorname{tor}(M)$, there exists $s \in R \setminus \{0\}$ such that $s (r m) = 0$.
        - By associativity in $M$, $(s r) m = 0$.
        - Since $R$ is an integral domain and $s \ne 0, r \ne 0$, the product $s r \ne 0$.
        - Thus $m \in \operatorname{tor}(M) = T$, which means $\bar{m} = m + T = \bar{0}$ in $M/T$.
        - Therefore $M/T$ is torsion-free.
    <2>5. By the given theorem, every finitely generated torsion-free module over a PID is free, so $F = M/T$ is a free $R$-module.
    <2>6. By Part (c), the short exact sequence splits, yielding an isomorphism:
    $$M \cong T \oplus M/T = \operatorname{tor}(M) \oplus F,$$
    where $\operatorname{tor}(M)$ is a torsion module and $F \cong M/T$ is a free module.

<1>5. Conclusion:
    *Proof:*
    Free modules have bases, torsion-free modules have no non-zero annihilators, surjections onto free modules split, and finitely generated modules over PIDs decompose as $\operatorname{tor}(M) \oplus F$.
:::
