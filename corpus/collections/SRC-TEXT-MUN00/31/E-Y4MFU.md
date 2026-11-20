---
schema: qual/card@1
id: E-Y4MFU
kind: problem
title: Perfect maps transfer separation and countability properties
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 31.7, printed
    pp. 5-6 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), which answers all four parts;
    checked against Munkres, Topology (2000), Section 31 Exercise 7, printed pp. 199-200, Theorem
    26.7, Lemma 26.4 (printed p. 166), Exercise 26.5 and Theorem 29.2. What was corrected: in
    part (b) the source begins "Given y in X and neighborhood U of y" and separates the compact
    fibre from p^{-1}(Y - U) without first noting that regularity of X makes X Hausdorff, so that
    part (a) applies and Y is T1; without that, regularity of Y is not defined. The card states it.
    In part (d) the source writes "the collection of S_J = p(U_J) (which is open since it is the
    union of open sets W)" and "it follows that S_J is contained in V"; the card writes the
    saturation identity p^{-1}(y) <= U_J and the two inclusions y in p(U_J) and p(U_J) <= W
    explicitly, which is what those sentences are compressing.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    nine steps, each carrying a `pf-proof`, and the four parts answer Munkres, Topology, §31
    Exercise 7. Cited by number only: Exercise 26.5 (disjoint compact subsets of a Hausdorff space
    have disjoint open neighbourhoods) and §22 (a closed continuous surjection is a quotient map).
    The transcription is from "Doug's World", Munkres -- Topology -- Chapter 4 Solutions, Problem
    31.7, and the card keeps the two points where it repairs the source: that regularity of X makes
    X Hausdorff, so that part (a) gives Y the T1 property needed for regularity of Y, and the two
    inclusions of the basis step. Checked: that the closed-map lemma really gives p^{-1}(W) inside
    U, that the separated set V misses the union U, that W and O of part (b) are disjoint, that a
    point of W in part (c) lies in p(K), and that the sets p(U_J) both contain y and lie in W in
    part (d).
---

::: {.exercise}

Let $p: X \to Y$ be a closed continuous surjective map such that $p^{-1}(\theset{y})$ is compact for each $y \in Y$.
(Such a map is called a perfect map.)

(a) Show that if $X$ is Hausdorff, then so is $Y$.

(b) Show that if $X$ is regular, then so is $Y$.

(c) Show that if $X$ is locally compact, then so is $Y$.

(d) Show that if $X$ is second-countable, then so is $Y$.
[Hint: Let $\mathcal{B}$ be a countable basis for $X$. For each finite subset $J$ of $\mathcal{B}$, let $U_J$ be the union of all sets of the form $p^{-1}(W)$, for $W$ open in $Y$, that are contained in the union of the elements of $J$.]
:::

::: {.solution}

The argument is "Doug's World", *Munkres -- Topology -- Chapter 4 Solutions*, Problem 31.7, read in the retained text `tmp/sources/munkres-solutions-dougsworld-ch4.pdf`. Two places where the card states what the source compresses are the $T_1$ step of part (b) (step [](#t1){.pf-ref}) and the two inclusions of part (d) (step [](#basis-covers){.pf-ref}).

::: pf

::: {.pf-step #lemma}
If $U\subseteq X$ is open and $p^{-1}(y)\subseteq U$, then $W=Y-p(X-U)$ is an open neighbourhood of $y$ with $p^{-1}(W)\subseteq U$.

::: pf-proof
$p$ is closed, so $p(X-U)$ is closed and $W$ is open. The fibre meets $X-U$ in no point, so $y\notin p(X-U)$ and $y\in W$. Finally $p^{-1}(W)=X-p^{-1}(p(X-U))\subseteq X-(X-U)=U$, because $X-U\subseteq p^{-1}(p(X-U))$.
:::

:::

::: {.pf-step #hausdorff}
(a) If $X$ is Hausdorff, then $Y$ is Hausdorff.

::: pf-proof
Let $y_1\ne y_2$ and put $F_i=p^{-1}(y_i)$. The fibres are compact and disjoint, so by Munkres, Exercise 26.5, there are disjoint open sets $U_1\supseteq F_1$ and $U_2\supseteq F_2$. Step [](#lemma){.pf-ref} gives open $W_i\ni y_i$ with $p^{-1}(W_i)\subseteq U_i$. Then $W_1\cap W_2=\varnothing$: a point $w$ of the intersection would have $p^{-1}(w)\subseteq U_1\cap U_2=\varnothing$, while $p^{-1}(w)\ne\varnothing$ because $p$ is surjective.
:::

:::

::: {.pf-step #t1}
(b) $Y$ is $T_1$.

::: pf-proof
A regular space is Hausdorff, and $X$ is regular by hypothesis, so $Y$ is Hausdorff by step [](#hausdorff){.pf-ref} and therefore $T_1$.
:::

:::

::: {.pf-step #separate}
(b) If $C\subseteq Y$ is closed and $y\notin C$, then there are disjoint open sets $U\supseteq p^{-1}(y)$ and $V\supseteq p^{-1}(C)$.

::: pf-proof
Put $F=p^{-1}(y)$ and $A=p^{-1}(C)$. $F$ is compact, $A$ is closed because $p$ is continuous, and the two are disjoint. For $x\in F$ the set $X-A$ is an open neighbourhood of $x$, so regularity gives an open neighbourhood $O_x$ of $x$ with $\overline{O_x}\subseteq X-A$. The $O_x$ cover the compact $F$, so $F\subseteq U=\bigcup_{i=1}^nO_{x_i}$ for finitely many points $x_i\in F$. Let $V=X-\bigcup_{i=1}^n\overline{O_{x_i}}$. The set $V$ is open because the finite union of the closed sets $\overline{O_{x_i}}$ is closed, it contains $A$ because each $\overline{O_{x_i}}$ misses $A$, and $U\cap V=\varnothing$ because $U\subseteq\bigcup_i\overline{O_{x_i}}$.
:::

:::

::: {.pf-step #regular}
(b) If $X$ is regular, then $Y$ is regular.

::: pf-proof
Let $C\subseteq Y$ be closed and $y\notin C$. Step [](#separate){.pf-ref} gives disjoint open sets $U\supseteq p^{-1}(y)$ and $V\supseteq p^{-1}(C)$, and step [](#lemma){.pf-ref} gives an open $W\ni y$ with $p^{-1}(W)\subseteq U$. For $c\in C$ the fibre $p^{-1}(c)$ lies in $V$, so step [](#lemma){.pf-ref} gives an open $W_c\ni c$ with $p^{-1}(W_c)\subseteq V$; then $O=\bigcup_{c\in C}W_c$ is open, contains $C$, and satisfies $p^{-1}(O)\subseteq V$. Hence $W\cap O=\varnothing$, since a point $z$ of the intersection would have $p^{-1}(z)\subseteq U\cap V=\varnothing$ while $p^{-1}(z)\ne\varnothing$. With step [](#t1){.pf-ref} this says that $Y$ is regular.
:::

:::

::: {.pf-step #locally-compact}
(c) If $X$ is locally compact, then $Y$ is locally compact.

::: pf-proof
Let $y\in Y$ and $F=p^{-1}(y)$. Each $x\in F$ lies in an open neighbourhood $U_x$ contained in a compact subspace $K_x$ of $X$, by local compactness of $X$; the $U_x$ cover the compact $F$, so $F\subseteq U=\bigcup_{i=1}^nU_{x_i}$ for finitely many $x_i$. Then $K=\bigcup_{i=1}^nK_{x_i}$ is compact and contains $U$, and step [](#lemma){.pf-ref} gives an open $W\ni y$ with $p^{-1}(W)\subseteq U\subseteq K$. Hence $W\subseteq p(K)$: a point $w\in W$ has a nonempty fibre $p^{-1}(w)\subseteq p^{-1}(W)\subseteq K$, so $w=p(x)$ for some $x\in K$. The set $p(K)$ is compact, being the continuous image of a compact space, so $Y$ is locally compact at $y$.
:::

:::

::: {.pf-step #basis-family}
(d) For a finite $J\subseteq\mathcal B$ put $U_J=\bigcup\{p^{-1}(W):W\subseteq Y\text{ open},\ p^{-1}(W)\subseteq\bigcup J\}$. Then $U_J$ is open and saturated, $p(U_J)$ is open in $Y$, and there are only countably many of the sets $p(U_J)$.

::: pf-proof
Each $p^{-1}(W)$ is open and saturated, and a union of open saturated sets is open and saturated, so $U_J$ is open and saturated. A closed continuous surjection is a quotient map (Munkres, §22), so it carries the saturated open set $U_J$ to an open set. The countable basis $\mathcal B$ has only countably many finite subsets $J$, hence the sets $p(U_J)$ are countable in number.
:::

:::

::: {.pf-step #basis-covers}
(d) For $y\in W$ with $W$ open in $Y$ there is a finite $J\subseteq\mathcal B$ with $y\in p(U_J)\subseteq W$.

::: pf-proof
$F=p^{-1}(y)$ is compact and lies in the open set $p^{-1}(W)$, so there are finitely many basis elements $B_1,\dots,B_n\in\mathcal B$ with $F\subseteq B_1\cup\cdots\cup B_n\subseteq p^{-1}(W)$: each point of $F$ has a basis element inside $p^{-1}(W)$, and finitely many of these cover $F$. Let $J=\{B_1,\dots,B_n\}$. Step [](#lemma){.pf-ref} applied to the open set $\bigcup J\supseteq F$ gives an open $W'\ni y$ with $p^{-1}(W')\subseteq\bigcup J$; this $W'$ is one of the open sets counted in $U_J$, so $p^{-1}(W')\subseteq U_J$, and $y\in p(U_J)$ because $y=p(x)$ for any $x\in p^{-1}(W')$. Conversely every open set counted in $U_J$ has its preimage in $\bigcup J\subseteq p^{-1}(W)$, so $U_J\subseteq p^{-1}(W)$ and $p(U_J)\subseteq W$. Hence $y\in p(U_J)\subseteq W$.
:::

:::

::: {.pf-step #second-countable}
(d) If $X$ is second countable, then so is $Y$.

::: pf-proof
Steps [](#basis-family){.pf-ref} and [](#basis-covers){.pf-ref} exhibit a countable family of open subsets of $Y$ that is a basis: for every point $y$ and every open set $W$ containing it, a member of the family lies between them. So $Y$ is second countable, and parts (a)--(d) are proved.
:::

:::

:::

:::
