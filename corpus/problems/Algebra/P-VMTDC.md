---
schema: qual/card@1
id: P-VMTDC
kind: problem
title: Maschke's theorem
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and prove Maschke's theorem.
What can go wrong if you work over the real field?
What can go wrong in characteristic $p$?
:::

::: solution
**Goal:** State and prove Maschke's Theorem, clarify the real representation case (where Maschke still holds but Schur's lemma / irreducibles change), and explain the failure of semisimplicity in modular representation theory (characteristic $p \mid |G|$).

<1>1. Statement of Maschke's Theorem:
    *Proof:*
    <2>1. **Theorem (Maschke):** Let $G$ be a finite group and $k$ a field whose characteristic does not divide $|G|$ (i.e. $\operatorname{char}(k) = 0$ or $\operatorname{char}(k) \nmid |G|$).
    <2>2. Let $V$ be a finite-dimensional representation of $G$ over $k$, and let $W \subseteq V$ be a $G$-invariant subspace (subrepresentation).
    <2>3. Then there exists a $G$-invariant subspace $W' \subseteq V$ such that:
        $$V = W \oplus W'.$$
    <2>4. Equivalently, every representation of $G$ over $k$ is completely reducible (semisimple), and the group algebra $k[G]$ is a semisimple ring.

<1>2. Proof of Maschke's Theorem (Averaging / Reynolds Operator):
    *Proof:*
    <2>1. Since $W \subseteq V$ is a vector subspace, choose any $k$-linear projection $\pi_0: V \to W$ (so $\pi_0|_W = \operatorname{id}_W$ and $\operatorname{im}\pi_0 = W$).
    <2>2. Define the **averaged operator** $\pi: V \to V$ by:
        $$\pi(v) = \frac{1}{|G|} \sum_{g \in G} g \cdot \pi_0(g^{-1} \cdot v).$$
        (This is well-defined because $|G| \ne 0$ in $k$).
    <2>3. **$\pi$ maps into $W$:** For any $v \in V$, $\pi_0(g^{-1} \cdot v) \in W$. Since $W$ is $G$-invariant, $g \cdot \pi_0(g^{-1} \cdot v) \in W$. Thus $\pi(v)$ is a linear combination of elements of $W$, so $\operatorname{im}\pi \subseteq W$.
    <2>4. **$\pi|_W = \operatorname{id}_W$:** For $w \in W$, $g^{-1} \cdot w \in W$, so $\pi_0(g^{-1} \cdot w) = g^{-1} \cdot w$. Then:
        $$\pi(w) = \frac{1}{|G|} \sum_{g \in G} g \cdot (g^{-1} \cdot w) = \frac{1}{|G|} \sum_{g \in G} w = \frac{|G|}{|G|} w = w.$$
    <2>5. **$\pi$ is $G$-equivariant ($G$-linear):** For any $h \in G$ and $v \in V$:
        $$\pi(h \cdot v) = \frac{1}{|G|} \sum_{g \in G} g \cdot \pi_0(g^{-1} h \cdot v) = \frac{1}{|G|} \sum_{u \in G} (h u) \cdot \pi_0(u^{-1} \cdot v) = h \cdot \pi(v)$$
        where we made the change of index $u = h^{-1} g$.
    <2>6. Set $W' = \ker\pi$.
        - Because $\pi$ is $G$-linear, $W' = \ker\pi$ is a $G$-invariant subspace.
        - Because $\pi$ is a projection onto $W$ ($\pi^2 = \pi$ and $\operatorname{im}\pi = W$), $V = \operatorname{im}\pi \oplus \ker\pi = W \oplus W'$.

<1>3. What happens over the real field $\mathbb{R}$?
    *Proof:*
    <2>1. Maschke's Theorem **still holds** over $\mathbb{R}$ because $\operatorname{char}(\mathbb{R}) = 0 \nmid |G|$: every real representation is completely reducible!
    <2>2. What changes compared to $\mathbb{C}$ is **irreducibility and Schur's Lemma**:
        - Irreducible real representations need not be 1-dimensional even for abelian groups (e.g. the standard 2D rotation representation of $\mathbb{Z}/n\mathbb{Z}$ for $n \ge 3$ is irreducible over $\mathbb{R}$ but splits into two 1D representations over $\mathbb{C}$).
        - By Schur's lemma, the endomorphism ring $\operatorname{End}_G(V)$ of an irreducible real representation can be $\mathbb{R}$, $\mathbb{C}$, or the quaternions $\mathbb{H}$ (Frobenius-Schur indicator).

<1>4. What can go wrong in characteristic $p$ ($p \mid |G|$)?
    *Proof:*
    <2>1. If $p \mid |G|$, the factor $\frac{1}{|G|}$ is undefined in $k$ ($|G| = 0$ in $k$), so the Reynolds averaging operator cannot be formed.
    <2>2. **Counterexample (failure of semisimplicity):**
        - Let $G = \mathbb{Z}/p\mathbb{Z} = \langle g \rangle$ and $k = \mathbb{F}_p$.
        - Consider the 2-dimensional representation $\rho: G \to \operatorname{GL}_2(\mathbb{F}_p)$ defined by:
            $$\rho(g) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
        - Note $\rho(g^k) = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, so $\rho(g^p) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$, so $\rho$ is a valid representation.
        - The 1-dimensional subspace $W = \operatorname{span}\{(1, 0)^T\}$ is $G$-invariant.
        - However, the only 1-dimensional invariant subspaces of $\rho$ correspond to eigenvectors of $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
        - The only eigenvalue is $\lambda = 1$, and its eigenspace is precisely $W = \operatorname{span}\{(1, 0)^T\}$.
        - Thus, there is **no other 1-dimensional $G$-invariant subspace** $W'$ to complement $W$.
        - Therefore, $V$ is indecomposable but not irreducible (an uniserial representation of length 2). Complete reducibility fails.

<1>5. Conclusion:
    Maschke's Theorem holds whenever $\operatorname{char}(k) \nmid |G|$ via the averaging projection $\pi = \frac{1}{|G|}\sum g \pi_0 g^{-1}$. It holds over $\mathbb{R}$ (complete reducibility holds, but 1D irreducibles/Schur lemma differ), and fails in characteristic $p \mid |G|$ (exhibited by Jordan blocks $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{F}_p$). Q.E.D.
:::
