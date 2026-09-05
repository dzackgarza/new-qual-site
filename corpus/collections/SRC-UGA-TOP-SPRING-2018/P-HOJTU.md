---
schema: qual/card@1
id: P-HOJTU
kind: problem
title: Why $H_1$ of a point vanishes in the singular chain complex
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
  date: 2026-09-05
  note: Checked the three alternatives against problem 5 of the official UGA Spring 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the singular boundary maps on the unique simplex in each degree and hence alternative (c).
---

::: problem
It is a fact that if $X$ is a single point then $H_1(X)=0$.
One of the following is the correct justification of this fact in terms of the singular chain complex.
Which one is correct and why is it correct?

(a) $C_1(X)=0$.

(b) $C_1(X)\neq0$ but $\ker\partial_1=0$, with $\partial_1:C_1(X)\to C_0(X)$.

(c) $\ker\partial_1\neq0$ but $\ker\partial_1=\operatorname{im}\partial_2$, with $\partial_2:C_2(X)\to C_1(X)$.
:::

::: {.solution}
The correct answer is **(c)**.

<1>1. For every $n\ge0$, the singular chain group of the one-point space $X=\{*\}$ is
\[
C_n(X)\cong\ZZ.
\]
::: {.proof}
There is exactly one continuous map
\[
\sigma_n:\Delta^n\longrightarrow\{*\},
\]
so there is exactly one singular $n$-simplex.
By definition, $C_n(X)$ is the free abelian group on the singular $n$-simplices, hence
\[
C_n(X)=\ZZ\langle\sigma_n\rangle\cong\ZZ.
\]
In particular, $C_1(X)\neq0$, so alternative (a) is false.
:::

<1>2. The boundary map
\[
\partial_1:C_1(X)\longrightarrow C_0(X)
\]
is the zero map.
::: {.proof}
The two faces of the unique singular $1$-simplex are both the unique singular $0$-simplex $\sigma_0$.
Therefore
\[
\partial_1\sigma_1
=\sigma_0-\sigma_0
=0.
\]
Hence
\[
\ker\partial_1=C_1(X)\cong\ZZ\neq0,
\]
so alternative (b) is false.
:::

<1>3. The boundary map
\[
\partial_2:C_2(X)\longrightarrow C_1(X)
\]
is surjective.
::: {.proof}
All three faces of the unique singular $2$-simplex are the unique singular $1$-simplex $\sigma_1$.
Thus
\[
\partial_2\sigma_2
=\sigma_1-\sigma_1+\sigma_1
=\sigma_1.
\]
Since $\sigma_1$ generates $C_1(X)$, it follows that
\[
\operatorname{im}\partial_2=C_1(X).
\]
:::

<1>4. Therefore
\[
H_1(X)
=\ker\partial_1/\operatorname{im}\partial_2
=0.
\]
::: {.proof}
By <1>2 and <1>3,
\[
\ker\partial_1
=C_1(X)
=\operatorname{im}\partial_2,
\]
and this common group is nonzero.
This is exactly alternative (c).
:::
:::
