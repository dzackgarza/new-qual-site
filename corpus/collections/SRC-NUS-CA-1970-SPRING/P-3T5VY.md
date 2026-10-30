---
schema: qual/card@1
id: P-3T5VY
kind: problem
title: Number of zeros of $2z^5-6z^2-z+1$ in the annulus $1\leq\abs{z}\leq 2$
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find the number of zeroes, counting multiplicities, of the polynomial

$f(z) = 2z^5 - 6z^2 - z + 1 = 0$

in the annulus $1 \leq \abs{z} \leq 2$.
:::

::: {.solution}
Let $f(z) = 2z^5 - 6z^2 - z + 1$, and let $A = \{z \in \CC : 1 \leq \abs{z} \leq 2\}$ be the closed annulus. Zeros are counted with multiplicity.

* * *

### Step 1: Zeros in the open disk $\abs{z} < 2$

::: pf

::: {.pf-step #five-zeros-in-disk-2}
**$f(z)$ has 5 zeros in $\abs{z} < 2$.**

::: pf-proof

::: pf-step
Decompose $f(z) = F_1(z) + G_1(z)$ on the circle $\abs{z} = 2$, where $F_1(z) = 2z^5$ and $G_1(z) = -6z^2 - z + 1$.

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
On $\abs{z} = 2$, by the triangle inequality: $$\abs{G_1(z)} = \abs{-6z^2 - z + 1} \leq 6\abs{z}^2 + \abs{z} + 1 = 6(4) + 2 + 1 = 27.$$

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
Decompose $f(z) = F_2(z) + G_2(z)$ on the circle $\abs{z} = 1$, where $F_2(z) = -6z^2$ and $G_2(z) = 2z^5 - z + 1$.

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
On $\abs{z} = 1$, by the triangle inequality: $$\abs{G_2(z)} = \abs{2z^5 - z + 1} \leq 2\abs{z}^5 + \abs{z} + 1 = 2(1) + 1 + 1 = 4.$$

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
