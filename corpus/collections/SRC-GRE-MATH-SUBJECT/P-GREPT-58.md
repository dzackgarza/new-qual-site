---
schema: qual/card@1
id: P-GREPT-58
kind: problem
title: "Closed sets, compactness and separation in the cofinite topology on $\\RR$"
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 58 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Define a topology, $\mathbf{T}$, on the set of real numbers, $\RR$, as follows: $\mathbf{T}$ contains the empty set, $\varnothing$, and a nonempty subset $O$ of $\RR$ is in $\mathbf{T}$ if and only if $O^c$, the complement of $O$, is a finite set. Which of the following statements is/are true about $\RR$ with this topology?

I. Every infinite subset of $\RR$ is closed.

II. Every subset of $\RR$ is compact.

III. $\RR$ is Hausdorff.

(A) I only
(B) II only
(C) III only
(D) I and II only
(E) II and III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement I is false.


::: pf-proof

The closed subsets of $\RR$ are precisely $\RR$ itself and the finite
subsets. Indeed, a proper subset $F$ is closed exactly when
$\RR\setminus F$ is open, which by the definition of the topology is
equivalent to $F$ being finite. Thus, for example, $\ZZ$ is an infinite
proper subset of $\RR$ that is not closed.

:::

:::

::: {.pf-step #s1-2}

Statement II is true: every subset $A\subseteq\RR$ is compact.


::: pf-proof

Let $\mathcal U$ be an open cover of $A$. If $A$ is empty, the empty
subfamily is a finite subcover. Otherwise choose $a\in A$ and some
$U_0\in\mathcal U$ containing $a$. By the definition of the subspace
topology, $U_0=A\cap O_0$ for some open $O_0\subseteq\RR$. Since
$O_0$ is nonempty, $\RR\setminus O_0$ is finite, and hence
$A\setminus U_0=A\setminus O_0$ is finite. For each point of
$A\setminus U_0$, choose one member of $\mathcal U$ containing that
point. Together with $U_0$, these finitely many sets cover $A$.
Therefore $A$ is compact.

:::

:::

::: {.pf-step #s1-3}

Statement III is false.


::: pf-proof

Any two nonempty open subsets $U,V\subseteq\RR$ intersect. Their
complements are finite, so
$\RR\setminus(U\cap V)=(\RR\setminus U)\cup(\RR\setminus V)$ is finite.
Since $\RR$ is infinite, $U\cap V$ cannot be empty. Hence two distinct
points cannot have disjoint open neighborhoods, so the space is not
Hausdorff.

:::

:::

::: {.pf-step #s1-4}

Therefore the correct answer is $\boxed{\text{(B) II only}}$.


::: pf-proof

Step [](#s1-1){.pf-ref} disproves I, step [](#s1-2){.pf-ref} proves II, and step [](#s1-3){.pf-ref} disproves III.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
