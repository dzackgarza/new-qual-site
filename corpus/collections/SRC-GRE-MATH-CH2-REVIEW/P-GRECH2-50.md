---
schema: qual/card@1
id: P-GRECH2-50
kind: problem
title: "Exponent $k$ making $(e^{x^2}-x^2-1)(\\cos x-1)/x^k$ have a finite nonzero limit"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 50 of the Chapter 2 review questions in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The chapter-2.pdf scan ends at Question 48 and omits this question on the chapter's last page."
---

::: {.problem}
There is exactly one value of the constant $k$ such that

$$\lim_{x \to 0} \frac{(e^{x^2} - x^2 - 1)(\cos x - 1)}{x^k}$$

is finite and nonzero. What is this value of $k$, and what is the limit, $L$?

(A) $k = 4$, $L = -\frac{1}{2}$
(B) $k = 6$, $L = \frac{1}{4}$
(C) $k = 4$, $L = 1$
(D) $k = 6$, $L = -\frac{1}{4}$
(E) $k = 4$, $L = \frac{1}{2}$
:::

::: pf

::: pf-step

As $x\to0$,
$$
e^{x^2}-x^2-1=\frac{x^4}{2}+O(x^6)
$$
and
$$
\cos x-1=-\frac{x^2}{2}+O(x^4).
$$


::: pf-proof

The Taylor expansions at $0$ are
$$
e^{x^2}
=1+x^2+\frac{x^4}{2}+\frac{x^6}{6}+O(x^8)
$$
and
$$
\cos x
=1-\frac{x^2}{2}+\frac{x^4}{24}+O(x^6).
$$
Subtracting the indicated lower-order terms gives the two displayed expansions.

:::

:::

::: pf-step

The numerator has leading term $-x^6/4$:
$$
(e^{x^2}-x^2-1)(\cos x-1)
=-\frac{x^6}{4}+O(x^8).
$$


::: pf-proof

Multiplying the expansions in step <1>1 gives
$$
\left(\frac{x^4}{2}+O(x^6)\right)
\left(-\frac{x^2}{2}+O(x^4)\right)
=-\frac{x^6}{4}+O(x^8).
$$

:::

:::

::: pf-step

The unique exponent producing a finite nonzero limit is
$$
\boxed{k=6},
$$
and then
$$
\boxed{L=-\frac14}.
$$


::: pf-proof

By step <1>2,
$$
\frac{(e^{x^2}-x^2-1)(\cos x-1)}{x^k}
=x^{6-k}\left(-\frac14+O(x^2)\right).
$$
For the quotient to tend to a finite nonzero value, the factor $x^{6-k}$ must have exponent $0$, so $k=6$. Substituting $k=6$ leaves
$$
-\frac14+O(x^2)\longrightarrow-\frac14.
$$

:::

:::

::: pf-step

Therefore the answer is (D).


::: pf-proof

Step <1>3 gives exactly the pair listed in choice (D).

:::

:::

::: pf-qed

Step <1>4 identifies the requested choice.

:::

:::
