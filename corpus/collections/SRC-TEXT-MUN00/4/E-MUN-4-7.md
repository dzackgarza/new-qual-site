---
schema: qual/card@1
id: E-MUN-4-7
kind: problem
title: Extending the laws of exponents to all integers
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 7, printed p. 35; the definition
    a^0 = 1, a^{-n} = 1/a^n and the request to extend all three laws to integer
    exponents are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.7,
    printed pp. 54-58 (tmp/sources/munkres-solutions-whitman.pdf). He separates the sign
    cases for the addition law and uses the identity 1/a^n = (1/a)^n, which he proves
    first; the card takes the shorter route through the same identity, writing
    a^r a^{-q} = a^r/a^q and splitting on r >= q, and it derives the reciprocal laws it
    needs from Exercise 4.1(m). The case coverage is the same: both signs, zero, and
    each composite case.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's existing prose into numbered steps without changing the mathematics; the
    case analysis is the card's shorter route, which its introduction contrasts with Whitman's
    case-by-case treatment (Exercise 4.7, printed pp. 54-58). Checked: the two sign cases of the
    addition law, the induction for the power law, the product law, and that no step divides by
    zero. Not checked: the cited pages, because tmp/sources holds no copy of the Whitman manual
    and the Munkres text is not retained in this VM.
---

::: {.exercise}

Let $a \in \RR$ and $a \neq 0$ . Define $a^0 = 1$, and for $n \in \ZZ_+$, $a^{-n} = 1 / a^n$ . Show that the laws of exponents hold for $a, b \neq 0$ and $n, m \in \ZZ$ .
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.7, printed ps 54-58, which the card cites; it is restructured into numbered steps below. The card reaches the same cases by the shorter route of comparing $r$ with $q$ in $a^r/a^q$, and that route is the one structured here; the three laws are $a^ra^s=a^{r+s}$, $(a^r)^s=a^{rs}$ and $(ab)^r=a^rb^r$, for $a,b\neq0$ and $r,s\in\ZZ$, with $a^0=1$ and $a^{-n}=1/a^n$ for $n>0$.

::: pf

::: {.pf-step #bothneg}

$a^{-r}a^{-s}=a^{-(r+s)}$ for $r,s>0$, and $a^ra^s=a^{r+s}$ for $r,s>0$ is the addition law for positive exponents.

::: pf-proof

For positive $r,s$, $a^{-r}a^{-s}=\frac{1}{a^{r}}\frac{1}{a^{s}}=\frac{1}{a^{r}a^{s}}=\frac{1}{a^{r+s}}=a^{-(r+s)}$, using the definition of negative powers and the addition law for positive exponents.

:::

:::

::: {.pf-step #mixed}

$a^{r}a^{-q}=a^{r-q}$ for $r\geq0$ and $q>0$.

::: pf-proof

$a^{r}a^{-q}=\frac{a^{r}}{a^{q}}$. If $r\geq q$ then $a^{r}=a^{r-q}a^{q}$ by the addition law for nonnegative exponents, and the quotient is $a^{r-q}$; if $r<q$ then $a^{q}=a^{r}a^{q-r}$, and the quotient is $\frac{1}{a^{q-r}}=a^{-(q-r)}=a^{r-q}$.

:::

:::

::: {.pf-step #addlaw}

$a^{r}a^{s}=a^{r+s}$ for all $r,s\in\ZZ$.

::: pf-proof

Steps [](#bothneg){.pf-ref} and [](#mixed){.pf-ref} cover the three sign cases up to the order of the factors, and $a^0a^{s}=a^{s}$ is immediate from $a^0=1$; multiplication in $\RR$ is commutative, so the remaining case follows from $a^{s}a^{r}=a^{r+s}$.

:::

:::

::: {.pf-step #powlaw}

$(a^{r})^{s}=a^{rs}$ for all $r,s\in\ZZ$.

::: pf-proof

For $s>0$, repeated application of step [](#addlaw){.pf-ref} gives $(a^{r})^{s}=a^{rs}$; for $s=0$ both sides are $1$; for $s=-q<0$, $(a^{r})^{s}=\frac{1}{(a^{r})^{q}}=\frac{1}{a^{rq}}=a^{-rq}=a^{rs}$.

:::

:::

::: {.pf-step #prodlaw}

$(ab)^{r}=a^{r}b^{r}$ for all $r\in\ZZ$.

::: pf-proof

For $r>0$ this is the law for positive exponents; for $r=0$ both sides are $1$; for $r=-q<0$, $(ab)^{-q}=\frac{1}{(ab)^{q}}=\frac{1}{a^{q}b^{q}}=a^{-q}b^{-q}$, using that $a,b\neq0$ makes the quotients defined.

:::

:::

::: {.pf-step #done}

All three laws of exponents hold for $a,b\neq0$ and integer exponents.

::: pf-proof

Steps [](#addlaw){.pf-ref}, [](#powlaw){.pf-ref} and [](#prodlaw){.pf-ref}.

:::

:::

:::

:::
