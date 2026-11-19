---
schema: qual/card@1
id: P-3T5VY
kind: problem
title: Number of zeros of $2z^5-6z^2+z+1$ in the annulus $1\leq\abs{z}\leq 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Polynomials
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read at the printed page in four published papers that carry this exercise. UC Irvine
    Complex Analysis Qualifying Examination, 18 June 2013, Problem 5 (PDF p. 6): "Determine the
    number of roots, counted with multiplicity, of the equation $2z^5-6z^2+z+1=0$ inside the
    annulus $1\leq\abs z\leq 2$." UC Irvine Complex Qualifying Examination, 20 September 2012,
    Problem 4 (PDF p. 5): the same equation and instruction, in the annulus
    $A(0,1,2)=\theset{z:1<\abs z<2}$. Johns Hopkins Qualifying Exam Spring 2016, Question 7
    (PDF p. 11 of `gradexam/analysisexams.pdf`, printed p. 1 of that paper): "Determine the
    number of zeroes of the polynomial $2z^5-6z^2+z+1=0$ in the annulus $1\leq\abs z\leq 2$."
    University of Iowa Analysis Qualifying Examination, 12 January 2024, Part II Problem C-3
    (PDF p. 16): "$p(z)\coloneqq 2z^5-6z^2+z+1$, determine the number of zeros of $p$ (counting
    multiplicities) inside the annulus ann(0; 1, 2)". All four print $+z$ on the linear term.
    Not checked in this pass: whether any of the four is the paper this question was set in.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The imported text this card was transcribed from, row 108 of
    `Combined_Questions.yaml` at revision `6190e0ee`, prints
    $f(z)=2z^5-6z^2-z+1$, and the card carried that sign. Since the only document that prints
    $-z$ is that transcription, and every published printing of the exercise prints $+z$, the
    statement now prints $+z$; its wording is the retained one. The two Rouché bounds were
    rewritten for the $+z$ polynomial and rechecked: on $\abs z=2$,
    $\abs{-6z^2+z+1}\leq 6\cdot 4+2+1=27<64=\abs{2z^5}$, and on $\abs z=1$,
    $\abs{2z^5+z+1}\leq 2+1+1=4<6=\abs{-6z^2}$. The answer $3$ does not depend on the sign, and
    a numeric root computation gives moduli $0.33172,0.51413,1.32755,1.48606,1.48606$ for $+z$
    against $0.33502,0.48870,1.44662,1.44662,1.45933$ for $-z$, three inside
    $1\leq\abs z\leq 2$ either way.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find the number of zeroes, counting multiplicities, of the polynomial

$$
f(z) = 2z^5 - 6z^2 + z + 1
$$

in the annulus $1 \leq \abs{z} \leq 2$.
:::

::: {.solution}
Let $f(z) = 2z^5 - 6z^2 + z + 1$, and let $A = \{z \in \CC : 1 \leq \abs{z} \leq 2\}$ be the closed annulus. Zeros are counted with multiplicity.

* * *

### Step 1: Zeros in the open disk $\abs{z} < 2$

::: pf

::: {.pf-step #five-zeros-in-disk-2}
**$f(z)$ has 5 zeros in $\abs{z} < 2$.**

::: pf-proof

::: pf-step
Decompose $f(z) = F_1(z) + G_1(z)$ on the circle $\abs{z} = 2$, where $F_1(z) = 2z^5$ and $G_1(z) = -6z^2 + z + 1$.

::: pf-proof
*Proof:* Algebraic splitting of terms.
:::

:::

::: pf-step
On $\abs{z} = 2$, $\abs{F_1(z)} = 2 \abs{z}^5 = 2 \cdot 2^5 = 64$.

::: pf-proof
*Proof:* Direct evaluation on $\abs{z}=2$.
:::

:::

::: pf-step
On $\abs{z} = 2$, by the triangle inequality: $$\abs{G_1(z)} = \abs{-6z^2 + z + 1} \leq 6\abs{z}^2 + \abs{z} + 1 = 6(4) + 2 + 1 = 27.$$

::: pf-proof
*Proof:* Triangle inequality $\abs{a+b+c} \leq \abs{a}+\abs{b}+\abs{c}$.
:::

:::

::: pf-step
Since $\abs{G_1(z)} \leq 27 < 64 = \abs{F_1(z)}$ on $\abs{z} = 2$, the strict inequality $\abs{G_1(z)} < \abs{F_1(z)}$ holds everywhere on the circle $\abs{z} = 2$.

::: pf-proof
*Proof:* $27 < 64$.
:::

:::

::: pf-step
By Rouché's Theorem, $f(z) = F_1(z) + G_1(z)$ and $F_1(z) = 2z^5$ have the same number of zeros inside $\abs{z} < 2$.

::: pf-proof
*Proof:* Hypotheses of Rouché's Theorem are satisfied on the simple closed curve $\abs{z}=2$.
:::

:::

::: pf-step
The polynomial $F_1(z) = 2z^5$ has a zero of multiplicity 5 at $z = 0 \in D(0, 2)$, and no other zeros.

::: pf-proof
*Proof:* $2z^5 = 0 \iff z = 0$.
:::

:::

::: {.pf-step #five-zeros-conclusion}
Thus, $f(z)$ has exactly 5 zeros in $\abs{z} < 2$.
Moreover, since $\abs{f(z)} \geq \abs{F_1(z)} - \abs{G_1(z)} \geq 64 - 27 = 37 > 0$ on $\abs{z}=2$, $f(z)$ has no zeros on the circle $\abs{z}=2$.

::: pf-proof
*Proof:* Reverse triangle inequality.
:::

:::

::: pf-qed
Step [](#five-zeros-conclusion){.pf-ref}.
:::

:::

:::

:::

* * *

### Step 2: Zeros in the open disk $\abs{z} < 1$

::: pf

::: {.pf-step #two-zeros-in-disk-1}
**$f(z)$ has 2 zeros in $\abs{z} < 1$.**

::: pf-proof

::: pf-step
Decompose $f(z) = F_2(z) + G_2(z)$ on the circle $\abs{z} = 1$, where $F_2(z) = -6z^2$ and $G_2(z) = 2z^5 + z + 1$.

::: pf-proof
*Proof:* Algebraic splitting of terms.
:::

:::

::: pf-step
On $\abs{z} = 1$, $\abs{F_2(z)} = 6 \abs{z}^2 = 6$.

::: pf-proof
*Proof:* Direct evaluation on $\abs{z}=1$.
:::

:::

::: pf-step
On $\abs{z} = 1$, by the triangle inequality: $$\abs{G_2(z)} = \abs{2z^5 + z + 1} \leq 2\abs{z}^5 + \abs{z} + 1 = 2(1) + 1 + 1 = 4.$$

::: pf-proof
*Proof:* Triangle inequality.
:::

:::

::: pf-step
Since $\abs{G_2(z)} \leq 4 < 6 = \abs{F_2(z)}$ on $\abs{z} = 1$, the strict inequality $\abs{G_2(z)} < \abs{F_2(z)}$ holds everywhere on the circle $\abs{z} = 1$.

::: pf-proof
*Proof:* $4 < 6$.
:::

:::

::: pf-step
By Rouché's Theorem, $f(z) = F_2(z) + G_2(z)$ and $F_2(z) = -6z^2$ have the same number of zeros inside $\abs{z} < 1$.

::: pf-proof
*Proof:* Hypotheses of Rouché's Theorem are satisfied on the simple closed curve $\abs{z}=1$.
:::

:::

::: pf-step
The polynomial $F_2(z) = -6z^2$ has a zero of multiplicity 2 at $z = 0 \in D(0, 1)$, and no other zeros.

::: pf-proof
*Proof:* $-6z^2 = 0 \iff z = 0$.
:::

:::

::: {.pf-step #two-zeros-conclusion}
Thus, $f(z)$ has exactly 2 zeros in $\abs{z} < 1$.
Furthermore, on $\abs{z}=1$, $\abs{f(z)} \geq \abs{F_2(z)} - \abs{G_2(z)} \geq 6 - 4 = 2 > 0$, so $f(z)$ has no zeros on the boundary circle $\abs{z}=1$.

::: pf-proof
*Proof:* Reverse triangle inequality.
:::

:::

::: pf-qed
Step [](#two-zeros-conclusion){.pf-ref}.
:::

:::

:::

:::

* * *

### Step 3: Zeros in the annulus $1 \leq \abs{z} \leq 2$

::: pf

::: pf-step
**$f(z)$ has exactly $5 - 2 = 3$ zeros in the annulus $1 \leq \abs{z} \leq 2$.**

::: pf-proof

::: pf-step
The closed disk $\overline{D}(0, 2) = \{\abs{z} \leq 2\}$ is the disjoint union of the open disk $D(0, 1) = \{\abs{z} < 1\}$ and the closed annulus $A = \{1 \leq \abs{z} \leq 2\}$.

::: pf-proof
*Proof:* Partition of the closed disk.
:::

:::

::: pf-step
By step [](#five-zeros-conclusion){.pf-ref} and step [](#two-zeros-conclusion){.pf-ref}, $f$ has no zeros on $\abs{z}=1$ or on $\abs{z}=2$.

::: pf-proof
*Proof:* Direct consequence of the non-vanishing bounds $\abs{f(z)} \geq 2 > 0$ on $\abs{z}=1$ and $\abs{f(z)} \geq 37 > 0$ on $\abs{z}=2$.
:::

:::

::: pf-step
Therefore, all zeros of $f$ in $\abs{z} \leq 2$ lie either in $\abs{z} < 1$ or in the interior of the annulus $1 < \abs{z} < 2$.

::: pf-proof
*Proof:* Disjoint union of zero sets.
:::

:::

::: {.pf-step #annulus-zero-count}
Number of zeros in $A$ = (Number of zeros in $\abs{z} < 2$) - (Number of zeros in $\abs{z} < 1$) = $5 - 2 = 3$.

::: pf-proof
*Proof:* Subtraction of counts from step [](#five-zeros-in-disk-2){.pf-ref} and step [](#two-zeros-in-disk-1){.pf-ref}.
:::

:::

::: pf-qed
Step [](#annulus-zero-count){.pf-ref}.
:::

:::

:::

:::

:::

::: {.remark}
The same count answers the exercise with the opposite sign of the linear term: that term enters the two triangle inequalities only through $\abs z$, so $\abs{-6z^2\mp z+1}\le 6\cdot4+2+1=27<64=\abs{2z^5}$ on $\abs z=2$ and $\abs{2z^5\mp z+1}\le 2+1+1=4<6=\abs{-6z^2}$ on $\abs z=1$ hold with either sign, leaving five zeros in $\abs z<2$, two in $\abs z<1$ and three in the annulus.
:::
