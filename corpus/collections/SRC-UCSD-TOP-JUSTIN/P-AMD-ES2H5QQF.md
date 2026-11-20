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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Seven steps asserted their claim with no justification and each now carries one: the CW structure,
    the mod 2 and mod 3 chain computations, both UCT checks, and the integral cochain computation with
    its UCT check. Each was recomputed while writing. $H_*(\RP^n;\ZZ_2)$ is $\ZZ_2$ in every degree
    $0 \le k \le n$ because every integral boundary is $0$ or multiplication by $2$; over $\ZZ_3$ the
    multiplication by $2$ is invertible with inverse $2$, so the answer is $\ZZ_3$ in degree $0$,
    nothing strictly between, and $\ZZ_3$ in degree $n$ only for odd $n$; and over $\ZZ_6$ the
    cohomology is $\ZZ_6$ in degrees $0$ and $n$ for odd $n$, and $\ZZ_2$ elsewhere, which the UCT
    reproduces from $\operatorname{Hom}(\ZZ/2,\ZZ_6) \cong \operatorname{Ext}^1(\ZZ/2,\ZZ_6) \cong
    \ZZ_2$. Two repairs: the step about $H_k(\RP^n;\ZZ)$ cited itself, which renders as its own number,
    and the closing pf-qed only pointed back at the four parts, which STYLE-08 does not admit, so it is
    gone. The statement is unchanged. The collection retains the UCSD 290 problem sheets and no
    solutions, so the argument is the card's own.
---

::: {.problem}
Compute the following directly from chain complexes and check using UCT:

1. $H_*(\RP^n; \ZZ_2)$

2. $H_*(\RP^n, \ZZ_3)$

3. $H^*(\RP^n, \ZZ_6)$
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Cellular chain complex and integral homology of $\RP^n$.

::: pf-proof

::: {.pf-step #cw-structure}
Standard CW structure of $\RP^n$: One cell $e^k$ in each dimension $0 \le k \le n$, so $C_k(\RP^n; \ZZ) \cong \ZZ$ for $0 \le k \le n$.

::: pf-proof
For each $k$ the open $k$-cell is the image of the open disc under the quotient $D^k \to \RP^k$, and $\RP^n$ is the disjoint union of the images of $\mathring D^k$ for $k = 0, \dots, n$, because $\RP^k \setminus \RP^{k-1}$ is a single open $k$-cell. So there is one cell in each dimension from $0$ to $n$, and the $k$-th cellular chain group is the free abelian group on that one generator.
:::

:::

::: pf-step
The cellular boundary map $d_k \colon C_k(\RP^n; \ZZ) \to C_{k-1}(\RP^n; \ZZ)$ is multiplication by $1+(-1)^k$:
$$d_k = \begin{cases} 0 & k \text{ odd}, \\ 2 & k \text{ even } (k \ge 2). \end{cases}$$

::: pf-proof
In the standard CW structure, the characteristic map of the $k$-cell is the quotient $D^k\to\RP^k$. To compute the incidence number with the unique $(k-1)$-cell, collapse the $(k-2)$-skeleton and compare the two hemispherical lifts of the attaching map to $S^{k-1}$. Their local degrees are $1$ and $(-1)^k$, so the cellular boundary coefficient is $1+(-1)^k$.
:::

:::

::: {.pf-step #s1-3}
The integral homology $H_k(\RP^n; \ZZ)$ is:
- $H_0 \cong \ZZ$,
- $H_k \cong \ZZ/2\ZZ$ for odd $k$ with $0 < k < n$,
- $H_k \cong 0$ for even $k$ with $0 < k < n$,
- Top dimension: $H_n(\RP^n; \ZZ) \cong \ZZ$ if $n$ is odd, and $0$ if $n$ is even.

::: pf-proof
With $d_k = 0$ for odd $k$ and $d_k = 2$ for even $k \ge 2$, the chain complex alternates between the zero map and multiplication by $2$; taking kernels and images gives the groups claimed here.
:::

:::

:::

:::

::: {.pf-step #s2}
Compute Part 1: $H_*(\RP^n; \ZZ_2)$.

::: pf-proof

::: {.pf-step #mod-2-chain}
Direct Chain Complex:
- $C_k(\RP^n; \ZZ_2) = C_k \otimes \ZZ_2 \cong \ZZ_2$ for $0 \le k \le n$.
- The boundary maps are $d_k \otimes \operatorname{id}_{\ZZ_2}$.
- Since $d_k \in \{0, 2\}$, $d_k \equiv 0 \pmod 2$ for all $k$.
- Thus all differentials are zero: $d_k = 0$.
- Therefore, $H_k(\RP^n; \ZZ_2) \cong \ZZ_2$ for all $0 \le k \le n$, and $0$ for $k > n$.

::: pf-proof
The chain groups satisfy $C_k(\RP^n;\ZZ_2) = C_k(\RP^n;\ZZ)\otimes \ZZ_2 \cong \ZZ\otimes\ZZ_2 \cong \ZZ_2$, and the boundary maps of the tensored complex are $d_k \otimes \id_{\ZZ_2}$ by construction. The integral boundary is $0$ or multiplication by $2$, and the tensor of either with $\ZZ_2$ is zero, so every differential in the complex vanishes; the homology of a complex with zero differentials is its chain group in each degree.
:::

:::

::: {.pf-step #mod-2-uct}
UCT Check:
- By UCT for homology: $H_k(\RP^n; \ZZ_2) \cong (H_k(\RP^n; \ZZ) \otimes \ZZ_2) \oplus \operatorname{Tor}_1(H_{k-1}(\RP^n; \ZZ), \ZZ_2)$.
- For $0 < k < n$:
  - If $k$ is odd: $H_k \otimes \ZZ_2 = (\ZZ/2) \otimes \ZZ_2 \cong \ZZ_2$, and $\operatorname{Tor}_1(H_{k-1}, \ZZ_2) = \operatorname{Tor}_1(0, \ZZ_2) = 0 \implies H_k \cong \ZZ_2$.
  - If $k$ is even: $H_k \otimes \ZZ_2 = 0 \otimes \ZZ_2 = 0$, and $\operatorname{Tor}_1(H_{k-1}, \ZZ_2) = \operatorname{Tor}_1(\ZZ/2, \ZZ_2) \cong \ZZ_2 \implies H_k \cong \ZZ_2$.
- Boundary cases $k=0$ and $k=n$ also yield $\ZZ_2$.

::: pf-proof
The universal coefficient theorem gives $H_k(\RP^n;\ZZ_2) \cong \left(H_k(\RP^n;\ZZ)\otimes\ZZ_2\right) \oplus \operatorname{Tor}_1\left(H_{k-1}(\RP^n;\ZZ),\ZZ_2\right)$, and the integral groups are those of step [](#s1-3){.pf-ref}. For odd $k$ strictly between $0$ and $n$ the free part $\ZZ/2\otimes\ZZ_2$ contributes $\ZZ_2$ and the Tor term vanishes because $H_{k-1} = 0$; for even $k$ the free part vanishes and $\operatorname{Tor}_1(\ZZ/2,\ZZ_2) \cong \ZZ_2$ contributes; in degree $0$ the group $H_0 = \ZZ$ gives $\ZZ_2$; and in degree $n$ the answer is $\ZZ_2$ whether $H_n$ is $\ZZ$ or $0$, through the free part in the first case and the Tor term in the second.
:::

:::

::: pf-qed
Both the direct chain computation and the UCT computation give $H_k(\RP^n; \ZZ_2) \cong \ZZ_2$ for $0 \le k \le n$.
:::

:::

:::

::: {.pf-step #s3}
Compute Part 2: $H_*(\RP^n; \ZZ_3)$.

::: pf-proof

::: {.pf-step #mod-3-chain}
Direct Chain Complex:
- $C_k(\RP^n; \ZZ_3) \cong \ZZ_3$ for $0 \le k \le n$.
- On $\ZZ_3$, multiplication by $2$ is an isomorphism (since $\gcd(2, 3) = 1$, $2^{-1} \equiv 2 \pmod 3$).
- Thus $d_k = 0$ for $k$ odd, and $d_k \colon \ZZ_3 \xrightarrow{\cong} \ZZ_3$ is an isomorphism for $k$ even ($k \ge 2$).
- Therefore, the homology vanishes in all intermediate dimensions:
  - $H_0(\RP^n; \ZZ_3) \cong \ZZ_3$,
  - $H_k(\RP^n; \ZZ_3) = 0$ for $0 < k < n$,
  - Top dimension: $H_n(\RP^n; \ZZ_3) \cong \ZZ_3$ if $n$ is odd, and $0$ if $n$ is even.

::: pf-proof
The chain groups are $C_k(\RP^n;\ZZ_3) \cong \ZZ\otimes\ZZ_3 \cong \ZZ_3$, and the boundary is $0$ for odd $k$ and multiplication by $2$ for even $k \ge 2$. In $\ZZ_3$ the class of $2$ is invertible with inverse $2$, because $4 \equiv 1$, so multiplication by $2$ is an isomorphism of $\ZZ_3$, with kernel $0$ and image everything. Hence $H_0 = \ZZ_3$ since $d_1 = 0$; $H_k = 0$ for $0 < k < n$ because kernel and image coincide there; and $H_n = \ZZ_3$ when $n$ is odd because $d_n = 0$, while $H_n = 0$ when $n$ is even because $d_n$ is then injective.
:::

:::

::: {.pf-step #mod-3-uct}
UCT Check:
- $\ZZ/2 \otimes \ZZ_3 = 0$ and $\operatorname{Tor}_1(\ZZ/2, \ZZ_3) = 0$ since $\gcd(2, 3) = 1$.
- Thus all 2-torsion vanishes under $\otimes \ZZ_3$, giving identical results.

::: pf-proof
The universal coefficient theorem expresses $H_k(\RP^n;\ZZ_3)$ through the integral groups of step [](#s1-3){.pf-ref}, which are $\ZZ$, $0$ and $\ZZ/2$. Since $\ZZ\otimes\ZZ_3 \cong \ZZ_3$ while $\ZZ/2\otimes\ZZ_3 = 0$ and $\operatorname{Tor}_1(\ZZ/2,\ZZ_3) = 0$, the coprime $2$ and $3$ killing every torsion term, the answer is the integral answer with $\ZZ$ replaced by $\ZZ_3$: $\ZZ_3$ in degree $0$, nothing strictly between, and in degree $n$ the group $\ZZ_3$ or $0$ according as $n$ is odd or even.
:::

:::

::: pf-qed
The direct chain computation and the UCT computation agree: both give $H_0 \cong \ZZ_3$, $H_k = 0$ for $0 < k < n$, and $H_n \cong \ZZ_3$ for odd $n$ (and $0$ for even $n$).
:::

:::

:::

::: {.pf-step #s4}
Compute Part 3: $H^*(\RP^n; \ZZ_6)$.

::: pf-proof

::: {.pf-step #z6-cochain}
Direct Cochain Complex:
- $C^k(\RP^n; \ZZ_6) = \operatorname{Hom}(C_k, \ZZ_6) \cong \ZZ_6$ for $0 \le k \le n$.
- The coboundary $\delta^k \colon C^k \to C^{k+1}$ is dual to $d_{k+1}$, so for $0 \le k < n$:
  $$\delta^k = d_{k+1}^* = \begin{cases} 0 & k \text{ even}, \\ 2 & k \text{ odd}. \end{cases}$$
  and $\delta^n = 0$ because $C^{n+1} = 0$.
- For $k = 0$: $\delta^0 = 0$, so $H^0 = \ker(\delta^0) / \operatorname{im}(\delta^{-1}) = \ZZ_6 / 0 \cong \ZZ_6$.
- For $0 < k < n$:
  - If $k$ is even: $\delta^k = 0$ and $\delta^{k-1} = 2$, so $H^k = \ZZ_6 / 2\ZZ_6 \cong \ZZ_2$.
  - If $k$ is odd: $\delta^k = 2$ and $\delta^{k-1} = 0$, so $H^k = \ker(\times 2) / 0 = \{0, 3\} \cong \ZZ_2$.
- For $k = n$: $\delta^n = 0$, and $\delta^{n-1} = d_n^*$:
  - If $n$ is odd: $d_n = 0$, so $H^n = \ZZ_6 / 0 \cong \ZZ_6$.
  - If $n$ is even: $d_n = 2$, so $H^n = \ZZ_6 / 2\ZZ_6 \cong \ZZ_2$.

::: pf-proof
The cochain groups are $C^k(\RP^n;\ZZ_6) = \operatorname{Hom}(C_k,\ZZ_6) \cong \operatorname{Hom}(\ZZ,\ZZ_6) \cong \ZZ_6$, and the coboundary $\delta^k$ is the dual of $d_{k+1}$; the dual of multiplication by $m$ on $\ZZ$ is multiplication by $m$ on $\ZZ_6$, and the dual of the zero map is zero. So $\delta^k = 0$ for even $k$ and $\delta^k$ is multiplication by $2$ for odd $k$, while $\delta^n = 0$ because there is no cell above dimension $n$. Taking kernel modulo image degree by degree: in degree $0$ the kernel is all of $\ZZ_6$; for even $k$ between $0$ and $n$ the quotient $\ZZ_6/2\ZZ_6$ is $\ZZ_2$; for odd $k$ the kernel of multiplication by $2$ is $\{0, 3\} \cong \ZZ_2$ and the image of the previous coboundary is $0$; and in degree $n$ the group is $\ZZ_6$ when $n$ is odd and $\ZZ_2$ when $n$ is even.
:::

:::

::: {.pf-step #z6-uct}
UCT Check for Cohomology:
- UCT: $H^k(X; G) \cong \operatorname{Hom}(H_k(X), G) \oplus \operatorname{Ext}^1(H_{k-1}(X), G)$.
- Note $\operatorname{Hom}(\ZZ, \ZZ_6) \cong \ZZ_6$, $\operatorname{Hom}(\ZZ/2, \ZZ_6) \cong \ZZ_2$, $\operatorname{Ext}^1(\ZZ/2, \ZZ_6) \cong \ZZ_2$, $\operatorname{Ext}^1(\ZZ, \ZZ_6) = 0$.
- Using $H_*(X; \ZZ)$ from step [](#s1){.pf-ref} gives:
  - $H^0 \cong \operatorname{Hom}(\ZZ, \ZZ_6) \oplus 0 \cong \ZZ_6$.
  - $0 < k < n$: $H^k \cong \ZZ_2$ for all $k$.
  - $k = n$: $H^n \cong \begin{cases} \ZZ_6 & n \text{ odd}, \\ \ZZ_2 & n \text{ even}. \end{cases}$

::: pf-proof
The universal coefficient theorem for cohomology gives $H^k(X;G) \cong \operatorname{Hom}(H_k(X),G) \oplus \operatorname{Ext}^1(H_{k-1}(X),G)$. With the integral homology of step [](#s1-3){.pf-ref}: $\operatorname{Hom}(\ZZ,\ZZ_6) \cong \ZZ_6$, $\operatorname{Hom}(\ZZ/2,\ZZ_6) \cong \ZZ_2$ because a homomorphism out of $\ZZ/2$ is an element of order dividing $2$, $\operatorname{Ext}^1(\ZZ/2,\ZZ_6) \cong \ZZ/2$, and $\operatorname{Ext}^1(\ZZ,\ZZ_6) = 0$ because $\ZZ$ is free. The only shapes occurring are a free group, $\ZZ/2$ and $0$, and substituting them gives $\ZZ_6$ in degree $0$, $\ZZ_2$ in each degree strictly between $0$ and $n$, and in degree $n$ the group $\ZZ_6$ for odd $n$ and $\ZZ_2$ for even $n$.
:::

:::

::: pf-qed
The direct cochain computation and the UCT computation agree in every degree, so both methods give the same groups.
:::

:::

:::

:::
:::

