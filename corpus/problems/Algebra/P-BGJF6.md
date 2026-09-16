---
schema: qual/card@1
id: P-BGJF6
kind: problem
title: Definition of a splitting field
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Polynomials
  - Field Extensions
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
State the definition of the splitting field of a polynomial $f(x) \in F[x]$ over a field $F$.
Prove the existence and uniqueness (up to $F$-isomorphism) of splitting fields.
:::

::: {.solution}
A splitting field of \(f\in F[x]\) is an extension \(L/F\) such that

1. \(f\) splits into linear factors in \(L[x]\), and
2. \(L\) is generated over \(F\) by the roots of \(f\).

Existence follows by induction on \(\deg f\). If \(f\) does not already split, choose an irreducible factor \(p\) of degree \(>1\) and form
\[
E=F[x]/(p).
\]
The class of \(x\) is a root of \(p\), hence of \(f\), so over \(E\) one linear factor can be removed. Induction on the remaining degree produces a field in which all roots lie; adjoining exactly those roots gives a splitting field.

For uniqueness, let \(L_1,L_2\) be splitting fields of \(f\) over \(F\). We extend an embedding one root at a time. Suppose \(E\subseteq L_1\) has already been embedded into \(L_2\) by \(\varphi:E\to L_2\), and let \(\alpha\in L_1\) be another root of \(f\). Let \(m_{\alpha,E}(x)\in E[x]\) be its minimal polynomial over \(E\). Since \(m_{\alpha,E}\mid f\) in \(E[x]\), the transported polynomial \(\varphi(m_{\alpha,E})\) divides \(f\) in \(\varphi(E)[x]\). Because \(f\) splits in \(L_2\), this polynomial has a root \(\beta\in L_2\). The standard simple-extension theorem therefore extends \(\varphi\) to
\[
E(\alpha)\longrightarrow L_2,
\qquad \alpha\longmapsto\beta.
\]
Starting from \(E=F\) and repeating over the finitely many roots gives an \(F\)-embedding \(L_1\to L_2\). Its image is a splitting field of \(f\) inside \(L_2\); by minimality of \(L_2\), the image is all of \(L_2\). Thus splitting fields are unique up to \(F\)-isomorphism.
:::
