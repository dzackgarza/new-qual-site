---
schema: qual/card@1
id: P-UCLARA14F-02
kind: problem
title: An $L^1$ function whose translates do not converge almost everywhere
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 2 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Construct an $f \in L^1(\mathbb{R})$ so that $f(x+y)$ does *not* converge almost everywhere to $f(x)$ as $y \to 0$. Prove that your $f$ has this property.
:::

::: {.solution}
<1>1. Let
\[
K\subset[0,1]
\]
be a fat Cantor set, so that $K$ is closed, has positive Lebesgue measure,
and has empty interior. Define
\[
\boxed{f=\chi_K}.
\]

::: {.proof}
Fat Cantor sets with these properties exist. Since $K$ is closed, it is
Borel measurable, so its indicator is measurable.
:::

<1>2. One has
\[
f\in L^1(\mathbb R).
\]

::: {.proof}
Because $K\subset[0,1]$,
\[
\int_{\mathbb R}|f(x)|\,dx
=
\int_{\mathbb R}\chi_K(x)\,dx
=
m(K)
\le1.
\]
Thus $f$ is integrable.
:::

<1>3. Every point $x\in K$ is a boundary point of $K$.

::: {.proof}
Since $K$ is closed,
\[
\overline K=K.
\]
Since $K$ has empty interior,
\[
\partial K
=
\overline K\setminus\operatorname{int}(K)
=K.
\]
:::

<1>4. For every $x\in K$, there is a sequence
\[
y_j\to0
\]
such that
\[
x+y_j\notin K
\qquad\text{for every }j.
\]

::: {.proof}
By step <1>3, every neighborhood of $x$ meets
\[
\mathbb R\setminus K.
\]
For each $j\ge1$, choose
\[
u_j\in
\left(x-\frac1j,x+\frac1j\right)
\setminus K.
\]
Set
\[
y_j=u_j-x.
\]
Then
\[
|y_j|<\frac1j,
\]
so $y_j\to0$, while $x+y_j=u_j\notin K$.
:::

<1>5. For every $x\in K$,
\[
f(x+y)
\]
does not converge to $f(x)$ as $y\to0$.

::: {.proof}
For $x\in K$,
\[
f(x)=1.
\]
For the sequence from step <1>4,
\[
f(x+y_j)
=
\chi_K(u_j)
=0
\]
for every $j$. Hence along the sequence $y_j\to0$,
\[
f(x+y_j)\to0\ne1=f(x).
\]
Therefore the limit as $y\to0$ cannot equal $f(x)$.
:::

<1>6. The failure in step <1>5 occurs on a set of positive measure.

::: {.proof}
The exceptional set contains all of $K$, and by construction
\[
m(K)>0.
\]
Thus convergence to $f(x)$ fails on a positive-measure set and therefore
does not hold almost everywhere.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 construct an $L^1$ function, while steps <1>5 and <1>6
prove the required failure of almost-everywhere translation convergence.
:::
:::
