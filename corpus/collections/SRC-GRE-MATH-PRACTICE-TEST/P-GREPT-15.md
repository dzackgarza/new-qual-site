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
<1>1. Statement I is true: the sequence $(a_n)$ converges to $0$.

::: {.proof}
Since $\log n\to\infty$ as $n\to\infty$,
$$
a_n=\frac1{\log n}\longrightarrow0.
$$
:::

<1>2. Statement II is false: the series
$$
\sum_{n=2}^\infty a_n
$$
diverges.

::: {.proof}
For every $n\ge2$, one has $\log n<n$, so
$$
a_n=\frac1{\log n}>\frac1n.
$$
Since the harmonic series $\sum_{n=2}^\infty 1/n$ diverges, the comparison
test implies that $\sum_{n=2}^\infty a_n$ diverges.
:::

<1>3. Statement III is true: the series
$$
\sum_{n=2}^\infty(-1)^na_n^2
$$
converges.

::: {.proof}
The positive terms
$$
a_n^2=\frac1{(\log n)^2}
$$
decrease monotonically for $n\ge2$ and tend to $0$ by step <1>1. Hence the
alternating-series test gives convergence of
$\sum_{n=2}^\infty(-1)^na_n^2$.
:::

<1>4. Therefore exactly I and III are true, so the answer is
$$
\boxed{\text{(C) I and III only}}.
$$

::: {.proof}
Steps <1>1--<1>3 establish respectively that I is true, II is false, and III
is true.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required choice.
:::
:::
