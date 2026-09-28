---
schema: qual/card@1
id: P-67WAD
kind: problem
title: The splitting field of $x^3-2$ is $\QQ(\sqrt[3]{2},\zeta_3)$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Roots of Unity
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that the splitting field of $f(x) = x^3-2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$ (where $\zeta_3 = e^{2\pi i/3}$).
:::

::: {.solution}
Let $\alpha=\sqrt[3]{2}$ and let $\zeta_3$ be a primitive cube root of unity. The roots of
\[
x^3-2
\]
are
\[
\alpha,\qquad \zeta_3\alpha,\qquad \zeta_3^2\alpha.
\]
Hence
\[
K=\mathbb Q(\alpha,\zeta_3)
\]
contains all roots, so the splitting field $L$ is contained in $K$.

Conversely, $L$ contains $\alpha$ and $\zeta_3\alpha$, hence also
\[
\zeta_3=\frac{\zeta_3\alpha}{\alpha}.
\]
Therefore $K\subseteq L$, and so
\[
L=\mathbb Q(\sqrt[3]{2},\zeta_3).
\]

Moreover, $[\mathbb Q(\alpha):\mathbb Q]=3$ by Eisenstein at $2$, and $\zeta_3\notin\mathbb R$ while $\mathbb Q(\alpha)\subset\mathbb R$. Thus adjoining $\zeta_3$ has degree $2$, giving
\[
[L:\mathbb Q]=6.
\]
:::
