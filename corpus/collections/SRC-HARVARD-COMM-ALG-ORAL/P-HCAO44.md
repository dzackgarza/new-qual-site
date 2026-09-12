---
schema: qual/card@1
id: P-HCAO44
kind: problem
title: Residue field before and after localization
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Local Rings
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $M$ be an $A$-module, and let $\mathfrak m$ be a maximal ideal of $A$.
Prove that
\[
M/\mathfrak mM \cong M_{\mathfrak m}/\mathfrak mM_{\mathfrak m}.
\]
:::

::: solution
Define
\[
\phi:M/\mathfrak mM\longrightarrow M_{\mathfrak m}/\mathfrak mM_{\mathfrak m},
\qquad
m+\mathfrak mM\longmapsto m/1+\mathfrak mM_{\mathfrak m}.
\]

<1>1. The map $\phi$ is well-defined.
::: proof
If $m-m'\in\mathfrak mM$, then $(m-m')/1\in\mathfrak mM_{\mathfrak m}$.
:::

<1>2. The map $\phi$ is surjective.
::: proof
Every class on the right is represented by $m/s$ with $s\notin\mathfrak m$.
Since $\mathfrak m$ is maximal, the image of $s$ in $A/\mathfrak m$ is a unit;
choose $a\in A$ with $as\equiv1\pmod{\mathfrak m}$. Then
\[
\frac ms-\frac{am}{1}=\frac{(1-as)m}{s}\in\mathfrak mM_{\mathfrak m}.
\]
Thus the class of $m/s$ is $\phi(am+\mathfrak mM)$.
:::

<1>3. The map $\phi$ is injective.
::: proof
Suppose $m/1\in\mathfrak mM_{\mathfrak m}$. Then for some $s\notin\mathfrak m$,
$s m\in\mathfrak mM$. Choose $a$ with $as\equiv1\pmod{\mathfrak m}$. Then
\[
m=asm+(1-as)m\in\mathfrak mM.
\]
Hence $m+\mathfrak mM=0$.
:::

Therefore $\phi$ is an isomorphism.
:::
