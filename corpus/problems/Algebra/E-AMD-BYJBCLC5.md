---
schema: qual/card@1
id: E-AMD-BYJBCLC5
kind: problem
title: Normality of $\QQ(\sqrt[3]{2})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Is $\QQ(2^{1\over 3})/\QQ$ normal?
:::

::: {.solution}
No. Let $\alpha=\sqrt[3]{2}$. The polynomial
\[
f(x)=x^3-2
\]
is irreducible over $\QQ$ by Eisenstein at $2$, so it is the minimal polynomial of $\alpha$ over $\QQ$.

Its roots are
\[
\alpha,\qquad \alpha\zeta_3,\qquad \alpha\zeta_3^2,
\]
where $\zeta_3=e^{2\pi i/3}$. Since
\[
\QQ(\alpha)\subseteq\RR,
\]
the two nonreal roots $\alpha\zeta_3$ and $\alpha\zeta_3^2$ do not lie in $\QQ(\alpha)$.

Thus an irreducible polynomial over $\QQ$ has a root in $\QQ(\alpha)$ but does not split there. Hence
\[
\QQ(\sqrt[3]{2})/\QQ
\]
is not normal.
:::
