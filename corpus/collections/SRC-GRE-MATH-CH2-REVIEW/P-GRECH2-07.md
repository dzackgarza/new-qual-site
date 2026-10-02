---
schema: qual/card@1
id: P-GRECH2-07
kind: problem
title: Limit of $x^{-2}\int_0^x (t+t^2)/(1+\sin t)\,dt$ at $0$
classification:
  areas: [prelim]
  topics: []
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

\[
\lim_{x \to 0} \left[ \frac{1}{x^2} \int_0^x \frac{t + t^2}{1 + \sin t} dt \right]
\]

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

<1>1. For $x$ near $0$,
$$
F'(x)=\frac{x+x^2}{1+\sin x}.
$$

::: {.proof}
The integrand is continuous near $0$ because $1+\sin t$ is nonzero there. The fundamental theorem of calculus therefore gives the displayed derivative.
:::

<1>2. The limit equals $1/2$.

::: {.proof}
Since $F(0)=0$, the original quotient has the indeterminate form $0/0$. By L'Hôpital's rule and step <1>1,
$$
\begin{aligned}
\lim_{x\to0}\frac{F(x)}{x^2}
&=\lim_{x\to0}\frac{x+x^2}{2x(1+\sin x)}\\
&=\lim_{x\to0}\frac{1+x}{2(1+\sin x)}\\
&=\frac12.
\end{aligned}
$$
:::

<1>3. Therefore
$$
\boxed{\frac12},
$$
so the answer is (C).

::: {.proof}
This is exactly the value obtained in step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested limit and corresponding choice.
:::
:::
