---
schema: qual/card@1
id: P-ALGF14B
kind: problem
title: $S_n$ has a subgroup with exactly $n$ Sylow $p$-subgroups
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2014; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the conjugation-action proof, including preservation of Sylow p-subgroups after quotienting by the action kernel and the normalizer-index count.
---

::: {.problem}
Suppose $G$ is a finite group with exactly $n$ Sylow $p$-subgroups and $n$ is at least $2$.
Prove that the symmetric group $S_n$ has a subgroup with exactly $n$ Sylow $p$-subgroups.
:::


::: {.solution}
Let
\[
\Omega=\{P_1,\ldots,P_n\}
\]
be the set of Sylow \(p\)-subgroups of \(G\).
Conjugation gives a homomorphism
\[
\varphi:G\longrightarrow S(\Omega)\cong S_n.
\]
Set
\[
K:=\varphi(G)\le S_n,
\qquad
N:=\ker\varphi.
\]
We will prove that \(K\) has exactly \(n\) Sylow \(p\)-subgroups.

<1>1. For every Sylow \(p\)-subgroup \(P\) of \(G\), one has
\[
N\subseteq N_G(P).
\]
::: {.proof}
An element of \(N\) acts trivially on the whole set \(\Omega\), so in particular it fixes \(P\) under conjugation.
Thus if \(x\in N\), then
\[
xPx^{-1}=P,
\]
which means \(x\in N_G(P)\).
:::

<1>2. The subgroup \(\varphi(P)\) is a Sylow \(p\)-subgroup of \(K\).
::: {.proof}
Because \(N\triangleleft G\), the intersection \(P\cap N\) is a Sylow \(p\)-subgroup of \(N\).
Indeed, a Sylow \(p\)-subgroup of a normal subgroup is the intersection of that normal subgroup with some Sylow \(p\)-subgroup of the whole group, and here we may choose \(P\) itself.
Hence the \(p\)-part of \(|N|\) is \(|P\cap N|\).
Therefore the \(p\)-part of
\[
|G/N|=|K|
\]
is
\[
\frac{|P|}{|P\cap N|}
=|PN/N|
=|\varphi(P)|.
\]
Thus \(\varphi(P)\) is a Sylow \(p\)-subgroup of \(K\).
:::

<1>3. The normalizer of \(\varphi(P)\) in \(K\) is exactly \(\varphi(N_G(P))\).
::: {.proof}
By <1>1, the subgroup \(N\) normalizes \(P\).
Hence \(P\triangleleft PN\).
Since \(P\) is a Sylow \(p\)-subgroup of \(G\), it is also a Sylow \(p\)-subgroup of \(PN\); being normal there, it is the unique Sylow \(p\)-subgroup of \(PN\).

Now
\[
\varphi(P)=PN/N.
\]
If \(gN\in K\) normalizes \(PN/N\), then
\[
g(PN)g^{-1}=PN.
\]
Thus \(gPg^{-1}\) is a Sylow \(p\)-subgroup of \(PN\).
By uniqueness of the Sylow \(p\)-subgroup of \(PN\),
\[
gPg^{-1}=P,
\]
so \(g\in N_G(P)\).
This proves
\[
N_K(\varphi(P))\subseteq \varphi(N_G(P)).
\]
The reverse inclusion is immediate: an element normalizing \(P\) clearly normalizes its image \(\varphi(P)\).
Therefore
\[
N_K(\varphi(P))=\varphi(N_G(P)).
\]
:::

<1>4. The group \(K\le S_n\) has exactly \(n\) Sylow \(p\)-subgroups.
::: {.proof}
By Sylow's theorem, the number of Sylow \(p\)-subgroups of \(K\) is
\[
[K:N_K(\varphi(P))].
\]
Using <1>3 and the fact \(N\subseteq N_G(P)\),
\[
[K:N_K(\varphi(P))]
=[G/N:N_G(P)/N]
=[G:N_G(P)].
\]
The last index is exactly the number of conjugates of \(P\), hence exactly the number of Sylow \(p\)-subgroups of \(G\), which is \(n\).
Thus \(K\) is a subgroup of \(S_n\) with exactly \(n\) Sylow \(p\)-subgroups.
:::
:::
