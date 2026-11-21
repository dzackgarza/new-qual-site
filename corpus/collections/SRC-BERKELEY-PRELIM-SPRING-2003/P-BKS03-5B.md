---
schema: qual/card@1
id: P-BKS03-5B
kind: problem
title: Distance between a compact set and a closed set is attained
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2003
    prelim solutions, Problem 5B, PDF p. 5, the file named in the collection's provenance),
    now cited on the body; the card previously carried no citation. One repair: the sheet,
    and the card after it, asserted that $D\cap B_{R_1}$ is nonempty without argument, and
    that nonemptiness is what makes the truncated product a nonempty compact set on which the
    minimum is attained. Step 4 now proves it from the definition of $d_0$ together with the
    reverse triangle inequality, and the infimum over the truncated product is shown equal to
    $d_0$ in both cases (infimum attained or not). The statement is unchanged, including its
    hypothesis that $D$ be closed and $C$ closed and bounded.
---

::: {.problem}
Let $C,D\subseteq\RR^n$ be nonempty closed sets and assume $C$ is bounded.
Prove there exist $x_0\in C$ and $y_0\in D$ such that
$$
d(x_0,y_0)\le d(x,y)
$$
for all $x\in C$ and $y\in D$.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2003 prelim solutions, Problem 5B** (`assets/attachments/s03solution.pdf`, the file named in this collection's `provenance`): the reduction to the bounded case, the truncating ball $B_{R_1}$ with $R_1=R_0+d_0+\varepsilon$, and the final compactness argument are that solution's. The card repairs one step of it: the sheet says "it follows that $D\cap B_{R_1}$ is non-empty" without proof, whereas that nonemptiness is what makes the truncated product nonempty; the argument is supplied in step [](#nonempty){.pf-ref} below.

Throughout $C,D\subseteq\RR^n$ are nonempty, $C$ is closed and bounded and $D$ is closed, $d$ is the Euclidean metric, and
$$
d_0\coloneqq\inf\theset{d(x,y)\mid x\in C,\ y\in D}\in[0,\infty).
$$

::: pf

::: {.pf-step #bounded}
$d:C\times D\to\RR$ is continuous, and if $C$ and $D$ are both bounded the minimum is attained.

::: pf-proof
$d(x,y)=\abs{x-y}$ is continuous on $\RR^n\times\RR^n$, and the topology of $C\times D$ is the subspace topology, so the restriction is continuous. If both factors are bounded and closed, $C\times D$ is closed and bounded in $\RR^{2n}$, hence compact, and a continuous real function on a compact set attains its minimum (the extreme value theorem for metric spaces).

:::

:::

::: {.pf-step #truncate}
There is $R_0$ with $C\subseteq B_{R_0}$, and for $\varepsilon>0$ and $R_1=R_0+d_0+\varepsilon$: if $y\notin B_{R_1}$ then $d(x,y)>d_0+\varepsilon$ for every $x\in C$.

::: pf-proof
$C$ is bounded, so it lies in some closed ball $B_{R_0}$ about the origin. For $x\in C$ and $y\notin B_{R_1}$ we have $\abs x\le R_0<\abs y$, so by the reverse triangle inequality
$$
d(x,y)=\abs{y-x}\ge\abs y-\abs x>R_1-R_0=d_0+\varepsilon .
$$

:::

:::

::: {.pf-step #nonempty}
$D\cap B_{R_1}\ne\varnothing$.

::: pf-proof
$d_0$ is the infimum of a nonempty set of nonnegative reals, so there are $x\in C$ and $y\in D$ with $d(x,y)<d_0+\varepsilon/2$. Then
$$
\abs y\le\abs x+d(x,y)\le R_0+d_0+\tfrac{\varepsilon}{2}<R_0+d_0+\varepsilon=R_1,
$$
so this $y$ lies in $D\cap B_{R_1}$. (The same conclusion holds with $\varepsilon$ in place of $\varepsilon/2$ if the infimum is attained, so the argument covers both cases.)

:::

:::

::: {.pf-step #same-infimum}
$\inf\theset{d(x,y)\mid x\in C,\ y\in D\cap B_{R_1}}=d_0$.

::: pf-proof
The set on the left is a subset of the set defining $d_0$, so its infimum is at least $d_0$. For the reverse inequality, let $\delta>0$; by the definition of $d_0$ there are $x\in C$, $y\in D$ with $d(x,y)<d_0+\min(\delta,\varepsilon/2)$, and by step [](#truncate){.pf-ref} such a $y$ must lie in $B_{R_1}$, since otherwise $d(x,y)>d_0+\varepsilon\ge d_0+\min(\delta,\varepsilon/2)$. So the left-hand infimum is at most $d_0$.

:::

:::

::: {.pf-step #attained}
There is $(x_0,y_0)\in C\times(D\cap B_{R_1})$ with $d(x_0,y_0)=d_0$, and it satisfies $d(x_0,y_0)\le d(x,y)$ for all $x\in C$, $y\in D$.

::: pf-proof
$C$ is closed and bounded, so compact; $D\cap B_{R_1}$ is closed (an intersection of closed sets) and bounded, so compact; hence $C\times(D\cap B_{R_1})$ is compact and nonempty by step [](#nonempty){.pf-ref}. By step [](#bounded){.pf-ref} the continuous $d$ attains its minimum there, say at $(x_0,y_0)$, and that minimum is the infimum computed in step [](#same-infimum){.pf-ref}, namely $d_0$. Since $d_0$ is the infimum over all of $C\times D$, $d(x_0,y_0)=d_0\le d(x,y)$ for every $(x,y)\in C\times D$.

:::

:::

:::
:::
