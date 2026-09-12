---
schema: qual/card@1
id: P-JHUFA01RAE
kind: problem
title: '$L^p$ inclusion relationships'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $1\le p<q<\infty$. Determine which statements are true and which are false:

(i) $L^p(\mathbb R)\subset L^q(\mathbb R)$;

(ii) $L^q(\mathbb R)\subset L^p(\mathbb R)$;

(iii) $L^p([0,1])\subset L^q([0,1])$;

(iv) $L^q([0,1])\subset L^p([0,1])$;

(v) $\ell^p(\mathbb Z)\subset\ell^q(\mathbb Z)$;

(vi) $\ell^q(\mathbb Z)\subset\ell^p(\mathbb Z)$.

Give counterexamples for the false statements. Also determine all $s\ge1$ for which
\[
L^p(\mathbb R)\cap L^q(\mathbb R)\subset L^s(\mathbb R).
\]
:::

::: {.solution}
The answers are
\[
\begin{array}{c|cccccc}
&\text{(i)}&\text{(ii)}&\text{(iii)}&\text{(iv)}&\text{(v)}&\text{(vi)}\\ \hline
&\text{false}&\text{false}&\text{false}&\text{true}&\text{true}&\text{false}.
\end{array}
\]
Moreover,
\[
L^p(\mathbb R)\cap L^q(\mathbb R)\subset L^s(\mathbb R)
\quad\Longleftrightarrow\quad
p\le s\le q.
\]

<1>1. Counterexamples for (i), (ii), and (iii).
::: {.proof}
Choose $a$ with
\[
\frac1q\le a<\frac1p.
\]
Then
\[
f(x)=x^{-a}\mathbf1_{(0,1)}(x)
\]
belongs to $L^p$ but not $L^q$, because
\[
\int_0^1x^{-ar}\,dx<\infty
\quad\Longleftrightarrow\quad ar<1.
\]
This disproves both (i) and (iii).

For (ii), choose $b$ with
\[
\frac1q<b\le\frac1p
\]
and set
\[
g(x)=x^{-b}\mathbf1_{[1,\infty)}(x).
\]
Then $g\in L^q(\mathbb R)$ but $g\notin L^p(\mathbb R)$, because
\[
\int_1^\infty x^{-br}\,dx<\infty
\quad\Longleftrightarrow\quad br>1.
\]
:::

<1>2. Statements (iv) and (v) are true, while (vi) is false.
::: {.proof}
Since $[0,1]$ has finite measure, Hölder's inequality gives
\[
\|f\|_p\le \|f\|_q
\]
for $f\in L^q([0,1])$, proving (iv).

For sequences, if $a=(a_n)\in\ell^p$, then $a_n\to0$, so all but finitely many terms satisfy $|a_n|\le1$. Hence for all sufficiently large $n$,
\[
|a_n|^q\le|a_n|^p,
\]
which proves $a\in\ell^q$ and therefore (v).

For (vi), choose $c$ with
\[
\frac1q<c\le\frac1p
\]
and set $a_n=n^{-c}$ for $n\ge1$ and $a_n=0$ for $n\le0$. Then $a\in\ell^q$ but $a\notin\ell^p$.
:::

<1>3. Determine the exponents $s$ in part (vii).
::: {.proof}
If $p\le s\le q$, choose $\theta\in[0,1]$ such that
\[
\frac1s=\frac\theta p+\frac{1-\theta}{q}.
\]
For $f\in L^p\cap L^q$, Hölder interpolation gives
\[
\|f\|_s\le \|f\|_p^\theta\|f\|_q^{1-\theta},
\]
so $f\in L^s$.

Now suppose $1\le s<p$. Choose $b$ with
\[
\frac1p<b\le\frac1s.
\]
Then
\[
f(x)=x^{-b}\mathbf1_{[1,\infty)}(x)
\]
belongs to both $L^p$ and $L^q$ but not to $L^s$.

Finally suppose $s>q$. Choose $a$ with
\[
\frac1s\le a<\frac1q.
\]
Then
\[
g(x)=x^{-a}\mathbf1_{(0,1)}(x)
\]
belongs to both $L^p$ and $L^q$ but not to $L^s$.

Thus the inclusion holds exactly for
\[
\boxed{p\le s\le q}.
\]
:::
:::
