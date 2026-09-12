---
schema: qual/card@1
id: E-AMD-JDUI45J5
kind: problem
title: Intermediate fields of $\QQ(2^{1/4},\zeta_8)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Re-derived the full D4 subgroup/fixed-field correspondence and retained all intermediate fields.
---

::: {.exercise}
Compute all intermediate fields of $\mathbb Q(2^{1/4},\zeta_8)$ over $\mathbb Q$.
:::

::: {.solution}
Let $\alpha=2^{1/4}$ and
\[
K=\mathbb Q(\alpha,\zeta_8).
\]
Since $\alpha^2=\sqrt2$ and $\zeta_8=(1+i)/\sqrt2$,
\[
i=\alpha^2\zeta_8-1,
\]
so $K=\mathbb Q(\alpha,i)$, the splitting field of $x^4-2$.

<1>1. The Galois group is $D_4$ of order $8$.
::: {.proof}
Eisenstein gives $[\mathbb Q(\alpha):\mathbb Q]=4$, and $i\notin\mathbb Q(\alpha)\subset\mathbb R$, hence $[K:\mathbb Q]=8$. Define
\[
\sigma(\alpha)=i\alpha,\quad \sigma(i)=i,
\qquad
\tau(\alpha)=\alpha,\quad \tau(i)=-i.
\]
Then $\sigma^4=\tau^2=1$ and $\tau\sigma\tau=\sigma^{-1}$, so
\[
G=\operatorname{Gal}(K/\mathbb Q)=\langle\sigma,\tau\rangle\cong D_4.
\]
:::

<1>2. The three quadratic intermediate fields are
\[
\mathbb Q(i),\qquad \mathbb Q(\sqrt2),\qquad \mathbb Q(i\sqrt2).
\]
::: {.proof}
They are the fixed fields of the three order-$4$ subgroups
\[
\langle\sigma\rangle,\qquad
\langle\sigma^2,\tau\rangle,\qquad
\langle\sigma^2,\sigma\tau\rangle,
\]
respectively. Each displayed generator is fixed by the corresponding subgroup and generates a quadratic extension, so the fixed field is exactly the one shown.
:::

<1>3. The five quartic intermediate fields are
\[
\mathbb Q(\zeta_8),\quad
\mathbb Q(\alpha),\quad
\mathbb Q(i\alpha),\quad
\mathbb Q((1+i)\alpha),\quad
\mathbb Q((1-i)\alpha).
\]
::: {.proof}
The five order-$2$ subgroups of $D_4$ are
\[
\langle\sigma^2\rangle,
\langle\tau\rangle,
\langle\sigma^2\tau\rangle,
\langle\sigma\tau\rangle,
\langle\sigma^3\tau\rangle.
\]
Their respective fixed fields are the five fields displayed above. For example, $\sigma^2$ fixes $i$ and $\alpha^2=\sqrt2$, hence fixes $\mathbb Q(i,\sqrt2)=\mathbb Q(\zeta_8)$; and $\sigma\tau$ fixes $(1+i)\alpha$. Each fixed field has degree $4$, so the indicated degree-$4$ subfield is the full fixed field.
:::

Together with $\mathbb Q$ and $K$, these are all intermediate fields, because they account for all ten subgroups of $D_4$.
:::
