---
schema: qual/card@1
id: P-GRECH2-07
kind: problem
title: Limit of $x^{-2}\int_0^x (t+t^2)/(1+\sin t)\,dt$ at $0$
classification:
  areas: [prelim]
  topics:
  - Limits
  - Fundamental Theorem of Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 7 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the following limit:

$$
\lim_{x \to 0} \left[ \frac{1}{x^2} \int_0^x \frac{t + t^2}{1 + \sin t} dt \right]
$$

(A) $\frac{1}{2\pi}$
(B) $\frac{1}{\pi}$
(C) $\frac{1}{2}$
(D) $1$
(E) $\frac{\pi}{2}$
:::

::: {.solution}

Let
$$
F(x)=\int_0^x\frac{t+t^2}{1+\sin t}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

For $x$ near $0$,
$$
F'(x)=\frac{x+x^2}{1+\sin x}.
$$


::: pf-proof

The integrand is continuous near $0$ because $1+\sin t$ is nonzero there. The fundamental theorem of calculus therefore gives the displayed derivative.

:::

:::

::: {.pf-step #s1-2}

The limit equals $1/2$.


::: pf-proof

Since $F(0)=0$, the original quotient has the indeterminate form $0/0$. By L'Hôpital's rule and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\lim_{x\to0}\frac{F(x)}{x^2}
&=\lim_{x\to0}\frac{x+x^2}{2x(1+\sin x)}\\
&=\lim_{x\to0}\frac{1+x}{2(1+\sin x)}\\
&=\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\frac12},
$$
so the answer is (C).


::: pf-proof

This is exactly the value obtained in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested limit and corresponding choice.

:::

:::

:::
