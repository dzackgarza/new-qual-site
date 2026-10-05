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

<1>1. Take
\[
M=S^3.
\]
Then $M$ is an orientable manifold.

::: {.proof}
The sphere $S^3$ is the boundary of the oriented $4$-ball and carries its standard orientation.
:::

<1>2. Suppose, for contradiction, that there were a connected nonorientable manifold $N$ and a two-sheeted covering
\[
p:S^3\to N.
\]

::: {.proof}
This is the assertion of the problem specialized to the orientable manifold from step <1>1. The image of connected $S^3$ is connected, so the relevant base component is connected.
:::

<1>3. Any connected covering with simply connected total space is the universal covering.

::: {.proof}
The sphere $S^3$ is simply connected. A connected simply connected covering space satisfies the defining lifting property of the universal cover, and universal covers are unique up to covering isomorphism.
:::

<1>4. Hence
\[
\pi_1(N)\cong\mathbb Z/2\mathbb Z.
\]

::: {.proof}
For a universal covering $\widetilde N\to N$, the deck transformation group is isomorphic to $\pi_1(N)$. Since the covering in step <1>2 has exactly two sheets, its deck group has order two. Thus $\pi_1(N)$ has order two.
:::

<1>5. The nontrivial deck transformation $\tau:S^3\to S^3$ is a free involution.

::: {.proof}
The deck group has order two by step <1>4. Its nonidentity element therefore satisfies $\tau^2=1$. A nonidentity deck transformation has no fixed point, so $\tau$ is free.
:::

<1>6. If $N$ were nonorientable, then $\tau$ would reverse the orientation of $S^3$.

::: {.proof}
The orientation double cover of a connected nonorientable manifold is characterized by the kernel of its orientation character $\pi_1(N)\to\{\pm1\}$. Since $\pi_1(N)$ has order two by step <1>4, this kernel is trivial, so the universal two-fold cover $S^3\to N$ is the orientation cover. Its nontrivial deck transformation must therefore interchange the two local orientations, i.e. reverse orientation on $S^3$.
:::

<1>7. Every orientation-reversing self-map of $S^3$ has a fixed point.

::: {.proof}
If $f:S^3\to S^3$ reverses orientation, then $\deg f=-1$. Its Lefschetz number is
\[
L(f)=\operatorname{tr}(f_*|H_0)-\operatorname{tr}(f_*|H_3)
=1-(-1)=2\ne0.
\]
By the Lefschetz fixed-point theorem, $f$ has a fixed point.
:::

<1>8. This contradicts freeness of the deck transformation $\tau$.

::: {.proof}
Step <1>6 says $\tau$ is orientation-reversing, so step <1>7 gives a fixed point. Step <1>5 says $\tau$ is free. These conclusions are incompatible.
:::

<1>9. Hence $S^3$ cannot be a two-fold cover of a nonorientable manifold.

::: {.proof}
This is the contradiction obtained in step <1>8 from the assumption in step <1>2.
:::

<1>10. Therefore the proposed statement is
\[
\boxed{\text{False}.}
\]

::: {.proof}
The orientable manifold $S^3$ supplied in step <1>9 cannot be a two-fold covering of any nonorientable manifold.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 answers the true-or-false question with a proved counterexample.
:::
:::
