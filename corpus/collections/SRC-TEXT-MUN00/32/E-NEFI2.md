---
schema: qual/card@1
id: E-NEFI2
kind: problem
title: Regular Lindelof spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 32 Exercise 4, printed p. 205,
    and against the proof of Theorem 32.1 (printed p. 200), whose indexing the card copies with a
    countable subcover in place of a countable basis, and Exercise 30.9 (a closed subspace of a
    Lindelof space is Lindelof, printed p. 194). No complete published proof was located, and the
    two sets that reach the exercise state the method without proving it: Ana Emilia de Orellana,
    printed p. 33, writes "it is very similar to the theorem, regular and second countable imply
    normal, so we just need to know that it has a countable basis, for this consider a cover a in
    B_n inside U_n and use the Lindelof condition"; "Doug's World", printed p. 6, writes "follow the
    same line of argument as with Theorem 32.1 but rely on a countable subcovering of the space in
    lieu of a countable basis". The card's proof is the argument both describe, with the
    checklists A <= U and B <= V carried out: this is the collision check: a point of U_m cap V_n
    lies in closure U_m, which the definition of U_m excludes, when m <= n, and in closure V_n,
    which the definition of V_n excludes, when n <= m. The search is recorded in the
    COMPLAINTS.md entry for this batch.
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Rechecked against the located published solution: dbFin, "Section 32: Problem 4 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-4-solution/ (read
    2026-11-10; kept at tmp/sources/dbfin/section-32-normal-spaces/problem-4-solution.txt), and
    against Munkres, Topology (2000), Section 32 Exercise 4, printed p. 205, and Theorem 32.1. The
    dbFin page is the one sentence "The only difference from the proof of the Theorem 32.1 is that
    we construct a countable covering using the Lindelof property of the space instead of its
    countable basis", the same position as Doug's World, printed p. 6; the card's proof is that
    sentence carried out, with the A <= U and B <= V checks. This exercise stays in the
    COMPLAINTS.md entry.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against Munkres, Topology (2000), Section 32 Exercise 4, printed p. 205, and
    found correct. The countable families $U_n\supseteq A$ and $V_n\supseteq B$ exist because a
    closed subspace of a Lindelöf space is Lindelöf (Exercise 30.9) and regularity separates
    each point of $A$ from the closed set $B$ by an open set whose closure misses $B$; the sets
    $U$ and $V$ are open and contain $A$ and $B$ because $a\notin\overline{V_i}$ for every $i$;
    and they are disjoint, a point of $U_m\setminus\bigcup_{i\le m}\overline{V_i}$ that also lay
    in $V_n\setminus\bigcup_{i\le n}\overline{U_i}$ contradicting $m\le n$ through
    $\overline{U_m}$ and $n\le m$ through $\overline{V_n}$. The two inclusions and the
    disjointness are those of the construction in Theorem 32.1, with a countable subcover in place
    of a countable basis. Not checked: the printed folio, the checkout holding only the extraction
    `tmp/sources/munkres-2000-topology.md`, which records page ranges and not folios; and no
    published solution was located in this pass, the two retained sets that reach the exercise
    giving the one-sentence reduction recorded in the earlier events.
---

::: {.exercise}

Show that every regular Lindelöf space is normal.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the countable covers, the two inclusions and the disjointness as separate steps.

Let $X$ be regular and Lindelöf, and let $A,B\subseteq X$ be disjoint closed sets.

::: pf

::: {.pf-step #trivial}
If $A=\varnothing$ or $B=\varnothing$ the sets $X$ and $\varnothing$ are disjoint open sets containing $A$ and $B$.

::: pf-proof
$X$ and $\varnothing$ are open and disjoint, and they contain $A$ and $B$ whatever those sets are; so assume from now on that both are nonempty.
:::

:::

::: {.pf-step #covers}
There are countable families of open sets $U_{n}\supseteq A$, $V_{n}\supseteq B$ with $\overline{U_{n}}\cap B=\varnothing$ and $\overline{V_{n}}\cap A=\varnothing$.

::: pf-proof
Regularity applied to $a\in A$ and the closed set $B$ not containing $a$ gives an open $W_{a}\ni a$ with $\overline{W_{a}}\cap B=\varnothing$. The traces $W_{a}\cap A$ form an open cover of the subspace $A$, and $A$ is Lindelöf: a closed subspace of a Lindelöf space is Lindelöf (Exercise 30.9, printed p. 194). So countably many of them, indexed $U_{n}$, cover $A$, and each satisfies $\overline{U_{n}}\cap B=\varnothing$. The same construction with the roles of $A$ and $B$ exchanged gives the $V_{n}$, using that $B$ is closed hence Lindelöf.
:::

:::

::: {.pf-step #open-sets}
The sets
$$U=\bigcup_{n\ge1}\Big(U_{n}\setminus\bigcup_{i\le n}\overline{V_{i}}\Big),\qquad V=\bigcup_{n\ge1}\Big(V_{n}\setminus\bigcup_{i\le n}\overline{U_{i}}\Big)$$
are open, with $A\subseteq U$ and $B\subseteq V$.

::: pf-proof
Each $\bigcup_{i\le n}\overline{V_{i}}$ is closed, being a finite union of closed sets, so $U_{n}\setminus\bigcup_{i\le n}\overline{V_{i}}$ is open and $U$ is a union of open sets; symmetrically for $V$. If $a\in A$ then $a\in U_{n}$ for some $n$, and $a\notin\overline{V_{i}}$ for every $i$ by step [](#covers){.pf-ref}, so $a\in U$. Symmetrically $B\subseteq V$.
:::

:::

::: {.pf-step #disjoint}
$U\cap V=\varnothing$.

::: pf-proof
Suppose $x\in U\cap V$. Then for some $m$ one has $x\in U_{m}$ and $x\notin\bigcup_{i\le m}\overline{V_{i}}$, and for some $n$ one has $x\in V_{n}$ and $x\notin\bigcup_{i\le n}\overline{U_{i}}$. If $m\le n$, then $x\in U_{m}\subseteq\overline{U_{m}}\subseteq\bigcup_{i\le n}\overline{U_{i}}$, contradicting the second statement; if $n\le m$, then $x\in V_{n}\subseteq\overline{V_{n}}\subseteq\bigcup_{i\le m}\overline{V_{i}}$, contradicting the first. One of the two cases always holds.
:::

:::

::: {.pf-qed}
Disjoint closed sets are separated by the disjoint open sets $U\supseteq A$ and $V\supseteq B$ of steps [](#open-sets){.pf-ref} and [](#disjoint){.pf-ref}, and the empty case is step [](#trivial){.pf-ref}; so $X$ is normal.
:::

:::

:::
