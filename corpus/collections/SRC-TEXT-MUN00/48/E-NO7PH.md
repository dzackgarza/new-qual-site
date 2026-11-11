---
schema: qual/card@1
id: E-NO7PH
kind: problem
title: Baire property of the lower limit line
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 11 (printed p. 300) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: the half-open
    intervals [a,b) form a basis of the lower limit topology (Lemma 13.4 and the definition of R_l in §13); the
    dense open sets G_{n+1} meet each nonempty basic open set [a_n, b_n), so a basis element [a_{n+1}, b') lies
    inside the intersection, and halving gives a closed interval inside it; the resulting closed bounded
    intervals of R are nested, so they have a common point, which lies in the first basic open set and in every
    G_n. Nothing needed correction. Note that R_l is not a Baire space for the reason one might expect: the
    argument does not use completeness under any metric, only the nesting of closed intervals in the usual
    order of R.
---

::: {.exercise}

Determine whether or not $\RR_\ell$ is a Baire space.
:::

::: {.solution}
$\RR_\ell$ is a Baire space. Let $G_1, G_2, \ldots$ be dense open subsets of $\RR_\ell$ and let $U_0$ be a nonempty open subset. It suffices to show that $U_0 \cap \bigcap_n G_n \neq \varnothing$.

::: pf

::: {.pf-step #s1}

There are real numbers $a_n < b_n$, $n \ge 0$, with $[a_0, b_0] \subseteq U_0$ and $[a_{n+1}, b_{n+1}] \subseteq G_{n+1} \cap [a_n, b_n)$ for $n \ge 0$.

::: pf-proof

The sets $[a, b)$ form a basis of $\RR_\ell$. The nonempty open set $U_0$ contains some $[a_0, b_0')$; put $b_0 = (a_0 + b_0')/2$. Given $a_n < b_n$, the set $G_{n+1} \cap [a_n, b_n)$ is open, and nonempty because $G_{n+1}$ is dense. It contains some $[a_{n+1}, b')$ with $a_{n+1} < b'$; put $b_{n+1} = (a_{n+1} + b')/2$. Then $[a_{n+1}, b_{n+1}] \subseteq [a_{n+1}, b') \subseteq G_{n+1} \cap [a_n, b_n)$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref} the closed bounded intervals $[a_n, b_n]$ of $\RR$ are nested and nonempty, so they have a common point $x$ by compactness. Then $x \in [a_0, b_0] \subseteq U_0$ and $x \in [a_{n}, b_{n}] \subseteq G_{n}$ for every $n \ge 1$.

:::

:::

:::
