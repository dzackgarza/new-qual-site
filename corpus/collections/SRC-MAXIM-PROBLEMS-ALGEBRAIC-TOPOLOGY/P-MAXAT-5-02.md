---
schema: qual/card@1
id: P-MAXAT-5-02
kind: problem
title: Maxim algebraic topology 5.2
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 5, problem 2 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that any vector bundle over a simply-connected base space is orientable.
:::

::: {.solution}

Let
$$
\xi:E\to X
$$
be a real rank-$r$ vector bundle over a path-connected simply connected base $X$.

::: pf

::: {.pf-step #s1-1}

A real vector bundle is orientable if and only if its first Stiefel--Whitney class vanishes:
$$
w_1(\xi)=0\in H^1(X;\ZZ/2).
$$


::: pf-proof

The transition functions of a rank-$r$ real bundle take values in $GL_r(\RR)$. Their determinant signs define a Cech $1$-cocycle with values in $\{\pm1\}\cong\ZZ/2$; its cohomology class is $w_1(\xi)$. This cocycle is a coboundary exactly when local orientations can be changed so that every transition function has positive determinant, i.e. exactly when the structure group reduces to $GL_r^+(\RR)$ and the bundle is orientable.

:::

:::

::: {.pf-step #s1-2}

Since $X$ is simply connected,
$$
H_1(X;\ZZ)=0.
$$


::: pf-proof

The Hurewicz theorem in degree one identifies
$$
H_1(X;\ZZ)\cong\pi_1(X)^{\mathrm{ab}}.
$$
Since $\pi_1(X)=0$, its abelianization is zero.

:::

:::

::: {.pf-step #s1-3}

The universal coefficient theorem gives
$$
H^1(X;\ZZ/2)
\cong\operatorname{Hom}(H_1(X;\ZZ),\ZZ/2).
$$


::: pf-proof

The degree-one universal coefficient sequence is
$$
0\to\operatorname{Ext}^1(H_0(X;\ZZ),\ZZ/2)
\to H^1(X;\ZZ/2)
\to\operatorname{Hom}(H_1(X;\ZZ),\ZZ/2)
\to0.
$$
Path connectedness gives $H_0(X;\ZZ)\cong\ZZ$, and
$$
\operatorname{Ext}^1(\ZZ,\ZZ/2)=0.
$$
Hence the right map is an isomorphism.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
H^1(X;\ZZ/2)=0.
$$


::: pf-proof

Substitute $H_1(X;\ZZ)=0$ from step [](#s1-2){.pf-ref} into the isomorphism of step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

In particular,
$$
w_1(\xi)=0.
$$


::: pf-proof

The first Stiefel--Whitney class lies in the zero group from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence $\xi$ is orientable.


::: pf-proof

Apply the criterion in step [](#s1-1){.pf-ref} to the vanishing established in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

Equivalently, parallel transport of a chosen orientation of one fiber is path-independent.


::: pf-proof

The orientation local system of $\xi$ has monodromy character
$$
\pi_1(X)\to\{\pm1\}.
$$
Since $\pi_1(X)=0$, this character is trivial. Thus an orientation chosen in one fiber transports consistently to every fiber. This is the local-system form of steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{\text{every real vector bundle over a simply connected base is orientable}.}
$$


::: pf-proof

This is step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
