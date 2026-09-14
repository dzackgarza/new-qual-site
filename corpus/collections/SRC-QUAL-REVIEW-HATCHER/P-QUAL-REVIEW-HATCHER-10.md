---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-10
kind: problem
title: Cohomological matrices of homeomorphisms of a product of even-dimensional spheres
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 10 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The MinerU display of the eight matrices is garbled; “the eight signed permutation matrices” is the exact compact description of the four displayed ±/∓ matrix patterns.
---

::: {.problem}
Let
\[
f:S^n\times S^n\longrightarrow S^n\times S^n
\]
be a homeomorphism.
Let $z$ generate $H^n(S^n)$ and put
\[
\alpha=z\times1,\qquad \beta=1\times z
\]
in $H^n(S^n\times S^n)$.
Write
\[
f^*(\alpha)=k\alpha+l\beta,\qquad f^*(\beta)=p\alpha+q\beta
\]
for integers $k,l,p,q$.

Prove that if $n$ is even, then
\[
\begin{pmatrix}k&l\\ p&q\end{pmatrix}
\]
is one of the eight signed permutation matrices.
Also find homeomorphisms $f$ realizing all eight possibilities.
:::
