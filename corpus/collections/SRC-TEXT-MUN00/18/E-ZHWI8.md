---
schema: qual/card@1
id: E-ZHWI8
kind: problem
title: The set where f is at most g is closed
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Order Topology
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 8, printed pp. 111-112, with the
    pasting lemma on printed p. 108; both parts are stored as printed, including the
    bracketed hint to (b).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.8, PDF p. 12. From them: the two cases for the
    openness of {g < f}, according to whether an element lies between g(a) and f(a) or f(a)
    is its immediate successor, and the pasting of f on {f <= g} with g on {g <= f}. Their
    second case needs the observation that g(x) <= g(a) < f(a) <= f(x), which the card
    supplies; their union is indexed by Y and not by X. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked both parts against Munkres §18 Exercise 8,
    printed pp. 111-112, and Theorem 18.3 (pasting lemma, printed p. 108): the two cases for
    the openness of {g < f} according to whether an element lies strictly between g(a) and
    f(a) or f(a) is its immediate successor, the supplied inequality g(x) <= g(a) < f(a) <=
    f(x) in the second case, and the pasting of f on {f <= g} with g on {g <= f} over a
    finite closed cover. positron0802, Exercise 18.8, PDF p. 12, with their union corrected
    from c in X to c in Y; Whitman, printed pp. 184-185, agrees. The printed statement
    needed no repair.
---

::: {.exercise}

Let $Y$ be an ordered set in the order topology.
Let $f, g: X \to Y$ be continuous.

(a) Show that the set $\theset{x \mid f(x) \leq g(x)}$ is closed in $X$.

(b) Let $h: X \to Y$ be the function

$$
h(x) = \min\theset{f(x), g(x)}.
$$

Show that $h$ is continuous.
[Hint: Use the pasting lemma.]
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.8** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two cases of (a) and the pasting argument of (b) are theirs, one step of their second case is supplied below, and one index set is corrected: their union is taken over $c\in Y$, not over $c\in X$. Whitman, §18 Exercise 8, proves (a) with the set of elements having an immediate successor and the same two cases, and (b) by the same pasting lemma.

Throughout, $Y$ is an ordered set in the order topology and $f,g:X\to Y$ are continuous.

::: pf

::: {.pf-step #part-a}
(a) $C=\{x\mid f(x)\le g(x)\}$ is closed in $X$.

:::: pf-proof

::: {.pf-step #a-first-case}
Let $a\in U=X-C$, so $g(a)<f(a)$, and suppose some $c\in Y$ satisfies $g(a)<c<f(a)$. Then $a$ has a neighbourhood contained in $U$.

::: pf-proof
The sets $(-\infty,c)=\{y\in Y\mid y<c\}$ and $(c,+\infty)=\{y\in Y\mid y>c\}$ are open in the order topology, so $g^{-1}\big((-\infty,c)\big)$ and $f^{-1}\big((c,+\infty)\big)$ are open in $X$ because $g$ and $f$ are continuous; their intersection $N$ is an open set containing $a$, since $g(a)<c<f(a)$. For $x\in N$ we have $g(x)<c<f(x)$, hence $g(x)<f(x)$ and $x\in U$. So $N\subset U$.
:::

:::

::: {.pf-step #a-second-case}
Let $a\in U$ and suppose no $c\in Y$ satisfies $g(a)<c<f(a)$. Then $f(a)$ is the immediate successor of $g(a)$, and $a$ has a neighbourhood contained in $U$.

::: pf-proof
That no element lies strictly between $g(a)$ and $f(a)$, together with $g(a)<f(a)$, says exactly that $f(a)$ is the immediate successor of $g(a)$ in $Y$. The set
$$
N=g^{-1}\big((-\infty,f(a))\big)\cap f^{-1}\big((g(a),+\infty)\big)
$$
is open in $X$ and contains $a$, because $g(a)<f(a)$ puts $g(a)$ in $(-\infty,f(a))$ and $f(a)$ in $(g(a),+\infty)$. Let $x\in N$; then $g(x)<f(a)$ and $f(x)>g(a)$. If $g(x)>g(a)$ then $g(a)<g(x)<f(a)$ would put $g(x)$ strictly between, which the hypothesis excludes; so $g(x)\le g(a)$. If $f(x)<f(a)$ then $g(a)<f(x)<f(a)$ would do the same; so $f(x)\ge f(a)$. Hence $g(x)\le g(a)<f(a)\le f(x)$, and $x\in U$. So $N\subset U$.
:::

:::

::: {.pf-step #a-conclusion}
$U$ is open in $X$ and $C$ is closed.

::: pf-proof
Let $a\in U$. By trichotomy exactly one of the two hypotheses of steps [](#a-first-case){.pf-ref} and [](#a-second-case){.pf-ref} holds at $a$: either some element of $Y$ lies strictly between $g(a)$ and $f(a)$, or none does. In either case $a$ has a neighbourhood contained in $U$. So $U$ is open in $X$, and its complement $C=\{x\mid f(x)\le g(x)\}$ is closed.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) $h(x)=\min\{f(x),g(x)\}$ is continuous.

:::: pf-proof

::: {.pf-step #b-cover}
With $A=\{x\mid f(x)\le g(x)\}$ and $B=\{x\mid g(x)\le f(x)\}$, the sets $A$ and $B$ are closed in $X$, $A\cup B=X$, and $A\cap B=\{x\mid f(x)=g(x)\}$.

::: pf-proof
$A$ is closed by step [](#part-a){.pf-ref} and $B$ is closed by the same step applied to the pair $(g,f)$. For each $x$ one of $f(x)\le g(x)$ and $g(x)\le f(x)$ holds by trichotomy, so $A\cup B=X$; and $x$ lies in both exactly when $f(x)\le g(x)\le f(x)$, that is $f(x)=g(x)$.
:::

:::

::: {.pf-step #b-paste}
The map $h$ is the pasting of $f\restriction_{A}$ and $g\restriction_{B}$ and is continuous.

::: pf-proof
On $A$ one has $h(x)=f(x)$, since $f(x)\le g(x)$ there; on $B$ one has $h(x)=g(x)$. So $h$ is well defined by these two formulas, the two formulas agree on $A\cap B$ by step [](#b-cover){.pf-ref}, and $A\cup B=X$. The restrictions $f\restrict_{A}$ and $g\restrict_{B}$ are continuous, the sets $A$ and $B$ are closed in $X$, and the family $\{A,B\}$ is finite, so the pasting lemma (Theorem 18.3) gives that $h$ is continuous.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Step [](#b-paste){.pf-ref} shows that $h(x)=\min\{f(x),g(x)\}$ is continuous, which is the assertion of (b).
:::

:::

:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref} are the two assertions of the exercise.
:::

:::

:::
:::
