---
schema: qual/card@1
id: P-TOP-WORKSHOP-QPH-06
kind: problem
title: The boundary sphere is not a retract of the ball
classification:
  areas: [topology]
  topics: [Retractions, Homology]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in assets/attachments/QualProblemsHomotopy_extracted.md.
---

::: {.problem}
Prove that $S^{n-1}$ is not a retract of $B^n$.
:::

::: {.solution}
Assume $n\ge1$.

<1>1. Let
\[
i:S^{n-1}\hookrightarrow B^n
\]
be the inclusion. If a retraction
\[
r:B^n\to S^{n-1}
\]
existed, then
\[
r\circ i
=
\operatorname{id}_{S^{n-1}}.
\]

::: {.proof}
By definition, a retraction onto $S^{n-1}$ restricts to the identity on $S^{n-1}$.
:::

<1>2. The reduced homology groups satisfy
\[
\widetilde H_{n-1}(S^{n-1};\mathbb Z)
\cong
\mathbb Z
\]
and
\[
\widetilde H_{n-1}(B^n;\mathbb Z)
=
0.
\]

::: {.proof}
The sphere has reduced homology
\[
\widetilde H_k(S^{n-1};\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=n-1,\\
0,&k\ne n-1.
\end{cases}
\]
The ball $B^n$ is contractible, so all of its reduced homology groups vanish.
:::

<1>3. Applying reduced homology in degree $n-1$ to step <1>1 gives
\[
r_*\circ i_*
=
\operatorname{id}_{\widetilde H_{n-1}(S^{n-1};\mathbb Z)}.
\]

::: {.proof}
Reduced homology is functorial, so
\[
(r\circ i)_*
=
r_*\circ i_*.
\]
By step <1>1,
\[
r\circ i
=
\operatorname{id}_{S^{n-1}},
\]
hence
\[
r_*\circ i_*
=
(\operatorname{id}_{S^{n-1}})_*
=
\operatorname{id}.
\]
:::

<1>4. The identity in step <1>3 is impossible.

::: {.proof}
By step <1>2,
\[
\widetilde H_{n-1}(B^n;\mathbb Z)=0.
\]
Therefore
\[
i_*:
\widetilde H_{n-1}(S^{n-1};\mathbb Z)
\longrightarrow
\widetilde H_{n-1}(B^n;\mathbb Z)
\]
is the zero homomorphism. Hence
\[
r_*\circ i_*=0.
\]

But step <1>2 also gives
\[
\widetilde H_{n-1}(S^{n-1};\mathbb Z)
\cong
\mathbb Z\ne0,
\]
so its identity homomorphism is nonzero. This contradicts step <1>3.
:::

<1>5. Therefore
\[
\boxed{
S^{n-1}\text{ is not a retract of }B^n.
}
\]

::: {.proof}
The assumption that a retraction exists leads to the contradiction in step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the desired conclusion.
:::
:::
