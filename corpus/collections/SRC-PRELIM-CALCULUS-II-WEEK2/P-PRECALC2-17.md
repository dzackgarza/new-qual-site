---
schema: qual/card@1
id: P-PRECALC2-17
kind: problem
title: Counterexamples for the alternating series test and for $\sum b_n$ versus $\sum b_n^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find a sequence $\left( a _ { n } \right)$ such that $a _ { n } > 0$ for all $n \in \NN$ and $a _ { n } \to 0$ but

$$
\sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } a _ { n } \mathrm { d i v e r g e s } .
$$

[Note: this shows that the assumption that $a _ { n }$ is decreasing is necessary in the Alternating Series Test.] Find a sequence $\left( b _ { n } \right)$ such that

$$
\sum _ { n = 1 } ^ { \infty } b _ { n } \mathrm { c o n v e r g e s ~ w h i l e } \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 } \mathrm { d i v e r g e s } .
$$

Is it possible to choose $\left( b _ { n } \right)$ so that $\sum _ { n = 1 } ^ { \infty } b _ { n }$ converges absolutely while $\textstyle \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 }$ diverges?
:::

::: {.solution}

## A nonmonotone alternating-series counterexample

For \(k\ge1\), define
\[
\boxed{
a_{2k}=\frac1k,
\qquad
a_{2k-1}=\frac1{2k}}.
\]

::: pf

::: pf-step

Every \(a_n\) is positive.


::: pf-proof

Both formulas defining \(a_{2k}\) and \(a_{2k-1}\) are positive for
\(k\ge1\).

:::

:::

::: pf-step

One has
\[
\boxed{a_n\to0}.
\]


::: pf-proof

Along the even subsequence,
\[
a_{2k}=\frac1k\to0.
\]
Along the odd subsequence,
\[
a_{2k-1}=\frac1{2k}\to0.
\]
Since both subsequences tend to \(0\), the whole sequence does.

:::

:::

::: {.pf-step #s1-3}

The contribution of the \(k\)th odd-even pair to the alternating
series is
\[
\boxed{
(-1)^{2k-1}a_{2k-1}
+
(-1)^{2k}a_{2k}
=
\frac1{2k}}.
\]


::: pf-proof

Since
\[
(-1)^{2k-1}=-1
\qquad\text{and}\qquad
(-1)^{2k}=1,
\]
one has
\[
-\frac1{2k}+\frac1k
=
\frac1{2k}.
\]

:::

:::

::: pf-step

The even partial sums satisfy
\[
S_{2N}
=
\sum_{k=1}^{N}\frac1{2k}.
\]


::: pf-proof

Group the first \(2N\) terms into the \(N\) consecutive pairs computed in
step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
S_{2N}\to+\infty.
\]


::: pf-proof

\[
S_{2N}
=
\frac12
\sum_{k=1}^{N}\frac1k,
\]
and the harmonic partial sums diverge to \(+\infty\).

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{
\sum_{n=1}^{\infty}
(-1)^na_n
\text{ diverges}}.
\]


::: pf-proof

A convergent series must have all subsequences of its partial sums converge
to the same finite limit. Step [](#s1-5){.pf-ref} shows the even partial sums diverge.

:::

:::

::: {.pf-step #s1-7}

The sequence
\[
\frac1{\sqrt n}
\]
is positive, decreasing, and tends to \(0\).


::: pf-proof

The function
\[
x\mapsto x^{-1/2}
\]
is positive and decreasing on \((0,\infty)\), and
\[
n^{-1/2}\to0.
\]

:::

:::

::: {.pf-step #s1-8}

Therefore
\[
\boxed{
\sum_{n=1}^{\infty}b_n
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{\sqrt n}
\text{ converges}}.
\]


::: pf-proof

Apply the alternating series test using step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

But
\[
\boxed{
b_n^2=\frac1n}.
\]


::: pf-proof

\[
\left(
\frac{(-1)^n}{\sqrt n}
\right)^2
=
\frac1n.
\]

:::

:::

::: {.pf-step #s1-10}

Hence
\[
\boxed{
\sum_{n=1}^{\infty}b_n^2
=
\sum_{n=1}^{\infty}\frac1n
\text{ diverges}}.
\]


::: pf-proof

Use step [](#s1-9){.pf-ref} and divergence of the harmonic series.

:::

:::

::: pf-step

Suppose
\[
\sum_{n=1}^{\infty}|b_n|
\]
converges. Then
\[
\boxed{b_n\to0}.
\]


::: pf-proof

A necessary condition for convergence of any series is that its terms tend
to zero. Apply this to the nonnegative series \(\sum|b_n|\).

:::

:::

::: pf-step

Hence there exists \(N\) such that
\[
\boxed{|b_n|\le1}
\qquad(n\ge N).
\]


::: pf-proof

Since \(b_n\to0\), eventually
\[
|b_n|<1.
\]

:::

:::

::: {.pf-step #s1-13}

For \(n\ge N\),
\[
\boxed{
b_n^2
=
|b_n|^2
\le
|b_n|}.
\]


::: pf-proof

If \(0\le x\le1\), then
\[
x^2\le x.
\]
Apply this with \(x=|b_n|\).

:::

:::

::: {.pf-step #s1-14}

Therefore
\[
\sum_{n=N}^{\infty}b_n^2
\]
converges.


::: pf-proof

By step [](#s1-13){.pf-ref}, the nonnegative series is termwise bounded by the convergent
tail
\[
\sum_{n=N}^{\infty}|b_n|.
\]
Apply the comparison test.

:::

:::

::: {.pf-step #s1-15}

Thus
\[
\boxed{
\sum |b_n|<\infty
\quad\Longrightarrow\quad
\sum b_n^2<\infty}.
\]


::: pf-proof

Step [](#s1-14){.pf-ref} gives convergence of the tail, and finitely many initial terms do
not affect convergence.

:::

:::

::: {.pf-step #s1-16}

Consequently, it is impossible to choose \((b_n)\) so that
\[
\sum b_n
\]
converges absolutely while
\[
\sum b_n^2
\]
diverges.


::: pf-proof

Such a sequence would contradict step [](#s1-15){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the first requested sequence, steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} give the
second, and step [](#s1-16){.pf-ref} answers the final question.

:::

:::

:::
