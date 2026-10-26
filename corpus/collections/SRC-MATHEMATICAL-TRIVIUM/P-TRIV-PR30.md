---
schema: qual/card@1
id: P-TRIV-PR30
kind: problem
title: Transition probabilities of a Markov chain on energy levels
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 30, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
An electron can occupy one of a countable number of energy levels in atom.
The transition probabilities from i’s to j’s level per second are given by

$$
P _ { i j } ( t = 1 ) = c _ { i } e ^ { - \alpha | i - j | } ,\tag{54}
$$

where $\alpha > 0$ and $c _ { i }$ are some constants.
Find

(a) $P _ { i j } ( t = 2 )$

(b) $c _ { i } .$
:::

Assume the energy levels are indexed by the nonnegative integers $0,1,2,\ldots$, and put
\[
r=e^{-\alpha}\in(0,1).
\]
Then the one-step transition probabilities are $P_{ij}=c_i r^{|i-j|}$.

::: pf

::: pf-step

Row normalization requires
\[
c_i^{-1}=\sum_{j=0}^{\infty}r^{|i-j|}.
\]


::: pf-proof

For fixed $i$, transition probabilities must sum to one:
\[
1=\sum_{j=0}^{\infty}P_{ij}
=c_i\sum_{j=0}^{\infty}r^{|i-j|}.
\]
Solve for $c_i$.

:::

:::

::: pf-step

The normalizing sum is
\[
\sum_{j=0}^{\infty}r^{|i-j|}
=\frac{1+r-r^{i+1}}{1-r}.
\]


::: pf-proof

Split at $j=i$:
\[
\sum_{j=0}^{i}r^{i-j}
+\sum_{j=i+1}^{\infty}r^{j-i}
=\sum_{k=0}^{i}r^k+\sum_{k=1}^{\infty}r^k.
\]
The two geometric sums equal
\[
\frac{1-r^{i+1}}{1-r}+\frac r{1-r}
=\frac{1+r-r^{i+1}}{1-r}.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
c_i=\frac{1-r}{1+r-r^{i+1}}
=\frac{1-e^{-\alpha}}
{1+e^{-\alpha}-e^{-(i+1)\alpha}}.}
\]


::: pf-proof

Invert the expression in step <1>2 and substitute $r=e^{-\alpha}$.

:::

:::

::: pf-step

By the Chapman--Kolmogorov equation,
\[
P_{ij}(2)=\sum_{k=0}^{\infty}P_{ik}(1)P_{kj}(1).
\]


::: pf-proof

To move from level $i$ to level $j$ in two steps, condition on the intermediate level $k$. The events corresponding to different $k$ are disjoint, and the Markov property makes the two factors the one-step transition probabilities.

:::

:::

::: pf-step

Hence
\[
\boxed{
P_{ij}(2)
=c_i\sum_{k=0}^{\infty}c_k
e^{-\alpha(|i-k|+|k-j|)}}.
}
\]


::: pf-proof

Substitute $P_{ik}(1)=c_i e^{-\alpha|i-k|}$ and $P_{kj}(1)=c_k e^{-\alpha|k-j|}$ into step <1>4 and factor out $c_i$.

:::

:::

::: pf-step

Substituting the normalization from step <1>3 gives the fully explicit convergent series
\[
\boxed{
P_{ij}(2)
=\frac{(1-r)^2}{1+r-r^{i+1}}
\sum_{k=0}^{\infty}
\frac{r^{|i-k|+|k-j|}}
{1+r-r^{k+1}},
\qquad r=e^{-\alpha}.}
\]


::: pf-proof

Replace $c_i$ and $c_k$ in step <1>5 by step <1>3. Since $0<r<1$, the summand is bounded by a constant multiple of $r^{|i-k|+|k-j|}$, so the series converges absolutely.

:::

:::

::: pf-qed

Step <1>3 gives the constants $c_i$, and steps <1>5--<1>6 give the two-step transition probabilities.

:::

:::
