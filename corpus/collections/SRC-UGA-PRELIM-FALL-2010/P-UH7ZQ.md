---
schema: qual/card@1
id: P-UH7ZQ
kind: problem
title: Negations of statements about odd integers and a sequential limit
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Negate each of the following statements in the most informative way possible (i.e., without using the words "no" or "not").

(a) There is an integer $x$ so that $x + y$ is odd for each integer $y$.

(b) If $x$ is an odd integer, then $xy$ is odd for every integer $y$.

(c) Given $\varepsilon > 0$, there is $N \in \NN$ so that whenever $n > N$, we have $\abs{ \dfrac{2+n}{1+n} - 1 } < \varepsilon$.
:::

::: {.solution}

The three negations are the card's own, obtained by the duality rule for quantifiers; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

::: pf

::: {.pf-step #rule}
Each negation replaces $\forall$ by $\exists$, $\exists$ by $\forall$ and negates the final predicate.

::: pf-proof
A statement is false exactly when its negation is true, so $\lnot\forall x\,P(x)$ holds exactly when $\exists x\,\lnot P(x)$ holds, and $\lnot\exists x\,P(x)$ exactly when $\forall x\,\lnot P(x)$. Applying the two equivalences successively through a string of quantifiers moves the negation inwards past all of them and leaves it on the innermost predicate; this is the only step used below, and it uses no "no" and no "not" in the resulting sentence once the predicate is read off negatively. For the predicate "is even", the negation of "is odd" is "is even" because an integer is even exactly when it is not odd.
:::

:::

::: {.pf-step #a}
(a) For every integer $x$ there is an integer $y$ such that $x+y$ is even.

::: pf-proof
The statement is $\exists x\,\forall y\,\big(x+y\text{ is odd}\big)$, where $y$ ranges over the integers. By step [](#rule){.pf-ref} its negation is $\forall x\,\exists y\,\big(x+y\text{ is even}\big)$, which is the displayed sentence.
:::

:::

::: {.pf-step #b}
(b) There is an odd integer $x$ and an integer $y$ such that $xy$ is even.

::: pf-proof
The statement is $\forall x\,\Big(\big(x\text{ is odd}\big)\Rightarrow\forall y\,\big(xy\text{ is odd}\big)\Big)$, and $P\Rightarrow Q$ is $\lnot P\lor Q$, so its negation is equivalent to $\exists x\,\Big(\big(x\text{ is odd}\big)\land\exists y\,\big(xy\text{ is even}\big)\Big)$, which is the displayed sentence.
:::

:::

::: {.pf-step #c}
(c) There is $\varepsilon>0$ such that for every $N\in\NN$ there is $n>N$ with $\abs{\dfrac{n+2}{n+1}-1}\ge\varepsilon$.

::: pf-proof
The statement is $\forall\varepsilon>0\ \exists N\in\NN\ \forall n\big(n>N\Rightarrow\abs{\frac{2+n}{1+n}-1}<\varepsilon\big)$. Negating as in step [](#rule){.pf-ref} gives $\exists\varepsilon>0\ \exists N$ negated, that is $\exists\varepsilon>0\ \forall N\in\NN\ \exists n\big(n>N\land\abs{\frac{n+2}{n+1}-1}\ge\varepsilon\big)$, since the negation of $P\Rightarrow Q$ is $P\land\lnot Q$ and $\lnot(\abs{\cdot}<\varepsilon)$ is $\abs{\cdot}\ge\varepsilon$. That is the displayed sentence.
:::

:::

:::
:::
