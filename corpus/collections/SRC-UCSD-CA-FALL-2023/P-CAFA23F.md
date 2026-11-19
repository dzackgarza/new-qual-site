---
schema: qual/card@1
id: P-CAFA23F
kind: problem
title: "Zeros of partial sums of the exponential function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card had part (b) as prose outside the proof block and part
    (a) as a single pf-step with no pf-proof child, which is not the layout the filter expects:
    both parts are now steps with their justifications. The mathematics is unchanged and was
    checked: the tail bound uses |z|/(N+i) <= c, the factorial inequality gives (ce)^{N+1} up to
    the factor (N/(N+1))^{N+1} < 1, and with c = 1/(4e) one gets ce = 1/4 and ce^{1+c} < 1/3,
    whence the quotient is below 1. Added: the convergence of the geometric series at c < 1, the
    two elementary inequalities 1/(4e) < 1/4 and e^{1/2} < 4/3 needed for the numerical bound,
    and the compactness argument converting 'finite intersection with every compact set' into
    'no accumulation point'. Not claimed: a retained solution set; the collection's provenance
    is the examination paper only.
---

::: {.problem}
For each $N \in \NN$, let $P_N(z) = \sum_{n=0}^{N} \frac{z^n}{n!}$.

(a) Show that the set $Z = \{z \in \CC \mid P_N(z) = 0 \text{ for some } N \in \NN\}$ is **discrete** (has no accumulation points in $\CC$).

(b) Find a constant $c > 0$ such that $P_N(z)$ has no zeros in $\{z \in \CC \mid \abs{z} < cN\}$.
*(You may use the inequality $n! > e^{-n} n^n$.)*
:::

::: {.solution}
Throughout $P_{N}(z) = \sum_{n=0}^{N}z^{n}/n!$, $R_{N} \coloneqq e^{z} - P_{N}(z) = \sum_{n \ge N+1}z^{n}/n!$ is the tail of the exponential series, $Z = \theset{z \in \CC \mid P_{N}(z) = 0 \text{ for some } N}$, and $c \coloneqq 1/(4e)$. The collection's `provenance` is the Fall 2023 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #tail}
For $\abs{z} \le cN$ with $N \ge 1$ one has $\abs{R_{N}(z)} \le \frac{\abs{z}^{N+1}}{(N+1)!}\cdot\frac{1}{1-c}$.

::: pf-proof
Bound the tail term by term: $\abs{R_{N}(z)} \le \sum_{n \ge N+1}\abs{z}^{n}/n! = \frac{\abs{z}^{N+1}}{(N+1)!}\sum_{j \ge 0}\frac{\abs{z}^{j}}{(N+2)(N+3)\cdots(N+1+j)}$, and each factor $\abs{z}/(N+i)$ with $i \ge 2$ is at most $\abs{z}/N \le c$ because $\abs{z} \le cN$. So the inner sum is at most $\sum_{j \ge 0}c^{j} = 1/(1-c)$, which converges since $c < 1$.

:::

:::

::: {.pf-step #factorial}
$\frac{\abs{z}^{N+1}}{(N+1)!} < (ce)^{N+1}$ for $\abs{z} \le cN$.

::: pf-proof
The given inequality $(N+1)! > e^{-(N+1)}(N+1)^{N+1}$ gives $\frac{\abs{z}^{N+1}}{(N+1)!} < \frac{(cN)^{N+1}e^{N+1}}{(N+1)^{N+1}} = (ce)^{N+1}\bigl(\frac{N}{N+1}\bigr)^{N+1} < (ce)^{N+1}$, since $N/(N+1) < 1$.

:::

:::

::: {.pf-step #exponential}
$\abs{e^{z}} \ge e^{-cN}$, and hence $\frac{\abs{R_{N}(z)}}{\abs{e^{z}}} < \frac{ce}{1-c}\bigl(ce^{1+c}\bigr)^{N}$ for $\abs{z} \le cN$.

::: pf-proof
$\abs{e^{z}} = e^{\operatorname{Re}z} \ge e^{-\abs{z}} \ge e^{-cN}$ because $\operatorname{Re}z \ge -\abs{z}$ and the exponential is increasing. Dividing the bound of step [](#tail){.pf-ref}, sharpened by step [](#factorial){.pf-ref}, by $e^{-cN}$ gives $\frac{(ce)^{N+1}e^{cN}}{1-c} = \frac{ce}{1-c}(ce\cdot e^{c})^{N}$.

:::

:::

::: {.pf-step #no-zeros}
(b) With $c = 1/(4e)$ that quotient is less than $1$ for every $N \ge 1$, so $P_{N}$ has no zero in $\abs{z} < cN$.

::: pf-proof
Here $ce = 1/4$ and $ce^{1+c} = \frac14e^{1/(4e)} \le \frac14e^{1/2} < \frac13$, using $1/(4e) < 1/2$ and $e^{1/2} < 4/3$; so the quotient is at most $\frac{1/4}{1-1/(4e)}\cdot\frac13 < \frac{1/4}{3/4}\cdot\frac13 = \frac19 < 1$, where $1 - 1/(4e) > 3/4$ because $1/(4e) < 1/4$. Hence $\abs{R_{N}(z)} < \abs{e^{z}}$ on $\abs{z} \le cN$; if $P_{N}(z) = 0$ there, then $e^{z} = R_{N}(z)$ and $\abs{e^{z}} = \abs{R_{N}(z)}$, a contradiction.

:::

:::

::: {.pf-step #discrete}
(a) For every compact $K \subseteq \CC$ the set $Z \cap K$ is finite, so $Z$ has no accumulation point in $\CC$.

::: pf-proof
Let $K$ be compact and $R$ large enough that $K \subseteq \overline{D(0,R)}$. By step [](#no-zeros){.pf-ref} a zero of $P_{N}$ has modulus at least $cN$, so if $N > R/c$ then $P_{N}$ has no zero in $K$; only the finitely many $N \le R/c$ can contribute, and each $P_{N}$ has at most $N$ zeros, being a polynomial of degree $N$. So $Z \cap K$ is finite. If $\zeta$ were an accumulation point of $Z$, the compact set $\overline{D(0,\abs{\zeta}+1)}$ would contain $\zeta$ and infinitely many points of $Z$.

:::

:::

::: pf-step
The two answers: $Z$ is discrete, and $P_{N}$ has no zero in $\abs{z} < \frac{N}{4e}$ for every $N \ge 1$.

::: pf-proof
Step [](#discrete){.pf-ref} is (a) and step [](#no-zeros){.pf-ref} is (b) with the explicit constant $c = 1/(4e)$.

:::

:::

:::
:::
