---
schema: qual/card@1
id: P-GRECH7-34
kind: problem
title: Exterior of $(0,1)\cup[4,6)$ in $\RR$
classification:
  areas: [topology]
  topics:
  - Interior and Exterior
  - Real Line Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 34 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $(X, T)$ be a topological space, and let $A$ be the subset $(0, 1) \cup [4, 6)$ in $\RR$. Find the exterior of $A$.

(A) $(-\infty, 0) \cup (2, 3) \cup (6, \infty)$
(B) $[0, 1] \cup [4, 6]$
(C) $(-\infty, 0) \cup (1, 4) \cup (6, \infty)$
(D) $(-\infty, 0] \cup [1, 4) \cup [6, \infty)$
(E) $(-\infty, 0) \cup (6, \infty)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The closure of
$$
A=(0,1)\cup[4,6)
$$
in the usual topology on $\RR$ is
$$
\overline A=[0,1]\cup[4,6].
$$


::: pf-proof

The interval $(0,1)$ has closure $[0,1]$, while $[4,6)$ has closure $[4,6]$. Since the closure of a finite union is the union of the closures, the displayed formula follows.

:::

:::

::: {.pf-step #s1-2}

The exterior of $A$ is
$$
\operatorname{ext}(A)=\RR\setminus\overline A.
$$


::: pf-proof

By definition, the exterior is the interior of the complement:
$$
\operatorname{ext}(A)=\operatorname{int}(\RR\setminus A).
$$
For every subset of a topological space,
$$
\operatorname{int}(X\setminus A)=X\setminus\overline A.
$$
Applying this identity in $\RR$ gives the claim.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\operatorname{ext}(A)
=\boxed{(-\infty,0)\cup(1,4)\cup(6,\infty)},
$$
so the answer is (C).


::: pf-proof

Taking the complement of the closed set in step [](#s1-1){.pf-ref} yields exactly the three displayed open intervals, by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested exterior.

:::

:::

:::
