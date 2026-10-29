---
schema: qual/card@1
id: P-UCLAB15F-11
kind: problem
title: Square roots of a nilpotent operator in dimensions six and twelve
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
Let $T:V\to V$ be linear with
\[
T^{18}=0,\qquad T^5\ne0.
\]
Suppose $V\cong\RR^6$.
Prove that there is no linear operator $S:V\to V$ such that $S^2=T$.

Does the answer change if $V\cong\RR^{12}$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
\[
T^{18}=0,
\]
then $T$ is nilpotent.


::: pf-proof

This is the definition of nilpotence: some positive power of $T$ is zero.

:::

:::

::: {.pf-step #s1-2}

If
\[
\dim V=6,
\]
then
\[
T^6=0.
\]


::: pf-proof

Since $T$ is nilpotent by step [](#s1-1){.pf-ref}, every eigenvalue of $T$ is $0$.
Hence the characteristic polynomial of $T$ on a six-dimensional space is
\[
\chi_T(X)=X^6.
\]
By the Cayley--Hamilton theorem,
\[
\chi_T(T)=T^6=0.
\]

:::

:::

::: {.pf-step #s1-3}

Suppose, for contradiction, that there exists
\[
S:V\to V
\]
with
\[
S^2=T.
\]
Then $S$ is nilpotent.


::: pf-proof

Using
\[
T^{18}=0,
\]
one gets
\[
S^{36}
=(S^2)^{18}
=T^{18}
=0.
\]
Thus $S$ is nilpotent.

:::

:::

::: {.pf-step #s1-4}

If
\[
\dim V=6,
\]
then
\[
S^6=0.
\]


::: pf-proof

By step [](#s1-3){.pf-ref}, $S$ is nilpotent.
As in step [](#s1-2){.pf-ref}, its characteristic polynomial is
\[
X^6.
\]
Cayley--Hamilton gives
\[
S^6=0.
\]

:::

:::

::: {.pf-step #s1-5}

Under the hypothesis
\[
S^2=T,
\]
one has
\[
T^3=S^6.
\]


::: pf-proof

\[
T^3
=(S^2)^3
=S^6.
\]

:::

:::

::: {.pf-step #s1-6}

No such square root $S$ exists when
\[
\dim V=6.
\]


::: pf-proof

If such $S$ existed, steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} would give
\[
T^3=S^6=0.
\]
Then
\[
T^5=T^2T^3=0,
\]
contradicting the hypothesis
\[
T^5\ne0.
\]
Therefore no such $S$ exists.

:::

:::

::: {.pf-step #s1-7}

In dimension $12$, the answer changes: such examples do exist.


::: pf-proof

Let
\[
V=\RR^{12}
\]
with basis
\[
e_1,\ldots,e_{12}.
\]
Define $S$ by
\[
Se_1=0,
\qquad
Se_j=e_{j-1}
\quad
(2\le j\le12).
\]
Then
\[
S^{12}=0
\]
but
\[
S^{10}e_{12}=e_2\ne0.
\]
Set
\[
T=S^2.
\]
Then
\[
T^5
=(S^2)^5
=S^{10}
\ne0.
\]
Also
\[
T^{18}
=(S^2)^{18}
=S^{36}
=0
\]
because already $S^{12}=0$.
Thus $T$ satisfies the hypotheses and has the square root $S$.

:::

:::

::: {.pf-step #s1-8}

Therefore
\[
\boxed{
\text{no square root exists in dimension }6,
\text{ but one may exist in dimension }12.
}
\]


::: pf-proof

Step [](#s1-6){.pf-ref} proves impossibility in dimension $6$, and step [](#s1-7){.pf-ref} gives an explicit dimension-$12$ example.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} answers both parts.

:::

:::

:::
