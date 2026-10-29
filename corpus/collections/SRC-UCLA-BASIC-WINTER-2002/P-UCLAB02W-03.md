---
schema: qual/card@1
id: P-UCLAB02W-03
kind: problem
title: Direct connectedness proof for the open unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Prove directly that the open unit disk
\[
\{(x,y)\in\RR^2:x^2+y^2<1\}
\]
is connected.

You may assume that intervals in $\RR$ are connected, but should not simply quote more general connectedness results.
:::

::: {.solution}

Let
$$
D=\{z\in\RR^2:\norm z<1\}.
$$

::: pf

::: {.pf-step #s1-1}

For every $p\in D$, the radial segment
$$
S_p=\{tp:0\le t\le1\}
$$
is contained in $D$.


::: pf-proof

If $0\le t\le1$, then
$$
\norm{tp}=t\norm p\le\norm p<1.
$$
Hence $tp\in D$ for every $t\in[0,1]$.

:::

:::

::: {.pf-step #s1-2}

Suppose, for contradiction, that $D$ is disconnected. Then there are disjoint nonempty subsets $U,V\subset D$, both open in the subspace topology of $D$, such that
$$
D=U\cup V.
$$
After interchanging $U$ and $V$ if necessary, assume $0\in U$.


::: pf-proof

This is the definition of disconnectedness by a separation into two nonempty relatively open sets. Since $0\in D$, it lies in exactly one of the two sets; rename them if necessary.

:::

:::

::: {.pf-step #s1-3}

No point of $D$ can lie in $V$.


::: pf-proof

Assume instead that $p\in V$. Define
$$
\gamma:[0,1]\to D,
\qquad
\gamma(t)=tp.
$$
Step [](#s1-1){.pf-ref} shows that the map indeed takes values in $D$, and it is continuous.

Set
$$
A=\gamma^{-1}(U),
\qquad
B=\gamma^{-1}(V).
$$
Because $U$ and $V$ are open in $D$ and $\gamma$ is continuous, $A$ and $B$ are open in the subspace topology of $[0,1]$. They are disjoint and satisfy
$$
[0,1]=A\cup B.
$$
Moreover,
$$
0\in A
$$
because $\gamma(0)=0\in U$, while
$$
1\in B
$$
because $\gamma(1)=p\in V$. Thus $A$ and $B$ are both nonempty.

This separates the interval $[0,1]$ into two disjoint nonempty open subsets, contradicting the assumed connectedness of intervals in $\RR$.

:::

:::

::: {.pf-step #s1-4}

Therefore $D$ is connected.


::: pf-proof

If $V$ were nonempty, it would contain some $p\in D$, contradicting step [](#s1-3){.pf-ref}. Hence the separation assumed in step [](#s1-2){.pf-ref} cannot exist.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is precisely the required conclusion for the open unit disk.

:::

:::

:::
