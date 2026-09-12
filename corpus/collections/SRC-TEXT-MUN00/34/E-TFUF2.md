---
schema: qual/card@1
id: E-TFUF2
kind: problem
title: Details of the imbedding theorem proof
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Check the details of the proof of Theorem 34.2 (the imbedding theorem for a space admitting a countable family of continuous functions that separates points from closed sets).
:::

::: {.solution}
Let \(\{f_n:X\to\mathbb R\}_{n\ge1}\) be a countable family of continuous functions that separates points from closed sets, and define
\[
F:X\longrightarrow\mathbb R^\omega,
\qquad
F(x)=(f_1(x),f_2(x),\ldots),
\]
where \(\mathbb R^\omega\) has the product topology. We verify that \(F\) is an embedding.

First, \(F\) is continuous. A subbasic open set in the product has the form
\[
\pi_n^{-1}(U),
\]
with \(U\subset\mathbb R\) open, and
\[
F^{-1}(\pi_n^{-1}(U))=f_n^{-1}(U),
\]
which is open in \(X\).

Second, \(F\) is injective. If \(x\ne y\), the singleton \(\{y\}\) is closed under the hypotheses of the theorem (the space is regular, hence \(T_1\)). Since the family separates points from closed sets, some \(f_n\) satisfies
\[
f_n(x)\notin \overline{f_n(\{y\})}=\{f_n(y)\}.
\]
Thus \(F(x)\ne F(y)\).

It remains to prove that \(F^{-1}:F(X)\to X\) is continuous. It is enough to show that for every open \(U\subset X\) and every \(x\in U\), there is a product-open set \(W\subset\mathbb R^\omega\) such that
\[
F(x)\in W
\quad\text{and}\quad
F^{-1}(W)\subset U.
\]
Let \(C=X-U\), a closed set not containing \(x\). By separation, choose \(f_n\) such that
\[
f_n(x)\notin\overline{f_n(C)}.
\]
There is therefore an open interval \(V\subset\mathbb R\) containing \(f_n(x)\) and disjoint from \(f_n(C)\). Set
\[
W=\pi_n^{-1}(V).
\]
Then \(W\) is product-open, contains \(F(x)\), and if \(z\in F^{-1}(W)\), then \(f_n(z)\in V\), so \(z\notin C\), hence \(z\in U\). Thus
\[
F(U)=F(X)\cap \bigcup_{x\in U}W_x
\]
is open in \(F(X)\). Therefore \(F\) is a homeomorphism from \(X\) onto the subspace \(F(X)\subset\mathbb R^\omega\), as required.
:::
