---
schema: qual/card@1
id: P-MAXAT-6-02
kind: problem
title: Maxim algebraic topology 6.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that a manifold M is orientable if and only if its first Stiefel-Whitney class vanishes.
:::

::: {.solution}

Let $M$ be a smooth $n$-manifold. By definition,
$$
w_1(M)=w_1(TM)\in H^1(M;\ZZ/2).
$$
It is enough to prove the corresponding statement for the tangent bundle.

::: pf

::: {.pf-step #s1-1}

Choose local frames of $TM$ on a trivializing cover $\{U_i\}$, with transition functions
$$
g_{ij}:U_i\cap U_j\to GL_n(\RR).
$$
Their determinant signs
$$
\epsilon_{ij}=\operatorname{sgn}(\det g_{ij})\in\{\pm1\}\cong\ZZ/2
$$
form a Cech $1$-cocycle.


::: pf-proof

On triple overlaps the transition functions satisfy
$$
g_{ij}g_{jk}=g_{ik}.
$$
Taking determinant signs gives
$$
\epsilon_{ij}\epsilon_{jk}=\epsilon_{ik},
$$
which is precisely the Cech cocycle condition for the constant coefficient group $\{\pm1\}$.

:::

:::

::: {.pf-step #s1-2}

The cohomology class of this cocycle is
$$
w_1(TM).
$$


::: pf-proof

The determinant-sign homomorphism
$$
GL_n(\RR)\to\{\pm1\}
$$
defines the orientation double cover of the frame bundle. The characteristic class classifying this double cover is, by definition, the first Stiefel--Whitney class. In transition-function terms it is represented exactly by the sign cocycle $\{\epsilon_{ij}\}$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

If $M$ is orientable, then
$$
w_1(M)=0.
$$


::: pf-proof

An orientation is equivalent to choosing local frames so that every change-of-frame matrix has positive determinant. For such oriented frames,
$$
\epsilon_{ij}=+1
$$
on every overlap. Thus the cocycle representing $w_1(TM)$ is trivial, so its cohomology class vanishes.

:::

:::

::: {.pf-step #s1-4}

Conversely, suppose
$$
w_1(M)=0.
$$
Then the sign cocycle is a coboundary: there exist locally constant signs
$$
\delta_i:U_i\to\{\pm1\}
$$
such that
$$
\epsilon_{ij}=\delta_i\delta_j^{-1}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the Cech class of $\{\epsilon_{ij}\}$ is $w_1(TM)$. Vanishing of this class means exactly that the cocycle is a Cech coboundary, which has the displayed form.

:::

:::

::: {.pf-step #s1-5}

Reverse the first vector of the local frame on $U_i$ whenever $\delta_i=-1$. The new transition functions all have positive determinant.


::: pf-proof

Changing one vector in a frame multiplies its orientation sign by $-1$. Thus modifying the $i$th local frame by the sign $\delta_i$ changes the determinant sign on $U_i\cap U_j$ to
$$
\delta_i^{-1}\epsilon_{ij}\delta_j.
$$
Using step [](#s1-4){.pf-ref} gives
$$
\delta_i^{-1}(\delta_i\delta_j^{-1})\delta_j=1.
$$
Hence every modified transition function lies in $GL_n^+(\RR)$.

:::

:::

::: {.pf-step #s1-6}

These modified local frames define an orientation of $M$.


::: pf-proof

On overlaps, step [](#s1-5){.pf-ref} shows that the two local frames differ by an orientation-preserving matrix. Therefore their induced local orientations agree and glue to a global orientation.

:::

:::

::: pf-step

Equivalently, $w_1(M)$ is the monodromy character of the orientation local system:
$$
\pi_1(M)\to\{\pm1\}.
$$


::: pf-proof

Transporting a local orientation around a loop either preserves or reverses it, producing a homomorphism to $\{\pm1\}$. Under
$$
H^1(M;\ZZ/2)\cong\operatorname{Hom}(\pi_1(M),\ZZ/2)
$$
on each path component, this homomorphism represents the same determinant-sign class of step [](#s1-2){.pf-ref}. Its vanishing says precisely that the orientation local system is trivial.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{M\text{ is orientable}\iff w_1(M)=0.}
$$


::: pf-proof

The forward implication is step [](#s1-3){.pf-ref}; the reverse implication is steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the desired equivalence.

:::

:::

:::
