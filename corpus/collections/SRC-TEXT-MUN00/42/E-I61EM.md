---
schema: qual/card@1
id: E-I61EM
kind: problem
title: Sections of the minimal uncountable well-ordered set are second countable
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 42 Exercise 2, printed p. 262, with Theorem 42.1 (Smirnov), Theorem 28.2 (in a metrizable space limit point compactness implies compactness) and the countability of the ordinals below $\Omega$. No correction was needed; part (a) is the countability of the section and part (b) derives a contradiction by metrizing $S_\Omega$ and then compactifying it.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (b) concluded non-paracompactness from the assertion that a countably compact metrizable space is
    compact, which is not one of the book's numbered results; the card now uses limit point compactness,
    which is: an infinite subset of $S_\Omega$ contains an increasing sequence whose supremum is a countable
    ordinal below $\Omega$ and is a limit point of the subset. With Theorem 28.2 (a metrizable limit point
    compact space is compact) and the cover $\{[0,\alpha)\mid\alpha<\Omega\}$, which has no finite subcover,
    the contradiction is the one the exercise asks for. Checked against Theorem 42.1 (Smirnov), Theorem 28.2
    and the countability of the ordinals below $\Omega$.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (a) said that an ordered space is regular without a reference; the section $S_x$ is a well-ordered
    set in the order topology, hence normal by Theorem 32.4 and regular, which is the hypothesis the Urysohn
    metrization theorem (Theorem 34.1) needs, its countable basis being the countability of $S_x$.
---

::: {.exercise}

(a) Show that for each $x \in S_\Omega$, the section of $S_\Omega$ by $x$ has a countable basis and hence is metrizable.

(b) Conclude that $S_\Omega$ is not paracompact.
:::

::: {.solution}

The argument is the card's own, built from the book's numbered results; no complete published solution of Munkres §42 Exercise 2 was located, and the sets searched are recorded in the audit trail of the §43--§50 entry of `COMPLAINTS.md`.

Let $S_{\Omega}=[0,\Omega)$ and, for $x\in S_{\Omega}$, let $S_{x}=\{y:y<x\}$ be the section of $S_{\Omega}$ by $x$.

::: pf

::: {.pf-step #section}
(a) For each $x\in S_{\Omega}$ the section $S_{x}$ has a countable basis and is metrizable.

::: pf-proof

::: {.pf-step #countable}
$S_{x}$ is countable and its subspace topology is its order topology.

::: pf-proof
Every element of $S_{\Omega}$ is a countable ordinal (Theorem 10.2 and §10, printed p. 66), so the set $S_{x}$ of ordinals below $x$ is countable. The set $S_{x}=[0,x)$ is a ray of the ordered set $S_{\Omega}$, hence convex, so the order topology of $S_{x}$ is the topology it inherits as a subspace (Theorem 16.4, printed p. 91).
:::

:::

::: {.pf-step #basis}
$S_{x}$ has a countable basis.

::: pf-proof
The intervals $(a,b)$, $[0,b)$ and $(a,x)$ with $a,b\in S_{x}$ form a basis for the order topology on $S_{x}$ (§14, printed p. 84), and there are countably many such intervals because $S_{x}$ is countable by step [](#countable){.pf-ref}. So $S_{x}$ is second countable.
:::

:::

::: {.pf-step #metrizable}
$S_{x}$ is metrizable.

::: pf-proof
A well-ordered set is normal in its order topology (Theorem 32.4, printed p. 205), hence regular, and $S_{x}$ is a well-ordered set in the order topology by step [](#countable){.pf-ref}; with the countable basis of step [](#basis){.pf-ref} the Urysohn metrization theorem (Theorem 34.1, printed p. 217) gives a metric for $S_{x}$ that induces its topology.
:::

:::

:::

:::

::: {.pf-step #not-paracompact}
(b) $S_{\Omega}$ is not paracompact.

::: pf-proof

::: {.pf-step #locally-metrizable}
$S_{\Omega}$ is locally metrizable.

::: pf-proof
For $x\in S_{\Omega}$ the set $[0,x+1)=S_{x+1}$ is an open neighbourhood of $x$, and by step [](#section){.pf-ref} it is metrizable. So every point of $S_{\Omega}$ has a metrizable neighbourhood.
:::

:::

::: {.pf-step #limit-point-compact}
$S_{\Omega}$ is limit point compact and not compact.

::: pf-proof
Let $A\subset S_{\Omega}$ be infinite. Recursively choose $a_{1}=\min A$ and $a_{n+1}=\min\{a\in A:a>a_{n}\}$, which exists since otherwise $A\subset[0,a_{n}]$, a finite set. Then $a_{1}<a_{2}<\cdots$ is an increasing sequence in $A$; its supremum $\alpha$ is a countable ordinal, being a countable supremum of countable ordinals (§10, printed p. 66, on the arithmetic of ordinals), so $\alpha\in S_{\Omega}$, and every neighbourhood of $\alpha$ contains all but finitely many $a_{n}$. Hence $\alpha$ is a limit point of $A$, and $S_{\Omega}$ is limit point compact. It is not compact: the sets $[0,\alpha)$ for $\alpha<\Omega$ are open, they cover $S_{\Omega}$, and a finite subcollection is contained in the largest of its members, $[0,\alpha_{0})$, which omits $\alpha_{0}$.
:::

:::

::: {.pf-step #contradiction}
If $S_{\Omega}$ were paracompact it would be metrizable, which is impossible.

::: pf-proof
By the Smirnov metrization theorem (Theorem 42.1, printed p. 261) a space that is locally metrizable and paracompact is metrizable; step [](#locally-metrizable){.pf-ref} gives the first hypothesis. Were $S_{\Omega}$ metrizable, it would be compact by Theorem 28.2 (printed p. 180), since it is limit point compact by step [](#limit-point-compact){.pf-ref}; but step [](#limit-point-compact){.pf-ref} also shows it is not compact. So $S_{\Omega}$ is not paracompact.
:::

:::

:::

:::

:::
:::
