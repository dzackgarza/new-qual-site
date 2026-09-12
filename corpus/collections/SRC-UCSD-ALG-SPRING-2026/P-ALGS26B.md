---
schema: qual/card@1
id: P-ALGS26B
kind: problem
title: "Normal p-subgroup and Sylow subgroups of subgroups"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Suppose $G$ is a finite group and $p$ is a prime divisor of $|G|$. Let
$\operatorname{Syl}_p(G)$ denote the set of all Sylow $p$-subgroups of $G$, and
$$
O_p(G) := \bigcap_{P \in \operatorname{Syl}_p(G)} P.
$$

(a) Prove that $O_p(G)$ is the largest normal $p$-subgroup of $G$.

(b) Suppose $H$ is a subgroup of $G$. Prove that there exists a function
$f : \operatorname{Syl}_p(H) \to \operatorname{Syl}_p(G)$ such that $f(P) \cap H = P$.

(c) Prove that if $|\operatorname{Syl}_p(H)| = |\operatorname{Syl}_p(G)|$, then
$O_p(H) = O_p(G) \cap H$.

Hint: Show that the function $f$ given in the previous part is a bijection.

(d) Prove that if $O_p(G) = 1$ and $\bar{P}$ is a non-trivial $p$-subgroup of $G$, then
$|\operatorname{Syl}_p(N_G(\bar{P}))| < |\operatorname{Syl}_p(G)|$.
:::

::: {.solution}
<1>1. The subgroup \(O_p(G)\) is a normal \(p\)-subgroup of \(G\).
::: {.proof}
Each Sylow \(p\)-subgroup is a \(p\)-group, so their intersection is again a
\(p\)-group. Conjugation permutes the Sylow \(p\)-subgroups of \(G\), hence
\[
gO_p(G)g^{-1}
 = \bigcap_{P\in\operatorname{Syl}_p(G)} gPg^{-1}
 = \bigcap_{P\in\operatorname{Syl}_p(G)} P
 = O_p(G)
\]
for every \(g\in G\). Thus \(O_p(G)\trianglelefteq G\).
:::

<1>2. Every normal \(p\)-subgroup \(N\trianglelefteq G\) is contained in \(O_p(G)\).
::: {.proof}
Fix \(P\in\operatorname{Syl}_p(G)\). Since \(N\trianglelefteq G\), the product \(NP\) is
a subgroup of \(G\). Both \(N\) and \(P\) are \(p\)-groups, so
\[
|NP|=\frac{|N||P|}{|N\cap P|}
\]
is a power of \(p\). By maximality of the Sylow subgroup \(P\), one has \(NP=P\), hence
\(N\le P\). Since this holds for every Sylow \(p\)-subgroup \(P\),
\[
N\le \bigcap_{P\in\operatorname{Syl}_p(G)}P=O_p(G).
\]
Together with <1>1, this proves part (a).
:::

<1>3. For every \(P\in\operatorname{Syl}_p(H)\), there exists
\(Q\in\operatorname{Syl}_p(G)\) such that \(Q\cap H=P\).
::: {.proof}
Since \(P\) is a \(p\)-subgroup of \(G\), it is contained in some Sylow \(p\)-subgroup
\(Q\) of \(G\). Then
\[
P\le Q\cap H.
\]
The subgroup \(Q\cap H\) is a \(p\)-subgroup of \(H\). Since \(P\) is Sylow in \(H\),
maximality gives \(Q\cap H=P\).
:::

<1>4. Choosing one such \(Q\) for each \(P\in\operatorname{Syl}_p(H)\) defines a
function
\[
f:\operatorname{Syl}_p(H)\longrightarrow\operatorname{Syl}_p(G)
\]
with \(f(P)\cap H=P\).
::: {.proof}
This is exactly the construction in <1>3, and proves part (b).
:::

<1>5. The function \(f\) from part (b) is injective.
::: {.proof}
If \(f(P_1)=f(P_2)=Q\), then
\[
P_1=Q\cap H=P_2.
\]
Hence \(P_1=P_2\).
:::

<1>6. If \(|\operatorname{Syl}_p(H)|=|\operatorname{Syl}_p(G)|\), then \(f\) is
bijective and
\[
O_p(H)=O_p(G)\cap H.
\]
::: {.proof}
By <1>5, \(f\) is an injection between finite sets of the same cardinality, hence a
bijection. Therefore every \(Q\in\operatorname{Syl}_p(G)\) is \(f(P)\) for a unique
\(P\in\operatorname{Syl}_p(H)\), and for that \(P\) one has \(P=Q\cap H\). Thus
\[
\begin{aligned}
O_p(H)
 &= \bigcap_{P\in\operatorname{Syl}_p(H)}P \\
 &= \bigcap_{Q\in\operatorname{Syl}_p(G)}(Q\cap H) \\
 &= \left(\bigcap_{Q\in\operatorname{Syl}_p(G)}Q\right)\cap H \\
 &= O_p(G)\cap H.
\end{aligned}
\]
This proves part (c).
:::

<1>7. Let \(\bar P\neq1\) be a \(p\)-subgroup of \(G\), and put \(H=N_G(\bar P)\). Then
\(O_p(H)\neq1\).
::: {.proof}
By definition of the normalizer, \(\bar P\trianglelefteq H\). Since \(\bar P\) is a
nontrivial normal \(p\)-subgroup of \(H\), part (a), applied to \(H\), gives
\[
1\neq\bar P\le O_p(H).
\]
:::

<1>8. If \(O_p(G)=1\), then
\[
|\operatorname{Syl}_p(N_G(\bar P))|<|\operatorname{Syl}_p(G)|.
\]
::: {.proof}
Part (b) gives an injection
\[
\operatorname{Syl}_p(H)\hookrightarrow\operatorname{Syl}_p(G),
\]
so \(|\operatorname{Syl}_p(H)|\le |\operatorname{Syl}_p(G)|\). If equality held, part
(c) would imply
\[
O_p(H)=O_p(G)\cap H=1,
\]
contradicting <1>7. Hence the inequality is strict. Since \(H=N_G(\bar P)\), this is
exactly part (d).
:::
:::
