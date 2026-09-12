---
schema: qual/card@1
id: P-PERUTZ08-3.4
kind: problem
title: PSL_2(Z) as the free product C_2*C_3
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.4 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
---

::: {.problem}
Let
\[
S=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
U=ST=\begin{pmatrix}0&1\\-1&1\end{pmatrix}
\]
in $\operatorname{SL}_2(\mathbb Z)$.

1. Verify that $S^2=U^3=-I$.
2. Show that, for every $A\in\operatorname{SL}_2(\mathbb Z)$, there is $n\in\mathbb Z$ such that if
   \[
   AT^n=\begin{pmatrix}a&b\\c&d\end{pmatrix},
   \]
   then either $c=0$ or $|d|\le |c|/2$.
3. Explain how to find $\ell\ge0$ and integers $n_1,\dots,n_\ell$ such that either
   \[
   AT^{n_1}ST^{n_2}S\cdots ST^{n_\ell}
   \]
   or the same product followed by $S$ has lower-left entry zero.
4. Show that $S$ and $T$ generate $\operatorname{SL}_2(\mathbb Z)$.
5. Define
   \[
   \theta:(\mathbb Z/2)*(\mathbb Z/3)=\langle a,b\mid a^2,b^3\rangle\to\operatorname{PSL}_2(\mathbb Z)
   \]
   by $\theta(a)=\pm S$ and $\theta(b)=\pm U$. Using the Möbius action on the upper half-plane $\mathbb H$, prove that for every nontrivial word $w$ the map $\mu_w$ corresponding to $\theta(w)$ satisfies $\mu_w(D)\cap D=\varnothing$, where
   \[
   D=\{z\in\mathbb H:0<\operatorname{Re}z<1/2,\ |z-1|>1\}.
   \]
   Deduce that $\theta$ is an isomorphism.

For the last part, the source suggests considering
\[
A=\{z\in\mathbb H:\operatorname{Re}z>0\},\qquad
B=\{z\in\mathbb H:|z-1|>\max(1,|z|)\}.
\]
:::
