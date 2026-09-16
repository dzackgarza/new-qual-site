---
schema: qual/card@1
id: E-SMI-8000E-MT1
kind: problem
title: Zorn's lemma and maximal ideals containing a nonunit
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both parts with the Smith Math 8000 Fall 2006 midterm."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Stated Zorn's lemma and applied it to the poset of proper ideals containing (x), verifying chain unions are proper upper bounds and that maximality in this poset is maximal-ideal maximality."
---

::: {.exercise}
(a) State Zorn's lemma.

(b) Prove that in a commutative ring $R$ with identity 1, if $x$ is any nonunit, there exists a proper maximal ideal of $R$ containing $x$.
:::

::: {.solution}
<1>1. State Zorn's lemma.
::: {.proof}
Zorn's lemma says:

> If a nonempty partially ordered set has the property that every chain has
> an upper bound in the set, then the partially ordered set contains a
> maximal element.

Here a chain means a totally ordered subset, and a maximal element means an
element which is not strictly below any other element of the poset.
:::

<1>2. The principal ideal $(x)$ is proper.
::: {.proof}
If
$$
(x)=R,
$$
then
$$
1=rx
$$
for some $r\in R$, so $x$ would be a unit. This contradicts the hypothesis.
Hence
$$
(x)\ne R.
$$
:::

<1>3. Set up the Zorn poset.
::: {.proof}
Let
$$
\mathcal P
=\{I\trianglelefteq R:(x)\subseteq I\subsetneq R\},
$$
ordered by inclusion. By step <1>2,
$$
(x)\in\mathcal P,
$$
so $\mathcal P$ is nonempty.
:::

<1>4. Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.
::: {.proof}
Let
$$
\mathcal C\subseteq\mathcal P
$$
be a chain and set
$$
J=\bigcup_{I\in\mathcal C}I.
$$
Because $\mathcal C$ is totally ordered by inclusion, $J$ is an ideal: if
$a,b\in J$, then $a\in I_1$ and $b\in I_2$ for some
$I_1,I_2\in\mathcal C$; after interchanging them if necessary,
$I_1\subseteq I_2$, so $a,b\in I_2$ and therefore
$a-b\in I_2\subseteq J$. Also $ra\in J$ for every $r\in R$ and
$a\in J$.

Every member of $\mathcal C$ contains $(x)$, hence so does $J$. Finally,
$J$ is proper. Indeed, if $1\in J$, then $1$ belongs to some
$I\in\mathcal C$, which would force $I=R$, contradicting
$I\in\mathcal P$.

Thus
$$
J\in\mathcal P
$$
and $J$ is an upper bound for the chain.
:::

<1>5. Apply Zorn's lemma and prove the maximal element is a maximal ideal of $R$.
::: {.proof}
By steps <1>3--<1>4 and Zorn's lemma, $\mathcal P$ has a maximal element
$M$. Then
$$
(x)\subseteq M\subsetneq R,
$$
so in particular
$$
x\in M.
$$

Suppose
$$
M\subsetneq J\subsetneq R
$$
for some ideal $J$ of $R$. Since $(x)\subseteq M\subseteq J$, the ideal
$J$ would be another member of $\mathcal P$ strictly containing $M$, which
contradicts maximality of $M$ in $\mathcal P$.

Therefore no proper ideal strictly contains $M$, so $M$ is a maximal ideal
of $R$. Hence
$$
\boxed{\text{every nonunit }x\in R\text{ lies in a proper maximal ideal}.}
$$
:::
:::
