---
schema: qual/card@1
id: P-UCLARA17F-12
kind: problem
title: Continuous $h$ with $g\circ h$ holomorphic is holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 12. Let $f$, $g$, and $h$ be complex-valued functions defined on $\CC$ with
$$
f=g\circ h.
$$
Show that if $h$ is continuous, and both $f$ and $g$ are non-constant and holomorphic, then $h$ is holomorphic as well.
:::

::: {.solution}

Let
$$
Z\coloneqq\{w\in\CC:g'(w)=0\},
\qquad
B\coloneqq h^{-1}(Z).
$$

::: pf

::: {.pf-step #s1-1}

The set $Z$ is discrete in $\CC$.


::: pf-proof

Since $g$ is non-constant and entire, $g'$ is not identically zero. The zeros of a nonzero holomorphic function are isolated, so $Z$ is discrete.

:::

:::

::: {.pf-step #s1-2}

The function $h$ is holomorphic on $\CC\setminus B$.


::: pf-proof

Fix $z_0\notin B$. Then
$$
g'(h(z_0))\ne0.
$$
By the holomorphic inverse function theorem, there are neighborhoods $V$ of $h(z_0)$ and $U$ of $f(z_0)=g(h(z_0))$ such that
$$
g\restrict_V:V\longrightarrow U
$$
is biholomorphic. By continuity of $h$, after shrinking a neighborhood $W$ of $z_0$ one has $h(W)\subset V$. Hence on $W$,
$$
h=(g\restrict_V)^{-1}\circ f.
$$
The right-hand side is holomorphic, so $h$ is holomorphic at $z_0$.

:::

:::

::: {.pf-step #s1-3}

The set $B$ is discrete in $\CC$.


::: pf-proof

Suppose instead that $B$ has an accumulation point $z_\infty\in\CC$. Choose distinct points $z_n\in B$ with
$$
z_n\longrightarrow z_\infty.
$$
Then $h(z_n)\in Z$ for all $n$, while continuity of $h$ gives
$$
h(z_n)\longrightarrow h(z_\infty).
$$
Because $Z$ is the zero set of the continuous function $g'$, it is closed, so $h(z_\infty)\in Z$. Since $Z$ is discrete by step [](#s1-1){.pf-ref}, there is a neighborhood of $h(z_\infty)$ containing no other point of $Z$. Therefore
$$
h(z_n)=h(z_\infty)
$$
for all sufficiently large $n$. It follows that
$$
f(z_n)=g(h(z_n))=g(h(z_\infty))=f(z_\infty)
$$
for infinitely many distinct $z_n\to z_\infty$. The identity theorem then forces the non-constant entire function $f$ to be constant, a contradiction. Thus $B$ has no accumulation point.

:::

:::

::: {.pf-step #s1-4}

Every point of $B$ is a removable singularity for the holomorphic function $h\restrict_{\CC\setminus B}$.


::: pf-proof

Fix $b\in B$. By step [](#s1-3){.pf-ref}, choose $r>0$ such that
$$
B(b,r)\cap B=\{b\}.
$$
Step [](#s1-2){.pf-ref} shows that $h$ is holomorphic on the punctured disk $0<\abs{z-b}<r$. Since $h$ is continuous at $b$, it is bounded on some smaller disk around $b$. Riemann's removable singularity theorem therefore extends the punctured-disk holomorphic function across $b$. The extension agrees with the given value $h(b)$ by continuity, so the original function $h$ is holomorphic at $b$.

:::

:::

::: {.pf-step #s1-5}

$h$ is holomorphic on $\CC$.


::: pf-proof

Step [](#s1-2){.pf-ref} gives holomorphy on $\CC\setminus B$, and step [](#s1-4){.pf-ref} gives holomorphy at every point of $B$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the desired conclusion.

:::

:::

:::
