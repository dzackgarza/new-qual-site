---
schema: qual/card@1
id: P-MMAQ-OSVOY6VRAB
kind: problem
title: Galois group and intermediate fields of $\QQ(\zeta_{12})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Describe the Galois group and the intermediate fields of the cyclotomic extension $\QQ(\zeta_{12})/\QQ$.
:::

::: {.solution}

::: pf

::: pf-step

The extension $\QQ(\zeta_{12})/\QQ$ is Galois of degree $4$, with
\[
\operatorname{Gal}(\QQ(\zeta_{12})/\QQ)
\cong(\ZZ/12\ZZ)^\times
=\{1,5,7,11\}
\cong C_2\times C_2.
\]

::: pf-proof

The $12$th cyclotomic polynomial has degree
\[
\varphi(12)=4,
\]
so
\[
[\QQ(\zeta_{12}):\QQ]=4.
\]
Cyclotomic extensions are Galois, and every automorphism is determined by
\[
\sigma_a(\zeta_{12})=\zeta_{12}^a,
\qquad a\in(\ZZ/12\ZZ)^\times.
\]
The units modulo $12$ are $1,5,7,11$, and each nonidentity element has order $2$, so the group is the Klein four group.

:::

:::

::: pf-step

The field $\QQ(\zeta_{12})$ equals
\[
\QQ(i,\sqrt3).
\]

::: pf-proof

We have
\[
i=\zeta_{12}^3
\]
and
\[
\sqrt3=\zeta_{12}+\zeta_{12}^{-1}=2\cos(\pi/6).
\]
Hence $\QQ(i,\sqrt3)\subseteq\QQ(\zeta_{12})$. Conversely,
\[
\zeta_{12}=\cos(\pi/6)+i\sin(\pi/6)=\frac{\sqrt3+i}{2},
\]
so $\zeta_{12}\in\QQ(i,\sqrt3)$.

:::

:::

::: {.pf-step #s3}

The subgroup
\[
H_i=\{1,5\}\le(\ZZ/12\ZZ)^\times
\]
fixes exactly $\QQ(i)$.

::: pf-proof

Since $i=\zeta_{12}^3$,
\[
\sigma_a(i)=i
\iff \zeta_{12}^{3a}=\zeta_{12}^3
\iff 3(a-1)\equiv0\pmod{12}
\iff a\equiv1\pmod4.
\]
Among $1,5,7,11$, this gives $a=1,5$. Thus the stabilizer of $i$ is $H_i$. Its fixed field has degree
\[
[\QQ(\zeta_{12})^{H_i}:\QQ]=\frac4{|H_i|}=2,
\]
and contains the quadratic field $\QQ(i)$, so equality holds.

:::

:::

::: {.pf-step #s4}

The subgroup
\[
H_{\sqrt3}=\{1,11\}
\]
fixes exactly $\QQ(\sqrt3)$.

::: pf-proof

The automorphism $\sigma_{11}$ is complex conjugation because $11\equiv-1\pmod{12}$. Hence it fixes
\[
\zeta_{12}+\zeta_{12}^{-1}=\sqrt3.
\]
Thus $\QQ(\sqrt3)$ lies in the fixed field of $H_{\sqrt3}$. Both fields have degree $2$ over $\QQ$, so they are equal.

:::

:::

::: {.pf-step #s5}

The subgroup
\[
H_{\sqrt{-3}}=\{1,7\}
\]
fixes exactly $\QQ(\sqrt{-3})=\QQ(\zeta_3)$.

::: pf-proof

Since
\[
\zeta_3=\zeta_{12}^4,
\]
we have
\[
\sigma_a(\zeta_3)=\zeta_3
\iff 4(a-1)\equiv0\pmod{12}
\iff a\equiv1\pmod3.
\]
Among the units modulo $12$, this gives $a=1,7$. Hence the fixed field of $\{1,7\}$ contains $\QQ(\zeta_3)=\QQ(\sqrt{-3})$; both have degree $2$ over $\QQ$, so they are equal.

:::

:::

::: pf-step

Therefore the complete list of intermediate fields is
\[
\boxed{
\QQ,
\quad \QQ(i),
\quad \QQ(\sqrt3),
\quad \QQ(\sqrt{-3}),
\quad \QQ(\zeta_{12})}.
\]

::: pf-proof

By the fundamental theorem of Galois theory, intermediate fields correspond bijectively to subgroups of the Klein four group. That group has exactly five subgroups: the whole group, the trivial subgroup, and its three distinct subgroups of order $2$. The corresponding three quadratic fixed fields were identified in steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
