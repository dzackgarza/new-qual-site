---
schema: qual/card@1
id: E-HAT-2.1-15
kind: problem
title: Middle term of exact sequence is zero iff outer maps have expected kernel/cokernel
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Applied exactness at B,C,D, then used consecutive five-term pieces of the long exact sequence of a pair.
---

For an exact sequence $A \to B \to C \to D \to E$ show that $C = 0$ iff the map $A \to B$ is surjective and $D \to E$ is injective.
Hence for a pair of spaces $(X, A)$, the inclusion $A \hookrightarrow X$ induces isomorphisms on all homology groups iff $H_n(X, A) = 0$ for all $n$.

::: {.solution}
Consider an exact sequence
\[
A\xrightarrow{\alpha}B\xrightarrow{\beta}C\xrightarrow{\gamma}D\xrightarrow{\delta}E.
\]

<1>1. If $C=0$, then $\alpha$ is surjective and $\delta$ is injective.
::: {.proof}
Exactness at $B$ gives
\[
\operatorname{im}\alpha=\ker\beta.
\]
Since $\beta:B\to0$ is zero, $\ker\beta=B$, so $\alpha$ is surjective.

Exactness at $D$ gives
\[
\ker\delta=\operatorname{im}\gamma.
\]
Since $\gamma:0\to D$ has zero image, $\ker\delta=0$, so $\delta$ is injective.
:::

<1>2. Conversely, if $\alpha$ is surjective and $\delta$ is injective, then $C=0$.
::: {.proof}
Surjectivity of $\alpha$ and exactness at $B$ imply
\[
\ker\beta=B,
\]
so $\beta=0$. Exactness at $C$ then gives
\[
\ker\gamma=\operatorname{im}\beta=0,
\]
so $\gamma$ is injective.

Injectivity of $\delta$ gives $\ker\delta=0$. Exactness at $D$ gives
\[
\operatorname{im}\gamma=0.
\]
Thus $\gamma$ is both injective and zero, forcing $C=0$.
:::

<1>3. For a pair $(X,A)$, the segment
\[
H_n(A)\xrightarrow{i_*}H_n(X)\to H_n(X,A)
\to H_{n-1}(A)\xrightarrow{i_*}H_{n-1}(X)
\]
is exact. Hence
\[
H_n(X,A)=0
\]
if and only if the first $i_*$ is surjective and the second $i_*$ is injective.
::: {.proof}
Apply <1>1--<1>2 to this five-term exact segment.
:::

<1>4. Therefore
\[
\boxed{H_n(X,A)=0\text{ for all }n
\iff i_*:H_n(A)\to H_n(X)\text{ is an isomorphism for all }n.}
\]
::: {.proof}
If all relative groups vanish, <1>3 gives surjectivity of $i_*$ in degree $n$ and injectivity in degree $n-1$ for every $n$, hence both properties in every degree. Conversely, if every $i_*$ is an isomorphism, the two conditions in <1>3 hold in every degree, so every relative group vanishes.
:::
:::
