---
schema: qual/card@1
id: E-AMD-DLD6LYAM
kind: problem
title: Groups of order $12$ with a normal subgroup of order $4$ are isomorphic to
  $A_4$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Normal Subgroups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $|G| = 12$ and $G$ is a non-abelian group with a normal subgroup of order $4$ (or equivalently, $n_3 = 4$), then $G \cong A_4$.
:::

::: {.solution}
Let \(V\trianglelefteq G\) have order \(4\), and let \(P\in\operatorname{Syl}_3(G)\). Then \(|P|=3\), \(V\cap P=1\), and
\[
|VP|=\frac{|V||P|}{|V\cap P|}=12=|G|.
\]
Hence
\[
G\cong V\rtimes P.
\]

There are two possibilities for \(V\): \(C_4\) and \(V_4\).

If \(V\cong C_4\), then
\[
\operatorname{Aut}(V)\cong C_2.
\]
Every homomorphism \(P\cong C_3\to C_2\) is trivial, so the semidirect product is direct:
\[
G\cong C_4\times C_3\cong C_{12},
\]
contrary to the hypothesis that \(G\) is nonabelian. Thus \(V\cong V_4\).

Now
\[
\operatorname{Aut}(V_4)\cong S_3.
\]
The conjugation action \(P\to S_3\) cannot be trivial, again because that would make \(G\cong V_4\times C_3\) abelian. Hence its image is the unique subgroup of order \(3\), acting cyclically on the three nonidentity elements of \(V_4\). Up to automorphisms of \(V_4\) and \(C_3\), this gives a unique nontrivial semidirect product
\[
V_4\rtimes C_3.
\]

In \(A_4\), the normal Klein four subgroup
\[
\{1,(12)(34),(13)(24),(14)(23)\}
\]
is acted on cyclically by conjugation with a \(3\)-cycle. Therefore
\[
\boxed{G\cong V_4\rtimes C_3\cong A_4.}
\]
:::
