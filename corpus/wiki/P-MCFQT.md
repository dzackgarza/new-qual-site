---
schema: qual/card@1
id: P-MCFQT
kind: problem
title: $\sqrt{n}(\sqrt{n+1}-\sqrt{n})\to\frac12$
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
relations: []
review: draft
solved: true
---

::: problem
Let $a_n =\sqrt{n}\left(\sqrt{n+1}-\sqrt{n}\right)$.
Prove that $\lim_{n\to\infty}a_n=1/2$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $a_n = \sqrt{n}(\sqrt{n+1} - \sqrt{n}) = \sqrt{n}\cdot\frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{\sqrt{n}}{\sqrt{n+1} + \sqrt{n}}$.
Proof: rationalize: $\sqrt{n+1} - \sqrt{n} = \frac{(n+1)-n}{\sqrt{n+1}+\sqrt{n}}$.

<1>2. $a_n = \dfrac{1}{\frac{\sqrt{n+1}}{\sqrt{n}} + 1} = \dfrac{1}{\sqrt{1 + 1/n} + 1}$.
Proof: divide numerator and denominator by $\sqrt{n}$.

<1>3. $\sqrt{1 + 1/n} \to 1$ as $n \to \infty$.
Proof: continuity of the square root and $1 + 1/n \to 1$ (or the standard squeeze $1 \le \sqrt{1+1/n} \le 1 + 1/(2n)$-style bound).

<1>4. Q.E.D.: $a_n \to \dfrac{1}{1 + 1} = \dfrac{1}{2}$.
Proof: <1>2 and <1>3, by the quotient law for limits.
:::
