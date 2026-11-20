---
schema: qual/card@1
id: E-KK77N
kind: problem
title: Locally metrizable regular Lindelof spaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology - Chapter 4
    Solutions" (30 August 2017), Problem 34.8, printed p. 12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 34: Problem 8 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-8-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-8-solution.txt); checked
    against Munkres, Topology (2000), Section 34 Exercise 8, printed p. 218, Exercise 30.9 and
    Exercise 30.5(b). The argument is the card's, and it answers the printed question about where
    regularity is used: to shrink a metrizable neighbourhood to one whose closure is closed in the
    Lindelof space, hence Lindelof and metrizable, hence second countable. What was corrected: the
    source writes "Since a closed subspace of a Lindeof space is Lindeof, cl(V_x) is Lindeof" and
    then "Since V_x is a subspace of U_x, it is metrizable. By exercise 30.5(b), cl(V_x) is second
    countable", applying 30.5(b) to the open subspace V_x where the argument gives it for the closed
    one, and then citing Theorem 30.2 for the passage to V_x; the card keeps the two steps separate.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed and every citation is made by
    its numbered statement --- §34 Exercise 8, §34 Exercise 7 for the definition of locally
    metrizable, Lemma 31.1(a), Theorem 30.2, §16 Exercise 1, Theorem 7.5, §20 and Theorem 34.1 ---
    each read in `tmp/sources/munkres-2000-topology.md`; Doug's World's Problem 34.8 is named by
    its problem number. The earlier events keep their text (QUAL-11); the numbered citations here
    supersede their page locators. No step or answer changes.

---

::: {.exercise}

Show that a regular Lindelöf space is metrizable if it is locally metrizable.
[Hint: A closed subspace of a Lindelöf space is Lindelöf.] Regularity is essential; where do you use it in the proof?
:::

::: {.solution}

The argument is transcribed from two located published solutions: "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017), Problem 34.8 (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`), and dbFin, "Section 34: Problem 8 Solution" (`tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-8-solution.txt`). Both run the book's hint: shrink a metrizable neighbourhood so its closure is a closed subspace of the Lindelöf space, hence Lindelöf and metrizable, hence second countable; both then cover $X$ by such open sets, pass to a countable subcover, and take the union of the countable bases. Where the card departs from them: Doug's World writes that $\overline{V_{x}}$ is second countable by Exercise 30.5(b) and then that $V_{x}$ is, by Theorem 30.2, running the two applications together; steps [](#closed-second-countable){.pf-ref} and [](#V-basis){.pf-ref} separate them, the first being the Lindelöf-metric argument for the closed subspace and the second the passage to its open subspace. dbFin's closing counterexample at $\RR_{K}$ is not reproduced here, since the printed question asks only where regularity is used. The statement was checked against Munkres, *Topology* (2000), §34 Exercise 8, with the definition of locally metrizable in §34 Exercise 7, Lemma 31.1(a), Theorem 30.2, §16 Exercise 1, and the Urysohn metrization theorem, Theorem 34.1.

Throughout, $X$ is regular and Lindelöf, and $X$ is locally metrizable: each point has a neighbourhood that is metrizable in the subspace topology.

::: pf

::: {.pf-step #neighbourhoods}
For each $x\in X$ there are an open set $U_{x}$ and a metrizable subspace $N_{x}$ of $X$ with $x\in U_{x}\subset N_{x}$.

::: pf-proof
Local metrizability gives a neighbourhood $N_{x}$ of $x$ that is metrizable as a subspace; being a neighbourhood, it contains an open set $U_{x}$ about $x$.
:::

:::

::: {.pf-step #shrinking}
For each $x\in X$ there is an open set $V_{x}$ with $x\in V_{x}\subset\overline{V_{x}}\subset U_{x}$.

::: pf-proof
This is Lemma 31.1(a): in a regular space, for a point $x$ and a neighbourhood $U_{x}$ of it there is a neighbourhood $V_{x}$ of $x$ whose closure lies in $U_{x}$. Taking $V_{x}$ open is no loss, since any neighbourhood of $x$ contains an open one, and shrinking only decreases the closure.
:::

:::

::: {.pf-step #closed-lindelof}
$\overline{V_{x}}$ is Lindelöf.

::: pf-proof
$\overline{V_{x}}$ is a closed subspace of the Lindelöf space $X$. If $\mathcal{U}$ is a cover of it by sets open in $X$, then $\mathcal{U}\cup\theset{X-\overline{V_{x}}}$ is an open cover of $X$, which has a countable subcover because $X$ is Lindelöf; discarding $X-\overline{V_{x}}$ leaves a countable subcollection of $\mathcal{U}$ covering $\overline{V_{x}}$.
:::

:::

::: {.pf-step #closed-metrizable}
$\overline{V_{x}}$ is metrizable.

::: pf-proof
$\overline{V_{x}}\subset N_{x}$ by step [](#shrinking){.pf-ref} and step [](#neighbourhoods){.pf-ref}. A subspace of a metric space is a metric space under the restricted metric: the balls of the restriction are the intersections of the balls of $N_{x}$ with $\overline{V_{x}}$, and balls form a basis for the topology of $N_{x}$ (§20), so they form a basis for the subspace topology. The topology $\overline{V_{x}}$ inherits from $N_{x}$ agrees with the one it inherits from $X$ because the subspace topology is transitive (§16 Exercise 1).
:::

:::

::: {.pf-step #closed-second-countable}
$\overline{V_{x}}$ has a countable basis.

::: pf-proof
A Lindelöf metric space is second countable: for each $n\geq1$ the cover by balls of radius $1/n$ has a countable subcover, by the Lindelöf property, and the union over $n$ of these countably many countable families is a countable family of balls; it is a basis, because for a point $x$ and $\varepsilon>0$ one takes $n$ with $2/n<\varepsilon$ and a ball $B(y,1/n)$ of the $n$-th subcover containing $x$, and then $x\in B(y,1/n)\subset B(x,\varepsilon)$ by the triangle inequality. Apply this to the Lindelöf metric space $\overline{V_{x}}$ of steps [](#closed-lindelof){.pf-ref} and [](#closed-metrizable){.pf-ref}.
:::

:::

::: {.pf-step #V-basis}
Each $V_{x}$ has a countable basis.

::: pf-proof
$V_{x}$ is open in $\overline{V_{x}}$, hence a subspace of it, and a subspace of a second-countable space is second-countable by Theorem 30.2; the intersections of the countably many basic open sets of $\overline{V_{x}}$ with $V_{x}$ form a countable basis for $V_{x}$.
:::

:::

::: {.pf-step #countable-subcover}
Some countable subfamily of $\theset{V_{x}\mid x\in X}$ covers $X$.

::: pf-proof
$\theset{V_{x}}$ is an open cover of $X$ by step [](#shrinking){.pf-ref}, and $X$ is Lindelöf, so it has a countable subcover, say $V_{x_{1}},V_{x_{2}},\ldots$.
:::

:::

::: {.pf-step #basis-for-X}
The union of countable bases $\mathcal{B}_{i}$ of the sets $V_{x_{i}}$ is a countable basis for $X$.

::: pf-proof
Let $\mathcal{B}\coloneqq\bigcup_{i}\mathcal{B}_{i}$, countable as a countable union of countable sets (Theorem 7.5). Each $B\in\mathcal{B}_{i}$ is open in $V_{x_{i}}$, and $V_{x_{i}}$ is open in $X$, so $B=V_{x_{i}}\cap O$ for some open $O\subset X$ and $B$ is open in $X$. Given a point $x$ and an open set $O$ containing it, step [](#countable-subcover){.pf-ref} gives $i$ with $x\in V_{x_{i}}$, the set $O\cap V_{x_{i}}$ is a neighbourhood of $x$ in $V_{x_{i}}$, and $\mathcal{B}_{i}$ being a basis for $V_{x_{i}}$ gives $B\in\mathcal{B}_{i}$ with $x\in B\subset O\cap V_{x_{i}}\subset O$. So $\mathcal{B}$ meets the criterion for a basis.
:::

:::

::: pf-step
Therefore $X$ is metrizable.

::: pf-proof
Step [](#basis-for-X){.pf-ref} exhibits a countable basis for $X$, and $X$ is regular by hypothesis, so the Urysohn metrization theorem (Theorem 34.1) makes $X$ metrizable. Regularity is used twice. First, in step [](#shrinking){.pf-ref}, it produces $V_{x}$ with $\overline{V_{x}}\subset U_{x}\subset N_{x}$: that containment is what lets the closed set $\overline{V_{x}}$ be metrizable while remaining a closed subspace of the Lindelöf space $X$, and without it a neighbourhood $U_{x}$ of $x$ inside the metrizable $N_{x}$ need not have a smaller neighbourhood whose closure still lies in $N_{x}$, so that no closed metrizable subspace at $x$ would be available. Second, it is a hypothesis of the Urysohn metrization theorem itself in this last step, where the countable basis of step [](#basis-for-X){.pf-ref} is converted into a metric; second countability alone does not give metrizability without it.
:::

:::

:::

:::
