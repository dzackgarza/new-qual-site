---
schema: qual/card@1
id: P-MOCTU
kind: problem
title: Free $R$-modules of rank at most $n$ in an $n$-dimensional vector space over
  a PID
classification:
  areas:
  - prelim
  topics:
  - Modules
  - Free Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a PID with field of fractions $F$.
Let $V$ be an $n$-dimensional vector space over $F$.

(a) Show that every finitely generated $R$-submodule $M \subseteq V$ is free of rank $\le n$.

(b) Let $M$ and $N$ be free $R$-submodules of rank $n$ in $V$.
Show that there exists a nonzero element $\alpha \in R$ such that $\alpha M \subseteq N$.
Use this to show that there exists an $R$-basis $\{e_1, \dots, e_n\}$ of $M$ and nonzero elements $\beta_1, \dots, \beta_n \in F$ such that $\{\beta_1 e_1, \dots, \beta_n e_n\}$ is an $R$-basis of $N$ (Invariant Factor Theorem for Lattices).
:::

::: solution
**Goal:** Prove that finitely generated submodules of vector spaces over a PID are torsion-free hence free of rank $\le n$, and prove the simultaneous basis theorem for full-rank lattices.

<1>1. Part (a): Finitely Generated $R$-Submodules of $V$ are Free of Rank $\le n$:
    *Proof:*
    <2>1. Let $M \subseteq V$ be a finitely generated $R$-submodule.
    <2>2. **Torsion-freeness:**
        If $r \in R \setminus \{0\}$ and $v \in M \subseteq V$ satisfy $r \cdot v = 0$, then in the $F$-vector space $V$, multiplying by $r^{-1} \in F$ gives $v = r^{-1}(r v) = 0$.
        Thus $M$ is a **torsion-free $R$-module**.
    <2>3. **Structure Theorem for Finitely Generated Modules over a PID:**
        Every finitely generated module over a PID is isomorphic to $R^k \oplus T(M)$. Since $M$ is torsion-free ($T(M) = 0$), $M$ is **free of finite rank $k$**:
        $$M \cong R^k \quad \text{for some } k \ge 0.$$
    <2>4. **Rank Bound $k \le n$:**
        Let $\{m_1, \dots, m_k\}$ be an $R$-basis of $M$.
        If $\sum_{i=1}^k c_i m_i = 0$ for $c_i \in F$, clear denominators: choose $d \in R \setminus \{0\}$ such that $d c_i \in R$ for all $i$.
        Then $\sum_{i=1}^k (d c_i) m_i = 0$ with $d c_i \in R$. Since $\{m_1, \dots, m_k\}$ is linearly independent over $R$, $d c_i = 0 \implies c_i = 0$.
        Thus $\{m_1, \dots, m_k\}$ is linearly independent over the field $F$.
        Since $\dim_F(V) = n$, any $F$-linearly independent subset has size at most $n$, so $k = \operatorname{rank}_R(M) \le n$.

<1>2. Part (b), Step 1: Existence of $\alpha \in R \setminus \{0\}$ with $\alpha M \subseteq N$:
    *Proof:*
    <2>1. Let $\{u_1, \dots, u_n\}$ be an $R$-basis for $M$, and $\{w_1, \dots, w_n\}$ an $R$-basis for $N$.
    <2>2. Since $N$ has rank $n$, $\{w_1, \dots, w_n\}$ is an $F$-basis for $V$.
    <2>3. Each basis vector $u_i \in M \subseteq V$ can be expanded in the $F$-basis $\{w_j\}$:
        $$u_i = \sum_{j=1}^n \frac{a_{ij}}{b_{ij}} w_j \quad \text{with } a_{ij}, b_{ij} \in R, \; b_{ij} \ne 0.$$
    <2>4. Let $\alpha = \prod_{i, j=1}^n b_{ij} \in R \setminus \{0\}$.
    <2>5. Then for every $i \in \{1, \dots, n\}$:
        $$\alpha u_i = \sum_{j=1}^n \left( \alpha \frac{a_{ij}}{b_{ij}} \right) w_j \in \sum_{j=1}^n R w_j = N.$$
    <2>6. Since $\alpha u_i \in N$ for all generators $u_i$ of $M$, $\alpha M \subseteq N$.

<1>3. Part (b), Step 2: Simultaneous Basis for $M$ and $N$:
    *Proof:*
    <2>1. Consider the submodule $\alpha M \subseteq N$.
    <2>2. Both $\alpha M \cong M$ and $N$ are free $R$-modules of rank $n$, with $\alpha M \subseteq N$.
    <2>3. By the **Submodule Structure Theorem for Free Modules over a PID** (or Smith Normal Form):
        There exists an $R$-basis $\{w_1', \dots, w_n'\}$ of $N$ and nonzero ring elements $d_1, \dots, d_n \in R \setminus \{0\}$ such that:
        $$\{d_1 w_1', d_2 w_2', \dots, d_n w_n'\} \text{ is an } R\text{-basis for } \alpha M.$$
    <2>4. Dividing by $\alpha \in F^\times$, the elements:
        $$e_i \coloneqq \frac{d_i}{\alpha} w_i' \quad (i = 1, \dots, n)$$
        form an $R$-basis for $M = \frac{1}{\alpha}(\alpha M)$.
    <2>5. Solving for $w_i'$ in terms of $e_i$:
        $$w_i' = \left( \frac{\alpha}{d_i} \right) e_i = \beta_i e_i \quad \text{where } \beta_i \coloneqq \frac{\alpha}{d_i} \in F \setminus \{0\}.$$
    <2>6. Since $\{w_1', \dots, w_n'\}$ is an $R$-basis of $N$, the set:
        $$\{\beta_1 e_1, \beta_2 e_2, \dots, \beta_n e_n\}$$
        is an $R$-basis of $N$, where $\{e_1, \dots, e_n\}$ is an $R$-basis of $M$.

<1>4. Conclusion:
    Torsion-free f.g. modules over a PID are free of rank $\le \dim(V)$; clearing denominators embeds $\alpha M \subseteq N$, and Smith Normal Form yields simultaneous bases $\{e_i\}$ of $M$ and $\{\beta_i e_i\}$ of $N$. Q.E.D.
:::
