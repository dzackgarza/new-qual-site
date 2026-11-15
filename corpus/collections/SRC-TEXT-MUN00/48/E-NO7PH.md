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
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from Brian M. Scott's answer 477117 (2013-08-27) to Math StackExchange 476821, "The Sorgenfrey
    line is a Baire Space" (https://math.stackexchange.com/questions/476821), text at
    tmp/sources/mse-476821-munkres-48-11.md, and checked against the book. The answer gives the short proof
    that the intersection of countably many dense open subsets of $\RR_\ell$ is dense: a set is dense in
    $\RR_\ell$ exactly when it is dense in $\RR$, the Euclidean interior $V_n$ of a dense open $U_n$ is dense
    open in $\RR$, and $\RR$ is Baire, so $\bigcap_n V_n\subseteq\bigcap_n U_n$ is dense. What the card adds
    is the proof of the two claims the answer states: that every point of an $\RR_\ell$-open $U$ has
    $(x,x+\varepsilon)\subseteq U$ for some $\varepsilon>0$, which makes the Euclidean interior dense, and that
    an $\RR_\ell$-open set contains a nonempty Euclidean open set, which carries density from $\RR$ to
    $\RR_\ell$. The question's own proof, kept on the card as a remark, is the nested half-open interval
    construction; Scott's repair of it, that $y_{n+1}$ must be chosen strictly greater than $x_{n+1}$, is the
    reason the remark takes $b' > a_{n+1}$ before halving. The post by Yougi, *Munkres Topology Solution:
    Chapter 8* (2025-07-10, https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/), answers
    this exercise at its Ex. 48.11 but its argument does not close: it replaces each $W_n$ by the union of the
    open intervals inside its half-open basis elements, asserts that this is dense in $\RR_\ell$ and hence in
    $\RR$, and concludes a statement about the union $\bigcup_n W_n$ where density of the intersection is
    wanted. That second answer is not used.
---

::: {.exercise}

Determine whether or not $\RR_\ell$ is a Baire space.
:::

::: {.solution}
$\RR_\ell$ is a Baire space. Two facts about the lower limit topology are used, both from its basis of half-open intervals $[a,b)$ (Lemma 13.4).

::: pf

::: {.pf-step #dense}
A set $D\subseteq\RR$ is dense in $\RR_\ell$ exactly when it is dense in $\RR$.

::: pf-proof
If $D$ is dense in $\RR$ and $[a,b)$ is a nonempty basic open set of $\RR_\ell$, then $(a,b)$ is a nonempty open interval, so it meets $D$, and hence so does $[a,b)$. Conversely, if $D$ is dense in $\RR_\ell$ and $(a,b)$ is a nonempty open interval, choose $c\in(a,b)$; then $[c,b)$ is a nonempty open set of $\RR_\ell$, so it meets $D$, and $[c,b)\subseteq(a,b)$.
:::

:::

::: {.pf-step #interior}
If $U\subseteq\RR$ is open and dense in $\RR_\ell$, its Euclidean interior $V$ is open and dense in $\RR$.

::: pf-proof
$V$ is open by definition. Let $x\in U$; since $U$ is open in $\RR_\ell$ there is $\varepsilon>0$ with $[x,x+\varepsilon)\subseteq U$, so $(x,x+\varepsilon)\subseteq V$. Hence every point of $U$ lies in the Euclidean closure of $V$, and since $U$ is dense in $\RR$ by step [](#dense){.pf-ref}, so does every point of $\RR$.
:::

:::

::: {.pf-step #baire}
$\bigcap_n U_n$ is dense in $\RR_\ell$ for every countable family of open dense $U_n$.

::: pf-proof
Each $V_n$ is open and dense in $\RR$ by step [](#interior){.pf-ref}, and $\RR$ is a complete metric space, so it is a Baire space by Theorem 48.2 and $\bigcap_n V_n$ is dense in $\RR$ by Lemma 48.1. Since $\bigcap_n V_n\subseteq\bigcap_n U_n$, the larger set $\bigcap_n U_n$ is dense in $\RR$, hence dense in $\RR_\ell$ by step [](#dense){.pf-ref}.
:::

:::

::: pf-qed
By step [](#baire){.pf-ref}, every countable intersection of dense open subsets of $\RR_\ell$ is dense, so $\RR_\ell$ is a Baire space by Lemma 48.1.
:::

:::

:::

::: {.remark title="Nested half-open intervals"}
The question at Math StackExchange 476821 proves the same statement by a different construction, which the card carried before this transcription. Let $G_1,G_2,\ldots$ be dense open and $U_0$ a nonempty basic open set. Choose $a_0<b_0'$ with $[a_0,b_0')\subseteq U_0$ and put $b_0=(a_0+b_0')/2$. Given $a_n<b_n$, the set $G_{n+1}\cap[a_n,b_n)$ is nonempty and open in $\RR_\ell$, so it contains some $[a_{n+1},b')$ with $a_{n+1}<b'$; put $b_{n+1}=(a_{n+1}+b')/2$. Then $[a_{n+1},b_{n+1}]\subseteq[a_{n+1},b')\subseteq G_{n+1}\cap[a_n,b_n)$, so the closed bounded intervals $[a_n,b_n]$ of $\RR$ are nested and nonempty and have a common point $x$, which lies in $U_0$ and in every $G_n$. Brian M. Scott's answer to that question notes the one care the construction needs: $a_{n+1}<b'$ must be arranged so that $[a_{n+1},b')$ is nonempty (his $y_{n+1}>x_{n+1}$), which is why $b_{n+1}$ is taken strictly between the two.
:::
