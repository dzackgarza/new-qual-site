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
::: pf

::: {.pf-step #s1}
Cellular chain complex and integral homology of $\RP^n$.

::: pf-proof

::: pf-step
Standard CW structure of $\RP^n$: One cell $e^k$ in each dimension $0 \le k \le n$, so $C_k(\RP^n; \ZZ) \cong \ZZ$ for $0 \le k \le n$.
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
With $d_k = 0$ for odd $k$ and $d_k = 2$ for even $k \ge 2$, the chain complex alternates between the zero map and multiplication by $2$; taking kernels and images gives the groups listed in step [](#s1-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s2}
Compute Part 1: $H_*(\RP^n; \ZZ_2)$.

::: pf-proof

::: pf-step
Direct Chain Complex:
- $C_k(\RP^n; \ZZ_2) = C_k \otimes \ZZ_2 \cong \ZZ_2$ for $0 \le k \le n$.
- The boundary maps are $d_k \otimes \operatorname{id}_{\ZZ_2}$.
- Since $d_k \in \{0, 2\}$, $d_k \equiv 0 \pmod 2$ for all $k$.
- Thus all differentials are zero: $d_k = 0$.
- Therefore, $H_k(\RP^n; \ZZ_2) \cong \ZZ_2$ for all $0 \le k \le n$, and $0$ for $k > n$.
:::

::: pf-step
UCT Check:
- By UCT for homology: $H_k(\RP^n; \ZZ_2) \cong (H_k(\RP^n; \ZZ) \otimes \ZZ_2) \oplus \operatorname{Tor}_1(H_{k-1}(\RP^n; \ZZ), \ZZ_2)$.
- For $0 < k < n$:
  - If $k$ is odd: $H_k \otimes \ZZ_2 = (\ZZ/2) \otimes \ZZ_2 \cong \ZZ_2$, and $\operatorname{Tor}_1(H_{k-1}, \ZZ_2) = \operatorname{Tor}_1(0, \ZZ_2) = 0 \implies H_k \cong \ZZ_2$.
  - If $k$ is even: $H_k \otimes \ZZ_2 = 0 \otimes \ZZ_2 = 0$, and $\operatorname{Tor}_1(H_{k-1}, \ZZ_2) = \operatorname{Tor}_1(\ZZ/2, \ZZ_2) \cong \ZZ_2 \implies H_k \cong \ZZ_2$.
- Boundary cases $k=0$ and $k=n$ also yield $\ZZ_2$.
:::

::: pf-qed
Both the direct chain computation and the UCT computation give $H_k(\RP^n; \ZZ_2) \cong \ZZ_2$ for $0 \le k \le n$.
:::

:::

:::

::: {.pf-step #s3}
Compute Part 2: $H_*(\RP^n; \ZZ_3)$.

::: pf-proof

::: pf-step
Direct Chain Complex:
- $C_k(\RP^n; \ZZ_3) \cong \ZZ_3$ for $0 \le k \le n$.
- On $\ZZ_3$, multiplication by $2$ is an isomorphism (since $\gcd(2, 3) = 1$, $2^{-1} \equiv 2 \pmod 3$).
- Thus $d_k = 0$ for $k$ odd, and $d_k \colon \ZZ_3 \xrightarrow{\cong} \ZZ_3$ is an isomorphism for $k$ even ($k \ge 2$).
- Therefore, the homology vanishes in all intermediate dimensions:
  - $H_0(\RP^n; \ZZ_3) \cong \ZZ_3$,
  - $H_k(\RP^n; \ZZ_3) = 0$ for $0 < k < n$,
  - Top dimension: $H_n(\RP^n; \ZZ_3) \cong \ZZ_3$ if $n$ is odd, and $0$ if $n$ is even.
:::

::: pf-step
UCT Check:
- $\ZZ/2 \otimes \ZZ_3 = 0$ and $\operatorname{Tor}_1(\ZZ/2, \ZZ_3) = 0$ since $\gcd(2, 3) = 1$.
- Thus all 2-torsion vanishes under $\otimes \ZZ_3$, giving identical results.
:::

::: pf-qed
The direct chain computation and the UCT computation agree: both give $H_0 \cong \ZZ_3$, $H_k = 0$ for $0 < k < n$, and $H_n \cong \ZZ_3$ for odd $n$ (and $0$ for even $n$).
:::

:::

:::

::: {.pf-step #s4}
Compute Part 3: $H^*(\RP^n; \ZZ_6)$.

::: pf-proof

::: pf-step
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
:::

::: pf-step
UCT Check for Cohomology:
- UCT: $H^k(X; G) \cong \operatorname{Hom}(H_k(X), G) \oplus \operatorname{Ext}^1(H_{k-1}(X), G)$.
- Note $\operatorname{Hom}(\ZZ, \ZZ_6) \cong \ZZ_6$, $\operatorname{Hom}(\ZZ/2, \ZZ_6) \cong \ZZ_2$, $\operatorname{Ext}^1(\ZZ/2, \ZZ_6) \cong \ZZ_2$, $\operatorname{Ext}^1(\ZZ, \ZZ_6) = 0$.
- Using $H_*(X; \ZZ)$ from step [](#s1){.pf-ref} gives:
  - $H^0 \cong \operatorname{Hom}(\ZZ, \ZZ_6) \oplus 0 \cong \ZZ_6$.
  - $0 < k < n$: $H^k \cong \ZZ_2$ for all $k$.
  - $k = n$: $H^n \cong \begin{cases} \ZZ_6 & n \text{ odd}, \\ \ZZ_2 & n \text{ even}. \end{cases}$
:::

::: pf-qed
The direct cochain computation and the UCT computation agree in every degree, so both methods give the same groups.
:::

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, and [](#s4){.pf-ref} directly compute and cross-verify all three cases.
:::

:::
:::

