---
schema: qual/card@1
id: E-JW56I
kind: problem
title: Countability axioms of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Countability
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 30.7, printed p. 2
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), which answers all four axioms for both
    S_Omega and S_bar_Omega; checked against Munkres, Topology (2000), Section 30 Exercise 7,
    printed p. 194, Theorem 10.3 (a countable subset of S_Omega has an upper bound below Omega),
    Example 3 and Example 5 (printed pp. 192-193), and Exercise 29.7 with Theorem 29.1 for the
    compactness of S_bar_Omega. What was corrected: the earlier card offered, at a limit ordinal
    alpha, the intervals (alpha_n, alpha] as a local basis, and these are not open sets of the
    order topology; the card now uses the open intervals (alpha_n, alpha + 1), and adds the
    least-element case. The answers themselves (first countable and nothing else for S_Omega;
    Lindelof and nothing else for S_bar_Omega) are Doug's World's and agree with the card.
---

::: {.exercise}

Which of our four countability axioms does $S_\Omega$ satisfy?
What about $\overline{S}_\Omega$?
:::

::: {.solution}

No retained solution set covers this exercise: the card's own answers are correct and are set out here as separate steps, one per space and axiom.

Write $\Omega=\omega_{1}$ for the least uncountable ordinal, $S_{\Omega}=[0,\Omega)$ and $\overline{S}_{\Omega}=[0,\Omega]$ in the order topology.

::: pf

::: {.pf-step #facts}
Every $\alpha<\Omega$ is a countable ordinal, the supremum of any countable set of countable ordinals is $<\Omega$, and $\overline{S}_{\Omega}$ is compact.

::: pf-proof
The first two are the definition of $\omega_{1}$ as the least uncountable ordinal: a countable set of countable ordinals is a countable set of countable ordinals, hence a countable ordinal, hence $<\Omega$. For compactness, $\overline{S}_{\Omega}$ is the one-point compactification of $S_{\Omega}$ (Exercise 29.7) and one-point compactifications are compact (Theorem 29.1, printed p. 183).
:::

:::

::: {.pf-step #first-countable}
$S_{\Omega}$ is first countable.

::: pf-proof
Let $\alpha<\Omega$. If $\alpha=\beta+1$ then $\{\alpha\}=(\beta,\alpha+1)$ is open, so the single set $(\beta,\alpha+1)$ is a local base. If $\alpha$ is a limit ordinal, $\alpha$ is countable, so there is a strictly increasing sequence $\alpha_{n}\uparrow\alpha$; every neighbourhood of $\alpha$ contains an interval $(\beta,\gamma)$ with $\beta<\alpha$, hence contains $(\alpha_{n},\alpha+1)$ for $n$ with $\alpha_{n}>\beta$, so the countably many sets $(\alpha_{n},\alpha+1)$ form a local base. At $0$ the sets $[0,\alpha_{n})$ do the same.
:::

:::

::: {.pf-step #not-separable}
$S_{\Omega}$ is not separable.

::: pf-proof
Let $D\subseteq S_{\Omega}$ be countable and $\beta=\sup D<\Omega$ by step [](#facts){.pf-ref}. Then $D\subseteq[0,\beta]$, which is closed, so the closure of $D$ is not all of $S_{\Omega}$ (it misses $\beta+1$); hence no countable set is dense.
:::

:::

::: {.pf-step #not-second}
$S_{\Omega}$ is not second countable, and neither is $\overline{S}_{\Omega}$.

::: pf-proof
A second-countable space is separable (Theorem 30.3(a), printed p. 194) and $S_{\Omega}$ is not, by step [](#not-separable){.pf-ref}. For $\overline{S}_{\Omega}$, if $D$ is countable then $\beta=\sup(D\cap S_{\Omega})<\Omega$ and the nonempty open interval $(\beta,\Omega)$ misses $D$ even when $\Omega\in D$, so $\overline{S}_{\Omega}$ is not separable either, hence not second countable.
:::

:::

::: {.pf-step #not-lindelof}
$S_{\Omega}$ is not Lindelöf.

::: pf-proof
The family $\theset{[0,\alpha)\mid\alpha<\Omega}$ is a cover by open sets. Were $\theset{[0,\alpha_{n})}$ a countable subcover, its union would be $[0,\beta)$ with $\beta=\sup_{n}\alpha_{n}<\Omega$ by step [](#facts){.pf-ref}, which is not all of $S_{\Omega}$. So there is no countable subcover.
:::

:::

::: {.pf-step #lindelof}
$\overline{S}_{\Omega}$ is Lindelöf.

::: pf-proof
It is compact by step [](#facts){.pf-ref}, and a compact space is Lindelöf: every open cover has a finite, hence countable, subcover.
:::

:::

::: {.pf-step #not-first-overline}
$\overline{S}_{\Omega}$ is not first countable at $\Omega$.

::: pf-proof
Suppose $\theset{V_{n}}$ were a countable local base at $\Omega$. Each $V_{n}$ contains a basis element $(\alpha_{n},\Omega]$ with $\alpha_{n}<\Omega$; put $\alpha=\sup_{n}\alpha_{n}<\Omega$ by step [](#facts){.pf-ref}. Then $(\alpha,\Omega]$ is a neighbourhood of $\Omega$ containing no $V_{n}$, since $V_{n}\subseteq(\alpha_{n},\Omega]\not\subseteq(\alpha,\Omega]$ — contradiction.
:::

:::

::: {.pf-qed}
$S_{\Omega}$ satisfies first countability (step [](#first-countable){.pf-ref}) and fails separability, second countability and Lindelöfness (steps [](#not-separable){.pf-ref}, [](#not-second){.pf-ref}, [](#not-lindelof){.pf-ref}), so it satisfies exactly one of the four axioms. $\overline{S}_{\Omega}$ satisfies Lindelöfness (step [](#lindelof){.pf-ref}) and fails first countability at $\Omega$, separability and second countability (steps [](#not-first-overline){.pf-ref}, [](#not-second){.pf-ref}), so it too satisfies exactly one, a different one.
:::

:::

:::
