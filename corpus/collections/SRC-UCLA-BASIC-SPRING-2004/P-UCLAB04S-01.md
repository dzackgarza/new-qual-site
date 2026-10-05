---
schema: qual/card@1
id: P-UCLAB04S-01
kind: problem
title: Injecting binary sequences into the real line by decimal expansion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Let $S$ be the set of sequences
\[
a=(a_1,a_2,\ldots),
\qquad a_k\in\{0,1\}.
\]
Show that the map $\theta:S\to\mathbb R$ defined by
\[
\theta(a)=\frac{a_1}{10}+\frac{a_2}{10^2}+\cdots
\]
is injective.
Include an explanation of why the infinite series converges.

Hint: if $a\ne b$, you may suppose their first differing coordinate is $n$ and write
\[
a=(a_1,\ldots,a_{n-1},0,a_{n+1},\ldots),
\qquad
b=(a_1,\ldots,a_{n-1},1,b_{n+1},\ldots).
\]
:::

::: {.solution}
<1>1. For every
\[
a=(a_1,a_2,\ldots)\in S,
\]
the series
\[
\sum_{k=1}^{\infty}\frac{a_k}{10^k}
\]
converges.

::: {.proof}
Since
\[
a_k\in\{0,1\},
\]
one has
\[
0
\le
\frac{a_k}{10^k}
\le
\frac1{10^k}.
\]
The geometric series
\[
\sum_{k=1}^{\infty}\frac1{10^k}
\]
converges.
Therefore the comparison test gives convergence of
\[
\sum_{k=1}^{\infty}\frac{a_k}{10^k}.
\]
Thus $\theta(a)$ is well-defined.
:::

<1>2. Let
\[
a,b\in S
\]
with
\[
a\ne b.
\]
Let $n$ be the first index for which
\[
a_n\ne b_n.
\]
After interchanging $a$ and $b$ if necessary, assume
\[
a_n=0,
\qquad
b_n=1.
\]

::: {.proof}
Since $a\ne b$, the set of indices where they differ is nonempty.
The positive integers are well-ordered, so this set has a least element $n$.
At that coordinate the two binary digits are $0$ and $1$; exchange the names of the sequences if necessary.
:::

<1>3. One has
\[
\theta(b)-\theta(a)
=
\frac1{10^n}
+
\sum_{k=n+1}^{\infty}
\frac{b_k-a_k}{10^k}.
\]

::: {.proof}
For every
\[
k<n,
\]
the coordinates agree:
\[
a_k=b_k.
\]
At the first differing index,
\[
b_n-a_n=1.
\]
Subtract the two convergent series term by term.
:::

<1>4. The tail in step <1>3 satisfies
\[
\sum_{k=n+1}^{\infty}
\frac{b_k-a_k}{10^k}
\ge
-
\sum_{k=n+1}^{\infty}
\frac1{10^k}
=
-\frac1{9\cdot10^n}.
\]

::: {.proof}
For each $k$,
\[
b_k-a_k\ge-1.
\]
Hence
\[
\frac{b_k-a_k}{10^k}
\ge
-\frac1{10^k}.
\]
Summing over $k>n$ gives the first inequality.
The geometric-series sum is
\[
\sum_{k=n+1}^{\infty}\frac1{10^k}
=
\frac{10^{-(n+1)}}{1-1/10}
=
\frac1{9\cdot10^n}.
\]
:::

<1>5. Therefore
\[
\theta(b)-\theta(a)
\ge
\frac1{10^n}
-
\frac1{9\cdot10^n}
=
\frac8{9\cdot10^n}
>
0.
\]

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>6. Hence
\[
\boxed{\theta(a)\ne\theta(b)}
\]
whenever
\[
a\ne b.
\]

::: {.proof}
Step <1>5 shows that, after possibly interchanging the two sequences,
\[
\theta(b)>\theta(a).
\]
Thus distinct sequences have distinct images.
:::

<1>7. Therefore
\[
\boxed{\theta:S\to\mathbb R\text{ is injective}.}
\]

::: {.proof}
Step <1>6 is exactly the definition of injectivity.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 proves that $\theta$ is well-defined, and step <1>7 proves injectivity.
:::
:::
