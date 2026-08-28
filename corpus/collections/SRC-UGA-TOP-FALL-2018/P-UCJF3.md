---
schema: qual/card@1
id: P-UCJF3
kind: problem
title: 'van Kampen''s theorem: the surjection $\pi_1(A)*\pi_1(B)\to\pi_1(A\cup B)$'
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Prove the following portion of van Kampen's theorem. 
If $X = A\cup B$ and $A$, $B$, and $A \cap B$ are nonempty and path connected with $\pt \in A \cap B$, then there is a surjection 
$$
\pi_1 (A, \pt) \ast \pi_1 (B, \pt) \to \pi_1 (X, \pt)
.$$
:::

::: solution
**Goal:** Prove that the canonical homomorphism $\Phi: \pi_1(A, \pt) \ast \pi_1(B, \pt) \to \pi_1(X, \pt)$ induced by the inclusion maps $i_A: A \hookrightarrow X$ and $i_B: B \hookrightarrow X$ is surjective, where $A, B$ are open subsets of $X = A \cup B$ (or subcomplexes) with $A, B, A \cap B$ path-connected and $\pt \in A \cap B$.

<1>1. Canonical homomorphism $\Phi$:
    The inclusions $i_A: A \hookrightarrow X$ and $i_B: B \hookrightarrow X$ induce group homomorphisms $(i_A)_*: \pi_1(A, \pt) \to \pi_1(X, \pt)$ and $(i_B)_*: \pi_1(B, \pt) \to \pi_1(X, \pt)$. By the universal property of the free product of groups, there exists a unique group homomorphism
    $$\Phi: \pi_1(A, \pt) \ast \pi_1(B, \pt) \to \pi_1(X, \pt)$$
    satisfying $\Phi|_{ \pi_1(A, \pt)} = (i_A)_*$ and $\Phi|_{ \pi_1(B, \pt)} = (i_B)_*$.

<1>2. Partition of an arbitrary loop $\gamma$:
    Let $[\gamma] \in \pi_1(X, \pt)$ be represented by a continuous loop $\gamma: [0, 1] \to X$ with $\gamma(0) = \gamma(1) = \pt$. There exists a partition $0 = t_0 < t_1 < t_2 < \cdots < t_k = 1$ of $[0, 1]$ such that each subpath $\gamma_i = \gamma|_{[t_{i-1}, t_i]}$ has image $\gamma([t_{i-1}, t_i])$ contained entirely in $A$ or entirely in $B$ for each $i \in \{1, \dots, k\}$.
    *Proof:* The preimages $\gamma^{-1}(A)$ and $\gamma^{-1}(B)$ form an open cover of the compact metric space $[0, 1]$. By the Lebesgue Number Lemma, there exists $\delta > 0$ such that every interval in $[0, 1]$ of length less than $\delta$ is contained in $\gamma^{-1}(A)$ or in $\gamma^{-1}(B)$. Choosing $k > 1/\delta$ and subdivision points $t_i = i/k$ yields the required partition.

<1>3. Connecting intermediate endpoints to the basepoint $\pt$:
    For each subdivision point $t_i$ ($i = 0, \dots, k$), there exists a path $\alpha_i: [0, 1] \to X$ from $\pt$ to $\gamma(t_i)$ such that:
    1. $\alpha_0 = c_{\pt}$ and $\alpha_k = c_{\pt}$ (the constant path at $\pt$).
    2. If $\gamma(t_i) \in A \cap B$, the image of $\alpha_i$ lies entirely within $A \cap B$.
    3. If $\gamma(t_i) \in A \setminus B$, $\alpha_i$ lies in $A$.
    4. If $\gamma(t_i) \in B \setminus A$, $\alpha_i$ lies in $B$.
    *Proof:* For $i=0$ and $i=k$, $\gamma(t_0) = \gamma(t_k) = \pt$, so we take $\alpha_0 = \alpha_k = c_{\pt}$. For $0 < i < k$, if $\gamma([t_{i-1}, t_i]) \subseteq A$ and $\gamma([t_i, t_{i+1}]) \subseteq B$ (or vice versa), then $\gamma(t_i) \in A \cap B$. Since $A \cap B$ is path-connected and contains $\pt$, there exists a path $\alpha_i$ in $A \cap B$ from $\pt$ to $\gamma(t_i)$. If both adjacent intervals map into $A$ (respectively $B$), $\gamma(t_i) \in A$ (respectively $B$), and path-connectedness of $A$ (respectively $B$) supplies a path $\alpha_i$ in $A$ (respectively $B$) from $\pt$ to $\gamma(t_i)$.

<1>4. Factorization into loops based at $\pt$:
    In $\pi_1(X, \pt)$, we have
    $$[\gamma] = [\sigma_1] \cdot [\sigma_2] \cdots [\sigma_k]$$
    where $\sigma_i = \alpha_{i-1} \ast \gamma_i \ast \overline{\alpha}_i$ is a loop based at $\pt$.
    *Proof:* Under path concatenation,
    $$\sigma_1 \ast \sigma_2 \ast \cdots \ast \sigma_k = (\alpha_0 \ast \gamma_1 \ast \overline{\alpha}_1) \ast (\alpha_1 \ast \gamma_2 \ast \overline{\alpha}_2) \ast \cdots \ast (\alpha_{k-1} \ast \gamma_k \ast \overline{\alpha}_k).$$
    Since $\overline{\alpha}_i \ast \alpha_i \simeq c_{\gamma(t_i)}$ and $\alpha_0 = \alpha_k = c_{\pt}$, the intermediate paths cancel up to homotopy:
    $$\sigma_1 \ast \cdots \ast \sigma_k \simeq \alpha_0 \ast \gamma_1 \ast \gamma_2 \ast \cdots \ast \gamma_k \ast \overline{\alpha}_k \simeq \gamma_1 \ast \cdots \ast \gamma_k = \gamma.$$
    Thus $[\gamma] = \prod_{i=1}^k [\sigma_i]$ in $\pi_1(X, \pt)$.

<1>5. Membership in images of factor groups:
    For each $i \in \{1, \dots, k\}$, the loop $\sigma_i = \alpha_{i-1} \ast \gamma_i \ast \overline{\alpha}_i$ lies entirely in $A$ or entirely in $B$, so $[\sigma_i] \in \operatorname{im}((i_A)_*)$ or $[\sigma_i] \in \operatorname{im}((i_B)_*)$.
    *Proof:* By construction, $\gamma_i$ lies in $A$ (or $B$). The boundary paths $\alpha_{i-1}$ and $\alpha_i$ were chosen in $A \cap B \subseteq A$ (or $A \cap B \subseteq B$) whenever $\gamma_i$ lies in $A$ (or $B$). Thus the concatenation $\sigma_i$ is a continuous map from $[0, 1]$ into $A$ (or $B$) with $\sigma_i(0) = \sigma_i(1) = \pt$. Therefore $[\sigma_i] = (i_A)_*([\sigma_i]_A)$ for some $[\sigma_i]_A \in \pi_1(A, \pt)$ if $\operatorname{im}(\sigma_i) \subseteq A$, or $[\sigma_i] = (i_B)_*([\sigma_i]_B)$ for some $[\sigma_i]_B \in \pi_1(B, \pt)$ if $\operatorname{im}(\sigma_i) \subseteq B$.

<1>6. Conclusion: $\Phi$ is surjective.
    *Proof:* For any $[\gamma] \in \pi_1(X, \pt)$, each factor $[\sigma_i]$ in the product $[\gamma] = \prod_{i=1}^k [\sigma_i]$ is in $\operatorname{im}(\Phi)$ by <1>5. Since $\Phi$ is a homomorphism, the word $w = [g_1] \ast [g_2] \ast \cdots \ast [g_k] \in \pi_1(A, \pt) \ast \pi_1(B, \pt)$ (where $[g_i] = [\sigma_i]_A \in \pi_1(A, \pt)$ or $[\sigma_i]_B \in \pi_1(B, \pt)$) satisfies $\Phi(w) = \prod_{i=1}^k \Phi([g_i]) = \prod_{i=1}^k [\sigma_i] = [\gamma]$. Hence $\Phi$ is surjective. Q.E.D.
:::
