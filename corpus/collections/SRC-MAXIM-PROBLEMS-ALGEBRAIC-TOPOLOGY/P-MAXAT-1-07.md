---
schema: qual/card@1
id: P-MAXAT-1-07
kind: problem
title: Maxim algebraic topology 1.7
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 7 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
True or False: Any orientable manifold is a 2-fold covering of a nonorientable manifold.
:::

::: {.solution}

The statement is false.

::: pf

::: {.pf-step #s1-1}

Take
\[
M=S^3.
\]
Then $M$ is an orientable manifold.


::: pf-proof

The sphere $S^3$ is the boundary of the oriented $4$-ball and carries its standard orientation.

:::

:::

::: {.pf-step #s1-2}

Suppose, for contradiction, that there were a connected nonorientable manifold $N$ and a two-sheeted covering
\[
p:S^3\to N.
\]


::: pf-proof

This is the assertion of the problem specialized to the orientable manifold from step [](#s1-1){.pf-ref}. The image of connected $S^3$ is connected, so the relevant base component is connected.

:::

:::

::: pf-step

Any connected covering with simply connected total space is the universal covering.


::: pf-proof

The sphere $S^3$ is simply connected. A connected simply connected covering space satisfies the defining lifting property of the universal cover, and universal covers are unique up to covering isomorphism.

:::

:::

::: {.pf-step #s1-4}

Hence
\[
\pi_1(N)\cong\ZZ/2\ZZ.
\]


::: pf-proof

For a universal covering $\widetilde N\to N$, the deck transformation group is isomorphic to $\pi_1(N)$. Since the covering in step [](#s1-2){.pf-ref} has exactly two sheets, its deck group has order two. Thus $\pi_1(N)$ has order two.

:::

:::

::: {.pf-step #s1-5}

The nontrivial deck transformation $\tau:S^3\to S^3$ is a free involution.


::: pf-proof

The deck group has order two by step [](#s1-4){.pf-ref}. Its nonidentity element therefore satisfies $\tau^2=1$. A nonidentity deck transformation has no fixed point, so $\tau$ is free.

:::

:::

::: {.pf-step #s1-6}

If $N$ were nonorientable, then $\tau$ would reverse the orientation of $S^3$.


::: pf-proof

The orientation double cover of a connected nonorientable manifold is characterized by the kernel of its orientation character $\pi_1(N)\to\{\pm1\}$. Since $\pi_1(N)$ has order two by step [](#s1-4){.pf-ref}, this kernel is trivial, so the universal two-fold cover $S^3\to N$ is the orientation cover. Its nontrivial deck transformation must therefore interchange the two local orientations, i.e. reverse orientation on $S^3$.

:::

:::

::: {.pf-step #s1-7}

Every orientation-reversing self-map of $S^3$ has a fixed point.


::: pf-proof

If $f:S^3\to S^3$ reverses orientation, then $\deg f=-1$. Its Lefschetz number is
\[
L(f)=\operatorname{tr}(f_*|H_0)-\operatorname{tr}(f_*|H_3)
=1-(-1)=2\ne0.
\]
By the Lefschetz fixed-point theorem, $f$ has a fixed point.

:::

:::

::: {.pf-step #s1-8}

This contradicts freeness of the deck transformation $\tau$.


::: pf-proof

Step [](#s1-6){.pf-ref} says $\tau$ is orientation-reversing, so step [](#s1-7){.pf-ref} gives a fixed point. Step [](#s1-5){.pf-ref} says $\tau$ is free. These conclusions are incompatible.

:::

:::

::: {.pf-step #s1-9}

Hence $S^3$ cannot be a two-fold cover of a nonorientable manifold.


::: pf-proof

This is the contradiction obtained in step [](#s1-8){.pf-ref} from the assumption in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore the proposed statement is
\[
\boxed{\text{False}.}
\]


::: pf-proof

The orientable manifold $S^3$ supplied in step [](#s1-9){.pf-ref} cannot be a two-fold covering of any nonorientable manifold.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} answers the true-or-false question with a proved counterexample.

:::

:::

:::
