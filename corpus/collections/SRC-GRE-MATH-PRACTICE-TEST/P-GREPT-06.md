---
schema: qual/card@1
id: P-GREPT-06
kind: problem
title: "Number of real roots of $x^5+x^3+x-2000$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 6 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
At how many points does the graph of the curve $y = x^5 + x^3 + x - 2000$ cross the $x$-axis?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $5$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The polynomial
$$
p(x)=x^5+x^3+x-2000
$$
has at least one real zero.


::: pf-proof

The function $p$ is continuous. Moreover,
$$
p(4)=4^5+4^3+4-2000=-908<0
$$
and
$$
p(5)=5^5+5^3+5-2000=1255>0.
$$
By the intermediate value theorem, $p(c)=0$ for some $c\in(4,5)$.

:::

:::

::: {.pf-step #s1-2}

The polynomial $p$ is strictly increasing on $\RR$.


::: pf-proof

Its derivative is
$$
p'(x)=5x^4+3x^2+1.
$$
Every term except the final $1$ is nonnegative, so $p'(x)>0$ for every real
$x$. Hence $p$ is strictly increasing on $\RR$.

:::

:::

::: {.pf-step #s1-3}

Therefore the graph crosses the $x$-axis at exactly
$$
\boxed{1}
$$
point, so the answer is (A).


::: pf-proof

Step [](#s1-1){.pf-ref} gives at least one real zero. By step [](#s1-2){.pf-ref}, a strictly increasing
function cannot take the value $0$ at two distinct real numbers. Thus the zero
from step [](#s1-1){.pf-ref} is unique.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested number of crossings.

:::

:::

:::
