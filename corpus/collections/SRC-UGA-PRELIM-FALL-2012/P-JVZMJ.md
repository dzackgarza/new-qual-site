---
schema: qual/card@1
id: P-JVZMJ
kind: problem
title: Smooth negations of a quantified inequality, the extreme value theorem, and
  a biconditional
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
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the three negations already on the card, all of which are
    correct: the non-strict bound in (a), the explicit interval and function quantifiers in (b),
    and the two disjuncts of the negated biconditional in (c). Added: the general rules the
    three parts apply, the derivation of the negated matrix in each part, the note that a closed
    interval in R is exactly [a,b] with a <= b, and the verification that 'n^2 + 4 is not prime'
    and 'n^2 + 4 is composite' say the same thing for every integer n, since n^2 + 4 >= 4 > 1.
    Nothing was weakened. Not claimed: a retained solution set; the collection's provenance is
    the examination paper only.
---

::: {.problem}
Write the negations of these sentences in as "smooth" a way as possible.
(In particular, you may not simply append "It is not the case that ...". Also, you should make explicit any "hidden" quantifiers.)

(a) There is a real number $x$ such that for every real number $y$, $\abs{x-y}>1$.

(b) A real-valued function that is continuous on a closed interval attains a minimum value on that interval.

(c) $3n+1$ is even if and only if $n^2+4$ is prime.
:::

::: {.solution}
Each part is negated by pushing the negation through the connectives: $\lnot\exists$ becomes $\forall\lnot$, $\lnot\forall$ becomes $\exists\lnot$, $\lnot(A \land B)$ becomes $\lnot A \lor \lnot B$, and $\lnot(A \iff B)$ becomes $(A \land \lnot B) \lor (\lnot A \land B)$. The collection's `provenance` is the Fall 2012 examination paper, and no solutions sheet accompanies it, so the negations below are the card's own.

::: pf

::: {.pf-step #a}
(a) For every real $x$ there is a real $y$ with $\abs{x-y} \le 1$.

::: pf-proof
The sentence is $\exists x \in \RR\\ \forall y \in \RR:\\ \abs{x-y} > 1$. Its negation is $\forall x \in \RR\\ \exists y \in \RR:\\ \lnot(\abs{x-y} > 1)$, and $\lnot(\abs{x-y} > 1)$ is $\abs{x-y} \le 1$ because the absolute value is a real number and the order on $\RR$ is total. This is the smoothest form: the bound is non-strict and no 'not' remains.

:::

:::

::: {.pf-step #b-quantifiers}
(b) The original assertion, with its hidden quantifiers explicit, is: for every pair of reals $a \le b$ and every continuous $f\colon[a,b] \to \RR$ there is $x \in [a,b]$ with $f(x) \le f(y)$ for all $y \in [a,b]$.

::: pf-proof
The original names a function, an interval and a value without quantifying any of them: 'a real-valued function continuous on a closed interval attains a minimum on that interval' is a universally quantified statement about the function and the interval, and 'attains a minimum' is the assertion that some point of the interval has the least value. Closed intervals in $\RR$ are exactly the sets $[a,b]$ with $a \le b$.

:::

:::

::: {.pf-step #b}
(b) There are reals $a \le b$ and a continuous $f\colon[a,b] \to \RR$ such that for every $x \in [a,b]$ there is $y \in [a,b]$ with $f(y) < f(x)$.

::: pf-proof
Negating step [](#b-quantifiers){.pf-ref}: the leading two universal quantifiers become existential, and the assertion 'there is a minimiser' becomes 'every point fails to be a minimiser'. Formally the negated matrix is $\lnot\exists x\\ \forall y:\\ f(x) \le f(y)$, that is $\forall x\\ \exists y:\\ \lnot(f(x) \le f(y))$, and $\lnot(f(x) \le f(y))$ is $f(y) < f(x)$. The statement is smooth in this form: it says the function has no least value, which is what failing to attain a minimum means.

:::

:::

::: {.pf-step #c}
(c) There is an integer $n$ such that either $3n+1$ is even and $n^{2}+4$ is not prime, or $3n+1$ is odd and $n^{2}+4$ is prime.

::: pf-proof
The sentence is a biconditional in the free variable $n$, so with the hidden quantifier over the integers it reads $\forall n \in \ZZ:\\ (P(n) \iff Q(n))$ with $P(n)$: '$3n+1$ is even' and $Q(n)$: '$n^{2}+4$ is prime'. The negation is $\exists n \in \ZZ:\\ (P(n) \land \lnot Q(n)) \lor (\lnot P(n) \land Q(n))$, and $\lnot P(n)$ is '$3n+1$ is odd' because an integer is even or odd and not both.

:::

:::

::: {.pf-step #c-composite}
The clause '$n^{2}+4$ is not prime' may be written '$n^{2}+4$ is composite'.

::: pf-proof
For an integer $n$ one has $n^{2}+4 \ge 4 > 1$, so if $n^{2}+4$ is not prime it has a divisor other than $1$ and itself, that is it is composite. This is the substitution the card makes, and it is exact for every integer $n$.

:::

:::

::: pf-step
The three smooth negations are: (a) $\forall x\\,\exists y:\\ \abs{x-y} \le 1$; (b) $\exists a \le b$ and continuous $f$ on $[a,b]$ such that $\forall x \in [a,b]\\ \exists y \in [a,b]: f(y) < f(x)$; (c) $\exists n \in \ZZ$ for which exactly one of '$3n+1$ is even', '$n^{2}+4$ is prime' holds.

::: pf-proof
Steps [](#a){.pf-ref}, [](#b){.pf-ref} and [](#c){.pf-ref} give the three negations, with the hidden quantifiers made explicit in steps [](#b-quantifiers){.pf-ref} and [](#c){.pf-ref} and the arithmetic identification of step [](#c-composite){.pf-ref}.

:::

:::

:::
:::
