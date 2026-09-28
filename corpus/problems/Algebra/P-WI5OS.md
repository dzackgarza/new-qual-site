---
schema: qual/card@1
id: P-WI5OS
kind: problem
title: The center of $S_n$ is trivial for $n\geq 4$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
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
Show that the center of $S_n$ for $n\geq 4$ (and in fact $n \ge 3$) is trivial.
:::

::: {.solution}
Let $\sigma\in Z(S_n)$ with $n\ge3$. Suppose $\sigma\ne1$. Choose $a$ with
\[
\sigma(a)=b\ne a,
\]
and choose $c$ distinct from $a,b$. Let
\[
\tau=(bc).
\]
Then $\tau(a)=a$, so
\[
(\sigma\tau)(a)=\sigma(a)=b,
\]
whereas
\[
(\tau\sigma)(a)=\tau(b)=c.
\]
Thus $\sigma\tau\ne\tau\sigma$, contradicting centrality. Hence
\[
\boxed{Z(S_n)=\{1\}\qquad(n\ge3)}.
\]
:::
