---
schema: qual/card@1
id: P-ALGF14A
kind: problem
title: Proper subgroups of nilpotent groups are properly contained in their normalizers
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $G$ be a (not necessarily finite) nilpotent group.
Prove that for any proper subgroup $H$ we have that $H \neq N_G(H)$.
:::

::: {.solution}
<1>1. Let
\[
1=Z_0(G)\le Z_1(G)\le \cdots \le Z_c(G)=G
\]
be the upper central series of the nilpotent group \(G\).
::: {.proof}
By nilpotence, the upper central series reaches \(G\) after finitely many steps.
:::

<1>2. Since \(H<G\), there is a least index \(i\ge 1\) such that \(Z_i(G)\nsubseteq H\). Thus
\[
Z_{i-1}(G)\le H.
\]
::: {.proof}
Because \(Z_0(G)=1\le H\) and \(Z_c(G)=G\nsubseteq H\), such a least \(i\) exists.
:::

<1>3. Choose \(x\in Z_i(G)\setminus H\). Then for every \(h\in H\),
\[
[x,h]\in Z_{i-1}(G)\le H.
\]
::: {.proof}
By definition of the upper central series,
\[
Z_i(G)/Z_{i-1}(G)=Z\bigl(G/Z_{i-1}(G)\bigr).
\]
Hence the image of \(x\) is central modulo \(Z_{i-1}(G)\), so \([x,h]\in Z_{i-1}(G)\).
:::

<1>4. The element \(x\) normalizes \(H\).
::: {.proof}
For \(h\in H\), one has
\[
xhx^{-1}=[x,h]h\in H.
\]
Thus \(xHx^{-1}\subseteq H\). Applying the same argument to \(x^{-1}\in Z_i(G)\) gives
\[
x^{-1}Hx\subseteq H,
\]
and conjugating this inclusion by \(x\) yields \(H\subseteq xHx^{-1}\). Therefore
\[
xHx^{-1}=H,
\]
so \(x\in N_G(H)\).
:::

<1>5. Since \(x\notin H\), we have \(H<N_G(H)\).
::: {.proof}
By <1>3, \(x\notin H\), while by <1>4, \(x\in N_G(H)\). Hence the inclusion \(H\le N_G(H)\) is proper.
:::
:::
