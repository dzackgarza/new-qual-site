---
schema: qual/card@1
id: E-HAT-2.B-11
kind: problem
title: "Homology of $X \\times \\mathbb{RP}^\\infty$ via transfer"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the determinant or transfer-sequence argument, including the mod-2 endpoint maps.
---

Use the transfer sequence for the covering $X \times S^\infty \to X \times \mathbb{RP}^\infty$ to produce isomorphisms $H_n(X \times \mathbb{RP}^\infty; \mathbb{Z}_2) \approx \bigoplus_{i \leq n} H_i(X; \mathbb{Z}_2)$ for all $n$.

::: {.solution}
Put
\[
E=X\times S^\infty,
\qquad
B=X\times\mathbb{RP}^\infty,
\]
and use $\mathbb Z_2$ coefficients. The projection $p:E\to B$ is a double cover, so its transfer sequence is
\[
\cdots\to H_n(B)\overset{\tau_*}{\longrightarrow}H_n(E)
\overset{p_*}{\longrightarrow}H_n(B)
\overset{\delta}{\longrightarrow}H_{n-1}(B)\to\cdots .
\]
Since $S^\infty$ is contractible, projection to the first factor gives
\[
H_n(E)\cong H_n(X).
\]

<1>1. Under this identification, $p_*:H_n(X)\to H_n(B)$ is split injective.
::: {.proof}
Choose $e_0\in S^\infty$ and write $b_0=[e_0]\in\mathbb{RP}^\infty$. After deforming $E$ to $X\times\{e_0\}$, the covering map becomes the inclusion
\[
j:X\to X\times\mathbb{RP}^\infty,
\qquad j(x)=(x,b_0).
\]
The projection
\[
q:B\to X
\]
satisfies $qj=\operatorname{id}_X$, so $j_*=p_*$ is split injective.
:::

<1>2. The transfer map
\[
\tau_*:H_n(B)\to H_n(E)\cong H_n(X)
\]
is zero for every $n$.
::: {.proof}
Let $r:E\to X$ be projection to the first factor. On singular chains, $\tau$ sends a simplex in $B$ to the sum of its two lifts. The two lifts have the same projection to $X$, hence
\[
r_\#\tau(\sigma)=2\,q_\#(\sigma)=0
\]
over $\mathbb Z_2$. Thus $r_*\tau_*=0$. Since $r_*:H_n(E)\to H_n(X)$ is an isomorphism, $\tau_*=0$.
:::

<1>3. Hence for every $n$ the transfer sequence breaks into a split short exact sequence
\[
0\longrightarrow H_n(X)
\overset{p_*}{\longrightarrow}H_n(B)
\overset{\delta}{\longrightarrow}H_{n-1}(B)
\longrightarrow0.
\]
::: {.proof}
By <1>2, exactness makes $\delta$ surjective. By <1>1, $p_*$ is injective, and exactness gives $\ker\delta=\operatorname{im}p_*$. The splitting of $p_*$ from <1>1 splits the short exact sequence.
:::

<1>4. Inductively,
\[
\boxed{
H_n(X\times\mathbb{RP}^\infty;\mathbb Z_2)
\cong
\bigoplus_{i=0}^{n}H_i(X;\mathbb Z_2).
}
\]
::: {.proof}
From <1>3,
\[
H_n(B)\cong H_n(X)\oplus H_{n-1}(B).
\]
For $n=0$, $H_0(B)\cong H_0(X)$ because $\mathbb{RP}^\infty$ is connected. Iterating the displayed recurrence yields the stated direct sum.
:::
:::
