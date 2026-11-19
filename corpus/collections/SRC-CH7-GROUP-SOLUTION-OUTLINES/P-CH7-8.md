---
schema: qual/card@1
id: P-CH7-8
kind: problem
title: Cosets of $\langle a^5\rangle$ in a cyclic group of order $15$
classification:
  areas: [algebra]
  topics:
    - Cosets and Lagrange's Theorem
relations: []
review: draft
audit:
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read against Gallian, Contemporary Abstract Algebra, seventh edition (2010),
      Chapter 7, exercise 8, printed page 149 (PDF page 164). The printed exercise reads
      "Suppose that a has order 15. Find all of the left cosets of <a^5> in <a>", which is
      the card's statement. The card's number agrees with the printed number here and with
      item 8 of the retained outline (assets/attachments/Ch7Sltns.pdf).
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Checked in the text that Lagrange's Theorem (Theorem 7.1, printed page 141) gives the
      number of left cosets as |G|/|H| for a finite group G and subgroup H, and that in a
      cyclic group of order 15 with generator a the elements a^0, ..., a^14 are distinct.
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Restructured into Lamport steps from the retained solution outline for Chapter 7,
      item 8, PDF page 1 (assets/attachments/Ch7Sltns.pdf). The outline lists the five
      cosets and states the count as a remark ("notice that 15/3 = 5"); the steps prove the
      order of a^5 by the order formula for powers, prove the five listed sets are distinct
      by comparing exponents modulo 5, and prove they exhaust <a> rather than invoking
      Lagrange for the covering.
---

::: {.problem}
Suppose that $a$ has order $15$. Find all of the left cosets of $\langle a^{5} \rangle$ in $\langle a \rangle$.
:::

::: {.solution}

The exercise is Gallian, *Contemporary Abstract Algebra* (7th ed.), Chapter 7 exercise 8,
printed p. 149, and is item 8 of the retained Chapter 7 solution outline
(`assets/attachments/Ch7Sltns.pdf`, PDF p. 1). The outline's five cosets are proved below to
be distinct and exhaustive.

Let $G=\langle a\rangle$ with $\cardinality{G}=15$ and $H=\langle a^{5}\rangle$.

::: pf

::: {.pf-step #order}

$H=\ts{e,a^{5},a^{10}}$ has order $3$.

::: pf-proof

The order of $a^{5}$ is $15/\gcd(15,5)=3$: generally $\cardinality{a^{m}}=|a|/\gcd(|a|,m)$
for a cyclic group, and here this is directly checkable, since $(a^{5})^{3}=a^{15}=e$ while
$(a^{5})^{1}=a^{5}\ne e$ and $(a^{5})^{2}=a^{10}\ne e$, the exponents $5,10,15$ all being
less than the order $15$ of $a$ at the first two and equal to it at the third. Hence $H$,
the set of powers $(a^{5})^{k}$, is $\ts{e,a^{5},a^{10}}$, three distinct elements.

:::

:::

::: {.pf-step #list}

For $k=0,1,2,3,4$, the coset $a^{k}H$ is $\ts{a^{k},a^{k+5},a^{k+10}}$.

::: pf-proof

$a^{k}H=\ts{a^{k}h : h\in H}=\ts{a^{k}e,a^{k}a^{5},a^{k}a^{10}}=\ts{a^{k},a^{k+5},a^{k+10}}$
by the laws of exponents. The three exponents $k,k+5,k+10$ are distinct and lie in
$\ts{0,\dots,14}$, so by step [](#order){.pf-ref} times $a^{k}$ each of the three elements
is distinct.

:::

:::

::: {.pf-step #distinct}

The five cosets of step [](#list){.pf-ref} are pairwise distinct.

::: pf-proof

Suppose $a^{j}H=a^{k}H$ with $0\le j,k\le4$. Then $j\equiv k\pmod 5$, because
$a^{j}H=\ts{a^{m} : m\equiv j \pmod 5}$: indeed $a^{j+5t}=a^{j}(a^{5})^{t}\in a^{j}H$ for
every $t$, and the $m$ with $m\equiv j\pmod5$ are exactly the $m=j+5t$; there are three of
them in $\ts{0,\dots,14}$, which is all of $a^{j}H$ by step [](#list){.pf-ref}. Since $j,k$
lie in $\ts{0,\dots,4}$, $j\equiv k\pmod 5$ forces $j=k$.

:::

:::

::: {.pf-step #exhaustive}

Every left coset of $H$ in $G$ is one of the five in step [](#list){.pf-ref}.

::: pf-proof

An element of $G$ is $a^{m}$ with $0\le m\le14$. Write $m=5t+k$ with $0\le k\le4$; then
$a^{m}=a^{k}(a^{5})^{t}\in a^{k}H$. So every element of $G$ lies in one of the five cosets,
hence every left coset — being $a^{m}H\subseteq G$ and nonempty, since it contains
$a^{m}$ — equals the coset $a^{k}H$ containing its element $a^{m}$. This also agrees with
the count $\cardinality{G}/\cardinality{H}=15/3=5$ of Lagrange's Theorem (Theorem 7.1,
printed p. 141).

:::

:::

::: {.pf-step #answer}

The left cosets of $\langle a^{5}\rangle$ in $\langle a\rangle$ are
$\ts{e,a^{5},a^{10}}$, $\ts{a,a^{6},a^{11}}$, $\ts{a^{2},a^{7},a^{12}}$,
$\ts{a^{3},a^{8},a^{13}}$ and $\ts{a^{4},a^{9},a^{14}}$.

::: pf-proof

By step [](#list){.pf-ref} with $k=0,1,2,3,4$ these are the five sets
$H,aH,a^{2}H,a^{3}H,a^{4}H$; by step [](#distinct){.pf-ref} they are distinct and by step
[](#exhaustive){.pf-ref} nothing else is a left coset.

:::

:::

:::

:::
