---
schema: qual/card@1
id: E-SS10.EX-4
kind: problem
title: Euler's pentagonal recurrence for the partition function
classification:
  areas:
  - complex-analysis
  topics:
  - Partitions
  - Generating Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The coefficient
    extraction is now a step in its own right, with the k = 0 term separated from the
    rest and the finiteness of the sum traced to p(j) = 0 for j < 0, and the sign
    pattern is derived from the exponent of -1 rather than read off the ordered list
    of pentagonal numbers. Every entry of the table was recomputed here from the
    recurrence (p(0..12) = 1,1,2,3,5,7,11,15,22,30,42,56,77, so p(10) = 42) and each
    of the six values is derived in the card from the previous ones. Not checked: the
    book's own text of the exercise and its statement of Euler's identity, since no
    copy of Stein and Shakarchi is retained in this checkout; the statement is as
    transcribed on the card. No retained solution set covers the exercise (the
    collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
Using the generating formula for $p(n)$, prove the recurrence formula
$$
\begin{aligned}
p(n) &= p(n-1) + p(n-2) - p(n-5) - p(n-7) + \cdots \\
&= \sum_{k\neq0} (-1)^{k+1}\, p\!\left(n - \frac{k(3k+1)}{2}\right),
\end{aligned}
$$
where the right-hand side is the finite sum taken over those $k \in \ZZ$, $k \neq 0$, with $k(3k+1)/2 \leq n$. Use this formula to calculate $p(5), p(6), p(7), p(8), p(9)$, and $p(10)$; check that $p(10) = 42$.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $p(n)$ be the number of partitions of $n$, with $p(0)=1$, and extend by $p(j)=0$ for $j<0$; write
$$
P(q)=\sum_{n\ge0}p(n)q^n=\prod_{m\ge1}(1-q^m)^{-1}
$$
as a formal power series, and put $g(k)=\dfrac{k(3k+1)}{2}$ for $k\in\ZZ$.

::: pf

::: {.pf-step #generating}
$P(q)=\prod_{m\ge1}(1-q^m)^{-1}$ as formal power series.

::: pf-proof
Each factor is $1+q^m+q^{2m}+\cdots$, a formal power series with constant term $1$, so the product is defined coefficient by coefficient: the coefficient of $q^n$ receives contributions only from the finitely many choices of exponents $e_m\ge0$ with $\sum_m me_m=n$. Such a choice is exactly a partition of $n$ written as a sum of $e_m$ copies of $m$, and conversely, so the coefficient of $q^n$ counts partitions of $n$, which is $p(n)$. Note $p(0)=1$, the empty partition.
:::

:::

::: {.pf-step #euler}
$\prod_{m\ge1}(1-q^m)=\sum_{k\in\ZZ}(-1)^{k}q^{g(k)}$, the pentagonal number identity.

::: pf-proof
This is Euler's identity, cited from the generating-function theory of the chapter; the usual form is the same sum with exponent $k(3k-1)/2$, and replacing $k$ by $-k$ there turns it into $g(k)$. Explicitly, the terms for $k\ge1$ are $(-1)^k\bigl(q^{k(3k-1)/2}+q^{k(3k+1)/2}\bigr)$ together with the constant term $1$, so the exponents are $1,2,5,7,12,15,\dots$.
:::

:::

::: {.pf-step #multiply}
$1=P(q)\prod_{m\ge1}(1-q^m)=\Bigl(\sum_{n\ge0}p(n)q^n\Bigr)\Bigl(\sum_{k\in\ZZ}(-1)^{k}q^{g(k)}\Bigr)$.

::: pf-proof
Multiply the identity of step [](#generating){.pf-ref} by the identity of step [](#euler){.pf-ref}: the left sides multiply to $\prod(1-q^m)\cdot\prod(1-q^m)^{-1}=1$, and the right sides multiply as displayed, coefficient by coefficient.
:::

:::

::: {.pf-step #coefficient}
For $n\ge1$ the coefficient of $q^n$ in that product is $p(n)+\sum_{k\ne0}(-1)^{k}p\bigl(n-g(k)\bigr)$, and it is $0$.

::: pf-proof
The coefficient of $q^n$ in a product of two series is the sum $\sum_k p(n-g(k))(-1)^k$ over the $k$ with $g(k)\le n$, a finite set because $g(k)\to\infty$ as $\abs{k}\to\infty$. Splitting off the term $k=0$, where $g(0)=0$ and $(-1)^0=1$, gives $p(n)$ plus the sum over $k\ne0$. Since the product equals $1=q^0$, the coefficient of $q^n$ is $0$ for every $n\ge1$. The convention $p(j)=0$ for $j<0$ is what makes the sum finite in form: a term with $g(k)>n$ contributes $p(n-g(k))=0$.
:::

:::

::: {.pf-step #recurrence}
$p(n)=\sum_{k\ne0}(-1)^{k+1}p\bigl(n-g(k)\bigr)$ for $n\ge1$, that is
$$
p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+\cdots
$$

::: pf-proof
Move the term $p(n)$ of step [](#coefficient){.pf-ref} to the other side: $p(n)=-\sum_{k\ne0}(-1)^kp(n-g(k))=\sum_{k\ne0}(-1)^{k+1}p(n-g(k))$. For the displayed form, order the values $g(k)$, $k\ne0$, increasingly: they are $1,2,5,7,12,15,\dots$, the numbers $k(3k\pm1)/2$. The sign of the term with exponent $g(k)$ is $(-1)^{k+1}$, which is $+$ for $k=\pm1$ (exponents $1,2$), $-$ for $k=\pm2$ (exponents $5,7$), $+$ for $k=\pm3$ (exponents $12,15$), and so on, which gives the displayed series. Only terms with $g(k)\le n$ occur.
:::

:::

::: {.pf-step #table}
$p(0),p(1),p(2),p(3),p(4)=1,1,2,3,5$ and $p(5),p(6),p(7),p(8),p(9),p(10)=7,11,15,22,30,42$, so in particular $p(10)=42$.

::: pf-proof
From $p(0)=1$ and step [](#recurrence){.pf-ref}, each with only the terms whose exponent is at most $n$: $p(1)=p(0)=1$; $p(2)=p(1)+p(0)=2$; $p(3)=p(2)+p(1)=3$; $p(4)=p(3)+p(2)=5$. Then
$$
p(5)=p(4)+p(3)-p(0)=5+3-1=7,
$$
$$
p(6)=p(5)+p(4)-p(1)=7+5-1=11,\qquad p(7)=p(6)+p(5)-p(2)-p(0)=11+7-2-1=15,
$$
$$
p(8)=p(7)+p(6)-p(3)-p(1)=15+11-3-1=22,\qquad p(9)=p(8)+p(7)-p(4)-p(2)=22+15-5-2=30,
$$
$$
p(10)=p(9)+p(8)-p(5)-p(3)=30+22-7-3=42 .
$$
Each line uses the exponents $1,2,5,7$ as they become available, with $p(j)=0$ for $j<0$ absorbing the missing terms, and the last line gives $p(10)=42$ as the exercise asks.
:::

:::

:::

:::
