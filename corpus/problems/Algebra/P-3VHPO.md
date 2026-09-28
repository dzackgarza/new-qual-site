---
schema: qual/card@1
id: P-3VHPO
kind: problem
title: $\QQ(2^{1\over 3})$ and $\QQ(\zeta_3 2^{1\over 3})$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
relations: []
review: draft
---

::: {.problem}
Show that
\[
\QQ(2^{1/3})
\qquad\text{and}\qquad
\QQ(\zeta_3 2^{1/3})
\]
are isomorphic fields over $\QQ$, but are not identical as subfields of $\CC$.
:::

::: {.solution}
Let
\[
\alpha=2^{1/3},
\qquad
\beta=\zeta_3\alpha.
\]
Both satisfy
\[
x^3-2=0.
\]
The polynomial $x^3-2$ is irreducible over $\QQ$ by Eisenstein at $2$, so it is the minimal polynomial of both $\alpha$ and $\beta$. Hence
\[
\QQ(\alpha)
\cong
\QQ[x]/(x^3-2)
\cong
\QQ(\beta),
\]
with the isomorphism sending $\alpha$ to $\beta$.

The fields are nevertheless distinct as subfields of $\CC$. Since $\alpha$ is real,
\[
\QQ(\alpha)\subset\RR.
\]
But $\beta=\zeta_3\alpha$ is nonreal, so
\[
\beta\notin\QQ(\alpha).
\]
Therefore
\[
\QQ(2^{1/3})\ne\QQ(\zeta_3 2^{1/3})
\]
as subsets of $\CC$, even though they are isomorphic as $\QQ$-fields.
:::
