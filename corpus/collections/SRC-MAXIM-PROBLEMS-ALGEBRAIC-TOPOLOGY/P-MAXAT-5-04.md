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
\[
\pi_3(SO(3))\cong\mathbb Z,
\]
and let its unit-sphere bundle be
\[
S^2\longrightarrow S(\xi)\longrightarrow S^4.
\]

<1>1. Oriented rank-$3$ vector bundles over $S^4$ are classified by
\[
\pi_3(SO(3))\cong\mathbb Z.
\]

::: {.proof}
Write
\[
S^4=D^4_+\cup_{S^3}D^4_-.
\]
An oriented rank-$3$ bundle is trivial over each hemisphere and is determined by an orientation-preserving clutching map
\[
g:S^3\to SO(3).
\]
Changing trivializations changes $g$ by homotopy, so isomorphism classes are $[S^3,SO(3)]=\pi_3(SO(3))$. The universal double cover $S^3\to SO(3)$ induces an isomorphism on $\pi_3$, hence this group is $\mathbb Z$.
:::

<1>2. Choose $\xi$ corresponding to a generator
\[
[g]\ne0\in\pi_3(SO(3)).
\]
Then $\xi$ is oriented and nontrivial.

::: {.proof}
Its structure group is $SO(3)$ by construction, so it is oriented. Under the clutching classification of step <1>1, the trivial bundle corresponds to the null-homotopic clutching map. Since $[g]\ne0$, $\xi$ is not trivial.
:::

<1>3. The Euler class of $\xi$ vanishes:
\[
e(\xi)=0.
\]

::: {.proof}
For an oriented rank-$3$ bundle,
\[
e(\xi)\in H^3(S^4;\mathbb Z).
\]
But
\[
H^3(S^4;\mathbb Z)=0,
\]
so the Euler class must vanish.
:::

<1>4. A section of the sphere bundle $S(\xi)\to S^4$ is equivalent to a nowhere-zero section of $\xi$.

::: {.proof}
The sphere bundle consists of the unit vectors in the fibers of $\xi$. A section of $S(\xi)$ is therefore already a nowhere-zero section of $\xi$. Conversely, any nowhere-zero section of $\xi$ can be normalized with a bundle metric to give a unit section.
:::

<1>5. If $S(\xi)$ had a section, then
\[
\xi\cong\varepsilon^1\oplus\eta
\]
for an oriented rank-$2$ bundle $\eta$ over $S^4$.

::: {.proof}
A nowhere-zero section spans a trivial line subbundle. Taking its orthogonal complement gives a rank-$2$ bundle $\eta$. The orientations of $\xi$ and the trivial line induce an orientation on $\eta$.
:::

<1>6. Every oriented rank-$2$ bundle over $S^4$ is trivial.

::: {.proof}
Oriented rank-$2$ bundles are classified by
\[
[S^4,BSO(2)]
\cong H^2(S^4;\mathbb Z),
\]
since $BSO(2)=BS^1\simeq\mathbb{CP}^{\infty}=K(\mathbb Z,2)$. But $H^2(S^4;\mathbb Z)=0$. Equivalently, their clutching group is
\[
\pi_3(SO(2))=\pi_3(S^1)=0.
\]
Thus $\eta\cong\varepsilon^2$.
:::

<1>7. Hence a section would force $\xi$ to be trivial, contradicting step <1>2.

::: {.proof}
By steps <1>5--<1>6,
\[
\xi\cong\varepsilon^1\oplus\varepsilon^2
\cong\varepsilon^3.
\]
This contradicts the nontrivial clutching class chosen in step <1>2.
:::

<1>8. Therefore the unit-sphere bundle
\[
\boxed{S^2\to S(\xi)\to S^4}
\]
is orientable, has zero Euler class, and has no section.

::: {.proof}
The bundle is oriented because its structure group is $SO(3)$; step <1>3 gives zero Euler class; and step <1>7 proves that no section exists.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 supplies the requested example with all three properties verified.
:::
:::
