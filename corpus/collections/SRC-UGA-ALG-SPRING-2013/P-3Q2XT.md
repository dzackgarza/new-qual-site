---
schema: qual/card@1
id: P-3Q2XT
kind: problem
title: Euclidean domains are UFDs; a UFD need not be Euclidean
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Factorization
  - Principal Ideal Domains
relations: []
review: draft
---

::: problem
(a) Define a **Euclidean domain**.

(b) Define a **unique factorization domain (UFD)**.

(c) Is every Euclidean domain a UFD? Give either a proof or a counterexample with justification.

(d) Is every UFD a Euclidean domain? Give either a proof or a counterexample with justification.
:::

::: solution
**Goal:** Define Euclidean domains and UFDs, prove that every Euclidean domain is a UFD in (c), and provide a counterexample showing the converse is false in (d).

<1>1. Part (a): Definition of a Euclidean domain.
    *Proof:*
    <2>1. An integral domain $R$ is a Euclidean domain if there exists a function $N: R \setminus \{0\} \to \mathbb{Z}_{\ge 0}$ (called a Euclidean norm or degree function) satisfying the division algorithm:
    <2>2. For any $a, b \in R$ with $b \ne 0$, there exist elements $q, r \in R$ such that
    $$a = b q + r,$$
    where either $r = 0$ or $N(r) < N(b)$.

<1>2. Part (b): Definition of a unique factorization domain (UFD).
    *Proof:*
    <2>1. An integral domain $R$ is a Unique Factorization Domain (UFD) if:
    <2>2. Existence of factorization: Every non-zero non-unit $r \in R$ can be written as a product of irreducibles,
    $$r = p_1 p_2 \cdots p_n,$$
    where $n \ge 1$ and each $p_i \in R$ is irreducible.
    <2>3. Uniqueness of factorization: If $r = p_1 \cdots p_n = q_1 \cdots q_m$ are two factorizations into irreducibles, then $n = m$ and there exists a permutation $\sigma \in S_n$ such that $p_i$ is an associate of $q_{\sigma(i)}$ (i.e. $p_i = u_i q_{\sigma(i)}$ for some unit $u_i \in R^\times$) for all $1 \le i \le n$.

<1>3. Part (c): Every Euclidean domain is a UFD.
    *Proof:*
    <2>1. Substep 1: Every Euclidean domain $R$ is a Principal Ideal Domain (PID).
        *Proof:* Let $I \subseteq R$ be an ideal. If $I = \{0\}$, then $I = \langle 0 \rangle$ is principal. If $I \ne \{0\}$, the set $\{N(x) : x \in I \setminus \{0\}\} \subset \mathbb{Z}_{\ge 0}$ is non-empty and has a minimal element; choose $b \in I \setminus \{0\}$ achieving this minimal norm. For any $a \in I$, write $a = b q + r$ with $r = 0$ or $N(r) < N(b)$. Since $r = a - b q \in I$, minimality of $N(b)$ forces $r = 0$, so $a = b q \in \langle b \rangle$. Thus $I = \langle b \rangle$.
    <2>2. Substep 2: In a PID, every non-zero non-unit factors into irreducibles.
        *Proof:* Every PID is Noetherian (every ideal is finitely generated), so $R$ satisfies the ascending chain condition on principal ideals (ACCP). If a non-zero non-unit $r$ could not be factored into irreducibles, one could construct a strictly ascending chain of principal ideals $\langle r \rangle \subsetneq \langle r_1 \rangle \subsetneq \langle r_2 \rangle \subsetneq \cdots$, contradicting the ACCP.
    <2>3. Substep 3: In a PID, every irreducible element is prime.
        *Proof:* Let $p \in R$ be irreducible, and suppose $p \mid a b$. If $p \nmid a$, the ideal $\langle p, a \rangle = \langle d \rangle$ since $R$ is a PID. Since $d \mid p$ and $p$ is irreducible, either $d$ is a unit or $d$ is an associate of $p$. Since $p \nmid a$, $d$ cannot be an associate of $p$, so $\langle d \rangle = R$. Thus $1 = x p + y a$ for some $x, y \in R$. Multiplying by $b$ gives $b = x p b + y a b$. Since $p \mid a b$, $p$ divides the right side, so $p \mid b$. Thus $p$ is prime.
    <2>4. Substep 4: Primeness implies uniqueness of factorization.
        *Proof:* Suppose $p_1 \cdots p_n = q_1 \cdots q_m$. Since $p_1$ is prime, $p_1 \mid \prod q_j$, so $p_1 \mid q_j$ for some $j$. Relabeling so $j = 1$, since $q_1$ is irreducible, $p_1$ and $q_1$ are associates ($q_1 = u_1 p_1$). Canceling $p_1$ gives $p_2 \cdots p_n = u_1 q_2 \cdots q_m$. By induction on $n$, $n = m$ and each $p_i$ is associate to some $q_{\sigma(i)}$.
    <2>5. Therefore, every Euclidean domain is a UFD.

<1>4. Part (d): A UFD is not necessarily a Euclidean domain.
    *Proof:*
    <2>1. Consider the ring of polynomials in two variables $R = \mathbb{C}[x, y]$.
    <2>2. Since $\mathbb{C}$ is a field, $\mathbb{C}[x]$ is a Euclidean domain, hence a UFD. By Gauss's Lemma, polynomial rings over UFDs are UFDs, so $R = \mathbb{C}[x, y] = (\mathbb{C}[x])[y]$ is a UFD.
    <2>3. However, the ideal $I = \langle x, y \rangle \subset \mathbb{C}[x, y]$ is not principal: any generator $d$ of $\langle x, y \rangle$ must divide both $x$ and $y$, forcing $d \in \mathbb{C}^\times$, which would mean $\langle x, y \rangle = \mathbb{C}[x, y]$, a contradiction since the evaluation at the origin gives $\mathbb{C}[x, y]/\langle x, y \rangle \cong \mathbb{C} \ne 0$.
    <2>4. Thus $\mathbb{C}[x, y]$ is not a PID.
    <2>5. Since every Euclidean domain is a PID by <1>3, $\mathbb{C}[x, y]$ cannot be a Euclidean domain.

<1>5. Conclusion:
    *Proof:*
    Every Euclidean domain is a UFD, but a UFD need not be a Euclidean domain.
:::



