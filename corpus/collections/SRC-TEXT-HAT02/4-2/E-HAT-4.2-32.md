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
review: draft
---

::: {.problem}
Show that if $S^k \to S^m \to S^n$ is a fiber bundle, then $k = n-1$ and $m = 2n-1$. [Look at the long exact sequence of homotopy groups.]
:::

::: {.solution}

The argument is the card's own: the homotopy exact sequence of the bundle in two degrees pins $k$ between $n-1$ and $n-1$. A published solution exists and is cited here for the two steps it does carry: Proudfoot, *Math 634: Algebraic Topology I*, Fall 2015, Homework #7, Problem 32, which derives $k<n$ and $\pi_{n-1}(S^{k})\cong\ZZ$ from the long exact sequence and stops at $k\le n-1$; the reverse inequality, which his retained text does not reach, is step [](#lower){.pf-ref} below, and both inequalities are read off the same exact sequence of Theorem 4.41, printed p. 376. Throughout $S^{k}\to S^{m}\to S^{n}$ is a fibre bundle with connected total space $S^{m}$.

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
:::

:::

:::
:::
