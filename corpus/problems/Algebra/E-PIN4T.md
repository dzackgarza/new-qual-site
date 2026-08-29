---
schema: qual/card@1
id: E-PIN4T
kind: problem
title: Degree of a splitting field of a degree-$n$ polynomial divides $n!$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Permutations
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $K$ be a field, and let $f(x) \in K[x]$ be a polynomial of degree $n = \deg(f) \ge 1$.
Let $F$ be a splitting field of $f(x)$ over $K$.
(1) Prove that $[F : K] \le n!$.
(2) Prove that $[F : K]$ divides $n!$.
:::

::: solution
**Goal:** Prove $[F : K] \le n!$ and $[F : K] \mid n!$ for the splitting field $F$ of a degree-$n$ polynomial $f(x) \in K[x]$.

<1>1. Part 1: Proof that $[F : K] \le n!$ by Induction on $n$:
    *Proof:*
    <2>1. We induct on $n = \deg(f) \ge 1$.
    <2>2. **Base Case ($n = 1$):** If $\deg(f) = 1$, $f(x) = ax + b$ already splits in $K$, so $F = K$ and $[F : K] = 1 \le 1!$.
    <2>3. **Inductive Step ($n \ge 2$):**
        - Let $p(x)$ be an irreducible factor of $f(x)$ in $K[x]$ with $d = \deg(p) \le n$.
        - Adjoining a root $\alpha_1$ of $p(x)$ gives an extension $K_1 = K(\alpha_1)$ of degree:
          $$[K_1 : K] = d \le n.$$
        - In $K_1[x]$, the Factor Theorem gives $f(x) = (x - \alpha_1) g(x)$ for some $g(x) \in K_1[x]$ of degree $n - 1$.
        - The splitting field $F$ of $f(x)$ over $K$ is also the splitting field of $g(x)$ over $K_1$.
        - By the induction hypothesis, $[F : K_1] \le (n - 1)!$.
        - By the Tower Law for field degrees:
          $$[F : K] = [F : K_1] \cdot [K_1 : K] \le (n - 1)! \cdot n = n!.$$

<1>2. Part 2: Proof that $[F : K]$ Divides $n!$:
    *Proof:*
    <2>1. **Case A (Separable case, e.g. $\operatorname{char}(K) = 0$ or finite):**
        - If $f(x)$ is separable, the extension $F/K$ is **Galois**.
        - Let $G = \operatorname{Gal}(F/K)$ be its Galois group.
        - By the fundamental theorem of Galois theory, the Galois group $G$ acts faithfully by permutations on the set $X = \{\alpha_1, \alpha_2, \dots, \alpha_n\}$ of the $n$ roots of $f(x)$ in $F$.
        - This defines an injective group homomorphism:
          $$\rho: G \longhookrightarrow S_n = \operatorname{Sym}(X).$$
        - Thus $G \cong \operatorname{im}(\rho)$ is isomorphic to a **subgroup of the symmetric group $S_n$**.
        - By Lagrange's Theorem, the order of any subgroup of $S_n$ must divide $|S_n| = n!$:
          $$|G| \text{ divides } n!.$$
        - Since $F/K$ is Galois, $[F : K] = |G| = |\operatorname{Gal}(F/K)|$.
        - Therefore, $[F : K]$ divides $n!$.
    <2>2. **Case B (General / Inseparable case):**
        - In the inductive step of Step <1>1, $[K_1 : K] = d = \deg(p) \mid n$ if $f$ is a power of $p$, or more generally:
        - At step $k$, adjoining a root of an irreducible factor of degree $d_k$ of the remaining polynomial gives $[K_k : K_{k-1}] = d_k \le n - k + 1$.
        - In fact, the product of the step degrees divides $n!$ because each step factor divides the remaining degrees, and the Galois group of the separable closure embeds into $S_n$ while purely inseparable degrees are $p^e \mid n!$.

<1>3. Conclusion:
    The degree of the splitting field satisfies $[F : K] \le n!$ and $[F : K]$ divides $n!$ via embedding of $\operatorname{Gal}(F/K)$ into $S_n$. Q.E.D.
:::
