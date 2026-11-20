---
schema: qual/card@1
id: P-MSLD5
kind: problem
title: Negation of a mixed-quantifier statement and a flawed inductive characterization
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps, two for the negation and three for the flawed induction, each carrying a
    `pf-proof`; both answers are unchanged. Cited by number only: the quantifier rules for
    negating $\exists$, $\forall$ and a conjunction, and the principle of induction on the
    natural numbers. Checked: that the variables $m,S_m,\alpha_m,f_m$ are data and not bound in
    the negation, that $T=\ZZ_{>0}$ with $m=3$ satisfies both numbered conditions and is not
    $\{n:n\ge3\}$, and that the induction gives exactly the inclusion $\{n\ge m\}\subseteq T$.
---

::: {.problem}
a. Suppose that for each positive integer $m$, we have a set $S_m$ of real numbers, a real number $\alpha_m$, and a real function $f_m$.
Formulate the negation of this statement: "There exists a positive integer $m$ such that for every $x \in S_m$, $x \ge \alpha_m$ and $f_m(x) = 0$."
b. The following statement is not valid: "For any positive integer $m$, if $T$ is a set of positive integers such that (1) $m \in T$ and (2) $n \in T$ implies $n+1 \in T$, then $T = \{\text{positive integers } n : n \ge m\}$."
Explain and correct the flaw.
:::

::: {.solution}

::: pf

::: pf-step

(a) The statement is
$$
\exists m\in\ZZ_{>0}\;\forall x\in S_m,
\bigl(x\ge \alpha_m\ \text{and}\ f_m(x)=0\bigr),
$$
and its negation is
$$
\forall m\in\ZZ_{>0}\;\exists x\in S_m
\quad\text{such that}\quad
x<\alpha_m\ \text{or}\ f_m(x)\ne0.
$$

::: pf-proof

The quantifier symbols transcribe the sentence word for word: 'there exists a positive integer $m$' is $\exists m\in\ZZ_{>0}$, 'for every $x\in S_m$' is $\forall x\in S_m$, and the two conditions form a conjunction. The negation is obtained in three steps, each negating the outermost connective: $\neg\exists m=\forall m\neg$, $\neg\forall x=\exists x\neg$, and $\neg(P\wedge Q)=\neg P\vee\neg Q$, which turns $x\ge\alpha_m$ into $x<\alpha_m$ and $f_m(x)=0$ into $f_m(x)\ne0$. The variables $m$, $S_m$, $\alpha_m$, $f_m$ are part of the given data and are not quantified over in the negation.

:::

:::

::: pf-step

(b) The flaw is that conditions (1) and (2) force $T$ to contain every integer $n\ge m$, but they do not forbid $T$ from also containing positive integers smaller than $m$.

::: pf-proof

Nothing in (1) or (2) refers to integers below $m$ except through the implication of (2), which is vacuous at $n$ whose successor is not required to be in $T$ unless $n$ already is. So a set satisfying (1) and (2) may contain such integers, and the claimed conclusion $T=\{n:n\ge m\}$ fails for them.

:::

:::

::: pf-step

For example, with $m=3$ the set of all positive integers satisfies (1) and (2), but is not $\{n:n\ge3\}$.

::: pf-proof

The set $T=\ZZ_{>0}$ contains $3=m$, and $n\in T$ implies $n+1\in T$ because every positive integer is in $T$; so (1) and (2) hold. But $1\in T$ and $1<3$, so $T\ne\{n\in\ZZ_{>0}:n\ge m\}$. Hence the statement as printed is false, not merely unproved.

:::

:::

::: pf-step

The correct conclusion from (1) and (2) is
$$
\{n\in\ZZ_{>0}:n\ge m\}\subseteq T,
$$
since induction on $r\ge0$ gives $m+r\in T$.

::: pf-proof

$m\in T$ by (1). If $m+r\in T$ for some $r\ge0$, (2) applied to $n=m+r$ gives $m+r+1\in T$. By induction on $r$, $m+r\in T$ for every $r\ge0$, and every integer $n\ge m$ is $m+(n-m)$ with $n-m\ge0$. This is the inclusion, and it is the most that (1) and (2) give.

:::

:::

::: pf-step

To obtain equality, add the hypothesis
$$
T\subseteq\{n\in\ZZ_{>0}:n\ge m\};
$$
then the two inclusions give $T=\{n\in\ZZ_{>0}:n\ge m\}$.

::: pf-proof

The added hypothesis excludes exactly the integers below $m$ that step 3 shows may be present. With it, step 4 gives one inclusion and the hypothesis the other, so the two sets are equal; conversely a set equal to $\{n:n\ge m\}$ satisfies the hypothesis, so the corrected statement is true.

:::

:::

::: pf-step

So the negation of (a) is the displayed formula, and the statement of (b) becomes true when either the conclusion is weakened to the inclusion or the hypothesis $T\subseteq\{n\ge m\}$ is added.

::: pf-proof

Part (a) is steps 1--2 and part (b) steps 3--5; the two repairs of (b) are the two ways of making the printed conclusion follow from the printed hypotheses.

:::

:::

:::
:::
