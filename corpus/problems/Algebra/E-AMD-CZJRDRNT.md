---
schema: qual/card@1
id: E-AMD-CZJRDRNT
kind: problem
title: $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic but not equal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
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
Show that $\QQ(2^{1\over 3})$ and $\QQ(\zeta_3 2^{1\over 3})$ are isomorphic fields, but not identical.
:::

::: {.solution}
Let
\[
\alpha=\sqrt[3]{2},\qquad \beta=\zeta_3\sqrt[3]{2}.
\]
Both are roots of $x^3-2$, which is irreducible over $\QQ$ by Eisenstein at $2$. Hence
\[
\QQ(\alpha)\cong \QQ[x]/(x^3-2)\cong \QQ(\beta),
\]
with the induced isomorphism sending $\alpha$ to $\beta$.

The two subfields of $\CC$ are nevertheless different. Since $\alpha$ is real,
\[
\QQ(\alpha)\subseteq\RR.
\]
But $\beta$ is nonreal, so
\[
\beta\in\QQ(\beta)\setminus\QQ(\alpha).
\]
Therefore
\[
\boxed{\QQ(\sqrt[3]{2})\cong\QQ(\zeta_3\sqrt[3]{2})\quad\text{but}\quad
\QQ(\sqrt[3]{2})\ne\QQ(\zeta_3\sqrt[3]{2}).}
\]
:::
