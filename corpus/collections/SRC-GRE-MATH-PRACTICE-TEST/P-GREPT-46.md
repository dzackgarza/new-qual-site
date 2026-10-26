---
schema: qual/card@1
id: P-GREPT-46
kind: problem
title: "Four-element subsets of a set with $\\binom n3-\\binom n2=14$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 46 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
$X$ is a finite set with the following property: The number of subsets of $X$ that contain exactly $3$ elements is $14$ more than the number of subsets of $X$ that contain exactly $2$ elements. How many subsets of $X$ contain exactly $4$ elements?

(A) $24$
(B) $25$
(C) $28$
(D) $32$
(E) $35$
:::

::: pf

::: pf-step

If $n=|X|$, then
$$
\binom n3-\binom n2=14.
$$


::: pf-proof

An $n$-element set has $\binom nk$ subsets containing exactly $k$ elements.
The stated difference between the numbers of three-element and two-element
subsets is therefore exactly the displayed equation.

:::

:::

::: pf-step

The equation in step <1>1 is equivalent to
$$
n(n-1)(n-5)=84.
$$


::: pf-proof

Using the binomial-coefficient formulas gives
$$
\begin{aligned}
14
&=\frac{n(n-1)(n-2)}6-\frac{n(n-1)}2\\
&=\frac{n(n-1)(n-5)}6.
\end{aligned}
$$
Multiplying by $6$ gives the claim.

:::

:::

::: pf-step

The only possible cardinality is
$$
n=7.
$$


::: pf-proof

The left side of step <1>2 is positive, so $n\ge6$. For $n=6$ it equals
$6\cdot5\cdot1=30$, while for $n=7$ it equals
$7\cdot6\cdot2=84$. For every $n\ge8$, all three positive factors are at
least their values at $n=8$, so the product is at least
$8\cdot7\cdot3=168>84$. Hence only $n=7$ works.

:::

:::

::: pf-step

Therefore the number of four-element subsets is
$$
\binom74=\boxed{35},
$$
so the answer is (E).


::: pf-proof

By step <1>3, $X$ has seven elements, and
$$
\binom74=\frac{7\cdot6\cdot5}{3\cdot2\cdot1}=35.
$$

:::

:::

::: pf-qed

Step <1>4 gives the requested number of subsets.

:::

:::
