---
schema: qual/card@1
id: P-WESRA10-II4
kind: problem
title: 'Continuity of translations in $L^1$'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash drops the absolute-value delimiters in the displayed integral; the card records the only norm-continuity statement compatible with the surrounding translation question.
---

::: {.problem}
Let $f\in L^1(\RR)$ and define $f_t(x)=f(x-t)$.
Prove
\[
\lim_{t\to0}\int_{\RR}|f-f_t|\,dm=0.
\]
If $A\subset\RR$ has finite Lebesgue measure, explain what this says about the translates $A+t$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $g\in C_c(\RR)$, then
\[
\|g-g_t\|_1\longrightarrow0
\qquad(t\to0).
\]


::: pf-proof

Choose $R>0$ such that
\[
\operatorname{supp}(g)\subseteq[-R,R].
\]
For $|t|\le1$, both $g$ and $g_t$ vanish outside
\[
[-R-1,R+1].
\]
Since $g$ is uniformly continuous on $\RR$,
\[
\sup_{x\in\RR}|g(x)-g(x-t)|\longrightarrow0
\]
as $t\to0$. Hence, for $|t|\le1$,
\[
\|g-g_t\|_1
\le
2(R+1)\sup_{x\in\RR}|g(x)-g(x-t)|,
\]
and the right-hand side tends to $0$.

:::

:::

::: {.pf-step #s1-2}

Translation preserves the $L^1$ norm:
\[
\|h_t\|_1=\|h\|_1
\]
for every $h\in L^1(\RR)$ and every $t\in\RR$.


::: pf-proof

By the translation invariance of Lebesgue measure,
\[
\|h_t\|_1
=\int_{\RR}|h(x-t)|\,dx
=\int_{\RR}|h(u)|\,du
=\|h\|_1.
\]

:::

:::

::: {.pf-step #s1-3}

For every $f\in L^1(\RR)$,
\[
\boxed{\|f-f_t\|_1\longrightarrow0}
\qquad(t\to0).
\]


::: pf-proof

Fix $\varepsilon>0$. Since $C_c(\RR)$ is dense in $L^1(\RR)$,
choose $g\in C_c(\RR)$ such that
\[
\|f-g\|_1<\frac{\varepsilon}{3}.
\]
By step [](#s1-1){.pf-ref}, for all sufficiently small $|t|$,
\[
\|g-g_t\|_1<\frac{\varepsilon}{3}.
\]
Using step [](#s1-2){.pf-ref},
\[
\|f_t-g_t\|_1
=\|(f-g)_t\|_1
=\|f-g\|_1
<\frac{\varepsilon}{3}.
\]
Therefore
\[
\|f-f_t\|_1
\le
\|f-g\|_1+\|g-g_t\|_1+\|g_t-f_t\|_1
<\varepsilon.
\]
This proves the limit.

:::

:::

::: {.pf-step #s1-4}

If $A\subseteq\RR$ is measurable with finite measure, then
\[
\boxed{m(A\triangle(A+t))\longrightarrow0}
\qquad(t\to0).
\]


::: pf-proof

Take
\[
f=\chi_A\in L^1(\RR).
\]
Then
\[
f_t(x)=\chi_A(x-t)=\chi_{A+t}(x).
\]
Moreover,
\[
|\chi_A-\chi_{A+t}|
=\chi_{A\triangle(A+t)}.
\]
Hence step [](#s1-3){.pf-ref} gives
\[
m(A\triangle(A+t))
=\|\chi_A-\chi_{A+t}\|_1
\longrightarrow0.
\]

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the translation-continuity statement, and step [](#s1-4){.pf-ref} gives
its consequence for finite-measure sets.

:::

:::

:::
