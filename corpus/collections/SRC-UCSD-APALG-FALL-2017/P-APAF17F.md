---
schema: qual/card@1
id: P-APAF17F
kind: problem
title: Induced $S_5$-module from $S^{(2)}\otimes S^{(2)}\otimes S^{(1)}$; $\operatorname{End}$ and sign projector
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
For a partition $\lambda\vdash n$, let $S^\lambda$ be the corresponding irreducible representation of the symmetric group $S_n$ over $\mathbb{C}$.

(a) Calculate the decomposition of the induced module
\[
V=(S^{(2)}\otimes S^{(2)}\otimes S^{(1)})\uparrow_{S_2\times S_2\times S_1}^{S_5}
\]
into irreducible $S_5$-modules.

(b) What is the dimension over $\mathbb{C}$ of the endomorphism algebra $\operatorname{End}_{S_5}(V)$?

(c) For any permutation $\sigma\in S_5$, let $\operatorname{sign}(\sigma)$ be the sign of $\sigma$.
Define a linear operator $\varphi\colon V\to V$ by
\[
\varphi(v)=\frac{1}{5!}\sum_{\sigma\in S_5}\operatorname{sign}(\sigma)\,v.
\]
What is the rank of the operator $\varphi$?
:::

::: remark
As printed, the sum in (c) carries no action: $\sum_{\sigma\in S_5}\operatorname{sign}(\sigma)=0$, so the printed formula makes $\varphi$ the zero map, whose rank is $0$.
The question is only substantive if the intended operator is the antisymmetrization projector $\varphi(v)=\frac{1}{5!}\sum_{\sigma}\operatorname{sign}(\sigma)\,\sigma v$.
The statement is left as the exam printed it.
:::

::: {.solution}
<1>1. Under the Frobenius characteristic map,
\[
\operatorname{ch}(V)=s_{(2)}s_{(2)}s_{(1)}.
\]
::: {.proof}
The representations $S^{(2)}$ of $S_2$ and $S^{(1)}$ of $S_1$ are trivial. Induction from a Young subgroup corresponds under the Frobenius characteristic to multiplication of the corresponding Schur functions. Hence the induced module has characteristic $s_{(2)}s_{(2)}s_{(1)}$.
:::

<1>2. One has
\[
s_{(2)}s_{(2)}=s_{(4)}+s_{(3,1)}+s_{(2,2)},
\]
and consequently
\[
s_{(2)}s_{(2)}s_{(1)}
=s_{(5)}+2s_{(4,1)}+2s_{(3,2)}+s_{(3,1,1)}+s_{(2,2,1)}.
\]
::: {.proof}
The first identity follows from the Pieri rule by adding a horizontal $2$-strip to the diagram $(2)$. Multiplying by $s_{(1)}=h_1$ and applying Pieri again gives
\[
\begin{aligned}
s_{(4)}s_{(1)}&=s_{(5)}+s_{(4,1)},\\
s_{(3,1)}s_{(1)}&=s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)},\\
s_{(2,2)}s_{(1)}&=s_{(3,2)}+s_{(2,2,1)}.
\end{aligned}
\]
Adding these identities yields the displayed expansion.
:::

<1>3. Therefore
\[
\boxed{
V\cong
S^{(5)}\oplus2S^{(4,1)}\oplus2S^{(3,2)}\oplus S^{(3,1,1)}\oplus S^{(2,2,1)}.}
\]
::: {.proof}
The Schur functions form the basis corresponding to irreducible $S_5$-characters under the Frobenius characteristic. Thus the coefficients in <1>2 are exactly the irreducible multiplicities. This proves part (a).
:::

<1>4. The endomorphism algebra has dimension
\[
\boxed{11}.
\]
::: {.proof}
For a completely reducible complex representation
\[
V\cong\bigoplus_\lambda m_\lambda S^\lambda,
\]
Schur's lemma gives
\[
\operatorname{End}_{S_5}(V)
\cong\bigoplus_\lambda M_{m_\lambda}(\mathbb C),
\]
so
\[
\dim_\mathbb C\operatorname{End}_{S_5}(V)=\sum_\lambda m_\lambda^2.
\]
Using the multiplicities from <1>3 gives
\[
1^2+2^2+2^2+1^2+1^2=11.
\]
This proves part (b).
:::

<1>5. For the operator exactly as printed in part (c),
\[
\boxed{\operatorname{rank}\varphi=0}.
\]
::: {.proof}
The printed formula contains no action of $\sigma$ on $v$, so
\[
\varphi(v)
=\frac1{5!}\left(\sum_{\sigma\in S_5}\operatorname{sign}(\sigma)\right)v.
\]
There are equally many even and odd permutations in $S_5$, hence
\[
\sum_{\sigma\in S_5}\operatorname{sign}(\sigma)=0.
\]
Therefore $\varphi=0$ and its rank is $0$.
:::

<1>6. If the intended operator was instead the antisymmetrizer
\[
\widetilde\varphi(v)=\frac1{5!}\sum_{\sigma\in S_5}\operatorname{sign}(\sigma)\,\sigma v,
\]
then its rank is also $0$.
::: {.proof}
The antisymmetrizer is the projection onto the sign-isotypic component of $V$. The sign representation of $S_5$ is $S^{(1^5)}$, and <1>3 shows that $S^{(1^5)}$ does not occur in $V$. Hence the sign-isotypic component is zero, so $\widetilde\varphi=0$ as well.
:::
:::
