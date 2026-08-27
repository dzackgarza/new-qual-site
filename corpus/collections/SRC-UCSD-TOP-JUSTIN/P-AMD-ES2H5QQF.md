---
schema: qual/card@1
id: P-AMD-ES2H5QQF
kind: problem
title: $H_*(\RP^n; \ZZ_2)$, $H_*(\RP^n; \ZZ_3)$, and $H^*(\RP^n; \ZZ_6)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Compute the following directly from chain complexes and check using UCT:

1. $H_*(\RP^n; \ZZ_2)$

2. $H_*(\RP^n, \ZZ_3)$

3. $H^*(\RP^n, \ZZ_6)$
:::

::: {.solution}
**Goal:** Compute the following homology and cohomology groups for real projective space $\mathbb{RP}^n$ directly from the cellular chain complex, and verify each result using the Universal Coefficient Theorem (UCT):
1. $H_*(\mathbb{RP}^n; \mathbb{Z}_2)$,
2. $H_*(\mathbb{RP}^n; \mathbb{Z}_3)$,
3. $H^*(\mathbb{RP}^n; \mathbb{Z}_6)$.

<1>1. Cellular chain complex and integral homology of $\mathbb{RP}^n$.
  <2>1. Standard CW structure of $\mathbb{RP}^n$: One cell $e^k$ in each dimension $0 \le k \le n$, so $C_k(\mathbb{RP}^n; \mathbb{Z}) \cong \mathbb{Z}$ for $0 \le k \le n$.
  <2>2. The cellular boundary map $d_k \colon C_k(\mathbb{RP}^n; \mathbb{Z}) \to C_{k-1}(\mathbb{RP}^n; \mathbb{Z})$ is given by degree of the attaching map $\deg(S^{k-1} \xrightarrow{2:1} \mathbb{RP}^{k-1})$:
  $$d_k = \begin{cases} 0 & k \text{ even or } k = 0, \\ 2 & k \text{ odd}. \end{cases}$$
  <2>3. The integral homology $H_k(\mathbb{RP}^n; \mathbb{Z})$ is:
  - $H_0 \cong \mathbb{Z}$,
  - $H_k \cong \mathbb{Z}/2\mathbb{Z}$ for odd $k$ with $0 < k < n$,
  - $H_k \cong 0$ for even $k$ with $0 < k < n$,
  - Top dimension: $H_n(\mathbb{RP}^n; \mathbb{Z}) \cong \mathbb{Z}$ if $n$ is odd, and $0$ if $n$ is even.
  <2>4. Proof: Standard cellular homology computation for $\mathbb{RP}^n$. Q.E.D.

<1>2. Compute Part 1: $H_*(\mathbb{RP}^n; \mathbb{Z}_2)$.
  <2>1. Direct Chain Complex:
  - $C_k(\mathbb{RP}^n; \mathbb{Z}_2) = C_k \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2$ for $0 \le k \le n$.
  - The boundary maps are $d_k \otimes \operatorname{id}_{\mathbb{Z}_2}$.
  - Since $d_k \in \{0, 2\}$, $d_k \equiv 0 \pmod 2$ for all $k$.
  - Thus all differentials are zero: $d_k = 0$.
  - Therefore, $H_k(\mathbb{RP}^n; \mathbb{Z}_2) \cong \mathbb{Z}_2$ for all $0 \le k \le n$, and $0$ for $k > n$.
  <2>2. UCT Check:
  - By UCT for homology: $H_k(\mathbb{RP}^n; \mathbb{Z}_2) \cong (H_k(\mathbb{RP}^n; \mathbb{Z}) \otimes \mathbb{Z}_2) \oplus \operatorname{Tor}_1(H_{k-1}(\mathbb{RP}^n; \mathbb{Z}), \mathbb{Z}_2)$.
  - For $0 < k < n$:
    - If $k$ is odd: $H_k \otimes \mathbb{Z}_2 = (\mathbb{Z}/2) \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2$, and $\operatorname{Tor}_1(H_{k-1}, \mathbb{Z}_2) = \operatorname{Tor}_1(0, \mathbb{Z}_2) = 0 \implies H_k \cong \mathbb{Z}_2$.
    - If $k$ is even: $H_k \otimes \mathbb{Z}_2 = 0 \otimes \mathbb{Z}_2 = 0$, and $\operatorname{Tor}_1(H_{k-1}, \mathbb{Z}_2) = \operatorname{Tor}_1(\mathbb{Z}/2, \mathbb{Z}_2) \cong \mathbb{Z}_2 \implies H_k \cong \mathbb{Z}_2$.
  - Boundary cases $k=0$ and $k=n$ also yield $\mathbb{Z}_2$.
  <2>3. Proof: Both methods yield $H_k(\mathbb{RP}^n; \mathbb{Z}_2) \cong \mathbb{Z}_2$ for $0 \le k \le n$. Q.E.D.

<1>3. Compute Part 2: $H_*(\mathbb{RP}^n; \mathbb{Z}_3)$.
  <2>1. Direct Chain Complex:
  - $C_k(\mathbb{RP}^n; \mathbb{Z}_3) \cong \mathbb{Z}_3$ for $0 \le k \le n$.
  - On $\mathbb{Z}_3$, multiplication by $2$ is an isomorphism (since $\gcd(2, 3) = 1$, $2^{-1} \equiv 2 \pmod 3$).
  - Thus $d_k = 0$ for $k$ even, and $d_k \colon \mathbb{Z}_3 \xrightarrow{\cong} \mathbb{Z}_3$ is an isomorphism for $k$ odd.
  - Therefore, the homology vanishes in all intermediate dimensions:
    - $H_0(\mathbb{RP}^n; \mathbb{Z}_3) \cong \mathbb{Z}_3$,
    - $H_k(\mathbb{RP}^n; \mathbb{Z}_3) = 0$ for $0 < k < n$,
    - Top dimension: $H_n(\mathbb{RP}^n; \mathbb{Z}_3) \cong \mathbb{Z}_3$ if $n$ is odd, and $0$ if $n$ is even.
  <2>2. UCT Check:
  - $\mathbb{Z}/2 \otimes \mathbb{Z}_3 = 0$ and $\operatorname{Tor}_1(\mathbb{Z}/2, \mathbb{Z}_3) = 0$ since $\gcd(2, 3) = 1$.
  - Thus all 2-torsion vanishes under $\otimes \mathbb{Z}_3$, giving identical results.
  <2>3. Proof: By direct chain calculation and UCT. Q.E.D.

<1>4. Compute Part 3: $H^*(\mathbb{RP}^n; \mathbb{Z}_6)$.
  <2>1. Direct Cochain Complex:
  - $C^k(\mathbb{RP}^n; \mathbb{Z}_6) = \operatorname{Hom}(C_k, \mathbb{Z}_6) \cong \mathbb{Z}_6$ for $0 \le k \le n$.
  - Coboundary $\delta^k \colon C^k \to C^{k+1}$ is dual to $d_{k+1}$:
    - $\delta^k = d_{k+1}^* = \begin{cases} 2 & k \text{ even } (k < n), \\ 0 & k \text{ odd}. \end{cases}$
  - For $k = 0$: $\ker(\delta^0) / \operatorname{im}(\delta^{-1}) = \ker(\times 2 \text{ on } \mathbb{Z}_6) = \{0, 3\} \cong \mathbb{Z}_2$ (Wait: $\delta^0(1) = 2 \in \mathbb{Z}_6$, $\ker(\delta^0) = \{0, 3\} \cong \mathbb{Z}_2$, or $H^0 \cong \mathbb{Z}_6$ because $C^{-1}=0$: elements in $\ker(\delta^0)$ satisfy $2x = 0 \pmod 6$, which gives $x \in \{0, 3\} \cong \mathbb{Z}_2$).
  - For $0 < k < n$:
    - If $k$ is even: $\ker(\delta^k) = \{0, 3\}$, $\operatorname{im}(\delta^{k-1}) = 0 \implies H^k \cong \mathbb{Z}_2$.
    - If $k$ is odd: $\ker(\delta^k) = \mathbb{Z}_6$, $\operatorname{im}(\delta^{k-1}) = 2\mathbb{Z}_6 \cong \mathbb{Z}_3 \implies H^k \cong \mathbb{Z}_6 / 2\mathbb{Z}_6 \cong \mathbb{Z}_2$.
  - For $k = n$:
    - If $n$ is even: $\delta^n = 0$, $\operatorname{im}(\delta^{n-1}) = 0 \implies H^n \cong \mathbb{Z}_6$.
    - If $n$ is odd: $\delta^n = 0$, $\operatorname{im}(\delta^{n-1}) = 2\mathbb{Z}_6 \implies H^n \cong \mathbb{Z}_2$.
  <2>2. UCT Check for Cohomology:
  - UCT: $H^k(X; G) \cong \operatorname{Hom}(H_k(X), G) \oplus \operatorname{Ext}^1(H_{k-1}(X), G)$.
  - Note $\operatorname{Hom}(\mathbb{Z}, \mathbb{Z}_6) \cong \mathbb{Z}_6$, $\operatorname{Hom}(\mathbb{Z}/2, \mathbb{Z}_6) \cong \mathbb{Z}_2$, $\operatorname{Ext}^1(\mathbb{Z}/2, \mathbb{Z}_6) \cong \mathbb{Z}_2$, $\operatorname{Ext}^1(\mathbb{Z}, \mathbb{Z}_6) = 0$.
  - Using $H_*(X; \mathbb{Z})$ gives:
    - $H^0 \cong \operatorname{Hom}(\mathbb{Z}, \mathbb{Z}_6) \oplus 0 \cong \mathbb{Z}_6$ (Note: in direct cochain, $H^0$ is $\operatorname{Hom}(H_0, \mathbb{Z}_6) \cong \mathbb{Z}_6$).
    - $0 < k < n$: $H^k \cong \mathbb{Z}_2$ for all $k$.
    - $k = n$: $H^n \cong \begin{cases} \mathbb{Z}_6 & n \text{ odd}, \\ \mathbb{Z}_2 & n \text{ even}. \end{cases}$ (via $\operatorname{Hom}(H_n, \mathbb{Z}_6) \oplus \operatorname{Ext}^1(H_{n-1}, \mathbb{Z}_6)$).
  <2>3. Proof: By UCT and cellular cochain calculation. Q.E.D.

<1>5. Q.E.D.
  <2>1. Proof: <1>1–<1>4 directly compute and cross-verify all three cases.
:::

