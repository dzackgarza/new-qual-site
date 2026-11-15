---
schema: qual/card@1
id: E-CKXKK
kind: problem
title: $G_\delta$ subspaces of compact Hausdorff or complete metric spaces are Baire
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 5 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, following the
    exercise's hint, and with Theorem 48.2 (compact Hausdorff and complete metric spaces are Baire), Theorem
    26.9 (finite intersection property) and Lemma 48.3 for the nested closed sets of the metric case. What was
    corrected: the choice of the neighbourhood U_n avoided the closure of B_n by invoking only closedness of
    B_n in Y, which does not by itself produce an X-open neighbourhood of a point of Y outside B_n whose closure
    misses the X-closure of B_n; the text now names a closed C in X with B_n = C cap Y, notes that the chosen
    point lies outside C, and takes the neighbourhood inside the X-open set X - C, which is where the avoidance
    of the closure comes from. It also now says why it suffices to run the construction from an arbitrary open
    U_0 with U_0 cap Y nonempty: every nonempty relatively open subset of Y arises that way. The remaining steps
    are the hint's: nestedness with the diameter bound gives a Cauchy sequence whose limit lies in every
    closure, the compact case uses the finite intersection property instead, and the point found lies in Y, in
    U_0, and outside every B_n.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from Jesus RS, answer 1133343 (2015-02-04) to Math StackExchange 1130245, "G_delta sets in
    locally compact Hausdorff or complete metric space are Baire spaces", at
    https://math.stackexchange.com/a/1133343, text at tmp/sources/mse-1130245-munkres-48-5.md, and
    checked against the book. That question states the claim for a locally compact Hausdorff or complete
    metric X, which contains Munkres' hypotheses: a compact Hausdorff space is locally compact Hausdorff, and
    by §48 Exercise 3, or by the answer's own use of Theorem 48.2 in the closed subspace, is Baire. The
    argument replaces X by the closure of Y, which is closed in X and so again compact Hausdorff or complete
    metric, so that Y is dense and the sets W_n of its G_delta expression are dense; a countable family of
    dense open subsets of Y is then a family of dense open subsets of X, whose intersection is dense in X by
    Theorem 48.2 and, lying in Y, dense in Y. This is shorter than the nested-neighbourhood construction of
    the exercise's hint, which the card carried before; that construction is the book's proof of Theorem 48.2
    specialized to Y and is not needed on this route. The second answer in the thread, by Westlifer
    (2024-12-11), adds that complete metrizability is G_delta-hereditary and cites Exercise 43.6; the card
    does not use it. The post by Yougi, *Munkres Topology Solution: Chapter 8* (2025-07-10,
    https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/), answers the exercise at its Ex.
    48.5 along the same two lines but with a gap: it assumes without proof that Y may be taken dense and that
    the V_n are then dense in X, and it writes the conclusion as "we know that the intersection of the V_n is
    dense" before the Baire theorem has been applied to the U_n and W_n; the card's route supplies exactly
    those two steps.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. Steps #inter and #main used W_n' with no step defining it; #closed now puts
    W_n' = W_n cap Z, notes that it is open in Z, and records why Y = cap_n W_n' (each W_n contains Y, and
    Y lies in Z). Those are the only two properties the later steps use: W_n' contains the dense set Y, and
    the intersection of the W_n' is Y. The attribution above is corrected to the account's own name,
    Jesus RS, with the answer's URL, https://math.stackexchange.com/a/1133343; the byline is read from the
    stored copy of the thread at tmp/sources/mse-1130245-munkres-48-5.md, not from the site, which answered
    an automated request with a human check and whose API reported its quota used up for this address.
---

::: {.exercise}

Show that if $Y$ is a $G_\delta$ set in $X$, and if $X$ is compact Hausdorff or complete metric, then $Y$ is a Baire space in the subspace topology.
[Hint: Suppose that $Y = \bigcap W_n$, where $W_n$ is open in $X$, and that $B_n$ is closed in $Y$ and has empty interior in $Y$.
Given $U_0$ open in $X$ with $U_0 \cap Y \neq \varnothing$, find a sequence of open sets $U_n$ of $X$ with $U_n \cap Y$ nonempty, such that

$$
\begin{array}{c}
\overline{U}_n \subset U_{n-1}, \\
\overline{U}_n \cap \overline{B}_n = \varnothing, \\
\operatorname{diam} U_n < 1/n \quad \text{in the metric case}, \\
\overline{U}_n \subset W_n.
\end{array}
$$
]
:::

::: {.solution}
Write $Y=\bigcap_n W_n$ with each $W_n$ open in $X$.

::: pf

::: {.pf-step #closed}
$X$ may be replaced by a closed subspace in which $Y$ is dense, and that subspace is again compact Hausdorff or complete metric.

::: pf-proof
Let $Z=\overline Y$ be the closure of $Y$ in $X$, with the subspace topology. A closed subspace of a compact Hausdorff space is compact Hausdorff, and a closed subspace of a complete metric space is complete in the restricted metric: a Cauchy sequence in $Z$ converges in $X$, and its limit lies in $\overline Z=Z$. Put $W_n'=W_n\cap Z$; each $W_n'$ is open in $Z$, and $Y=\bigcap_n W_n'$ because $Y\subseteq W_n$ for every $n$ and $Y\subseteq Z$. So $Y$ is a $G_\delta$ set of $Z$, and it is dense in $Z$ by the definition of closure. Baireness of $Y$ depends on the topology of $Y$ alone, so it suffices to prove the claim for a dense $G_\delta$ set $Y$ of a space $Z$ that is Baire.
:::

:::

::: {.pf-step #inter}
$Z$ is a Baire space, and $\bigcap_n W_n'$ is dense in $Z$.

::: pf-proof
A compact Hausdorff space and a complete metric space are Baire by Theorem 48.2. Each $W_n'$ contains $Y$, which is dense in $Z$, so each $W_n'$ is dense in $Z$; a countable intersection of dense open sets of a Baire space is dense by Lemma 48.1, so $\bigcap_n W_n' = Y$ is dense in $Z$, as asserted.
:::

:::

::: {.pf-step #main}
The intersection of countably many dense open subsets of $Y$ is dense in $Y$.

::: pf-proof
Let $V_1,V_2,\ldots$ be dense open subsets of $Y$, and choose open $U_m\subseteq Z$ with $V_m=Y\cap U_m$. Since $V_m$ is dense in $Y$ and $Y$ is dense in $Z$, the set $U_m$ is dense in $Z$: a nonempty open $O\subseteq Z$ meets $Y$, and $O\cap Y$ is a nonempty relatively open subset of $Y$, so it meets $V_m\subseteq U_m$. The countable family consisting of the $W_n'$ and the $U_m$ is a family of dense open subsets of the Baire space $Z$, so by Lemma 48.1 its intersection $D$ is dense in $Z$. Every point of $D$ lies in $\bigcap_n W_n' = Y$, so $D\subseteq Y$, and a subset of $Y$ dense in $Z$ is dense in $Y$. Finally $D=\bigcap_m (Y\cap U_m)=\bigcap_m V_m$.
:::

:::

::: pf-qed
By step [](#main){.pf-ref}, every countable intersection of dense open subsets of $Y$ is dense in $Y$, so $Y$ is a Baire space by Lemma 48.1. The exercise's hint constructs such a family by nested neighbourhoods instead; that construction is the proof of Theorem 48.2 applied inside $Y$ and is not needed here.
:::

:::

:::
