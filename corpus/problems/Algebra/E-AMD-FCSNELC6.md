---
schema: qual/card@1
id: E-AMD-FCSNELC6
kind: problem
title: $\GF(p^d)\leq\GF(p^n)$ iff $d$ divides $n$
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

::: {.exercise}
Show that $\FF_{p^d} \le \FF_{p^n} \iff d \mid n$.
:::

::: {.solution}
Suppose first that
$$
\FF_{p^d}\subseteq\FF_{p^n}.
$$
Then the tower law gives
$$
n=[\FF_{p^n}:\FF_p]
=[\FF_{p^n}:\FF_{p^d}]\,[\FF_{p^d}:\FF_p]
=[\FF_{p^n}:\FF_{p^d}]\,d,
$$
so $d\mid n$.

Conversely, assume $d\mid n$. In an algebraic closure of $\FF_p$,
$$
\FF_{p^m}=\{x:x^{p^m}=x\}.
$$
If $n=dk$ and $x^{p^d}=x$, then iterating the $p^d$-power Frobenius $k$ times gives
$$
x^{p^n}=x.
$$
Hence every element of $\FF_{p^d}$ lies in $\FF_{p^n}$. Thus
$$
\boxed{\FF_{p^d}\subseteq\FF_{p^n}\iff d\mid n.}
$$
:::
