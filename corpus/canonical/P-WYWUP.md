---
schema: qual/card@1
id: P-WYWUP
kind: problem
title: Fitting's lemma
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - jordan-canonical-form
  - minimal-and-characteristic-polynomials
relations: []
review: draft
solved: true
---

::: problem
Let $V$ be a finite dimensional vector space over a field (the field is not necessarily algebraically closed).

Let $\phi : V \to V$ be a linear transformation.
Prove that there exists a decomposition of $V$ as $V = U \oplus W$ , where $U$ and $W$ are $\phi\dash$invariant subspaces of $V$ , $\restrictionof{\phi}{U}$ is nilpotent, and $\restrictionof{\phi}{W}$ is nonsingular.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

This is Fitting's Lemma for vector spaces.

1. **Chains of kernels and images:** Consider the nested sequences of subspaces:
   $$
   \{0\} = \ker(\phi^0) \subseteq \ker(\phi^1) \subseteq \ker(\phi^2) \subseteq \cdots \subseteq V,
   $$
   $$
   V = \im(\phi^0) \supseteq \im(\phi^1) \supseteq \im(\phi^2) \supseteq \cdots \supseteq \{0\}.
   $$
   Since $V$ is finite dimensional (say $\dim V = n$), the sequence of dimensions cannot strictly increase indefinitely.
   Thus there exists an integer $k \leq n$ such that:
   $$
   \ker(\phi^k) = \ker(\phi^{k+1}) = \ker(\phi^{k+2}) = \cdots
   $$
   and consequently:
   $$
   \im(\phi^k) = \im(\phi^{k+1}) = \im(\phi^{k+2}) = \cdots
   $$

2. **Define $U$ and $W$:** Set $U = \ker(\phi^k)$ and $W = \im(\phi^k)$.

   - **$\phi$-invariance:** If $u \in U$, then $\phi^k(\phi(u)) = \phi(\phi^k(u)) = \phi(0) = 0$, so $\phi(u) \in U$.
     If $w \in W$, then $w = \phi^k(v)$ for some $v \in V$, so $\phi(w) = \phi^{k+1}(v) = \phi^k(\phi(v)) \in W$.
     Thus both $U$ and $W$ are $\phi$-invariant.

3. **Direct sum decomposition $V = U \oplus W$:**

   - **Intersection $U \cap W = \{0\}$:** Let $x \in U \cap W$.
     Since $x \in W = \im(\phi^k)$, $x = \phi^k(y)$ for some $y \in V$.
     Since $x \in U = \ker(\phi^k)$, $0 = \phi^k(x) = \phi^k(\phi^k(y)) = \phi^{2k}(y)$.
     Thus $y \in \ker(\phi^{2k}) = \ker(\phi^k)$ (by stabilization).
     Hence $x = \phi^k(y) = 0$.
     Thus $U \cap W = \{0\}$.

   - **Dimension sum:** By the Rank-Nullity Theorem applied to $\phi^k$:
     $$
     \dim(U) + \dim(W) = \dim(\ker(\phi^k)) + \dim(\im(\phi^k)) = \dim(V).
     $$
     Since $U \cap W = \{0\}$, it follows that $V = U \oplus W$.

4. **Properties of the restrictions:**

   - On $U = \ker(\phi^k)$: For any $u \in U$, $(\restrictionof{\phi}{U})^k(u) = \phi^k(u) = 0$.
     Thus $\restrictionof{\phi}{U}$ is **nilpotent** (with index of nilpotency at most $k$).

   - On $W = \im(\phi^k)$: If $w \in W$ and $\restrictionof{\phi}{W}(w) = 0$, then $w \in \ker(\phi) \subseteq \ker(\phi^k) = U$.
     Since $w \in U \cap W = \{0\}$, we have $w = 0$.
     Thus $\ker(\restrictionof{\phi}{W}) = \{0\}$, so $\restrictionof{\phi}{W}$ is injective.
     Since $W$ is finite-dimensional, $\restrictionof{\phi}{W}$ is an isomorphism, hence **nonsingular**.
:::
