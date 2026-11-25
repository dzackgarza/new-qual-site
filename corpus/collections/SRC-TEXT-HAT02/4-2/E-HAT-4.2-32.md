---
schema: qual/card@1
id: E-HAT-4.2-32
kind: problem
title: "Fiber bundles $S^k \to S^m \to S^n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §4.2. Read against Hatcher, Exercise 32 of §4.2, printed p. 392, and
    the printed page is added, the card having had none. Checked: dimensions add, $m=n+k$; for
    $n\ge2$ a fibre $S^0$ would make $S^m$ a nontrivial two-sheeted cover of the simply connected
    $S^n$, hence disconnected, so $k\ge1$; the exact sequence at $\pi_n$ injects $\pi_n(S^n)=\ZZ$
    into $\pi_{n-1}(S^k)$ because $\pi_n(S^m)=0$ for $m>n$, giving $k\le n-1$; the sequence at
    $\pi_k$ surjects $\pi_{k+1}(S^n)$ onto $\pi_k(S^k)=\ZZ$ because $\pi_k(S^m)=0$ for $m>k$,
    giving $k+1\ge n$; so $k=n-1$ and $m=2n-1$; and for $n=1$ the case $k\ge1$ would force
    $\pi_1(S^m)\neq0$, hence $m=1$, against $m=1+k\ge2$, so $k=0$ and the bundle is $S^0\to S^1\to
    S^1$. One addition: the statement's conclusion has no content at $n=0$, where a bundle over
    $S^0$ is trivial and connectedness forces $m=k=0$, giving $k=0\ne n-1$; the card now says that
    the two cases treated are exactly the meaningful ones. The published solution cited for the
    upper bound is Proudfoot, Homework #7, Problem 32, whose text stops at $k\le n-1$; the lower
    bound is the card's own and was checked directly.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 32. One false provenance sentence repaired: the card said
    Proudfoot's retained Problem 32 stops at $k\le n-1$ and does not reach the reverse inequality.
    His solution does reach $k=n-1$, and the paragraph now says so and leaves the sequence's two
    inequalities to step `lower`, which is where the card checks them.
review: draft
---

::: {.problem}
Show that if $S^k \to S^m \to S^n$ is a fiber bundle, then $k = n-1$ and $m = 2n-1$. [Look at the long exact sequence of homotopy groups.]
:::

::: {.solution}
The exercise is §4.2 Exercise 32.

The argument is the card's own: the homotopy exact sequence of the bundle in two degrees pins $k$ between $n-1$ and $n-1$. A published solution covers the exercise: Proudfoot, *Math 634: Algebraic Topology I*, Fall 2015, Homework #7, Problem 32, which derives $k<n$ and $\pi_{n-1}(S^{k})\cong\ZZ$ from the long exact sequence and reaches $k=n-1$; both inequalities are read off that sequence of Theorem 4.41, and step [](#lower){.pf-ref} below records the second one. Throughout $S^{k}\to S^{m}\to S^{n}$ is a fibre bundle with connected total space $S^{m}$.

::: pf

::: {.pf-step #dimension}
$m=n+k$, and for $n\ge2$ one has $k\ge1$.

::: pf-proof
A fibre bundle is locally a product, so $\dim S^{m}=\dim S^{n}+\dim S^{k}$, that is $m=n+k$. If $n\ge2$ then $S^{n}$ is simply connected, so a bundle with fibre $S^{0}$ would be a two-sheeted covering of $S^{n}$, whose total space is disconnected; but $S^{m}$ is connected. So $k\ne0$, that is $k\ge1$, and then $m=n+k>n$.
:::

:::

::: {.pf-step #upper}
For $n\ge2$, $k\le n-1$.

::: pf-proof
The homotopy exact sequence of the bundle contains
$$
\pi_{n}(S^{m})\longrightarrow\pi_{n}(S^{n})\longrightarrow\pi_{n-1}(S^{k}).
$$
Since $m>n$ one has $\pi_{n}(S^{m})=0$, so the map $\pi_{n}(S^{n})\to\pi_{n-1}(S^{k})$ has zero kernel; it therefore injects $\ZZ=\pi_{n}(S^{n})$ into $\pi_{n-1}(S^{k})$, which is thus nonzero. And $\pi_{j}(S^{k})=0$ for $j<k$, so $\pi_{n-1}(S^{k})\ne0$ forces $n-1\ge k$.
:::

:::

::: {.pf-step #lower}
For $n\ge2$, $k\ge n-1$.

::: pf-proof
The sequence contains
$$
\pi_{k+1}(S^{n})\longrightarrow\pi_{k}(S^{k})\longrightarrow\pi_{k}(S^{m}).
$$
Since $m=n+k>k$ one has $\pi_{k}(S^{m})=0$, so the second map is onto the zero group and exactness makes the first map surjective onto $\ZZ=\pi_{k}(S^{k})$; hence $\pi_{k+1}(S^{n})\ne0$, which by $\pi_{j}(S^{n})=0$ for $j<n$ forces $k+1\ge n$.
:::

:::

::: {.pf-step #conclusion}
For $n\ge2$, $k=n-1$ and $m=2n-1$.

::: pf-proof
Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give $k\le n-1\le k$, so $k=n-1$, and step [](#dimension){.pf-ref} gives
$$
\boxed{m=n+k=n+(n-1)=2n-1.}
$$
:::

:::

::: {.pf-step #circle}
For $n=1$, $k=0$ and $m=1$, again $k=n-1$ and $m=2n-1$.

::: pf-proof
Suppose $k\ge1$. Then $S^{k}$ is connected, so $\pi_{0}(S^{k})=0$, and the exact sequence
$$
\pi_{1}(S^{k})\to\pi_{1}(S^{m})\to\pi_{1}(S^{1})\to\pi_{0}(S^{k})
$$
shows that $\pi_{1}(S^{m})\to\ZZ$ is surjective, so $\pi_{1}(S^{m})\ne0$ and hence $m=1$. But $m=n+k=1+k\ge2$ by step [](#dimension){.pf-ref}, a contradiction. So $k=0$ and $m=1$, which is the double cover $S^{1}\to S^{1}$ with fibre $S^{0}$, and gives $k=n-1=0$ and $m=2n-1=1$.
The case $n=0$ is excluded by the statement itself: a bundle over $S^0$ is trivial, so $S^m\cong S^0\times S^k$, connected only when $m=k=0$, and then $k=0\neq n-1$. The two cases treated above are exactly those in which the printed conclusion has content.

:::

:::

:::
:::
