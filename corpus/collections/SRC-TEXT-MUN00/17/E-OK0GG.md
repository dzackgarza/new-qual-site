---
schema: qual/card@1
id: E-OK0GG
kind: problem
title: Closure behavior under unions
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 6, printed p. 101, with Theorem 17.5
    on printed p. 97; the stored statement is the printed one, including the demand for an
    example in (c).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.6, PDF p. 7, for (a), (b) and the
    counterexample to equality in (c), which is the family of one-point sets of rationals:
    their union is Q and its closure is R, while each of them is closed. Whitman's printed
    p. 162 has the same two inclusions and the example of the intervals (1/n, 2], which the
    note records. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 with (a), (b), (c) as steps and the counterexample to the converse of (c) as a step of its own. Re-checked Theorem 17.5 (printed p. 97) for the characterization of the closure used in (a) and (b). No statement change.
---

::: {.exercise}

Let $A$, $B$, and $A_\alpha$ denote subsets of a space $X$.
Prove the following:

(a) If $A \subset B$, then $\overline{A} \subset \overline{B}$.

(b) $\overline{A \cup B} = \overline{A} \cup \overline{B}$.

(c) $\overline{\bigcup A_\alpha} \supset \bigcup \overline{A}_\alpha$; give an example where equality fails.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.6, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); (a) and (b) are theirs, with Whitman's printed p. 162 supplying the same two arguments in neighbourhood form; the counterexample to the converse of (c) is theirs. Whitman's example for (c) on printed p. 162 is the family $A_{n}=(1/n,2]$ in $\RR$, whose union is $(0,2]$: the point $0$ lies in its closure and in no $\overline{A_{n}}$.

Throughout, $\overline{A}$ is the closure of $A$ in $X$: a closed set containing $A$ and contained in every closed set containing $A$ (Theorem 17.5, printed p. 97).

::: pf

::: {.pf-step #monotone}

If $A\subset B$ then $\overline{A}\subset\overline{B}$.

::: pf-proof

$B$ is a closed set containing $A$, so $\overline{A}\subset B$; and $\overline{B}$ is a closed set containing $A$, since $A\subset B\subset\overline{B}$, so $\overline{A}\subset\overline{B}$.

:::

:::

::: pf-step

$\overline{A\cup B}=\overline{A}\cup\overline{B}$.

::: pf-proof

Since $A\subset A\cup B$ and $B\subset A\cup B$, step [](#monotone){.pf-ref} gives $\overline{A}\subset\overline{A\cup B}$ and $\overline{B}\subset\overline{A\cup B}$, hence $\overline{A}\cup\overline{B}\subset\overline{A\cup B}$. Conversely $\overline{A}\cup\overline{B}$ is a union of two closed sets, hence closed, and it contains $A\cup B$; so it contains $\overline{A\cup B}$.

:::

:::

::: {.pf-step #union-inclusion}

$\bigcup_{\alpha}\overline{A_{\alpha}}\subset\overline{\bigcup_{\alpha}A_{\alpha}}$.

::: pf-proof

Let $x\in\bigcup_{\alpha}\overline{A_{\alpha}}$, say $x\in\overline{A_{\beta}}$. Every neighbourhood of $x$ meets $A_{\beta}$, hence meets $\bigcup_{\alpha}A_{\alpha}$, so $x\in\overline{\bigcup_{\alpha}A_{\alpha}}$.

:::

:::

::: pf-step

The inclusion of step [](#union-inclusion){.pf-ref} can be strict.

::: pf-proof

In $\RR$ with the standard topology take the family of one-point sets $\{q\}$ with $q\in\QQ$. Each $\{q\}$ is closed, so $\bigcup_{q\in\QQ}\overline{\{q\}}=\QQ$; but $\bigcup_{q\in\QQ}\{q\}=\QQ$ and $\overline{\QQ}=\RR$, since every open interval contains a rational. Hence $\QQ\subsetneq\RR$ exhibits the strict inclusion.

:::

:::

:::
:::
