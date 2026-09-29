---
schema: qual/card@1
id: P-ALGS23B
kind: problem
title: "Sylow p-subgroups with trivial pairwise intersections and congruence condition"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $G$ is a finite group of order $p^k m$ where $p$ is prime and $p \nmid m$. Let
$\operatorname{Syl}_p(G)$ be the set of all the Sylow $p$-subgroups of $G$. Suppose
$P_1 \cap P_2 = \{1\}$ for every two distinct Sylow $p$-subgroups $P_1$ and $P_2$.

(a) Prove that $N_G(P_1) \cap P_2 = \{1\}$, where $P_1, P_2 \in \operatorname{Syl}_p(G)$
are distinct.

(b) Suppose $P_0 \in \operatorname{Syl}_p(G)$ and consider its action on
$\operatorname{Syl}_p(G)$ by conjugation. For $P \in \operatorname{Syl}_p(G)$, let
$\mathcal{O}_P$ be the $P_0$-orbit of $P$. Prove that if $P \neq P_0$, then
$|\mathcal{O}_P| = p^k$.

(c) Prove that $|G| \equiv 1 \pmod{p^k}$.
:::

::: {.solution}
**(a).**

::: pf

::: pf-step

Let \(P_1,P_2\in\operatorname{Syl}_p(G)\) be distinct and put
\[
K=N_G(P_1)\cap P_2.
\]
Then \(K\) is a \(p\)-subgroup of \(N_G(P_1)\).

::: pf-proof

The group \(K\) is a subgroup of the \(p\)-group \(P_2\), so its order is a power of
\(p\). By definition it also lies in \(N_G(P_1)\).

:::

:::

::: {.pf-step #s2}

The product \(P_1K\) is a \(p\)-subgroup of \(G\).

::: pf-proof

Because \(K\le N_G(P_1)\), the subgroup \(P_1\) is normal in \(P_1K\). Therefore
\[
|P_1K|=\frac{|P_1||K|}{|P_1\cap K|}
\]
is a power of \(p\), so \(P_1K\) is a \(p\)-subgroup of \(G\).

:::

:::

::: {.pf-step #s3}

Since \(P_1\) is Sylow, \(P_1K=P_1\), hence \(K\le P_1\). Therefore
\[
N_G(P_1)\cap P_2=K\le P_1\cap P_2=1.
\]

::: pf-proof

A Sylow \(p\)-subgroup is maximal among \(p\)-subgroups. By step [](#s2){.pf-ref}, \(P_1K\) is a
\(p\)-subgroup containing \(P_1\), so equality holds. Thus \(K\le P_1\). The standing
hypothesis gives \(P_1\cap P_2=1\) because \(P_1\ne P_2\).

**(b).**

:::

:::

::: {.pf-step #s4}

For \(P\in\operatorname{Syl}_p(G)\), the stabilizer of \(P\) under conjugation by
\(P_0\) is
\[
\operatorname{Stab}_{P_0}(P)=P_0\cap N_G(P).
\]

::: pf-proof

An element \(x\in P_0\) fixes \(P\) under conjugation exactly when \(xPx^{-1}=P\), which
is exactly the condition \(x\in N_G(P)\).

:::

:::

::: {.pf-step #s5}

If \(P\ne P_0\), then \(\operatorname{Stab}_{P_0}(P)=1\).

::: pf-proof

Apply part (a), step [](#s3){.pf-ref}, with \(P_1=P\) and \(P_2=P_0\). Then
\[
N_G(P)\cap P_0=1.
\]
Combine this with step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

If \(P\ne P_0\), then
\[
|\mathcal O_P|=p^k.
\]

::: pf-proof

By orbit-stabilizer and step [](#s5){.pf-ref},
\[
|\mathcal O_P|=[P_0:\operatorname{Stab}_{P_0}(P)]=|P_0|=p^k.
\]

**(c).**

:::

:::

::: pf-step

Part (c) is false as printed in the source: the hypothesis \(|G|=p^km\) implies
\[
|G|\equiv0\pmod{p^k},
\]
not \(1\pmod{p^k}\).

::: pf-proof

The integer \(p^k\) divides \(|G|\) by the first sentence of the problem. Thus the
requested congruence cannot hold for \(k\ge1\).

:::

:::

::: pf-step

The conclusion that follows from part (b), and hence the evidently intended
statement, is
\[
|\operatorname{Syl}_p(G)|\equiv1\pmod{p^k}.
\]

::: pf-proof

Let \(P_0\) act by conjugation on \(\operatorname{Syl}_p(G)\). The subgroup \(P_0\)
itself is fixed. By step [](#s6){.pf-ref}, every orbit not equal to \(\{P_0\}\) has exactly \(p^k\)
elements. Thus for some integer \(r\ge0\),
\[
|\operatorname{Syl}_p(G)|=1+r p^k,
\]
which is the claimed congruence.

:::

:::

:::

:::
