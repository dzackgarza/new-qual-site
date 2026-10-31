---
schema: qual/card@1
id: P-TRIV-PR33
kind: problem
title: Borel's normal number theorem
classification:
  areas: [prelim]
  topics:
  - Normal Numbers
  - Strong Law of Large Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
*Normal numbers*

Let $x \in [0, 1)$. Consider the infinite decimal notation for $x$:
$$
x = 0.a_1a_2\ldots, \quad a_i = 0, 1, \ldots, 9, \quad i \in \NN, \tag{55}
$$
where for the numbers with finite amount of decimal places we complete the records with infinite series of 0s. Now select *randomly* one $x$. What can one say about the typical distribution of digits $0, \ldots, 9$ in $x$? To answer the question, consider the following sequence of approximations:
$$
\begin{array}{l} x_0 = 0 \\ x_1 = 0.a_1 \\ \ldots \\ x_n = 0.a_1\ldots a_n \\ \ldots \end{array} \tag{56}
$$

(a) Show that
$$
P\left( \lim_{n \to \infty} \frac{1}{n} I_n(i) = \frac{1}{10} \right) = 1, \quad \forall i, \tag{57}
$$
where $I_n(i)$ gives the number of $i$ digit in $x_n$. The result implies that almost all numbers contain equal (and infinite) amount of all 10 digits. Such numbers are called *normal*.

(b) Check if the rational numbers are normal.

(c) Check if the following number is normal:
$$
x = 0,12345678910111213\ldots \tag{58}
$$
(all integers are written in ascending order).
:::

::: {.solution}

Choose $x$ uniformly from $[0,1)$. The ambiguity of terminating decimal expansions occurs only for a countable set and hence has probability zero.

::: pf

::: {.pf-step #s1-1}

For each fixed digit $i\in\{0,\ldots,9\}$, define
$$
X_k^{(i)}=\mathbf1_{\{a_k=i\}}.
$$
Then the variables $X_k^{(i)}$ are independent Bernoulli variables with parameter $1/10$.


::: pf-proof

For any prescribed digits $d_1,\ldots,d_m$, the set of $x\in[0,1)$ whose first $m$ decimal digits equal this string is a half-open interval of length $10^{-m}$. Therefore
$$
P(a_1=d_1,\ldots,a_m=d_m)=10^{-m}
=\prod_{k=1}^mP(a_k=d_k),
$$
with each marginal probability $1/10$. Thus the decimal digits are independent and uniform, and the indicators have the claimed Bernoulli law.

:::

:::

::: {.pf-step #s1-2}

Since
$$
I_n(i)=\sum_{k=1}^nX_k^{(i)},
$$
the strong law of large numbers gives
$$
P\left(\lim_{n\to\infty}\frac{I_n(i)}n=\frac1{10}\right)=1.
$$


::: pf-proof

The variables in step [](#s1-1){.pf-ref} are iid and integrable with mean $1/10$. The strong law states that their sample averages converge almost surely to their common mean.

:::

:::

::: {.pf-step #s1-3}

In fact, with probability one the limit in step [](#s1-2){.pf-ref} holds simultaneously for all ten digits.


::: pf-proof

For each digit $i$, let $E_i$ be the probability-one event from step [](#s1-2){.pf-ref}. Since there are only ten digits,
$$
P\left(\bigcap_{i=0}^9E_i\right)
=1-P\left(\bigcup_{i=0}^9E_i^c\right)
\geq1-\sum_{i=0}^9P(E_i^c)=1.
$$

:::

:::

::: {.pf-step #s1-4}

A rational number has an eventually periodic decimal expansion.


::: pf-proof

In the long-division algorithm for a rational $a/b$, each successive digit is determined by the current remainder modulo $b$. There are only finitely many possible remainders, so either remainder $0$ occurs, giving a terminating expansion, or a remainder repeats, after which the digits repeat periodically.

:::

:::

::: {.pf-step #s1-5}

Rational numbers are not necessarily normal in the digit-frequency sense used in the problem; for example,
$$
\boxed{1/3=0.333\ldots}
$$
is not normal.


::: pf-proof

For $1/3$, the limiting frequency of digit $3$ is $1$, while the limiting frequency of every other digit is $0$, rather than $1/10$. Thus the class of rational numbers is not contained in the normal numbers. Some specially chosen periodic blocks can have equal single-digit frequencies, so the stronger statement that no rational satisfies this problem's single-digit criterion would be false.

:::

:::

::: {.pf-step #s1-6}

The number in part (c),
$$
0.1234567891011121314\ldots,
$$
obtained by concatenating the positive integers, is normal in base $10$.


::: pf-proof

This is Champernowne's number. To see the required single-digit conclusion directly, consider the concatenation through all $m$-digit integers. There are $9\cdot10^{m-1}$ such integers and hence $9m10^{m-1}$ digit positions in that block. For every non-leading position, each digit occurs exactly equally often. At the leading position, digits $1,\ldots,9$ each occur $10^{m-1}$ times and $0$ never occurs; this discrepancy is only $O(10^{m-1})$, whereas the block length is $\Theta(m10^{m-1})$. Thus each digit's frequency in the $m$-digit block differs from $1/10$ by $O(1/m)$. Earlier blocks contain only $O((m-1)10^{m-2})$ digits, negligible compared with the $m$-digit block. The same estimates remain valid for a terminal partial block of $m$-digit integers, by counting complete cycles in each decimal position, with boundary error $O(m)$ per cycle decomposition. Hence the cumulative frequency of every digit tends to $1/10$. Champernowne's stronger theorem gives normality for every finite block as well.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} answer part (b), and step [](#s1-6){.pf-ref} answers part (c).

:::

:::

:::
