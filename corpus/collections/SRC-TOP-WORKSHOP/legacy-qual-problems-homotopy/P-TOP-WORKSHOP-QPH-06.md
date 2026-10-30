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
  note: Checked against Problem 6 in assets/attachments/Legacy_packet_-_Homotopy_and_Retractions_extracted.md.
---

::: {.problem}
Prove that $S^{n-1}$ is not a retract of $B^n$.
:::

::: {.solution}

Assume $n\ge1$.

::: pf

::: {.pf-step #s1-1}

Let
$$
i:S^{n-1}\hookrightarrow B^n
$$
be the inclusion. If a retraction
$$
r:B^n\to S^{n-1}
$$
existed, then
$$
r\circ i
=
\operatorname{id}_{S^{n-1}}.
$$


::: pf-proof

By definition, a retraction onto $S^{n-1}$ restricts to the identity on $S^{n-1}$.

:::

:::

::: {.pf-step #s1-2}

The reduced homology groups satisfy
$$
\widetilde H_{n-1}(S^{n-1};\ZZ)
\cong
\ZZ
$$
and
$$
\widetilde H_{n-1}(B^n;\ZZ)
=
0.
$$


::: pf-proof

The sphere has reduced homology
$$
\widetilde H_k(S^{n-1};\ZZ)
\cong
\begin{cases}
\ZZ,&k=n-1,\\
0,&k\ne n-1.
\end{cases}
$$
The ball $B^n$ is contractible, so all of its reduced homology groups vanish.

:::

:::

::: {.pf-step #s1-3}

Applying reduced homology in degree $n-1$ to step [](#s1-1){.pf-ref} gives
$$
r_*\circ i_*
=
\operatorname{id}_{\widetilde H_{n-1}(S^{n-1};\ZZ)}.
$$


::: pf-proof

Reduced homology is functorial, so
$$
(r\circ i)_*
=
r_*\circ i_*.
$$
By step [](#s1-1){.pf-ref},
$$
r\circ i
=
\operatorname{id}_{S^{n-1}},
$$
hence
$$
r_*\circ i_*
=
(\operatorname{id}_{S^{n-1}})_*
=
\operatorname{id}.
$$

:::

:::

::: {.pf-step #s1-4}

The identity in step [](#s1-3){.pf-ref} is impossible.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\widetilde H_{n-1}(B^n;\ZZ)=0.
$$
Therefore
$$
i_*:
\widetilde H_{n-1}(S^{n-1};\ZZ)
\longrightarrow
\widetilde H_{n-1}(B^n;\ZZ)
$$
is the zero homomorphism. Hence
$$
r_*\circ i_*=0.
$$

But step [](#s1-2){.pf-ref} also gives
$$
\widetilde H_{n-1}(S^{n-1};\ZZ)
\cong
\ZZ\ne0,
$$
so its identity homomorphism is nonzero. This contradicts step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
S^{n-1}\text{ is not a retract of }B^n.
}
$$


::: pf-proof

The assumption that a retraction exists leads to the contradiction in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the desired conclusion.

:::

:::

:::
