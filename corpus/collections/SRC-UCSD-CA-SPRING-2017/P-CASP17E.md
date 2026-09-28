---
schema: qual/card@1
id: P-CASP17E
kind: problem
title: "Holomorphic functions on D with f(0)=1 and Re f > 0 form a normal family"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Montel
relations: []
review: draft
---

::: {.problem}
Let $\mathcal{F}$ be the family of holomorphic functions $f : \mathbb{D} \to \mathbb{C}$ defined over the open unit disc with $f(0) = 1$ and $\operatorname{Re} f > 0$.
Show that $\mathcal{F}$ is a normal family.
:::

::: {.solution}
For $f\in\mathcal F$, define
\[
\phi_f(z)=\frac{f(z)-1}{f(z)+1}.
\]
Because $\operatorname{Re}f>0$, this maps $\mathbb D$ holomorphically into
$\mathbb D$, and $\phi_f(0)=0$. Schwarz's lemma gives
\[
|\phi_f(z)|\le |z|.
\]
Hence, for $|z|\le r<1$,
\[
|f(z)|=\left|\frac{1+\phi_f(z)}{1-\phi_f(z)}\right|
\le \frac{1+r}{1-r}.
\]
Thus $\mathcal F$ is locally uniformly bounded. Montel's theorem implies that
$\mathcal F$ is normal.
:::
