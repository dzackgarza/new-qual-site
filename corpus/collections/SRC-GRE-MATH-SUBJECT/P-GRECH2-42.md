---
schema: qual/card@1
id: P-GRECH2-42
kind: problem
title: Convergence threshold for $\sum (n!)^2a^n/(2n)!$
classification:
  areas: [prelim]
  topics:
  - Series
  - Ratio Test
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 42 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Find the smallest value of b that makes the following statement true:

If $0 \le a < b$, then the series $\sum_{n=1}^{\infty} \frac{(n!)^2 a^n}{(2n)!}$ converges.

(A) $1$
(B) $2 \log 2$
(C) $2$
(D) $\sqrt{2}$
(E) $4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
c_n(a)=\frac{(n!)^2a^n}{(2n)!},
$$
the ratio of consecutive terms satisfies
$$
\lim_{n\to\infty}\frac{c_{n+1}(a)}{c_n(a)}=\frac a4
$$
for $a>0$.


::: pf-proof

Direct cancellation gives
$$
\frac{c_{n+1}(a)}{c_n(a)}
=a\frac{(n+1)^2}{(2n+1)(2n+2)}.
$$
Dividing numerator and denominator by $n^2$ and taking the limit gives $a/4$.

:::

:::

::: {.pf-step #s1-2}

The series converges for every $0\le a<4$ and diverges for every $a>4$.


::: pf-proof

If $a=0$, every term is zero, so the series converges. If $0<a<4$, then the limit in step [](#s1-1){.pf-ref} is strictly less than $1$, so the ratio test gives convergence. If $a>4$, that limit is strictly greater than $1$, so the terms do not tend to zero and the series diverges.

:::

:::

::: {.pf-step #s1-3}

The largest value of $b$ for which
$$
0\le a<b\quad\Longrightarrow\quad
\sum_{n=1}^{\infty}\frac{(n!)^2a^n}{(2n)!}
\text{ converges}
$$
is
$$
\boxed{b=4}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} shows that $b=4$ has the stated property. If $b>4$, choose any $a$ with $4<a<b$; step [](#s1-2){.pf-ref} shows that the corresponding series diverges. Thus no $b>4$ has the property.

:::

:::

::: {.pf-step #s1-4}

The source's word “smallest” makes the question false as a characterization of the threshold.


::: pf-proof

By step [](#s1-2){.pf-ref}, every positive $b\le4$ also has the displayed implication, since $0\le a<b$ then forces $a<4$. Hence $4$ is not the smallest such positive $b$; among the listed choices, $1$ is smaller and also satisfies the implication. Without restricting $b$ to be positive, every $b\le0$ makes the implication vacuous. The source's supplied answer (E) therefore answers the mathematically intended largest-threshold question established in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} determine both the convergence threshold and the defect in the literal wording.

:::

:::

:::
