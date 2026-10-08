---
schema: qual/card@1
id: P-RAYX2
kind: problem
title: Produce sequences $\{a_n\},\,\{b_n\}$ of
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Produce sequences $\{a_n\},\,\{b_n\}$ of positive real numbers such that $$\liminf_{n\to\infty}(a_nb_n)>\left(\liminf_{n\to\infty} a_n\right) \left(\liminf_{n\to\infty} b_n\right).$$

If $\{a_n\},\,\{b_n\}$ are sequences of positive real numbers and $\{a_n\}$ converges, prove that $$\liminf_{n\to\infty}(a_nb_n)=\left(\lim_{n\to\infty}a_n\right)\left(\liminf_{n\to\infty}b_n\right).$$
:::
::: {.solution}
<1>1. The sequences $a_n=2+(-1)^n$ and $b_n=2-(-1)^n$ satisfy the strict inequality in part (a).

::: {.proof}
Both sequences have terms in $\{1,3\}$, and each has lower limit $1$. On the other hand, $a_nb_n=4-(-1)^{2n}=3$ for every $n$. Thus
\[
\boxed{\liminf_{n\to\infty}(a_nb_n)=3>1
=\left(\liminf_{n\to\infty}a_n\right)
\left(\liminf_{n\to\infty}b_n\right)}.
\]
:::

<1>2. Part (b), as stated in the source, is false.

::: {.proof}
Take $a_n=1/n$ and $b_n=n$. Both sequences are positive and $a_n\to0$, while $a_nb_n=1$ for every $n$. Thus $\liminf(a_nb_n)=1$. The right-hand side of the proposed identity is $0\cdot(+\infty)$, which is undefined in the extended real numbers. Assigning it the value $0$ would give a false identity. The source's unrestricted assertion is therefore not a well-defined equality under its stated hypotheses.
:::

<1>3. If $a_n\to a>0$, then $\liminf(a_nb_n)=a\liminf b_n$, including when $\liminf b_n=+\infty$.

::: {.proof}
Fix $0<\varepsilon<a$. Eventually
\[
(a-\varepsilon)b_n\leq a_nb_n\leq(a+\varepsilon)b_n.
\]
Let $L=\liminf b_n\in[0,+\infty]$. If $L<+\infty$, taking lower limits gives
\[
(a-\varepsilon)L\leq\liminf(a_nb_n)\leq(a+\varepsilon)L.
\]
Letting $\varepsilon\downarrow0$ proves the equality. If $L=+\infty$, the lower bound $(a-\varepsilon)b_n$ tends to $+\infty$, so $\liminf(a_nb_n)=+\infty=aL$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 answers part (a). Step <1>2 identifies the defect in part (b), and step <1>3 proves the corrected assertion under the sufficient additional hypothesis $a>0$.
:::
:::
