---
schema: qual/card@1
id: P-UCLAB09F-06
kind: problem
title: Uniform continuity on a compact superellipse
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Consider
\[
f(x,y)=\sin^3(xy)+y^2|x|
\]
on
\[
S=\{(x,y)\in\mathbb R^2:x^{2010}+y^{2010}\le1\}.
\]
Define what it means for $f$ to be uniformly continuous on $S$, and prove that $f$ is uniformly continuous there.
You may use any applicable general theorem, provided you state it and justify its hypotheses.
:::

::: {.solution}
<1>1. Uniform continuity of $f$ on $S$ means that for every $\varepsilon>0$ there exists $\delta>0$ such that for all
\[
p,q\in S,
\]
if
\[
\|p-q\|_2<\delta,
\]
then
\[
|f(p)-f(q)|<\varepsilon.
\]

::: {.proof}
This is the definition of uniform continuity for a real-valued function on the metric space $S$ with the Euclidean metric restricted from $\mathbb R^2$.
:::

<1>2. The set
\[
S=
\{(x,y)\in\mathbb R^2:x^{2010}+y^{2010}\le1\}
\]
is closed.

::: {.proof}
The map
\[
h(x,y)=x^{2010}+y^{2010}
\]
is continuous, and
\[
S=h^{-1}((-\infty,1]).
\]
Since $(-\infty,1]$ is closed in $\mathbb R$, the inverse image $S$ is closed.
:::

<1>3. The set $S$ is bounded.

::: {.proof}
If $(x,y)\in S$, then
\[
x^{2010}\le1
\qquad\text{and}\qquad
y^{2010}\le1,
\]
because both terms are nonnegative. Hence
\[
|x|\le1
\qquad\text{and}\qquad
|y|\le1.
\]
Thus
\[
S\subseteq[-1,1]^2.
\]
:::

<1>4. The set $S$ is compact.

::: {.proof}
By steps <1>2--<1>3, $S$ is closed and bounded in $\mathbb R^2$. The Heine--Borel theorem therefore implies that $S$ is compact.
:::

<1>5. The function
\[
f(x,y)=\sin^3(xy)+y^2|x|
\]
is continuous on $\mathbb R^2$, hence on $S$.

::: {.proof}
The maps
\[
(x,y)\mapsto xy,
\qquad
t\mapsto\sin t,
\qquad
t\mapsto t^3,
\qquad
x\mapsto|x|,
\qquad
y\mapsto y^2
\]
are continuous. Products, compositions, and sums of continuous functions are continuous. Therefore both terms in $f$ are continuous, so $f$ is continuous.
:::

<1>6. The function $f$ is uniformly continuous on $S$.

::: {.proof}
The Heine--Cantor theorem states that every continuous real-valued function on a compact metric space is uniformly continuous. Step <1>4 shows that $S$ is compact, and step <1>5 shows that $f$ is continuous on $S$. Therefore
\[
\boxed{f\text{ is uniformly continuous on }S}.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 gives the definition, and step <1>6 proves that $f$ satisfies it.
:::
:::
