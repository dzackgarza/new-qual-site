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
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: "The source statement was a bullet item that did not declare $p$; the statement now says that $p$ is a prime and $n$ a positive integer."
---

::: {.problem}
Let $p$ be a prime and $n$ a positive integer.
Show that a field with $p^n$ elements has exactly one subfield of size $p^d$ for every $d$ dividing $n$.
:::

::: {.solution}
Let $F=\FF_{p^n}$. The Frobenius automorphism
$$
\varphi(x)=x^p
$$
generates
$$
\Gal(F/\FF_p)\cong C_n.
$$
If $d\mid n$, then $\langle\varphi^d\rangle$ has order $n/d$, so its fixed field has degree $d$ over $\FF_p$ and therefore has $p^d$ elements. Explicitly, that fixed field is
$$
F_d=\{x\in F:x^{p^d}=x\}.
$$
Thus a subfield of order $p^d$ exists for every $d\mid n$.

It is unique. If $K\subseteq F$ has $p^d$ elements, then every $x\in K$ satisfies $x^{p^d}=x$, so
$$
K\subseteq F_d.
$$
Both fields have $p^d$ elements, hence $K=F_d$.

Conversely, if $K\subseteq\FF_{p^n}$ has $p^d$ elements, then
$$
p^n=\abs{K}^{[F:K]}=p^{d[F:K]},
$$
so $d\mid n$. Therefore the subfields of $\FF_{p^n}$ are exactly the unique fields $\FF_{p^d}$ for divisors $d$ of $n$.
:::
