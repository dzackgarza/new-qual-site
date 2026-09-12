---
schema: qual/card@1
id: E-HAT-4.F-1
kind: problem
title: "Direct limit axiom vs. wedge sum axiom"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Assuming the first two axioms for a homology theory on the CW category, show that the direct limit axiom implies the wedge sum axiom.
Show that the converse also holds for countable CW complexes.

::: {.solution}
Let \(\widetilde h_*\) satisfy the homotopy and exactness axioms. Recall first that these two axioms already imply the wedge axiom for finite wedge sums.

Assume the direct-limit axiom. Let
\[
X=\bigvee_{\alpha}X_\alpha.
\]
Every finite subcomplex \(K\subset X\) is contained in a finite wedge
\[
K_{\alpha_1}\vee\cdots\vee K_{\alpha_r}
\]
with each \(K_{\alpha_i}\subset X_{\alpha_i}\) finite. Hence, using the finite-wedge result,
\[
\widetilde h_n(K)
\cong\bigoplus_{i=1}^r\widetilde h_n(K_{\alpha_i}).
\]
Taking the filtered colimit over finite subcomplexes and using the direct-limit axiom in each summand gives
\[
\widetilde h_n\!\left(\bigvee_\alpha X_\alpha\right)
\cong\bigoplus_\alpha \widetilde h_n(X_\alpha).
\]
Thus the wedge axiom follows.

Conversely, assume the wedge axiom and let \(X\) be a countable CW complex. Choose an exhaustion by finite subcomplexes
\[
X_1\subset X_2\subset\cdots,
\qquad X=\bigcup_iX_i.
\]
Let \(T\) be the mapping telescope of this sequence. There is a standard cofibration
\[
\bigvee_{i\ge1}X_i
\xrightarrow{\,1-s\,}
\bigvee_{i\ge1}X_i
\longrightarrow T,
\tag{1}
\]
where on the \(i\)-th summand the shift \(s\) is the inclusion \(X_i\to X_{i+1}\) followed by inclusion into the \((i+1)\)-st wedge summand. The telescope deformation retracts onto \(X\) up to homotopy, so \(\widetilde h_*(T)\cong\widetilde h_*(X)\).

By the wedge axiom, applying \(\widetilde h_n\) to (1) yields
\[
\bigoplus_i\widetilde h_n(X_i)
\xrightarrow{\,1-s_*\,}
\bigoplus_i\widetilde h_n(X_i)
\longrightarrow\widetilde h_n(T)
\longrightarrow
\bigoplus_i\widetilde h_{n-1}(X_i).
\]
The map \(1-s_*\) on a direct sum is injective: if a finite-support element lies in its kernel, inspect its first nonzero coordinate and proceed inductively. Therefore exactness gives
\[
\widetilde h_n(T)
\cong\operatorname{coker}(1-s_*)
\cong\varinjlim_i\widetilde h_n(X_i).
\]
Hence
\[
\boxed{\widetilde h_n(X)\cong\varinjlim_i\widetilde h_n(X_i),}
\]
which is the direct-limit axiom for countable CW complexes.
:::
