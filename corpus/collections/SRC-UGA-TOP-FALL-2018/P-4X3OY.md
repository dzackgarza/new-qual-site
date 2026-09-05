---
schema: qual/card@1
id: P-4X3OY
kind: problem
title: Positivity of $f(x,0)$ persists for small $|t|$ when $X$ is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both the compactness assertion and requested noncompact example against problem 2 of the official UGA Fall 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the finite-subcover uniformization and the explicit noncompact counterexample on R.
---

::: {.problem}
Let $X$ be a compact space and let
\[
f:X\times\RR\longrightarrow\RR
\]
be a continuous function such that $f(x,0)>0$ for all $x\in X$.
Prove that there is $\varepsilon>0$ such that
\[
f(x,t)>0
\]
whenever $|t|<\varepsilon$.
Moreover, give an example showing that this conclusion may not hold if $X$ is not assumed compact.
:::

::: {.solution}
<1>1. For every $x\in X$, there are an open neighborhood $U_x\subseteq X$ of $x$ and a number $\varepsilon_x>0$ such that
\[
f(y,t)>0
\qquad
\text{for all }y\in U_x\text{ and }|t|<\varepsilon_x.
\]
::: {.proof}
Since $f(x,0)>0$ and $(0,\infty)$ is open in $\RR$, continuity gives an open neighborhood
\[
W_x\subseteq X\times\RR
\]
of $(x,0)$ such that
\[
f(W_x)\subseteq(0,\infty).
\]
By the definition of the product topology, there are an open neighborhood $U_x$ of $x$ and an open interval $(-\varepsilon_x,\varepsilon_x)$ about $0$ with
\[
U_x\times(-\varepsilon_x,\varepsilon_x)\subseteq W_x.
\]
The claimed positivity follows.
:::

<1>2. There is one $\varepsilon>0$ that works simultaneously for every $x\in X$.
::: {.proof}
The sets $U_x$ from <1>1 form an open cover of the compact space $X$.
Choose a finite subcover
\[
X=U_{x_1}\cup\cdots\cup U_{x_m}.
\]
Set
\[
\varepsilon=\min_{1\le j\le m}\varepsilon_{x_j}>0.
\]
If $x\in X$ and $|t|<\varepsilon$, choose $j$ with $x\in U_{x_j}$.
Then
\[
|t|<\varepsilon\le\varepsilon_{x_j},
\]
so <1>1 gives $f(x,t)>0$.
:::

<1>3. Compactness cannot be omitted.
::: {.proof}
Take the noncompact space
\[
X=\RR
\]
and define
\[
f(x,t)=1-x^2t^2.
\]
This function is continuous and satisfies
\[
f(x,0)=1>0
\qquad
\text{for every }x\in\RR.
\]
However, no uniform $\varepsilon>0$ works.
Indeed, given $\varepsilon>0$, set
\[
t=\frac{\varepsilon}{2}
\]
and choose $x>2/\varepsilon$.
Then $|t|<\varepsilon$ but
\[
x^2t^2>1,
\qquad
f(x,t)<0.
\]
Thus the conclusion can fail when $X$ is noncompact.
:::
:::
