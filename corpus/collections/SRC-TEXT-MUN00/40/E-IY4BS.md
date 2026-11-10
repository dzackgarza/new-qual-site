---
schema: qual/card@1
id: E-IY4BS
kind: problem
title: Complements of $F_\sigma$ sets are $G_\delta$ sets
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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
    Checked against Munkres, Topology (2000), Section 40 Exercise 2, printed p. 251, with the definitions of $F_\sigma$ and $G_\delta$ and De Morgan's laws (§1). No correction was needed.
---

::: {.exercise}

A subset $W$ of $X$ is said to be an "$F_\sigma$ set" in $X$ if $W$ equals a countable union of closed sets of $X$.
Show that $W$ is an $F_\sigma$ set in $X$ if and only if $X - W$ is a $G_\delta$ set in $X$.

[The terminology comes from the French. The "F" stands for "fermé," which means "closed," and the "σ" for "somme," which means "union."]
:::

::: {.solution}
Suppose first that
$$
W=\bigcup_{n=1}^{\infty}F_n
$$
with each $F_n$ closed. By De Morgan's law,
$$
X-W
 =X-\bigcup_nF_n
 =\bigcap_n(X-F_n).
$$
Each $X-F_n$ is open, so $X-W$ is a $G_\delta$ set.

Conversely, suppose
$$
X-W=\bigcap_{n=1}^{\infty}U_n
$$
with each $U_n$ open. Again by De Morgan's law,
$$
W
=X-\bigcap_nU_n
=\bigcup_n(X-U_n).
$$
Each $X-U_n$ is closed, so $W$ is $F_\sigma$.

Therefore
$$
\boxed{W\text{ is }F_\sigma\iff X-W\text{ is }G_\delta.}
$$
:::
