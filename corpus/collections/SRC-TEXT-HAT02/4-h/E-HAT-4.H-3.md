---
schema: qual/card@1
id: E-HAT-4.H-3
kind: problem
title: "Fiber-preserving homotopy equivalences are fiber homotopy equivalences"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.H, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

For fibrations $E_1 \to B$ and $E_2 \to B$, show that a fiber-preserving map $E_1 \to E_2$ that is a homotopy equivalence is in fact a fiber homotopy equivalence.

::: {.solution}
Let
\[
p_1:E_1\to B,
\qquad
p_2:E_2\to B
\]
be fibrations, and let
\[
f:E_1\to E_2,
\qquad p_2f=p_1,
\]
be a homotopy equivalence. We write \(\simeq_B\) for a homotopy through fiber-preserving maps.

Choose an ordinary homotopy inverse
\[
g:E_2\to E_1
\]
with
\[
fg\simeq\operatorname{id}_{E_2},
\qquad
gf\simeq\operatorname{id}_{E_1}.
\]
Since
\[
p_1g=p_2fg\simeq p_2,
\]
the homotopy lifting property for \(p_1\) deforms \(g\) to a map
\[
g':E_2\to E_1
\]
with
\[
p_1g'=p_2.
\]
Thus we may replace \(g\) by \(g'\) and assume from now on that \(g\) itself is fiber-preserving. It remains to improve the two ordinary homotopies to fiber homotopies.

We use the following lemma.

**Lemma.** If \(p:E\to B\) is a fibration and \(u:E\to E\) is fiber-preserving and ordinarily homotopic to \(\operatorname{id}_E\), then \(u\) has a left homotopy inverse over \(B\).

Choose an ordinary homotopy
\[
h_t:u\simeq\operatorname{id}_E.
\]
Since \(ph_0=p\), lift the base homotopy \(ph_t\), starting at \(\operatorname{id}_E\), to a homotopy
\[
k_t:\operatorname{id}_E\simeq k_1
\]
with
\[
p k_t=p h_t.
\]
In particular \(k_1\) is fiber-preserving because \(ph_1=p\).

Now concatenate the homotopies
\[
k_1u\simeq u=h_0\simeq h_1=\operatorname{id}_E
\]
to obtain a homotopy \(J\) from \(k_1u\) to \(\operatorname{id}_E\). Its projection \(pJ\) is a loop of maps \(E\to B\) based at \(p\). The square of homotopies obtained from \(h_t\) and the lifted homotopy \(k_t\) gives a homotopy of \(pJ\), rel endpoints, to the constant homotopy at \(p\). Lift this two-parameter homotopy using the fibration property of \(p\). Reading along the opposite boundary gives a homotopy over \(B\)
\[
k_1u\simeq_B\operatorname{id}_E.
\]
This proves the lemma.

Apply the lemma to
\[
u=gf:E_1\to E_1.
\]
Then there is a fiber-preserving \(a:E_1\to E_1\) with
\[
a\,gf\simeq_B\operatorname{id}_{E_1}.
\]
Set
\[
\ell=ag:E_2\to E_1.
\]
Then
\[
\ell f\simeq_B\operatorname{id}_{E_1}.
\tag{1}
\]
Since \(a\simeq\operatorname{id}_{E_1}\) ordinarily and \(g\) is an ordinary homotopy equivalence, \(\ell\) is also an ordinary homotopy equivalence. Repeating the preceding construction with \(\ell\) in place of \(f\), we obtain a fiber-preserving map
\[
m:E_1\to E_2
\]
with
\[
m\ell\simeq_B\operatorname{id}_{E_2}.
\tag{2}
\]
Compose (1) on the left with \(m\). Using (2),
\[
m\simeq_Bm\ell f\simeq_B f.
\]
Therefore
\[
f\ell\simeq_Bm\ell\simeq_B\operatorname{id}_{E_2}.
\]
Together with (1), this shows that \(\ell\) is a fiber-preserving homotopy inverse to \(f\). Hence
\[
\boxed{f\text{ is a fiber homotopy equivalence}.}
\]
:::
