---
schema: qual/card@1
id: E-L2EHD
kind: problem
title: The Stone--Čech compactification of a discrete space is extremally disconnected
classification:
  areas:
  - topology
  topics:
  - Compactness
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
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.7, pages 1-2 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is
    dated 2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939
    of web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf). Checked against Munkres, Topology (2000), Section 38
    Exercise 7, printed p. 242, Theorem 38.4, Exercise 17.8 and Theorem 17.6. The sheet's argument is the
    card's: (a) is the extension to beta(X) of the characteristic function of A, whose two level sets are
    disjoint closed sets; (b) shows U and U cap X have the same closure, by density of X, and concludes
    from (a) that this closure is the complement of a closed set; (c) separates two distinct points of
    beta(X) by a clopen set, which is the sheet's explicit statement that beta(X) is extremally
    disconnected and hence totally disconnected. No correction was needed. Not checked here: the sheet
    states the extremally-disconnected conclusion in prose between its parts (b) and (c); the card puts
    it inside (b), where the proof of it is.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the three parts as the top-level steps with (c) as
    the QED step. Re-checked each: $\chi_A$ is continuous on a discrete space and extends to
    $\beta X$; the image lies in $\{0,1\}$ because that set is closed and $i(X)$ dense; the two
    preimages are disjoint closed sets containing $i(A)$ and $i(X-A)$; $A=U\cap i(X)$ is dense in
    $U$ so the closures agree; the closure of the union $X=A\cup(X-A)$ is $\beta X$; and $\beta X$
    is compact Hausdorff, so a point and a point can be separated by a regular open neighbourhood
    whose closure is clopen. Added: the closedness of $\{0,1\}$ in $[0,1]$ as the reason the image
    stays there, the closure-of-a-union identity, and the regularity step producing $q\notin
    \overline{U}$, each of which the earlier prose used implicitly. No defect found in the
    statement, §38 Exercise 7 on printed p. 242. Not claimed: a printed publication, the source being
    a posted solution sheet.
---

::: {.exercise}

Let $X$ be a discrete space; consider the space $\beta(X)$.

(a) Show that if $A \subset X$, then $\overline{A}$ and $\overline{X - A}$ are disjoint, where the closures are taken in $\beta(X)$.

(b) Show that if $U$ is open in $\beta(X)$, then $\overline{U}$ is open in $\beta(X)$.

(c) Show that $\beta(X)$ is totally disconnected.
:::

::: {.solution}
The argument of all three parts is the retained published solution, Jesper Michael Møller, *Solutions to exercises in Munkres*, file `S38.pdf`, Exercise 38.7, pages 1--2 of the file (`tmp/sources/munkres-solutions-poulsen-S38.pdf`). Write $i\colon X\to\beta X$ for the canonical embedding, whose image is dense in $\beta X$ by Theorem 38.4.

::: pf

::: {.pf-step #part-a}
(a) For $A\subseteq X$ the closures $\overline{A}$ and $\overline{X-A}$ in $\beta X$ are disjoint.

:::: pf-proof

::: {.pf-step #characteristic}
The characteristic function $\chi_A\colon X\to\{0,1\}\subseteq[0,1]$ is continuous and extends to a continuous $\widetilde\chi_A\colon\beta X\to[0,1]$.

::: pf-proof
In a discrete space every subset is open, so $\chi_A^{-1}(0)=\{x:\chi_A(x)=0\}=X-A$ and $\chi_A^{-1}(1)=A$ are open and $\chi_A$ is continuous. The extension property of the Stone--Čech compactification (Theorem 38.4) applies to the compact Hausdorff space $[0,1]$ and gives a continuous $\widetilde\chi_A$ with $\widetilde\chi_A\circ i=\chi_A$.
:::

:::

::: {.pf-step #level-sets}
$\widetilde\chi_A(\beta X)\subseteq\{0,1\}$.

::: pf-proof
$\{0,1\}$ is closed in $[0,1]$, and $\widetilde\chi_A(i(X))=\chi_A(X)\subseteq\{0,1\}$; since $i(X)$ is dense in $\beta X$ and $\widetilde\chi_A$ is continuous, $\widetilde\chi_A(\beta X)\subseteq\overline{\{0,1\}}=\{0,1\}$.
:::

:::

::: {.pf-step}
(a) $\overline{A}\subseteq\widetilde\chi_A^{-1}(1)$ and $\overline{X-A}\subseteq\widetilde\chi_A^{-1}(0)$, so the two closures are disjoint.

::: pf-proof
$\widetilde\chi_A^{-1}(1)$ is closed and contains $i(A)$, hence contains $\overline{i(A)}=\overline{A}$; likewise $\widetilde\chi_A^{-1}(0)$ is closed and contains $i(X-A)$, hence $\overline{X-A}$; and the two preimages are disjoint because a value of $\widetilde\chi_A$ is $0$ or $1$ and not both, by step [](#level-sets){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) If $U$ is open in $\beta X$, then $\overline{U}$ is open in $\beta X$.

:::: pf-proof

::: {.pf-step #same-closure}
With $A=U\cap i(X)$, one has $\overline{U}=\overline{A}$ in $\beta X$.

::: pf-proof
Every nonempty open subset $W$ of $U$ meets $i(X)$, because $W$ is open in $\beta X$ and $i(X)$ is dense; so $W\cap A\ne\varnothing$ and $A$ is dense in $U$. Hence $U\subseteq\overline{A}$, so $\overline{U}\subseteq\overline{A}$, while $A\subseteq U$ gives the reverse inclusion.
:::

:::

::: {.pf-step #cover}
$\beta X=\overline{A}\cup\overline{X-A}$.

::: pf-proof
$X=A\cup(X-A)$ is dense in $\beta X$, so $\beta X=\overline{i(X)}=\overline{i(A)\cup i(X-A)}=\overline{i(A)}\cup\overline{i(X-A)}=\overline{A}\cup\overline{X-A}$, the middle equality because the closure of a union is the union of the closures.
:::

:::

::: {.pf-step}
(b) $\overline{U}$ is both closed and open in $\beta X$.

::: pf-proof
By steps [](#same-closure){.pf-ref} and [](#cover){.pf-ref}, $\overline{U}=\overline{A}=\beta X\setminus\overline{X-A}$, which is the complement of a closed set and therefore open; it is the closure of $U$ and therefore closed. So the closure of every open set is open, that is, $\beta X$ is extremally disconnected.
:::

:::

:::

:::

::: {.pf-step}
(c) $\beta X$ is totally disconnected.

:::: pf-proof

::: {.pf-step #clopen-separation}
Any two distinct points of $\beta X$ are separated by a clopen set.

::: pf-proof
Let $p\ne q$ in $\beta X$. By Theorem 38.4 the space $\beta X$ is compact Hausdorff, hence normal and regular, so the point $p$ and the closed set $\{q\}$ have disjoint open neighbourhoods $U$ and $V$; then $q\notin\overline{U}$, since $V$ is a neighbourhood of $q$ disjoint from $U$. By part [](#part-b){.pf-ref}, $\overline{U}$ is clopen, and $p\in\overline{U}$ while $q\notin\overline{U}$.
:::

:::

::: {.pf-step}
(c) Every connected subset of $\beta X$ is a single point.

::: pf-proof
Let $C\subseteq\beta X$ be connected and suppose it contains distinct points $p,q$. Step [](#clopen-separation){.pf-ref} gives a clopen set $K$ with $p\in K$ and $q\notin K$; then $C\cap K$ is a nonempty proper subset of $C$ that is open and closed in the subspace $C$, so $C$ is not connected, a contradiction. Hence every component of $\beta X$, being connected, is a point, and $\beta X$ is totally disconnected.
:::

:::

:::

:::

:::
:::
