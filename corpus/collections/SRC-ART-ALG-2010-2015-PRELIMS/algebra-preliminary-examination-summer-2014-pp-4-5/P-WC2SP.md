---
schema: qual/card@1
id: P-WC2SP
kind: problem
title: Units of a local ring, nonarchimedean valuation rings, and $R/M^n$
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the three parts and all absolute-value axioms with Summer 2014 problem 3 in the retained extraction; the problem belongs to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked maximal-ideal existence, closure and unique maximality of the valuation ideal including a trivial absolute value, and every maximal ideal above M^n."
---
::: {.problem}
A local ring is a commutative ring with $1$ which has a unique maximal ideal.

(a) Show that the group of units of a local ring is precisely the set of elements lying outside of $M$.

(b) Let $F$ be a field, and $\abs{ \ } : F \longrightarrow \RR$ such that

(i) $\abs{x} \geq 0$ for all $x \in F$ and $\abs{x} = 0$ if and only if $x = 0$;

(ii) $\abs{xy} = \abs{x}\abs{y}$, for all $x, y \in F$;

(iii) $\abs{x + y} \leq \max\{\abs{x}, \abs{y}\}$, for all $x, y \in F$.

Show that the set $R = \{x \in F : \abs{x} \leq 1\}$ is a local ring.

(c) Let $M$ be a maximal ideal of a commutative ring $R$ with $1$ and $n$ be a positive integer.
Show that $R/M^n$ is a local ring.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $A$ is a local ring with unique maximal ideal $M$, then
$A^\times=A\setminus M$.

::: pf-proof

A unit cannot lie in a proper ideal: if $u\in I$ and $u$ is a
unit, then $1=u^{-1}u\in I$. Thus no element of $M$ is a unit.

Conversely, if $a\in A$ is not a unit, then $(a)$ is proper.
Every proper ideal of a commutative unital ring is contained in
a maximal ideal. To recall the argument, order the proper ideals
containing $(a)$ by inclusion. The union of any nonempty chain is
an ideal containing $(a)$ and remains proper, since membership
of $1$ in that union would put $1$ in a member of the chain.
Zorn's lemma gives a maximal element, which is a maximal ideal
of $A$ [@DF04]. By uniqueness it is $M$, so $a\in M$.

:::

:::

::: {.pf-step #s2}

In part (b), $R$ is local with unique maximal ideal
$$
\mathfrak m=\{x\in F:\abs{x}<1\}.
$$

::: pf-proof

The axioms imply $\abs{0}=0$ and $\abs{1}>0$. Multiplicativity gives
$\abs{1}=\abs{1}^2$, hence $\abs{1}=1$. Also $\abs{-1}^2=\abs{1}=1$ and
$\abs{-1}\geq0$, so $\abs{-1}=1$ and $\abs{-x}=\abs{x}$.

The set $R$ contains $0,1$. For $x,y\in R$,
$\abs{x-y}\leq\max\{\abs{x},\abs{y}\}\leq1$ and
$\abs{xy}=\abs{x}\abs{y}\leq1$. Thus $R$ is a commutative unital subring
of $F$. The set $\mathfrak m$ contains zero, is closed under
subtraction by the same inequality, and satisfies
$\abs{rx}=\abs{r}\abs{x}<1$ for $r\in R$, $x\in\mathfrak m$.
It is an ideal of $R$, proper because $\abs{1}=1$.

For $x\ne0$, multiplicativity gives $\abs{x^{-1}}=1/\abs{x}$.
Consequently an element $x\in R$ is a unit in $R$ exactly
when $\abs{x}=1$: in that case its inverse lies in $R$, and
conversely $xy=1$ with $x,y\in R$ forces $\abs{x}=\abs{y}=1$.
Thus every element of $R\setminus\mathfrak m$ is a unit.
An ideal strictly containing $\mathfrak m$ contains such a
unit and hence is all of $R$, proving maximality.
Every proper ideal contains no unit, so is contained in
$\mathfrak m$. This proves uniqueness. The argument also
covers the trivial absolute value, when $R=F$ and
$\mathfrak m=(0)$.

:::

:::

::: {.pf-step #s3}

In part (c), the unique maximal ideal of $R/M^n$ is $M/M^n$.

::: pf-proof

Since $n\geq1$, one has $M^n\subseteq M\ne R$.
Moreover,
$$
(R/M^n)/(M/M^n)\cong R/M
$$
is a field, so $M/M^n$ is maximal [@DF04].

Let $\mathfrak n$ be any maximal ideal of $R/M^n$, and let
$N\subset R$ be its inverse image under the quotient map.
Then $M^n\subseteq N$ and $R/N\cong(R/M^n)/\mathfrak n$
is a field. In particular $N$ is a proper prime ideal.
For each $m\in M$, one has $m^n\in M^n\subseteq N$.
Primality, applied repeatedly to this product of $n$ copies
of $m$, gives $m\in N$. Hence $M\subseteq N$.
Maximality of $M$ and properness of $N$ give $N=M$, so
$\mathfrak n=M/M^n$. Thus no other maximal ideal exists.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a)--(c), respectively.

:::

:::

:::
