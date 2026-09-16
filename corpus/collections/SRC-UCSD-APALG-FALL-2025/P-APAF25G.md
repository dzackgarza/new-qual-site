---
schema: qual/card@1
id: P-APAF25G
kind: problem
title: Averaged character formula $\frac{1}{|G|}\sum_h\chi(g_1hg_2h^{-1})=\frac{\chi(g_1)\chi(g_2)}{\dim V}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $(V,\varphi)$ be a finite-dimensional irreducible complex representation of a finite group $G$, and let $\chi$ be its character.
Show that for any $g_1,g_2\in G$ we have
\[
\frac{1}{|G|}\sum_{h\in G}\chi(g_1hg_2h^{-1})=\frac{\chi(g_1)\chi(g_2)}{\dim V}.
\]
:::

::: {.solution}
Let \(d=\dim V\) and define
\[
T:=\frac1{|G|}\sum_{h\in G}\varphi(h)\varphi(g_2)\varphi(h)^{-1}.
\]

<1>1. The operator \(T\) commutes with \(\varphi(k)\) for every \(k\in G\).
::: {.proof}
For \(k\in G\),
\[
\begin{aligned}
\varphi(k)T\varphi(k)^{-1}
&=\frac1{|G|}\sum_{h\in G}
\varphi(kh)\varphi(g_2)\varphi(kh)^{-1}.
\end{aligned}
\]
As \(h\) runs through \(G\), so does \(kh\). Hence this sum is exactly \(T\). Therefore
\[
\varphi(k)T=T\varphi(k).
\]
:::

<1>2. Since \(V\) is irreducible, there is \(c\in\mathbb C\) such that
\[
T=cI_V.
\]
::: {.proof}
By <1>1, \(T\) is an endomorphism of the irreducible \(G\)-module \(V\). Schur's lemma over \(\mathbb C\) therefore implies that \(T\) is scalar.
:::

<1>3. The scalar is
\[
c=\frac{\chi(g_2)}{d}.
\]
::: {.proof}
Taking traces in the definition of \(T\) and using invariance of trace under conjugation,
\[
\operatorname{Tr}(T)
=\frac1{|G|}\sum_{h\in G}\operatorname{Tr}\bigl(\varphi(h)\varphi(g_2)\varphi(h)^{-1}\bigr)
=\frac1{|G|}\sum_{h\in G}\chi(g_2)
=\chi(g_2).
\]
On the other hand, by <1>2,
\[
\operatorname{Tr}(T)=\operatorname{Tr}(cI_V)=cd.
\]
Thus \(cd=\chi(g_2)\), giving the formula.
:::

<1>4. Therefore
\[
\frac1{|G|}\sum_{h\in G}\chi(g_1hg_2h^{-1})
=\frac{\chi(g_1)\chi(g_2)}{d}.
\]
::: {.proof}
Using multiplicativity of the representation and linearity of trace,
\[
\begin{aligned}
\frac1{|G|}\sum_{h\in G}\chi(g_1hg_2h^{-1})
&=\frac1{|G|}\sum_{h\in G}
\operatorname{Tr}\bigl(\varphi(g_1)\varphi(h)\varphi(g_2)\varphi(h)^{-1}\bigr)\\
&=\operatorname{Tr}(\varphi(g_1)T).
\end{aligned}
\]
By <1>3,
\[
\operatorname{Tr}(\varphi(g_1)T)
=\frac{\chi(g_2)}{d}\operatorname{Tr}(\varphi(g_1))
=\frac{\chi(g_1)\chi(g_2)}{d}.
\]
:::
:::
