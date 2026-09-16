---
schema: qual/card@1
id: P-BL7XW
kind: problem
title: Groups of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Group Presentations
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
Classify all groups of order $p^3$ for $p$ prime up to isomorphism.
:::

::: {.solution}
There are exactly five groups of order \(p^3\) up to isomorphism.

The three abelian groups are
\[
C_{p^3},\qquad C_{p^2}\times C_p,\qquad C_p^3.
\]

If \(p=2\), the two nonabelian groups are
\[
D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle
\]
and \(Q_8\).

Now assume \(p\) is odd and \(G\) is nonabelian of order \(p^3\). Then \(|Z(G)|=p\), \(G/Z(G)\cong C_p^2\), and \([G,G]=Z(G)\). There are two cases.

If \(G\) contains an element of order \(p^2\), then its cyclic subgroup \(\langle a\rangle\) has index \(p\) and is normal. Choosing \(b\notin\langle a\rangle\), conjugation by \(b\) induces the unique subgroup of order \(p\) in \(\operatorname{Aut}(C_{p^2})\), so
\[
G\cong\langle a,b\mid a^{p^2}=b^p=1,\ bab^{-1}=a^{1+p}\rangle.
\]

If every nonidentity element has order \(p\), choose \(x,y\) whose images form a basis of \(G/Z(G)\), and let \(z=[x,y]\), which generates \(Z(G)\). Then
\[
G\cong\langle x,y,z\mid x^p=y^p=z^p=1,\ [x,y]=z,\ [x,z]=[y,z]=1\rangle,
\]
the Heisenberg group \(UT_3(\mathbb F_p)\).

The two nonabelian groups are nonisomorphic because their exponents are \(p^2\) and \(p\), respectively. Hence there are exactly five groups of order \(p^3\).
:::
