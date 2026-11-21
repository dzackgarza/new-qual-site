---
schema: qual/card@1
id: P-CAFA21B
kind: problem
title: "Polynomial approximation and polynomial hull of a compact set"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the two answers already on the card, False and
    the closed disk of radius 3, both correct. Added: the description of the complement and the
    identification of its two bounded components; the verification that the boundary circles of
    those disks lie in K, which is what makes the maximum-modulus comparison legitimate; the
    explicit contradiction showing 1/(z - 1) is not a uniform limit of polynomials on K, with
    q_n(1) = -1 against sup_K |q_n| -> 0; and the computation that K together with the two
    disks is exactly the closed disk, 0 lying in K. The description of the polynomial hull as K
    plus the bounded complementary components is named as the one external input rather than
    proved. Not claimed: a retained solution set; the provenance names the examination paper.
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UCSD Complex Analysis Qualifying Exam, Fall 2021; both parts match.
---

::: {.problem}
Let $K = \{ z \in \CC : \abs{z} \leq 3,\, \abs{z-1} \geq 1,\, \abs{z+1} \geq 1 \}$.

(i) True/false: every holomorphic function in a neighborhood of $K$ is the local uniform limit on $K$ of a sequence of polynomials.
Please justify your answer.

(ii) Determine, with justification, the set
$$
\widehat{K} = \{ z \in \CC : \abs{p(z)} \leq \sup_{w \in K} \abs{p(w)} \text{ for all polynomials } p \}.
$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2021 complex-analysis examination paper, which carries no solutions. The answers — (i) false, (ii) $\widehat K=\theset{\abs z\le3}$ — are the card's own and follow the card's previous prose, with the one external input named: the description of the polynomial hull as $K$ together with the bounded components of its complement.

Throughout $K=\theset{z:\abs z\le3,\ \abs{z-1}\ge1,\ \abs{z+1}\ge1}$ and $\widehat K=\theset{a:\abs{p(a)}\le\sup_K\abs p\text{ for all polynomials }p}$.

::: pf

::: {.pf-step #complement}
$\CC\setminus K=\theset{\abs z>3}\cup B(1,1)\cup B(-1,1)$, and $B(1,1)$ and $B(-1,1)$ are its two bounded components.

::: pf-proof
$z\notin K$ iff $\abs z>3$ or $\abs{z-1}<1$ or $\abs{z+1}<1$. The set $\theset{\abs z>3}$ is connected and unbounded, and each $B(c,1)$ for $c=\pm1$ is an open disk with boundary circle $\abs{z-c}=1$ contained in $K$ (step [](#circle-in-K){.pf-ref}), so each disk is a connected component of the complement and bounded. The two disks are disjoint since their centres are $2$ apart and their radii sum to $2$.

:::

:::

::: {.pf-step #circle-in-K}
For $c\in\theset{1,-1}$ the circle $\abs{z-c}=1$ lies in $K$; hence for every polynomial $p$ and every $z$ with $\abs{z-c}\le1$, $\abs{p(z)}\le\sup_K\abs p$.

::: pf-proof
On $\abs{z-1}=1$: $\abs z\le2\le3$ and $\abs{z+1}=\abs{(z-1)+2}\ge2-\abs{z-1}=1$; symmetrically $z\mapsto-z$ handles $c=-1$. So the circle lies in $K$. The maximum modulus principle on the closed disk $\overline{B(c,1)}$ gives $\abs{p(z)}\le\max_{\abs{\zeta-c}=1}\abs{p(\zeta)}$ for $\abs{z-c}\le1$, and that maximum is at most $\sup_K\abs p$ since the circle lies in $K$.

:::

:::

::: {.pf-step #hull}
$\widehat K=K\cup B(1,1)\cup B(-1,1)=\theset{\abs z\le3}$.

::: pf-proof
For compact $K\subset\CC$ the polynomial hull is $K$ together with all bounded components of $\CC\setminus K$ — the standard form of the maximum modulus principle, one inclusion being step [](#circle-in-K){.pf-ref} applied componentwise and the other the maximum principle on the boundary of the unbounded component. By step [](#complement){.pf-ref} the bounded components are the two disks, so $\widehat K=K\cup B(1,1)\cup B(-1,1)$, and that union is the closed disk $\abs z\le3$ because $\theset{\abs z\le3}\setminus K$ is exactly the union of the two disks, $\set{0}$ lying in $K$ as $\abs{0-1}=\abs{0+1}=1$.

:::

:::

::: {.pf-step #part-i}
(i) is false: $f(z)=1/(z-1)$ is holomorphic on a neighbourhood of $K$ and is not the uniform limit on $K$ of a sequence of polynomials.

::: pf-proof
$f$ is holomorphic on $\CC\setminus\set{1}$, a neighbourhood of $K$ because $B(1,1)$, which contains $1$, is disjoint from $K$ by step [](#complement){.pf-ref}. Suppose $p_n\to f$ uniformly on $K$ and set $q_n(z)=(z-1)p_n(z)-1$, a polynomial. Since $(z-1)p_n\to(z-1)f=1$ uniformly on $K$, we get $q_n\to0$ uniformly on $K$. But $1\in\widehat K$ by step [](#hull){.pf-ref}, so $\abs{q_n(1)}\le\sup_K\abs{q_n}\to0$, whereas $q_n(1)=-1$ gives $\abs{q_n(1)}=1$ for every $n$. Contradiction.

:::

:::

::: {.pf-step #part-ii}
(ii) $\widehat K=\theset{\abs z\le3}$.

::: pf-proof
This is step [](#hull){.pf-ref}. The reason (i) fails is visible in it: $\widehat K$ strictly contains $K$, and polynomial approximation of a holomorphic function on $K$ would force $\abs{p(a)-f(a)}$ to be small for $a$ in the filled-in disks, which is impossible at the pole $a=1$ while $\sup_K\abs{p_n}$ stays bounded by the maximum principle.

:::

:::

:::
:::
