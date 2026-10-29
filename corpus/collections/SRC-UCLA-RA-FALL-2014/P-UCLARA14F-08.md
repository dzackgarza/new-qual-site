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
Let $f : \CC \to \CC$ be an entire function. Show that
$$
|f(z)| \leq C e^{a|z|}, \quad z \in \CC,
$$
for some constants $C$ and $a$ if and only if we have
$$
|f^{(n)}(0)| \leq M^{n+1}, \quad n = 0, 1, \ldots,
$$
for some constant $M$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume first that there are constants $C>0$ and $a\ge0$ such that
$$
|f(z)|\le Ce^{a|z|}
\qquad(z\in\CC).
$$
Then for every $R>0$ and every $n\ge0$,
$$
|f^{(n)}(0)|
\le
\frac{n!}{R^n}Ce^{aR}.
$$


::: pf-proof

On the circle $|z|=R$,
$$
\max_{|z|=R}|f(z)|
\le
Ce^{aR}.
$$
Cauchy's derivative estimate therefore gives
$$
|f^{(n)}(0)|
\le
\frac{n!}{R^n}
\max_{|z|=R}|f(z)|
\le
\frac{n!}{R^n}Ce^{aR}.
$$

:::

:::

::: {.pf-step #s1-2}

If $a=0$, then $f$ is constant.


::: pf-proof

The growth assumption becomes
$$
|f(z)|\le C
$$
on all of $\CC$. Liouville's theorem implies that $f$ is constant.
Hence
$$
f^{(n)}(0)=0
$$
for every $n\ge1$.

:::

:::

::: {.pf-step #s1-3}

Suppose $a>0$. For every $n\ge1$,
$$
|f^{(n)}(0)|
\le
C(ae)^n.
$$


::: pf-proof

In step [](#s1-1){.pf-ref} choose
$$
R=\frac na.
$$
Then
$$
|f^{(n)}(0)|
\le
C\,n!\,
\frac{e^n a^n}{n^n}.
$$
Since
$$
n!\le n^n,
$$
this yields
$$
|f^{(n)}(0)|
\le
C(ae)^n.
$$

:::

:::

::: {.pf-step #s1-4}

Under the exponential-growth hypothesis, there exists $M>0$ such that
$$
\boxed{
|f^{(n)}(0)|
\le
M^{n+1}
\qquad(n\ge0)}.
$$


::: pf-proof

If $a=0$, step [](#s1-2){.pf-ref} applies. Choose
$$
M\ge\max\{1,C\}.
$$
Then
$$
|f(0)|\le C\le M
$$
and every higher derivative is zero.

If $a>0$, choose
$$
M\ge\max\{1,C,ae\}.
$$
For $n=0$,
$$
|f(0)|\le C\le M.
$$
For $n\ge1$, step [](#s1-3){.pf-ref} gives
$$
|f^{(n)}(0)|
\le
C(ae)^n
\le
M^{n+1}.
$$

:::

:::

::: {.pf-step #s1-5}

Conversely, assume there is $M>0$ such that
$$
|f^{(n)}(0)|
\le
M^{n+1}
\qquad(n\ge0).
$$
Then
$$
\boxed{
|f(z)|
\le
M e^{M|z|}
\qquad(z\in\CC)}.
$$


::: pf-proof

Since $f$ is entire, its Taylor series at $0$ converges everywhere:
$$
f(z)
=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(0)}{n!}z^n.
$$
Therefore
$$
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
$$
Thus the required exponential-growth estimate holds with
$$
C=M,
\qquad
a=M.
$$

:::

:::

::: {.pf-step #s1-6}

Hence the two conditions are equivalent.


::: pf-proof

Step [](#s1-4){.pf-ref} proves the forward implication and step [](#s1-5){.pf-ref} proves the reverse
implication.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required equivalence.

:::

:::

:::
