---
schema: qual/card@1
id: P-4IWVY
kind: problem
title: Irreducible modules over a PID are $R/(p)$ and indecomposable modules are $R/(p^n)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $R$ be a Principal Ideal Domain (PID).
(1) Prove that the irreducible (simple) $R$-modules are precisely $R/(p)$ where $p \in R$ is a prime (irreducible) element.
(2) Prove that the finitely generated indecomposable $R$-modules are precisely $R$ and $R/(p^n)$ where $p \in R$ is prime and $n \ge 1$.
:::

::: solution
**Goal:** Classify all simple $R$-modules and all finitely generated indecomposable $R$-modules over a PID $R$.

<1>1. Classification of Simple (Irreducible) $R$-modules:
    *Proof:*
    <2>1. Let $M$ be a simple $R$-module (i.e. $M \ne \{0\}$ and the only submodules of $M$ are $\{0\}$ and $M$).
    <2>2. Choose any non-zero element $x \in M \setminus \{0\}$.
    <2>3. The cyclic submodule $R x = \{r x \mid r \in R\} \subseteq M$ is a non-zero submodule of $M$.
    <2>4. Since $M$ is simple, $R x = M$. Thus $M$ is cyclic.
    <2>5. Consider the surjective $R$-module homomorphism $\phi: R \to M$ defined by $\phi(r) = r x$.
    <2>6. By the First Isomorphism Theorem for modules, $M \cong R / \ker\phi = R / \mathfrak{m}$, where $\mathfrak{m} = \operatorname{Ann}_R(x) = \ker\phi$.
    <2>7. By the Lattice Isomorphism Theorem (Correspondence Theorem) for submodules, the submodules of $R/\mathfrak{m}$ correspond bijectively to the ideals of $R$ containing $\mathfrak{m}$.
    <2>8. Since $M$ has no non-trivial proper submodules, $R/\mathfrak{m}$ has no non-trivial proper ideals, which means $\mathfrak{m}$ is a **maximal ideal** of $R$.
    <2>9. In a PID, every non-zero prime ideal is maximal. Thus $\mathfrak{m} = (p)$ for some prime (irreducible) element $p \in R$.
    <2>10. Conversely, if $p \in R$ is prime, $(p)$ is maximal, so $R/(p)$ is a field, and any 1-dimensional vector space over a field is simple.
    <2>11. Thus the simple $R$-modules are precisely $R/(p)$ for prime elements $p \in R$.

<1>2. Classification of Finitely Generated Indecomposable $R$-modules:
    *Proof:*
    <2>1. An $R$-module $M$ is **indecomposable** if $M \ne \{0\}$ and $M \cong N_1 \oplus N_2 \implies N_1 = \{0\}$ or $N_2 = \{0\}$.
    <2>2. By the Structure Theorem for Finitely Generated Modules over a PID (Primary Decomposition):
        $$M \cong R^r \oplus \bigoplus_{i=1}^k R/(p_i^{n_i})$$
        where $r \ge 0$, $p_i \in R$ are prime elements, and $n_i \ge 1$.
    <2>3. If $M$ is indecomposable:
        - $M$ cannot be a non-trivial direct sum of two or more non-zero modules.
        - If $r > 0$ and $k > 0$, $M \cong R \oplus (R^{r-1} \oplus \bigoplus R/(p_i^{n_i}))$ is decomposable.
        - If $r \ge 2$, $M \cong R \oplus R^{r-1}$ is decomposable.
        - If $k \ge 2$, $M \cong R/(p_1^{n_1}) \oplus \bigoplus_{i=2}^k R/(p_i^{n_i})$ is decomposable.
    <2>4. Therefore, an indecomposable finitely generated module must have exactly one direct summand:
        - Either $r = 1, k = 0 \implies M \cong R$.
        - Or $r = 0, k = 1 \implies M \cong R/(p^n)$ for some prime $p \in R$ and integer $n \ge 1$.
    <2>5. **$R$ is indecomposable:** Since $R$ is an integral domain, $R \cong N_1 \oplus N_2 \implies$ one of the summands has rank 0 and is torsion-free, hence is $\{0\}$.
    <2>6. **$R/(p^n)$ is indecomposable:** The submodules of $R/(p^n)$ are the ideals containing $(p^n)$, which form a strictly nested chain:
        $$(p^n)/(p^n) \subset (p^{n-1})/(p^n) \subset \cdots \subset (p)/(p^n) \subset R/(p^n).$$
        Every non-zero submodule contains the unique minimal submodule $(p^{n-1})/(p^n)$.
        Thus any two non-zero submodules have non-trivial intersection, so $R/(p^n)$ cannot be written as an internal direct sum $N_1 \oplus N_2$ of non-zero submodules.

<1>3. Conclusion:
    The simple $R$-modules are $R/(p)$, and the indecomposable finitely generated $R$-modules are $R$ and $R/(p^n)$ ($n \ge 1$). Q.E.D.
:::
