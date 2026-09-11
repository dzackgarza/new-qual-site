---
schema: qual/card@1
id: P-APAS13E
kind: problem
title: Induced representations and Frobenius reciprocity
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $H$ be a subgroup of $G$ and $A\colon H\to\mathrm{GL}_n(\mathbb{C})$ be a representation of $H$.
Let $\chi^A\colon H\to\mathbb{C}$ be the character of $A$.
Define $\chi^{\overline{A}}\colon G\to\mathbb{C}$ by
\[
\chi^{\overline{A}}(\sigma)=
\begin{cases}
\chi^A(\sigma) & \text{if }\sigma\in H,\\
0 & \text{if }\sigma\in G\setminus H.
\end{cases}
\]

(a) Define the representation $A\uparrow_H^G$.

(b) Prove that
\[
\chi^{A\uparrow_H^G}=\frac{1}{|H|}\sum_{\sigma\in G}\sigma\cdot\chi^{\overline{A}}\cdot\sigma^{-1}.
\]

(c) State and prove the Frobenius Reciprocity Theorem.
:::

::: solution
Let \(V\) be the representation space of \(A\). The induced representation is
\[
\operatorname{Ind}_H^G V
 =\mathbb C[G]\otimes_{\mathbb C[H]}V,
\]
with \(G\) acting by left multiplication on the first tensor factor:
\[
g\cdot(x\otimes v)=(gx)\otimes v.
\]
This is the representation denoted \(A\uparrow_H^G\).

Choose representatives \(t_1,\ldots,t_r\) for the left cosets \(G/H\). Then
\[
\operatorname{Ind}_H^G V
 =\bigoplus_{i=1}^r t_i\otimes V.
\]
Fix \(g\in G\). The operator induced by \(g\) sends the summand \(t_i\otimes V\) to \(t_j\otimes V\) whenever
\[
gt_iH=t_jH.
\]
Hence only those coset summands fixed by \(g\) contribute to the trace. The coset \(t_iH\) is fixed exactly when
\[
t_i^{-1}gt_i\in H.
\]
On such a fixed summand,
\[
g(t_i\otimes v)
=t_i\otimes A(t_i^{-1}gt_i)v,
\]
so its trace is \(\chi^A(t_i^{-1}gt_i)\). Therefore
\[
\chi^{A\uparrow_H^G}(g)
=\sum_{\substack{i\\t_i^{-1}gt_i\in H}}
\chi^A(t_i^{-1}gt_i).
\]

Now each left coset \(t_iH\) contains \(|H|\) elements, and if \(x=t_ih\), then
\[
x^{-1}gx=h^{-1}(t_i^{-1}gt_i)h.
\]
Since \(\chi^A\) is a class function on \(H\), whenever \(t_i^{-1}gt_i\in H\) we have
\[
\chi^A(x^{-1}gx)=\chi^A(t_i^{-1}gt_i).
\]
Thus
\[
\chi^{A\uparrow_H^G}(g)
=\frac1{|H|}\sum_{x\in G}\chi^{\overline A}(x^{-1}gx).
\]
If the action of \(x\in G\) on functions is written as
\[
(x\cdot f\cdot x^{-1})(g)=f(x^{-1}gx),
\]
this is exactly
\[
\boxed{
\chi^{A\uparrow_H^G}
=\frac1{|H|}\sum_{x\in G}x\cdot\chi^{\overline A}\cdot x^{-1}.}
\]

For part (c), Frobenius reciprocity states that if \(V\) is a finite-dimensional representation of \(H\) with character \(\chi\), and \(W\) is a finite-dimensional representation of \(G\) with character \(\psi\), then
\[
\boxed{
\left\langle \operatorname{Ind}_H^G\chi,\psi\right\rangle_G
=
\left\langle \chi,\operatorname{Res}_H^G\psi\right\rangle_H.}
\]
Equivalently,
\[
\dim\operatorname{Hom}_G(\operatorname{Ind}_H^G V,W)
=
\dim\operatorname{Hom}_H(V,\operatorname{Res}_H^G W).
\]

Using the character formula just proved,
\[
\begin{aligned}
\left\langle \operatorname{Ind}_H^G\chi,\psi\right\rangle_G
&=\frac1{|G|}\sum_{g\in G}
\left(\frac1{|H|}\sum_{x\in G}\chi^{\overline A}(x^{-1}gx)\right)
\overline{\psi(g)}\\
&=\frac1{|G||H|}\sum_{x\in G}\sum_{g\in G}
\chi^{\overline A}(x^{-1}gx)\overline{\psi(g)}.
\end{aligned}
\]
For fixed \(x\), substitute \(h=x^{-1}gx\). Since \(\psi\) is a class function,
\[
\psi(g)=\psi(xhx^{-1})=\psi(h).
\]
Hence the inner sum is independent of \(x\), and
\[
\begin{aligned}
\left\langle \operatorname{Ind}_H^G\chi,\psi\right\rangle_G
&=\frac1{|H|}\sum_{h\in G}\chi^{\overline A}(h)\overline{\psi(h)}\\
&=\frac1{|H|}\sum_{h\in H}\chi(h)\overline{\psi(h)}\\
&=\left\langle \chi,\operatorname{Res}_H^G\psi\right\rangle_H.
\end{aligned}
\]
This proves Frobenius reciprocity.
:::
