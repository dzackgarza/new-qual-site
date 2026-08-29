---
schema: qual/card@1
id: P-QYCPP
kind: problem
title: Sylow $p$-subgroups of $\GL_3(\FF_p)$, their conjugates, and their normalizers
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G = \operatorname{GL}_3(\mathbb{F}_p)$ for $p$ prime.
(1) What is the order of $G$, and what is the order of a Sylow $p$-subgroup?
(2) Give the standard matrix form for the canonical Sylow $p$-subgroup $P \le G$.
(3) Give the matrix form for the normalizer $N_G(P)$ and compute the number of conjugates (Sylow $p$-subgroups) $n_p$.
(4) Explain conjugacy of Sylow $p$-subgroups in terms of complete flags / eigenspaces.
:::

::: solution
**Goal:** Compute the Sylow $p$-subgroups of $\operatorname{GL}_3(\mathbb{F}_p)$, their matrix form, normalizer, and flag-variety geometric interpretation.

<1>1. Order of $G = \operatorname{GL}_3(\mathbb{F}_p)$ and Sylow $p$-subgroup order:
    *Proof:*
    <2>1. By counting linearly independent columns in $\mathbb{F}_p^3$:
        $$|G| = (p^3 - 1)(p^3 - p)(p^3 - p^2) = p^3 (p^3 - 1)(p^2 - 1)(p - 1) = p^3 (p - 1)^3 (p + 1)(p^2 + p + 1).$$
    <2>2. The highest power of $p$ dividing $|G|$ is $p^3$.
    <2>3. Thus, every Sylow $p$-subgroup of $G$ has order $|P| = p^3$.

<1>2. Matrix Form of the Canonical Sylow $p$-subgroup $U_3(\mathbb{F}_p)$:
    *Proof:*
    <2>1. The group of **strictly upper-triangular unipotent matrices**:
        $$P = U_3(\mathbb{F}_p) = \left\{ \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} \;\middle|\; a, b, c \in \mathbb{F}_p \right\}.$$
    <2>2. The size of this subgroup is $p \times p \times p = p^3$, so $P$ is a Sylow $p$-subgroup of $\operatorname{GL}_3(\mathbb{F}_p)$ (isomorphic to the Heisenberg group over $\mathbb{F}_p$).

<1>3. Normalizer $N_G(P)$ (The Standard Borel Subgroup $B$):
    *Proof:*
    <2>1. An invertible matrix $M$ normalizes $P = U_3(\mathbb{F}_p)$ if and only if $M$ is **upper-triangular** (the standard Borel subgroup $B$):
        $$N_G(P) = B_3(\mathbb{F}_p) = \left\{ \begin{pmatrix} d_1 & a & b \\ 0 & d_2 & c \\ 0 & 0 & d_3 \end{pmatrix} \;\middle|\; d_1, d_2, d_3 \in \mathbb{F}_p^\times, \; a, b, c \in \mathbb{F}_p \right\}.$$
    <2>2. **Size of the Normalizer:**
        $$|N_G(P)| = (p - 1)^3 p^3.$$
    <2>3. **Number of Sylow $p$-subgroups (Conjugates):**
        By the Orbit-Stabilizer Theorem / Sylow's Third Theorem:
        $$n_p = [G : N_G(P)] = \frac{|G|}{|N_G(P)|} = \frac{p^3 (p - 1)^3 (p + 1)(p^2 + p + 1)}{p^3 (p - 1)^3} = (p + 1)(p^2 + p + 1) = (p + 1)(p + 1 + p^2).$$
        Note that $(p+1)(p^2+p+1) = p^3 + 2p^2 + 2p + 1 \equiv 1 \pmod p$, matching Sylow's congruence $n_p \equiv 1 \pmod p$.

<1>4. Geometric Interpretation in terms of Flags and Eigenvectors:
    *Proof:*
    <2>1. Every matrix in $P = U_3(\mathbb{F}_p)$ is unipotent with single eigenvalue $\lambda = 1$ of algebraic multiplicity 3.
    <2>2. A matrix $u \in U_3(\mathbb{F}_p)$ stabilizes the standard complete flag of subspaces:
        $$\mathcal{F}_0: \quad \{0\} \subset V_1 = \operatorname{span}(e_1) \subset V_2 = \operatorname{span}(e_1, e_2) \subset V_3 = \mathbb{F}_p^3.$$
    <2>3. Any conjugate subgroup $g P g^{-1}$ is the unipotent stabilizer of the transformed complete flag $g \mathcal{F}_0$:
        $$\mathcal{F}: \quad \{0\} \subset W_1 = g V_1 \subset W_2 = g V_2 \subset \mathbb{F}_p^3.$$
    <2>4. The set of Sylow $p$-subgroups is in bijection with the **flag variety** $\operatorname{Flags}(\mathbb{F}_p^3)$ (the set of all complete flags of $\mathbb{F}_p^3$):
        - Number of 1D subspaces $W_1 \subset \mathbb{F}_p^3$: $\frac{p^3 - 1}{p - 1} = p^2 + p + 1$.
        - Number of 2D subspaces $W_2$ containing a fixed $W_1$: $\frac{p^2 - 1}{p - 1} = p + 1$.
        - Total number of complete flags: $(p^2 + p + 1)(p + 1) = n_p$.

<1>5. Conclusion:
    The Sylow $p$-subgroups are unipotent upper-triangular matrices $U_3(\mathbb{F}_p)$ of order $p^3$, normalized by the Borel subgroup $B$, with $n_p = (p+1)(p^2+p+1)$ conjugates corresponding bijectively to complete flags in $\mathbb{F}_p^3$. Q.E.D.
:::
