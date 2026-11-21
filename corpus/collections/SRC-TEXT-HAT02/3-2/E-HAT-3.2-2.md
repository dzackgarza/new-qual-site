---
schema: qual/card@1
id: E-HAT-3.2-2
kind: problem
title: Cup products vanish on unions of contractible open sets
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: $H^p(A;R)=0$ for $p>0$ makes $H^p(X,A;R)\to H^p(X;R)$ surjective, so
    positive-dimensional classes lift to the relative groups, and the relative cup product lands in
    $H^{p+q}(X,A\cup B;R)=0$; forgetting the relative structure gives $x\smile y=0$. The $n$-fold
    statement is the same iteration with $A_1\cup\cdots\cup A_n=X$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 2 (p.229) including the suspension remark and the n-fold generalization. Rechecked: contractibility of A and B kills their positive cohomology, so positive-degree classes lift to the relative groups by exactness of the sequence of the pair (p.200), and the relative cup product of p.209 lands in H^*(X,X) = 0; forgetting the relative structure gives the absolute product. The n-fold case iterates the same pairing. Citations added for p.200 and p.209. Not covered: no statement about infinite unions, which the exercise does not ask.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the two lifts, the relative product which vanishes
    because $A\cup B=X$, the suspension case, and the induction for $n$ contractible open subsets. No
    retained solution set covers this exercise, so the argument is the card's own; it was re-read for this
    pass and each use of the relative cup product is now its own step.
---

::: {.problem}
Using the cup product $H^k(X, A; R) \times H^\ell(X, B; R) \to H^{k+\ell}(X, A \cup B; R)$, show that if $X$ is the union of contractible open subsets $A$ and $B$, then all cup products of positive-dimensional classes in $H^*(X; R)$ are zero.
This applies in particular if $X$ is a suspension.
Generalize to the situation that $X$ is the union of $n$ contractible open subsets, to show that all $n$-fold cup products of positive-dimensional classes are zero.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The tools are the long exact cohomology sequence of a pair and the relative cup product $H^{k}(X,A;R)\times H^{\ell}(X,B;R)\to H^{k+\ell}(X,A\cup B;R)$, which is available when $A$ and $B$ are open in $X$.

::: pf

::: {.pf-step #lift}
With $X=A\cup B$, $A$ and $B$ contractible and open, every class of positive degree lifts to a relative class: if $x\in H^{p}(X;R)$ with $p>0$ there is $\bar x\in H^{p}(X,A;R)$ mapping to $x$, and likewise for $B$.

::: pf-proof
The pair $(X,A)$ gives the exact sequence $\cdots\to H^{p}(X,A)\to H^{p}(X)\to H^{p}(A)\to\cdots$; the map $H^{p}(X)\to H^{p}(A)$ is restriction along the inclusion. Since $A$ is contractible, $H^{p}(A;R)=0$ for $p>0$, so the restriction is the zero map and exactness shows the map $H^{p}(X,A)\to H^{p}(X)$ is surjective. Hence $x$ has a preimage $\bar x$. The same argument with $B$ gives $\bar y\in H^{q}(X,B)$ for $y\in H^{q}(X;R)$.
:::

:::

::: {.pf-step #product}
For $x,y$ of positive degree, $x\smile y=0$.

::: pf-proof
By step [](#lift){.pf-ref} choose the lifts $\bar x\in H^{p}(X,A)$ and $\bar y\in H^{q}(X,B)$. Because $A$ and $B$ are open, the relative cup product is defined, and $\bar x\smile\bar y\in H^{p+q}(X,A\cup B;R)=H^{p+q}(X,X;R)=0$, the relative group of a pair whose second space is the whole space vanishing in every degree. Forgetting the relative structure is a ring map $H^{*}(X,A\cup B)\to H^{*}(X)$, so it sends $\bar x\smile\bar y$ to $x\smile y$; the image of $0$ is $0$, hence $x\smile y=0$. As $x,y$ were arbitrary classes of positive degree, all cup products of positive-dimensional classes vanish.
:::

:::

::: {.pf-step #suspension}
The same vanishing holds for a suspension.

::: pf-proof
The suspension $\Sigma Y$ is the union of the two cones $CY$ on $Y$, each of which is contractible, and the two cones are open in $\Sigma Y$ after removing the obvious closed cores, or one replaces them by slightly enlarged open cones with the same contractibility. So $\Sigma Y$ is the union of two contractible open subsets, and step [](#product){.pf-ref} applies.
:::

:::

::: {.pf-step}
If $X=A_{1}\cup\cdots\cup A_{n}$ with each $A_{i}$ contractible and open, then every $n$-fold cup product of positive-dimensional classes vanishes.

::: pf-proof
Induction on $n$, with the case $n=2$ being step [](#product){.pf-ref}. For the step, let $x_{1},\dots,x_{n}\in H^{*}(X;R)$ have positive degrees $d_{i}$, each $A_{i}$ open and contractible. As in step [](#lift){.pf-ref} each $x_{i}$ lifts to $\bar x_{i}\in H^{d_{i}}(X,A_{i};R)$, since $H^{d_{i}}(A_{i};R)=0$ for $d_{i}>0$. Applying the relative cup product inductively over the open sets $A_{1},\dots,A_{n}$ gives
$$
\bar x_{1}\smile\cdots\smile\bar x_{n}\in H^{d_{1}+\cdots+d_{n}}(X,A_{1}\cup\cdots\cup A_{n};R)=H^{d_{1}+\cdots+d_{n}}(X,X;R)=0,
$$
the last group vanishing because $A_{1}\cup\cdots\cup A_{n}=X$. The map forgetting relative structure sends this class to $x_{1}\smile\cdots\smile x_{n}$, so that product is $0$. Hence every $n$-fold product of positive-dimensional classes vanishes, as claimed.
:::

:::

:::
:::
