---
schema: qual/card@1
id: E-HAT-2.2-19
kind: problem
title: $H_i(\RP^n/\RP^m)$ by cellular homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
  - Cellular Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 19; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    The cellular complex with one cell in degrees m+1, ..., n, d_{m+1} = 0 and d_i = 2 for even
    i > m+1, is checked in proofs/cards/DeltaComplexHomology.sage through Sage's ChainComplex for
    the sampled range m = 0, ..., 4 and m < n <= 8, against the card's case table; every sampled case
    agrees. This is a finite check, not a proof of the case table.

    Rerun on the supported Sage development image: Sage 11.0.beta5, Python 3.14.10, source
    HEAD b0cd7d86e2, all checks passing there.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 19 as printed on p. 157. Recomputed the alternating pattern by
    hand on (n,m) = (2,1), (3,0), (3,1), (4,0), (4,2): with d_{m+1} = 0 and d_i = 1+(-1)^i
    for i > m+1, H_{m+1} is Z for m odd and Z_2 for m even, H_i is Z_2 for odd i and 0 for
    even i strictly between, and H_n is Z for odd n and 0 for even n. Results now cited:
    Example 0.4 p. 6 and Example 2.42 p. 144 for the cells and the projective boundary
    d_i = 1+(-1)^i, the Cellular Boundary Formula p. 141 for why d_i above dimension m+1 is
    unchanged by the collapse, Proposition 2.22 p. 124 for H_i(RP^n/RP^m) = H_i(RP^n,RP^m),
    and Theorem 2.35 p. 139 for cellular equals singular. Added the missing statement that
    the groups vanish in degrees 1 to m. What is not covered: no certificate.
---

::: {.problem}
Compute $H_i(\RP^n/\RP^m)$ for $m < n$ by cellular homology, using the standard CW structure on $\RP^n$ with $\RP^m$ as its $m$ skeleton.
:::

::: {.solution}
Let
$$
Y=\RP^n/\RP^m,
\qquad m<n.
$$
The quotient CW structure has one $0$-cell and one cell in each dimension
$$
m+1,m+2,\dots,n.
$$
The cells of $\RP^n$ are one in each dimension (Example 0.4, p. 6, and Example 2.42, p. 144) and $\RP^m$ is a subcomplex, so $Y$ is a CW complex and $(Y,\ast)$ is a good pair; by Proposition 2.22 (p. 124), $H_i(Y)=H_i(\RP^n,\RP^m)$.
Thus its reduced cellular chain groups are
$$
\widetilde C_i(Y)\cong
\begin{cases}
\ZZ,&m<i\le n,\\
0,&\text{otherwise}.
\end{cases}
$$
For $i>m+1$, the cellular boundary is the usual projective-space boundary
$$
d_i=
\begin{cases}
2,&i\text{ even},\\
0,&i\text{ odd},
\end{cases}
$$
which is $d_i=1+(-1)^i$ in Example 2.42 (p. 144); it is unchanged by the collapse because the Cellular Boundary Formula (p. 141) computes its entries as degrees of maps into the $(i-1)$-skeleton, which for $i-1\ge m+1$ is the same in $Y$ as in $\RP^n$. On the other hand $d_{m+1}=0$ because its target chain group has been collapsed away.

::: pf

::: {.pf-step #s1}
If $n=m+1$, then
$$
\widetilde H_n(Y)\cong\ZZ
$$
and all other reduced homology groups vanish.

::: pf-proof
There is a single nonzero reduced cellular chain group, in degree $n$, and both adjacent boundary maps are zero.
:::

:::

:::

Assume henceforth that $n\ge m+2$.

::: pf

::: {.pf-step #s2}
In the bottom degree $m+1$,
$$
\widetilde H_{m+1}(Y)\cong
\begin{cases}
\ZZ,&m+1\text{ even},\\
\ZZ_2,&m+1\text{ odd}.
\end{cases}
$$

::: pf-proof
The outgoing differential is zero. The incoming differential is $d_{m+2}$, which is zero when $m+2$ is odd and multiplication by $2$ when $m+2$ is even. These are exactly the two displayed cases.
:::

:::

::: {.pf-step #s3}
For $m+1<i<n$,
$$
\widetilde H_i(Y)\cong
\begin{cases}
\ZZ_2,&i\text{ odd},\\
0,&i\text{ even}.
\end{cases}
$$

::: pf-proof
If $i$ is even, $d_i=2$ is injective, so there are no cycles. If $i$ is odd, $d_i=0$ and $d_{i+1}=2$, giving
$$
H_i\cong\ZZ/2\ZZ.
$$
:::

:::

::: {.pf-step #s4}
In the top degree $n$,
$$
\widetilde H_n(Y)\cong
\begin{cases}
\ZZ,&n\text{ odd},\\
0,&n\text{ even},
\end{cases}
\qquad(n>m+1).
$$

::: pf-proof
There is no incoming boundary from degree $n+1$. Thus top homology is $\ker d_n$, which is $\ZZ$ for odd $n$ and $0$ for even $n$.
:::

:::

::: pf-step
Finally $Y$ is connected, so
$$
H_0(Y)\cong\ZZ,
$$
and for $1\le i\le m$ there are no $i$-chains at all, so $\widetilde H_i(Y)=0$. The cellular groups computed above are the singular homology groups by Theorem 2.35 (p. 139). Together steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} give all homology groups of $\RP^n/\RP^m$.
:::

:::

:::
