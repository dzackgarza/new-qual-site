---
schema: qual/card@1
id: P-PGDJ2
kind: problem
title: How many zeros does the polynomial
classification:
  areas:
  - real-analysis
  topics:
  - rouche
  - polynomials
relations: []
review: draft
---

::: {.problem title="?"}
How many zeros does the polynomial $$z^9 + z^6 + 30z^5 - 3z + 2$$ have in the annulus $\{1 \le |z| \le 3\}$.
Justify your answer.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Count the zeros of $p(z) = z^9 + z^6 + 30z^5 - 3z + 2$ in the annulus $\{1 \le |z| \le 3\}$.

<1>1. On $|z| = 3$, $|z^6 + 30z^5 - 3z + 2| < |z^9|$.
    Proof: $|z^6 + 30z^5 - 3z + 2| \le 3^6 + 30\cdot 3^5 + 3\cdot 3 + 2 = 729 + 7290 + 9 + 2 = 8030$, while $|z^9| = 3^9 = 19683 > 8030$.

<1>2. $p$ has 9 zeros in $|z| < 3$ counting multiplicity.
    Proof: Rouch\'e's theorem on $|z| = 3$ with $f = z^9$, $g = z^6 + 30z^5 - 3z + 2$: by <1>1, $p = f + g$ has as many zeros as $z^9$ in $|z| < 3$, namely 9.

<1>3. On $|z| = 1$, $|z^9 + z^6 - 3z + 2| < |30z^5|$.
    Proof: $|z^9 + z^6 - 3z + 2| \le 1 + 1 + 3 + 2 = 7 < 30 = |30z^5|$.

<1>4. $p$ has 5 zeros in $|z| < 1$ counting multiplicity.
    Proof: Rouch\'e's theorem on $|z| = 1$ with $f = 30z^5$, $g = z^9 + z^6 - 3z + 2$: by <1>3, $p = f + g$ has as many zeros as $30z^5$ in $|z| < 1$, namely 5 (all at $z = 0$).

<1>5. $p$ has $9 - 5 = 4$ zeros in the annulus $1 < |z| < 3$, and none on the circles.
    Proof: <1>2 and <1>4 give the count by subtraction; the strict inequalities <1>1 and <1>3 show $p \ne 0$ on $|z| = 3$ and $|z| = 1$, so the annulus $\{1 \le |z| \le 3\}$ contains exactly the 4 zeros found.

<1>6. Q.E.D.
    Proof: <1>1–<1>5 answer the question.
:::
