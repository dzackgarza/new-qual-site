---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-07
kind: problem
title: 'Compare liminf of products of positive sequences'
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
  - counterexamples
relations: []
review: draft
---

::: {.problem title="?"}
(January 2014 #2)

(a) Produce sequences $\{a_n\}$, $\{b_n\}$ of positive real numbers such that
$$
\liminf_{n\to\infty}(a_nb_n)>\left(\liminf_{n\to\infty}a_n\right)\left(\liminf_{n\to\infty}b_n\right).
$$

(b) If $\{a_n\}$, $\{b_n\}$ are sequences of positive real numbers and $\{a_n\}$ converges, prove that
$$
\liminf_{n\to\infty}(a_nb_n)=\left(\lim_{n\to\infty}a_n\right)\left(\liminf_{n\to\infty}b_n\right).
$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (a) Example with strict inequality.
    Proof: take $a_n = 2 + (-1)^n$ and $b_n = 2 - (-1)^n$ for $n \ge 1$. Both are positive. The sequence $a_n$ alternates $3, 1, 3, 1, \ldots$, so $\liminf a_n = 1$; similarly $\liminf b_n = 1$. But $a_n b_n = (2+(-1)^n)(2-(-1)^n) = 4 - 1 = 3$ for every $n$, so $\liminf (a_n b_n) = 3 > 1\cdot 1 = (\liminf a_n)(\liminf b_n)$.
<1>2. (b) If $a_n \to a$, then $\liminf (a_n b_n) = a\,\liminf b_n$.
    Proof: since $a_n \to a$, for every $\epsilon > 0$ there is $N$ with $a - \epsilon < a_n < a + \epsilon$ for all $n \ge N$; the first finitely many terms do not affect any liminf. For $n \ge N$, $b_n > 0$ gives
    \[(a - \epsilon)\,b_n < a_n b_n < (a + \epsilon)\,b_n.\]
    Taking liminf over $n \ge N$ (equivalently over all $n$):
    \[(a-\epsilon)\,\liminf b_n \le \liminf (a_n b_n) \le (a+\epsilon)\,\liminf b_n,\]
    where we used that for positive $c$, $\liminf (c\,b_n) = c\,\liminf b_n$. Letting $\epsilon \to 0$ yields $\liminf(a_n b_n) = a\,\liminf b_n$.
<1>3. Q.E.D.
:::
