---
schema: qual/card@1
id: P-HGRO41
kind: problem
title: Core theorem
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction; theorem identification independently checked against the standard subgroup-core theorem.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
State and prove the core theorem.
:::

::: {.solution}
**Core theorem.** Let $H\le G$ have finite index $n$. Define
\[
\operatorname{core}_G(H)=\bigcap_{g\in G}gHg^{-1}.
\]
Then $\operatorname{core}_G(H)$ is the largest normal subgroup of $G$ contained
in $H$, and
\[
G/\operatorname{core}_G(H)
\]
is isomorphic to a subgroup of $S_n$. In particular,
\[
[G:\operatorname{core}_G(H)]\mid n!
\]
when $G$ is finite.

::: pf

::: {.pf-step #s1}

The core is normal in $G$ and contained in $H$.

::: pf-proof

It is contained in the conjugate corresponding to $g=1$, namely $H$. For any
$x\in G$,
\[
x\left(\bigcap_{g\in G}gHg^{-1}\right)x^{-1}
=\bigcap_{g\in G}(xg)H(xg)^{-1}
=\operatorname{core}_G(H),
\]
so it is normal.

:::

:::

::: {.pf-step #s2}

Every normal subgroup of $G$ contained in $H$ lies in the core.

::: pf-proof

If $N\trianglelefteq G$ and $N\le H$, then for every $g\in G$,
\[
N=gNg^{-1}\le gHg^{-1}.
\]
Hence $N$ lies in the intersection of all conjugates of $H$.

:::

:::

::: {.pf-step #s3}

The kernel of the action of $G$ on the left cosets $G/H$ is the core.

::: pf-proof

The action gives
\[
\varphi:G\to S_{G/H}\cong S_n.
\]
An element $x\in G$ lies in $\ker\varphi$ exactly when
\[
xgH=gH
\]
for every $g\in G$, equivalently when
\[
g^{-1}xg\in H
\]
for every $g$. This is exactly
$x\in\bigcap_g gHg^{-1}$.

:::

:::

::: pf-step

Therefore $G/\operatorname{core}_G(H)$ embeds in $S_n$.

::: pf-proof

By step [](#s3){.pf-ref} and the first isomorphism theorem,
\[
G/\operatorname{core}_G(H)\cong\operatorname{im}\varphi\le S_n.
\]
The maximality assertion is steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
