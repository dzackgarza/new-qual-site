---
schema: qual/card@1
id: P-ZWJ7K
kind: problem
title: 'a. Let $f: \RR \to \RR$.'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - measure-theory
relations: []
review: draft
---

::: problem
a. Let $f: \RR \to \RR$.
Prove that
$$
f(x) \leq \liminf_{y\to x} f(y)~ \text{for each}~ x\in {\RR} \iff \{ x\in {\RR} \mid f(x) > a \}~\text{is open for all}~ a\in {\RR}
$$

b. Recall that a function $f: {\RR} \to {\RR}$ is called *lower semi-continuous* iff it satisfies either condition in part (a) above.

Prove that if $\mathcal{F}$ is any family of lower semi-continuous functions, then
$$
g(x) = \sup\{ f(x) \mid f\in \mathcal{F}\}
$$
is Borel measurable.

> Note that $\mathcal{F}$ need not be a countable family.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. ($\Leftarrow$) If $\{f > a\}$ is open for all $a$, then $f(x) \le \liminf_{y\to x} f(y)$ for all $x$.
    Proof: fix $x$ and $a < f(x)$. Then $x \in \{f > a\}$, which is open, so any sequence $y_n \to x$ lies in $\{f > a\}$ eventually, i.e. $f(y_n) > a$ for all large $n$; hence $\liminf_{y\to x}f(y) \ge a$. Since $a < f(x)$ is arbitrary, $\liminf_{y\to x}f(y) \ge f(x)$.
<1>2. ($\Rightarrow$) If $f(x) \le \liminf_{y\to x}f(y)$ for all $x$, then $\{f > a\}$ is open for all $a$.
    Proof: suppose $\{f > a\}$ is not open for some $a$; then some $x \in \{f > a\}$ is not an interior point, so there is a sequence $y_n \to x$ with $f(y_n) \le a$ for all $n$ (points outside the set approaching $x$). Then $\liminf_{y\to x} f(y) \le a < f(x)$, contradicting the hypothesis.
<1>3. (Part b) $g = \sup_{f\in\mathcal F} f$ satisfies $\{g > a\} = \cup_{f\in\mathcal F}\{f > a\}$.
    Proof: $g(x) > a$ iff $f(x) > a$ for some $f \in \mathcal F$, which is exactly $x \in \cup_{f\in\mathcal F}\{f > a\}$.
<1>4. $g$ is lower semi-continuous, hence Borel measurable.
    Proof: each $\{f > a\}$ is open (<1>1, <1>2, since each $f$ is l.s.c.), so by <1>3, $\{g > a\}$ is an arbitrary union of open sets, hence open. Thus $g$ satisfies the l.s.c. condition, so $g$ is l.s.c.; in particular each $\{g > a\}$ is open, so $g$ is Borel measurable. (No countability of $\mathcal F$ is needed: arbitrary unions of open sets are open.)
<1>5. Q.E.D.
:::
