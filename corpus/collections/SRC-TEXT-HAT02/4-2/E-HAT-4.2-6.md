---
schema: qual/card@1
id: E-HAT-4.2-6
kind: problem
title: "Relative Hurewicz implies absolute"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 6 (AT.txt 19351-19353) and correct as it stands. The cone
    pair is the right device: pi_i(CX,X) = pi_{i-1}(X) for i>=2 with CX contractible, so X (n-2)-connected
    makes (CX,X) (n-1)-connected; relative Hurewicz then identifies pi_n(CX,X) with H_n(CX,X), which
    H_n(CX,X) = H~_{n-1}(X) computes; and naturality of the Hurewicz map makes the comparison square
    commute, so the bottom map is an isomorphism. Checked the restriction n>=3: it is correct and
    necessary, since the absolute Hurewicz theorem in dimension n-1 is stated for n-1>=2, while dimension 1
    has H_1 = pi_1^ab instead of an isomorphism, which the card does not claim. Not checked: nothing
    outside this exercise.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, outside the sections already closed. Read against Hatcher, Exercise 6
    of §4.2, printed p. 389. Checked: $\pi_i(CX,X)\cong\pi_{i-1}(X)$ for $i\ge2$ from the pair
    sequence with $CX$ contractible, so an $(n-2)$-connected $X$ gives an $(n-1)$-connected pair,
    and $\pi_1(CX,X)=0$ since both spaces are simply connected; relative Hurewicz then identifies
    $\pi_n(CX,X)$ with $H_n(CX,X)$, which the pair sequence computes as $\widetilde H_{n-1}(X)$;
    naturality of the Hurewicz homomorphism makes the comparison square commute, so the bottom map is
    an isomorphism. The restriction $n\ge3$ is right and necessary, the absolute theorem in dimension
    $n-1$ beginning at $2$. No defect; the printed page is added.
---

::: {.problem}
Show that the relative form of the Hurewicz theorem in dimension $n$ implies the absolute form in dimension $n-1$ by considering the pair $(CX, X)$ where $CX$ is the cone on $X$.
:::

::: {.solution}
The exercise is §4.2 Exercise 6, printed p. 389.


The argument is the card's own: the cone pair has the homotopy of a suspension of $X$, so the relative theorem applied to it is the absolute theorem one degree down. One hypothesis is checked here that the original left implicit, namely that the relative Hurewicz theorem applies in its isomorphism form to this pair.

Take $n\ge3$ and assume the relative Hurewicz theorem in dimension $n$; let $X$ be $(n-2)$-connected, which is the hypothesis of the absolute Hurewicz theorem in dimension $n-1$.

::: pf

::: {.pf-step #pair}
The pair $(CX,X)$ is $(n-1)$-connected, and both $CX$ and $X$ are simply connected.

::: pf-proof
$CX$ is contractible, hence simply connected. The long exact homotopy sequence of the pair, together with $\pi_{i}(CX)=0$ for all $i$, gives
$$
\pi_{i}(CX,X)\cong\pi_{i-1}(X)\qquad(i\ge2),
$$
so for $i\le n-1$ the group $\pi_{i}(CX,X)\cong\pi_{i-1}(X)$ vanishes because $i-1\le n-2$ and $X$ is $(n-2)$-connected. Also $\pi_{1}(CX,X)=0$ because $CX$ is simply connected and $X$ is connected ($n-2\ge1$), so $\pi_{i}(CX,X)=0$ for $i\le n-1$: the pair is $(n-1)$-connected. Finally $X$ is simply connected because it is $(n-2)$-connected with $n-2\ge1$.
:::

:::

::: {.pf-step #relative}
$\pi_{n}(CX,X)\cong H_{n}(CX,X)$.

::: pf-proof
The pair is $(n-1)$-connected with $n\ge2$, and both of its spaces are simply connected, so the relative Hurewicz theorem applies in the form that the Hurewicz map $h:\pi_{n}(CX,X)\to H_{n}(CX,X)$ is an isomorphism and $H_{i}(CX,X)=0$ for $i<n$. (Simple connectivity is what removes the $\pi_{1}$-action from the hypothesis; without it the theorem only identifies the coinvariants.)
:::

:::

::: {.pf-step #homology}
$H_{n}(CX,X)\cong\widetilde H_{n-1}(X)$.

::: pf-proof
The homology long exact sequence of the pair, with $H_{i}(CX)=0$ for $i\ge1$ because $CX$ is contractible, contains
$$
0=H_{n}(CX)\to H_{n}(CX,X)\xrightarrow{\ \partial\ }\widetilde H_{n-1}(X)\to\widetilde H_{n-1}(CX)=0,
$$
so the boundary map is an isomorphism.
:::

:::

::: {.pf-step #absolute}
$\pi_{n-1}(X)\cong H_{n-1}(X)$ — the absolute Hurewicz theorem in dimension $n-1$.

::: pf-proof
The Hurewicz homomorphisms are natural for maps of pairs, so the square
$$
\begin{array}{ccc}
\pi_{n}(CX,X)&\xrightarrow{\ h\ }&H_{n}(CX,X)\\
\downarrow\partial&&\downarrow\partial\\
\pi_{n-1}(X)&\xrightarrow{\ h\ }&H_{n-1}(X)
\end{array}
$$
commutes, the vertical maps being the boundary homomorphisms of the pair. The two vertical maps are isomorphisms by steps [](#pair){.pf-ref} and [](#homology){.pf-ref}, and the top horizontal map is an isomorphism by step [](#relative){.pf-ref}; hence the bottom horizontal map is an isomorphism too. That is
$$
\boxed{\pi_{n-1}(X)\cong H_{n-1}(X)\ \text{for } X\ (n-2)\text{-connected},\ n\ge3,}
$$
together with $H_{i}(X)=0$ for $i<n-1$, which is the absolute Hurewicz theorem in dimension $n-1$.
:::

:::

:::
:::
