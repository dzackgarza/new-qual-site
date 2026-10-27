---
schema: qual/card@1
id: P-GRECH2-18
kind: problem
title: The $n$th derivative of $1/(1-2x)$ at $x=-1/2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 18 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $n$ is a positive integer, what is the value of the $n^{\text{th}}$ derivative of $f(x) = \frac{1}{1 - 2x}$ at $x = -\frac{1}{2}$?

(A) $\frac{1}{2}(n^n)$
(B) $\frac{1}{2}(n!)$
(C) $\frac{1}{2}n$
(D) $n$
(E) $\frac{n^n}{n!}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $n\geq0$,
$$
f^{(n)}(x)=2^n n!(1-2x)^{-(n+1)}.
$$


::: pf-proof

For $n=0$, the formula is
$$
f(x)=(1-2x)^{-1},
$$
which is true. Suppose it holds for some $n\geq0$. Differentiating gives
$$
\begin{aligned}
f^{(n+1)}(x)
&=2^n n!\bigl(-(n+1)\bigr)(1-2x)^{-(n+2)}(-2)\\
&=2^{n+1}(n+1)!(1-2x)^{-(n+2)}.
\end{aligned}
$$
Thus the formula follows by induction.

:::

:::

::: {.pf-step #s1-2}

At $x=-1/2$,
$$
f^{(n)}\left(-\frac12\right)=\frac{n!}{2}.
$$


::: pf-proof

Substitute $x=-1/2$ into step [](#s1-1){.pf-ref}:
$$
\begin{aligned}
f^{(n)}\left(-\frac12\right)
&=2^n n!\left(1-2\left(-\frac12\right)\right)^{-(n+1)}\\
&=2^n n!\,2^{-(n+1)}\\
&=\frac{n!}{2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the requested value is
$$
\boxed{\frac12 n!},
$$
so the answer is (B).


::: pf-proof

This is exactly the value established in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the $n^{\mathrm{th}}$ derivative at the specified point and corresponding choice.

:::

:::

:::
