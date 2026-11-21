---
schema: qual/card@1
id: E-MUN-4-2
kind: problem
title: Laws of inequalities for $\RR$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 2; the stored statement matches.
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
    Read against Munkres, Topology (2000), §4 Exercise 2, printed p. 34; the eleven parts
    (a)-(k) are stored as printed, using axioms (1)-(6) and the results of Exercise 1.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.2,
    printed pp. 45-49 (tmp/sources/munkres-solutions-whitman.pdf). His arguments are the
    card's: (e) multiplies x - y > 0 by -z > 0 to get yz > xz, (h) separates the two
    same-sign cases and uses (e) for the mixed one, and (i) rules out 1/x < 0 by
    multiplying x > 0. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: one step per printed part (a)-(k), with
    (h) split into its two same-sign directions and the converse. Axiom (6) was re-read in
    the book's text (tmp/sources/munkres-2000-topology.md, section 4) and the steps cite its
    two clauses as printed; the retained solution's cited pages were not re-read in this
    pass, and the section's exercise page was not re-read either.
---

::: {.exercise}

Prove the following "laws of inequalities" for $\RR$, using axioms (1)-(6) along with the results of Exercise 1:

(a) $x > y$ and $w > z \Rightarrow x + w > y + z$ .

(b) $x > 0$ and $y > 0 \Rightarrow x + y > 0$ and $x \cdot y > 0$ .

(c) $x > 0 \Leftrightarrow -x < 0$ .

(d) $x > y \Leftrightarrow -x < -y$ .

(e) $x > y$ and $z < 0 \Rightarrow xz < yz$ .

(f) $x \neq 0 \Rightarrow x^2 > 0$, where $x^2 = x \cdot x$ .

(g) $-1 < 0 < 1$

(h) $xy > 0 \Leftrightarrow x$ and $y$ are both positive or both negative.

(i) $x > 0 \Rightarrow 1 / x > 0$ .

(j) $x > y > 0 \Rightarrow 1 / x < 1 / y.$

(k) $x < y \Rightarrow x < (x + y) / 2 < y$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.2** (`tmp/sources/munkres-solutions-whitman.pdf`); the eleven arguments below, each written in terms of $x>y\iff x-y>0$ together with axiom (6), are his.

Recall that $x>y$ means $x-y>0$, and that axiom (6) of §4 has two clauses: $x>y$ implies $x+z>y+z$, and $x>y$ with $z>0$ implies $xz>yz$. Also $x<y$ means $y>x$.

::: pf

::: {.pf-step #sum}
(a) $x>y$ and $w>z$ imply $x+w>y+z$.

::: pf-proof
Since $x-y>0$ and $w-z>0$, the first clause of (6) applied twice gives
$$
(x+w)-(y+z)=(x-y)+(w-z)>0,
$$
so $x+w>y+z$.
:::

:::

::: {.pf-step #positive}
(b) $x>0$ and $y>0$ imply $x+y>0$ and $xy>0$.

::: pf-proof
The first clause of (6) with $x>0=y$ and $z=y$ gives $x+y>0+y=y>0$, and the second clause with $x>0$, $y>0$ gives $xy>0\cdot y=0$. These are exactly the two closure statements for the positive reals.
:::

:::

::: {.pf-step #signs}
(c) $x>0\iff -x<0$.

::: pf-proof
$-x<0$ means $0-(-x)>0$, and $0-(-x)=x$ by the laws of algebra of Exercise 1; so $-x<0\iff x>0$.
:::

:::

::: {.pf-step #negation}
(d) $x>y\iff -x<-y$.

::: pf-proof
$-x<-y$ means $(-y)-(-x)>0$, and $(-y)-(-x)=x-y$ by the laws of algebra; so $-x<-y\iff x-y>0\iff x>y$.
:::

:::

::: {.pf-step #negative-multiplier}
(e) $x>y$ and $z<0$ imply $xz<yz$.

::: pf-proof
By step [](#signs){.pf-ref}, $z<0$ gives $-z>0$, and $x-y>0$ by hypothesis. The second clause of (6) multiplies the inequality $x-y>0$ by the positive number $-z$:
$$
0<(x-y)(-z)=yz-xz,
$$
using the laws of algebra. Hence $yz-xz>0$, that is $xz<yz$.
:::

:::

::: {.pf-step #square}
(f) $x\ne0$ implies $x^{2}>0$, where $x^{2}=x\cdot x$.

::: pf-proof
Trichotomy for the order gives $x>0$ or $x<0$ when $x\ne0$. If $x>0$, the second clause of (6) gives $x^{2}=x\cdot x>0\cdot x=0$. If $x<0$, then $-x>0$ by step [](#signs){.pf-ref} and similarly $(-x)^{2}>0$; by the laws of algebra $(-x)^{2}=x^{2}$, so $x^{2}>0$.
:::

:::

::: {.pf-step #one}
(g) $-1<0<1$.

::: pf-proof
By (3) the element $1$ differs from $0$, so step [](#square){.pf-ref} gives $1=1^{2}>0$; then step [](#signs){.pf-ref} gives $-1<0$. Hence $-1<0<1$.
:::

:::

::: {.pf-step #product-sign}
(h) $xy>0$ if and only if $x$ and $y$ are both positive or both negative.

::: pf-proof
The two same-sign directions and the converse.

::: {.pf-step #both-positive}
If $x>0$ and $y>0$, or $x<0$ and $y<0$, then $xy>0$.

::: pf-proof
In the first case the second clause of (6) gives $xy>0\cdot y=0$. In the second case steps [](#signs){.pf-ref} give $-x>0$ and $-y>0$, so $(-x)(-y)>0$ by the first case, and $(-x)(-y)=xy$ by the laws of algebra.
:::

:::

::: {.pf-step #mixed}
If one factor is positive and the other negative, then $xy<0$.

::: pf-proof
Suppose $x>0$ and $y<0$. Step [](#negative-multiplier){.pf-ref} applied to $x>0$ and the negative multiplier $y$ gives $xy<0\cdot y=0$. The case $x<0$, $y>0$ is the same with the factors exchanged, using commutativity.
:::

:::

::: {.pf-step #converse}
If $xy>0$ then the factors have the same sign.

::: pf-proof
Since $xy>0\ne0$ neither factor is $0$. If the signs differed, step [](#mixed){.pf-ref} would give $xy<0$, which trichotomy excludes; so the factors are both positive or both negative, and with step [](#both-positive){.pf-ref} this proves the equivalence.
:::

:::

:::

:::

::: {.pf-step #reciprocal}
(i) $x>0$ implies $1/x>0$.

::: pf-proof
Let $x>0$. By [[E-MUN-4-1]] the reciprocal satisfies $x\cdot(1/x)=1$, so $1/x\ne0$. Were $1/x<0$, then step [](#mixed){.pf-ref} applied to the positive $x$ and the negative $1/x$ would give $x\cdot(1/x)<0$, that is $1<0$, contradicting step [](#one){.pf-ref}. So $1/x>0$.
:::

:::

::: {.pf-step #reciprocal-order}
(j) $x>y>0$ implies $1/x<1/y$.

::: pf-proof
If $x>y>0$ then $x>0$, so $1/x>0$ by step [](#reciprocal){.pf-ref}. By step [](#positive){.pf-ref} $y>0$ and $x>0$ give $xy>0$, hence $1/(xy)>0$ by step [](#reciprocal){.pf-ref}. Multiplying $x-y>0$ by the positive number $1/(xy)$ with the second clause of (6),
$$
0<(x-y)\cdot\frac{1}{xy}=\frac{1}{y}-\frac{1}{x},
$$
the equality being the laws of algebra of Exercise 1. Hence $1/y-1/x>0$, that is $1/x<1/y$.
:::

:::

::: {.pf-step #midpoint}
(k) $x<y$ implies $x< (x+y)/2<y$.

::: pf-proof
Suppose $x<y$. Step [](#sum){.pf-ref} applied to $x<x$ and $x<y$ gives $2x=x+x<x+y$, and applied to $x<y$ and $y<y$ gives $x+y<y+y=2y$. Since $2=1+1$ with $1>0$, step [](#positive){.pf-ref} gives $2>0$, hence $1/2>0$ by step [](#reciprocal){.pf-ref}. Multiplying both inequalities by the positive number $1/2$ with the second clause of (6) gives
$$
x=\frac{2x}{2}<\frac{x+y}{2}<\frac{2y}{2}=y,
$$
as claimed.
:::

:::

:::
:::
