---
schema: qual/card@1
id: P-OFICU
kind: problem
title: $\lim_{p\to\infty}\|f\|_p=\|f\|_\infty$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Merged P-VAZ7S, a statement reconstructed from a solutions-only document that assumes f essentially bounded on a finite measure space; its solution omits the case of infinite essential supremum and was not carried."
---


::: {.problem}
Let $f$ be a nonnegative measurable function on $[0,1]$. Show that
\[
\lim_{p\to\infty}
\left(\int_0^1 f(x)^p\,dx\right)^{1/p}
=\|f\|_\infty.
\]
:::

::: {.solution}
Write
\[
M:=\|f\|_\infty\in[0,\infty].
\]

<1>1. Suppose first that $M<\infty$.
::: {.proof}
Since $f\le M$ almost everywhere and $m([0,1])=1$,
\[
\|f\|_p^p=\int_0^1 f^p\le M^p,
\]
so
\[
\|f\|_p\le M.
\]
Thus
\[
\limsup_{p\to\infty}\|f\|_p\le M.
\]

Fix $0<a<M$. By the definition of essential supremum,
\[
E_a:=\{x\in[0,1]:f(x)>a\}
\]
has positive measure. Hence
\[
\|f\|_p^p
\ge \int_{E_a}f^p
\ge a^p m(E_a),
\]
so
\[
\|f\|_p\ge a\,m(E_a)^{1/p}.
\]
Letting $p\to\infty$ gives
\[
\liminf_{p\to\infty}\|f\|_p\ge a.
\]
Since this holds for every $a<M$,
\[
\liminf_{p\to\infty}\|f\|_p\ge M.
\]
Therefore
\[
\lim_{p\to\infty}\|f\|_p=M.
\]
:::

<1>2. Suppose now that $M=\infty$.
::: {.proof}
Fix $A>0$. Since the essential supremum is infinite,
\[
E_A:=\{x:f(x)>A\}
\]
has positive measure. Exactly as above,
\[
\|f\|_p\ge A\,m(E_A)^{1/p}.
\]
Hence
\[
\liminf_{p\to\infty}\|f\|_p\ge A.
\]
Because $A>0$ is arbitrary,
\[
\|f\|_p\longrightarrow\infty=M.
\]
Thus in all cases,
\[
\boxed{\lim_{p\to\infty}\|f\|_p=\|f\|_\infty.}
\]
:::
:::
