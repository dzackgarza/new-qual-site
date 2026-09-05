---
schema: qual/card@1
id: P-QICKA
kind: problem
title: Continuous images of compact sets are compact, while continuous images of closed
  sets need not be closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both alternatives against problem 1 of the official UGA Fall 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the open-cover proof for compact images and the explicit continuous closed-set counterexample f(x)=1/(1+x^2).
---

::: {.problem}
Let $f : X \to Y$ be a continuous function between topological spaces.

Let $A$ be a subset of $X$ and let $f(A)$ be its image in $Y$.

One of the following statements is true and one is false.
Decide which is which, prove the true statement, and provide a counterexample to the false statement:

1. If $A$ is closed then $f(A)$ is closed.

2. If $A$ is compact then $f(A)$ is compact.
:::

::: {.solution}
<1>1. The statement “if $A$ is compact, then $f(A)$ is compact” is true.
::: {.proof}
Let
\[
f(A)\subseteq\bigcup_{\lambda\in\Lambda}U_\lambda
\]
be an open cover of $f(A)$ by open subsets of $Y$.
Since $f$ is continuous, the sets
\[
f^{-1}(U_\lambda),
\qquad
\lambda\in\Lambda,
\]
are open in $X$, and they cover $A$.
Compactness of $A$ gives indices
\[
\lambda_1,\ldots,\lambda_m
\]
such that
\[
A\subseteq
f^{-1}(U_{\lambda_1})\cup\cdots\cup f^{-1}(U_{\lambda_m}).
\]
Applying $f$ shows
\[
f(A)\subseteq
U_{\lambda_1}\cup\cdots\cup U_{\lambda_m}.
\]
Thus every open cover of $f(A)$ has a finite subcover, so $f(A)$ is compact.
:::

<1>2. The statement “if $A$ is closed, then $f(A)$ is closed” is false.
::: {.proof}
Take
\[
X=Y=\RR,
\qquad
A=\RR,
\qquad
f(x)=\frac{1}{1+x^2}.
\]
The set $A$ is closed in $X$, and $f$ is continuous.
Its image is
\[
f(A)=(0,1].
\]
Indeed, $0<f(x)\le1$ for every $x$, the value $1$ occurs at $x=0$, and every $y\in(0,1]$ is attained by
\[
x=\sqrt{\frac1y-1}.
\]
But $(0,1]$ is not closed in $\RR$, since $0$ belongs to its closure but not to the set itself.
Hence a continuous map need not send closed sets to closed sets.
:::
:::
