---
schema: qual/card@1
id: P-GRECH2-49
kind: problem
title: "Taylor terms of $e^x$ needed to approximate $\\sqrt[5]{e}$ to within $10^{-6}$"
classification:
  areas: [prelim]
  topics:
  - Taylor Series
  - Error Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 49 of the Chapter 2 review questions in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The chapter-2.pdf scan ends at Question 48 and omits this question on the chapter's last page."
---

::: {.problem}
If the function $f(x) = e^x$ is expanded in powers of $x$, what is the minimum number of terms of the Taylor series that must be used to ensure that the resulting polynomial will approximate $\sqrt[5]{e}$ to within $10^{-6}$?

(A) $3$
(B) $4$
(C) $5$
(D) $6$
(E) $7$
:::

::: {.solution}

Since $\sqrt[5]{e}=e^{1/5}$, set
$$
t_k=\frac{(1/5)^k}{k!}.
$$

::: pf

::: {.pf-step #s1-1}

Five Taylor terms are not sufficient.


::: pf-proof

Using five terms gives the degree-$4$ Taylor polynomial
$$
P_4(1/5)=\sum_{k=0}^4 t_k.
$$
Every term of the exponential series at $1/5$ is positive, so
$$
e^{1/5}-P_4(1/5)
=\sum_{k=5}^\infty t_k
>t_5
=\frac1{5^5 5!}
=\frac1{375000}
>10^{-6}.
$$
Thus five terms cannot give the required accuracy.

:::

:::

::: {.pf-step #s1-2}

Six Taylor terms are sufficient.


::: pf-proof

Using six terms gives
$$
P_5(1/5)=\sum_{k=0}^5 t_k,
$$
whose error is
$$
R_5=\sum_{k=6}^\infty t_k.
$$
For $k\ge6$,
$$
\frac{t_{k+1}}{t_k}
=\frac1{5(k+1)}
\le\frac1{35}.
$$
Therefore
$$
\begin{aligned}
0<R_5
&\le t_6\sum_{j=0}^\infty\left(\frac1{35}\right)^j\\
&=\frac1{5^6 6!}\frac{35}{34}\\
&<\frac2{11250000}\\
&<10^{-6}.
\end{aligned}
$$
Hence six terms ensure the required accuracy.

:::

:::

::: {.pf-step #s1-3}

The minimum number of terms is
$$
\boxed{6},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-1){.pf-ref} rules out five terms, while step [](#s1-2){.pf-ref} proves that six terms suffice. Therefore six is minimal.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested minimum and corresponding choice.

:::

:::

:::
