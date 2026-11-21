---
schema: qual/card@1
id: E-3SU0X
kind: problem
title: Quotient topology on a three-point image of the line
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 1, printed p. 144, with Example 3 of
    §22 and its Figure 22.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.1, PDF p. 27. The six preimages are computed
    and the three that are open in R give the topology {empty, A, {a}, {b}, {a,b}}, which is
    the one in Figure 22.3. The published list of proper subsets of A is printed with {a,b}
    replaced by {a,c} twice; the card lists all six. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, with the source left as the retained set it was
    transcribed from. Re-checked each step: the quotient topology consists exactly of the $U$ with
    $p^{-1}(U)$ open, and $p$ is surjective; the six preimages are read off the three cases of the
    definition, unions giving the two-element ones; the first three are open and the three
    containing $0$ with a closed side are not; and the four open sets with $\varnothing$ and $A$
    form the topology of Figure 22.3. Added: the claim that the four sets form a topology, which
    the prose left as a citation of the figure, and the surjectivity of $p$. The earlier
    `solution-written` event's note that the set prints $\{a,c\}$ twice is unchanged and is why
    the card lists all six. Not claimed: a printed publication, the source being a posted
    solution set.
---

::: {.exercise}

Check the details of Example 3 of §22: for the map $p: \RR \to A = \theset{a, b, c}$ defined by

$$
p(x) =
\begin{cases}
a & \text{if } x > 0, \\
b & \text{if } x < 0, \\
c & \text{if } x = 0,
\end{cases}
$$

determine the quotient topology on $A$ induced by $p$.
:::

::: {.solution}
The retained published solution is **positron0802, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.1** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the computation of the six preimages is its, with its list of the proper subsets of $A$ corrected.

::: pf

::: {.pf-step #criterion}
A subset $U\subseteq A$ is open in the quotient topology on $A$ if and only if $p^{-1}(U)$ is open in $\RR$.

::: pf-proof
The quotient topology on $A$ consists, by definition, of the subsets $U$ with $p^{-1}(U)$ open in $\RR$, where $p$ is the given surjection: $p$ is surjective because $a,b,c$ all have preimages.
:::

:::

::: {.pf-step #preimages}
The preimages of the six proper nonempty subsets of $A$ are
$$
p^{-1}(\{a\})=(0,\infty),\quad p^{-1}(\{b\})=(-\infty,0),\quad p^{-1}(\{a,b\})=\RR\setminus\{0\},
$$
$$
p^{-1}(\{c\})=\{0\},\quad p^{-1}(\{a,c\})=[0,\infty),\quad p^{-1}(\{b,c\})=(-\infty,0].
$$

::: pf-proof
Reading the definition of $p$ off the three cases: $p(x)=a$ exactly for $x>0$; $p(x)=b$ exactly for $x<0$; $p(x)=c$ exactly for $x=0$. A preimage of a union of values is the union of the preimages of the values, which gives the three two-element cases, and the three one-element cases are the displayed intervals and points.
:::

:::

::: {.pf-step #open-ones}
Of these, the open ones are $(0,\infty)$, $(-\infty,0)$ and $\RR\setminus\{0\}$; the sets $\{0\}$, $[0,\infty)$ and $(-\infty,0]$ are not open in $\RR$.

::: pf-proof
An open interval is open in the usual topology of $\RR$, and $\RR\setminus\{0\}=(-\infty,0)\cup(0,\infty)$ is a union of open sets. The interval $[0,\infty)$ is not open because no ball about $0$ lies in it; $(-\infty,0]$ fails for the same reason; and $\{0\}$ is not open.
:::

:::

::: {.pf-step}
$\boxed{\mathcal{T}=\{\varnothing,\ A,\ \{a\},\ \{b\},\ \{a,b\}\}}$, which is the topology drawn in Figure 22.3 of §22.

::: pf-proof
The empty set and $A$ have preimages $\varnothing$ and $\RR$, both open. Steps [](#preimages){.pf-ref} and [](#open-ones){.pf-ref} then admit exactly the three subsets $\{a\}$, $\{b\}$, $\{a,b\}$ as proper nonempty open sets, since a subset is open exactly when its preimage is. Collected with $\varnothing$ and $A$ they form a topology on the three-point set $A$: it is closed under unions and finite intersections, as one checks on the four listed sets. That is the topology of the quotient drawn in Figure 22.3 of §22.
:::

:::

:::
:::
