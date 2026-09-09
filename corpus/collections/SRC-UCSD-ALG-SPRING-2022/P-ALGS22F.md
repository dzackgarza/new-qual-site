---
schema: qual/card@1
id: P-ALGS22F
kind: problem
title: "Powers of generators of the unit ideal and detection of zero modules by localization"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
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
Let $A$ be a commutative ring and let $f_1, \ldots, f_r \in A$ be elements which generate the unit ideal.

(a) Show that for any non-negative integers $p_1, \ldots, p_r$, the powers $f_1^{p_1}, \ldots, f_r^{p_r}$ also generate the unit ideal.

(b) Let $M$ be an $A$-module.
Show that $M = 0$ if and only if $M_{f_i} = 0$ for $i = 1, \ldots, r$.

(Recall that $M_f$ is the localization of $M$ at the multiplicative system $\{1, f, f^2, f^3, \ldots\}$.)
:::


::: {.solution}
<1>1. For any nonnegative integers \(p_1,\dots,p_r\), the elements \(f_1^{p_1},\dots,f_r^{p_r}\) generate the unit ideal.
::: {.proof}
If some \(p_i=0\), then \(f_i^{p_i}=1\), so the claim is immediate. Assume therefore that every \(p_i>0\). Let
\[
J=(f_1^{p_1},\dots,f_r^{p_r}).
\]
If \(J\neq A\), then \(J\) is contained in a maximal ideal \(\mathfrak m\). Since maximal ideals are prime and \(f_i^{p_i}\in\mathfrak m\), one has \(f_i\in\mathfrak m\) for every \(i\). Hence \((f_1,\dots,f_r)\subseteq\mathfrak m\), contradicting \((f_1,\dots,f_r)=A\). Thus \(J=A\).
:::

<1>2. If \(M=0\), then \(M_{f_i}=0\) for every \(i\).
::: {.proof}
Localization preserves the zero module.
:::

<1>3. Conversely, suppose \(M_{f_i}=0\) for every \(i\), and fix \(x\in M\). For each \(i\), there exists \(n_i\ge0\) such that
\[
f_i^{n_i}x=0.
\]
::: {.proof}
The element \(x/1\) is zero in \(M_{f_i}\). By the defining equivalence relation for localization, this means some power of \(f_i\) annihilates \(x\).
:::

<1>4. The element \(x\) is zero.
::: {.proof}
By <1>1, the powers \(f_1^{n_1},\dots,f_r^{n_r}\) generate the unit ideal. Hence there exist \(a_1,\dots,a_r\in A\) with
\[
1=\sum_{i=1}^r a_if_i^{n_i}.
\]
Multiplying by \(x\) and using <1>3 gives
\[
x=\sum_{i=1}^r a_if_i^{n_i}x=0.
\]
:::

<1>5. Therefore
\[
M=0\quad\Longleftrightarrow\quad M_{f_i}=0\text{ for all }i.
\]
::: {.proof}
The forward implication is <1>2; the reverse implication follows from <1>3 and <1>4 because every \(x\in M\) is zero.
:::
:::
