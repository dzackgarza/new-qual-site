---
schema: qual/card@1
id: P-ALGS14A
kind: problem
title: Proper subgroups of finite $p$-groups are properly contained in their normalizers
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $G$ be a finite $p$-group.
Show that, if $H$ is a proper subgroup of $G$, then $H$ is a proper subgroup of its normalizer $N_G(H)$.
(Hint: center of a finite $p$-group is non-trivial.)
:::

::: {.solution}
<1>1. We argue by induction on \,\(|G|\). The result is trivial for \(|G|=p\).
::: {.proof}
The only proper subgroup is the trivial subgroup, whose normalizer is all of \(G\).
:::

<1>2. Let \(Z=Z(G)\). Since \(G\) is a nontrivial finite \(p\)-group, \(Z\neq 1\).
::: {.proof}
The center of every nontrivial finite \(p\)-group is nontrivial.
:::

<1>3. If \(Z\nsubseteq H\), then \(H<N_G(H)\).
::: {.proof}
Choose \(z\in Z\setminus H\). Because \(z\) is central, \(zHz^{-1}=H\), so \(z\in N_G(H)\setminus H\). Hence the inclusion \(H\le N_G(H)\) is proper.
:::

<1>4. Suppose \(Z\le H\). Then \(H/Z\) is a proper subgroup of the finite \(p\)-group \(G/Z\).
::: {.proof}
Since \(H<G\) and \(Z\le H\), equality \(H/Z=G/Z\) would imply \(H=G\), impossible.
Also \(G/Z\) is again a finite \(p\)-group and has smaller order than \(G\).
:::

<1>5. By induction,
\[
H/Z<N_{G/Z}(H/Z).
\]
::: {.proof}
Apply the induction hypothesis to the proper subgroup \(H/Z<G/Z\).
:::

<1>6. We have
\[
N_{G/Z}(H/Z)=N_G(H)/Z.
\]
::: {.proof}
For \(g\in G\), the coset \(gZ\) normalizes \(H/Z\) iff
\[
(gZ)(H/Z)(gZ)^{-1}=H/Z,
\]
which is equivalent to \(gHg^{-1}Z=H\). Because \(Z\le H\), this is equivalent to \(gHg^{-1}=H\), i.e. \(g\in N_G(H)\).
:::

<1>7. Therefore \(H<N_G(H)\).
::: {.proof}
By <1>5 and <1>6, \(H/Z\) is properly contained in \(N_G(H)/Z\). Hence \(H\) is properly contained in \(N_G(H)\).
:::
:::
