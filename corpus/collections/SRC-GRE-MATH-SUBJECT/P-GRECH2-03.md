---
schema: qual/card@1
id: P-GRECH2-03
kind: problem
title: One-sided limits of $|x|-[x]$ at $\pm n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 3 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $[x]$ denote the greatest integer $\le x$. If $n$ is a positive integer, then

$$
\lim_{x \to -n^-} (|x| - [x]) - \lim_{x \to n^-} (|x| - [x]) = ?
$$

(A) $-2$
(B) $0$
(C) $2$
(D) $2n - 1$
(E) $2n$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The left-hand limit at $-n$ is $2n+1$.


::: pf-proof

For $x<-n$ sufficiently close to $-n$, one has
$$
-n-1<x<-n,
$$
so $[x]=-n-1$. Also $|x|=-x$ near the negative point $-n$. Therefore
$$
\lim_{x\to -n^-}(|x|-[x])
=n-(-n-1)
=2n+1.
$$

:::

:::

::: {.pf-step #s1-2}

The left-hand limit at $n$ is $1$.


::: pf-proof

For $x<n$ sufficiently close to the positive integer $n$,
$$
n-1<x<n,
$$
so $[x]=n-1$, while $|x|=x$. Hence
$$
\lim_{x\to n^-}(|x|-[x])
=n-(n-1)
=1.
$$

:::

:::

::: {.pf-step #s1-3}

The requested difference is
$$
\boxed{2n},
$$
so the answer is (E).


::: pf-proof

Subtract the limits from steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}:
$$
(2n+1)-1=2n.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
