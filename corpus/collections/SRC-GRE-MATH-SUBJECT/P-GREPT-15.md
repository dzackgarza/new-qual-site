---
schema: qual/card@1
id: P-GREPT-15
kind: problem
title: "Convergence of $1/\\log n$ and two series built from it"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 15 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
For each integer $n > 1$, let $a_n = 1/(\log n)$. Which of the following statements is/are true?

I. The sequence $(a_n)$ converges.

II. The series $\sum_{n=2}^{\infty} a_n$ converges.

III. The series $\sum_{n=2}^{\infty} (-1)^n a_n^2$ converges.

(A) I only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement I is true: the sequence $(a_n)$ converges to $0$.


::: pf-proof

Since $\log n\to\infty$ as $n\to\infty$,
$$
a_n=\frac1{\log n}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-2}

Statement II is false: the series
$$
\sum_{n=2}^\infty a_n
$$
diverges.


::: pf-proof

For every $n\ge2$, one has $\log n<n$, so
$$
a_n=\frac1{\log n}>\frac1n.
$$
Since the harmonic series $\sum_{n=2}^\infty 1/n$ diverges, the comparison
test implies that $\sum_{n=2}^\infty a_n$ diverges.

:::

:::

::: {.pf-step #s1-3}

Statement III is true: the series
$$
\sum_{n=2}^\infty(-1)^na_n^2
$$
converges.


::: pf-proof

The positive terms
$$
a_n^2=\frac1{(\log n)^2}
$$
decrease monotonically for $n\ge2$ and tend to $0$ by step [](#s1-1){.pf-ref}. Hence the
alternating-series test gives convergence of
$\sum_{n=2}^\infty(-1)^na_n^2$.

:::

:::

::: {.pf-step #s1-4}

Therefore exactly I and III are true, so the answer is
$$
\boxed{\text{(C) I and III only}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} establish respectively that I is true, II is false, and III
is true.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
