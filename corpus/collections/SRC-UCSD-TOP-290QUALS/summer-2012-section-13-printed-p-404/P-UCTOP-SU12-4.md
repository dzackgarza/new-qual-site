---
schema: qual/card@1
id: P-UCTOP-SU12-4
kind: problem
title: 'Homology of $\RP^2\times X$ where $H_k(X;\ZZ)\cong\ZZ/k\ZZ$'
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    The solution had six steps and not one proof block: the chain computation, the Kuenner application
    and the degree-by-degree values were all asserted. Every step now has a proof. The homology of RP^2
    is computed from its three-cell structure and the degree-2 attaching map rather than quoted. The
    Kunneth step names the theorem, keeps the Tor term, and says why the sequence splits (cellular
    chains are free, so the algebraic Kunneth sequence over a PID splits) and what X must be for it
    (a CW complex, or its CW approximation, since only its homology enters). The low degrees 0, 1, 2 are
    computed from the hypothesis H_k(X) = Z/k, including the point that H_1(X) = Z/1 = 0. The cyclic
    tensor and Tor values are derived from the free resolution 0 -> Z -m-> Z -> Z/m -> 0 rather than
    stated. The high degrees use that n-1 and n-2 are consecutive, so exactly one of the two extra
    summands is Z/2. The final display assembles the ranges and is not a bare back-reference.
    The answer is unchanged: Z, then Z/2, Z/2, then Z/n + Z/2 for n >= 3. Not checked: no independent
    source for the exercise beyond the imported statement.

---

::: {.problem}
Let $X$ be a path-connected space whose homology groups in positive dimensions are $H_k(X;\ZZ) = \ZZ/k\ZZ$.
Compute the integer homology $H_*(\RP^2 \times X;\ZZ)$.

:::

::: {.solution}
Throughout, $X$ is taken to be a CW complex, or replaced by a CW approximation, since only its integral homology enters; the Künneth sequence used below is the one for CW complexes.

::: pf

::: {.pf-step #rp2}
The integral homology of $\RP^2$ is
$$
H_i(\RP^2;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=1,\\
0,&i\ge2.
\end{cases}
$$

::: pf-proof
$\RP^2$ has a CW structure with one cell in each of the dimensions $0,1,2$, and the attaching map of the $2$-cell is a map $S^1\to\RP^1$ of degree $2$. The cellular chain complex is therefore
$$
0\longrightarrow\ZZ\xrightarrow{\ \times2\ }\ZZ\xrightarrow{\ 0\ }\ZZ\longrightarrow0 ,
$$
with the middle differential zero because the $1$-cell is attached to the single $0$-cell at both ends. Hence $H_0=\ZZ/0=\ZZ$, $H_1=\ker 0/\operatorname{im}\times2=\ZZ/2\ZZ$, and $H_2=\ker(\times2)=0$, with nothing above degree $2$.

:::

:::

::: {.pf-step #kunneth}
For every $n\ge0$ there is a split short exact sequence
$$
0\to\bigoplus_{i+j=n}H_i(\RP^2)\otimes H_j(X)\to H_n(\RP^2\times X)\to\bigoplus_{i+j=n-1}\operatorname{Tor}_1^{\ZZ}(H_i(\RP^2),H_j(X))\to0,
$$
so that
$$
H_n(\RP^2\times X;\ZZ)\cong H_n(X)\oplus\bigl((\ZZ/2)\otimes H_{n-1}(X)\bigr)\oplus\operatorname{Tor}_1^{\ZZ}(\ZZ/2,H_{n-2}(X)),
$$
where groups of negative index are $0$.

::: pf-proof
That is the Künneth theorem for CW complexes, in the form that keeps the Tor term and is split exact. It splits because the cellular chains of a CW complex are free $\ZZ$-modules and the algebraic Künneth sequence over a principal ideal domain is a split sequence of free resolutions. Only the two nonzero reduced homology groups of $\RP^2$ from step [](#rp2){.pf-ref} contribute: $H_0(\RP^2)=\ZZ$ is free and so contributes no Tor, leaving the tensor terms $\ZZ\otimes H_n(X)\cong H_n(X)$ and $(\ZZ/2)\otimes H_{n-1}(X)$, and the Tor terms $\operatorname{Tor}(\ZZ,H_{n-1}(X))=0$ and $\operatorname{Tor}(\ZZ/2,H_{n-2}(X))$.

:::

:::

::: {.pf-step #low-degrees}
$H_0(\RP^2\times X)\cong\ZZ$, $H_1(\RP^2\times X)\cong\ZZ/2$ and $H_2(\RP^2\times X)\cong\ZZ/2$.

::: pf-proof
Apply step [](#kunneth){.pf-ref} with the hypothesis that $H_k(X)=\ZZ/k\ZZ$ for $k\ge1$, so that in particular $H_1(X)=\ZZ/1=0$ and $H_2(X)=\ZZ/2$, and $H_j(X)=0$ for $j<0$. For $n=0$: $H_0(X)=\ZZ$ and the other two summands vanish, so $H_0=\ZZ$, as it must be for a path-connected space. For $n=1$: $H_1(X)\oplus(\ZZ/2\otimes H_0(X))\oplus\operatorname{Tor}(\ZZ/2,H_{-1}(X))=0\oplus\ZZ/2\otimes\ZZ\oplus0\cong\ZZ/2$. For $n=2$: $H_2(X)\oplus(\ZZ/2\otimes H_1(X))\oplus\operatorname{Tor}(\ZZ/2,H_0(X))=\ZZ/2\oplus0\oplus0\cong\ZZ/2$, because $\ZZ/2\otimes0=0$ and $\operatorname{Tor}(\ZZ/2,\ZZ)=0$.

:::

:::

::: {.pf-step #cyclic}
For $m\ge1$,
$$
(\ZZ/2)\otimes(\ZZ/m)\cong\operatorname{Tor}_1^{\ZZ}(\ZZ/2,\ZZ/m)\cong\ZZ/\gcd(2,m).
$$

::: pf-proof
Use the free resolution $0\to\ZZ\xrightarrow{\ m\ }\ZZ\to\ZZ/m\to0$ and apply $\ZZ/2\otimes-$, which gives
$$
0\to\operatorname{Tor}(\ZZ/2,\ZZ/m)\to\ZZ/2\xrightarrow{\ m\ }\ZZ/2\to(\ZZ/2)\otimes(\ZZ/m)\to0 .
$$
Multiplication by $m$ on $\ZZ/2$ has kernel and cokernel both isomorphic to $\ZZ/\gcd(2,m)$: it is zero when $m$ is even, and the identity when $m$ is odd.

:::

:::

::: {.pf-step #high-degrees}
For $n\ge3$,
$$
H_n(\RP^2\times X;\ZZ)\cong\ZZ/n\oplus\ZZ/2 .
$$

::: pf-proof
In step [](#kunneth){.pf-ref} with $n\ge3$ all indices $n,n-1,n-2$ are positive, so $H_n(X)=\ZZ/n$, $H_{n-1}(X)=\ZZ/(n-1)$ and $H_{n-2}(X)=\ZZ/(n-2)$, and step [](#cyclic){.pf-ref} gives
$$
H_n(\RP^2\times X)\cong\ZZ/n\ \oplus\ \ZZ/\gcd(2,n-1)\ \oplus\ \ZZ/\gcd(2,n-2).
$$
The integers $n-1$ and $n-2$ are consecutive, so exactly one of them is even and the other odd; therefore exactly one of $\gcd(2,n-1),\gcd(2,n-2)$ equals $2$ and the other equals $1$, and the two extra summands contribute a single $\ZZ/2$.

:::

:::

::: {.pf-step #answer}
$$
H_n(\RP^2\times X;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ/2,&n=1,2,\\
\ZZ/n\oplus\ZZ/2,&n\ge3.
\end{cases}
$$

::: pf-proof
The three ranges are steps [](#low-degrees){.pf-ref}, which gives $\ZZ$ in degree $0$ and $\ZZ/2$ in degrees $1$ and $2$, and step [](#high-degrees){.pf-ref}, which gives $\ZZ/n\oplus\ZZ/2$ from degree $3$ on. There is no further degree: $\RP^2$ has cells only in dimensions $\le2$, so the summands of step [](#kunneth){.pf-ref} vanish above $n+1$ only through the vanishing of $H_j(X)$ at negative indices, and every $n\ge3$ is covered by step [](#high-degrees){.pf-ref}.

:::

:::

:::

:::
