---
schema: qual/card@1
id: P-UGAP13F-01
kind: problem
title: Negate uniform continuity and give a continuous non-uniformly-continuous example
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
A function $f:\RR\to\RR$ is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
\]

(a) Give a definition of what it means for $f$ not to be uniformly continuous.

(b) Give an example, with brief explanation, of a function $f:\RR\to\RR$ that is continuous but not uniformly continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The negation of uniform continuity is:
\[
\boxed{
\exists\varepsilon_0>0
\text{ such that }
\forall\delta>0
\text{ there exist }x,y\in\RR
\text{ with }
|x-y|<\delta
\text{ and }
|f(x)-f(y)|\ge\varepsilon_0.
}
\]


::: pf-proof

Uniform continuity is the statement
\[
\forall\varepsilon>0+\exists\delta>0+\forall x,y\in\RR,
\quad
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon.
\]

Negating the quantifiers gives
\[
\exists\varepsilon_0>0+\forall\delta>0+\exists x,y\in\RR
\]
such that the implication fails.
Failure of
\[
|x-y|<\delta
\Longrightarrow
|f(x)-f(y)|<\varepsilon_0
\]
means precisely
\[
|x-y|<\delta
\]
and
\[
|f(x)-f(y)|\ge\varepsilon_0.
\]

:::

:::

::: {.pf-step #s1-2}

Take
\[
\boxed{
f(x)=x^2.
}
\]
Then $f$ is continuous on $\RR$.


::: pf-proof

It is a polynomial.

:::

:::

::: {.pf-step #s1-3}

The function
\[
f(x)=x^2
\]
is not uniformly continuous.


::: pf-proof

Take
\[
\varepsilon_0=1.
\]
Let
\[
\delta>0
\]
be arbitrary, and set
\[
h
\coloneqq
\frac\delta2.
\]
Choose
\[
x>
\frac1{2h}.
\]
Set
\[
y=x+h.
\]
Then
\[
|x-y|
=
h
=
\frac\delta2
<
\delta.
\]

But
\[
\begin{aligned}
|f(y)-f(x)|
&=
(x+h)^2-x^2\\
&=
2xh+h^2\\
&>
1.
\end{aligned}
\]
Thus the fixed number
\[
\varepsilon_0=1
\]
defeats every choice of $\delta$.
By step [](#s1-1){.pf-ref}, $f$ is not uniformly continuous.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} answer part (b).

:::

:::

:::
