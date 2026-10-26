---
schema: qual/card@1
id: P-GREPT-62
kind: problem
title: "Consequences of Lebesgue integrability for a bounded function"
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 62 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $f\colon \RR \to \RR$ is a bounded function that is Lebesgue integrable, then which of the following must be true?

(A) $f$ is Riemann integrable.
(B) There does not exist a countably infinite $E$ of $\RR$ such that $f$ is nondifferentiable at every $x \in E$.
(C) There does not exist an uncountable subset $E$ of $\RR$ such that $f$ is nondifferentiable at every $x \in E$.
(D) There does not exist an uncountable subset $E$ of $\RR$ such that $f$ is discontinuous at every $x \in E$.
(E) None of the above.
:::

Define $f=\mathbf 1_{\QQ}$, the characteristic function of the rational numbers.

::: pf

::: pf-step

The function $f$ is bounded and Lebesgue integrable on $\RR$.


::: pf-proof

The function takes only the values $0$ and $1$, so it is bounded. Since
$\QQ$ is countable, it has Lebesgue measure zero. Thus $f=0$ almost
everywhere, and consequently
\[
\int_{\RR}|f|\,dx=0.
\]
Hence $f$ is Lebesgue integrable.

:::

:::

::: pf-step

The function $f$ is discontinuous at every point of $\RR$.


::: pf-proof

Every interval contains both rational and irrational numbers. Therefore,
for every $x\in\RR$ and every neighborhood of $x$, the function assumes
both values $0$ and $1$ in that neighborhood. Hence $f$ is not continuous
at $x$. Since $x$ was arbitrary, $f$ is nowhere continuous.

:::

:::

::: pf-step

The function $f$ is nondifferentiable at every point of $\RR$.


::: pf-proof

Differentiability at a point implies continuity at that point. Step <1>2
shows that $f$ is continuous nowhere, so it is differentiable nowhere.

:::

:::

::: pf-step

Statement (A) is false.


::: pf-proof

On the interval $[0,1]$, every nondegenerate subinterval contains both
rational and irrational points. Hence every lower Darboux sum of $f$ is
$0$ and every upper Darboux sum is $1$. Thus $f$ is not Riemann integrable
even on $[0,1]$.

:::

:::

::: pf-step

Statements (B), (C), and (D) are false.


::: pf-proof

By step <1>3, $f$ is nondifferentiable on all of $\RR$. Therefore any
countably infinite subset of $\RR$ contradicts (B), while the uncountable
set $E=\RR$ contradicts (C). By step <1>2, the same set $E=\RR$
contradicts (D).

:::

:::

::: pf-step

The correct answer is $\boxed{\text{(E) None of the above}}$.


::: pf-proof

Step <1>1 supplies a function satisfying the hypotheses, while steps
<1>4 and <1>5 show that none of statements (A)--(D) must hold.

:::

:::

::: pf-qed

Step <1>6 gives the required choice.

:::

:::
