---
schema: qual/card@1
id: P-MAXAT-5-04
kind: problem
title: Maxim algebraic topology 5.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 5, problem 4 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Construct an orientable sphere bundle with zero Euler class, but no section.
:::

::: {.solution}

Take an oriented rank-$3$ real vector bundle over $S^4$ representing the nonzero element of
$$
\pi_3(SO(3))\cong\ZZ,
$$
and let its unit-sphere bundle be
$$
S^2\longrightarrow S(\xi)\longrightarrow S^4.
$$

::: pf

::: {.pf-step #s1-1}

Oriented rank-$3$ vector bundles over $S^4$ are classified by
$$
\pi_3(SO(3))\cong\ZZ.
$$


::: pf-proof

Write
$$
S^4=D^4_+\cup_{S^3}D^4_-.
$$
An oriented rank-$3$ bundle is trivial over each hemisphere and is determined by an orientation-preserving clutching map
$$
g:S^3\to SO(3).
$$
Changing trivializations changes $g$ by homotopy, so isomorphism classes are $[S^3,SO(3)]=\pi_3(SO(3))$. The universal double cover $S^3\to SO(3)$ induces an isomorphism on $\pi_3$, hence this group is $\ZZ$.

:::

:::

::: {.pf-step #s1-2}

Choose $\xi$ corresponding to a generator
$$
[g]\ne0\in\pi_3(SO(3)).
$$
Then $\xi$ is oriented and nontrivial.


::: pf-proof

Its structure group is $SO(3)$ by construction, so it is oriented. Under the clutching classification of step [](#s1-1){.pf-ref}, the trivial bundle corresponds to the null-homotopic clutching map. Since $[g]\ne0$, $\xi$ is not trivial.

:::

:::

::: {.pf-step #s1-3}

The Euler class of $\xi$ vanishes:
$$
e(\xi)=0.
$$


::: pf-proof

For an oriented rank-$3$ bundle,
$$
e(\xi)\in H^3(S^4;\ZZ).
$$
But
$$
H^3(S^4;\ZZ)=0,
$$
so the Euler class must vanish.

:::

:::

::: pf-step

A section of the sphere bundle $S(\xi)\to S^4$ is equivalent to a nowhere-zero section of $\xi$.


::: pf-proof

The sphere bundle consists of the unit vectors in the fibers of $\xi$. A section of $S(\xi)$ is therefore already a nowhere-zero section of $\xi$. Conversely, any nowhere-zero section of $\xi$ can be normalized with a bundle metric to give a unit section.

:::

:::

::: {.pf-step #s1-5}

If $S(\xi)$ had a section, then
$$
\xi\cong\varepsilon^1\oplus\eta
$$
for an oriented rank-$2$ bundle $\eta$ over $S^4$.


::: pf-proof

A nowhere-zero section spans a trivial line subbundle. Taking its orthogonal complement gives a rank-$2$ bundle $\eta$. The orientations of $\xi$ and the trivial line induce an orientation on $\eta$.

:::

:::

::: {.pf-step #s1-6}

Every oriented rank-$2$ bundle over $S^4$ is trivial.


::: pf-proof

Oriented rank-$2$ bundles are classified by
$$
[S^4,BSO(2)]
\cong H^2(S^4;\ZZ),
$$
since $BSO(2)=BS^1\simeq\CP^{\infty}=K(\ZZ,2)$. But $H^2(S^4;\ZZ)=0$. Equivalently, their clutching group is
$$
\pi_3(SO(2))=\pi_3(S^1)=0.
$$
Thus $\eta\cong\varepsilon^2$.

:::

:::

::: {.pf-step #s1-7}

Hence a section would force $\xi$ to be trivial, contradicting step [](#s1-2){.pf-ref}.


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref},
$$
\xi\cong\varepsilon^1\oplus\varepsilon^2
\cong\varepsilon^3.
$$
This contradicts the nontrivial clutching class chosen in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore the unit-sphere bundle
$$
\boxed{S^2\to S(\xi)\to S^4}
$$
is orientable, has zero Euler class, and has no section.


::: pf-proof

The bundle is oriented because its structure group is $SO(3)$; step [](#s1-3){.pf-ref} gives zero Euler class; and step [](#s1-7){.pf-ref} proves that no section exists.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} supplies the requested example with all three properties verified.

:::

:::

:::
