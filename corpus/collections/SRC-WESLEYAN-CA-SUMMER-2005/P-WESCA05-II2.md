---
schema: qual/card@1
id: P-WESCA05-II2
kind: problem
title: "Prove the Fundamental Theorem of Algebra using Liouville"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 2 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
\[
f(z)=a_0+a_1z+\cdots+a_nz^n,
\qquad n\ge1,\quad a_n\ne0.
\]
Prove that there exists $z\in\CC$ such that $f(z)=0$.

Hint: use Liouville's theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume for contradiction that
\[
f(z)\ne0
\qquad
\text{for every }z\in\CC.
\]
Then
\[
g(z)=\frac1{f(z)}
\]
is entire.


::: pf-proof

The polynomial \(f\) is entire. Under the stated assumption it has no zeros, so its reciprocal is analytic on all of \(\CC\).

:::

:::

::: {.pf-step #s1-2}

There is \(R>0\) such that
\[
|f(z)|\ge \frac{|a_n|}{2}|z|^n
\qquad
\text{whenever }|z|\ge R.
\]


::: pf-proof

Write
\[
f(z)=z^n\left(
a_n+\frac{a_{n-1}}z+\cdots+\frac{a_0}{z^n}
\right).
\]
As \(|z|\to\infty\), the expression in parentheses tends to \(a_n\). Hence there is \(R>0\) such that, for \(|z|\ge R\),
\[
\left|
a_n+\frac{a_{n-1}}z+\cdots+\frac{a_0}{z^n}
\right|
\ge\frac{|a_n|}{2}.
\]
Multiplying by \(|z|^n\) gives the claimed estimate.

:::

:::

::: {.pf-step #s1-3}

The entire function \(g=1/f\) is bounded outside the disk \(|z|<R\).


::: pf-proof

By step [](#s1-2){.pf-ref}, for \(|z|\ge R\),
\[
|g(z)|
=
\frac1{|f(z)|}
\le
\frac{2}{|a_n||z|^n}
\le
\frac{2}{|a_n|R^n}.
\]

:::

:::

::: {.pf-step #s1-4}

The function \(g\) is bounded on the closed disk
\[
\{z:|z|\le R\}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, \(g\) is continuous on \(\CC\). The closed disk is compact, so the continuous real-valued function \(|g|\) attains a finite maximum there.

:::

:::

::: {.pf-step #s1-5}

The function \(g\) is constant.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} together show that \(g\) is bounded on all of \(\CC\). Since \(g\) is entire by step [](#s1-1){.pf-ref}, Liouville's theorem implies that \(g\) is constant.

:::

:::

::: {.pf-step #s1-6}

The conclusion of step [](#s1-5){.pf-ref} contradicts \(n\ge1\) and \(a_n\ne0\).


::: pf-proof

If \(g=1/f\) is constant and never zero, then \(f=1/g\) is constant. But the polynomial \(f\) has degree \(n\ge1\) because \(a_n\ne0\). This is impossible.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{\text{there exists }z\in\CC\text{ such that }f(z)=0.}
\]


::: pf-proof

The assumption that \(f\) has no zero led to the contradiction in step [](#s1-6){.pf-ref}. Hence \(f\) must have at least one complex zero.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
