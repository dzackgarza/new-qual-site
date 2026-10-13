---
schema: qual/card@1
id: P-GREPT-52
kind: problem
title: "Connectedness, compactness and the Hausdorff property for a set between two others"
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 52 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $X$ be a topological space, and let $A$, $B$, and $C$ be nonempty subsets of $X$ such that $A \subset B \subset C$; that is, $A$ is a proper subset of $B$, and $B$ is a proper subset of $C$. Which of the following statements is/are true?

I. If $A$ and $C$ are connected, then $B$ is connected.

II. If $A$ and $C$ are compact, then $B$ is compact.

III. If $A$ and $C$ are Hausdorff, then $B$ is Hausdorff.

(A) I and II only
(B) I and III only
(C) II and III only
(D) III only
(E) I, II, and III
:::

::: {.solution}
<1>1. Statement I is false.

::: {.proof}
Take $X=\RR$ with its usual topology and set
$$
A=\{0\},
\qquad
B=\{0\}\cup(1,2],
\qquad
C=[0,2].
$$
Then $A\subset B\subset C$ are proper inclusions. The sets $A$ and $C$ are
connected, but $B$ is disconnected because
$$
B=\{0\}\sqcup(1,2]
$$
is a separation into two nonempty relatively open subsets of $B$.
:::

<1>2. Statement II is false.

::: {.proof}
Again take $X=\RR$ and set
$$
A=\{0\},
\qquad
B=[0,2),
\qquad
C=[0,2].
$$
The sets $A$ and $C$ are compact, whereas $B$ is not compact. Indeed, in the
Hausdorff space $\RR$, every compact subset is closed, but $[0,2)$ is not
closed in $\RR$.
:::

<1>3. Statement III is true.

::: {.proof}
The assumption that $C$ is Hausdorff is sufficient. If $x,y\in B$ are
distinct, then as points of $C$ they have disjoint open neighborhoods
$U,V\subseteq C$. Their intersections $U\cap B$ and $V\cap B$ are disjoint
open neighborhoods of $x$ and $y$ in the subspace $B$. Hence $B$ is
Hausdorff.
:::

<1>4. Therefore exactly statement III is true, so the answer is
$$
\boxed{\text{(D) III only}}.
$$

::: {.proof}
Steps <1>1--<1>3 show respectively that I is false, II is false, and III is
true.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required choice.
:::
:::
