---
schema: qual/card@1
id: P-ALGS25E
kind: problem
title: Localization vanishing at generators of the unit ideal implies $M = 0$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Localization
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $A$ is a unital commutative ring and $\langle a_1, \ldots, a_n\rangle = A$.
Suppose $M$ is an $A$-module and $S_{a_i} := \{1, a_i, a_i^2, \ldots\}$.
Suppose that $S_{a_i}^{-1}M = 0$ for all $i$.
Prove that $M = 0$.
(Hint.
For $x \in M$, consider the annihilator $\operatorname{ann}(x)$ of $x$.)
:::


::: {.solution}
<1>1. Fix \(x\in M\) and let
\[
I=\operatorname{ann}_A(x)=\{r\in A:rx=0\}.
\]
::: {.proof}
This is an ideal of \(A\). It suffices to prove \(1\in I\), because then \(x=1x=0\).
:::

<1>2. For each \(i\), there exists an integer \(N_i\ge0\) such that
\[
a_i^{N_i}x=0.
\]
::: {.proof}
The hypothesis \(S_{a_i}^{-1}M=0\) implies that \(x/1=0\) in the localization. By the definition of zero in a localized module, some element of \(S_{a_i}\), hence some power \(a_i^{N_i}\), annihilates \(x\).
:::

<1>3. Hence
\[
a_i^{N_i}\in I
\qquad(1\le i\le n).
\]
::: {.proof}
This is exactly the definition of the annihilator ideal \(I\).
:::

<1>4. Let
\[
J=(a_1^{N_1},\dots,a_n^{N_n}).
\]
Then \(J=A\).
::: {.proof}
By construction, each \(a_i\in\sqrt J\). Therefore
\[
(a_1,\dots,a_n)\subseteq\sqrt J.
\]
But \((a_1,\dots,a_n)=A\) by hypothesis, so \(\sqrt J=A\). Hence \(1\in\sqrt J\), which means \(1^r=1\in J\) for some positive integer \(r\). Thus \(J=A\).
:::

<1>5. One has \(J\subseteq I\), so \(I=A\).
::: {.proof}
Each generator \(a_i^{N_i}\) of \(J\) lies in \(I\) by <1>3. Hence \(J\subseteq I\). By <1>4, \(J=A\), so \(I=A\).
:::

<1>6. Therefore \(x=0\). Since \(x\in M\) was arbitrary, \(M=0\).
::: {.proof}
By <1>5, \(1\in I=\operatorname{ann}(x)\), so \(x=0\). Apply this to every element of \(M\).
:::
:::
