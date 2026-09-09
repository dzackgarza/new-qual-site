---
schema: qual/card@1
id: P-VMTDC
kind: problem
title: Maschke's theorem
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
State and prove Maschke's theorem.
What can go wrong if you work over the real field?
What can go wrong in characteristic $p$?
:::

::: solution
**Maschke's theorem.** Let $G$ be finite and let $k$ be a field with
\[
\operatorname{char}k\nmid |G|.
\]
Then every finite-dimensional $k$-representation of $G$ is completely reducible.

Let $W\subseteq V$ be $G$-stable and choose any linear projection
\[
p_0:V\to W.
\]
Average it over the group:
\[
p=\frac1{|G|}\sum_{g\in G}g\,p_0\,g^{-1}.
\]
The scalar $|G|^{-1}$ exists by hypothesis. The map $p$ is $G$-equivariant, has image $W$, and restricts to the identity on $W$. Hence
\[
V=W\oplus\ker p,
\]
with $\ker p$ also $G$-stable.

Over $\mathbb R$, nothing fails in Maschke's theorem: characteristic $0$ still gives complete reducibility. What changes from the complex theory is the form of irreducibles and Schur's lemma; for an irreducible real representation, the division algebra $\operatorname{End}_G(V)$ can be $\mathbb R$, $\mathbb C$, or $\mathbb H$.

If $\operatorname{char}k=p$ divides $|G|$, semisimplicity can fail. For
\[
G=C_p=\langle g\rangle,
\qquad k=\mathbb F_p,
\]
take
\[
\rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Because $(I+N)^p=I$ in characteristic $p$ when $N^2=0$, this is a representation of $C_p$. The line spanned by $e_1$ is invariant, but it has no invariant complementary line: the only eigenline of $\rho(g)$ is $\langle e_1\rangle$. Thus complete reducibility fails.
:::
