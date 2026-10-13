---
schema: qual/card@1
id: P-UGASAMP-02
kind: problem
title: Continuity at a point and continuity of $x^2$ at $2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $a\in\mathbb R$ and let $I$ be an open interval containing $a$. For a function $f:I\to\mathbb R$, give the definition of continuity at $a$. Prove that
\[
f(x)=x^2
\]
is continuous at $a=2$.
:::

::: {.solution}
<1>1. A function \(f:I\to\mathbb R\) is continuous at \(a\in I\) if for every \(\varepsilon>0\) there exists \(\delta>0\) such that, for every \(x\in I\),
\[
|x-a|<\delta
\quad\Longrightarrow\quad
|f(x)-f(a)|<\varepsilon.
\]

::: {.proof}
This is the \(\varepsilon\)--\(\delta\) definition of continuity at a point.
:::

<1>2. If \(|x-2|<1\), then
\[
|x+2|<5.
\]

::: {.proof}
The inequality \(|x-2|<1\) implies
\[
1<x<3.
\]
Hence
\[
3<x+2<5,
\]
so \(|x+2|<5\).
:::

<1>3. Given \(\varepsilon>0\), set
\[
\delta=\min\left\{1,\frac{\varepsilon}{5}\right\}.
\]
If \(|x-2|<\delta\), then
\[
|x^2-4|<\varepsilon.
\]

::: {.proof}
Since \(\delta\le1\), the hypothesis \(|x-2|<\delta\) implies \(|x-2|<1\). By step <1>2,
\[
|x+2|<5.
\]
Therefore
\[
|x^2-4|
=
|x-2|\,|x+2|
<
5|x-2|
<
5\delta
\le
\varepsilon.
\]
:::

<1>4. The function \(f(x)=x^2\) is continuous at \(2\).

::: {.proof}
Step <1>3 verifies the definition in step <1>1 with \(a=2\) and \(f(2)=4\). Thus
\[
\boxed{f(x)=x^2\text{ is continuous at }2.}
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 gives the requested definition, and step <1>4 proves the required continuity.
:::
:::
