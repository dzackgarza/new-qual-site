---
schema: qual/card@1
id: E-AMD-E3UUQEAP
kind: problem
title: Splitting field of $x^3-2$ is $\QQ(\sqrt[3]{2},\zeta_3)$
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
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that the splitting field of $f(x) = x^3-2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.
:::

::: {.solution}
Let
\[
\alpha=\sqrt[3]{2},
\qquad
\zeta_3=e^{2\pi i/3}.
\]
The three roots of \(x^3-2\) are
\[
\alpha,\qquad \alpha\zeta_3,\qquad \alpha\zeta_3^2.
\]
Hence all roots lie in \(\mathbb Q(\alpha,\zeta_3)\), so the splitting field \(L\) satisfies
\[
L\subseteq\mathbb Q(\alpha,\zeta_3).
\]
Conversely, \(L\) contains \(\alpha\) and \(\alpha\zeta_3\), so
\[
\zeta_3=\frac{\alpha\zeta_3}{\alpha}\in L.
\]
Thus \(\alpha,\zeta_3\in L\), giving the reverse inclusion. Therefore
\[
\boxed{L=\mathbb Q(\sqrt[3]{2},\zeta_3).}
\]

For completeness, \(x^3-2\) is Eisenstein at \(2\), so \([\mathbb Q(\alpha):\mathbb Q]=3\). Since \(\mathbb Q(\alpha)\subset\mathbb R\) while \(\zeta_3\notin\mathbb R\), adjoining \(\zeta_3\) has degree \(2\). Hence
\[
[L:\mathbb Q]=6.
\]
:::
