---
schema: qual/card@1
id: P-MMAQ-OSVOY6VRAB
kind: problem
title: Galois group and intermediate fields of $\mathbb Q(\zeta_{12})/\mathbb Q$
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

::: problem
Describe the Galois group and the intermediate fields of the cyclotomic extension $\mathbb Q(\zeta_{12})/\mathbb Q$.
:::


::: solution
<1>1. The extension $\mathbb Q(\zeta_{12})/\mathbb Q$ is Galois of degree $4$, with
\[
\operatorname{Gal}(\mathbb Q(\zeta_{12})/\mathbb Q)
\cong(\mathbb Z/12\mathbb Z)^\times
=\{1,5,7,11\}
\cong C_2\times C_2.
\]
::: {.proof}
The $12$th cyclotomic polynomial has degree
\[
\varphi(12)=4,
\]
so
\[
[\mathbb Q(\zeta_{12}):\mathbb Q]=4.
\]
Cyclotomic extensions are Galois, and every automorphism is determined by
\[
\sigma_a(\zeta_{12})=\zeta_{12}^a,
\qquad a\in(\mathbb Z/12\mathbb Z)^\times.
\]
The units modulo $12$ are $1,5,7,11$, and each nonidentity element has order $2$, so the group is the Klein four group.
:::

<1>2. The field $\mathbb Q(\zeta_{12})$ equals
\[
\mathbb Q(i,\sqrt3).
\]
::: {.proof}
We have
\[
i=\zeta_{12}^3
\]
and
\[
\sqrt3=\zeta_{12}+\zeta_{12}^{-1}=2\cos(\pi/6).
\]
Hence $\mathbb Q(i,\sqrt3)\subseteq\mathbb Q(\zeta_{12})$. Conversely,
\[
\zeta_{12}=\cos(\pi/6)+i\sin(\pi/6)=\frac{\sqrt3+i}{2},
\]
so $\zeta_{12}\in\mathbb Q(i,\sqrt3)$.
:::

<1>3. The subgroup
\[
H_i=\{1,5\}\le(\mathbb Z/12\mathbb Z)^\times
\]
fixes exactly $\mathbb Q(i)$.
::: {.proof}
Since $i=\zeta_{12}^3$,
\[
\sigma_a(i)=i
\iff \zeta_{12}^{3a}=\zeta_{12}^3
\iff 3(a-1)\equiv0\pmod{12}
\iff a\equiv1\pmod4.
\]
Among $1,5,7,11$, this gives $a=1,5$. Thus the stabilizer of $i$ is $H_i$. Its fixed field has degree
\[
[\mathbb Q(\zeta_{12})^{H_i}:\mathbb Q]=\frac4{|H_i|}=2,
\]
and contains the quadratic field $\mathbb Q(i)$, so equality holds.
:::

<1>4. The subgroup
\[
H_{\sqrt3}=\{1,11\}
\]
fixes exactly $\mathbb Q(\sqrt3)$.
::: {.proof}
The automorphism $\sigma_{11}$ is complex conjugation because $11\equiv-1\pmod{12}$. Hence it fixes
\[
\zeta_{12}+\zeta_{12}^{-1}=\sqrt3.
\]
Thus $\mathbb Q(\sqrt3)$ lies in the fixed field of $H_{\sqrt3}$. Both fields have degree $2$ over $\mathbb Q$, so they are equal.
:::

<1>5. The subgroup
\[
H_{\sqrt{-3}}=\{1,7\}
\]
fixes exactly $\mathbb Q(\sqrt{-3})=\mathbb Q(\zeta_3)$.
::: {.proof}
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
Among the units modulo $12$, this gives $a=1,7$. Hence the fixed field of $\{1,7\}$ contains $\mathbb Q(\zeta_3)=\mathbb Q(\sqrt{-3})$; both have degree $2$ over $\mathbb Q$, so they are equal.
:::

<1>6. Therefore the complete list of intermediate fields is
\[
\boxed{
\mathbb Q,
\quad \mathbb Q(i),
\quad \mathbb Q(\sqrt3),
\quad \mathbb Q(\sqrt{-3}),
\quad \mathbb Q(\zeta_{12})}.
\]
::: {.proof}
By the fundamental theorem of Galois theory, intermediate fields correspond bijectively to subgroups of the Klein four group. That group has exactly five subgroups: the whole group, the trivial subgroup, and its three distinct subgroups of order $2$. The corresponding three quadratic fixed fields were identified in <1>3--<1>5.
:::
:::
