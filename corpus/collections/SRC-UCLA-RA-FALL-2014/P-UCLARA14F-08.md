---
schema: qual/card@1
id: P-UCLARA14F-08
kind: problem
title: Entire functions of exponential type and growth of derivatives at 0
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 8 on pages 1-2 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function. Show that
\[
|f(z)| \leq C e^{a|z|}, \quad z \in \mathbb{C},
\]
for some constants $C$ and $a$ if and only if we have
\[
|f^{(n)}(0)| \leq M^{n+1}, \quad n = 0, 1, \ldots,
\]
for some constant $M$.
:::

::: {.solution}
<1>1. Assume first that there are constants $C>0$ and $a\ge0$ such that
\[
|f(z)|\le Ce^{a|z|}
\qquad(z\in\mathbb C).
\]
Then for every $R>0$ and every $n\ge0$,
\[
|f^{(n)}(0)|
\le
\frac{n!}{R^n}Ce^{aR}.
\]

::: {.proof}
On the circle $|z|=R$,
\[
\max_{|z|=R}|f(z)|
\le
Ce^{aR}.
\]
Cauchy's derivative estimate therefore gives
\[
|f^{(n)}(0)|
\le
\frac{n!}{R^n}
\max_{|z|=R}|f(z)|
\le
\frac{n!}{R^n}Ce^{aR}.
\]
:::

<1>2. If $a=0$, then $f$ is constant.

::: {.proof}
The growth assumption becomes
\[
|f(z)|\le C
\]
on all of $\mathbb C$. Liouville's theorem implies that $f$ is constant.
Hence
\[
f^{(n)}(0)=0
\]
for every $n\ge1$.
:::

<1>3. Suppose $a>0$. For every $n\ge1$,
\[
|f^{(n)}(0)|
\le
C(ae)^n.
\]

::: {.proof}
In step <1>1 choose
\[
R=\frac na.
\]
Then
\[
|f^{(n)}(0)|
\le
C\,n!\,
\frac{e^n a^n}{n^n}.
\]
Since
\[
n!\le n^n,
\]
this yields
\[
|f^{(n)}(0)|
\le
C(ae)^n.
\]
:::

<1>4. Under the exponential-growth hypothesis, there exists $M>0$ such that
\[
\boxed{
|f^{(n)}(0)|
\le
M^{n+1}
\qquad(n\ge0)}.
\]

::: {.proof}
If $a=0$, step <1>2 applies. Choose
\[
M\ge\max\{1,C\}.
\]
Then
\[
|f(0)|\le C\le M
\]
and every higher derivative is zero.

If $a>0$, choose
\[
M\ge\max\{1,C,ae\}.
\]
For $n=0$,
\[
|f(0)|\le C\le M.
\]
For $n\ge1$, step <1>3 gives
\[
|f^{(n)}(0)|
\le
C(ae)^n
\le
M^{n+1}.
\]
:::

<1>5. Conversely, assume there is $M>0$ such that
\[
|f^{(n)}(0)|
\le
M^{n+1}
\qquad(n\ge0).
\]
Then
\[
\boxed{
|f(z)|
\le
M e^{M|z|}
\qquad(z\in\mathbb C)}.
\]

::: {.proof}
Since $f$ is entire, its Taylor series at $0$ converges everywhere:
\[
f(z)
=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(0)}{n!}z^n.
\]
Therefore
\[
\begin{aligned}
|f(z)|
&\le
\sum_{n=0}^{\infty}
\frac{|f^{(n)}(0)|}{n!}|z|^n\\
&\le
\sum_{n=0}^{\infty}
\frac{M^{n+1}|z|^n}{n!}\\
&=
M
\sum_{n=0}^{\infty}
\frac{(M|z|)^n}{n!}\\
&=
Me^{M|z|}.
\end{aligned}
\]
Thus the required exponential-growth estimate holds with
\[
C=M,
\qquad
a=M.
\]
:::

<1>6. Hence the two conditions are equivalent.

::: {.proof}
Step <1>4 proves the forward implication and step <1>5 proves the reverse
implication.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required equivalence.
:::
:::
