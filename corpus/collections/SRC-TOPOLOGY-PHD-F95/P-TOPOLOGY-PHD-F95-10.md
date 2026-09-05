---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-10
kind: problem
title: $\mathbb R^2$ does not retract onto $S^1$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section II, problem 5 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used functoriality of the based fundamental group: a retraction would split
    the inclusion of S^1 into the contractible plane, forcing the identity on
    pi_1(S^1) to factor through the trivial group pi_1(R^2).
---

::: {.problem}
Prove that $\mathbb R^2$ cannot be retracted to $S^1$.
:::

::: {.solution}
Fix a basepoint $x_0\in S^1\subset\mathbb R^2$, and let
\[
i:S^1\hookrightarrow\mathbb R^2
\]
denote inclusion.

<1>1. If a retraction
\[
r:\mathbb R^2\longrightarrow S^1
\]
existed, then
\[
r\circ i=\id_{S^1}.
\]
::: {.proof}
By definition, a retraction onto the subspace $S^1$ restricts to the identity on $S^1$.
Thus for every $z\in S^1$,
\[
(r\circ i)(z)=r(z)=z.
\]
Since $r(x_0)=x_0$, both $i$ and $r$ are based maps at $x_0$.
:::

<1>2. Functoriality would therefore give
\[
r_*\circ i_*=\id_{\pi_1(S^1,x_0)}.
\]
::: {.proof}
Applying the fundamental-group functor to the identity in <1>1 gives
\[
r_*\circ i_*
=(r\circ i)_*
=(\id_{S^1})_*
=\id_{\pi_1(S^1,x_0)}.
\]
:::

<1>3. On the other hand, the homomorphism
\[
i_*:\pi_1(S^1,x_0)\longrightarrow\pi_1(\mathbb R^2,x_0)
\]
is the zero homomorphism.
::: {.proof}
The plane is contractible, hence simply connected, so
\[
\pi_1(\mathbb R^2,x_0)=0.
\]
Therefore every homomorphism into this group, in particular $i_*$, is zero.
:::

<1>4. This contradicts <1>2, so no retraction $\mathbb R^2\to S^1$ exists.
::: {.proof}
By <1>3,
\[
r_*\circ i_*=0.
\]
But <1>2 says the same composite is the identity on
\[
\pi_1(S^1,x_0)\cong\mathbb Z,
\]
which is nontrivial.
Hence the assumed retraction cannot exist.
:::
:::
