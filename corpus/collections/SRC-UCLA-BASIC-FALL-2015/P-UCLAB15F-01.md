---
schema: qual/card@1
id: P-UCLAB15F-01
kind: problem
title: Fekete's lemma for a subadditive positive sequence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $\{a_n\}_{n=1}^{\infty}$ be a sequence of positive numbers such that
\[
a_{n+m}\le a_n+a_m,\qquad m,n\ge1.
\]
Prove that $\lim_{n\to\infty}a_n/n$ exists by showing
\[
\lim_{n\to\infty}\frac{a_n}{n}=\inf_{n\ge1}\frac{a_n}{n}.
\]
Hint: Treat $\liminf$ and $\limsup$ separately.
:::

::: {.solution}
Set
\[
\alpha=\inf_{m\ge1}\frac{a_m}{m}.
\]

<1>1. One has
\[
\liminf_{n\to\infty}\frac{a_n}{n}\ge\alpha.
\]

::: {.proof}
By definition of the infimum,
\[
\frac{a_n}{n}\ge\alpha
\]
for every $n\ge1$.
Taking the lower limit preserves this inequality.
:::

<1>2. Fix an integer $m\ge1$.
For every $n$, write
\[
n=qm+r,
\qquad
q\ge0,
\qquad
0\le r<m.
\]
Then
\[
a_n\le q\,a_m+a_r,
\]
where we set
\[
a_0=0.
\]

::: {.proof}
Repeatedly applying subadditivity gives
\[
a_{qm}
\le
q\,a_m.
\]
If $r>0$, then
\[
a_{qm+r}
\le
a_{qm}+a_r
\le
q\,a_m+a_r.
\]
If $r=0$, the same formula holds with $a_0=0$.
:::

<1>3. Let
\[
C_m=\max\{a_0,a_1,\ldots,a_{m-1}\}.
\]
Then
\[
\frac{a_n}{n}
\le
\frac{q\,a_m}{n}
+
\frac{C_m}{n}.
\]

::: {.proof}
The remainder index $r$ in step <1>2 satisfies
\[
0\le r<m,
\]
so
\[
a_r\le C_m.
\]
Divide the inequality in step <1>2 by $n>0$.
:::

<1>4. For fixed $m$,
\[
\limsup_{n\to\infty}\frac{a_n}{n}
\le
\frac{a_m}{m}.
\]

::: {.proof}
Since
\[
n=qm+r,
\qquad
0\le r<m,
\]
one has
\[
\frac{qm}{n}\to1
\]
as $n\to\infty$.
Hence
\[
\frac{q}{n}\to\frac1m.
\]
Also
\[
\frac{C_m}{n}\to0.
\]
Taking $\limsup$ in step <1>3 gives
\[
\limsup_{n\to\infty}\frac{a_n}{n}
\le
\frac{a_m}{m}.
\]
:::

<1>5. Therefore
\[
\limsup_{n\to\infty}\frac{a_n}{n}
\le
\alpha.
\]

::: {.proof}
Step <1>4 holds for every $m\ge1$.
Taking the infimum over $m$ gives
\[
\limsup_{n\to\infty}\frac{a_n}{n}
\le
\inf_{m\ge1}\frac{a_m}{m}
=
\alpha.
\]
:::

<1>6. One has
\[
\boxed{
\lim_{n\to\infty}\frac{a_n}{n}
=
\inf_{n\ge1}\frac{a_n}{n}
}.
\]

::: {.proof}
By step <1>1,
\[
\liminf_{n\to\infty}\frac{a_n}{n}
\ge
\alpha.
\]
By step <1>5,
\[
\limsup_{n\to\infty}\frac{a_n}{n}
\le
\alpha.
\]
Since always
\[
\liminf\le\limsup,
\]
both must equal $\alpha$.
Thus the ordinary limit exists and equals the stated infimum.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is Fekete's lemma in the requested form.
:::
:::
