---
schema: qual/card@1
id: E-L3F4O
kind: exercise
title: Middle-thirds Cantor set is compact, totally disconnected, perfect, and null;
  Borel–Cantelli lemma
classification:
  areas:
  - real-analysis
  topics:
  - Cantor Set
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Show that that Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.

- Prove the Borel-Cantelli lemma.
:::

::: {.solution}
<1>1. The Cantor middle-thirds set is compact.
<2>1. Write $C = \bigcap_{n \ge 0} C_n$, where $C_0 = [0,1]$ and $C_n$ is obtained from $C_{n-1}$ by deleting the open middle third of each constituent interval.
::: {.proof}
definition of the Cantor middle-thirds construction.
:::
<2>2. Each $C_n$ is a finite union of $2^n$ closed intervals of length $3^{-n}$, hence compact.
::: {.proof}
deleting an open middle third replaces an interval by two closed intervals, so the number of intervals doubles and their length divides by $3$ at each step.
:::
<2>3. $C$ is compact.
::: {.proof}
$C$ is a closed subset of the compact set $C_0$.
:::
<2>4. Q.E.D.
::: {.proof}
<2>3.
:::

<1>2. The Cantor set has outer measure zero.
<2>1. $m^*(C_n) = (2/3)^n$ for every $n$.
::: {.proof}
$C_n$ is a union of $2^n$ intervals of length $3^{-n}$ by <1>1<2>2. <2>2. $m^*(C) \le m^*(C_n) = (2/3)^n$ for every $n$.
:::
::: {.proof}
$C \subseteq C_n$ and outer measure is monotone.
:::
<2>3. $m^*(C) = 0$.
::: {.proof}
$(2/3)^n \to 0$ as $n \to \infty$ in <2>2.
:::

<1>3. The Cantor set is totally disconnected.
<2>1. $C$ contains no interval of positive length.
::: {.proof}
an interval of positive length inside $C$ would force $m^*(C) \ge m^*(I) > 0$, contradicting <1>2. <2>2. Any two distinct points $x < y$ of $C$ are separated by a gap of $C$.
:::
::: {.proof}
the ternary expansions of $x$ and $y$ (using the convention that ends in all $2$'s at ambiguous points) first differ at some digit, where one of them has a $1$; a $1$ in the $n$-th ternary digit places the point in a middle third removed at stage $n$, and the open interval between the two stage-$n$ intervals containing $x$ and $y$ is disjoint from $C$ and separates them.
:::
<2>3. Q.E.D.
::: {.proof}
if a connected subset of $C$ contained two distinct points, it would have to cross the gap of <2>2 and would then contain a nondegenerate interval of $C$, contradicting <2>1.
:::

<1>4. The Cantor set is perfect: every point is a limit point of $C$.
<2>1. Fix $x \in C$ and $n \ge 1$.
The stage-$n$ interval $I^{(n)} \ni x$ splits into two closed halves separated by the middle third removed at stage $n+1$, and $x$ lies in one of the halves.
::: {.proof}
$x \in C \subseteq C_{n+1}$, and the removed middle third is open, so $x$ is not inside it.
:::
<2>2. The other half contains a point of $C$ different from $x$.
::: {.proof}
the other half is a stage-$(n+1)$ interval whose ternary digits are all $0$ or $2$; completing them by $0$'s produces a point of $C$ lying in that half.
:::
<2>3. Any point of the other half is at distance at least $3^{-(n+1)}$ from $x$.
::: {.proof}
the two halves are separated by the removed middle third, of length $3^{-(n+1)}$.
:::
<2>4. Q.E.D.
::: {.proof}
as $n \to \infty$ the distances $3^{-(n+1)}$ tend to $0$, so <2>2 and <2>3 give points of $C \setminus \{x\}$ arbitrarily close to $x$.
:::

<1>5. Borel–Cantelli lemma: if $(E_n)$ is a sequence of measurable sets with $\sum_n \mu(E_n) < \infty$, then $\mu(\limsup_n E_n) = 0$.
<2>1. $\limsup_n E_n = \bigcap_N \bigcup_{n \ge N} E_n$ is measurable.
::: {.proof}
countable unions and intersections of measurable sets are measurable.
:::
<2>2. $\mu\left(\bigcup_{n \ge N} E_n\right) \le \sum_{n \ge N} \mu(E_n)$ for every $N$.
::: {.proof}
countable subadditivity.
:::
<2>3. $\mu(\limsup_n E_n) \le \sum_{n \ge N} \mu(E_n)$ for every $N$.
::: {.proof}
$\limsup_n E_n \subseteq \bigcup_{n \ge N} E_n$, so monotonicity and <2>2 apply.
:::
<2>4. $\sum_{n \ge N} \mu(E_n) \to 0$ as $N \to \infty$.
::: {.proof}
the partial sums of $\sum_n \mu(E_n)$ converge, so the tails tend to $0$.
:::
<2>5. Q.E.D.
::: {.proof}
<2>3 and <2>4 force $\mu(\limsup_n E_n) \le 0$.
:::

<1>6. Q.E.D.
::: {.proof}
<1>1–<1>4 establish compactness, total disconnectedness, perfectness, and outer measure zero; <1>5 proves the Borel–Cantelli lemma.
:::
:::
