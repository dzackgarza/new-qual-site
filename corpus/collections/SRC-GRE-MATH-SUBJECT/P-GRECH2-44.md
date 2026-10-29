---
schema: qual/card@1
id: P-GRECH2-44
kind: problem
title: Implications between convergence of nonnegative series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 44 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following statements are true?

I. If $a_n \ge 0$ for every $n$, then: $\sum_{n=1}^{\infty} a_n$ converges $\Rightarrow \sum_{n=1}^{\infty} \sqrt{a_n}$ converges.

II. If $a_n \ge 0$ for every $n$, then: $\sum_{n=1}^{\infty} n a_n$ converges $\Rightarrow \sum_{n=1}^{\infty} a_n$ converges.

III. If $a_n \ge 0$ and $a_{n+1} \le a_n$ for every $n$, then: $\sum_{n=1}^{\infty} a_n^2$ converges $\Rightarrow \sum_{n=1}^{\infty} (-1)^n a_n$ converges.

(A) I and II only
(B) I and III only
(C) II only
(D) II and III only
(E) III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement I is false.


::: pf-proof

Take
$$
a_n=\frac1{n^2}.
$$
Then $a_n\ge0$ and the $p$-series $\sum_{n=1}^\infty a_n$ converges, but
$$
\sum_{n=1}^\infty\sqrt{a_n}
=\sum_{n=1}^\infty\frac1n
$$
is the divergent harmonic series. Thus the implication in I fails.

:::

:::

::: {.pf-step #s1-2}

Statement II is true.


::: pf-proof

For every $n\ge1$,
$$
0\le a_n\le n a_n.
$$
Hence, if $\sum_{n=1}^\infty n a_n$ converges, then the comparison test implies that $\sum_{n=1}^\infty a_n$ converges.

:::

:::

::: {.pf-step #s1-3}

Statement III is true.


::: pf-proof

If $\sum_{n=1}^\infty a_n^2$ converges, then its terms satisfy $a_n^2\to0$. Since $a_n\ge0$, it follows that $a_n\to0$. Together with the hypothesis $a_{n+1}\le a_n$, the alternating-series test applies to
$$
\sum_{n=1}^\infty(-1)^n a_n,
$$
so that series converges.

:::

:::

::: {.pf-step #s1-4}

Exactly statements II and III are true, so the answer is
$$
\boxed{\text{(D) II and III only}}.
$$


::: pf-proof

This follows from steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested choice.

:::

:::

:::
