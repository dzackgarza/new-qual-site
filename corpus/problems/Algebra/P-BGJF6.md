---
schema: qual/card@1
id: P-BGJF6
kind: problem
title: Definition of a splitting field
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Polynomials
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State the definition of the splitting field of a polynomial $f(x) \in F[x]$ over a field $F$.
Prove the existence and uniqueness (up to $F$-isomorphism) of splitting fields.
:::

::: solution
**Goal:** Define splitting fields, prove existence via Kronecker's Theorem (iterated polynomial quotients), and prove uniqueness up to $F$-isomorphism via the Isomorphism Extension Theorem.

<1>1. Definition of a Splitting Field:
    *Proof:*
    <2>1. Let $F$ be a field and $f(x) \in F[x]$ a non-constant polynomial of degree $n \ge 1$.
    <2>2. An extension field $L/F$ is a **splitting field** of $f(x)$ over $F$ if:
        1. $f(x)$ **splits completely into linear factors** over $L$:
           $$f(x) = c \prod_{i=1}^n (x - \alpha_i) \in L[x] \quad (\text{with } c \in F^\times, \; \alpha_i \in L).$$
        2. $L$ is **generated over $F$ by the roots** of $f(x)$:
           $$L = F(\alpha_1, \alpha_2, \dots, \alpha_n).$$

<1>2. Existence of Splitting Fields:
    *Proof:*
    <2>1. We proceed by induction on $n = \deg(f) \ge 1$.
    <2>2. **Base Case ($n = 1$):** If $\deg(f) = 1$, $f(x) = c(x - \alpha)$ already has its root $\alpha \in F$. Thus $L = F$ is the splitting field.
    <2>3. **Inductive Step ($n \ge 2$):**
        - Let $p(x)$ be an irreducible factor of $f(x)$ in $F[x]$ of degree $d \ge 1$.
        - If $d = 1$, $f(x)$ has a root in $F$.
        - If $d \ge 2$, by **Kronecker's Theorem**, $E_1 = F[x]/(p(x))$ is a field extension of $F$ in which $\bar{x} = \alpha_1$ is a root of $p(x)$ (and hence of $f(x)$).
        - In $E_1[x]$, the Factor Theorem gives $f(x) = (x - \alpha_1) g(x)$ for some $g(x) \in E_1[x]$ with $\deg(g) = n - 1$.
        - By the induction hypothesis, there exists a splitting field $L$ for $g(x)$ over $E_1$.
        - Then $L = E_1(\alpha_2, \dots, \alpha_n) = F(\alpha_1, \dots, \alpha_n)$ is a splitting field of $f(x)$ over $F$.

<1>3. Uniqueness up to $F$-Isomorphism (Isomorphism Extension Theorem):
    *Proof:*
    <2>1. **Lemma (Extension of Isomorphisms):** Let $\sigma: F_1 \xrightarrow{\sim} F_2$ be an isomorphism of fields. Let $f(x) \in F_1[x]$ and let $f^\sigma(x) \in F_2[x]$ be its image under $\sigma$.
        If $L_1$ is a splitting field of $f(x)$ over $F_1$ and $L_2$ is a splitting field of $f^\sigma(x)$ over $F_2$, then there exists an isomorphism $\tau: L_1 \xrightarrow{\sim} L_2$ such that $\tau|_{F_1} = \sigma$.
    <2>2. *Proof of Lemma:* Induction on $[L_1 : F_1]$.
        - If $[L_1 : F_1] = 1$, $f$ splits in $F_1$, so $f^\sigma$ splits in $F_2$, and $L_2 = F_2$. Then $\tau = \sigma$.
        - If $[L_1 : F_1] > 1$, choose an irreducible factor $p(x) \mid f(x)$ of degree $\ge 2$ in $F_1[x]$.
        - Let $\alpha \in L_1$ be a root of $p(x)$, and let $\beta \in L_2$ be a root of the corresponding irreducible factor $p^\sigma(x) \mid f^\sigma(x)$.
        - The isomorphism $\sigma$ extends to $\sigma': F_1(\alpha) \xrightarrow{\sim} F_2(\beta)$ mapping $\alpha \mapsto \beta$.
        - Since $[L_1 : F_1(\alpha)] < [L_1 : F_1]$, by induction $\sigma'$ extends to an isomorphism $\tau: L_1 \xrightarrow{\sim} L_2$.
    <2>3. Applying this lemma with $F_1 = F_2 = F$ and $\sigma = \operatorname{id}_F$, any two splitting fields of $f(x)$ over $F$ are isomorphic via an isomorphism fixing $F$ point-wise.

<1>4. Conclusion:
    Splitting fields exist by Kronecker's quotient construction and are unique up to $F$-isomorphism. Q.E.D.
:::
