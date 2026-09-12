---
schema: qual/card@1
id: E-HAT-4.2-33
kind: problem
title: "Homotopy groups if all Hopf-like bundles existed"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 33; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that if there were fiber bundles $S^{n-1} \to S^{2n-1} \to S^n$ for all $n$, then the groups $\pi_i(S^n)$ would be finitely generated free abelian groups computable by induction, and nonzero for $i \geq n \geq 2$.

::: {.solution}
Assume bundles
\[
S^{n-1}\longrightarrow S^{2n-1}\longrightarrow S^n
\]
exist for every \(n\ge2\). The fiber inclusion is nullhomotopic since
\[
\pi_{n-1}(S^{2n-1})=0.
\]
Exercise 31 therefore gives, for all \(i\),
\[
\pi_i(S^n)\cong
\pi_i(S^{2n-1})\oplus\pi_{i-1}(S^{n-1}). \tag{*}
\]

For fixed \(i\), repeated use of (*) terminates: following the first summand increases the sphere dimension from \(n\) to \(2n-1\), so after finitely many such steps the sphere dimension exceeds \(i\) and that summand is zero; following the second summand decreases both indices by one. Hence every \(\pi_i(S^n)\) is obtained by finitely many direct sums from groups \(\pi_j(S^j)\cong\mathbb Z\) and zero groups. Consequently all groups are finitely generated free abelian, and (*) provides an effective recursive computation.

It remains to prove nonvanishing for \(i\ge n\ge2\). First consider \(S^2\). The \(n=2\) bundle gives
\[
\pi_i(S^2)\cong\pi_i(S^3)
\qquad(i>2).
\]
For \(n=3\), (*) gives
\[
\pi_i(S^3)\cong\pi_i(S^5)\oplus\pi_{i-1}(S^2).
\]
Since \(\pi_2(S^2)\cong\mathbb Z\), induction on \(i\) shows
\[
\pi_i(S^2)\ne0\qquad(i\ge2).
\]
Now for arbitrary \(i\ge n\), repeatedly take the second direct summand in (*) to obtain an injection
\[
\pi_{i-n+2}(S^2)\hookrightarrow\pi_i(S^n).
\]
The source is nonzero by the preceding paragraph. Thus
\[
\boxed{\pi_i(S^n)\text{ would be finitely generated free abelian and nonzero for every }i\ge n\ge2.}
\]
:::
