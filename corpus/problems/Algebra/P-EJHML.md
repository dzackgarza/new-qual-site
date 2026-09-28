---
schema: qual/card@1
id: P-EJHML
kind: problem
title: Unique subfield of order $p^d$ in a field with $p^n$ elements
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that a field with $p^n$ elements has exactly one subfield of size $p^d$ for every $d$ dividing $n$.
:::

::: {.solution}
Let $F=\mathbb F_{p^n}$. The Frobenius automorphism
\[
\varphi(x)=x^p
\]
generates
\[
\operatorname{Gal}(F/\mathbb F_p)\cong C_n.
\]
If $d\mid n$, then $\langle\varphi^d\rangle$ has order $n/d$, so its fixed field has degree $d$ over $\mathbb F_p$ and therefore has $p^d$ elements. Explicitly, that fixed field is
\[
F_d=\{x\in F:x^{p^d}=x\}.
\]
Thus a subfield of order $p^d$ exists for every $d\mid n$.

It is unique. If $K\subseteq F$ has $p^d$ elements, then every $x\in K$ satisfies $x^{p^d}=x$, so
\[
K\subseteq F_d.
\]
Both fields have $p^d$ elements, hence $K=F_d$.

Conversely, if $K\subseteq\mathbb F_{p^n}$ has $p^d$ elements, then
\[
p^n=|K|^{[F:K]}=p^{d[F:K]},
\]
so $d\mid n$. Therefore the subfields of $\mathbb F_{p^n}$ are exactly the unique fields $\mathbb F_{p^d}$ for divisors $d$ of $n$.
:::
