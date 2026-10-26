---
schema: qual/card@1
id: P-UCLAB03F-01
kind: problem
title: Uncountability of the real numbers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Prove that $\mathbb R$ is uncountable.

If you use the Baire category theorem, you must prove it.
:::

Let
\[
\Sigma=\{0,1\}^{\mathbb N}
\]
be the set of all infinite binary sequences.

::: pf

::: pf-step

There is no surjection
\[
\mathbb N\to\Sigma.
\]


::: pf-proof

Suppose
\[
s^{(1)},s^{(2)},\ldots
\]
were an enumeration of all binary sequences, where
\[
s^{(n)}=(s^{(n)}_1,s^{(n)}_2,\ldots).
\]
Define a binary sequence $t=(t_1,t_2,\ldots)$ by
\[
t_n=1-s^{(n)}_n.
\]
Then $t$ differs from $s^{(n)}$ in its $n$th coordinate for every $n$. Hence $t$ is not in the enumeration, contradicting surjectivity.

:::

:::

::: pf-step

The map
\[
\Phi:\Sigma\to[0,1]
\]
defined by
\[
\Phi((s_n))=\sum_{n=1}^{\infty}\frac{2s_n}{3^n}
\]
is injective.


::: pf-proof

The series converges absolutely because
\[
0\le
\sum_{n=1}^{\infty}\frac{2s_n}{3^n}
\le
\sum_{n=1}^{\infty}\frac2{3^n}
=1.
\]

Suppose $s=(s_n)$ and $t=(t_n)$ are distinct. Let $m$ be the first index for which $s_m\ne t_m$. After exchanging $s$ and $t$ if necessary, assume $s_m=1$ and $t_m=0$. Then
\[
\begin{aligned}
\Phi(s)-\Phi(t)
&=
\frac2{3^m}
+
\sum_{n>m}\frac{2(s_n-t_n)}{3^n}\\
&\ge
\frac2{3^m}
-
\sum_{n>m}\frac2{3^n}\\
&=
\frac2{3^m}-\frac1{3^m}
=
\frac1{3^m}>0.
\end{aligned}
\]
Thus $\Phi(s)\ne\Phi(t)$, so $\Phi$ is injective.

:::

:::

::: pf-step

The interval $[0,1]$ is uncountable.


::: pf-proof

If $[0,1]$ were countable, then composing an enumeration of $[0,1]$ with the inverse relation supplied by the injection in step <1>2 would imply that $\Sigma$ is countable. More directly, every subset of a countable set is countable, while step <1>2 identifies $\Sigma$ with the subset $\Phi(\Sigma)\subseteq[0,1]$. This contradicts step <1>1.

:::

:::

::: pf-step

The real numbers are uncountable.


::: pf-proof

Since
\[
[0,1]\subseteq\mathbb R,
\]
countability of $\mathbb R$ would imply countability of $[0,1]$, contradicting step <1>3. Therefore
\[
\boxed{\mathbb R\text{ is uncountable}.}
\]

:::

:::

::: pf-qed

Step <1>4 is the required conclusion and does not use the Baire category theorem.

:::

:::
