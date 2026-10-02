---
schema: qual/card@1
id: P-GRECH2-25
kind: problem
title: Evaluate $\int_{-1}^0 x^2(x+1)^3\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 25 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the following integral:

\[
\int_{-1}^{0} x^2 (x+1)^3 dx
\]

(A) $-\frac{7}{20}$
(B) $-\frac{1}{60}$
(C) $\frac{2}{15}$
(D) $\frac{1}{60}$
(E) $\frac{7}{20}$
:::

::: {.solution}
<1>1. With the substitution $u=x+1$, the integral becomes
$$
\int_0^1 (u^5-2u^4+u^3)\,du.
$$

::: {.proof}
When $u=x+1$, one has $x=u-1$ and $dx=du$. The bounds $x=-1$ and $x=0$ become $u=0$ and $u=1$. Thus
$$
x^2(x+1)^3=(u-1)^2u^3=u^5-2u^4+u^3,
$$
which gives the displayed integral.
:::

<1>2. The value of the integral is
$$
\frac1{60}.
$$

::: {.proof}
Integrating term by term in step <1>1 gives
$$
\left[\frac{u^6}{6}-\frac{2u^5}{5}+\frac{u^4}{4}\right]_0^1
=\frac16-\frac25+\frac14
=\frac{10-24+15}{60}
=\frac1{60}.
$$
:::

<1>3. Therefore
$$
\boxed{\frac1{60}},
$$
so the answer is (D).

::: {.proof}
This is exactly the value established in step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested integral and corresponding choice.
:::
:::
