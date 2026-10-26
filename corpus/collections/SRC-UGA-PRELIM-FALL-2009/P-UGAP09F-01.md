---
schema: qual/card@1
id: P-UGAP09F-01
kind: problem
title: Formalize, negate, and take the converse of a quantified implication
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Consider the following statement about real numbers:

> If $x\le0$ and $x<y$, then there is a real number $z$ such that $xz>y$.

(a) Using logical symbols, write the statement in symbolic form, including all implicit quantifiers.

(b) Write its negation in verbal form without using the word "not."

(c) Write its converse in verbal form.
:::

Let
$$
P(x,y)\coloneqq (x\le 0)\land(x<y),
\qquad
Q(x,y)\coloneqq \exists z\in\RR\;(xz>y).
$$

::: pf

::: pf-step

The symbolic form of the statement is
$$
\boxed{\forall x\in\RR\;\forall y\in\RR\;
\bigl(P(x,y)\to Q(x,y)\bigr).}
$$


::: pf-proof

The original sentence makes an assertion for arbitrary real numbers $x$ and $y$, so both are universally quantified. Its hypothesis is $P(x,y)$, and its conclusion is that there exists a real number $z$ satisfying $xz>y$, which is $Q(x,y)$.

:::

:::

::: pf-step

The negation, without using the word "not," is: there exist real numbers $x$ and $y$ such that $x\le0$ and $x<y$, and for every real number $z$ one has $xz\le y$.


::: pf-proof

By step <1>1,
$$
\neg\!\left(\forall x\in\RR\;\forall y\in\RR\;(P(x,y)\to Q(x,y))\right)
$$
is equivalent to
$$
\exists x\in\RR\;\exists y\in\RR\;
\bigl(P(x,y)\land\neg Q(x,y)\bigr),
$$
because $\neg(A\to B)$ is equivalent to $A\land\neg B$. Moreover,
$$
\neg Q(x,y)
=
\neg\!\left(\exists z\in\RR\;(xz>y)\right)
\iff
\forall z\in\RR\;(xz\le y).
$$
Translating this last formula into words gives the sentence in the claim.

:::

:::

::: pf-step

The converse is: for all real numbers $x$ and $y$, if there is a real number $z$ such that $xz>y$, then $x\le0$ and $x<y$.


::: pf-proof

The converse of an implication $A\to B$ is $B\to A$. Thus the converse of the formula in step <1>1 is
$$
\forall x\in\RR\;\forall y\in\RR\;
\bigl(Q(x,y)\to P(x,y)\bigr),
$$
which is exactly the verbal statement in the claim.

:::

:::

::: pf-qed

Step <1>1 answers part (a), step <1>2 answers part (b), and step <1>3 answers part (c).

:::

:::
